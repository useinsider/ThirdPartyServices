import atexit
import unittest
from pact import Consumer, Provider
import requests

import os

# Get API key from environment variable
apikey = os.getenv('SHOPIFY_API_KEY')
if apikey is None:
    raise ValueError("API key (SHOPIFY_API_KEY) must be set as an environment variable.")


# Pact konfigürasyonu
pact = Consumer('ShopifyConsumer').has_pact_with(Provider('ShopifyProvider'), pact_dir='./pacts')
pact.start_service()  # Pact servisini başlatıyoruz
atexit.register(pact.stop_service)  # Servisin durdurulmasını sağlıyoruz

class ShopifyGetRequestContract(unittest.TestCase):
    def test_get_shopify_product(self):
        # Beklenen yanıt verisi
        expected_response = {
                "product": {
                    "id": 7183556673579,
                    "title": "10% OFF on All Shoes",
                    "body_html": "<p>jesus</p>\n<p>jesus</p>\n<p>jesus</p>\n<p>jesus</p>\n<p> </p>",
                    "vendor": "Posh",
                    "product_type": "",
                    "created_at": "2023-12-28T15:04:00+03:00",
                    "handle": "10-off-on-all-shoes",
                    "updated_at": "2024-04-18T23:07:55+03:00",
                    "published_at": "2023-12-28T15:03:58+03:00",
                    "template_suffix": None,
                    "published_scope": "web",
                    "tags": "accessories, arrivals, AW15, bottoms, bounty, collection_195285352492, man, mothermoon, SALE, signature, ss15, visible, Woman",
                    "status": "active",
                    "admin_graphql_api_id": "gid://shopify/Product/7183556673579",
                    "variants": [
                        {
                            "id": 40982094250027,
                            "product_id": 7183556673579,
                            "title": "Default Title",
                            "price": "45.00",
                            "sku": "",
                            "position": 1,
                            "inventory_policy": "deny",
                            "compare_at_price": "50.00",
                            "fulfillment_service": "manual",
                            "inventory_management": None,
                            "option1": "Default Title",
                            "option2": None,
                            "option3": None,
                            "created_at": "2023-12-28T15:04:00+03:00",
                            "updated_at": "2024-03-13T17:38:26+03:00",
                            "taxable": True,
                            "barcode": "",
                            "grams": 0,
                            "weight": 0.0,
                            "weight_unit": "kg",
                            "inventory_item_id": 43080007221291,
                            "inventory_quantity": -6,
                            "old_inventory_quantity": -6,
                            "requires_shipping": False,
                            "admin_graphql_api_id": "gid://shopify/ProductVariant/40982094250027",
                            "image_id": None
                        }
                    ],
                    "options": [
                        {
                            "id": 9210504806443,
                            "product_id": 7183556673579,
                            "name": "Title",
                            "position": 1,
                            "values": [
                                "Default Title"
                            ]
                        }
                    ],
                    "images": [
                        {
                            "id": 32289864613931,
                            "alt": None,
                            "position": 1,
                            "product_id": 7183556673579,
                            "created_at": "2023-12-28T15:04:00+03:00",
                            "updated_at": "2023-12-28T15:04:00+03:00",
                            "admin_graphql_api_id": "gid://shopify/ProductImage/32289864613931",
                            "width": 480,
                            "height": 268,
                            "src": "https://cdn.shopify.com/s/files/1/0573/5710/7243/products/Artboard_59.png?v=1703765040",
                            "variant_ids": []
                        }
                    ],
                    "image": {
                        "id": 32289864613931,
                        "alt": None,
                        "position": 1,
                        "product_id": 7183556673579,
                        "created_at": "2023-12-28T15:04:00+03:00",
                        "updated_at": "2023-12-28T15:04:00+03:00",
                        "admin_graphql_api_id": "gid://shopify/ProductImage/32289864613931",
                        "width": 480,
                        "height": 268,
                        "src": "https://cdn.shopify.com/s/files/1/0573/5710/7243/products/Artboard_59.png?v=1703765040",
                        "variant_ids": []
                    }
                }
        }

        # İstek başlıkları
        headers = {
            "X-Shopify-Access-Token": apikey
        }

        # Pact etkileşimini tanımlıyoruz
        (pact
         .given('Product exists in Shopify store')
         .upon_receiving('a request to get product details')
         .with_request('get', '/admin/products/7183556673579.json', headers=headers)
         .will_respond_with(200, body=expected_response))

        # Pact servisi çalışırken isteği gönderiyoruz ve yanıtı kontrol ediyoruz
        with pact:
            result = requests.get(pact.uri + f'/admin/products/7183556673579.json', headers=headers)
            self.assertEqual(result.json(), expected_response)

if __name__ == '__main__':
    unittest.main()
