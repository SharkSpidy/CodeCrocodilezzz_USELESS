from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chord-detect', methods=['POST'])
def chord_detect():
    # Process incoming audio data here
    return jsonify({"message": "Chord recognized!"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
