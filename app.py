from flask import Flask
from models import engine
from models import DB_URL
from sqlalchemy import text

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
