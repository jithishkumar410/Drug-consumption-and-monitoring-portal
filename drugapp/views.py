from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404
from .models import Complaint,Alerts,CriminalDetails,Coma
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm
from django.shortcuts import render

def bas(request):
    return render(request,'base.html')

def adetails(request):
    a=CriminalDetails.objects.filter(private=False)
    return render(request,'wanted.html',{'a':a})

def acom(request,id):
    if request.method == 'POST':
        info = request.POST.get('info') 
        name = request.POST.get('name')
        mobile_number = request.POST.get('no')
        lat = request.POST.get('lat')
        lon = request.POST.get('lon')
        clat = request.POST.get('clat')
        clon = request.POST.get('clon')
        acom = Coma(
            info=info,
            aid=id,
            name=name,
            mobile_number=mobile_number,
            lat=lat,
            lon=lon,
            clat=clat,
            clon=clon,
        )
       
        acom.save()
        messages.success(request,"Thanks for your Contibution :)")
        return redirect('aw')
    
    b=CriminalDetails.objects.filter(crimeid=id)
    
    return render(request,'aqcom.html',{'a':id,'b':b[0]})
    

def poldash(request):
    if request.user.is_authenticated:
        a=Complaint.objects.filter(viewed=False)
        b=Alerts.objects.filter(viewed=False)
        c=Complaint.objects.all()
        d=Alerts.objects.all()
        e=Coma.objects.all()
        return render(request,'pd.html',{'a':len(a),'b':len(b),'c':c,'d':d,'e':len(e)})
    messages.warning(request,"You are not permitted to access that page :(")
    return redirect('base')

def acform(request):
    if request.method == 'POST':
        complaint_text = request.POST.get('Complainttext')
        email = request.POST.get('email')
        uploaded_file = request.FILES.get('file')  
        name = request.POST.get('name')
        mobile_number = request.POST.get('no')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        new_complaint = Complaint(
            complaint_text=complaint_text,
            email=email,
            file= uploaded_file,
            name=name,
            mobile_number=mobile_number,
            latitude=latitude,
            longitude=longitude
        )
       
        new_complaint.save()
        messages.success(request,"Thanks for your Contibution :)")
        return redirect('base')

    return render(request, 'acform.html')

def alform(request):
    if request.method == 'POST':
        atext = request.POST.get('at')
        lat = request.POST.get('latitude')
        lon = request.POST.get('longitude')
        print(atext)
        new_alert = Alerts(
            alertText=atext,
            alertby=request.user.username,
            lat=lat,
            lon=lon
        )
       
        new_alert.save()
        messages.success(request,"Alert message is submitted!")
        return redirect('poldash')

    return render(request, 'alform.html')

def pollog(request):
    if request.method == 'GET':
            form = LoginForm()
            return render(request, 'pollog.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            userID = form.cleaned_data['userID']
            password = form.cleaned_data['password']
            user = authenticate(request,username=userID,password=password)
            if user:
                login(request, user)
                messages.success(request,f'Hi {userID.title()}, welcome!')
                return redirect('poldash')
        
        
        messages.error(request,f'Invalid username or password :(')
        return render(request,'pollog.html',{'form': form})
def Logout(request):
    logout(request)
    messages.success(request,f'Logout.')
    return redirect('base')    

def complaint(request):
    a=Complaint.objects.all()[::-1]
    
    return render(request,'complaints.html',{'f':a})
def viecom(request,id):
    a = get_object_or_404(Complaint, cid=id)
    a.viewed = True
    a.save()
    return render(request,'viewcom.html',{'f':a})

def alertmsg(request):
    a=Alerts.objects.all()[::-1]
    return render(request,'alertmsg.html',{'f':a})

def viewalert(request,id):
    a = get_object_or_404(Alerts, aid=id)
    a.viewed = True
    a.save()
    return render(request,'viewalert.html',{'f':a})

def wanv(request):
    a=CriminalDetails.objects.all()
    return render(request,'polwant.html',{'a':a})

def vwancom(request,id):
    a=CriminalDetails.objects.filter(crimeid=id)
    b=Coma.objects.filter(aid=id)
    return render(request,'vwancom.html',{'a':a,'b':b[::-1]})

def vwan(request,id):
    b = get_object_or_404(Coma, acomid=id)
    b.viewed = True
    b.save()
    return render(request,'vwan.html',{'b':b,'a':id})

def survey(request):
    return render(request,'surway.html')

def maln(request):
    return render(request,'maln.html')

def socwor(request):
    return render(request,'index.html')

