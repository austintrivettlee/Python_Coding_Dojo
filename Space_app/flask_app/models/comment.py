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
        self.creator_id = data['creator_id']

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
    def validate_comment(form):
        is_valid = True
        if len(form['comment']) < 2:
            flash("Comment must be longer than 2 characters")
            is_valid = False
        return is_valid
    
    @classmethod
    def get_all_with_creator(cls):
        query = """
        SELECT * FROM comments
        JOIN users ON  users.id = creator_id
        """
        
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_comments = []
            for row in results:
                one_comment = cls(row)
                user_data = {
                    **row,
                    "id": row['id'],
                    "first_name": row['first_name'],
                    "last_name": row['last_name'],
                    "created_at": row['created_at'],
                    "updated_at": row['updated_at']
                }
                
                one_comment.creator = user.User(user_data)
                all_comments.append(one_comment)
            return all_comments

    @classmethod
    def get_one_with_creator(cls, id):
        query = """
        SELECT * FROM comments
        JOIN users ON  users.id = creator_id
        WHERE id = %(id)s
        """
        results = connectToMySQL(DATABASE).query_db(query, id)
        if results:
            row = results[0]
            one_comment = cls(row)
            user_data ={
                    **row,
                    "id": row['user.id'],
                    "first_name": row['user.first_name'],
                    "last_name": row['user.last_name'],
                    "created_at": row['user.created_at'],
                    "updated_at": row['user.updated_at']
                }
            one_comment.creator = user.User(user_data)
        return one_comment