from onvif.client import ONVIFClient
from lxml import etree

onvif_client = ONVIFClient(
    host='10.19.57.69',
    port=80,
    username='admin',
    password='Angelcam123',
)

result = onvif_client.device.GetDeviceInformation()
print(result)

event_prop = onvif_client.event.GetEventProperties()
topic_set = event_prop.TopicSet
topic_attr_name='{http://docs.oasis-open.org/wsn/t-1}topic'
for topic in topic_set._value_1:
    print(topic.tag)
    tree = etree.ElementTree(topic)
    for e in tree.iter():
        if topic_attr_name in e.attrib:
            path = tree.getpath(e)
            print(path)





