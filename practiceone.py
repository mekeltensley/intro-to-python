# students = [
#     { 
#         "name": "Kimmie",
#         "city": "Atlanta"
#     },
#     { 
#         "name": "Chris",
#         "city": "Salt Lake City"
#     },
#     { 
#         "name": "Zack",
#         "city": "Los Angeles"
#     }
# ]

# def get_cities(students):
#     '''Return a [list] of all cities from the students list'''
#     result = []

#     for s in students:
#         if s.get('name'):
#             result.append(s.get('name'))

#     return result

# print('Cities list: ', get_cities(students))


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
    },
     { 
        "name": "John",
        "city": "Atlanta"
    },
    { 
        "name": "Jane",
        "city": "New York"
    },
    { 
        "name": "Rob",
        "city": "Los Angeles"
    },
     { 
        "name": "Harper",
        "city": "Washington"
    },
    { 
        "name": "Mike",
        "city": "Seattle"
    },
    { 
        "name": "Set",
        "city": "San Francisco"
    },
]

def parse_by_city(students):

    result = {}

    for s in students:
        if 'city' != students