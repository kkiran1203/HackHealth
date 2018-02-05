import numpy as np
import pandas as pd

from subprocess import check_output
#print(check_output(["ls", "survey.csv"]).decode("utf8"))

from sklearn.preprocessing import LabelEncoder
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve
from sklearn.model_selection import validation_curve
le = LabelEncoder()

from flask import Flask, render_template, request

app = Flask(__name__)


#################################################
clf = ""
df = ""
def predictionModel():
    global df
    df = pd.read_csv('survey.csv')

    def dataCleaning():
        '''df.family_history = le.fit_transform(df.family_history)
        df.mental_health_consequence = le.fit_transform(df.mental_health_consequence)
        df.phys_health_consequence = le.fit_transform(df.phys_health_consequence)
        df.coworkers = le.fit_transform(df.coworkers)
        df.supervisor = le.fit_transform(df.supervisor)
        df.mental_health_interview = le.fit_transform(df.mental_health_interview)
        df.phys_health_interview = le.fit_transform(df.phys_health_interview)
        df.mental_vs_physical = le.fit_transform(df.mental_vs_physical)
        df.obs_consequence = le.fit_transform(df.obs_consequence)
        df.remote_work = le.fit_transform(df.remote_work)
        df.tech_company = le.fit_transform(df.tech_company)
        df.benefits = le.fit_transform(df.benefits)
        df.care_options = le.fit_transform(df.care_options)
        df.wellness_program = le.fit_transform(df.wellness_program)
        df.seek_help = le.fit_transform(df.seek_help)
        df.anonymity = le.fit_transform(df.anonymity)'''

        df.loc[df['work_interfere'].isnull(),['work_interfere']]=0
        df['self_employed'].fillna('Don\'t know',inplace=True)
        #df.self_employed = le.fit_transform(df.self_employed)
        df['self_employed'].replace(['Yes', 'No', 'Don\'t know'],
                                    [1, 2, 3], inplace=True)
        df.loc[df['comments'].isnull(),['comments']]=0
        df.loc[df['comments']!=0,['comments']]=1
        df['family_history'].replace(['Yes', 'No'],
                            [1, 2], inplace=True)
        df['mental_health_consequence'].replace(['Yes', 'No','Maybe'],
                                     [1, 2, 3], inplace=True)
        df['phys_health_consequence'].replace(['Yes', 'No', 'Maybe'],
                                                [1, 2, 3], inplace=True)
        df['coworkers'].replace(['Yes', 'No', 'Some of them'],
                                              [1, 2, 3], inplace=True)
        df['supervisor'].replace(['Yes', 'No', 'Some of them'],
                                [1, 2, 3], inplace=True)
        df['mental_health_interview'].replace(['Yes', 'No', 'Maybe'], [1, 2, 3], inplace=True)
        df['phys_health_interview'].replace(['Yes', 'No', 'Maybe'], [1, 2, 3], inplace=True)
        df['mental_vs_physical'].replace(['Yes', 'No','Don\'t know'], [1, 2,3], inplace=True)
        df['remote_work'].replace(['Yes', 'No'],
                                     [1, 2], inplace=True)
        df['obs_consequence'].replace(['Yes', 'No'],
                                  [1, 2], inplace=True)
        df['tech_company'].replace(['Yes', 'No'],
                                     [1, 2], inplace=True)
        df['anonymity'].replace(['Yes', 'No', 'Don\'t know'],
                                [1, 2, 3], inplace=True)
        df['wellness_program'].replace(['Yes', 'No', 'Don\'t know'],
                                        [1, 2, 3], inplace=True)
        df['seek_help'].replace(['Yes', 'No', 'Don\'t know'],
                                 [1, 2, 3], inplace=True)
        df['care_options'].replace(['Yes', 'No', 'Not sure'],
                                    [1, 2, 3], inplace=True)
        df['benefits'].replace(['Yes', 'No', 'Don\'t know'],
                                [1, 2, 3], inplace=True)
        df['leave'].replace(['Very easy', 'Somewhat easy', "Don\'t know", 'Somewhat difficult', 'Very difficult'],
                             [1, 2, 3, 4, 5],inplace=True)
        df['work_interfere'].replace(['Never','Rarely','Sometimes','Often'],[1,2,3,4],inplace=True)
        df.loc[df['Gender'].str.contains('F|w', case=False,na=False),'Gender']=2
        df.loc[df['Gender'].str.contains('queer/she',case=False,na=False),'Gender']=1
        df.loc[df['Gender'].str.contains('male leaning',case=False,na=False),'Gender']=-1
        df.loc[df['Gender'].str.contains('something kinda male',case=False,na=False),'Gender']=-1
        df.loc[df['Gender'].str.contains('ish',case=False,na=False),'Gender']=-1
        df.loc[df['Gender'].str.contains('m',case=False,na=False),'Gender']=-2
        df.loc[df['Gender'].str.contains('',na=False),'Gender']=0
        df.loc[df['no_employees']=='1-5',['no_employees']]=1
        df.loc[df['no_employees']=='6-25',['no_employees']]=2
        df.loc[df['no_employees']=='26-100',['no_employees']]=3
        df.loc[df['no_employees']=='100-500',['no_employees']]=4
        df.loc[df['no_employees']=='500-1000',['no_employees']]=5
        df.loc[df['no_employees']=='More than 1000',['no_employees']]=6

    dataCleaning()

    def prepareData():
        global df
        drop_elements = ['Timestamp', 'Country', 'state', 'work_interfere']
        df = df.drop(drop_elements, axis=1)

    prepareData()
    global clf
    X = df.drop(['treatment'], axis=1)
    X = X.drop(['Age'], axis=1)
    y = df['treatment']
    y = le.fit_transform(y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)
    stdsc = StandardScaler()
    #X_train_std = stdsc.fit_transform(X_train)
    #X_test_std = stdsc.fit_transform(X_test)

    clf = LogisticRegression(C=0.01).fit(X_train, y_train)
    y_true, y_pred = y_test, clf.predict(X_test)

