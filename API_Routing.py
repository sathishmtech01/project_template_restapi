from flask_restful import reqparse,Api,Resource
from API_Defaults import parser

# Module 1 class
class Module1(Resource):

    def post(self):
        '''

        :return:
        '''

        # getting the input arguments
        inputs = parser.parse_args()
        #Calling Chat function
        result = inputs
        return {"module1":result}

# Module 2 class
class Module2(Resource):

    def post(self):
        '''

        :return:
        '''

        # getting the input arguments
        inputs = parser.parse_args()
        #Calling Chat function
        result = inputs
        return {"module2":result}

# Chating Class
class Module3(Resource):

    def get(self):
        '''

        :return:
        '''

        return {"module3":{"name":"csk"}}

