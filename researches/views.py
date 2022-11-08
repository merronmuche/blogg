from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse
from researches.models import Research
from researches.forms import ResearchForm

# Create your views here.

def list(request):
    my_researches= Research.objects.all().values()
    content = {
        'my_researches' : my_researches
    }
    return render(request,'research/list.html',content)

def detail(request,id):
    selected_research=Research.objects.get(id=id)
    content = {
         'selected_research': selected_research
    }
    return render(request = request, template_name= 'research/detail.html',context = content)

def add(request):

    if request.method == 'GET':
        form = ResearchForm()
        context = {
            'form': form
        }

        return render(request,'research/create.html', context)

    else:

        form = ResearchForm(request.POST)

        if form.is_valid():
            Research = form.save()
            return redirect(reverse('list'))

