from flask import Flask, render_template, request, session, flash, redirect, url_for
import os
import openai
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
import json
import os

app = Flask(__name__)











@app.route('/', methods=['GET', 'POST'])
def index():


    result = None 
    if request.method == 'POST':
       
        Query = request.form['Query']


        client = openai.OpenAI(api_key=os.environ.get('secret_key'))
     
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            temperature=0,
            max_tokens=1000,
            messages=[
                    {"role": "system", "content": f"You are an ai tutor and edu assistant named ChatAcademyAI, You should understand the question with 100% accuracy and give the most suitable  and helpful response to the user, be kind and friendy and do this job as perfecly as possible use all your technolgy, resources and intelligence."},
               { "role": "user", "content":  Query},
            ]
        )
        result = response.choices[0].message.content
        

    return render_template('index.html', result=result)
