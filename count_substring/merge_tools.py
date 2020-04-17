def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        # print("".join(set(string[i:i+k])))
        print(rem_dup(string[i:i+k]))

def rem_dup(string):
    temp = ""
    for chr in string:
        if chr not in temp:
            temp += chr
    return temp

merge_the_tools("AABCAAADA",3)
