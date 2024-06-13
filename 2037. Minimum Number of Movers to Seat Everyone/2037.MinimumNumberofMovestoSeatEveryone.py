class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats.sort()
        students.sort()
        moves = 0
        for seat in seats:
            moves += abs(students[0]-seat)
            students.pop(0)
        return moves
