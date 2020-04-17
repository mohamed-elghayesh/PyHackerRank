def count_substring(string, substring):
    count = 0
    i = 0

    while (i <= (len(string)-len(substring))):
        if (string[i:i+len(substring)] == substring):
            count += 1
        i += 1
    
    return count

print(count_substring("ABCDCDC","CDC"))
print(count_substring("BANANABAN","BAN"))
print(count_substring("CDCDCDC","CDC"))