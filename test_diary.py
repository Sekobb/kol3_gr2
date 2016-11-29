from __future__ import division

import unittest
from diary import *

class test_diary(unittest.TestCase):

	def setUp(self):
		self.przedmioty = ['matematyka', 'fizyka', 'cpp']
		self.studenci = ['Jan Kowalski', 'Wojciech Nowak', 'Jerzy Gzik']

		self.dziennik = diary(self.przedmioty, self.studenci)

		self.dziennik.dodaj('fizyka', 'Wojciech Nowak', 'spr', 4)
		self.dziennik.dodaj('fizyka', 'Wojciech Nowak', 'spr', 5)
		self.dziennik.dodaj('fizyka', 'Wojciech Nowak', 'spr', 5)
		self.dziennik.dodaj('fizyka', 'Wojciech Nowak', 'inne', 2)

		self.dziennik.dodaj('matematyka', 'Jan Kowalski', 'ob', 1)
		self.dziennik.dodaj('matematyka', 'Jan Kowalski', 'ob', 0)
		self.dziennik.dodaj('matematyka', 'Jan Kowalski', 'ob', 0)
		self.dziennik.dodaj('matematyka', 'Jan Kowalski', 'ob', 0)

	def test_dziennik(self):
		print("Sprawdzenie, czy obiekt jest instancja klasy diary")
		self.assertIsInstance(self.dziennik, diary)

	def test_przedmioty(self):
		print("Sprawdzenie, czy obiekt zawiera wszystkie przedmioty")
		self.assertEqual(['matematyka', 'fizyka', 'cpp'], self.dziennik.lista_przedmiotow)

	def test_studenci(self):
		print("Sprawdzenie, czy obiekt zawiera wszystkich studentow")
		self.assertEqual(['Jan Kowalski', 'Wojciech Nowak', 'Jerzy Gzik'], self.dziennik.lista_studentow)

	def test_klucz_spr(self):
		print("Sprawdzenie poprawnosci wyszukiwania po kluczach dla ocen ze sprawdzianow")
		self.assertEqual([4,5,5], self.dziennik.baza['fizyka']['Wojciech Nowak']['spr'])

	def test_klucz_inne(self):
		print("Sprawdzenie poprawnosci wyszukiwania po kluczach dla innych ocen")
		self.assertEqual([2], self.dziennik.baza['fizyka']['Wojciech Nowak']['inne'])

	def test_klucz_obecnosci(self):
		print("Sprawdzenie poprawnosci wyszukiwania po kluczach dla obecnosci")
		self.assertEqual([1,0,0,0], self.dziennik.baza['matematyka']['Jan Kowalski']['ob'])

	def test_srednia_instance_of_float(self):
		print("Sprawdzenie, czy metoda srednia() zwraca odpowiednia wartosc")
		self.assertIsInstance(self.dziennik.srednia('fizyka', 'Wojciech Nowak'), float)
		self.assertNotIsInstance(self.dziennik.srednia('fizyka', 'Wojciech Nowak'), str)

	def test_spr_srednia_instance_of_float(self):
		print("Sprawdzenie, czy metoda spr_srednia() zwraca odpowiednia wartosc")
		self.assertIsInstance(self.dziennik.spr_srednia('fizyka', 'Wojciech Nowak'), float)
		self.assertNotIsInstance(self.dziennik.spr_srednia('fizyka', 'Wojciech Nowak'), str)

	def test_obecnosc_instance_of_str(self):
		print("Sprawdzenie, czy metoda obecnosc() zwraca odpowiednia wartosc")
		self.assertIsInstance(self.dziennik.obecnosc('matematyka', 'Jan Kowalski'), str)
		self.assertNotIsInstance(self.dziennik.obecnosc('matematyka', 'Jan Kowalski'), float)
		self.assertNotIsInstance(self.dziennik.obecnosc('matematyka', 'Jan Kowalski'), int)

	def test_student_usun(self):
		print("Sprawdzenie poprawnosci usuwania studenta")
		self.assertIsNone(self.dziennik.student_usun("Jan Kowalski"))

	def test_przedmiot_usun(self):
		print("Sprawdzenie poprawnosci usuwania przedmiotu")
		self.assertIsNone(self.dziennik.przedmiot_usun("fizyka"))

	def test_student_dodaj(self):
		print("Sprawdzenie poprawnosci dodawania studenta")
		self.assertIsNone(self.dziennik.student_dodaj('Marian Bzik'))

	def test_przedmiot_dodaj(self):
		print("Sprawdzenie poprawnosci dodawania przedmiotu")
		self.assertIsNone(self.dziennik.przedmiot_dodaj('python'))

if __name__ == '__main__':
	unittest.main()


