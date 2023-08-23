from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from pprint import pprint
from flask import flash, request

DATABASE = "stellascope"

class Comment:
    def __init__(self, data):
        self.id = data['id']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM comments;"
        results = connectToMySQL(DATABASE).query_db(query)
        comments = []
        for dictionary in results:
            comments.append(Comment(dictionary))
        return comments
    
    @classmethod
    def create_comment(cls, form_data):
        query = """
        INSERT INTO comments (comment, user_id)
        VALUES (%(comment)s, %(user_id)s);
        """
        
        results = connectToMySQL(DATABASE).query_db(query, form_data)
        return results
    
    @staticmethod
    def validate_comment(request.form):
        is_valid = True
        if len(request.form['comment'] < 2):
            flash("Comment must be longer than 2 characters")
            is_valid = False
        return is_valid