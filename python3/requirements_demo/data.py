persons = {
    "person_1": {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    },
    "person_2": {
        "name": "Bob",
        "age": 25,
        "city": "Los Angeles"
    },
    "person_3": {
        "name": "Charlie",
        "age": 35,
        "city": "Chicago"
    }
}

def avg_age():
    sum = 0
    for i in persons.keys():
        sum += persons[i]['age']
    return sum / len(persons)