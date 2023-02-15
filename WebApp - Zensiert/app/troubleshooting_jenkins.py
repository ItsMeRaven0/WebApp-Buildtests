from flask import render_template
import requests

USERNAME = ''
ACCESSTOKEN = ''
URLTEST1 = ''
URLTEST2 = ''
URLTEST3 = ''
URLTEST4 = ''
URLTEST5 = ''
URLTEST6 = ''

def troubleshooting_jenkins():
    liste_problems_jenkins = []

    #Jenkins: Anfrage welcher Teil broken:
    hed_jenkins = (USERNAME, ACCESSTOKEN)
    error_url1_jenkins = URLTEST1
    error_request1_buildserver_jenkins = requests.get(error_url1_jenkins, auth=hed_jenkins)
    error_json_request1_buildserver_jenkins = error_request1_buildserver_jenkins.json()
                
    if error_json_request1_buildserver_jenkins['result'] == "FAILURE":
        liste_problems_jenkins.append(Url1)   

    error_url2_jenkins = URLTEST2
    error_request2_buildserver_jenkins = requests.get(error_url2_jenkins, auth=hed_jenkins)
    error_json_request2_buildserver_jenkins = error_request2_buildserver_jenkins.json()
                
    if error_json_request2_buildserver_jenkins['result'] == "FAILURE":
        liste_problems_jenkins.append(Url2)

    error_url3_jenkins = URLTEST3
    error_request3_buildserver_jenkins = requests.get(error_url3_jenkins, auth=hed_jenkins)
    error_json_request3_buildserver_jenkins = error_request3_buildserver_jenkins.json()
                
    if error_json_request3_buildserver_jenkins['result'] == "FAILURE":
        liste_problems_jenkins.append(Url3)
        
    error_url4_jenkins = URLTEST4
    error_request4_buildserver_jenkins = requests.get(error_url4_jenkins, auth=hed_jenkins)
    error_json_request4_buildserver_jenkins = error_request4_buildserver_jenkins.json()
                
    if error_json_request4_buildserver_jenkins['result'] == "FAILURE":
        liste_problems_jenkins.append(Url4)
        
    error_url5_jenkins = URLTEST5
    error_request5_buildserver_jenkins = requests.get(error_url5_jenkins, auth=hed_jenkins)
    error_json_request5_buildserver_jenkins = error_request5_buildserver_jenkins.json()
                
    if error_json_request5_buildserver_jenkins['result'] == "FAILURE":
        liste_problems_jenkins.append(Url5)
        
    error_url6_jenkins = URLTEST6
    error_request6_buildserver_jenkins = requests.get(error_url6_jenkins, auth=hed_jenkins)
    error_json_request6_buildserver_jenkins = error_request6_buildserver_jenkins.json()
                
    if error_json_request6_buildserver_jenkins['result'] == "FAILURE":
        liste_problems_jenkins.append(Url6)
    
    return render_template('base.html') + render_template('jenkins_failure.html') +"<h4> Failed Unit tests:" + str(liste_problems_jenkins) + "</h4>"