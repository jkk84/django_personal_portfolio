from django.shortcuts import render
import random

def passgenerator(request):
	characters = list('abcdefghijklmnopqrstuvwxyz')

	if request.GET.get('uppercase'):
		characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
	if request.GET.get('special'):
		characters.extend(['`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}','}','|','\\',':',';','"',"'",'<',',','>','.','?','/'])
		# characters.extend(list('!@#$%^&*()'))
	if request.GET.get('numbers'):
		characters.extend(list('0123456789'))

	length = int(request.GET.get('length', 12))

	thepassword = ''
	for x in range(length):
		thepassword += random.choice(characters)

	return render(request, 'passgenerator/passgenerator.html', {'password': thepassword})