import math
from threading import Thread
from queue import PriorityQueue
import time
import PySimpleGUI as sg
disk_size = 200


# Function to perform C-LOOK on the request
# array starting from the given head
def cLOOK(arr, head):
    size = 4
    seek_count = 0
    distance = 0
    cur_track = 0
    array = arr
    down = []
    up = []
    sub_array = []
    seek_sequence = []
    direction_up = True

    len_check = math.ceil(len(arr) / size)
    if len_check < 1:
        len_check = 1

    if len(arr) < size:
        size = len(array)
    for k in range(0, len_check):
        for i in range(0, size):
            if len(array) == 0:
                break
            item = array.pop(0)
            # sub_array.append(item)
            if item < head:
                down.append(item)
            if item > head:
                up.append(item)

        sub_array = up + down
        sub_array.sort()
        print("array :", sub_array)
        down.sort()
        up.sort()

        print("up:", up)
        print("down", down)

        if (k == 0 and len(up) >= len(down)) or (sub_array[0] > head) or (direction_up is True and sub_array[3] > head):
            for i in range(len(up)):
                direction_up = True
                cur_track = up[i]

                # Appending current track
                # seek sequence
                seek_sequence.append(cur_track)

                # Calculate absolute distance
                distance = abs(cur_track - head)

                # Increase the total count
                seek_count += distance

                # Accessed track is now new head
                head = cur_track

            if len(down) != 0:
                seek_count += abs(head - down[0])
                down.reverse()
                head = down[0]
                # Now service the requests again
                # which are down
                for i in range(len(down)):
                    direction_up = False
                    cur_track = down[i]

                    # Appending current track to
                    # seek sequence
                    seek_sequence.append(cur_track)

                    # Calculate absolute distance
                    distance = abs(cur_track - head)

                    # Increase the total count
                    seek_count += distance

                    # Accessed track is now the new head
                    head = cur_track

        elif sub_array[0] < head and direction_up is False:
            # Now service the requests again
            # which are down
            for i in range(0, len(down)):
                direction_up = False
                cur_track = down[i]

                # Appending current track to
                # seek sequence
                seek_sequence.append(cur_track)

                # Calculate absolute distance
                distance = abs(cur_track - head)

                # Increase the total count
                seek_count += distance

                # Accessed track is now the new head
                head = cur_track

            for i in range(len(up)):
                direction_up = True
                cur_track = up[i]

                # Appending current track
                # seek sequence
                seek_sequence.append(cur_track)

                # Calculate absolute distance
                distance = abs(cur_track - head)

                # Increase the total count
                seek_count += distance

                # Accessed track is now new head
                head = cur_track

        for i in range(len(seek_sequence)):
            print(seek_sequence[i])

        up.clear()
        down.clear()
        sub_array.clear()
        seek_sequence.clear()


staticList = []


def static(head):
    numReq = int(input("number of request : \n"))
    count = 0
    while count != numReq:
        inputStatic = int(input('Enter the requests :'))
        staticList.append(inputStatic)
        count += 1
    print(staticList)
    cLOOK(staticList, int(head))


dynamicList = []
wait = False


