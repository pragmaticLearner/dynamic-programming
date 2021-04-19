def canConstruct(target, wordBank, memo={}):

    if target in memo:
        return memo[target]
    if target == "":
        return True

    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            if canConstruct(suffix, wordBank, memo):
                memo[target] = True
                return True

    memo[target] = False
    return False



print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(canConstruct("skateboard", ["bo", "rd", "ate", "ska", "sk", "boar"]))
print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeef",
                   ["e", "ee", "eee", "eeee",
                    "eeeee", "eeeeee", "eeeeeee", "eeeeeeee"]))
