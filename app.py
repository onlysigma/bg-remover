from flask import Flask, request, send_file, jsonify
from rembg import remove
import io

app = Flask(__name__)

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/remove_bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    img_file = request.files['image']
    input_bytes = img_file.read()

    try:
        output_bytes = remove(input_bytes)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return send_file(io.BytesIO(output_bytes), mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
