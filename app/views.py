from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.

def insert_topic(request):
    tn = input("Enter topi name : ") # taking topi_name as input() from user

    #creating topic object with tn(topic name)
    #we are performing indexing because get_or_create() will return tuple (object, boolean_value) , we want only object
    TO =Topic.objects.get_or_create(topic_name = tn)[0]


    # saving the object
    TO.save()

    # finally returning a string after scucessfull cretion of topic object
    return HttpResponse('Topic object is created successfully')
    

def insert_webpage(request):
    tn = input("Enter topi name : ") # taking topi_name as input() from user , to create weppage object we need its parent object topic_name

    #creating topic object with tn(topic name)
    #we are performing indexing because get_or_create() will return tuple (object, boolean_value) , we want only object
    TO =Topic.objects.get_or_create(topic_name = tn)[0]

    # saving the object
    TO.save()

    name = input("Enter name : ") # taking name from user to create webpage object
    url  =input("Enter url : ") # taking url from user to create webpage object

    # creating webpage object with topic object and name and url variable
    #we are performing indexing because get_or_create() will return tuple (object, boolean_value) , we want only object
    WO = Webpage.objects.get_or_create(topic_name = TO, name = name , url = url)[0]
    # saving the object
    WO.save()

     # finally returning a string after scucessfull cretion of webpage object
    return HttpResponse('Webpage object is created successfully')

def insert_access(request):
    tn = input("Enter topi name : ") # taking topi_name as input() from user , to create weppage object we need its parent object topic_name

    #creating topic object with tn(topic name)
    #we are performing indexing because get_or_create() will return tuple (object, boolean_value) , we want only object
    TO =Topic.objects.get_or_create(topic_name = tn)[0]

    # saving the object
    TO.save()

    name = input("Enter name : ") # taking name from user to create webpage object
    url  =input("Enter url : ") # taking url from user to create webpage object

    # creating webpage object with Topic object(TO) and name and url variable
    #we are performing indexing because get_or_create() will return tuple (object, boolean_value) , we want only object
    WO = Webpage.objects.get_or_create(topic_name = TO, name = name , url = url)[0]
    # saving the object
    WO.save()
    
    date = input("Enter date : ") # taking date from user to create AccessRecord Object
    author = input("Enter author : ")# taking author from user to create AccessRecord Object
    
    # creating AccessRecord object with Webpage object(WO) and date and author variable
    #we are performing indexing because get_or_create() will return tuple (object, boolean_value) , we want only object
    AO= AccessRecord.objects.get_or_create(name = WO, date = date , author = author)[0]
    # saving the object
    AO.save()

    # finally returning a string after scucessfull cretion of AcsessRecord object
    return HttpResponse('AccessRecord object is created successfully')



