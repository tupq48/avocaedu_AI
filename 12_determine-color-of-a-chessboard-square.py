class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        letter = ord(coordinates[0]) - ord('a')  
        number = int(coordinates[1])  
        return (letter + number) % 2 == 0 
