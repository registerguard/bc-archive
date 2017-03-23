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
url = "https://cms.api.brightcove.com/v1/accounts/{}/videos?limit=2&sort=-created_at".format(accountid)
bctoken = getToken()
headers = {"Authorization": "Bearer {}".format(bctoken)}
r = requests.get(url, headers=headers)
videos = json.loads(r.text)
for video in videos:
    #print(video, "\n\n\n")
    #print(video['id'])
    #print(video['src'])
    #print(video['digital_master_id'])
    vurl = "https://cms.api.brightcove.com/v1/accounts/{0}/videos/{1}/sources".format(accountid,video['id'])
    vr = requests.get(vurl, headers=headers)
    vdata = json.loads(vr.text)
    print(vdata)
#5366518646001


# Need to investigate this link for downloading video links
# http://docs.brightcove.com/en/video-cloud/cms-api/samples/download-links.html