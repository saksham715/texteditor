#This file is created by me
#server first goes to urls.py and search for views.py
from django.http import HttpResponse
from django.shortcuts import render
# def txtfile(request):
#     with open("1.txt", "r") as f:
#         return HttpResponse(f.read())

def index(request):
#     # return HttpResponse("Home<br><a href = /spaceremove>next</a>")
     return render(request, 'index.html')
#
# def spacelineremove(request):
#     print(request.GET.get('text', 'default'))
#     return HttpResponse("spaceremove<br><a href = />back</a><br><a href = /newlineremove>next</a>")
#
# def newlineremove(request):
#     return HttpResponse("newline remove<br><a href = /spaceremove>back</a><br><a href = /capfirst>next</a>")
#
# def capfirst(request):
#     return HttpResponse("Capitalize first<br><a href = /newlineremove>back</a><br><a href = /removepunc>next</a>")
#
# def removepunc(request):
#     return HttpResponse("remove punctuation<br><a href = /capfirst>back</a><br><a href = /charcount>next</a>")
#
# def charcount(request):
#     return HttpResponse("count characters<br><a href = /removepunc>back</a>")

# def home(request):
#     return render(request, 'index.html')
#
def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    # Checking the checkbox value
    rempun = request.POST.get('removepunc', 'Off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newline = request.POST.get('newline', 'Off')
    space = request.POST.get('space', 'Off')
    count = request.POST.get('count', 'Off')
    which = request.POST.get('which', 'default')


    #Check which checkbox is on

#################################################################################
    if rempun == 'on':
        punc = '''.”“‘,-!:;()[]{}=\+…/'<>"""@#$%^&*_?'''
        analyzed = ""
        for i in djtext:
            if i not in punc:
                analyzed  = analyzed + i
        params = {'purpose':'Removed Punctuation', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

#################################################################################
    if fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

#################################################################################
    if newline == 'on':
        analyzed = ""
        for char in djtext:
            if char != '\n' and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

###################################################################################
    if space == 'on':
        analyzed = ""
        for index,char in enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1] == " ":
                pass
            else:
                analyzed = analyzed + char

        params = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)
###################################################################################
    if count == 'on':
        if len(which) == 1:
            analyzed = ""
            analyzed = analyzed + str(djtext.count(which))

            params = {'purpose': 'Character Count', 'analyzed_text': analyzed}

            # Analyze the text
            # return render(request, 'analyze.html', params)
        elif len(which)>1:
            analyzed = ""
            analyzed = analyzed + str(djtext.count(which[0]))

            params = {'purpose': 'Character Count', 'analyzed_text': analyzed}

######################################################################################

    if rempun != 'on' and count != 'on' and space != 'on' and newline != 'on' and fullcaps != 'on':
        return HttpResponse("<h1>Please select any operation!</h1>")



    return render(request, 'analyze.html', params)

######################################################################################

#
# def newlineremove(request):
#     return HttpResponse("newline remove")
#
# def capfirst(request):
#     return HttpResponse("Capitalize first")

# def removepunc(request):
#     return HttpResponse("remove punctuation")

# def charcount(request):
#     return HttpResponse("count characters")