def getPreditionForUser(l):
    df_test = pd.DataFrame.from_items(l)

    def cleanTestData(df):

        '''df.family_history = le.fit_transform(df.family_history)
        df.mental_health_consequence = le.fit_transform(df.mental_health_consequence)
        df.phys_health_consequence = le.fit_transform(df.phys_health_consequence)
        df.coworkers = le.fit_transform(df.coworkers)
        df.supervisor = le.fit_transform(df.supervisor)
        df.mental_health_interview = le.fit_transform(df.mental_health_interview)
        df.phys_health_interview = le.fit_transform(df.phys_health_interview)
        df.mental_vs_physical = le.fit_transform(df.mental_vs_physical)
        df.obs_consequence = le.fit_transform(df.obs_consequence)
        df.remote_work = le.fit_transform(df.remote_work)
        df.tech_company = le.fit_transform(df.tech_company)
        df.benefits = le.fit_transform(df.benefits)
        df.care_options = le.fit_transform(df.care_options)
        df.wellness_program = le.fit_transform(df.wellness_program)
        df.seek_help = le.fit_transform(df.seek_help)
        df.anonymity = le.fit_transform(df.anonymity)'''

        df['self_employed'].fillna('Don\'t know', inplace=True)
        #df.self_employed = le.fit_transform(df.self_employed)
        df['self_employed'].replace(['Yes', 'No','Don\'t know'],
                                     [1, 2,3], inplace=True)
        df.loc[df['comments'].isnull(),['comments']] = 0
        df.loc[df['comments'] != 0, ['comments']] = 1
        df['family_history'].replace(['Yes', 'No'],
                                     [1, 2], inplace=True)
        df['mental_health_consequence'].replace(['Yes', 'No', 'Maybe'],
                                                [1, 2, 3], inplace=True)
        df['phys_health_consequence'].replace(['Yes', 'No', 'Maybe'],
                                              [1, 2, 3], inplace=True)
        df['coworkers'].replace(['Yes', 'No', 'Some of them'],
                                [1, 2, 3], inplace=True)
        df['supervisor'].replace(['Yes', 'No', 'Some of them'],
                                 [1, 2, 3], inplace=True)
        df['mental_health_interview'].replace(['Yes', 'No', 'Maybe'], [1, 2, 3], inplace=True)
        df['phys_health_interview'].replace(['Yes', 'No', 'Maybe'], [1, 2, 3], inplace=True)
        df['mental_vs_physical'].replace(['Yes', 'No','Don\'t know'], [1, 2,3], inplace=True)
        df['remote_work'].replace(['Yes', 'No'],
                                  [1, 2], inplace=True)
        df['obs_consequence'].replace(['Yes', 'No'],
                                      [1, 2], inplace=True)
        df['tech_company'].replace(['Yes', 'No'],
                                   [1, 2], inplace=True)
        df['anonymity'].replace(['Yes', 'No', 'Don\'t know'],
                                [1, 2, 3], inplace=True)
        df['wellness_program'].replace(['Yes', 'No', 'Don\'t know'],
                                       [1, 2, 3], inplace=True)
        df['seek_help'].replace(['Yes', 'No', 'Don\'t know'],
                                [1, 2, 3], inplace=True)
        df['care_options'].replace(['Yes', 'No', 'Not sure'],
                                   [1, 2, 3], inplace=True)
        df['benefits'].replace(['Yes', 'No', 'Don\'t know'],
                               [1, 2, 3], inplace=True)
        df['leave'].replace(['Very easy', 'Somewhat easy', "Don\'t know", 'Somewhat difficult', 'Very difficult'],
                            [1, 2, 3, 4, 5], inplace=True)
        df.loc[df['Gender'].str.contains('F|w', case=False, na=False), 'Gender'] = 2
        df.loc[df['Gender'].str.contains('queer/she', case=False, na=False), 'Gender'] = 1
        df.loc[df['Gender'].str.contains('male leaning', case=False, na=False), 'Gender'] = -1
        df.loc[df['Gender'].str.contains('something kinda male', case=False, na=False), 'Gender'] = -1
        df.loc[df['Gender'].str.contains('ish', case=False, na=False), 'Gender'] = -1
        df.loc[df['Gender'].str.contains('m', case=False, na=False), 'Gender'] = -2
        df.loc[df['Gender'].str.contains('', na=False), 'Gender'] = 0
        df.loc[df['no_employees'] == '1-5', ['no_employees']] = 1
        df.loc[df['no_employees'] == '6-25', ['no_employees']] = 2
        df.loc[df['no_employees'] == '26-100', ['no_employees']] = 3
        df.loc[df['no_employees'] == '100-500', ['no_employees']] = 4
        df.loc[df['no_employees'] == '500-1000', ['no_employees']] = 5
        df.loc[df['no_employees'] == 'More than 1000', ['no_employees']] = 6
        print df.loc[0]

        return df
    global clf
    df_test = cleanTestData(df_test)
    stdsc = StandardScaler()
    #df_test_std = stdsc.fit_transform(df_test)
    pred = clf.predict( df_test )
    return pred
