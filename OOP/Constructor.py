class Kotak :
  def __init__(self,p,l,t) :
    self.panjang = p
    self.lebar = l
    self.tinggi = t
  def hitungVolume(self) :
    return self.panjang * self.lebar * self.tinggi
  def cetakVolume(self) :
    print('Panjang : ', self.panjang)
    print('Lebar : ', self.lebar)
    print('Tinggi : ', self.tinggi)
    print('Volume ', self.hitungVolume())
temp = Kotak(2,3,4)
temp.cetakVolume()