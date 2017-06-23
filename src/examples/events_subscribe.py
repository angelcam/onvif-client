from zeep import xsd

from onvif.client import ONVIFClient
from lxml import etree

onvif_client = ONVIFClient(
    host='10.19.57.72',
    port=80,
    username='admin',
    password='Angelcam123',
)


# consumer_reference={
#     'Address': 'http://b34b2a42.ngrok.io',
# }
# filter=""
# output = onvif_client.notification.Subscribe(ConsumerReference=consumer_reference, InitialTerminationTime="PT1M", Filter=filter)
#


print(output)




