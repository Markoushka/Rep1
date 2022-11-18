from bs4 import BeautifulSoup
import requests
response = requests.get("https://minfin.com.ua/ua/currency/nbu/")
if response.status_code == 200:
     soup = BeautifulSoup(response.text, features="html.parser")
     soup_list = soup.find("p", {"class": "sc-1x32wa2-9 glerpA"})
     res1 = soup_list.__str__().split('glerpA">')
     res2 = soup_list.__str__().split('<span')
     dollar = res1[1][0:2]
     dollar = dollar + "." + res2[0][len(res2[0])-2:len(res2[0])]
     print(dollar)

class Converter:
    def __init__(self,uahCount):
        self.kursdollar = dollar
        self.uahCount = uahCount
    def convertToUah(self):
        print(self.uahCount / float(self.kursdollar))
obj = Converter(15000000000)
obj.convertToUah()