from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

# Путь к файлу со счетчиком
counter_file = 'counter.txt'

# Инициализация счетчика
if not os.path.exists(counter_file):
    with open(counter_file, 'w') as f:
        f.write('0')

def get_counter():
    with open(counter_file, 'r') as f:
        return int(f.read())

def increment_counter():
    counter = get_counter() + 1
    with open(counter_file, 'w') as f:
        f.write(str(counter))
    return counter

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/increment', methods=['POST'])
def increment():
    counter = increment_counter()
    return jsonify({'counter': counter})

if __name__ == '__main__':
    app.run(debug=True)
