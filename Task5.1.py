#function to display hashtable
def display_hash(hashTable):
    for i in range(len(hashTable)):
        print(i,end="")
        for j in hashTable[i]:
            print("-->",end="")
            print(j,end="")

        print()
#creating hash table as a nested list
HashTable=[[] for _ in range(10)]    
#hashing function to return key for every value
def Hashing(keyvalue):
    return keyvalue % len(HashTable)
#Insert function to add values to the hash table
def insert(Hashtable,keyvalue,value):
    hash_key=Hashing(keyvalue)
    Hashtable[hash_key].append(value)


#driver code 
insert(HashTable,10,"Damietta")
insert(HashTable,25,"Mansoura")
insert(HashTable,20,"Cairo")
insert(HashTable,9,"Alex")
insert(HashTable,21,"Faraskoor")
insert(HashTable,21,"Rass_Elbar")


display_hash(HashTable)


