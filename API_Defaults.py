from flask_restful import reqparse

# Default Parameters used in the development
# Parsing API request from API
parser = reqparse.RequestParser()
# adding the argument actions : 'append'
parser.add_argument('name')
parser.add_argument('age')
parser.add_argument('sex')