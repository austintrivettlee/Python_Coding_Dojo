from dojo_app.config.mysqlconnection import connectToMySQL
from pprint import pprint

DATABASE = "dojos_and_ninjas_schema"

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
        
    def __repr__(self):
        return f"<Name: {self.first_name} {self.last_name} || Age: {self.age} || Dojo: {self.dojo_id}>"
    
    @classmethod
    def get_all_ninjas(cls):
        query = """
        SELECT * FROM ninjas;
        """
        
        results = connectToMySQL(DATABASE).query_db(query)
        ninjas = []
        
        for each_ninja in results:
            ninjas.append(Ninja(each_ninja))
        return ninjas
    
    @classmethod
    def get_one_ninja(cls, id):
        query = """
        SELECT * FROM ninjas
        WHERE id = %(id)s"""
        
        data = {"id": id}
        
        results = connectToMySQL(DATABASE).query_db(query, data)
        ninja = Ninja(results[0])
        return ninja
    
    @classmethod
    def create_ninja(cls, form_data):
        query = """
        INSERT INTO users (first_name, last_name, age, dojo_id)
        VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);
        """
        
        results = connectToMySQL(DATABASE).query_db(query, form_data)
        return results
    
    @classmethod
    def edit_ninja(cls, form_data):
        query = """
        UPDATE users
        SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s, dojo_id = %(dojo_id)s
        WHERE id = %(ninja_id)s;
        """
        
        connectToMySQL(DATABASE).query_db(query, form_data)
        return
    
    @classmethod
    def delete_ninja(cls, id):
        query = """
        DELETE FROM ninjas WHERE id = %(id)s
        """
        data = {"id": id}
        
        connectToMySQL(DATABASE).query_db(query, data)
        return