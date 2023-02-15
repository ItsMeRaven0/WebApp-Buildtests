from flask import render_template
import requests
import jxmlease

ACCESSTOKEN = ''
SERVERURL = ''

def troubleshooting_teamcity():
    #Teamcity: Anfrage Buildserver
    auth_token_teamcity = ACCESSTOKEN
    hed_teamcity = {'Authorization': 'Bearer ' + auth_token_teamcity}
    data_teamcity = {'app' : 'aaaaa'}
    url_teamcity = SERVERURL + '/app/rest/builds?locator=count:1,buildType:Bos_PublishBosToDevelopmentTestserver,state:finished'
    request_buildserver_teamcity = requests.get(url_teamcity, json=data_teamcity, headers=hed_teamcity)

    #Teamcity: Weiterverarbeitung
    xml_teamcity = jxmlease.parse(request_buildserver_teamcity.content)
    teamcity_build_id = xml_teamcity['builds']['build'].get_xml_attr("id")

    #Teamcity: Anfrage Problems
    error_url_teamcity = SERVERURL + '/app/rest/problemOccurrences?locator=build:(id:' + teamcity_build_id + ')'
    error_request_buildserver_teamcity = requests.get(error_url_teamcity, json=data_teamcity, headers=hed_teamcity)

    #Teamctiy: Weiterverarbeitung 
    error_request_buildserver_teamcity_content = str(error_request_buildserver_teamcity.content)
    error_request_buildserver_teamcity_content = error_request_buildserver_teamcity_content.split(" ")
    liste_temporary = []
    for x in error_request_buildserver_teamcity_content:
        if 'id="build' in x:
            liste_temporary.append(x)
    text_temporary = ""
    for x in liste_temporary:
        text_temporary = text_temporary + x
    text_temporary = text_temporary.split(")")
    liste_temporary = []
    for x in text_temporary:
        if 'problem' in x:
            liste_temporary.append(x)
    text_temporary = ""
    for x in liste_temporary:
        text_temporary = text_temporary + x
    text_temporary = text_temporary.split(":")
    liste_temporary = []
    for x in text_temporary:
        if '1' in x:
            liste_temporary.append(x)
    text_temporary = ""
    liste_complete = []
    for x in liste_temporary:
        if ',' in x:
            text_temporary = text_temporary + x + ","
        else:
            liste_complete.append(x)
    text_temporary = text_temporary.split(",")
    for x in text_temporary:
        if '1' in x:
            liste_complete.append(x)
    liste_problems_teamcity = []

    #Teamcity: Anfrage ProblemID + ProblemType
    for id in liste_complete:
        new_url = SERVERURL + "/app/rest/problemOccurrences?locator=count:1,problem:(id:" + id + ")"
        new_request = requests.get(new_url, json=data_teamcity, headers=hed_teamcity)
        new_xml_teamcity = jxmlease.parse(new_request.content)
        teamcity_problem_type = new_xml_teamcity['problemOccurrences']['problemOccurrence'].get_xml_attr("type")
        liste_problems_teamcity.append(id)
        liste_problems_teamcity.append(teamcity_problem_type)

    #Teamcity: Return result to WebApp
    return render_template('base.html') + render_template('teamcity_failure.html') +"<h4> All Problems:" + str(liste_problems_teamcity) + "</h4>"