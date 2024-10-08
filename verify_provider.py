import unittest
from pact import Verifier
from global_values import BASE_URL, SHOPIFY_BASE_URL


class ProviderVerification(unittest.TestCase):
    def test_verify_create_profile_provider(self):
        verifierCreateProfile = Verifier(provider='UserCreateConsumer', provider_base_url=BASE_URL)
        verifierCreateProfile.verify_pacts('./tests/pacts/usercreateconsumer-usercreateprovider.json')

    def test_verify_contact_profile_provider(self):
        verifierContactProfile = Verifier(provider='ContactProfileConsumer', provider_base_url=BASE_URL)
        verifierContactProfile.verify_pacts('./tests/pacts/contactprofileconsumer-contactprofileprovider.json')

    def test_verify_event_provider(self):
        verifierEvent = Verifier(provider='EventConsumer', provider_base_url=BASE_URL)
        verifierEvent.verify_pacts('./tests/pacts/eventconsumer-eventprovider.json')

    def test_verify_identity_provider(self):
        verifierIdentity = Verifier(provider='IdentityConsumer', provider_base_url=BASE_URL)
        verifierIdentity.verify_pacts('./tests/pacts/identityconsumer-identityprovider.json')

    def test_verify_single_product_provider(self):
        verifierSingleProduct = Verifier(provider='ShopifyProvider', provider_base_url=SHOPIFY_BASE_URL)
        verifierSingleProduct.verify_pacts('./tests/pacts/shopifyconsumer-shopifyprovider.json')


if __name__ == '__main__':
    unittest.main()
