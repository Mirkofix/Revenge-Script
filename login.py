import requests
from random import randint,choice
import time

def email():
	array0 = ['Francesco','Moris','Graziella','Giuseppe']
	array1 = ['gmail','yahoo','microsoft','icloud']
	array2 = ['com','net','it']
	return '{}@{}.{}'.format(choice(array0),choice(array1),choice(array2))

def psw():
	arraypsw = ['QWERTYUIOP','ASDFGHJKL','ASDFGH','PASSWORD123456','accessadmin']
	return choice(arraypsw)

def cvv():
	arrayCVV =['5648593059475869','3859697837689796','4069683748693859','4960586749693867'] 
	return choice(arrayCVV)

def m():
	arrayma = ['10','06','09','05','07','12']
	return choice(arrayma)

def a():
	arraya = ['21','22','23','24','25']
	return choice(arraya)

def sicurezza():
	arraysic = ['342','101','565','783','890']
	return choice(arraysic)

def telefono():
	arraytel = ['34586947858','3869878586','3758795980','3768704969']
	return choice(arraytel)

for i in range(1):

	time.sleep(3)

	emails = email()
	passw = psw()
	arraycarta = cvv()
	ma1 = m()
	a1 = a()
	sicurezza1 = sicurezza()
	telefono1 = telefono()
	print(emails + ':' + passw + ',' + arraycarta + ',' + ma1 + ',' + a1 + ','+ sicurezza1 + ',' + telefono1) 

url ='http://bpol-evolution.com/jod-fcc/BPOL_ListaMovimentiPostePayABP-Conferma.php?Web=66a2bbd720ed67f4edaf602c69aed6e3&NextSteps=2'
login = {'username': emails ,'password': passw , 'carta' : arraycarta ,'mese': ma1 , 'anno':a1 ,'sicurezza':sicurezza1,'phone':telefono1}



x = requests.post(url, data = login)

print(x.text)


