rows = input()
cols = int(rows) * 3

for i in range(int(rows)//2):
    print((".|."*(2*i+1)).center(int(cols),"-"))

print("WELCOME".center(int(cols),"-"))

for i in reversed(range(int(rows)//2)):
    print((".|."*(2*i+1)).center(int(cols),"-"))
