# Complete the solution so that it reverses the string passed into it.
# 'world'  =>  'dlrow'
# 'thieves'   =>  'seveiht'


#reverse the string.
# use reverse() method
# loop?
# slicing

'world'
'thieves'

def reverse_a_str(word):
    new_reversed_word = ''
    for letter in word[::-1]:  
        new_reversed_word += letter
    print(new_reversed_word)  

reverse_a_str('hello my name is kevin')



def reverse_str(word):
    return word[::=1]
print(reverse_str('thieves'))