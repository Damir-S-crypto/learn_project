from wsgiref.util import application_uri
from flask import Flask, jsonify
import os
app = Flask(__name__)

CORS(app)
@app.route('/')
def home():
    return jsonify({
        'massage': 'API системы учета товаров',
        'version': '1.0.0',
        'endpoints': {
            'GET /': 'Информация об API',
            'GET /health': 'Проверка информации сервера'
        }
    })
@app.route('/health')
def health_check():
    return jsonify({'status': 'OK'}), 200
if __name__ == '__main__':
    if not os.path.exists('data'):
        os.mkdir('data')
        print("создана папка'data'")

        print("=" * 40)
        print("Сервер запущен")
        print("API доступен по адресу: http://localhost:5000")
        print("Фронтед: fronted/index.html")
        print("=" * 40)
        app.run(debug=True, host='0.0.0.0', port=5000)