import random

class Palavra():

	def __init__(self):
		self.__vogais=['a','e','i','o','u']
		self.__consoantes=['B','C','D','F','G','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z']
		self.__palavra=[]

	def gera_palavra(self):
		self.__palavra.append(random.choice(self.__vogais))
		self.__palavra.append(random.choice(self.__consoantes))
		self.__palavra.append(random.choice(self.__vogais))
		self.__palavra.append(random.choice(self.__consoantes))
		palavra="".join(self.__palavra)
		self.__palavra=[]
		return palavra.lower()