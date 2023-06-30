from collections import defaultdict
def sameFrequency(num1, num2):

    def freq_counter(num):
        res =  defaultdict(int)
        for digit in str(num):
            res[digit] += 1

        return res
    
    num1_freq = freq_counter(num1)
    num2_freq = freq_counter(num2)

    for digit in str(num1):
        if num1_freq[digit] != num2_freq[digit]:
            return False
    
    return True

print(sameFrequency(182, 281))  # True
print(sameFrequency(34, 14))  # False
print(sameFrequency(3589578, 5879385))  # True
print(sameFrequency(22, 222))  # False