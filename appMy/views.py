from django.shortcuts import render
from .models import *
import datetime
from django.db.models import Count

def index(request):
    
    depature=Airways_depture.objects.all()
    flight = Flight.objects.all()
    arrive=Airways_arrive.objects.all()
   
        
           
    context={
         "depature":depature,
         "flight":flight,
         "arrive":arrive
    }
    return render(request,'index.html',context)


def ticket(request):
    myBtn=request.POST.get("submit")


    if request.method=="POST":
            if myBtn=="flight-submit":
                nereden=request.POST.get("nereden")
                nereye=request.POST.get("varis")
                kalkis_date=request.POST.get("kalkis")
                yetiskin=request.POST.get("yetiskin")
                cocuk=request.POST.get("cocuk")
                variş_date=request.POST.get("varis")
                if  Flight.objects.filter(depeture_place__name=nereden).exists():
                    if Flight.objects.filter(arrive_place__name=nereye).exists():
                        if Flight.objects.filter(time=kalkis_date).exists():
                                flights=Flight.objects.filter(time=kalkis_date,depeture_place__name=nereden,arrive_place__name=nereye)
                                flights.update(adult=yetiskin,child=cocuk);
                                context={
                                        "flights":flights,
                                                }
                                return render(request,'ticket.html',context)
                        else:
                                hata="Bu tarih de bir uçuşumuz yoktur"
                                context={
                                "hata":hata,
                                }
                                return render(request,'ticket.html',context)
                    else:
                        hata="öyle  uçuşumuz yok"
                        context={
                            "hata":hata,
                        }
                        return render(request,'ticket.html',context)         
                    
                else:
                    hata="öyle  uçuşumuz yok"
                    context={
                            "hata":hata,
                        }
                    return render(request,'ticket.html',context)
            else:
                hata="Bu tarih de bir uçuşumuz yoktur"
                context={
                            "hata":hata,
                            }
                return render(request,'ticket.html',context)
 
    else:
        hata="Bu tarih de bir uçuşumuz yoktur"
        context={
                            "hata":hata,
                            }
        return render(request,'ticket.html',context)
 
         
            

def ticketId(request,id):
    flight=Flight.objects.get(id=id);
    
    context={
          "flight":flight,
         
     }
    return render(request,'ticketId.html',context)

def getTurkey(request):
     flight=Flight.objects.all()
     context={
          "flight":flight
     }
     return render(request,'flightTurkey.html',context)


def cartFlight(request,id):
    flight=Flight.objects.get(id=id);
    
    context={
          "flight":flight,
         
     }
   
    return render(request,'cart.html',context)