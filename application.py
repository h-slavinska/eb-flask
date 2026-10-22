from flask import Flask

application = Flask(__name__)

@application.route("/")
def index():
    return "Hello from is9pw9s2 Elastic Beanstalk CI-CD"
