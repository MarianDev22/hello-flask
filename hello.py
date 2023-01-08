from flask import Flask, render_template

#para inicializar el servidor de flask
#en Win: set FLASK_APP=hello.py

#para ejecutar el servidor de flask --> flask --app hello run
#Actualizar el servidor con cambios de codigo en tiempo real --> flask --app hello --debug run

#Comando espcial para lanzar el servidor en un puerto diferente en caso de que esté ocupado:
# flask --app hello run -p 5001

app = Flask(__name__)#inicializar flask en app

@app.route("/hola")#definimos la ruta donde vamos a estar ejecutando esta funcion
def hello_mundo():
    return "hola mundo flask"#retorna el str hola mundo flask

#Ejercicio: crear una ruta "adios" que retorne una despedida: Hasta pronto Rolando

@app.route("/adios")#definimos la ruta donde vamos a estar ejecutando esta funcion
def despedida():
    return "Hasta pronto Pepe"#retorna el str hola mundo flask

# Ejemplo para enviar parametros a traves de las rutas

@app.route("/nombre/<n>")
def name(n):
    return f"Tu nombre es {n}"

# Realizar una ruta con un parametro que devuelva el cuadrado de un numero

@app.route("/numero/<int:n>")
def cuadrado(n):
    return f"El cuadrado de {n} es {n*n}"

# Realizar una ruta que dinamicamente pueda solicitar realizar
# operaciones de suma, resta, multiplicacion y division segun los parametros
# pasados por la ruta url

@app.route("/operaciones/<float:n1>/<float:n2>/<ope>")
def calculadora(n1, n2, ope):
    if ope == "suma":
        return render_template('hola.html', resultado=f"La suma es {n1+n2}")
    elif ope == "resta":
        return render_template('hola.html', resultado=f"La resta es {n1-n2}")
    elif ope == "division":
        return render_template('hola.html', resultado=f"La division es {n1/n2}")
    elif ope == "multiplicacion":
        return render_template('hola.html', resultado=f"La multiplicacion es {n1*n2}")

# ejemplo de como devolver un html por flask

#@app.route("/primerhtml")
#def callhtml():
#    return render_template('hola.html')

# ejemplo de como devolver un html por flask

@app.route("/primerhtml/<nombre>")
def callhtml(nombre):
    return render_template('hola.html', name=nombre)