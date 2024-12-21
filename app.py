from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample route to process data
@app.route('/process-data', methods=['POST'])
def process_data():
    # Get the JSON data from the request
    input_data = request.json
    
    # For example, we can return the input data back to the client
    result = {
        "message": "Data processed successfully",
        "received_data": input_data
    }
    
    # Return the result as a JSON response
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
