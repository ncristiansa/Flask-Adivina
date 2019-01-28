from flask import Flask, request
import random
app = Flask(__name__)

numero = random.randint(0, 100)

@app.route("/adivina", methods=['GET', 'POST'])
def hello():
    if request.method=="POST":
        num1=request.form.get("num1")
        if int(num1)== int(numero):
        	return "<p>El numero aleatorio es {}</p>".format(str(numero))
        else:
        	return "<p>No has acertado</p>"
    else:
        return '''<form action="/adivina" method="POST">
                <label>Numero:</label></br>
                <input type="number" name="num1"/><br/><br/>
                <input type="submit"/>
                </form>'''
