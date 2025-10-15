from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/process-data', methods=['POST'])
def process_data():
    # Get the JSON data from the request
    input_data = request.json
    
    # Return message
    result = {
        "message": "Data processed successfully",
        "received_data": input_data
    }
    
    # Returning the result as a JSON response
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
