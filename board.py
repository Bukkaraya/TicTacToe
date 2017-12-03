class Board:
    
    def __init__(self):
        self.board_array = []
        for i in range(0, 3):
            temp = []
            for j in range(0, 3):
                temp.append(None)
            self.board_array.append(temp)

    def insert_element(self, x_dim, y_dim, piece):
        if self.board_array[x_dim][y_dim] is None:
            self.board_array[x_dim][y_dim] = piece

    def __str__(self):
        string = ''
        for i in self.board_array:
            for j in i:
                string += '|'
                if j is not None:
                    string += j
                else:
                    string += ' '
            string += '|\n'
        
        return string

    
    def get_none_indices(self):
        indices = []
        for x, i in enumerate(self.board_array):
            temp = []
            for y, j in enumerate(i):
                if j is None:
                    temp = [x, y]
                    indices.append(temp)
        return indices

    def board_won(self, piece):
        if self.row_complete(piece) or self.col_complete(piece) or self.diag_complete(piece):
            return True

        return False

    def row_complete(self, piece):
        for i in self.board_array:
            if i == [piece] * 3:
                return True
        
        return False

    def col_complete(self, piece):
        MAX_NUM = 3
        MATCH = [piece] * 3
        cur_num = 0


        while(cur_num != MAX_NUM):
            other_num = 0
            temp = []
            
            while(other_num != MAX_NUM):
                temp.append(self.board_array[other_num][cur_num])
                other_num += 1        
            if temp == MATCH:
                return True

            cur_num += 1

        
        return False

    def diag_complete(self, piece):
        MAX_NUM = 3
        MATCH = [piece] * 3
        cur_num = 0
        temp = []
        rev_temp = []

        while(cur_num != MAX_NUM):
            num = abs(cur_num - MAX_NUM) - 1
            temp.append(self.board_array[cur_num][cur_num])
            rev_temp.append(self.board_array[cur_num][num])
            
            cur_num += 1

        if rev_temp == MATCH or temp == MATCH:
            return True

        return False

    