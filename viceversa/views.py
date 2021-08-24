from django.http import	HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def reverse(request):
	user_text = request.GET['usertext']
	num_words = len(user_text.split(' '))
	print(num_words)
	reversed_text = user_text[::-1]
	return render(request, 'reverse.html', {'usertext':user_text,
		'reversedtext':reversed_text, 'num_words':num_words})