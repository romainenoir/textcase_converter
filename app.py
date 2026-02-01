from flask import Flask, render_template, redirect, url_for
from components.forms import TextConvertForm
from components.textcase_functions import request_lower_case, request_sentence_case, request_title_case, request_upper_case


app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_string"

@app.route("/convert-text", methods=['GET', 'POST'])
def text_converter():
    new_string = None
    text_convert=TextConvertForm()
    if text_convert.validate_on_submit():
        
        if text_convert.uppercase.data:
            # convert string to uppercase letters
            new_string = request_upper_case(text_convert.textarea.data)
            
        if text_convert.lowercase.data:
            # convert string to lowercase letters
            new_string = request_lower_case(text_convert.textarea.data)
            
        if text_convert.sentence_case.data:
            # convert string to lowercase letters
            new_string = request_sentence_case(text_convert.textarea.data)
            
        if text_convert.title_case.data:
            # convert string to lowercase letters
            new_string = request_title_case(text_convert.textarea.data)
            
    
    return render_template("index.html",
                           text_convert=text_convert,
                           new_string=new_string)

@app.route("/")
def index():
    return redirect(url_for("text_converter"))

