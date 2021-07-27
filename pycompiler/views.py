from sys import stdout
from typing import overload
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
import json
from .getcode import *
def compileCode(request):
    if request.method=='POST':
        import sys 
        from io import StringIO
        import contextlib
        print(request.POST.dtype())
        code=request.POST["code"]
        code=code.replace("input()","parameters")
        @contextlib.contextmanager
        def stdoutIO(stdout=None):
            old=sys.stdout
            if stdout is None:
                stdout=StringIO()
            sys.stdout=stdout
            yield stdout
            sys.stdout= old 
        with stdoutIO() as s:
            try:
                exec(code,{'parameters':request.POST["params"]})
            except Exception as e:
                print(e)
        from datetime import datetime as dt
        response={
            'time':dt.now(),
            'code':code,
            'response':s.getvalue()
        }
        return JsonResponse(response)
    else:
        response={
            'response':'Invalid Request',
        }
        return JsonResponse(response)
    
def code_form(request):
    if request.method=='POST':
        form=json.loads(compileCode(request).content)
        out={
            'form':form['response'],
            'flag':'hidden',
        }
    else:
        form=codeForm()
        out={
            'form':form,
            'flag':'',
        }
    
    return render(request,'codeexec.html',out)
        