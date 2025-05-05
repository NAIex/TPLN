from flask import Flask

from classes.Gender import Gender
from classes.questions.data import questions_by_subscale

from flask_cors import CORS


app = Flask(__name__)

CORS(app)

questions = []
for _, question_pack in questions_by_subscale.items():
    questions += question_pack


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"   


@app.route('/start')
def start():
    gender = Gender.M
    
    start_questions = [e.json for e in [
        questions_by_subscale['Tulburare depresivă majoră'][0],
        questions_by_subscale['Tulburare de stres posttraumatic'][4],
        questions_by_subscale['Bulimie/Alimentație compulsivă'][1],
        questions_by_subscale['Tulburare obsesiv-compulsivă'][2],
        questions_by_subscale['Tulburare de panică'][3],
        questions_by_subscale['Tulburări psihotice'][0],
        questions_by_subscale['Agorafobie'][0],
        questions_by_subscale['Fobie socială'][3],
        questions_by_subscale['Abuz/dependență de alcool'][4],
        questions_by_subscale['Abuz/dependență de medicamente'][4],
        questions_by_subscale['Tulburare de anxietate generalizată'][3],
        questions_by_subscale['Tulburare de somatizare'][0],
        questions_by_subscale['Ipohondrie'][3],
    ]]

    return start_questions
