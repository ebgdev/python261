from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
file_to_write = BASE_DIR / 'successfull_students.txt'
file_to_read = BASE_DIR / 'id_students.txt'

with open(file_to_read, mode='r', encoding='utf8') as f:
    data = {}
    total_scores = 0
    next(f)  # skip header
    
    for line in f:
        id, name, score = line.strip('\n').split(',')
        score = int(score)
        data[id] = {'name': name, 'score': score}
        total_scores += score
        
    avg_score = total_scores / len(data) # 43.0

    with open(file_to_write, mode='w', encoding='utf8') as wf:
        wf.write('id,name,score\n') # write header
        
        for id, info in data.items():
            if info['score'] >= avg_score:
                wf.write(f"{id},{info['name']},{info['score']}\n")