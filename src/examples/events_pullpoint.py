from datetime import timedelta

from zeep import xsd

from onvif.client import ONVIFClient
from lxml import etree
onvif_client = ONVIFClient(
    host='10.19.57.91',
    port=80,
    username='admin',
    password='Angelcam123',
)


# topic = onvif_client.pull_point._client.get_type('ns5:TopicExpressionType')
# # value = xsd.AnyObject(xsd.String(), 'tns1:Monitoring/ProcessorUsage')
# # topic = topic(_value_1=value, Dialect='http://docs.oasis-open.org/wsn/t-1/TopicExpression/Concrete')
# topic = topic(Dialect='http://docs.oasis-open.org/wsn/t-1/TopicExpression/Concrete')

# output = onvif_client.event.CreatePullPointSubscription()
# print(output)


output = onvif_client.pull_point_subscription.PullMessages(Timeout='', MessageLimit=100)

print(output)




