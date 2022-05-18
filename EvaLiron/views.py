from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.contrib import messages
import mysql.connector
import requests
from EvaLiron.models import User, Invitation
# Create your views here.
#db_connection = mysql.connector.connect(
#  host="localhost",
#  user="root",
#  database="db_wea")

#db_connection = mysql.connector.connect(
#    host="database-1.c4joaqwcqrpg.eu-central-1.rds.amazonaws.com",
#    user="admin",
#    password="okoklol123",
#    database=""
#)

#cursor = db_connection.cursor()
#print(db_connection)
# ====================|All Views Functions|==================== #
# ============================================================= #

#Index Page - return the first main page
def indexfr(request):
    return render(request,'index.html')

def indexhe(request):
    return render(request,'indexhe.html')

def contactfr(request):
    return render(request,'contact.html')

#def login(request):
#    return render(request,'login.html')

#def f_login(request):
#    if request.method=='POST':
#        v_idnumber=request.POST.get('username')
#        v_password=request.POST.get('password')
#        usercheck=User.objects.filter(username=v_idnumber,password=v_password)
#        allinvite1=Invitation.objects.all()
#        if usercheck:
#            return render(request ,'invitation.html', {"usercheck":usercheck, "allinvite1":allinvite1})
#    else :
#        messages.error(request,'Not correct, please try again!')   
#        return login(request)

#def f_addinvite(request):
#    if request.method == 'POST':
#        save_record=Invitation()
#        save_record.fname=request.POST.get('fname')
#        save_record.lname=request.POST.get('lname')
#        save_record.numinvite=request.POST.get('numinvite')
#        save_record.participate=request.POST.get('participate')
#        save_record.comment=request.POST.get('comment')
#        save_record.save()
#        return render(request, 'merci.html')
