class hitungVolume :
  def __init__(self,p,l,t) :
    self.panjang = p
    self.lebar = l
    self.tinggi = t
  def getPanjang(self) :
    return self.panjang
  def getLebar(self) :
    return self.lebar
  def getTinggi(self) :
    return self.tinggi
  def getVolume(self) :
    return self.panjang * self.lebar * self.tinggi
