from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from pprint import pprint
from flask import flash


DATABASE = "belt_exam_schema"

class Car:
    def __init__(self, data):
        self.id = data['id']
        self.model = data['model']
        self.year = data['year']
        self.price = data['price']
        self.make = data['make']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.seller = ""
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cars;"
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        cars = []
        for dictionary in results:
            cars.append(Car(dictionary))
        return cars
        
    @classmethod
    def get_one(cls, id):
        query = """ 
        SELECT * from cars
        WHERE id = %(id)s 
        """
        data = {"id": id}
        results = connectToMySQL(DATABASE).query_db(query, data)
        cars = Car(results[0])
        return cars
    
    @classmethod
    def edit_car(cls, form_data):
        query = """
        UPDATE cars
        SET model = %(model)s, year = %(year)s, price = %(price)s, make = %(make)s, description = %(description)s
        WHERE id = %(id)s;
        """
        
        return connectToMySQL(DATABASE).query_db(query, form_data)
    
    @classmethod
    def delete_car(cls, id):
        query = """
        DELETE FROM cars WHERE id = %(id)s
        """
        data = {"id": id}
        
        connectToMySQL(DATABASE).query_db(query, data)
        return
    
    @classmethod
    def get_cars_with_seller(cls):
        query = """
        SELECT * FROM cars
        LEFT JOIN users
        ON users.id = cars.user_id
        """
        
        results = connectToMySQL(DATABASE).query_db(query)
        cars = []
        
        for each_car in results:
            car = Car(each_car)
            car.seller = f"{each_car['first_name']} {each_car['last_name']}"
            car.id = each_car['id']
            cars.append(car)
        return cars
    
    @classmethod
    def create_car(cls, form_data):
        query = """
        INSERT INTO cars (make, model, price, year, description, user_id)
        VALUES (%(make)s,%(model)s,%(price)s,%(year)s,%(description)s, %(user_id)s);
        """
        
        results = connectToMySQL(DATABASE).query_db(query, form_data)
        return results

    @staticmethod
    def is_valid_car(form):
        is_valid = True
        if len(form['price']) < 1:
            flash('Price cannot be blank.')
            is_valid = False
        elif form['price'] == "" or int(form['price']) < 1:
            flash('Price cannot be less than $1.')
            is_valid = False
        if len(form['make']) < 1:
            flash('Make cannot be left blank.')
            is_valid = False
        if len(form['model']) < 1:
            flash('Model cannot be left blank.')
            is_valid = False
        if len(form['year']) < 1:
            flash('Price cannot be blank.')
            is_valid = False
        elif form['year'] == "" or int(form['year']) < 1:
            flash('Year cannot be less than 1.')
            is_valid = False
        if len(form['description']) < 1:
            flash('description cannot be left blank.')
            is_valid = False
        return is_valid
