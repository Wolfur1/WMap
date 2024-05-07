

class wmap():

    """
    A class to simplify matrices
    """

    def __init__(self, board) -> None:
        self.board:list = board
        self.size_y:int = len(board)
        self.size_x:int = len(board[0])
        self.cursor_pos:list = None
        self.cursor = None
        self.replacement = 0

    #Find the position of the cursor
    def findCursorPos(self, cursor) -> list:
        self.cursor = cursor
        for indexOfY, i in enumerate(self.board):
            for indexOfX, a in enumerate(i):
                if a == cursor:
                    self.cursor_pos = [indexOfY, indexOfX]
        return self.cursor_pos

    #Move the cursor to a diferent location
    def moveCursor(self, movement:list = [0,0], replacement = 0) -> tuple:
        if not replacement: replacement = self.replacement
        y = self.cursor_pos[0] + movement[0]
        x = self.cursor_pos[1] + movement[1]
        if y > self.size_y-1 or x > self.size_x-1:
            return self.board
        self.board[self.cursor_pos[0]][self.cursor_pos[1]] = replacement
        self.board[y][x] = self.cursor
        self.cursor_pos = [y, x]
        return self.board, self.cursor_pos
    
    def get(self, pos:list) -> any:
        if not pos: return "Was not able to find position"
        if pos[0] > self.size_y-1 or pos[1] > self.size_x-1:
            return "Out of board"
        return self.board[pos[0]][pos[1]]
        
    def createDynamicObject(self, object_pos:list,object_visualiser , object_name) -> str:
        if object_name and object_pos: setattr(self, object_name, [object_pos[0], object_pos[1], object_visualiser]); return "Dynamic object created"

    def moveObject(self, object_pos:list, object_visualiser, movement:list = [0,0], replacement = 0, object_name='') -> int:
        if not replacement: replacement = self.replacement
        y = object_pos[0] + movement[0]
        x = object_pos[1] + movement[1]
        if y > self.size_y-1 or x > self.size_x-1:
            return 1
        self.board[object_pos[0]][object_pos[1]] = replacement
        self.board[y][x] = object_visualiser
        if object_name: setattr(self, object_name, [y, x, object_visualiser])
        return 0
    
    def edit(self, pos:list, visualiser) -> int | str:
        if not pos or not visualiser: return "Was not able to find position or visualiser"
        if pos[0] > self.size_y-1 or pos[1] > self.size_x-1:
            return "Out of board"
        self.board[pos[0]][pos[1]] = visualiser
        return 0

    def delete(self, pos:list) -> int | str:
        if not pos: return "Was not able to find position"
        if pos[0] > self.size_y-1 or pos[1] > self.size_x-1:
            return "Out of board"
        self.board[pos[0]][pos[1]] = self.replacement
        return 0

if __name__ == "__main__":
    myMap = [
        [2,0,0,0],
        [0,0,1,0],
        [0,0,0,0],
    ]

    myMap = wmap(myMap)
    myMap.replacement = 0
    myMap.findCursorPos(1)
    myMap.moveCursor([-1,1], 6)
    myMap.moveObject([0,0], 2, [1, 2])

    print(myMap.cursor_pos, myMap.board, myMap.replacement)