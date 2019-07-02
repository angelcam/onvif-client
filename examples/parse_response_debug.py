# This is for debugging during parsing of response

import pretend  # pip install pretend
from zeep import Client
# Replace wsdl file, Binding with namespace and the method name you are calling.
#  The response needs to be set in the content=b'' var.


client = Client('../../wsdl/*********.wsdl')
service = client.create_service('{http://www.onvif.org/ver10/*****/wsdl}*Binding*', '')

response = pretend.stub(
status_code=200,
headers={},
content=b'',
)

operation = service._binding._operations['**MethodName**']
result = service._binding.process_reply(client, operation, response)
print(result)
