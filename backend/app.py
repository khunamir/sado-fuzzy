from flask import Flask, request, jsonify
from sado import Sado

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "SADO 2.0!"

@app.route("/start", methods=["POST"])
def run():
    sado_fuzzy = Sado()
    if request.method == 'POST':
        user_data = request.json
        calorie = sado_fuzzy.start(
            user_data['weight'], 
            user_data['height'], 
            user_data['age'],
            user_data['bmi'],
            user_data['intensity']
        )
        print(calorie)
        return calorie
