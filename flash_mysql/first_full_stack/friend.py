# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
from pprint import pprint
# model the class after the friend table from our database

DATABASE = 'friends_db'

class Friend:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    
    def __repr__(self):
        return f"<Friends: {self.first_name} {self.last_name}"
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        # Create an empty list to append our instances of friends
        friends = []
        # Iterate over the db results and create instances of friends with cls.
        for dictionary in results:
            friends.append(Friend(dictionary) )
        return friends
            
