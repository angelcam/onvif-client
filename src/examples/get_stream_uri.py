from urllib.parse import urlparse
from onvif_client import ONVIFClient

host = '89.22.65.217'
port = 10089
client = ONVIFClient(
    host=host,
    port=port,
    username='admin',
    password='Angelcam123',
)


profiles = client.media.GetProfiles()

stream_setup = {
    'Stream': 'RTP-Multicast',
    'Transport': {
        'Protocol': 'RTSP',
    }
}

for profile in profiles:
    uri = client.media.GetStreamUri(StreamSetup=stream_setup, ProfileToken=profile.token)
    parsed = urlparse(uri.Uri)
    print('{}://{}:{}{}'.format(parsed.scheme, host, port, parsed.path))
