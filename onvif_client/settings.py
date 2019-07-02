import os


class BindingDefinition:
    dir_path = os.path.dirname(os.path.realpath(__file__))

    def __init__(self, wsdl, namespace, binding):
        self.wsdl = os.path.join(self.dir_path, 'wsdl', wsdl)
        self.namespace = namespace
        self.binding = "{{{namespace}}}{binding}".format(namespace=namespace, binding=binding)


DEVICE = 'Device'
MEDIA = 'Media'
EVENT = 'Event'


BINDINGS = {
    DEVICE: BindingDefinition(
        wsdl='devicemgmt.wsdl',
        namespace="http://www.onvif.org/ver10/device/wsdl",
        binding='DeviceBinding'
    ),
    MEDIA: BindingDefinition(
        wsdl='media.wsdl',
        namespace="http://www.onvif.org/ver10/media/wsdl",
        binding='MediaBinding'
    ),
    EVENT: BindingDefinition(
        wsdl='event.wsdl',
        namespace="http://www.onvif.org/ver10/events/wsdl",
        binding='EventBinding'
    )

}