predictionModel()
###########################################################

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/', methods=['POST','GET'])
def my_form_post():
    #name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    #country = request.form['country']
    #state = request.form['state']
    se = request.form['se']
    fh = request.form['fh']
    enum = request.form['enum']
    r = request.form['r']
    tech = request.form['tech']
    mhb = request.form['mhb']
    mhc = request.form['mhc']
    dmh = request.form['dmh']
    rmh = request.form['rmh']
    p = request.form['p']
    easyLeave = request.form['easyLeave']
    MConsequence = request.form['MConsequence']
    PConsequence = request.form['PConsequence']
    Coworkers = request.form['Coworkers']
    Supervisor = request.form['Supervisor']
    MHEmployer = request.form['MHEmployer']
    PHEmployer = request.form['PHEmployer']
    Seriously = request.form['Seriously']
    ObservedConsequences = request.form['ObservedConsequences']
    comment = request.form['message']
    comment=comment.strip()
    if len(comment)==0:
        comment= None

    l = [#('Age', [age]),
         ('Gender', [gender]),
         ('self_employed', [se]),
         ('family_history', [fh]),
         ('no_employees', [enum]),
         ('remote_work', [r]),
         ('tech_company', [tech]),
         ('benefits', [mhb]),
         ('care_options', [mhc]),
         ('wellness_program', [dmh]),
         ('seek_help', [rmh]),
         ('anonymity', [p]),
         ('leave', [easyLeave]),
         ('mental_health_consequence', [MConsequence]),
         ('phys_health_consequence', [PConsequence]),
         ('coworkers', [Coworkers]),
         ('supervisor', [Supervisor]),
         ('mental_health_interview', [MHEmployer]),
         ('phys_health_interview', [PHEmployer]),
         ('mental_vs_physical', [Seriously]),
         ('obs_consequence', [ObservedConsequences]),
         ('comments', [comment])
         ]

    result = getPreditionForUser(l)
    print l
    print result

    if result[0] == 1:
        return render_template('Results.html')
    else :
        #return render_template('Results.html')
        return render_template('Results1.html')




if __name__ == "__main__":
    app.run()