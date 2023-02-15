
from flask import Flask , render_template
from Request_Scripts import request_teamcity
from Request_Scripts import request_jenkins
from Request_Scripts import troubleshooting_teamcity
from Request_Scripts import troubleshooting_jenkins

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/overview/')
def overview():
    failure_teamcity = request_teamcity.request_teamcity()
    failure_jenkins = request_jenkins.request_jenkins()
    if failure_teamcity == False:
        html_teamcity = 'teamcity_success.html'
    elif failure_teamcity == True:
        html_teamcity = 'teamcity_failure.html'
    else:
        html_teamcity = 'teamcity_unknown.html'
    if failure_jenkins == False:
        html_jenkins = 'jenkins_success.html'
    elif failure_jenkins == True:
        html_jenkins = 'jenkins_failure.html'
    else:
        html_jenkins = 'jenkins_unknown.html'
    return render_template('base.html') + render_template('overview.html') + render_template(html_teamcity) + render_template(html_jenkins) + render_template('more_information.html')

@app.route('/teamcity/')
def teamcity():
    failure_teamcity = request_teamcity.request_teamcity()
    if failure_teamcity == False:
        return render_template('base.html') + render_template('teamcity_success.html')
    elif failure_teamcity == True:
        return troubleshooting_teamcity.troubleshooting_teamcity()
    else:
        return render_template('base.html') + render_template('requesterror.html')

@app.route('/jenkins/')
def jenkins():
    failure_jenkins = request_jenkins.request_jenkins()
    if failure_jenkins == False:
        return render_template('base.html') + render_template('jenkins_success.html')
    elif failure_jenkins == True:
        return troubleshooting_jenkins.troubleshooting_jenkins()
    else: 
        return render_template('base.html') + render_template('requesterror.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)