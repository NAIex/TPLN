from flask import Flask

from classes.Questionnaire import Questionnaire
from classes.questions.data import questions_by_subscale
from classes.Gender import Gender

app = Flask(__name__)
questionnaire = Questionnaire(questions_by_subscale,Gender.M)
questions = []
for _, question_pack in questionnaire.questions_by_subscale.items():
    questions = questions.__add__(question_pack)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"   


@app.route('/start')
def start():
    
    start_questions = []

    start_questions.append(questionnaire.questions_by_subscale['Tulburare depresivă majoră'][0].text)
    start_questions.append(questionnaire.questions_by_subscale['Tulburare de stres posttraumatic'][4].text)
    start_questions.append(questionnaire.questions_by_subscale['Bulimie/Alimentație compulsivă'][1].text)
    start_questions.append(questionnaire.questions_by_subscale['Tulburare obsesiv-compulsivă'][2].text)
    start_questions.append(questionnaire.questions_by_subscale['Tulburare de panică'][3].text)
    start_questions.append(questionnaire.questions_by_subscale['Tulburări psihotice'][0].text)
    start_questions.append(questionnaire.questions_by_subscale['Agorafobie'][0].text)
    start_questions.append(questionnaire.questions_by_subscale['Fobie socială'][3].text)
    start_questions.append(questionnaire.questions_by_subscale['Abuz/dependență de alcool'][4].text)
    start_questions.append(questionnaire.questions_by_subscale['Abuz/dependență de medicamente'][4].text)
    start_questions.append(questionnaire.questions_by_subscale['Tulburare de anxietate generalizată'][3].text)
    start_questions.append(questionnaire.questions_by_subscale['Tulburare de somatizare'][0].text)
    start_questions.append(questionnaire.questions_by_subscale['Ipohondrie'][3].text)


    return start_questions
