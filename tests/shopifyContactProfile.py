import atexit
import unittest
from pact import Consumer, Provider
import requests
from global_values import EMAIL, PARTNER, INSIDERID

# Pact configurations
pact = Consumer('ContactProfileConsumer').has_pact_with(Provider('ContactProfileProvider'), pact_dir='./pacts')
pact.start_service()  # Pact services starting
atexit.register(pact.stop_service)

class ContactProfileContract(unittest.TestCase):
    def test_contact_profile(self):
        expected_response = {
            "attributes": {
                "actv": True,
                "crea": "2024-07-09T17:14:44Z",
                "em": "erencontract@test.com",
                "eo": True,
                "gdpr": True,
                "global_unsubscribe": 0,
                "idat": "2024-07-09T17:14:49Z",
                "iid": INSIDERID,
                "upta": "2024-07-09T23:11:51Z"
            }
        }

        request_body = {
            "partner": PARTNER,
            "sources": ["last"],
            "identifiers": {
                "em": EMAIL
            },
            "attributes": ["*"],
            "events": {
                "start_date": 1,
                "end_date": 1797643132,
                "wanted": [
                    {
                        "event_name": "confirmation_page_view",
                        "params": ["url", "crea"]
                    }
                ]
            }
        }

        # Define the Pact interaction
        (pact
         .given('User profile exists')
         .upon_receiving('a request to create or get profile')
         .with_request('post', '/api/contact/v1/profile', body=request_body)
         .will_respond_with(200, body=expected_response))

        # With the Pact service running, send the request and check the response
        with pact:
            result = requests.post(pact.uri + '/api/contact/v1/profile', json=request_body)
            self.assertEqual(result.json(), expected_response)


if __name__ == '__main__':
    unittest.main()
