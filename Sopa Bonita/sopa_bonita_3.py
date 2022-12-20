from bs4 import BeautifulSoup
import requests

#HTML From Website
url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
#print(doc.prettify())
prices = doc.find_all(text="$")
parent = prices[0].parent
strong = parent.find("strong")
print("O valor atual é:",strong.string,"dólares")

#Video de Referência:
#https://www.youtube.com/watch?v=gRLHr664tXA