from flask import *

application = Flask(__name__)
@application.route('/<int:panjang>')
def index(panjang) :
  return '<p> Panjang = %d,</p>' % panjang

if __name__ == '__main__' :
  application.run(debug=True)