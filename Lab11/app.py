from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
     dane = {'tytul':'Strona główna', 'tresc':'Treść strony głównej.'}
     return render_template('index.html', tytul=dane['tytul'], tresc=dane['tresc'])

	
@app.route("/omnie")
def about():
     dane = {'tytul':'O mnie', 'tresc':'Nazywam się Alicja z Krainy Czarów.'}
     return render_template('omnie.html', tytul=dane['tytul'], tresc=dane['tresc'])

@app.route('/informacje')
def info():
    posty = [
        {
         'author': {'username': 'Mateusz'},
         'body': '19291'
        },
        {
         'author': {'username': 'Monika'},
         'body': 'Test'
    }]
    dane = {'tytul':'Informacje', 'tresc':'Spis informacji'}
    return render_template('informacje.html', tytul=dane['tytul'], tresc=dane['tresc'], posty=posty)
 
@app.route("/kontent")
def kontent():
     dane = {'tytul':'Kontent', 'tresc':'Test kontentu'}
     return render_template('kontent.html', tytul=dane['tytul'], tresc=dane['tresc'])
	
if __name__ == "__main__":
	app.run()