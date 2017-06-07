import asyncio

from zeep import Client
from zeep.wsse.username import UsernameToken
from zeep.asyncio import AsyncTransport
from zeep.transports import Transport

from urllib.parse import urlparse

from onvif import settings


class ONVIFClient:

    def __init__(self, host, port, username=None, password=None):
        self.__host = host
        self.__port = int(port)
        self.__token = None
        if username is not None and password is not None:
            self.__token = UsernameToken(username, password, use_digest=True)
        self.__transport = self._get_transport()
        self.__addr_paths = {
            settings.DEVICE: '/onvif/device_service',
        }
        # Active service client container
        self.__cached_services = {}
        self.__paths_loaded = False

    def __get_service(self, name, cache=True):
        if cache:
            service = self.__cached_services.get(name)
            if not service:
                service = self.__create_service(name)
                self.__cached_services[name] = service
            return service
        else:
            return self.__create_service(name)

    def __get_address(self, name):
        if not (self.__paths_loaded or name == settings.DEVICE):
            self.__load_paths()
        return "{scheme}://{host}:{port}{service_point}".format(
            scheme='http',
            host=self.__host,
            port=self.__port,
            service_point=self.__addr_paths.get(name)
        )

    def __get_client(self, name):
        client = Client(
            wsdl=settings.BINDINGS.get(name).wsdl,
            wsse=self.__token,
            transport=self.__transport,
        )
        return client

    def __create_service(self, name):
        client = self.__get_client(name)
        binding = settings.BINDINGS.get(name).binding
        address = self.__get_address(name)
        service = client.create_service(binding, address)
        return service

    def __load_paths(self):
        capabilities = self.device.GetServices(IncludeCapability=False)
        for capability in capabilities:
            namespace = capability.Namespace
            for name, binding in settings.BINDINGS.items():
                if namespace == binding.namespace:
                    self.__addr_paths[name] = urlparse(capability.XAddr).path
        self.__paths_loaded = True

    def _get_transport(self):
        return Transport()

    def get_new_service(self, name, raw_response):
        """
        Just for debugging purpose.
        """
        service = self.__get_service(name, cache=False)
        service._client.raw_response = raw_response
        return service

    @property
    def device(self):
        return self.__get_service(settings.DEVICE)

    @property
    def media(self):
        return self.__get_service(settings.MEDIA)

    @property
    def event(self):
        return self.__get_service(settings.EVENT)


class AsyncONVIFClient(ONVIFClient):
    def __init__(self, host, port, username, password, loop=None):
        self.loop = loop or asyncio.get_event_loop()
        super().__init__(host, port, username, password)

    def _get_transport(self):
        return AsyncTransport(loop=self.loop)
