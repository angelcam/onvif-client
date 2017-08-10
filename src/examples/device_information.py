from onvif_client import ONVIFClient

onvif_client = ONVIFClient(
    host='89.22.65.217',
    port=10080,
    username='admin',
    password='Angelcam123',
)

result = onvif_client.device.GetDeviceInformation()
print(result)

