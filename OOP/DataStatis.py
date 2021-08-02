"""
Variabel : variabel objek(instance variable) & variabel kelas(class variable)
class Kotak(object):
   ObjectCounter = 0 # class variable
   def __init__(self, p, l, t):
      self.panjang = p # instance variable
      self.lebar = l # instance variable
      self.tinggi = t # instance variable
"""

class Kotak(object) :
  # Menghitung banyaknya object
  objectCounter = 0
  def __init__(self,p,l,t) :
    print('Konstruktor dipanggil!')
    self.panjang = p
    self.lebar = l
    self.tinggi = t
    Kotak.objectCounter += 1
  def __del__(self) :
    print('Destruktor dipanggil!')
  def hitungVolume(self) :
    return self.panjang * self.lebar * self.tinggi
  def cetakData(self) :
    print('Panjang : ',self.panjang)
    print('Lebar : ',self.lebar)
    print('Tinggi : ',self.tinggi)
    print('Volume : ',self.hitungVolume())

print('Object 1')
obj1 = Kotak(3,4,5)
obj1.cetakData()
print('Jumlah object : ',obj1.objectCounter)
del obj1

print()

print('Object 2')
obj2 = Kotak(5,6,7)
obj2.cetakData()
print('Jumlah Object : ',obj2.objectCounter)
del obj2
