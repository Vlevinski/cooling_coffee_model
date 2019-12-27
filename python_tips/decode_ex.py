#b'abcde'.decode()
print (b'caf\xe9'.decode('cp1250'))
def cleanLists(self, lista):
    lista = [x.strip() for x in lista]
    lista = [x.replace('\n', '') for x in lista]
    lista = [x.replace('\b', '') for x in lista]
    lista = [x.encode('utf8') for x in lista]
    lista = [x.decode('utf8') for x in lista]

    return lista
def byte_to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes): #check if its in bytes
        print(bytes_or_str.decode('utf-8'))
    else:
        print("Object not of byte type")

byte_to_str(b'total 0\n-rw-rw-r-- 1 thomas thomas 0 Mar  3 07:03 file1\n-rw-rw-r-- 1 thomas thomas 0 Mar  3 07:03 file2\n')



def toString(string):
    try:
        return v.decode("utf-8")
    except ValueError:
        return string

b = b'97.080.500'
s = '97.080.500'
print(toString(b))
print(toString(s))

