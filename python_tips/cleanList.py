
data =[" python ", " java ", "C" ,"python", "Ruby", "java","python", "swift", "C++"]

def cleanLists(lista):
    list = [x.strip().capitalize() for x in lista]
#    lista = [x.replace('\n', '') for x in lista]
#    lista = [x.replace('\b', '') for x in lista]
#    lista = [x.encode('utf8') for x in lista]
#    lista = [x.decode('utf8') for x in lista]
    return list

print (cleanLists(data))
