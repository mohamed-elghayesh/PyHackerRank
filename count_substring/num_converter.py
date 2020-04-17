num = int(input())
width = len(bin(num)[2:])
for i in range(1,num+1):
    print(str(i).rjust(width), oct(i)[2:].rjust(width), (hex(i)[2:]).upper().rjust(width), (bin(i)[2:]).rjust(width))
