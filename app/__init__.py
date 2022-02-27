from flask import Flask
import os

# The __name__ variable passed to the Flask class is a Python predefined
# variable, which is set to the name of the module in which it is used.
app = Flask(__name__)

from app import hello
from app import getMessages
from app import getMessage
from app import addMessage
from app import deleteMessage