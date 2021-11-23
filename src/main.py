from flask import Flask, jsonify
from db import Database

app = Flask(__name__)

db = Database()
port = 3001

@app.route('/municipios/<id>')
def get_municipio(id):
    return jsonify(db.get_mun(id))

@app.route('/')
def all():
    return jsonify(db.get_all())

if __name__ == "__main__":
    app.run(debug = True, port=port)