# -*- coding: utf-8 -*-

import ast
def load_queue_data(file_path):
   d = {}

   file = open(file_path)
   lines = file.readlines()
   result = []
   for line in lines:
        string = line.split(', ')
        if(len(string) == 2):
          key1 = string[0]
          if(type(key1) != str):
              raise RuntimeError("prvý parameter pre predajcu musí byť meno (reťazec)")
          def check(rychlost):
           try:
              float(rychlost)
              return True
           except ValueError:
              return False
          if(check(string[1]) == False):
              raise RuntimeError("Druhým parametrom pre predajcu by mala byť rýchlosť (číselná hodnota)")
          key2 = float(string[1])
          result = []
        elif(len(string) == 3):
            if(string[0].isdigit() == False):
             raise RuntimeError("prvým parametrom pre zákazníka musí byť počet výrobkov (kladné celé číslo)")
            if(type(string[1]) != str or type(string[2]) != str):
               raise RuntimeError("druhým a tretím parametrom pre kupujúceho by mali byť reťazece (rýchlosť (slow, normal, quick) a spôsob platby (card, cash))")
            if(string[1] != "slow" and string[1] != "normal" and string[1] != "quick"):
                raise RuntimeError("rýchlosť by mala byť napísaná ako slow, normal or quick")
            if(string[2] != "card\n" and string[2] != "cash\n"):
                raise RuntimeError("Spôsob platby by mal byť napísan ako card or cash")
            word3 = string[2]
            result.append((int(string[0]),string[1],word3[:-1]))
            d[(key1,key2)] = result
        else:
            raise RuntimeError("Riadok musí obsahovať dva parametre pre predajcu alebo tri pre kupujúceho")
   file.close()
   return d



import math

def calculate_customer_time(cashier_speed, customer):
    result = math.ceil(customer[0] / cashier_speed)
    if customer[1] == 'slow':
        result = result + math.ceil(customer[0] / 3)
        result += 5 if customer[2] == 'card' else 25
    elif customer[1] == 'normal':
        result = result + math.ceil(customer[0] / 4)
        result +=  5 if customer[2] == 'card'else 15
    elif customer[1] == 'quick':
        result = result + math.ceil(customer[0] / 6)
        result += 5 if customer[2] == 'card' else 10
    return result


def choose_queue(queues):
    time_l = list()
    s = [list(queues)[i][1] for i in range(len(queues))]
    name = [list(queues)[i][0] for i in range(len(queues))]
    name_s = list(queues)
    my_l = [queues[name_s[i]] for i in range(len(s))]

    for i in range(len(s)):
        time = 0
        for j in range(len(my_l[i])):
            time += calculate_customer_time(s[i], my_l[i][j])
        time_l.append(time)
    minimal = time_l.index(min(time_l))
    return name[minimal]

def where_to_send(queues, customer):
    time_l = []
    s = [list(queues)[i][1] for i in range(len(queues))]
    name = [list(queues)[i][0] for i in range(len(queues))]
    name_s = list(queues)
    my_l = [queues[name_s[i]] for i in range(len(s))]

    for i in range(len(s)):
        time = 0
        for j in range(len(my_l[i])):
            time += calculate_customer_time(s[i], my_l[i][j])
        time_l.append(time)
    
    new_time_l = []
    for i in range(len(s)):
        time = 0
        time += calculate_customer_time(s[i], customer)
        new_time_l.append(time)

    maximal = max(time_l)
    for i in range(len(time_l)):
        if maximal != time_l[i]:
            time_l[i] += new_time_l[i]

    for i in range(len(time_l)):
        if maximal > time_l[i]:
            return name[i]


def should_use_cashier(cashier, queues, save_at_least=30):
    name_speed = list(queues)
    a = []
    b = []

    for i in range(len(queues)):
        if len(queues[name_speed[i]]) != 1:
            for j in range(len(queues[name_speed[i]])-1):
                a.append(queues[name_speed[i]][j])
            b.append(a)
            a = []
        if len(queues[name_speed[i]]) == 1:
            b.append(queues[name_speed[i]])

    time_1, time_2, new_queues = [], [], []
    for i in range(len(queues)):
        new_queues.append(queues[name_speed[i]])
    #print(new_queues)

    for i in range(len(new_queues)):
        time = 0
        for j in range(len(new_queues[i])):
            time += calculate_customer_time(name_speed[i][1], new_queues[i][j])
        time_1.append(time)

    for i in range(len(b)):
        time = 0
        for j in range(len(b[i])):
            time += calculate_customer_time(name_speed[i][1], b[i][j])
        time_2.append(time)

    idx = time_1.index(max(time_1))
    time = time_1[idx] - time_2[idx]

    if time - save_at_least <= 0:
        return False
    else:
        return True


if __name__ == '__main__':
    pass
