from flask import Flask, json
from flask import render_template
from flask import request
from flask import jsonify
from bs4 import BeautifulSoup
from googlesearch import search
import requests
import spacy

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def homepage():
    if request.method == "POST":
        news_title = request.form.get('title')
        print(news_title)
        news_publishers_pt = ['https://www.publico.pt/', 'https://www.dn.pt/', 'https://www.rtp.pt/',
                    'https://www.cmjornal.pt/', 'https://www.iol.pt/', 'https://www.tvi24.iol.pt/',
                    'https://www.sapo.pt/', 'https://observador.pt/', 'https://expresso.pt/',
                    'https://www.jn.pt/', 'https://sicnoticias.pt/', 'https://www.noticiasaominuto.com/']
        
        trust_counter = 0
        trustful_sources = []

        for i in search(news_title, tld='pt', lang='pt', num=10, stop=10, pause=2):
            if any(x in i for x in news_publishers_pt):
                print(i)
                url = i
                result = requests.get(url)
                try:
                    doc = BeautifulSoup(result.text, "html.parser")
                    doc_title = doc.title.string
                    #nlp = spacy.load('en_core_web_sm')
                    nlp_pt = spacy.load('pt_core_news_md')
                    prompt = nlp_pt(news_title)
                    target_news = nlp_pt(str(doc_title))
                    print(prompt.similarity(target_news))
                    similarity = prompt.similarity(target_news)
                    if similarity > 0.50:
                        trust_counter += 1
                        trustful_sources.append(i)
                except:
                    print('Unable to output')
        if trust_counter >= 6:
            reliable = True
            certainty = "very high"
        elif trust_counter == 4 or trust_counter == 5:
            reliable = True
            certainty = "high"
        elif trust_counter == 3:
            reliable = True
            certainty = "medium"
        elif trust_counter == 2:
            reliable = True
            certainty = "low to medium"
        elif trust_counter == 1:
            reliable = False
            certainty = "low"
        else:
            reliable = False
            certainty = "high"
        return render_template('results.html', reliable = reliable, certainty = certainty, trustful_sources= trustful_sources)
    return render_template('homepage.html')
    
@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/blog/how-it-works')
def how_it_works():
    return render_template('how_it_works.html')

@app.route('/blog/breaking-down-misinformation')
def breaking_down_misinformation():
    return render_template('breaking_down_misinformation.html')

@app.route('/blog/but-why')
def but_why():
    return render_template('but_why.html')

@app.route('/blog/best-practices')
def best_practices():
    return render_template('best_practices.html')

@app.route('/coming-soon')
def coming_soon():
    return render_template('coming-soon.html')

if __name__ == '__main__': 
    app.run(debug=True, host='0.0.0.0')