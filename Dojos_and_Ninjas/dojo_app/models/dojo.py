from dojo_app.config.mysqlconnection import connectToMySQL
from pprint import pprint

DATABASE = "dojos_and_ninjas_schema"

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_all_dojos(cls):
        query = """
        SELECT * FROM dojos;
        """
        
        results = connectToMySQL(DATABASE).query_db(query)
        dojos = []
        
        for each_dojo in results:
            dojos.append(Dojo(each_dojo))
        return dojos
    
    @classmethod
    def get_one_dojo(cls, id):
        query = """
        SELECT * FROM dojos
        WHERE id = %(id)s"""
        
        data = {"id": id}
        
        results = connectToMySQL(DATABASE).query_db(query, data)
        dojo = dojo(results[0])
        return dojo
    
    @classmethod
    def create_dojo(cls, form_data):
        query = """
        INSERT INTO users (first_name, last_name, age, dojo_id)
        VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);
        """
        
        results = connectToMySQL(DATABASE).query_db(query, form_data)
        return results
    
    @classmethod
    def edit_dojo(cls, form_data):
        query = """
        UPDATE users
        SET first_name = %(name)s
        WHERE id = %(dojo_id)s;
        """
        
        connectToMySQL(DATABASE).query_db(query, form_data)
        return
    
    @classmethod
    def delete_dojo(cls, id):
        query = """
        DELETE FROM dojos WHERE id = %(id)s
        """
        data = {"id": id}
        
        connectToMySQL(DATABASE).query_db(query, data)
        return