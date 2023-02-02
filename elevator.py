# Python3 implementation of the approach
import math
from threading import Thread
from queue import PriorityQueue
import time
disk_size = 200

# Function to perform C-LOOK on the request
# array starting from the given head
def CLOOK(arr, head):
    size = 4
    seek_count = 0
    distance = 0
    cur_track = 0
    array = arr
    down = []
    up = []
    sub_array = []
    seek_sequence = []
    directionUp = True 
    
    lenCheck = math.ceil(len(arr) / size)
    if  lenCheck < 1:
        lencheck = 1
    
    if len(arr) < size :
        size = len(array)
    for k in range(0 , lenCheck) :
        for i in range(0 , size):
            if len(array) == 0:
                break
            item = array.pop(0)
                # sub_array.append(item)
            if (item < head):
                down.append(item)
            if (item > head):
                up.append(item)

        sub_array = up + down
        sub_array.sort()
        print("array :" , sub_array)
        down.sort()
        up.sort()
        
        print("up:" , up)
        print("down" , down)

       
        if (k == 0 and len(up) >= len(down)) or (sub_array[0] > head) or (directionUp == True and sub_array[3] > head):
            for i in range(len(up)):
                directionUp = True
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

            if len(down) != 0 :
                seek_count += abs(head - down[0])
                down.reverse()
                head = down[0]
            # Now service the requests again
            # which are down
                for i in range(len(down)):
                    directionUp = False
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
                    
        elif sub_array[0] < head and directionUp == False :
            # Now service the requests again
            # which are down
            for i in range(0 , len(down)):
                directionUp = False
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
                directionUp = True
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
        while count != numReq :
            inputStatic = int(input('Enter the requests :'))
            staticList.append(inputStatic)
            count += 1
        print(staticList)
        CLOOK(staticList , int(head))
        
dynamicList = []
wait = False

def thread():
    while True :
        in1 = input("enter request\n")
        t1 = time.time()
        dynamicList.append([in1 , t1])
        if wait :
            time.sleep(5)
         
def dynamic(head):
    t1 = Thread(target=thread, args=())
    t1.start()
    
    # global wait
    directionUp = True
    time.sleep(1)
    if len(dynamicList) != 0:
        fiestReq = dynamicList[0]
        diff =  int(head) - int(fiestReq[0])
        if diff < 0 :
            dirctionUp = False
            
    while True :    
        time.sleep(3)
        wait = True
        q1 = update(dynamicList, head, directionUp)
        sizeQ = q1.qsize()
        for i in range(0 , sizeQ):
            head = q1.get()[1]
            time.sleep(1)
            print("floor is now :\n" , head)
            dynamicList.pop(0)
        # dynamicList.clear()
        if q1.empty() :
            wait = False
        
           
def update(dynamic, head, direction):
    list1 = []
    index = []
    q = PriorityQueue()
    now  = time.time()
    for i in dynamic:
        # print("i is :\n", i )
        difference = abs(head - int(i[0]))
        diff = now - i[1]
        d1 = difference / diff
        if (head - int(i[0]) > 0 and direction) or (head - int(i[0]) < 0 and not direction):
            d1 *= 0.7
        list1.append(d1)
        index.append(int(i[0]))
        # print("list1 is :\n" , list1)
    for i in range(0,len(list1)):
        q.put((list1[i], index[i]))    
        # print("printed :" , (list1[i], index[i]))
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
        headDynamic = input("enter the current floor of elevator\n")
        dynamic(headDynamic)

