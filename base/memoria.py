import gerador.palavra as pal

class Memoria():

	def __init__(self):
		self.__palavra=pal.Palavra()

	def salvar_palavras(self,qtde_linhas):
		open('base_palavras.txt','w').close()
		arq=open('base_palavras.txt','w')
		for i in range(qtde_linhas):
			p=self.__palavra.gera_palavra()
			arq.write(p+'\n')
		arq.close()

	def carregar_arquivo(self):
		arq=open('base_palavras.txt','r')
		for f in arq.readlines():
			print(f)