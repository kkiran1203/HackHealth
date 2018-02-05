from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello():
    #predictionModel()
    return render_template('index.html')

@app.route('/', methods=['POST'])
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
    """
    l = [('Age', [age]),
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
         ('mental_health_consequence', [PConsequence]),
         ('coworkers', [Coworkers]),
         ('supervisor', [Supervisor]),
         ('mental_health_interview', [MHEmployer]),
         ('physical_health_interview', [PHEmployer]),
         ('mental_vs_physical', [Seriously]),
         ('obs_consequence', [ObservedConsequences]),
         ('comments', [comment])
         ]

    #result = getPreditionForUser(l)
    """
    return age
if __name__ == "__main__":
    app.run()
