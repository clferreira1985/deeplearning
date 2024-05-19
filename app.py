from flask import Flask, request, jsonify, render_template
from feeling import feeling  # Import the feeling function from the feeling.py file

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/feeling', methods=['GET', 'POST'])
def handle_feeling():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        print("Received a request at /feeling")  # Debug log
        print(f"Request Content-Type: {request.content_type}")  # Debug log to check content type
        if request.is_json:
            data = request.get_json()
            print(f"Request JSON: {data}")  # Debug log for received JSON
            if 'prompt' not in data:
                return jsonify({"error": "No prompt provided"}), 400

            prompt = data['prompt']
            try:
                result = feeling(prompt)
                return jsonify({"feeling": result})
            except Exception as e:
                return jsonify({"error": str(e)}), 500
        else:
            return jsonify({"error": "Request must be JSON"}), 415

if __name__ == '__main__':
    app.run(debug=True)

