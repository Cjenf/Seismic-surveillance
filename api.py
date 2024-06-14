from flask import Flask, jsonify
from lib import erf, ewfi

erf_data = erf.json()
ewfi_data = ewfi.json()

app = Flask(__name__)

@app.route('/api/erf_', methods=['GET'])
def erf_():
    return jsonify(erf_data)

@app.route('/api/ewfi', methods=['GET'])
def ewfi_():
    return jsonify(ewfi_data)

if __name__ == '__main__':
    app.run(debug=True)