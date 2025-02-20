from flask import Flask, request, render_template
import spacy
from collections import Counter

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

def extract_skills(resume_text):
    doc = nlp(resume_text)
    skills = [token.text.lower() for token in doc if token.pos_ in ["NOUN", "PROPN"]]
    return ", ".join(dict(Counter(skills).most_common(10)).keys())

@app.route("/", methods=["GET", "POST"])
def index():
    skills = ""
    if request.method == "POST":
        resume_text = request.form["resume_text"]
        skills = extract_skills(resume_text)
    return render_template("main.html", skills=skills)

if __name__ == "__main__":
    app.run(debug=True)
