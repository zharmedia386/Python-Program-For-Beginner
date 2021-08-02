"""
Tidak diperkenankan membuat 2 modul atau lebih dengan nama yang sama
"""

class person :
  def __init__(self,name='',age=0) : 
    self.name = name
    self.age = age
  def setPerson(self,name,age,status) :
    self.name = name
    self.age =age
    self.status = status
  def cetakPerson(self) :
    print('Name : ', self.name)
    print('Age : ', self.age)
    print('Status : ',self.status)

orang = person()
orang.setPerson('Azhar',18,'Mahasiswa')
orang.cetakPerson()