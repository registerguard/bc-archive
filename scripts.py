import os, json

# ----------------------------------------------------------------------------------------
# SECRETS
# ----------------------------------------------------------------------------------------

def getSecret(service, token='null'):
    
    secrets_path = os.path.join(os.path.abspath(os.path.dirname(__file__)))
    #print "Service: {}".format(service)
    #print "Token: {}".format(token)
    with open("{}/secrets.json".format(secrets_path)) as data:
        s = json.load(data)
        #print s
        #print s['{}'.format(service)]['{}'.format(token)]
        # If there is no token, return whole parent object
        if token == 'null':
            secret = s['{}'.format(service)]
        else:
            secret = s['{}'.format(service)]['{}'.format(token)]
        #logger.debug("EXIT secrets: {}".format(len(secret)))
        return secret