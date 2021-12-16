from flask import Flask, request, jsonify
from flask_cors import CORS
from sado import SadoFuzzy

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def hello_world():
    return "SADO 2.0!"

@app.route("/start", methods=["POST"])
def run():
    sado_fuzzy = SadoFuzzy()
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
        return jsonify(calorie=round(calorie['Calorie'], 2))
        