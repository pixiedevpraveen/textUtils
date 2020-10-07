# I have created this file - praveen
from django.http import HttpResponse
from django.shortcuts import render

def index(request): 
	return render(request, 'index.html')

def analyze(request):
	# get the text
	djtext = request.POST.get('text', 'default')
	removepunc = request.POST.get('removepunc', 'off')
	fullcaps = request.POST.get('fullcaps', 'off')
	newLineRemover = request.POST.get('newLineRemover', 'off')
	extraSpaceRemover = request.POST.get('extraSpaceRemover', 'off')
	charCount = request.POST.get('charCount', 'off')
	charCountWithoutSpace = request.POST.get('charCountWithoutSpace', 'off')
	analyzed = djtext
	purpose = "result"
	if removepunc == "on":
		Punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
		for char in djtext:
			if char not in Punctuations:
				analyzed = analyzed + char

	if(fullcaps == "on"):
		if analyzed != "":
			djtext = analyzed
			analyzed = ""
		for char in djtext:
			analyzed = analyzed + char.upper()

	if(extraSpaceRemover == "on"):
		if analyzed != "":
			djtext = analyzed
			analyzed = ""
		for index,char in enumerate(djtext):
			if not(djtext[index] == " " and djtext[index+1] == " "):
				analyzed = analyzed + char

	if(newLineRemover == "on"):
		if analyzed != "":
			djtext = analyzed
			analyzed = ""
		for char in djtext:
			if char != '\n' and char != '\r':
				analyzed = analyzed + char

	if(charCount == "on"):
		if analyzed != "":
			djtext = analyzed
		analyzed = analyzed + " character count: " + str(len(djtext))
		
	elif(charCountWithoutSpace == "on"):
		if analyzed != "":
			djtext = analyzed
		count = 0
		for char in djtext:
			if char == " ":
				count = count + 1
		analyzed = analyzed + " character count(without space): " + str(len(djtext)-count)

		
	prms = {'purpose':purpose,  'analyzed_text':analyzed }
	return render(request,'analyze.html',prms)

def capfirst(request):
	return HttpResponse("capitalize first")

def newlineremove(request):
	return HttpResponse("newlineRemove")
	
def spaceremove(request):
	return HttpResponse("spaceRemove")
	
def charcount(request):
	return HttpResponse("charCount")

# my custom
def reversed(request):
	Text = request.POST.get('text', 'default')
	size=0
	for x in Text:
		size+=1
	revText=""
	size-=1
	while size>=0:
		revText+=Text[size]
		size-=1

	print(revText)
	return HttpResponse("<h1>Output:</h1><br> <input type=\"text\" value=\""+revText+"\">")


def reverse(request):
	return render(request, 'reverse.html')

def about(request):
	return render(request, 'about.html')

def contact(request):
	return render(request, 'contact.html')
