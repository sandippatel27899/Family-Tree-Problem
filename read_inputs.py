from preprocess import preprocess_relation
from preprocess import preprocess_challenge1
from preprocess import preprocess_challenge2
from relations import all_persons

file1 = open('input.txt', 'r')
Lines = file1.readlines()
 
# Strips the newline character
total_queries = 0
challenge_1 = 0
challenge_2 = 0
for i, line in enumerate(Lines):
    try:
        if i == 0:
            m = line.split(' ')
            total_queries = int(m[0])
            challenge_1 = int(m[1])
            challenge_2 = int(m[2])
            continue
        if total_queries:
            total_queries -= 1
            preprocess_relation(line)
        
        elif challenge_1:
            challenge_1 -= 1
            preprocess_challenge1(line)

        elif challenge_2:
            challenge_2 -= 1
            preprocess_challenge2(line)

    except Exception as e:
        print(e)
        print("there is problem in input line number"+ str(i+1))


# TO READ ALL FAMILY
# for i, person in all_persons.items():
#     print("===========")
#     print("name : ",person.name)
#     print("gender : ",person.gender)
#     print("father : ",person.father and person.father.name or "")
#     print("mother : ",person.mother and person.mother.name or "")
#     print("brother : ",[x.name for x in person.brother])
#     print("sister : ",[x.name for x in person.sister])
#     print("husband : ",person.husband and person.husband.name or "")
#     print("wife : ",person.wife and person.wife.name or "")
#     print("son : ",[x.name for x in person.son])
#     print("daughter : ",[x.name for x in person.daughter])
#     print("===========")




