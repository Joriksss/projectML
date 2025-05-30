from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
import json
from PIL import Image
import random
import sqlite3
from datetime import datetime


character_folder = 'static/images_the_boys'

def init_db():
    conn = sqlite3.connect('logs.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            character TEXT,
            confidence REAL,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()


app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = 'uploads'

model = load_model('model/model.h5')
with open('model/labels.json', 'r') as f:
    class_names = json.load(f)


img_size = 224


def preprocess_image(img_path):
    img = Image.open(img_path).convert('RGB').resize((img_size, img_size))
    img_array = np.array(img).astype('float32') / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def get_random_photo(character_name):
    folder_path = os.path.join(character_folder, character_name)
    if not os.path.exists(folder_path):
        return None
    files = os.listdir(folder_path)
    photos = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    if not photos:
        return None
    random_photo = random.choice(photos)
    return os.path.join(folder_path, random_photo)


def log_prediction(filename, character, confidence):
    timestamp = datetime.utcnow().isoformat()
    conn = sqlite3.connect('logs.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO logs (filename, character, confidence, timestamp)
        VALUES (?, ?, ?, ?)
    ''', (filename, character, confidence, timestamp))
    conn.commit()
    conn.close()

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'Нет файла'}), 400

    file = request.files['file']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    try:
        img_tensor = preprocess_image(filepath)
        preds = model.predict(img_tensor)[0]
        class_idx = int(np.argmax(preds))
        confidence = float(np.max(preds)) * 100

        character_name = class_names[str(class_idx)]
        photo_path = get_random_photo(character_name)

        if photo_path:
            photo_url = '/' + photo_path.replace('\\', '/')
        else:
            photo_url = ''

        log_prediction(file.filename, character_name, round(confidence, 2))

        result = {
            'name': character_name,
            'confidence': round(confidence, 2),
            'photo_url': photo_url
        }

        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        os.remove(filepath)



if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    init_db()
    app.run(debug=True, port=5000)
