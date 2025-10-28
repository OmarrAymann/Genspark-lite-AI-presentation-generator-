import os
from flask import Flask, request, send_file, jsonify
from ppt_generator import generate_presentation

app = Flask(__name__)
@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()
        topic = data.get("topic", " Messi")
        slides = data.get("slides", 15)
        theme = data.get("theme", " Modern Dark ")
        
        if not topic or len(topic.strip()) == 0:
            return jsonify({"error": "Topic cannot be empty"}), 400
        
        if slides < 5 or slides > 15:
            return jsonify({"error": "Slides must be between 5 and 16"}), 400
        
        if theme not in [" Navy ", " White ", " Modern Dark ", " Baby Blue "]:
            return jsonify({"error": "Invalid theme"}), 400
        
        output_dir = "presentations"
        os.makedirs(output_dir, exist_ok=True)

        output_path = os.path.join(output_dir, f"{topic.replace(' ', '_')}.pptx")

        generate_presentation(topic,slides,output_path)
        return send_file(output_path, as_attachment=True)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)