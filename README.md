# hackHealth2018
Mental Health Survey

## Introduction:
Mental illness is one of the most serious diseases currently being faced by 300,000 people per year in our society. 
With proper care and attention, a serious and dangerous disease can also be cured. Here we are presenting a web application using Machine Learning algorithms to determine whether you require an assistance/care for your good mental health through a brief survey.

## Specifications:
1.Data Set used - Mental health in tech survey in Kaggle

2.Programming Languages used - Python

3.ML Libraries - scikit-learn

4.Scripting languages used - HTML,CSS

5.UI/UX Python library used - Flask

6.Tools used - Pycharm

## Steps to Install:
1. Download the FlaskApp directory
2. Run the following command on the terminal

python app.py

3. Open "http://localhost:5000/" on your favorite web browser.

## Details:
1.The project started with importing a csv file which consisted the survey of more than 1200 people in their tech industry. The data was cleaned and preprocessed and was later divided for testing and training purpose.

2.The next phase was creating a model which can efficiently predict whether the person requires treatment based on the survey. The various classification algorithms used were Logistic Regression, SVM and Bagging model. 

3.Based on the K-cross validation results, we chose Logistic regression as our base model to decide on the survey results.The accuracy given by Logistic regression was 71.18%.

4.Once the modeling was done, we moved towards building the front end of the web page which included a survey page as well as the suggestion page, which possibly gives you the attributes behind your mental illness. 

5.The front end was designed primarily using the Flask python library and was designed using HTML and CSS. There were 25 attributes based on which the user's survey results were determined. Depending upon the results,  we determine whether the user requires an assistance or not,  if it requires assistance, then we redirect the user to the specific supportive page or else the user was given a positive lookout.

6.Once the front end was designed the python models were integrated with the front end using function module class. 

7.The last stage included the designing of a suggestion page, which generates various charts giving you a possible glimpse of the reason behind your illness.
