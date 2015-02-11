from django.conf import settings

class Constants:
    def __init__(self, switch, value):
        self.INVALID_VALUE = "The specified value for the switch %s is invalid " %(switch)
        self.MAX_NUMBER_OF_RELAYS = "The number of relays to scan is more larger than the permitted. In the free version of Tortazo, you can scan only %s relays" %(str(settings.MAX_TORTAZO_RELAYS))
        self.PORT_INVALID="One or more of the specified ports are invalid. Check the list of ports used in the switch '--list-ports'. It must be a list comma-separated of integers between 1 and 65535."
        self.NONEVALUE = "You must specify a valid value for the switch %s." %(switch)
        self.SCANID_INVALID="The scan identifier specified is invalid. It must be a numeric value."

class ScanUtils:
    def __init__(self, tortazoExecutor):
        self.tortazoExecutor = tortazoExecutor
        self.message = ""
    
    
    '''
    Check if the "mode" argument is present in the structure received from the client.
    '''
    def validateMandatoryScanArgument(self, structure):
        if structure.has_key("mode"):
            self.tortazoExecutor.mode.setValue(structure["mode"]["value"])
            return True
        else:
            return False

    '''
    Validate the scan argument received from the client.
    '''
    def validateScanArgument(self, argument):
        self.constants = Constants(argument["switch"], argument["value"])
        if argument["switch"] == "--use-meMirrors":
            self.tortazoExecutor.useMirrors.setValue(True)
            return True
            
        if argument["switch"] == "--use-database":
            self.tortazoExecutor.useDatabase.setValue(True)
            return True
            
        if argument["switch"] == "--servers-to-attack":
            numberRelays = argument["value"]
            print "accept"
            if numberRelays is not None and numberRelays.isdigit():
                print "good"
                relays = int(numberRelays)
                print "good good"
                if relays < settings.MAX_TORTAZO_RELAYS:
                    self.message = self.constants.MAX_NUMBER_OF_RELAYS
                    return False
                else:
                    self.tortazoExecutor.serversToAttack.setValue(numberRelays)
                    return True
            else:
                self.message = self.constants.INVALID_VALUE
                return False
                
        if argument["switch"] == "--list-ports":
            if argument["value"] is None:
                self.message = self.constants.NONEVALUE
                return False
            ports = argument["value"].split(',')
            for port in ports:
                if port.isdigit():
                    scanPort = int(port)
                    if scanPort in range(1,65535):
                        continue
                else:
                    self.message = self.constants.PORT_INVALID
                    return False
            self.tortazoExecutor.listScanPorts.setValue(argument["value"])
            return True
        
        if argument["switch"] == "--exit-node-fingerprint":
            if argument["value"] is None:
                self.message = self.constants.NONEVALUE
                return False
            else:
                self.tortazoExecutor.exitNodeFingerprint.setValue(argument["value"])
                return True
                
        
        if argument["switch"] == "--exclude-fingerprints":
            if argument["value"] is None:
                self.message = self.constants.NONEVALUE
                return False
            fingerprints = argument["value"].split(',')
            for fingerprint in fingerprints:
                if fingerprint is None:
                    self.message = self.constants.NONEVALUE
                    return False
            self.tortazoExecutor.exitNodeFingerprint.setValue(argument["value"])
            return True
            
        
        if argument["switch"] == "--scan-arguments":
            if argument["value"] is None:
                self.message = self.constants.NONEVALUE
                return False
            else:
                return True
                
        if argument["switch"] == "--scan-identifier":
            if argument["value"] is None:
                self.message = self.constants.NONEVALUE
                return False
            else:
                if argument["value"].isdigit() == False:
                    self.message = self.constants.SCANID_INVALID
                    return False
                else:
                    return True

class PluginUtils:
    pass

class BotnetUtils:
    pass