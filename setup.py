from distutils.core import setup

setup(
    name="onvif-client",
    version='1.0',
    description="ONVIF client based on Zeep library",
    keywords="ONVIF, Zeep",
    author="Angelcam",
    author_email="dev@angelcam.com",
    url="https://bitbucket.org/angelcam/onvif-client",
    license="MIT",
    long_description=open('README.md').read(),
    install_requires=['zeep[async]==2.0.0'],
    packages=['onvif'],
    package_dir={'onvif': 'src/onvif'},
    package_data={'onvif': ['wsdl/*.wsdl', 'wsdl/*.xsd']},
)
