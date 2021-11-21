from django.shortcuts import render
from django.http import JsonResponse
from . import compile
from datetime import datetime
from uuid import uuid4

SUPPORTED_LANGUAGES = {'Python','C++','Java','C'}

def genId():
    with open('id.txt','r') as file:
        d = file.read()
        if d is None or d[0]=='':
            d=0
        if int(d)>=5:
            d=0
    with open('id.txt','w') as file:
        file.write(str(int(d)+1))
    return str(int(d)+1)

# Create your views here.
def home(request):
    if request.method == 'GET':
        return render(request,'home.html',{'langs':SUPPORTED_LANGUAGES})
    elif request.method == 'POST':
        values = dict(request.POST)
        id = genId()
        out = compile.main(values['code'][0],values['language'][0],id=id,arguments=values['args'][0])
        val = {
            'response':out
        }
        print(val)
        return JsonResponse(val)

