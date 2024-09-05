import atexit
import unittest
from pact import Consumer, Provider
import requests

# Pact configurations
pact = Consumer('InternalQueryConsumer').has_pact_with(Provider('InternalQueryProvider'), pact_dir='./pacts')
pact.start_service()  # Pact services starting
atexit.register(pact.stop_service)


class InternalQueryContract(unittest.TestCase):
    def test_internal_query(self):
        expected_response = {
            "data": [
                {
                    "image_url": "https://img.lowestfare.com.hk/Content/img/logo.png",
                    "name": "邁爾斯堡薩尼貝爾蓋特威溫德姆拉昆塔套房酒店 迈尔斯堡萨尼贝尔盖特威温德姆拉昆塔套房酒店 La Quinta Inn & Suites by Wyndham Ft. Myers-Sanibel Gateway",
                    "item_id": "1024295",
                    "product_last_modified_by": "CatalogAPI",
                    "url": "https://aws-www-test-3.hutchgo.com.hk/zh-hk/",
                    "in_stock": 1,
                    "price": {
                        "HKD": 0
                    },
                    "product_modified_at": "2024-08-08 02:53:59",
                    "locale": "zh_HK:hotel",
                    "id": "1024295:zh_HK:hotel",
                    "category": [],
                    "discount": {
                        "HKD": 0
                    },
                    "original_price": {
                        "HKD": 0
                    }
                },
                {
                    "image_url": "https://img.lowestfare.com.hk/Content/img/logo.png",
                    "name": "龐當PLT套房酒店 庞当PLT套房酒店 Pendang Suite Hotel PLT",
                    "item_id": "1559382",
                    "product_last_modified_by": "CatalogAPI",
                    "url": "https://aws-www-test-3.hutchgo.com.hk/zh-hk/",
                    "in_stock": 1,
                    "price": {
                        "HKD": 0
                    },
                    "product_modified_at": "2024-08-08 02:53:59",
                    "locale": "zh_HK:hotel",
                    "id": "1559382:zh_HK:hotel",
                    "category": [],
                    "discount": {
                        "HKD": 0
                    },
                    "original_price": {
                        "HKD": 0
                    }
                },
                {
                    "image_url": "https://img.lowestfare.com.hk/Content/img/logo.png",
                    "name": "龍目島蘭科馬塔蘭菲芙酒店 (favehotel Langko Mataram - Lombok) 龙目岛兰科马塔兰菲芙酒店 (favehotel Langko Mataram - Lombok) favehotel Langko Mataram - Lombok",
                    "item_id": "1340653",
                    "product_last_modified_by": "CatalogAPI",
                    "url": "https://aws-www-test-3.hutchgo.com.hk/zh-hk/",
                    "in_stock": 1,
                    "price": {
                        "HKD": 0
                    },
                    "product_modified_at": "2024-08-08 02:53:59",
                    "locale": "zh_HK:hotel",
                    "id": "1340653:zh_HK:hotel",
                    "category": [],
                    "discount": {
                        "HKD": 0
                    },
                    "original_price": {
                        "HKD": 0
                    }
                },
                {
                    "image_url": "https://img.lowestfare.com.hk/Content/img/logo.png",
                    "name": "黑風洞酒店 黑风洞酒店 Batu Caves Hotel",
                    "item_id": "1533940",
                    "product_last_modified_by": "CatalogAPI",
                    "url": "https://aws-www-test-3.hutchgo.com.hk/zh-hk/",
                    "in_stock": 1,
                    "price": {
                        "HKD": 0
                    },
                    "product_modified_at": "2024-08-08 02:53:59",
                    "locale": "zh_HK:hotel",
                    "id": "1533940:zh_HK:hotel",
                    "category": [],
                    "discount": {
                        "HKD": 0
                    },
                    "original_price": {
                        "HKD": 0
                    }
                },
                {
                    "image_url": "https://img.lowestfare.com.hk/Content/img/logo.png",
                    "name": "龍仁中心CO'OP酒店 (Yongin Central CO'OP Hotel) 龙仁中心CO'OP酒店 (Yongin Central CO'OP Hotel) Yongin Central CO'OP Hotel",
                    "item_id": "1289139",
                    "product_last_modified_by": "CatalogAPI",
                    "url": "https://aws-www-test-3.hutchgo.com.hk/zh-hk/",
                    "in_stock": 1,
                    "price": {
                        "HKD": 0
                    },
                    "product_modified_at": "2024-08-08 02:53:59",
                    "locale": "zh_HK:hotel",
                    "id": "1289139:zh_HK:hotel",
                    "category": [],
                    "discount": {
                        "HKD": 0
                    },
                    "original_price": {
                        "HKD": 0
                    }
                }
            ],
            "scroll_id": "DXF1ZXJ5QW5kRmV0Y2gBAAAAAd34d_sWejAzaTNwTlhUYVdzMjBHLThhTmNjZw==",
            "size": 5,
            "success": True,
            "total": 10
        }

        request_body = {
            "size": 5,
            "_source": {
                "exclude": ["modified_by", "modified_at", "recommendations", "suggest"]
            },
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "locale": "zh_HK:hotel"
                            }
                        }
                    ],
                    "must_not": [
                        {
                            "bool": {
                                "must": [
                                    {
                                        "exists": {
                                            "field": "is_status_passive"
                                        }
                                    },
                                    {
                                        "term": {
                                            "is_status_passive": 1
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
        }

        # Define the Pact interaction
        (pact
         .given('Internal query endpoint with given partner data')
         .upon_receiving('a request to insert an event')
         .with_request('POST', '/v2/internal-query', body=request_body, headers={'Content-Type': 'application/json'})
         .will_respond_with(200, body=expected_response, headers={'Content-Type': 'application/json'}))

        # With the Pact service running, send the request and check the response
        with pact:
            result = requests.post(pact.uri + '/v2/internal-query',
                                   params=
                                   {
                                       'partner': 'hutchgouat'
                                   }, json=request_body,
                                   headers={'Content-Type': 'application/json'})
            self.assertEqual(result.status_code, 200)
            actual_response = result.json()

            self.assertEqual(actual_response, expected_response)


if __name__ == '__main__':
    unittest.main()
