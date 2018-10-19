import base.memoria as mem
import gerador.palavra as pal
from os import system,name

def clear():
	if name=='nt':
		_=system('cls')
	else:
		_=system('clear')

def main():
	choice=0

	memoria=mem.Memoria()
	palavra=pal.Palavra()

	while(choice!=3):
		choice=int(input("1 - Insira a qtde. de palavras que deseja gerar\n2 - Carregar arquivo das palavras\n3 - Sair\n  --> "))
		if choice==1:
			qtde=int(input("\nQtde -> "))
			memoria.salvar_palavras(qtde)
			clear()
		if choice==2:
			clear()
			memoria.carregar_arquivo()

if __name__ == "__main__":
	main()
