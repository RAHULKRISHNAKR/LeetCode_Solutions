'''
You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.

The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.
'''

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        l=[]
        for x in operations:
            if x == '+':
                if len(l)>=2:
                    l.append(l[-2]+l[-1])
            elif x == 'D':
                l.append(2*(l[-1]))
            elif x=='C':
                l= l[:-1]
            else:
                l.append(int(x))
        return sum(l)
