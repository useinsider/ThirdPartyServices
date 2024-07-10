import atexit
import unittest
from pact import Consumer, Provider
import requests
from global_values import EMAIL, PARTNER


# Pact configurations
pact = Consumer('UserCreateConsumer').has_pact_with(Provider('UserCreateProvider'), pact_dir='./pacts')
pact.start_service()  # Pact servisini başlatıyoruz
atexit.register(pact.stop_service)  # Servisin durdurulmasını sağlıyoruz

class UserCreateContract(unittest.TestCase):
    def test_user_create(self):

        # Gönderilecek istek verisi
        request_body = {
            "partner": PARTNER,
            "source": "email",
            "lane": 0,
            "users": [
                {
                    "identifiers": {
                        "em": EMAIL
                    },
                    "attributes": {
                        "eo": True,
                        "gdpr": True,
                        "global_unsubscribe": 0
                    }
                }
            ]
        }

        expected_response = {}

        # Define the Pact interaction
        (pact
         .given('User with email exists')
         .upon_receiving('a request to update attributes')
         .with_request('post', '/api/attribute/v1/update', body=request_body)
         .will_respond_with(200, body=expected_response))

        # With the Pact service running, send the request and check the response
        with pact:
            result = requests.post(pact.uri + '/api/attribute/v1/update', json=request_body)
            self.assertEqual(result.status_code, 200)
            self.assertEqual(result.json(), expected_response)

if __name__ == '__main__':
    unittest.main()
