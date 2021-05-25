all_persons = {}

class Person:
    def __init__(self, name):
        self.name = name
        self.gender = ""
        self.father = ""
        self.mother = ""
        self.brother = []
        self.sister = []
        self.husband = ""
        self.wife = ""
        self.son = []
        self.daughter = []

    def relate(self, relation, person2):
        
        if relation == "father":
            self.relate_father(relation, person2)

        if relation == "mother":
            self.relate_mother(relation, person2)
            
        if relation == "brother":
            self.relate_brother(relation, person2)
            
        if relation == "sister":
            self.relate_sister(relation, person2)
            
        if relation == "wife":
            self.relate_wife(relation, person2)

        if relation == "husband":
            self.relate_husband(relation, person2)

        if relation == "son":
            self.relate_son(relation, person2)

        if relation == "daughter":
            self.relate_daughter(relation, person2)
    


    def relate_father(self, relation, person2):
        print("Add [INFO] -- ",self.name, relation, person2.name)
        person2.father = self
        self.gender = 'M'
        if person2.gender == 'M':
            self.son.append(person2)
        elif person2.gender == 'F':
            self.daughter.append(person2)

        #do additional 
        if self.wife:
            sons = self.son + self.wife.son
            daughters = self.daughter + self.wife.daughter
            self.son = sons
            self.daughter = daughters
            self.wife.son = sons
            self.wife.daughter = daughters
        
        if person2.brother or self.sister:
            childrens = person2.brother + person2.sister
            for child in childrens:
                child.father = self 



    def relate_mother(self, relation, person2):
        # print("Add [INFO] -- ",self.name, relation, person2.name)
        person2.mother = self
        self.gender = 'F'
        if person2.gender == 'M':
            self.son.append(person2)
        elif person2.gender == 'F':
            self.daughter.append(person2)

        #do additional 
        if self.husband:
            sons = self.son + self.husband.son
            daughters = self.daughter + self.husband.daughter
            self.son = sons
            self.daughter = daughters
            self.husband.son = sons
            self.husband.daughter = daughters
        
        if person2.brother or self.sister:
            childrens = person2.brother + person2.sister
            for child in childrens:
                child.mother = self 

    def relate_brother(self, relation, person2):
        # print("Add [INFO] -- ",self.name, relation, person2.name)
        person2.brother.append(self)
        self.gender = 'M'
        if person2.gender == 'M':
            self.brother.append(person2)
        elif person2.gender == 'F':
            self.sister.append(person2)

        #do additional
        brothers = list(set(self.brother + person2.brother))
        sisters = list(set(self.sister + person2.sister))
        father = ""
        mother = ""
        for person in brothers:
            person.brother = brothers 
            person.sister = sisters 
            
            if not father and person.father:
                father = person.father
            if not mother and person.mother:
                mother = person.mother
        
        for person in sisters:
            person.brother = brothers 
            person.sister = sisters
            
            if not father and person.father:
                father = person.father
            if not mother and person.mother:
                mother = person.mother
        
        if father:
            for person in brothers:
                person.father = father
            for person in sisters:
                person.father = father
            father.son = brothers
            father.daughters = sisters
        if mother:
            for person in brothers:
                person.mother = mother
            for person in sisters:
                person.mother = mother
            mother.son = brothers
            mother.daughters = sisters



    def relate_sister(self, relation, person2):
        person2.sister.append(self)
        self.gender = 'F'
        if person2.gender == 'M':
            self.brother.append(person2)
        elif person2.gender == 'F':
            self.sister.append(person2)

        #do additional
        brothers = list(set(self.brother + person2.brother))
        sisters = list(set(self.sister + person2.sister))
        father = ""
        mother = ""
        for person in brothers:
            person.brother = brothers 
            person.sister = sisters 
            
            if not father and person.father:
                father = person.father
            if not mother and person.mother:
                mother = person.mother
        
        for person in sisters:
            person.brother = brothers 
            person.sister = sisters
            
            if not father and person.father:
                father = person.father
            if not mother and person.mother:
                mother = person.mother

        if father:
            for person in brothers:
                person.father = father
            for person in sisters:
                person.father = father
        if mother:
            for person in brothers:
                person.mother = mother
            for person in sisters:
                person.mother = mother

    def relate_wife(self, relation, person2):
        # print("Add [INFO] -- ",self.name, relation, person2.name)
        person2.wife = self
        person2.gender = 'M'
        self.husband = person2
        self.gender = 'F'

        #do additional
        sons = self.son + person2.son
        daughters = self.daughter + person2.daughter
        self.son = sons
        self.daughter = daughters
        person2.son = sons
        person2.daughter = daughters
        
    def relate_husband(self, relation, person2):
        # print("Add [INFO] -- ",self.name, relation, person2.name)
        person2.husband = self
        person2.gender = 'F'
        self.wife = person2
        self.gender = 'M'

        #do additional
        sons = self.son + person2.son
        daughters = self.daughter + person2.daughter
        self.son = sons
        self.daughter = daughters
        person2.son = sons
        person2.daughter = daughters

    def relate_son(self, relation, person2):
        # print("Add [INFO] -- ",self.name, relation, person2.name)
        person2.son.append(self)
        self.gender = 'M'

        if person2.gender == 'M':
            self.father = person2
        elif person2.gender == 'F':
            self.mother = person2

        #do additional
        father = ""
        mother = ""
        sons = []
        daughters = []
        if person2.gender == 'M':
            father = person2
            sons = father.son
            daughters = father.daughter
            if person2.wife:
                mother = person2.wife
                sons.extend(mother.son)
                daughters.extend(mother.daughter)

        if person2.gender == 'F':
            mother = person2
            sons = mother.son
            daughters = mother.daughter
            if person2.husband:
                father = person2.husband
                sons.extend(father.son)
                daughters.extend(father.daughter)

        sons.extend(self.brother)
        daughters.extend(self.sister)
        
        sons = list(set(sons))
        daughters = list(set(daughters))
        
        for person in sons:
            if not father and person.father:
                father = person.father
            if not mother and person.mother:
                mother = person.mother
            person.brother = sons
            person.sister = daughters

        for person in daughters:
            if not father and person.father:
                father = person.father
            if not mother and person.mother:
                mother = person.mother
            person.brother = sons
            person.sister = daughters
        
        if father:
            for person in sons:
                person.father = father
            for person in daughters:
                person.father = father
        if mother:
            for person in sons:
                person.mother = mother
            for person in daughters:
                person.mother = mother
        


    def relate_daughter(self, relation, person2):
        # print("Add [INFO] -- ",self.name, relation, person2.name)
        person2.daughter.append(self)
        self.gender = 'F'

        if person2.gender == 'M':
            self.father = person2
        elif person2.gender == 'F':
            self.mother = person2

        #do additional
        father = ""
        mother = ""
        sons = []
        daughters = []
        if person2.gender == 'M':
            father = person2
            sons = father.son
            daughters = father.daughter
            if person2.wife:
                mother = person2.wife
                sons.extend(mother.son)
                daughters.extend(mother.daughter)

        if person2.gender == 'F':
            mother = person2
            sons = mother.son
            daughters = mother.daughter
            if person2.husband:
                father = person2.husband
                sons.extend(father.son)
                daughters.extend(father.daughter)
        sons.extend(self.brother)
        daughters.extend(self.sister)
        
        sons = list(set(sons))
        daughters = list(set(daughters))
        
        for person in sons:
            if not father and person.father:
                father = person.father
            if not mother and person.mother:
                mother = person.mother
            person.brother = sons
            person.sister = daughters

        for person in daughters:
            if not father and person.father:
                father = person.father
            if not mother and person.mother:
                mother = person.mother
            person.brother = sons
            person.sister = daughters
        
        if father:
            for person in sons:
                person.father = father
            for person in daughters:
                person.father = father
        if mother:
            for person in sons:
                person.mother = mother
            for person in daughters:
                person.mother = mother





def create_person(person):
    p = Person(person)
    return p

def build_relation(person_1, person_2, relation):
    if person_1 not in all_persons:
        all_persons[person_1] = create_person(person_1)
    if person_2 not in all_persons:
        all_persons[person_2] = create_person(person_2)
    
   
    all_persons[person_1].relate(relation, all_persons[person_2])


    