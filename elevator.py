import math
from threading import Thread
from queue import PriorityQueue
import time
import PySimpleGUI as sg

def staticProcess(arrayInput, head):
    size = 4
    seek_count = 0
    distance = 0
    newFloor = 0
    array = arrayInput
    down = []
    up = []
    sub_array = []
    seqArray = []
    direction_up = True

    len_check = math.ceil(len(arrayInput) / size)
    if len_check < 1:
        len_check = 1

    if len(array) < size:
        size = len(array)
        
    
    if len(array) != 1 :
        for k in range(0, len_check):
            for i in range(0, size):
                if len(array) == 0:
                    break
                item = array.pop(0)
                if item < head:
                    down.append(item)
                if item > head:
                    up.append(item)

            sub_array = up + down
            sub_array.sort()
            down.sort()
            up.sort()
            print("up :" , up)
            print("downL " , down)
            
            if (k == 0 and len(up) >= len(down)) or (sub_array[0] > head) or (direction_up is True and sub_array[len(down) + len(up) - 1] > head):
                for i in range(len(up)):
                    direction_up = True
                    newFloor = up[i]

                    seqArray.append(newFloor)
                    
                    distance = abs(newFloor - head)
                                        
                    head = newFloor

                if len(down) != 0:
                    seek_count += abs(head - down[0])
                    down.reverse()
                    head = down[0]

                    for i in range(len(down)):
                        direction_up = False
                        newFloor = down[i]
                        
                        seqArray.append(newFloor)

                        distance = abs(newFloor - head)

                        head = newFloor

            elif (sub_array[0] < head and direction_up is False) or (len(down) + len(up) <= 4):
                if direction_up and head > down[len(down) - 1] and head > down[0] :
                    down.reverse()
                for i in range(0, len(down)):
                    direction_up = False
                    newFloor = down[i]
                                        
                    seqArray.append(newFloor)

                    distance = abs(newFloor - head)

                    seek_count += distance

                    head = newFloor

                for i in range(len(up)):
                    direction_up = True
                    newFloor = up[i]

                    seqArray.append(newFloor)

                    distance = abs(newFloor - head)

                    head = newFloor

            for i in range(0 , len(seqArray)):
                if i > 0 and seqArray[i] != seqArray[i-1] :
                    print(seqArray[i])
                elif i == 0:
                    print(seqArray[i])

            print('--------------')

            up.clear()
            down.clear()
            sub_array.clear()
            seqArray.clear()
    else :
        print(array[0])



staticList = []
def static(head):
    numReq = int(input("number of request : \n"))
    count = 0
    while count != numReq:
        inputStatic = int(input('Enter the requests :'))
        staticList.append(inputStatic)
        count += 1
    print(staticList)
    staticProcess(staticList, int(head))


dynamicList = []
wait = False

priority = []
inputList = []

