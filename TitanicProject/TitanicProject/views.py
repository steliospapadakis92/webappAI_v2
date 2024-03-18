from django.shortcuts import render
from . import fake_model
from . import ml_predict

def home(request):
    return render(request, 'index.html')

def result(request):
    #return render(request, 'result.html')

    # If we need to show that dictionary value to result.html that we put in the form. See name in index.html
    if request.method == 'POST':

        #Uncomment A, B or C

        #A. Use a fake model to print age:
        #user_input_age=int( request.POST.get("age_text") )
        #prediction=fake_model.fake_predict(user_input_age)
        #return render(request, 'result.html', {'prediction':prediction})

        #B. Use to print age:
        #user_input_age=request.POST.get("age_text") #to get and store the input in dictionary with the name age from index.html
        #user_input_age+=" is the word !!!"         #data manipulation
        #return render(request, 'result.html', {'age':user_input_age})


        #C. Use the ML model:
        pclass=int( request.POST.get("pclass") )
        sex=int( request.POST.get("sex") )
        age=int( request.POST.get("age") )
        sibsp=int( request.POST.get("sibsp") )
        parch=int( request.POST.get("parch") )
        fare=int( request.POST.get("fare") )
        embarked=int( request.POST.get("embarked") )
        title=int( request.POST.get("title") )

        prediction=ml_predict.prediction_model(pclass,sex,age,sibsp,parch,fare,embarked,title)
        return render(request, 'result.html', {'prediction':prediction})
    else:
        return render(request, 'result.html')
