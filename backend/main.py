from flask import Flask, request
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


@app.route('/determine-forms', methods=['POST'])
def determine_forms():
    """
    Function meant for determining what forms the client will receive.
    """

    # implementation

    #1. extracting data
    data = request.form.get('text_data')

    #2. similarity check with the data

    #3. returning the keys of the 3 most similar diagnosis(ex: cutoff for scores < value)

    # implementation


    pass

@app.route('/fetch-form', methods=['POST'])
def fetch_form():
    """
    Function meant for fetching the next form based on the id sent by the client.
    """

    #1. extracting data
    form_name = request.form.get('form_name')

    #2. getting & returning the questions from the form

    pass


@app.route('/fetch-diagnosis', methods=['POST'])
def fetch_diagnosis():
    """
    Function meant for sending user data to a LLM and returning this data back to the client.
    """

    #1. extracting data
    client_data = request.form.get('questions_data')


    #2. sending this data to external server


    #3. getting answer and returning it to user

    pass
        