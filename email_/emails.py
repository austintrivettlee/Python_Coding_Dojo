from mysqlconnection import connectToMySQL
from pprint import pprint
import re
from flask import flash

DATABASE = "email_schema"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        
    @classmethod
    def create(cls, form_data):
        query = """
        INSERT INTO emails (email)
        VALUES (%(email)s);
        """
        
        return connectToMySQL(DATABASE).query_db(query, form_data)
    
    @classmethod
    def get_one(cls, id):
        query = """ 
        SELECT * from emails 
        WHERE id = %(id)s 
        """
        data = {"id": id}
        results = connectToMySQL(DATABASE).query_db(query, data)
        email = Email(results[0])
        return email
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        emails = []
        for dictionary in results:
            emails.append(Email(dictionary))
        return emails
    
    @staticmethod
    def is_valid_email(email):
        is_valid = True
        if len(email['email']) == 0:
            flash("Email must be entered")
            is_valid = False
        if not EMAIL_REGEX.match(email['email']):
            flash("Invalid Email Address!")
            is_valid = False
        return is_valid