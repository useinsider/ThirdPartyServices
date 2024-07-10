# ThirdPartyServices
# Pact Contract Testing

This project was developed to perform contract testing of integrations.

## Installations

To install the necessary packages:

```bash
pip install -r requirements.txt

To run consumer tests:

pre-conditions:
go to directory cd tests
export SHOPIFY_API_KEY='paste_current_key'

python shopifyGetSingleProduct.py
python shopifyContactProfile.py
python shopifyCreateUser.py
python shopifyIdentity.py
python shopifyTriggerEvent.py

To run provider tests:

python verify_provider.py

Global values are stored in the following directory:
 
ThirdPartyServices/global_values.py
