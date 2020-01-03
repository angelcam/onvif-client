from setuptools import setup

setup(
    name="onvif-client",
    version='1.1',
    description="ONVIF client based on Zeep library",
    keywords="ONVIF, Zeep",
    author="Angelcam",
    author_email="dev@angelcam.com",
    url="https://bitbucket.org/angelcam/onvif-client",
    license="MIT",
    long_description=open('README.md').read(),
    install_requires=['zeep[async]==2.3.0'],
    packages=['onvif_client'],
    package_dir={'': 'src'},
    package_data={'onvif_client': ['wsdl/*.wsdl', 'wsdl/*.xsd']},
)
