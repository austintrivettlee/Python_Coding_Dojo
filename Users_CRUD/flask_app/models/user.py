from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint

DATABASE = "users_schema"


class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    def __repr__(self):
        return f"<Name: {self.first_name} {self.last_name} || Email: {self.email}>"

    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM users;
        """
        results = connectToMySQL(DATABASE).query_db(query)

        users = []

        for dictionary in results:
            users.append(User(dictionary))
        return users

    @classmethod
    def get_one(cls, id):
        query = """
        SELECT * FROM users
        WHERE id = %(id)s;
        """

        data = {"id": id}
        results = connectToMySQL(DATABASE).query_db(query, data)

        user = User(results[0])
        return user

    @classmethod
    def create(cls, form_data):
        query = """
        INSERT INTO users (first_name, last_name, email)
        VALUES (%(first_name)s,%(last_name)s,%(email)s);
        """
        results = connectToMySQL(DATABASE).query_db(query, form_data)
        return results

    @classmethod
    def delete(cls, id):
        query = """
        DELETE FROM users WHERE id= %(id)s;
        """
        data = {"id": id}
        connectToMySQL(DATABASE).query_db(query, data)
        return
    
    @classmethod
    def update(cls, form_data):
        query = """
        UPDATE users
        SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s
        WHERE id = %(user_id)s;
        """
        connectToMySQL(DATABASE).query_db(query, form_data)
        return
