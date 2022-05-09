from ast import Break
from django.shortcuts import render
from .models import *
from .forms import *
from django.db.models import Sum
from django.http.response import HttpResponseRedirect
from django.urls import reverse



# Create your views here.
def home(request):
    form = PUForm()
    PU = None
    if request.method == 'POST':        
        form = PUForm(request.POST)                                         
        
        if form.is_valid():
            PUname = form.cleaned_data.get('polling_unit_id')
            PUid = PUname.uniqueid
            PU = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=PUid)
    context = {"form":form, 'PUs':PU}
    return render(request,"Election/home.html",context)

def index(request):

    return render(request, "Election/landing_page.html")

def LGA_result(request):
    form = Lgaform()
    LG = None
    party_names = list(Party.objects.values_list("partyname",flat=True))
    total = []
    if request.method == 'POST': 
        form = Lgaform(request.POST) 
                                                 
        
        if form.is_valid():
            LGname = form.cleaned_data.get('lga_id')
            LGid = LGname.lga_id
            LG = AnnouncedPuResults.objects.filter(polling_unit_uniqueid__lga_id=LGid )   
            
            for i in party_names:
                party = LG.filter(party_abbreviation=i)
                party = party.aggregate(Sum('party_score'))['party_score__sum']
                total.append(party)

    context = {"form":form,'sum':total, 'party_names':party_names}


    return render(request, "Election/LGA_result.html", context)

def New_PU(request):
    form = NewPUForm()
    if request.method == 'POST':        
        form = PUForm(request.POST)                                         
        
        if form.is_valid():        
           form.save()
           return HttpResponseRedirect(reverse("index"))

    context = {'form':form}
    return render(request, 'Election/New_PU_page.html', context)