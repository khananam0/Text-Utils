# --> from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render

def indexes(request):
    return render(request, 'index.html')

def analyze(request):
    # --> get text
    djtext = request.POST.get('text', 'default')
    # --> Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    # -->Check which checkbox is on
    if(removepunc=='on'):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed

    if(fullcaps=='on'):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Change to upper text', 'analyzed_text': analyzed}
        djtext=analyzed

    if(newlineremover=='on'):
        analyzed = ''
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed+char
                print(analyzed)
        params = {'purpose': 'Remove NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if(extraspaceremover=='on'):
        analyzed = ''
        for index, char in enumerate(djtext):
            if not (djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed = analyzed + char
        params = {'purpose': 'Remove Extra Spaces', 'analyzed_text': analyzed}

    if(removepunc!='on' and (fullcaps!='on') and (newlineremover!='on') and (extraspaceremover!='on')):
        return HttpResponse('Please Select any operation and TRY AGAIN LATER')


    return render(request, 'analyze.html', params)






