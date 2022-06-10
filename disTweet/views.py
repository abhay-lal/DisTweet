from django.http import StreamingHttpResponse
from pykafka import KafkaClient


def get_kafka_client():
    return KafkaClient(hosts='127.0.0.1:9092')


def get_message(request):
    client = get_kafka_client()
    topic = client.topics['twitterdata1']
    consumer = topic.get_simple_consumer()

    def events():
        for message in consumer:
            if message is not None:
                yield 'data:{0}\n\n'.format(message.value.decode())

    return StreamingHttpResponse(events(), content_type='text/event-stream')