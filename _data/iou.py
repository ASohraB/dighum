from icecream import *

uc=IceCreamDebugger()
tc=IceCreamDebugger()
oc=IceCreamDebugger()

celscilist = {
'dd':{'fb':{'followers': 400}},
'jp':{'fb':{'followers': 300}},
'sh':{'fb':{'followers': 200}},
'gs':{'fb':{'followers': 100}}
}

class celsci():

    def famus(x):
        y="low"
        if x>300:
            y= 'high'
        return y
 
def findperson(x):
    person = celsci.famus(celscilist[x]['fb']['followers'])
    return person
    

#ic(celsci.person)
ic(findperson('gs'))
