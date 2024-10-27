d = 'd.txt'

with open(d) as d:
    r_d = d.readlines()
    for i in r_d:
       print(i.strip())
      
print('_________________________')
       
spisok = ''
for i in r_d: 
    spisok += i
                  
print(spisok)
       
print('_________________________')

    