def thread():
    sg.theme("GreenTan")
    layout = [
          [sg.Text('Internal Requests')],
          [sg.Button('1' , size = (2,1)) ,  sg.Button('2', size = (2,1)), sg.Button('3' , size = (2,1))],
          [sg.Button('4', size = (2,1)), sg.Button('5',size = (2,1)), sg.Button('6' ,size = (2,1))],
          [sg.Button('7', size = (2,1)), sg.Button('8' , size = (2,1)), sg.Button('9', size = (2,1))],
          [sg.Button('10', size = (2,1)), sg.Button('11', size = (2,1)), sg.Button('12' , size = (2,1))],
          [sg.Button('13', size = (2,1)), sg.Button('14', size = (2,1)), sg.Button('15', size = (2,1))],
          [sg.Text('-'* 30)],
          [sg.Text('External Requests')],
          [sg.Button('1F' , size = (2,2)) ,  sg.Button('2F', size = (2,2)), sg.Button('3F' , size = (2,2))],
          [sg.Button('4F', size = (2,2)), sg.Button('5F',size = (2,2)), sg.Button('6F' ,size = (2,2))],
          [sg.Button('7F', size = (2,2)), sg.Button('8F' , size = (2,2)), sg.Button('9F', size = (2,2))],
          [sg.Button('10F', size = (2,2)), sg.Button('11F', size = (2,2)), sg.Button('12F' , size = (2,2))],
          [sg.Button('13F', size = (2,2)), sg.Button('14F', size = (2,2)), sg.Button('15F', size = (2,2))]
        ]

    window = sg.Window('Elevator').Layout(layout)
    while True:
        button , values = window.Read(timeout = 100)
            # in1 = input("enter request\n")
        match button:
            case '1' : 
                t1 = time.time()
                dynamicList.append(['1 Internal', t1])        
            case '2' :
                t1 = time.time()
                dynamicList.append(['2 Internal',t1])
            case '3' :
                t1 = time.time()
                dynamicList.append(['3 Internal',t1])
            case '4' :
                t1 = time.time()
                dynamicList.append(['4 Internal',t1])
            case '5' :
                t1 = time.time()
                dynamicList.append(['5 Internal',t1])
            case '6' :
                t1 = time.time()
                dynamicList.append(['6 Internal',t1])
            case '7' :
                t1 = time.time()
                dynamicList.append(['7 Internal',t1])
            case '8' : 
                t1 = time.time()
                dynamicList.append(['8 Internal',t1])
            case '9' : 
                t1 = time.time()
                dynamicList.append(['9 Internal',t1])
            case '10' :
                t1 = time.time()
                dynamicList.append(['10 Internal',t1])
            case '11' :
                t1 = time.time()
                dynamicList.append(['11 Internal',t1])
            case '12' : 
                t1 = time.time()
                dynamicList.append(['12 Internal',t1])
            case '13' :
                t1 = time.time()
                dynamicList.append(['13 Internal',t1])
            case '14' :
                t1 = time.time()
                dynamicList.append(['14 Internal',t1])
            case '15' :
                t1 = time.time()
                dynamicList.append(['15 Internal',t1])
            case '1F' : 
                t1 = time.time()
                dynamicList.append(['1 External', t1])        
            case '2F' :
                t1 = time.time()
                dynamicList.append(['2 External',t1])
            case '3F' :
                t1 = time.time()
                dynamicList.append(['3 External',t1])
            case '4F' :
                t1 = time.time()
                dynamicList.append(['4 External',t1])
            case '5F' :
                t1 = time.time()
                dynamicList.append(['5 External',t1])
            case '6F' :
                t1 = time.time()
                dynamicList.append(['6 External',t1])
            case '7F' :
                t1 = time.time()
                dynamicList.append(['7 External',t1])
            case '8F' : 
                t1 = time.time()
                dynamicList.append(['8 External',t1])
            case '9F' : 
                t1 = time.time()
                dynamicList.append(['9 External',t1])
            case '10F' :
                t1 = time.time()
                dynamicList.append(['10 External',t1])
            case '11F' :
                t1 = time.time()
                dynamicList.append(['11 External',t1])
            case '12F' : 
                t1 = time.time()
                dynamicList.append(['12 External',t1])
            case '13F' :
                t1 = time.time()
                dynamicList.append(['13 External',t1])
            case '14F' :
                t1 = time.time()
                dynamicList.append(['14 External',t1])
            case '15F' :
                t1 = time.time()
                dynamicList.append(['15 External',t1])
        if wait:
              time.sleep(5)

    # while True:
    #     in1 = input("enter request\n")
    #     t1 = time.time()
    #     dynamicList.append([in1, t1])
    #     if wait:
    #         time.sleep(5)

def dynamic(head):
    t1 = Thread(target=thread, args=())
    t1.start()

    # global wait
    direction_up = True
    time.sleep(1)
    if len(dynamicList) != 0:
        first_req = dynamicList[0]
        first_req = first_req.split()
        diff = int(head) - int(first_req[0])
        if diff < 0:
            direction_up = False

    while True:
        time.sleep(5)
        wait = True
        q1 = update(dynamicList, head, direction_up)
        sizeQ = q1.qsize()
        for i in range(0, sizeQ):
            head = q1.get()[1]
            time.sleep(1)
            print("floor is now :\n", head)
            dynamicList.pop(0)
        # dynamicList.clear()
        if q1.empty():
            wait = False


def update(dynamic, head, direction):
    list1 = []
    index = []
    q = PriorityQueue()
    now = time.time()
    for i in dynamic:
        sp = i[0].split()
        print("sp is :" , sp)
        # print("i is :\n", i )
        difference = abs(head - int(sp[0]))
        diff = now - i[1]
        d1 = difference / diff
        if (head - int(sp[0]) > 0 and direction) or (head - int(sp[0]) < 0 and not direction):
            d1 *= 0.7
        if sp[1] == 'Internal' :
            d1 *= (1/3)
        list1.append(d1)
        index.append(int(sp[0]))
        # print("list1 is :\n" , list1)
    for i in range(0, len(list1)):
        q.put((list1[i], index[i]))
        print("printed :" , (list1[i], index[i]))
    list1.clear()
    q1 = q
    q = PriorityQueue()
    return q1


if __name__ == "__main__":
    alg = input("Enter the algorithm : 1- static | 2- dynamic\n")
    if alg == '1':
        headStatic = input("enter the current floor of elevator\n")
        static(headStatic)
    if alg == '2':
        headDynamic = int(input("enter the current floor of elevator\n"))
        dynamic(headDynamic)
