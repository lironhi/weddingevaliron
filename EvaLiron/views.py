from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.contrib import messages
import mysql.connector
import requests
# Create your views here.

# ====================|All Views Functions|==================== #
# ============================================================= #

#Index Page - return the first main page
def indexfr(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')
