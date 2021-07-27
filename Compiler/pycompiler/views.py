from json.encoder import JSONEncoder
from sys import stdout
from typing import overload
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .getcode import * 

def get_code(request):
    if request.method=='POST':
        import sys 
        from io import StringIO
        import contextlib
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
            'params':request.POST["params"],
            'output':s.getvalue()
        }
        return JsonResponse(response)
    else:
        return render(request,'codeexec.html',{'form':codeForm()})
        