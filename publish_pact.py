from pact import Broker

broker = Broker(broker_base_url='http://localhost:9292')
broker.publish('SearchReportConsumer', version='1.0.0', pact_dir='./pacts')