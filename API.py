# Libraries
from flask import Flask
from flask_restful import reqparse,Api,Resource
import logging
from API_Routing import Module1,Module2,Module3
#logging.basicConfig(filename='Log.log',level=logging.INFO,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

# Creating Flask app and API
app = Flask(__name__)
api = Api(app)

# placing the restapi routing resource
api.add_resource(Module1,'/module1')
api.add_resource(Module2,'/module2')
api.add_resource(Module3,'/module3')

if __name__ == '__main__':
    app.run(host = '127.0.0.1',debug=True)