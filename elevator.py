# Python3 implementation of the approach
import math
disk_size = 200

# Function to perform C-LOOK on the request
# array starting from the given head
def CLOOK(arr, head):
    size = 5
    seek_count = 0
    distance = 0
    cur_track = 0
    array = arr
    down = []
    up = []
    sub_array = []
    seek_sequence = []
    directionUp = True 
    
	# Tracks on the down of the
	# head will be serviced when
	# once the head comes back
	# to the beginning (down end)
    for k in range(0 , math.ceil(len(arr) / size)) :
        for i in range(0 , size - 1):
            # if array[i] != None :
                item = array.pop(0)
                # sub_array.append(item)
                if (item < head):
                    down.append(item)
                if (item > head):
                    up.append(item)

        sub_array = up + down
        sub_array.sort()
        print("array :" , sub_array)
        # Sorting down and up vectors
        down.sort()
        up.sort()
        
        print("up:" , up)
        print("down" , down)

        # First service the requests
        # on the up side of the
        # head
        
       
        if (k == 0 and len(up) >= len(down)) or (sub_array[0] > head):
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

            # Once reached the up end
            # jump to the last track that
            # is needed to be serviced in
            # down direction
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
                    
        # if head < sub_array[3] :
        #     sub_array.reverse()
        #     for i in range(len(up)):
        #         directionUp = True
        #         up.reverse()
        #         cur_track = up[i]
                
        #         # Appending current track
        #         # seek sequence
        #         seek_sequence.append(cur_track)

        #         # Calculate absolute distance
        #         distance = abs(cur_track - head)

        #         # Increase the total count
        #         seek_count += distance

        #         # Accessed track is now new head
        #         head = cur_track

        #     # Once reached the up end
        #     # jump to the last track that
        #     # is needed to be serviced in
        #     # down direction
        #     if len(down) != 0 :
        #         seek_count += abs(head - down[0])
        #         head = down[0]
        #     # Now service the requests again
        #     # which are down
        #         for i in range(len(down)):
        #             directionUp = False
        #             down.reverse()
        #             cur_track = down[i]

        #             # Appending current track to
        #             # seek sequence
        #             seek_sequence.append(cur_track)

        #             # Calculate absolute distance
        #             distance = abs(cur_track - head)

        #             # Increase the total count
        #             seek_count += distance

        #             # Accessed track is now the new head
        #             head = cur_track
            
                
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
        
        elif directionUp == True and sub_array[3] > head :
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

            # Once reached the up end
            # jump to the last track that
            # is needed to be serviced in
            # down direction
            if len(down) != 0 :
                seek_count += abs(head - down[0])
                head = down[0]
            # Now service the requests again
            # which are down
                down.reverse()
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
            
            # Once reached the up end
            # jump to the last track that
            # is needed to be serviced in
            # down direction
                # seek_count += abs(head - down[0])
                # head = down[0]
            
           
        # print("Total number of seek operations =",  seek_count)
        # print("Seek Sequence is")

        for i in range(len(seek_sequence)):
            print(seek_sequence[i])
        
        
        up.clear()
        down.clear()
        sub_array.clear()
        seek_sequence.clear()


# Request array
arr = [ 176, 79, 34, 60, 92, 12, 41, 114 , 120 , 31 , 80 , 121]
arr2 = [2 , 4 , 5 , 1, 0 , 2 , 6 ,1 , 9 , 2 , 3 ,1]
head = 3

print("Initial position of head:", head)

CLOOK(arr2, head)

# This code is contributed by rag2127
