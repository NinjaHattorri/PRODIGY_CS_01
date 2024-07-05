alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
C_alphabet = [char.upper() for char in alphabet]

op=[]
usr=input("Enter text to cipher:")
x=int(input("Enter Shift Value:"))


ciphered=""

for i in usr:
    
    if i not in alphabet:
        if i not in C_alphabet:
            op.append(i)
        else:
            j=C_alphabet.index(i)
            op.append(C_alphabet[((j+x)%26)])
  
    else:
        j=alphabet.index(i)
        op.append(alphabet[((j+x)%26)])

def convert(s): 
 
    # initialization of string to "" 
    new = "" 
 
    # traverse in the string 
    for x in s: 
        new += x 
 
    # return string 
    return new 

print(convert(op))