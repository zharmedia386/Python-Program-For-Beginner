from flask import Flask
from models import hello2
application = Flask(__name__)

@application.route('/')
def index() :
  model = hello2()
  return model.getText()

if __name__ == '__main__' :
  application.run(debug=True)