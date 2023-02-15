import response_dictionary
import jxmlease
import requests

ACCESSTOKEN = ''
SERVERURL = ''

def request_teamcity():
    #Teamcity: Anfrage Buildserver 
    auth_token_teamcity = ACCESSTOKEN
    hed_teamcity = {'Authorization': 'Bearer ' + auth_token_teamcity}
    data_teamcity = {'app' : 'aaaaa'}
    url_teamcity = SERVERURL
    request_buildserver_teamcity = requests.get(url_teamcity, json=data_teamcity, headers=hed_teamcity)

    #Teamcity: Weiterverarbeitung + Fehlerabfrage
    if int(request_buildserver_teamcity.status_code) == 200:
        xml_teamcity = jxmlease.parse(request_buildserver_teamcity.content)
        status_teamcity = xml_teamcity['builds']['build'].get_xml_attr("status")

        #Teamcity: Abfrage nach SUCCESS oder FAILURE
        if status_teamcity == 'SUCCESS':
              return False
        elif status_teamcity == 'FAILURE':
              return True
        else:
              print("ERROR: teamcity-build status unclear")
    else:  
        print("ERROR: teamcity-buildserver not responding properly")
        print(request_buildserver_teamcity.status_code , " " , response_dictionary.responses[request_buildserver_teamcity.status_code])