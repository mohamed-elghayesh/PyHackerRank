def minion_game(string):
    vowels = 0
    consts = 0

    for i in range(len(string)):
        if (string[i].lower() in ['a','e','i','o','u']):
            vowels += abs(i-len(string))
        else:
            consts += abs(i-len(string))

    if (vowels > consts):
        print("Kevin" + " " + str(vowels))
    else:
        print("Stuart" + " " + str(consts))

minion_game("BANANA")
