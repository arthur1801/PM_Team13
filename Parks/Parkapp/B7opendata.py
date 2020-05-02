import json
import urllib.request as request
from .models import B7data

B7_url = 'https://opendataprod.br7.org.il/dataset/8ab84c8f-2842-4d41-8838-978a757b5759/resource/f3d2fe4a-0b57-4c88-b6c5-089df5949278/download/playgrounds.json'


def getdataB7_JSON():

    with request.urlopen(B7_url) as response:
        source = response.read()
        data = json.loads(source)
    return data

def updatedb():
    # B7_url = 'https://opendataprod.br7.org.il/dataset/8ab84c8f-2842-4d41-8838-978a757b5759/resource/f3d2fe4a-0b57-4c88-b6c5-089df5949278/download/playgrounds.json'
    # with request.urlopen(B7_url) as response:
    #     source = response.read()
    #     data = json.loads(source)
    # print(data)
    data = getdataB7_JSON()
    for i in data:
        temp = B7data(Name = i['Name'],surface = i['surface'],shadowing = i['shadowing'],combined1 = i['combined1'],combined2 = i['combined2'],combined3 = i['combined3'],SpecialCom = i['SpecialCom'],Swing = i['Swing'],slid = i['slid'],carrousel = i['carrousel'],spring = i['spring'],omega = i['omega'],roserose = i['roserose'],other = i['other'],lat = i['lat'],lon = i['lon'])
        temp.save()


