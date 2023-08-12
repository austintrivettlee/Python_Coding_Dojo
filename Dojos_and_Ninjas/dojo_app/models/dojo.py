from dojo_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
from dojo_app.models import ninja

DATABASE = "dojos_and_ninjas_schema"

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
        
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
        dojo = Dojo(results[0])
        return dojo
    
    @classmethod
    def create_dojo(cls, form_data):
        query = """
        INSERT INTO dojos (name)
        VALUES (%(name)s);
        """
        
        results = connectToMySQL(DATABASE).query_db(query, form_data)
        return results
    
    @classmethod
    def edit_dojo(cls, form_data):
        query = """
        UPDATE dojos
        SET name = %(name)s
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
    
    @classmethod
    def get_one_dojo_with_ninjas(cls, id):
        query = """
        SELECT * FROM dojos
        LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id
        WHERE dojos.id = %(id)s;"""
        
        data = {
            "id" : id
        }
        results = connectToMySQL(DATABASE).query_db(query, data)
        dojo = cls(results[0])
        for each_ninja in results:
            ninja_data = {
                "id" : each_ninja["ninjas.id"],
                "first_name" : each_ninja["first_name"],
                "last_name" : each_ninja["last_name"],
                "age" : each_ninja["age"],
                "created_at" : each_ninja["ninjas.created_at"],
                "updated_at" : each_ninja["ninjas.updated_at"]
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo.ninjas