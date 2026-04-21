from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route('/<string>')
def return_backwards_string(string):
    return "".join(reversed(string))

@app.route('/get-mode')
def get_mode():
    return os.getenv('MODE', 'No mode set')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)