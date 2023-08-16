from mysqlconnection import connectToMySQL
from pprint import pprint
from flask import flash

DATABASE = "dojo_survey_schema"


class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.location = data["location"]
        self.language = data["language"]
        self.comment = data["comment"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def add_info(cls, form_data):
        query = """
        INSERT INTO dojos (name, location, language, comment)
        VALUES (%(name)s,%(location)s,%(language)s,%(comment)s);
        """
        results = connectToMySQL(DATABASE).query_db(query, form_data)
        return results
    
    @staticmethod
    def validate_info(dojo):
        is_valid = True
        if len(dojo['name']) < 3:
            flash("Name must be longer than 3 characters.")
            is_valid = False
        if len(dojo['comment']) < 3:
            flash("Comment must be longer than 3 characters.")
            is_valid = False
        return is_valid
    
    @classmethod
    def get_one(cls, id):
        query = """
        SELECT * FROM dojos
        WHERE id = %(id)s;
        """

        data = {"id": id}
        results = connectToMySQL(DATABASE).query_db(query, data)

        dojo = Dojo(results[0])
        return dojo