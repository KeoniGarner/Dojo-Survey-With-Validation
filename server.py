#!/usr/bin/env python
from flask import Flask, render_template, redirect, request, flash, session

app = Flask(__name__)
app.secret_key = "SECRETKEY"

@app.route('/')

def dojo_survey():
    return render_template('index.html')

@app.route('/results', methods=['POST'])

def results():
    errors = False
    name = request.form['name']
    if len(name) < 1:
        flash('Name cannot be blank!')
        errors = True
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    if len(comment) < 1:
        flash('Comment cannot be blank!')
        errors = True
    elif len(comment) > 120:
        flash('Comment must be less than 120 characters!')
        errors = True;        
    if errors:
        return redirect('/')
    else:
        return render_template('results.html', name=name, location=location, language=language, comment=comment)

app.run(debug=True)