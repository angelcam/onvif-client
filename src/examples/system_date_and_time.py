from onvif.client import ONVIFClient

onvif_client = ONVIFClient(
    host='89.22.65.217',
    port=10080,
    username='admin',
    password='Angelcam123',
)

system_datetime = onvif_client.device.GetSystemDateAndTime()
print(system_datetime)
