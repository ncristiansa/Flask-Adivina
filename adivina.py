from flask import Flask, session,request
import random
app = Flask(__name__)

numero = random.randint(0, 100)

@app.route("/adivina", methods=['GET', 'POST'])
def adivinanumero():
    if request.method=="POST":
        num1=request.form.get("num1")
        if int(num1)== int(numero):
        	return "<p>El numero aleatorio es {}</p>".format(str(numero))
        else:
        	return "<p>No has acertado</p>"
    else:
        return '''<form action="/adivina" method="POST">
                <h2>Numero aleatorio (0-100)</h2>
                <label>Numero:</label></br>
                <input type="number" name="num1"/><br/><br/>
                <input type="submit"/>
                </form>'''
