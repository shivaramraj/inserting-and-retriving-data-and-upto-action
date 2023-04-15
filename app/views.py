from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.
def Insert_topic(request):
    if request.method=='POST':
        tn=request.POST['un']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('data inserted sucessfully')


    return render(request,'insert_topic.html')

def Insert_webpages(request):
    TO=Topic.objects.all()
    d={'topics':TO}
    if request.method=='POST':
        tname=request.POST['topic']
        wname=request.POST['name']
        wurl=request.POST['url']
        wemail=request.POST['email']
        TO=Topic.objects.get(topic_name=tname)[0]
        WO=WebPages.objects.create(topic_name=TO,name=wname,url=wurl,email=wemail)
        WO.save()
        return HttpResponse('inserted data sucessfully into webpages')
    return render(request,'insert_webpages.html',d)
def Insert_Access_Record(request):
    WO=WebPages.objects.all()
    d={'webpages':WO}
    if request.method=='POST':
        Aname=request.POST['Aname']
        Aauther=request.POST['Aauther']
        Adate=request.POST['Adate']
        WO=WebPages.objects.get(name=Aname)
        AO=AcessRecord.objects.create(name=WO,auther=Aauther,date=Adate)
        AO.save()
        return HttpResponse('inserted data into accessrecord sucessfully')
    return render(request,'insert_access.html',d)
def retrieve_data(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}
    if request.method=='POST':
        td=request.POST.getlist('topic')
        print(td)
        webqueryset=WebPages.objects.none()

        for i in td:
            webqueryset=webqueryset|WebPages.objects.filter(topic_name=i)
        d1={'webpages':webqueryset}
        return render(request,'displaywebpages.html',d1)
    return render(request,'selecttopics.html',d)