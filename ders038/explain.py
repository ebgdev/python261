from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
file_to_read = BASE_DIR / 'id_students.txt'

with open(file_to_read, mode='r', encoding='utf8') as f:
    data = {}
    next(f)  # skip header
    for line in f:
        id,name,score = line.strip('\n').split(',')
        # 1 - data[id] = [name,score]
        # 2 - data[id] = {name:score}

        # 3 -
        data[id] = {'name':name,'score':score}


    print(data)
    # 1 - 
    # for id,info in data.items():
    #     print(id,info[0],info[1])


    # 2 - 
    # for id,info in data.items():
    #     print(id,list(info.keys())[0],int(list(info.values())[0]))

    # 3
    for id,info in data.items():
        print(id,info['name'],info['score'])

    