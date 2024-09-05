import atexit
import unittest
from pact import Consumer, Provider
import requests

# Pact configurations
pact = Consumer('SearchReportConsumer').has_pact_with(Provider('SearchReportProvider'), pact_dir='./pacts')
pact.start_service()  # Pact services starting
atexit.register(pact.stop_service)


class SearchReportContract(unittest.TestCase):
    def test_search_report(self):
        expected_response = {
            "data": {
                "noSearch": 1,
                "search": 5,
                "searchResults": {
                    "searchResultFound": {
                        "noSearch": 0,
                        "search": 5,
                        "searchResultType": "searchResultFound",
                        "terms": [
                            {
                                "noSearch": 0,
                                "search": 1,
                                "searchTerm": "çanta",
                                "totalSearch": 1
                            },
                            {
                                "noSearch": 0,
                                "search": 2,
                                "searchTerm": "Terlik",
                                "totalSearch": 2
                            },
                            {
                                "noSearch": 0,
                                "search": 1,
                                "searchTerm": "vs",
                                "totalSearch": 1
                            },
                            {
                                "noSearch": 0,
                                "search": 1,
                                "searchTerm": "Survivor",
                                "totalSearch": 1
                            }
                        ],
                        "totalSearch": 5
                    },
                    "searchResultNotFound": {
                        "noSearch": 1,
                        "search": 0,
                        "searchResultType": "searchResultNotFound",
                        "terms": [
                            {
                                "noSearch": 1,
                                "search": 0,
                                "searchTerm": "Statrum",
                                "totalSearch": 1
                            }
                        ],
                        "totalSearch": 1
                    }
                },
                "totalSearch": 6
            },
            "metaData": {
                "isCached": False,
                "cacheTime": 0,
                "expireTime": 0,
                "ttl": 0,
                "expireIn": 0,
                "checksum": "e3ba8dcb1334f7a5a458f01f7cf1bb2cfbf456de56d34cff6682edab02f6c3b4"
            },
            "status": 200
        }

        request_body = {
            "partners": [
                "kappatr"
            ],
            "time": {
                "start": 1690502400,
                "end": 1690543915
            },
            "timezone": "Europe/Istanbul",
            "_compare": {
                "start": 1660425659,
                "end": 1683765360
            },
            "select": [
                "search",
                "noSearch",
                "totalSearch"
            ],
            "aggregations": [
                {
                    "outputName": "searchResults",
                    "field": "searchResultType",
                    "outputType": "object",
                    "subAggregations": [
                        {
                            "outputName": "terms",
                            "field": "searchTerm",
                            "outputType": "array",
                            "subAggregations": []
                        }
                    ]
                }
            ],
            "preFilters": [],
            "postFilters": []
        }

        # Define the Pact interaction
        (pact
         .given('Search report with given partner data')
         .upon_receiving('a request to insert an event')
         .with_request('POST', '/v3/search-report', body=request_body, headers={'Content-Type': 'application/json'})
         .will_respond_with(200, body=expected_response, headers={'Content-Type': 'application/json'}))

        # With the Pact service running, send the request and check the response
        with pact:
            result = requests.post(pact.uri + '/v3/search-report', json=request_body,
                                   headers={'Content-Type': 'application/json'})
            self.assertEqual(result.status_code, 200)
            actual_response = result.json()

            self.assertEqual(actual_response, expected_response)


if __name__ == '__main__':
    unittest.main()
