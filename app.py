import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/a-hluti')
def ahluti():
    return render_template('default.html')

@app.route('/ktsida/<kt>')
def ktsida(kt):
    summa = 0
    for item in kt:
        summa = summa + int(item)
    return render_template('kt-sum.html', kt=kt, summa = summa)

@app.errorhandler(404)
def pagenotfound(error):
    return render_template('pagenotfound.html'), 404



@app.route('/b-hluti')
def bhluti():
    return render_template('frettir.html', frettir=frettir)

@app.route('/frett<int:id>')
def news(id):
    return render_template('frett.html', frett=frettir[id], nr=id)
    
@app.errorhandler(404)
def pagenotfound(error):
    return render_template('frett.html'), 404

frettir = [
    ["0","florens veldur usla a florida",
    "thad er bara helvitis vesen a fellibylinum og allt i klessu i flor",
    "dsg@frettir.is"],
    ["1","veidin er draem thetta haustid",
    "veidin hefur heldur verid dopur  thetta haust thratt fyrir agaeti",
    "est@frettir.is"],
    ["2","olafia stendur sig vel",
    "olafia er komin i 65 saeti peningalistans og hefur thvi tryggt ser"],
    ["3","island dottid ur leik",
    "islenska arlalidid i korfubolta er dottid ur leik a evropumotinu",
    "dsg@frettir.is"]
]
if __name__ == '__main__':
    app.run(debug=True)