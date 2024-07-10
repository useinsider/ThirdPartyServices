# ThirdPartyServices
# Pact Contract Testing

Bu proje, entegrasyonların contract testlerini gerçekleştirmek için geliştirildi.

## Kurulum

Gerekli paketleri yüklemek için:

```bash
pip install -r requirements.txt

Consumer testlerini çalıştırmak için:

pre-conditions:
go to directory cd tests
export SHOPIFY_API_KEY='paste_current_key'

python shopifyGetSingleProduct.py
python shopifyContactProfile.py
python shopifyCreateUser.py
python shopifyIdentity.py
python shopifyTriggerEvent.py

Provider testlerini çalıştırmak için:

python verify_provider.py

Global değerler aşağıdaki dizinde tutulur:
 
ThirdPartyServices/global_values.py
