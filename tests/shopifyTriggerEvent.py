import atexit
import unittest
from pact import Consumer, Provider
import requests
from global_values import EMAIL, PARTNER

# Pact configurations
pact = Consumer('EventConsumer').has_pact_with(Provider('EventProvider'), pact_dir='./pacts')
pact.start_service()  # Pact services starting
atexit.register(pact.stop_service)

class EventTriggerContract(unittest.TestCase):
    def test_trigger_event(self):

        expected_response = {"eren": True}

        request_body = {
            "partner": PARTNER,
            "source": "email",
            "identifiers": {
                "em": EMAIL
            },
            "events": [
                {
                    "event_name": "email_open",
                    "timestamp": 1719827005
                }
            ]
        }

        # Define the Pact interaction
        (pact
         .given('User with email exists')
         .upon_receiving('a request to insert an event')
         .with_request('post', '/api/event/v1/insert', body=request_body)
         .will_respond_with(200, body=expected_response))

        # With the Pact service running, send the request and check the response
        with pact:
            result = requests.post(pact.uri + '/api/event/v1/insert', json=request_body)
            self.assertEqual(result.status_code, 200)
            self.assertEqual(result.json(), expected_response)

if __name__ == '__main__':
    unittest.main()
