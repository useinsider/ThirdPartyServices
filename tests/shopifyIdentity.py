import atexit
import unittest
from pact import Consumer, Provider
import requests
from global_values import EMAIL, PARTNER, INSIDERID

# Pact konfigürasyonu
pact = Consumer('IdentityConsumer').has_pact_with(Provider('IdentityProvider'), pact_dir='./pacts')
pact.start_service()  # Pact servisini başlatıyoruz
atexit.register(pact.stop_service)  # Servisin durdurulmasını sağlıyoruz

class IdentityGetContract(unittest.TestCase):
    def test_get_identity(self):
        # Beklenen yanıt verisi
        expected_response = INSIDERID

        # Gönderilecek istek verisi
        request_body = {
            "partner": PARTNER,
            "read_only": True,
            "identifiers": {
                "em": EMAIL
            }
        }

        # Pact etkileşimini tanımlıyoruz
        (pact
         .given('User with email exists')
         .upon_receiving('a request to get identity')
         .with_request('post', '/api/identity/v1/get', body=request_body)
         .will_respond_with(200, body=expected_response))

        # Pact servisi çalışırken isteği gönderiyoruz ve yanıtı kontrol ediyoruz
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
