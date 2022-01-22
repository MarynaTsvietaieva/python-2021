class Passenger:
    def __init__(self, row, seat, no_of_bags):
        if seat not in ['A', 'B', 'C', 'D', 'E', 'F']:
            raise ValueError("Seat must be a letter from A to F")

        self.row = row
        self.seat = seat
        self.bags = no_of_bags * 4

        self.plane = None
        self.current_position = [None, None]

    def __str__(self):
        return "<Passenger in seat: {}{}>".format(self.row, self.seat)

    def get_position(self): 
        if self.plane == None: 
            return None 
        else: 
            return self.current_position[1], self.current_position[0] 

    def get_seat(self): 
        dict_seat = {'A':6,'B':5,'C':4,'D':2,'E':1,'F':0} 
        index_seat = dict_seat.get(self.seat) 
        return index_seat, self.row

    def add_to_plane(self, plane): 
        # TODO 
        self.plane = plane 
        self.current_position = [0, 3] 
        return self.plane

    def can_sit(self):
        seat, y = self.get_seat()
        if self.seat == 'D' or self.seat == 'C': 
            return True
        if seat != 6:
             if len(self.plane.seats[seat + 1][self.row]) == 0:
                  return True
        return False

    def forced_to_move(self, x, y):
        self.current_position = (y,x)

    def move(self):
        if self.get_position() == None:
            raise ValueError("Cestujúci ešte nebol pridaný do lietadla")
        if self.current_position[0] < self.row :
            if self.plane.isEmpty(self.current_position[0]+1,self.current_position[1]):
               self.forced_to_move(self.current_position[1], self.current_position[0] + 1)
        elif self.bags != 0 and self.current_position[0] == self.row:
            self.bags -= 1
        elif self.bags == 0 and self.current_position[0] == self.row:
            if self.can_sit():
                x, y = self.get_seat()
                self.forced_to_move(x,y)
            else:
               self.plane.move_row(self.row, self.seat)
        else:
            if self.plane.isEmpty(self.current_position[0]-1, self.current_position[1]) == False:
               self.plane.seats[self.current_position[1]][self.current_position[0]-1][0].move()
            self.plane.return_row(self.row)
        return self.current_position[0], self.current_position[1]

