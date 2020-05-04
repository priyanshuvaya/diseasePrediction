from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import UserRegister
from .models import User, Symptoms
from django.shortcuts import redirect
import pandas as pd
import csv
from collections import defaultdict
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier, export_graphviz
import numpy as np
import time
from sklearn.model_selection import train_test_split
import csv
from collections import defaultdict
from sklearn.metrics import accuracy_score

def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save()
            user.role = User.PATIENT
            user.date_of_birth = request.POST.get('date_of_birth')
            user.save()
            return redirect("/")
    else:
        form = UserRegister()
    return render(request,'registration/sign_up.html',{'form':form})

def index(request):
    symptoms = Symptoms.objects.all()
    symptoms.reverse()
    disease_list = []
    if request.method == "POST":
        symptom_list = request.POST.getlist('checks')
        final_array = []
        for symptom in symptoms:
            if symptom.name in symptom_list:
                final_array.append(1)
            else:
                final_array.append(0)
        for i in range(0,3):
            tempo = algoProcessing(final_array)

            disease_list.append(tempo[0])
        disease_list = set(disease_list)
        return render(request,'location.html',{"disease_list":disease_list})

    return render(request,'index.html',{"data":symptoms})

def dashboard(request):
    pass

def algoProcessing(final_array):
    print("hello world")
    data = pd.read_csv("H:\PROJECT2018-master\TrainingDisease.csv")
    df = pd.DataFrame(data)
    cols = df.columns
    cols = cols[:-1]
    x = df[cols]
    y = df['prognosis']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.6, random_state=42)
    test_data = pd.read_csv("TrainingDisease.csv")
    testx = test_data[cols]
    testy = test_data['prognosis']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.6, random_state=42)
    print ("DecisionTree")
    dt = DecisionTreeClassifier()
    clf_dt=dt.fit(x_train,y_train)
    output=clf_dt.predict([final_array])
    print(output)
    return output
