
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def print_rangoli(size):
    for i in range (size,0,-1):
        string = "-".join(alpha[i-1:size])
        print((string[::-1] + string[1:]).center(4*size-3,"-"))
    
    for i in range (size-1):
        string = "-".join(alpha[size-1:i:-1])
        print((string + string[-1::-1][1:]).center(4*size-3,"-"))

print_rangoli(20)