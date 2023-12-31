from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
from flask import flash
from flask_app.models.comment import Comment
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
DATABASE = "stellascope"

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    def __str__(self) -> str:
        print (f"{self.id} || {self.first_name} || {self.last_name} || {self.email} || {self.password}")
        
    @classmethod
    def create(cls, form_data):
        query = """
        INSERT INTO users (first_name, last_name, email, password)
        VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);
        """
        
        return connectToMySQL(DATABASE).query_db(query, form_data)
    
    @staticmethod
    def is_valid_user(user):
        is_valid = True
        if len(user['first_name']) < 3:
            flash('First Name must be longer than 3 characters.')
            is_valid = False
        if len(user['last_name']) < 3:
            flash('Last Name must be longer than 3 characters.')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash('Invalid Email')
            is_valid = False
        if user['password'] != user['password_conf']:
            flash('Passwords do not match.')
            is_valid = False
        if len(user['password']) < 8:
            flash('Password must be at least 8 characters.')
            is_valid = False
        special_chars = ['$', '&', '!']
        for char in user['password']:
            if char.isalpha():
                continue
            elif char.isdigit():
                continue
            elif char not in special_chars:
                    is_valid = False
        if not is_valid:
            flash("Invalid Password Characters. Can only use $ ! &")
        return is_valid
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        users = []
        for dictionary in results:
            users.append(User(dictionary))
        return users
    
    @classmethod
    def get_one(cls, id):
        query = """ 
        SELECT * from users 
        WHERE id = %(id)s 
        """
        data = {"id": id}
        results = connectToMySQL(DATABASE).query_db(query, data)
        user = User(results[0])
        return user
    
    @classmethod
    def get_by_email(cls, data):
        query = """
        SELECT * FROM users
        WHERE email = %(email)s
        """
        result = connectToMySQL(DATABASE).query_db(query,data)
        
        if len(result) < 1:
            return False
        return cls(result[0])
    
    @classmethod
    def get_one_user_with_comments(cls, data):
        query = """
        SELECT * FROM users
        LEFT JOIN comments ON users.id = creator_id
        WHERE users.id = %(id)s;
        """
        
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            one_user = cls(results[0])
            one_user.comments_created = []
            for row in results:
                comment_data = {
                    "id": row['comments.id'],
                    "comment": row['comment'],
                    "created_at": row['comments.created_at'],
                    "updated_at": row['comments.updated_at'],
                    "creator_id": row['comments.creator_id'],
                    "creator_id": row['creator_id']
                }
                comment = Comment(comment_data)
                one_user.comments_created.append(comment)
        return one_user