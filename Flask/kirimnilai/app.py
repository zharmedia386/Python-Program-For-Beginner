from flask import *
from models import hitungVolume
from models1 import hitungLuas

application = Flask(__name__)

@application.route('/')
def index() :
  temp = hitungVolume(3,4,5)
  panjang = temp.getPanjang()
  lebar = temp.getLebar()
  tinggi = temp.getTinggi()
  volume = temp.getVolume()
  return render_template('template.html',panjang=panjang,lebar=lebar,tinggi=tinggi,volume=volume)

@application.route('/circle')
def circle() :
  temp1 = hitungLuas(21)
  radius = temp1.getRadius()
  luas = temp1.getLuas()
  return render_template('template1.html',radius=radius,luas=luas)
if __name__ == '__main__' :
  application.run(debug=True)