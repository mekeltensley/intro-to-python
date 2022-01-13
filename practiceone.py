students = [
    { 
        "name": "Kimmie",
        "city": "Atlanta"
    },
    { 
        "name": "Chris",
        "city": "Salt Lake City"
    },
    { 
        "name": "Zack",
        "city": "Los Angeles"
    }
]

def get_cities(students):
    '''Return a [list] of all cities from the students list'''
    result = []

    for s in students:
        if s.get('city'):
            result.append(s.get('city'))

    return result

print('Cities list: ', get_cities(students))
