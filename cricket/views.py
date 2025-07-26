from django.shortcuts import HttpResponse
from django.template import loader
from .models import players

# Create your views here.

def cricket(request):
    mymembers=players.objects.all().values()
    template=loader.get_template('all.players.html')
    context={"mymembers":mymembers,
             }
    return HttpResponse(template.render(context,request))

def details(request,id):
    mymember=players.objects.get(id=id)
    template=loader.get_template('details.html')
    context={
        'mymember':mymember,
    }
    return HttpResponse(template.render(context,request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
 
  template = loader.get_template('template.html')
  context = {
     'fruits': ['Apple', 'Banana', 'Cherry'],   

  }
  return HttpResponse(template.render(context, request))