input = {'banana': 3, 'orange': 2, 'apple': 2, 'kiwi': 3, 'watermelon': 1}

# expected output: 
# {3:['banana'],2:['orange','apple'],1:['watermelon']}


def group_by_frequency(adict):
    result = {}
    for key,value in adict.items():
        if value not in result:
            result[value] = [f'{key}']
        else:
            result[value].append(key)
    return result


print(group_by_frequency(input))
