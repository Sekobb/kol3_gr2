from __future__ import division

class diary(object):

	def __init__(self, przedmioty, studenci):
		self.lista_przedmiotow = przedmioty
		self.lista_studentow = studenci
		self.baza = {}
		for p in self.lista_przedmiotow:
			self.baza[p] = {}
			for s in self.lista_studentow:
				self.baza[p][s] = {}
				self.baza[p][s]['spr'] = []
				self.baza[p][s]['inne'] = []
				self.baza[p][s]['ob'] = []


	def dodaj(self, przedmiot, student, status, ocena):
		self.baza[przedmiot][student][status].append(ocena)

	def srednia(self, przedmiot, student):
		suma = sum(self.baza[przedmiot][student]['spr']) + sum(self.baza[przedmiot][student]['inne'])
		ilosc = len(self.baza[przedmiot][student]['spr']) + len(self.baza[przedmiot][student]['inne'])
		return round(suma/ilosc, 2)

	def spr_srednia(self, przedmiot, student):
		suma = sum(self.baza[przedmiot][student]['spr'])
		ilosc = len(self.baza[przedmiot][student]['spr'])
		return round(suma/ilosc, 2)

	def obecnosc(self, przedmiot, student):
		suma = sum(self.baza[przedmiot][student]['ob'])
		ilosc = len(self.baza[przedmiot][student]['ob'])
		return str(round((suma/ilosc) * 100, 2)) + '%'

	def przedmiot_dodaj(self, przedmiot):
		self.lista_przedmiotow.append(przedmiot)
		self.baza[przedmiot] = {}
		for s in self.lista_studentow:
			self.baza[przedmiot][s] = {}
			self.baza[przedmiot][s]['spr'] = []
			self.baza[przedmiot][s]['inne'] = []
			self.baza[przedmiot][s]['ob'] = []

	def przedmiot_usun(self, przedmiot):
		self.lista_przedmiotow.remove(przedmiot)
		del self.baza[przedmiot]

	def student_dodaj(self, student):
		self.lista_studentow.append(student)
		for p in self.lista_przedmiotow:
			self.baza[p][student] = {}
			self.baza[p][student]['spr'] = []
			self.baza[p][student]['inne'] = []
			self.baza[p][student]['ob'] = []

	def student_usun(self, student):
		self.lista_studentow.remove(student)
		for p in self.lista_przedmiotow:
			del self.baza[p][student]



	

