from flask import Flask
from rutas.rutas_experimentos import bp_experimentos
from rutas.rutas_cientificos import bp_cientificos

app = Flask(__name__) #creamos una instancia de la clase Flask


#registramos el blueprint
app.register_blueprint(bp_experimentos)
app.register_blueprint(bp_cientificos)

if __name__ == '__main__':
    app.run(debug=True) #iniciamos la aplicación