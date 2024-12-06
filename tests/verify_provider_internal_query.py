import unittest
from pact import Verifier
import yaml
import os

# Config dosyasını yükleyelim
current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, "config.yml")  # Config dosyasının yolunu doğru ayarlayın
print("Checking config file path:", os.path.abspath(config_path))

if not os.path.exists(config_path):
    raise FileNotFoundError(f"Config file not found: {config_path}")

with open(config_path, "r") as ymlfile:
    config = yaml.safe_load(ymlfile)

# Config dosyasından gelen ayarlar
# provider_name = config['provider']['name']
# provider_base_url = config['provider']['base_url']
# pact_files_path = config['pact_files']['path']
# broker_url = config.get('pact_broker', {}).get('url', None)
# broker_username = config.get('pact_broker', {}).get('username', None)
# broker_password = config.get('pact_broker', {}).get('password', None)
# consumer_version_tag = config.get('pact_broker', {}).get('consumer_version_tag', None)
# provider_version_tag = config.get('pact_broker', {}).get('provider_version_tag', None)
# enable_ssl_verification = config.get('pact_broker', {}).get('enable_ssl_verification', True)


class ProviderVerification(unittest.TestCase):
    def test_verify_provider(self):
        # Verifier sınıfı ile provider'ı doğrulayın
        verifier = Verifier(provider='InternalQueryProvider', provider_base_url="https://kube-prod-dataforce.useinsider.com/pcd-api")
        verifier.verify_pacts('./pacts/internalqueryconsumer-internalqueryprovider.json')

        # Pact dosyasını doğrulama işlemi
        #success, logs = verifier.verify_pacts('./pacts/internalqueryconsumer-internalqueryprovider.json')

        # Doğrulamanın başarılı olduğunu kontrol edin
        #assert success == 0, f"Verification failed: {logs}"


if __name__ == '__main__':
    unittest.main()