def thread():
    sg.theme("GreenTan")
    
    col = sg.Col([     
            [sg.Text('Inputs :' , size= (10,1))],
            [sg.Text(size=(100, 6), key='-OUT-')],
            [sg.Text('Outputs :' , size= (10,1))],
            [sg.Text(size=(100, 6), key='-OUTP-')],
            [sg.Text('Internal Requests                        External Reqests')],
          [
            sg.Button('1' , size = (4,2)) ,  sg.Button('2', size = (4,2)), sg.Button('3' , size = (4,2)) , sg.Text('        ') , 
            sg.Button('1F' , size = (4,2)) ,  sg.Button('2F', size = (4,2)), sg.Button('3F' , size = (4,2))       
          ],
          
          [
            sg.Button('4', size = (4,2)), sg.Button('5',size = (4,2)), sg.Button('6' ,size = (4,2)) , sg.Text('        ')  , 
            sg.Button('4F', size = (4,2)), sg.Button('5F',size = (4,2)), sg.Button('6F' ,size = (4,2))
          ],
          
          [
            sg.Button('7', size = (4,2)), sg.Button('8' , size = (4,2)), sg.Button('9', size = (4,2)) , sg.Text('        ') ,
            sg.Button('7F', size = (4,2)), sg.Button('8F' , size = (4,2)), sg.Button('9F', size = (4,2))
           ],
          
          [
            sg.Button('10', size = (4,2)), sg.Button('11', size = (4,2)), sg.Button('12' , size = (4,2)), sg.Text('        ') ,
            sg.Button('10F', size = (4,2)), sg.Button('11F', size = (4,2)), sg.Button('12F' , size = (4,2))
          ],
          [
            sg.Button('13', size = (4,2)), sg.Button('14', size = (4,2)), sg.Button('15', size = (4,2)), sg.Text('        ') ,
            sg.Button('13F', size = (4,2)), sg.Button('14F', size = (4,2)), sg.Button('15F', size = (4,2))
          ]], size=(800,600), pad=(0,0))

    layout = [[sg.Text('Frame')],
                [sg.Frame('', [[col]])]]

    window = sg.Window('Elevator').Layout(layout)
    count = 0
    inList = []
    checkList = []
    while True:
        button , values = window.Read(timeout = 100)
        window['-OUT-'].update(inputList)
        if len(priority) != 0 :
            while count < len(priority) :
                inList.append(priority[count])
                # checkList.append(priority[count])
                # for checkList[count] in checkList :
                #     countinue
                # for check in checkList:
                
                # if checkList[count] in checkList and checkList[count] != '--Next Request--':
                #     continue 
                # else :
                # inList.append(checkList[count])
                # inList.append(priority[count]) 
                window['-OUTP-'].update(inList)
                count += 1
            checkList = []
         
        if button == '1' :
            t1 = time.time()
            dynamicList.append(['1 Internal',t1])
            inputList.append('1 Internal')        
        elif button == '2' :
            t1 = time.time()
            dynamicList.append(['2 Internal',t1])
            inputList.append('2 Internal')        
        elif button == '3' :
            t1 = time.time()
            dynamicList.append(['3 Internal',t1])
            inputList.append('3 Internal')        
        elif button == '4' :
            t1 = time.time()
            dynamicList.append(['4 Internal',t1])
            inputList.append('4 Internal')        
        elif button == '5' :
            t1 = time.time()
            dynamicList.append(['5 Internal',t1])
            inputList.append('5 Internal')        
        elif button == '6' :
            t1 = time.time()
            dynamicList.append(['6 Internal',t1])
            inputList.append('6 Internal')      
        elif button == '7' :
            t1 = time.time()
            dynamicList.append(['7 Internal',t1])    
            inputList.append('7 Internal')        
        elif button == '8' :
            t1 = time.time()
            dynamicList.append(['8 Internal',t1])
            inputList.append('8 Internal')        
        elif button == '9' :
            t1 = time.time()
            dynamicList.append(['9 Internal',t1])
            inputList.append('9 Internal')       
        elif button == '10' :
            t1 = time.time()
            dynamicList.append(['10 Internal',t1])
            inputList.append('10 Internal')        
        elif button == '11' :
            t1 = time.time()
            dynamicList.append(['11 Internal',t1])
            inputList.append('11 Internal')        
        elif button == '12' :
            t1 = time.time()
            dynamicList.append(['12 Internal',t1])
            inputList.append('12 Internal')       
        elif button == '13' :
            t1 = time.time()
            dynamicList.append(['13 Internal',t1])
            inputList.append('13 Internal')  
        elif button == '14' :
            t1 = time.time()
            dynamicList.append(['13 Internal',t1])
            inputList.append('13 Internal')
        elif button == '15' :
            t1 = time.time()
            dynamicList.append(['13 Internal',t1])
            inputList.append('13 Internal')    
        elif button == '1F':
            t1 = time.time()
            dynamicList.append(['1 External',t1])
            inputList.append('1 Externa;')  
        elif button == '2F':
            t1 = time.time()
            dynamicList.append(['2 External',t1])
            inputList.append('2 External')  
        elif button == '3F':
            t1 = time.time()
            dynamicList.append(['3 External',t1])
            inputList.append('3 External')    
        elif button == '4F':
            t1 = time.time()
            dynamicList.append(['4 External',t1])
            inputList.append('4 External')  
        elif button == '5F':
            t1 = time.time()
            dynamicList.append(['5 External',t1])
            inputList.append('5 External')  
        elif button == '6F':
            t1 = time.time()
            dynamicList.append(['6 External',t1])
            inputList.append('6 External')  
        elif button == '7F':
            t1 = time.time()
            dynamicList.append(['7 External',t1])
            inputList.append('7 External')  
        elif button == '8F':
            t1 = time.time()
            dynamicList.append(['8 External',t1])
            inputList.append('8 External') 
        elif button == '9F':
            t1 = time.time()
            dynamicList.append(['9 External',t1])
            inputList.append('9 External') 
        elif button == '10F' :
            t1 = time.time()
            dynamicList.append(['10 External',t1])
            inputList.append('10 External') 
        elif button == '11F' :
            t1 = time.time()
            dynamicList.append(['11 External',t1])
            inputList.append('11 External') 
        elif button == '12F' :
            t1 = time.time()
            dynamicList.append(['12 External',t1])
            inputList.append('12 External') 
        elif button == '13F' :
            t1 = time.time()
            dynamicList.append(['13 External',t1])
            inputList.append('13 External') 
        elif button == '14F' :
            t1 = time.time()
            dynamicList.append(['14 External',t1])
            inputList.append('14 External') 
        elif button == '15F' :
            t1 = time.time()
            dynamicList.append(['15 External',t1])
            inputList.append('15 External') 
        
        elif wait:
              time.sleep(5)


def dynamic(head):
    t1 = Thread(target=thread, args=())
    t1.start()

    # global wait
    direction_up = True
    # time.sleep(1)
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
            priority.append(head)
            time.sleep(1)
            # print("headr is :" , header)
            print("floor is now :\n", head)
            dynamicList.pop(0)
            if i == sizeQ - 1:
                priority.append('--Next Requests--')
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
        differenceFloor = abs(int(head) - int(sp[0]))
        differenceTime = now - i[1]
        d1 = differenceFloor / differenceTime
        if (head - int(sp[0]) > 0 and direction) or (int(head) - int(sp[0]) < 0 and not direction):
            d1 *= 0.65
        if sp[1] == 'Internal' :
            d1 *= (1/2)
        list1.append(d1)
        index.append(int(sp[0]))
        # print("list1 is :\n" , list1)
    for i in range(0, len(list1)):
        q.put((list1[i], index[i]))
        # priority.append(("floor :" , index[i]))
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
