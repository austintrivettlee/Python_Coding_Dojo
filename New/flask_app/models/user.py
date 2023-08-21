from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint

DATABASE = "users_schema"

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['email']
        self.dojo_id = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']