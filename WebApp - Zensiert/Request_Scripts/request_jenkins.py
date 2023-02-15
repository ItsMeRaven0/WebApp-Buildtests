import response_dictionary
import requests

USERNAME  = ''
ACCESSTOKEN = ''
SERVERURL = ''

def request_jenkins():
    failure_jenkins = False
    #Jenkins: Anfrage Buildserver
    hed_jenkins = (USERNAME, ACCESSTOKEN)
    url_jenkins = SERVERURL
    request_buildserver_jenkins = requests.get(url_jenkins, auth=hed_jenkins)
    json_request_buildserver_jenkins = request_buildserver_jenkins.json()

    #Jenkins: Weiterverarbeitung + Fehlerabfrage
    if request_buildserver_jenkins.status_code == 200:

        #Jenkins: Abfrage nach SUCCESS oder FAILURE
        if json_request_buildserver_jenkins['result'] == "SUCCESS":
            failure_jenkins = False
        elif json_request_buildserver_jenkins['result'] == "FAILURE":
            failure_jenkins = True
        else:
            print("ERROR: jenkins-build result unclear")
    else:
        print(request_buildserver_jenkins.status_code , " " , response_dictionary.responses[request_buildserver_jenkins.status_code])

    if failure_jenkins == False:

        #Jenkins: Anfrage2 Buildserver
        hed_jenkins = (USERNAME, ACCESSTOKEN)
        url2_jenkins = SERVERURL
        request2_buildserver_jenkins = requests.get(url2_jenkins, auth=hed_jenkins)
        json_request2_buildserver_jenkins = request2_buildserver_jenkins.json()

        #Jenkins: Weiterverarbeitung + Fehlerabfrage
        if request2_buildserver_jenkins.status_code == 200:

            #Jenkins: Abfrage nach SUCCESS oder FAILURE
            if json_request2_buildserver_jenkins['result'] == "SUCCESS":
                failure_jenkins = False
            elif json_request2_buildserver_jenkins['result'] == "FAILURE":
                failure_jenkins = True
            else:
                print("ERROR: jenkins-build result unclear")
        else:
              print(request2_buildserver_jenkins.status_code , " " , response_dictionary.responses[request2_buildserver_jenkins.status_code]) 
    if failure_jenkins == False:
        return False
    elif failure_jenkins == True:
        return True 
