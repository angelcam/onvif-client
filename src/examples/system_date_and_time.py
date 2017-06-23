from onvif.client import ONVIFClient

onvif_client = ONVIFClient(
    host='10.19.57.126',
    port=80,
    username='admin',
    password='Angelcam123',
)

system_datetime = onvif_client.device.GetSystemDateAndTime()
print(system_datetime)
