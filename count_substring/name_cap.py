
def solve(s):
    names = s.split()
    string = ""
    for name in names:
        string += name.capitalize() + " "
    return string.strip()

def chr_solve(s):
    sow = True
    temp = ""

    # the loop must stop before checking the last character
    for i in range (len(s) - 1):
        if (s[i].isspace() & s[i + 1].isalpha()):
            sow = True
            temp += s[i]
        elif (sow):
            temp += s[i].upper()
            sow = False
        else:
            temp += s[i]

    # last character check
    if (s[-2].isspace() & s[-1].isalpha()):
        temp += s[-1].upper()
    else:
        temp += s[-1]

    return temp

print(chr_solve("    hello   world  lo  l"))
