import os
import sys
import zmq
from time import sleep
from pandas import DataFrame, Timestamp
from threading import Thread
from DWX_ZeroMQ_Connector_v2_0_1_RC8 import DWX_ZeroMQ_Connector

class TradingBot:

    def __init__(self):
        pass

    def response(self, user_message):
        print('# User -->: '+user_message)
        
        # # Limit word count
        # if len(user_message) > 200:
        #     return self.mybot.respond('MAX')
        # elif len(user_message) < 2:
        #     return self.mybot.respond('MIN')
        
        
        #       Start Conversation
        # **************************************************
        responseAnswer = 'Trading Bot Reply!!!'
        
        return responseAnswer 
    
if __name__ == '__main__':
    bot = TradingBot()
    while True:		
        user_message = input('User > ')
        bot.response(user_message)
