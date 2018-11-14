from flask import Flask, jsonify

app = Flask(__name__)


from api.views.parcels import *
from api.views.users import *

if __name__ == "__main__":
  app.run()