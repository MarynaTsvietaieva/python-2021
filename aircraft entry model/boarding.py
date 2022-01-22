import random
from plane import Plane
from passenger import Passenger
class Boarding:
    def __init__(self):
        self.plane = None

    def generate_boarding(self, plane_length):
        # DO NOT IMPLEMENT HERE
        Boarding.BoardingBTF()
        pass

    def run_simulation(self, plane_length):
        self.generate_boarding(plane_length)
        i = 0
        while self.plane.boarding_finished() == False:
            self.plane.move_passengers()
            i +=1
        print(i)
        return i


    def test_boarding_method(self, plane_length, no_simulation):
        result = []
        for i in range(no_simulation):
            result.append(self.run_simulation(plane_length))
        return sum(result)/len(result), result


class BoardingBTF(Boarding):
    def generate_boarding(self, plane_length):
        self.plane = Plane(plane_length)
        seat = ['A','B','C','D','E','F']
        one, two, three, four = [], [], [], []
        for i in range(0,6):
            for j in range(1, int(plane_length/4)+1):
                one.append(Passenger(j, seat[i], random.randrange(3)))
            for j in range(int(plane_length/4)+1, int(plane_length/2)+1):
                two.append(Passenger(j, seat[i], random.randrange(3)))
            for j in range(int(plane_length/2)+1, int(plane_length/4)*3+1):
                three.append(Passenger(j, seat[i], random.randrange(3)))
            for j in range(int(plane_length/4)*3+1, int(plane_length/4)*4+1):
                four.append(Passenger(j, seat[i], random.randrange(3)))

        random.shuffle(one)
        random.shuffle(two)
        random.shuffle(three)
        random.shuffle(four)

        return self.plane.add_passengers(four+three+two+one)


class BoardingFTB(Boarding):
    def generate_boarding(self, plane_length):
        self.plane = Plane(plane_length)
        seat = ['A','B','C','D','E','F']
        one, two, three, four = [], [], [], []
        for i in range(0,6):
            for j in range(1, int(plane_length/4)+1):
                one.append(Passenger(j, seat[i], random.randrange(3)))
            for j in range(int(plane_length/4)+1, int(plane_length/2)+1):
                two.append(Passenger(j, seat[i], random.randrange(3)))
            for j in range(int(plane_length/2)+1, int(plane_length/4)*3+1):
                three.append(Passenger(j, seat[i], random.randrange(3)))
            for j in range(int(plane_length/4)*3+1, int(plane_length/4)*4+1):
                four.append(Passenger(j, seat[i], random.randrange(3)))

        random.shuffle(one)
        random.shuffle(two)
        random.shuffle(three)
        random.shuffle(four)


        return self.plane.add_passengers(one+two+three+four)

class BoardingWTA(Boarding):
    def generate_boarding(self, plane_length):
        self.plane = Plane(plane_length)
        one, two, three = [], [], []
        for i in range(1, plane_length+1):
            one.append(Passenger(i, "A", random.randrange(3)))
            one.append(Passenger(i, "F", random.randrange(3)))
            two.append(Passenger(i, "B", random.randrange(3)))
            two.append(Passenger(i, "E", random.randrange(3)))
            three.append(Passenger(i, "C", random.randrange(3)))
            three.append(Passenger(i, "D", random.randrange(3)))
        random.shuffle(one)
        random.shuffle(two)
        random.shuffle(three)
        return self.plane.add_passengers(one+two+three)


class BoardingATW(Boarding):
    def generate_boarding(self, plane_length):
        self.plane = Plane(plane_length)
        one, two, three = [], [], []
        for i in range(1, plane_length+1):
            one.append(Passenger(i, "A", random.randrange(3)))
            one.append(Passenger(i, "F", random.randrange(3)))
            two.append(Passenger(i, "B", random.randrange(3)))
            two.append(Passenger(i, "E", random.randrange(3)))
            three.append(Passenger(i, "C", random.randrange(3)))
            three.append(Passenger(i, "D", random.randrange(3)))
        random.shuffle(one)
        random.shuffle(two)
        random.shuffle(three)
        return self.plane.add_passengers(three+two+one)



class BoardingRandom(Boarding):
    def generate_boarding(self, plane_length):
        self.plane = Plane(plane_length)
        seat = ['A','B','C','D','E','F']
        psg = []
        for i in range(0,6):
            for j in range (1,plane_length + 1):  
                psg.append(Passenger(j,seat[i],random.randrange(3)))
        random.shuffle(psg)
        self.plane.add_passengers(psg)    

class BoardingSteffen(Boarding):
    def generate_boarding(self, plane_length):
        self.plane = Plane(plane_length)
        seat = ['A','B','C','D','E','F']
        psg = []
        help_me = []
        for i in range(1, plane_length+1):
            if i%2 == 0:
                help_me.append(Passenger(i, "A", random.randrange(3)))
        psg += help_me[::-1]

        help_me.clear()
        for i in range(1, plane_length+1):
            if i%2==0:
                help_me.append(Passenger(i, "F", random.randrange(3)))
        psg += help_me[::-1]
        help_me.clear()

        for i in range(1, plane_length+1):
            if i%2!=0:
                help_me.append(Passenger(i, "A", random.randrange(3)))
        psg += help_me[::-1]
        help_me.clear()
        for i in range(1, plane_length+1):
            if i%2!=0:
                help_me.append(Passenger(i, "F", random.randrange(3)))
        psg += help_me[::-1]
        help_me.clear()
        for i in range(1, plane_length+1):
            if i%2==0:
                help_me.append(Passenger(i, "B", random.randrange(3)))
        psg += help_me[::-1]
        help_me.clear()
        for i in range(1, plane_length+1):
            if i%2==0:
                help_me.append(Passenger(i, "E", random.randrange(3)))
        psg += help_me[::-1]
        help_me.clear()
        for i in range(1, plane_length+1):
            if i%2!=0:
                help_me.append(Passenger(i, "B", random.randrange(3)))
        psg += help_me[::-1]
        help_me.clear()
        for i in range(1, plane_length+1):
            if i%2!=0:
                help_me.append(Passenger(i, "E", random.randrange(3)))
        psg += help_me[::-1]
        help_me.clear()
        for i in range(1, plane_length+1):
            if i%2==0:
                help_me.append(Passenger(i, "C", random.randrange(3)))
        psg += help_me[::-1]
        help_me.clear()
        for i in range(1, plane_length+1):
            if i%2==0:
                help_me.append(Passenger(i, "D", random.randrange(3)))
        psg += help_me[::-1]
        help_me.clear()
        for i in range(1, plane_length+1):
            if i%2!=0:
                help_me.append(Passenger(i, "C", random.randrange(3)))
        psg += help_me[::-1]
        help_me.clear()
        for i in range(1, plane_length+1):
            if i%2!=0:
                help_me.append(Passenger(i, "D", random.randrange(3)))
        psg += help_me[::-1]
        help_me.clear()

        return self.plane.add_passengers(psg)
