
from osmparser.IOSMPbfParser import IOSMPbfParser
from osmparser.OSMPbfParserImpl import OSMPbfParserImpl 
from PFinderConfig import osmPbfFile
from RepositoryConnection import RepositoryConnection
from PFinderConfig import dbHost
from PFinderConfig import dbPort
from PFinderConfig import dbRepository
from sys import argv   
def invokeParser():
    try:
        repository=RepositoryConnection(dbHost, dbPort, dbRepository)
        osmParser  = OSMPbfParserImpl(IOSMPbfParser(),osmPbfFile,callback_type=argv[1],repository=repository)
        osmParser.start()
    except Exception as e:
        print(e)
invokeParser()
