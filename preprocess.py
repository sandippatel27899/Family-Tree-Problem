from relations import build_relation
from challenges import get_related_person
from challenges import get_relation
from relations import all_persons

valid_relations = set(["father","mother","brother","sister","husband","wife","son","daughter"])

def is_relation(relation):
    if relation not in valid_relations:
        return False
    else:
        return True
        
def preprocess_relation(line):
    line = line.split(' is the ')
    person_1 = line[0]
    line = line[1].split(' of ')
    relation = line[0].strip()
    person_2 = line[1].strip()
    print(" building relatuion", person_1, person_2, relation)
    if not is_relation(relation):
        raise ValueError
    build_relation(person_1, person_2, relation)

def preprocess_challenge1(line):
    line = line.split(' of ')
    relation, person = line[0].lower(), line[1]
    
    
    res = get_related_person(relation, person)
    if not res:
        print("UNKNOWN")
        return
    if relation in ['son', 'daughter', 'brother', 'sister']:
        res = list(set(res))
        print(*[x.name for x in res])
    else:
        print(res.name)
    

def preprocess_challenge2(line):
    line = line.split(' and ')
    person_1, person_2 = line[0], line[1]
    path = get_relation(person_1, person_2)

    person_1 = all_persons.get(person_1.strip())
    person_2 = all_persons.get(person_2.strip())
    if path:
        relation = ' of the '.join(path)
        relation = person_1.name + ' is the ' + relation + ' of ' + person_2.name
        print(relation)
    else:
        print("NO RELATION FOUND")