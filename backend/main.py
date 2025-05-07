from flask import Flask, request
from classes.Gender import Gender
from classes.questions.data import questions_by_subscale
from classes.SubscaleSelector import select_next_subscale

from flask_cors import CORS

import cohere
from similarity_check import check_similarity

app = Flask(__name__)
co = cohere.Client(open('key.txt','r').readline())

CORS(app)

@app.route('/start')
def start(): return "lol" #I sincerely have no idea what the purpose of this is (maybe send the introductory question?)

@app.route('/next-form', methods=['POST'])
def next_form():
    first_text = request.json.get("text_data", "") # should be assigned the value of the introductory text from the frontend
    print(first_text)
    answers_by_subscale = request.json.get("questions_data", {}) # should be assigned the value of the form answers from the frontend
    # the frontend form answers should look the following way:
    # before completing any forms: {}
    # completing only the suicide form: {"Tulburare depresivă majoră": {...}}
    # completing the suicide form and the anxiety form: {"Tulburare depresivă majoră": {...}, "Tulburare de anxietate generalizată": {...}}
    # i'm open to suggestions if you think this should change aka flatten the inner dictionaries like:
    # before completing any forms: {}
    # completing only the suicide form: {1: True, 2: True, 3: False, ...}
    # completing the suicide form and the anxiety form: {1: True, 2: True, 3: False, ..., 92: "js pop a cig to mellow yourself", 93: False}
    subscale = select_next_subscale(first_text, answers_by_subscale)
    qs = questions_by_subscale[subscale]
    return {"form_section":subscale, "items":[q.json for q in qs]}

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

'''
 temp = f"""[INST] You are a mental health assistant. Your task is to determine wether a person suffers from a mental problem, given a context.
        Context: {context}

  """
  temp += """Use the context from above to determine the diagnosis based on the feelings of the user from below. The answer should be detailed and in Romanian.
          The feelings: {question}

        Your Answer:[/INST]
        """
'''

@app.route('/fetch-diagnosis', methods=['POST'])
def fetch_diagnosis():
    global psychiatric_templates
    """
    Function meant for sending user data to a LLM and returning this data back to the client.
    """

    #1. extracting data
    client_data = request.json.get('questions_data')
    most_similar = check_similarity(client_data)

    context = '\n'.join(psychiatric_templates[most_similar])

    prompt = f"""

    ## Instructions
    Using the possible diagnosis, possible feelings and the input feelings determine if the user has the diagnosis or not.
    Start the response with Da or Nu, depending on if you think they need medical consulting or not.

    
    DETAIL WHY YOU'VE GIVEN THE ANSWER NU OR DA.
    ANSWER ONLY IN ROMANIAN.


    ## Possible Diagnosis
    {most_similar}

    ## Possible Feelings
    {context}

    ## Input Text
    {client_data}


"""
    '''
    prompt = f"""Esti un asistent medical pentru bunastarea mentala. Scopul tau este sa ajuti omul sa isi dea seama daca sufera de o boala mentala sau nu in functie de urmatorul posibil diagnostic posibil.
    Diagnostic: {context}
    """
    prompt += f"""Foloseste diagnosticul de mai sus si sentimentele de mai jos pentru a determina daca are nevoie de un control medical. Incepe raspunsul prin Da sau Nu si dupa detaliaza daca nevoie sa consulte un specialist sau nu. Answer in Romanian.
          Sentimentele:
        """
    '''

    #2. sending this data to external server
    response = co.generate(
        model='command-r-plus',
        prompt=prompt,
        max_tokens=1000,
        temperature=0.7
    )
    print(response.generations[0].text)
    #3. getting answer and returning it to user
    return [response.generations[0].text]
        

    pass

# print(select_next_subscale("sunt foarte fericit", {}))
