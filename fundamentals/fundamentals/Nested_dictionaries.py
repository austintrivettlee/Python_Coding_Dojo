# -----------ONE---------
# x = [ [5,2,3], [10,8,9] ] 
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# x[1][0] = 15
# print(x)

# students[0]["last_name"] = "Bryant"
# print(students)

# sports_directory["soccer"][0] = "Andres"
# print(sports_directory)

# z[0]["y"] = 30
# print(z)

---------TWO---------
students = [
        {'first_name' : 'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(students):
    for each_key in students:
        print(each_key)

def iterateDictionary2(key, students):
    for i in range(len(students)):
        print(students[i][key])
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
iterateDictionary(students)
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

# -----------THREE-----------
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dojo):
    for key in dojo:
        print(len(dojo[key]), key.upper())
        for value in range(len(dojo[key])):
            print(dojo[key][value])

printInfo(dojo)

# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
