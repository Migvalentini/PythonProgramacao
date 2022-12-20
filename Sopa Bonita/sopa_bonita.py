from bs4 import BeautifulSoup

# HTML From File
with open("index.html", "r") as f:
	doc = BeautifulSoup(f, "html.parser")

funcao_prettify=doc.prettify()
print("FUNÇÃO PRETTIFY: \n",funcao_prettify)

funcao_extrair_texto = doc.get_text()
#print(funcao_extrair_texto)

funcao_printar_classe=doc.p
#print("FUNÇÃO PRINTAR CLASSE P: \n",funcao_printar_classe)#