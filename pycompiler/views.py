from sys import stdout
from typing import overload
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .getcode import codeForm
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
        form=s.getvalue()
    else:
        form=codeForm()
        
    return render(request,'codeexec.html',{'form':form})
        