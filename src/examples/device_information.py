from onvif.client import ONVIFClient

onvif_client = ONVIFClient(
    host='10.19.57.91',
    port=80,
    username='admin',
    password='Angelcam123',
)

result = onvif_client.device.GetDeviceInformation()
print(result)

