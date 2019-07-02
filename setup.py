from distutils.core import setup

setup(
    name="onvif_client",
    version='1.3',
    description="ONVIF client based on Zeep library",
    keywords="ONVIF, Zeep",
    author="Angelcam",
    author_email="dev@angelcam.com",
    url="https://bitbucket.org/angelcam/onvif-client",
    license="MIT",
    long_description=open('README.md').read(),
    install_requires=['zeep[async]==2.3.0'],
    packages=['onvif_client'],
    package_dir={'onvif_client': 'src/onvif_client'},
    package_data={'onvif_client': ['wsdl/*.wsdl', 'wsdl/*.xsd']},
)
