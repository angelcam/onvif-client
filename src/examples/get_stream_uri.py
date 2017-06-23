from urllib.parse import urlparse
from onvif.client import ONVIFClient

onvif_client = ONVIFClient(
    host='10.19.57.91',
    port=80,
    username='admin',
    password='Angelcam123',
)
result = onvif_client.device.GetDeviceInformation()
print(result)

profiles = onvif_client.media.GetProfiles()
# print(profiles)
stream_setup = {
    'Stream': 'RTP-Multicast',
    'Transport': {
        'Protocol': 'RTSP',
    }
}

for profile in profiles:
    print("Name:", profile.Name)
    print("Encoding:", profile.VideoEncoderConfiguration.Encoding)
    print("Resolution:", profile.VideoEncoderConfiguration.Resolution.Width, 'x', profile.VideoEncoderConfiguration.Resolution.Height)
    uri = onvif_client.media.GetStreamUri(StreamSetup=stream_setup, ProfileToken=profile.token)
    parsed = urlparse(uri.Uri)
    print("Path:", parsed.path)
    print('******************************************************')
