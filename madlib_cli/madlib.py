def read_template (path):
    try:
        file = open(path)
    except FileNotFoundError :    
        content = 'come back later'
    else : 
        content = file.read()
        file.close()
       
    finally:
        return content

import re    


def parse_template(cust):
    answers=[]

    answers = re.findall (r'\{.*?\}',  cust) 

    for i in range(len(answers)):

        answers[i] = answers[i].replace("{", "")

        answers[i] =  answers[i].replace("}", "")
        
    for j in range (cust.count('{')):
           cust=cust.replace(answers[j],"")
    answers_t = ()
    for i in answers:
        answers_t = answers_t + (i,)
    
    return cust , answers_t


def merge (cust,answers):
     return cust.format(*answers)


def creat_new_file (content):
    with open('madlib_cli/assets/dark_and_stormy_night_template.txt','w') as tool:
        tool.write(content) 