class kotak(object) :
  def __init__(self,p,l) :
    print('Konstruktor dipanggil!')
    self.panjang = p
    self.lebar = l
  def __del__(self) :
    print('Destruktor dipanggil!')
  def hitungLuas(self) :
    return self.panjang * self.lebar
  def cetakData(self) :
    print('Panjang : ', self.panjang)
    print('Lebar : ', self.lebar)
    print('Luas : ', self.hitungLuas())

def main() :
  # Konstruktor
  obj = kotak(4,2)
  obj.cetakData()
  # Destruktor
  del obj

  # obj.cetakData() Jika di-run, akan ada notifikasi error

if __name__ == '__main__' :
  main()