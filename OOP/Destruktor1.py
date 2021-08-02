class myFile(object) :
  def __init__(self,namaFile) :
    # membuka file
    self.file = open(namaFile)
  def __del__(self) :
    # menutup files
    self.file.close()
  def bacadata(self) :
    for baris in self.file :
      print(baris,end='')

# Instansiasi Objek
f = myFile('D:\\02 ZHAR\'S PROJECT\\0000 Programming\Python\Python-Programming-Exercies\OOP\sample.txt')

f.bacadata()
f.__del__()
# f.bacadata() Jika di-run, akan ada notifikasi error