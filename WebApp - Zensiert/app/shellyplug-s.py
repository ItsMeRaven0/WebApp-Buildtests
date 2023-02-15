#Set-up
import requests
import time
from Request_Scripts import response_dictionary
from Request_Scripts import request_teamcity
from Request_Scripts import request_jenkins

a = 0
failure_teamcity = False
failure_jenkins = False


#loop-start
while a == 0:
      #Teamcity: Anfrage Buildserver 
      failure_teamcity = request_teamcity.request_teamcity()

      #Jenkins: Anfrage Buildserver
      failure_jenkins = request_jenkins.request_jenkins()

      #Shellyplug: Anfrage Plug
      request_shellyplug = requests.get("http://192.168.33.1/relay/0")

      #Shellyplug: Weiterverarbeitung + Fehlerabfrage
      if request_shellyplug.status_code == 200:

            #Shellyplug: Abfrage nach ON oder OFF
            if ((failure_teamcity == True) or (failure_jenkins == True)) and ('"ison":false' in request_shellyplug.text):
                  requests.get("http://192.168.33.1/relay/0?turn=on")
            elif ((failure_teamcity == False) and (failure_jenkins == False)) and ('"ison":true' in request_shellyplug.text):
                  requests.get("http://192.168.33.1/relay/0?turn=off")
      else:
            print("ERROR:Shellyplug not responding properly")
            print(request_shellyplug.status_code , " " , response_dictionary.responses[request_shellyplug.status_code])

      #loop-restart
      print("runningcheck")
      time.sleep(10)
      continue
