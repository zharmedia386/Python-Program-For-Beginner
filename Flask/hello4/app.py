from flask import *
from models import testHello4

application = Flask(__name__)

@application.route('/')
def index() :
  model = testHello4()
  return render_template('template.html',model=model)

if __name__ == '__main__' :
  application.run(debug=True)