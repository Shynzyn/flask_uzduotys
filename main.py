from flask import Flask, render_template, request
from funkcija import *

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('base.html')


@app.route("/<vardas>")
def penki_kartai(vardas):
    return (vardas + " ") * 5

@app.route('/sveikaspasauli')
def sveikas_pasauli():
    return render_template("hello_world.html")

@app.route("/skaiciavimai/")
def skaiciavimai():
    return render_template("skaiciavimai.html")

@app.route("/zmones/")
def vardai():
    masyvas = ["Jonas", "Antanas", "Petras", "Lukas"]
    return render_template("zmones.html", vardai=masyvas)


@app.route("/login", methods=['GET', 'POST'])
def prisijungimas():
    if request.method == "GET":
        return render_template('prisijungimas.html')
    if request.method == "POST":
        vardas = request.form['fname']
        return render_template('greetings.html', vardas=vardas)

@app.route("/keliamieji")
def keliamieji():
    visi_metai = []
    for year in range(1900,2101):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            visi_metai.append(year)
    return render_template('keliamieji.html', visi_metai=visi_metai)

@app.route('/ar_keliamieji', methods=['GET', 'POST'])
def ar_keliamieji():
    if request.method == "GET":
        return render_template('ar_keliamieji.html')
    if request.method == "POST":
        metai = request.form['metai']
        result = funkcija(metai)
        return render_template('atsakymas.html', metai=metai, funkcija=result)





if __name__ == "__main__":
    app.run(debug=True)
