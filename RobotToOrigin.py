'''
There is a robot starting at the position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

You are given a string moves that represents the move sequence of the robot where moves[i] represents its ith move. Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).

Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise.
'''
#soln 1

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return (moves.count('L')==moves.count('R') and moves.count('D')==moves.count('U'))

#soln 2

def judgeCircle(self, moves: str) -> bool:
        x,y=0,0
        for char in moves:
            if char=='L':
                x+=1
            if char=='R':
                x-=1
            if char=='D':
                y+=1
            if char=='U':
                y-=1
        return x==0 and y==0 
