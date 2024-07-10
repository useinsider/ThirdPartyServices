# ThirdPartyServices
# Pact Contract Testing

Bu proje, tüketici ve sağlayıcı arasında kontrat testleri gerçekleştirmek için kullanılmaktadır.

## Kurulum

Gerekli paketleri yüklemek için:

```bash
pip install -r requirements.txt

Consumer testlerini çalıştırmak için:

python tests/shopifyContactProfile.py
python tests/shopifyCreateUser.py
python tests/shopifyIdentity.py
python tests/shopifyTriggerEvent.py

Provider testlerini çalıştırmak için:

python verify_provider.py

Global değerler aşağıdaki dizinde tutulur:
 
ThirdPartyServices/global_values.py
