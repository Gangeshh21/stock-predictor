from flask import Flask, request, jsonify
from flask_cors import CORS
from model import predict_stock

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    ticker = data.get("ticker")
    days = int(data.get("days"))

    forecast, accuracy, historical = predict_stock(ticker, days)
    return jsonify({
    "forecast": forecast,
    "accuracy": accuracy,
    "historical": historical
})

if __name__ == "__main__":
    app.run(debug=True)

    