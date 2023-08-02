def count_down_by_one(start: int):
    list = []
    end = 0
    incr = -1
    end += incr
    for i in range(start, end, incr):
        list.append(i)
    return list

print(count_down_by_one(10))


def print_and_return(list: list):
    print("This is the print:", list[0])
    return list[1]

print("This is the return:", print_and_return([3, 6]))

def first_plus_length(list: list):
    output = 0
    output += list[0]
    output += len(list)
    return output

print(first_plus_length([1,2,3,4,5]))

def values_greater_than_second(list: list):
    output = []
    for i in range(len(list)):
        if (list[i] > list[1]):
            output.append(list[i])
    return output

print(values_greater_than_second([5,2,3,2,1,4]))

def length_and_value(size:int , value: int):
    output = []
    for i in range(size):
        output.append(value)
    return output

print(length_and_value(4,7))
print(length_and_value(6,2))

