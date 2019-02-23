from flask import Flask,jsonify
from config import DevelopmentConfig
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

@app.route("/ping",methods=['GET'])
def ping_pong():
    return jsonify({
        'status':'success',
        'message':'pong'
    })
