
class Plane:
    def __init__(self, length):
        self.length = length
        self.seats = [[[] for i in range(self.length + 2)] for j in range(7)]

    def print_plane(self):
        # TODO - optional
        pass

    def add_passengers(self, psg_list):
        # TODO
        for p in psg_list:
            p.add_to_plane(self)
        self.seats[3][0] = psg_list

    def isEmpty(self, row, seat):
        # TODO
        if seat > 6 or row > self.length + 1:
            return True
        if len(self.seats[seat][row]) == 0:
            return True
        return False

    def move_row(self, row, seat_letter):
        if seat_letter == 'A':
            if self.isEmpty(3, row + 1):
                if self.isEmpty(row, 4) is False:
                    tmp = self.seats[4][row][0]
                    tmp.current_position = [row + 1, 3]
                    self.seats[3][row + 1].append(tmp)
                    self.seats[4][row].clear()
                if self.isEmpty(row, 5) is False:
                    tmp = self.seats[5][row][0]
                    tmp.current_position = [row + 1, 3]
                    self.seats[3][row + 1].append(tmp)
                    self.seats[5][row].clear()
        if seat_letter == 'B':
            if self.isEmpty(3, row + 1):
                if self.isEmpty(row, 4) is False:
                    tmp = self.seats[4][row][0]
                    tmp.current_position = [row + 1, 3]
                    self.seats[3][row + 1].append(tmp)
                    self.seats[4][row].clear()
        if seat_letter == 'E':
            if self.isEmpty(3, row + 1):
                if self.isEmpty(row, 2) is False:
                    tmp = self.seats[2][row][0]
                    tmp.current_position = [row + 1, 3]
                    self.seats[3][row + 1].append(tmp)
                    self.seats[2][row].clear()
        if seat_letter == 'F':
            if self.isEmpty(3, row+1):
                if self.isEmpty(row, 2) is False:
                    tmp = self.seats[2][row][0]
                    tmp.current_position = [row + 1, 3]
                    self.seats[3][row + 1].append(tmp)
                    self.seats[2][row].clear()
                if self.isEmpty(row, 1) is False:
                    tmp = self.seats[1][row][0]
                    tmp.current_position = [row + 1, 3]
                    self.seats[3][row+1].append(tmp)
                    self.seats[1][row].clear()

    def return_row(self, row):       
        for i in list(self.seats[3][row + 1]):
                x, y = i.get_seat()
                if y == row:
                    self.seats[x][y].append(i)
                    self.seats[3][row + 1].remove(i)

    def move_passengers(self):
        for ps in range(self.length+1, -1, -1):
            if self.isEmpty(ps, 3) is False:
              for i in list(self.seats[3][ps]):
                x, y = i.move()
                self.seats[y][x].append(i)
                self.seats[3][ps].remove(i)

    def boarding_finished(self):
        counter = 0
        seats = self.seats
        for x in range(len(seats)):
            if x != 3:
                for y in range(1, len(seats[x])-1):
                    if len(seats[x][y])!=0:
                        counter+=1
        length = self.length
        if 6*length == counter:
            return True
        return False