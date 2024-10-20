from flask import Flask, request, jsonify
import google.generativeai as genai
import os
api = os.environ.get('GOOGLE_API_KEY')
genai.configure(api_key=api)

app = Flask(__name__)

# Load the pre-trained model and tokenizer
model = genai.GenerativeModel("gemini-1.5-flash")

def summary(text):
    response = model.generate_content(f"Write summary of the patient on the following text so the doctor can get its insights text: {text}")
    return response.text

@app.route('/summarize', methods=['POST'])
def summarize_patient():
    data = request.get_json()
    patient_description = data.get('description')
    summary_text = summary(patient_description)
    return jsonify({'summary': summary_text})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Get the port from environment variable or use 5000 as default
    app.run(host='0.0.0.0', port=port, debug=True)  # Bind to 0.0.0.0 and use the port
