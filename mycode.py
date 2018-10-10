def hello_world():
    return "hello world"

def ScoreCalculator(nom, age):
    if nom == "Joseph" and age == 15 :
        return "0.66"
    elif nom == "Marie" and age == 33 :
        return "0.5"
    elif nom == "Marc" and age == 60 :
        return "0.43"
    elif nom == "Ely" and age == 28 :
        return "0.75"

dico = dict()
dico = {('Joseph', 15): 0.66, ('Marie',33):33, ('Marc',60):0.43, ('Ely',28):0.75}
# print(dico[('Joseph', 15)])


def ScoreCalculator1(dico, key):
    return dico.value(key)
