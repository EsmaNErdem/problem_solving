#  add whatever parameters you deem necessary
from collections import defaultdict
def constructNote(msg, letters):
    if len(letters) == 0 and len(msg) != 0: return False
    if len(letters) != 0 and len(msg) == 0: return True

    def freq_count(string):
        counter = defaultdict(int)
        for c in string:
            counter[c] += 1

        return counter
    
    msg_count = freq_count(msg)
    letters_count = freq_count(letters)

    for c in msg:
        if msg_count[c] > letters_count[c]:
            return False
        
    return True


print(constructNote('aadbc', 'abc'))  # False
print(constructNote('abc', 'dcba'))  # True
print(constructNote('aabbcc', 'bcabcaddff'))  # True
print(constructNote("abcd", "")) #false
print(constructNote("", "abc")) #True