import json
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import requests
from scripts import getSecret

# Get oauth2 token from Brightcove
# See: http://requests-oauthlib.readthedocs.io/en/latest/oauth2_workflow.html#backend-application-flow
# See: http://docs.brightcove.com/en/video-cloud/oauth-api/guides/get-token.html#python-code
def getToken():
    client_id = getSecret('rg-bc-client', 'id')
    client_secret = getSecret('rg-bc-client', 'secret')
    auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
    client = BackendApplicationClient(client_id=client_id)
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(token_url='https://oauth.brightcove.com/v3/access_token', auth=auth)
    auth = token['access_token']
    return auth

# Call Brightcove CMS API
# See: http://docs.brightcove.com/en/video-cloud/oauth-api/guides/get-token.html#python-code-line-76----------
# See: http://docs.python-requests.org/en/master/user/quickstart/#custom-headers
# See: http://docs.brightcove.com/en/video-cloud/cms-api/getting-started/overview-cms.html#parameters
accountid = getSecret('rg-bc-account')
url = "https://cms.api.brightcove.com/v1/accounts/{}/videos?limit=3&sort=-created_at".format(accountid) # NEED TO FIGURE OUT HOW TO PAGE ON THIS
bctoken = getToken()
headers = {"Authorization": "Bearer {}".format(bctoken)}
r = requests.get(url, headers=headers)
videos = json.loads(r.text)
for video in videos:
    print(video, "\n\n\n")
    #print(video['id'])
    #print(video['src'])
    #print(video['digital_master_id'])
    vurl = "https://cms.api.brightcove.com/v1/accounts/{0}/videos/{1}/sources".format(accountid,video['id'])
    vr = requests.get(vurl, headers=headers)
    vtext = vr.text
    vorig = video['original_filename'].split(".")
    #print(vtext)
    # Get all renditions
    rens = json.loads(vtext)
    for ren in rens:
        #print(ren['width'])
        if ren.has_key('width') and ren.has_key('src'):
            if ren['width'] == 960:
                if "http://" in ren['src']:
                    print ren['src']
                    # See: http://docs.brightcove.com/en/video-cloud/cms-api/references/cms-api/versions/v1/index.html#api-videoGroup-Get_Videos
                    outname = "out2/{0}-{1}.mp4".format(vorig[0],video['id'])
                    rr = requests.get(ren['src'])
                    outfile = open(outname, 'wb')
                    # See: http://stackoverflow.com/a/28374584
                    for chunk in rr.iter_content(chunk_size=255):
                        if chunk:
                            outfile.write(chunk)
                    outfile.close()
                    
                    