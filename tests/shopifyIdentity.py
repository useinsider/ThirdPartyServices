import atexit
import unittest
from pact import Consumer, Provider
import requests
from global_values import EMAIL, PARTNER, INSIDERID

# Pact configurations
pact = Consumer('IdentityConsumer').has_pact_with(Provider('IdentityProvider'), pact_dir='./pacts')
pact.start_service()  # Pact services starting
atexit.register(pact.stop_service)

class IdentityGetContract(unittest.TestCase):
    def test_get_identity(self):

        expected_response = INSIDERID

        request_body = {
            "partner": PARTNER,
            "read_only": True,
            "identifiers": {
                "em": EMAIL
            }
        }

        # Define the Pact interaction
        (pact
         .given('User with email exists')
         .upon_receiving('a request to get identity')
         .with_request('post', '/api/identity/v1/get', body=request_body)
         .will_respond_with(200, body=expected_response))

        # With the Pact service running, send the request and check the response
        with pact:
            result = requests.post(pact.uri + '/api/identity/v1/get', json=request_body)
            self.assertEqual(result.status_code, 200)
            try:
                response_json = result.json()
            except ValueError:
                response_json = result.text

            self.assertEqual(response_json, expected_response)

if __name__ == '__main__':
    unittest.main()
