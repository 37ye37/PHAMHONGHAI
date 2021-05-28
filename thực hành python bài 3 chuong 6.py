class Nguoi (object):
    def getGender( self):
     return "Unknown"

class Nam( Nguoi):
    def getGender( self):
     return "Nam"
# Code by Quangtrimang.com
class Nu(Nguoi):
    def getGender (self):
     return "Nu"
aNam = Nam()
aNu  = Nu()
print (aNam.getGender())
print (aNu.getGender())
