# This is my website which i have created
# from django.http import HttpResponse

# def index(request):
#     return HttpResponse(''' Hello ANAM , Harry Bhai pagal <br>
#     <a href= "https://www.youtube.com/watch?v=gfDE2a7MKjA">Visit this page</a>''')
#
# def about(request):
#     return HttpResponse("<h1>This is about! I am Bold</h1>")
# _______________________________________________________________________


# --> from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render

def indexes(request):
    # params = {'name':"Harry", 'video':"Youtube"}
    # return render(request,'index.html',params)
    # return HttpResponse("Home")
    return render(request, 'index.html')

def ex1(request):
    s = '''Navigation Bar <br> </h2>
    <a href= "https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9" > Django Code With Harry Bhai </a><br>
    <a href="https://www.facebook.com/"> Facebook </a> <br>
    <a href="https://www.flipkart.com/"> Flipkart </a> <br>
    <a href="https://www.hindustantimes.com/"> News </a> <br>
    <a href="https://www.google.com/"> Google </a> <br>'''
    return HttpResponse(s)

def analyze(request):
    # --> get text
    djtext = request.POST.get('text', 'default')
    # --> Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    # print(djtext)
    # print(removepunc)
    # print(fullcaps)
    # return HttpResponse("Remove Punc Remover <a href='/'>Back </a>")

    #-->Check which checkbox is on
    if(removepunc=='on'):
        # analyzed = djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(fullcaps=='on'):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Change to upper text', 'analyzed_text': analyzed}
        # -->Analyze the text
        return render(request, 'analyze.html', params)

    elif(newlineremover=='on'):
        analyzed=''
        for char in djtext:
            if char!='\n' and char!='\r':
                analyzed=analyzed+char
                print(analyzed)
        params={'purpose': 'Remove NewLines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(extraspaceremover=='on'):
        analyzed = ''
        for index,char in enumerate(djtext):
            if not (djtext[index]==' ' and djtext[index+1]==' '):
                analyzed = analyzed + char
        params = {'purpose': 'Remove NewLines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")

# def removepunc(request):
#     # get the text
#     djtext=request.GET.get('text','default')
#     print(djtext)
#     # analyze the text
#     return HttpResponse("Remove Punc Remover <a href='/'>Back </a>")
#
# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("new line remover")
#
# def spaceremove(request):
#     return HttpResponse("space remover")
#
# def charcount(request):
#     return HttpResponse("charcount")








