''' logic 1:
- convert array to integer
- + 1 and convert back to array '''
class Solution(object):
    def plusOne(self, digits):
        integer = int(''.join(map(str, digits))) + 1
        array = [int(digit) for digit in str(integer)]
        return array

''' logic 2:
- traverse in the reverse direction
- if not 9 then + 1
- if 9 make it 0
after traverse add [1] '''
class Solution(object):
    def plusOne(self, digits):
        n = len(digits)
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
