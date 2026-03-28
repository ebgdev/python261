musteriler = {
    1000000001: {
        'name': 'John',
        'sur_name': 'Doe',
        'age': 17,
        'married': False
    },
    1000000002: {
        'name': 'jane',
        'sur_name': 'Smith',
        'age': 18,
        'married': True
    },
    1000000003: {
        'name': 'Alice',
        'sur_name': 'Brown',
        'age': 22,
        'married': False
    },
    1000000004: {
        'name': 'BOB',
        'sur_name': 'Johnson',
        'age': 45,
        'married': True
    },
    1000000005: {
        'name': 'Charlie',
        'sur_name': 'Williams',
        'age': 30,
        'married': True
    },
    1000000006: {
        'name': 'Eve',
        'sur_name': 'Davis',
        'age': 27,
        'married': False
    },
    1000000007: {
        'name': 'JuliA',
        'sur_name': 'Miller',
        'age': 40,
        'married': True
    },
    1000000008: {
        'name': 'Nancy',
        'sur_name': 'Wilson',
        'age': 35,
        'married': True
    },
    1000000009: {
        'name': 'James',
        'sur_name': 'Taylor',
        'age': 21,
        'married': False
    },
    1000000010: {
        'name': 'olivia',
        'sur_name': 'Anderson',
        'age': 38,
        'married': True
    }
}


def filter_age_name_married(age,adict):
    names = []
    for value in adict.values():
        if value['age'] > age and value['married']:
            names.append(value['name'].capitalize())
    return names


print(filter_age_name_married(25,musteriler))