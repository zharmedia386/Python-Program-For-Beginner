class PersegiPanjang(object) :
  def __init__(self,p,l) :
    self.panjang = p
    self.lebar = l
  def hitungLuas(self) :
    return  self.panjang * self.lebar
  def cetakLuas(self) :
    print('Panjang : ',self.panjang)
    print('Lebar : ',self.lebar)
    print('Luas : ',self.hitungLuas())

def main() :
  test = PersegiPanjang(5,6)
  test.cetakLuas()

if __name__ == '__main__' :
  main()