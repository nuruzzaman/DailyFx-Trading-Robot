import os
import sys
import colorama
from TradingBot import TradingBot
from DWX_ZeroMQ_Connector_v2_0_1_RC8 import DWX_ZeroMQ_Connector

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import logging
from logging.handlers import TimedRotatingFileHandler
from flask import Flask, render_template, request

colorama.init()

def init_log(log_file='log/info.log'):

    handler = TimedRotatingFileHandler(log_file, when="D", interval=1, backupCount=7)
    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
    handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    
    return logger

logger = init_log()
bot = TradingBot()
app = Flask(__name__, static_url_path='')

# ###################################################################

@app.route('/', methods=['GET', 'POST'])
def view():
    return render_template('index.html')


@app.route('/chat', methods=['GET'])
def response():
    data = request.args.to_dict()
    message = data['message']
                
    if message != '':
        if message.strip() == 'exit' or message.strip() == 'quit':
            answer = 'Thank you for using IntelliBot. GoodBye' 
        else:
            answer = bot.response(message)
    return answer


@app.route('/forget', methods=['GET'])
def forget():
    return 'success'


if __name__ == '__main__':
    print ("Server started...Port 5000")
    app.run('127.0.0.1', debug=True)
