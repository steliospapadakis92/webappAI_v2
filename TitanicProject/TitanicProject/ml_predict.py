def prediction_model(pclass,sex,age,sibsp,parch,fare,embarked,title):
    import pickle
    #import joblib
    x=[[pclass,sex,age,sibsp,parch,fare,embarked,title]]
    #randomforest = joblib.load('titanic_model.sav')
    randomforest=pickle.load(open('titanic_model.sav','rb'))
    prediction=randomforest.predict(x)

    if prediction==0:
        prediction='Person not survived'
    elif prediction==1:
        prediction='Person survived'
    else:
        prediction='Error'

    return prediction
