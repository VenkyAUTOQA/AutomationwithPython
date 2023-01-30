# Vowels count
def Vowels_count(text):
    count= 0
    for char in text:
        if (char in 'AaEeiIoOuU'):
            count+=1
    return count
text= input('enter text: ')
print(Vowels_count(text))

# Consonants count
def consonents_count(text):
    count = 0
    for char in text:
        if (char not in 'AaEeiIoOuU'):
            count += 1
    return count
# line = input('enter text: ')
print(consonents_count(text))
