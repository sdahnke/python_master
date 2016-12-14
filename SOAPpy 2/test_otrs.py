from SOAPpy import WSDL

server = WSDL.Proxy('file//C:/Users/sdahnke/Desktop/otrs.wsdl')
print server.methods.keys()
