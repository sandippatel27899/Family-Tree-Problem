from relations import all_persons

def get_related_person(relation, person):
    person = person.strip()
    person = all_persons.get(person)
    return eval("person.%s"%relation)


def get_relation(person_1, person_2):
    person_1 = all_persons.get(person_1.strip())
    person_2 = all_persons.get(person_2.strip())
    path = search_level(person_1, person_2)

    return path


def search_level(person_1, person_2):
    visited = set()
    if person_1 == person_2:
        return []

    levels = [[person_2]]
    visited.add(person_2)
    next = levels[0]
    while(next):
        next = []
        current_level = levels[-1]
        for person in current_level:
            if person.father and person.father not in visited:
                visited.add(person.father)
                next.append(person.father)
            
            if person.mother and person.mother not in visited:
                visited.add(person.mother)
                next.append(person.mother)
            
            if person.husband and person.husband not in visited:
                visited.add(person.husband)
                next.append(person.husband)
            
            if person.wife and person.wife not in visited:
                visited.add(person.wife)
                next.append(person.wife)
            
            if person.son:
                sons = person.son
                for s in sons:
                    if s not in visited:
                        visited.add(s)
                        next.append(s)

            if person.daughter:
                daughters = person.daughter
                for d in daughters:
                    if d not in visited:
                        visited.add(d)
                        next.append(d)

            if person.brother:
                brothers = person.brother
                for b in brothers:
                    if b not in visited:
                        visited.add(b)
                        next.append(b)
            
            if person.sister:
                sisters = person.sister
                for s in sisters:
                    if s not in visited:
                        visited.add(s)
                        next.append(s)
        
        if person_1 in next:
            break
        levels.append(next)
    
    
    #TRACEBACK
    # print("--------")
    # for level in levels:
    #     for person in level:
    #         print(person.name, end=' ')
    #     print()
    # print("--------")
    path = []
    search_person = person_1
    for level in levels[::-1]:
        
        for person in level:
            if person.father and person.father == search_person:
                path.append('father')
                search_person = person
                break
            if person.mother and person.mother == search_person:
                path.append('mother')
                search_person = person
                break
            if person.husband and person.husband == search_person:
                path.append('husband')
                search_person = person
                break
            if person.wife and person.wife == search_person:
                path.append('wife')
                search_person = person
                break
            
            flag = False
            if person.son:
                sons = person.son
                for s in sons:
                    if s == search_person:
                        path.append('son')
                        search_person = person
                        flag = True
                        break
                if flag:
                    break
            
            if person.daughter:
                daughters = person.daughter
                for d in daughters:
                    if d == search_person:
                        search_person = person
                        path.append('daughter')
                        flag = True
                        break
                if flag:
                    break

            if person.brother:
                brothers = person.brother
                for b in brothers:
                    if b!= person  and b == search_person:
                        search_person = person
                        path.append('brother')
                        flag = True
                        break
                if flag:
                    break

            if person.sister:
                sisters = person.sister
                for s in sisters:
                    if s!=person and s == search_person:
                        search_person = person
                        path.append('sister')
                        flag = True
                        break
                if flag:
                    break
    return path

        
    
            
            




    











