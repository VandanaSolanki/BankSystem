from django.shortcuts import render,HttpResponse
# import requests
# import sys
# from subprocess import run, PIPE
# from even import evenodd
# Create your views here.
def button(request):
    return render(request, 'home.html')

def external(request):
    # a=evenodd()
    # a.external()
    
    inp=request.POST.get('input1')
    if int(inp)%2==0:
        out="Even"
    else:
        out="Odd"
    # out=run(sys.executable,external(),shell=False,stdout=PIPE)
    print(out)
    return render(request, 'home.html', {'data1':out})
