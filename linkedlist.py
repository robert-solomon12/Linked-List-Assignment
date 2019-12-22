
#IMPORTING THE NODE CLASS INTO OUR MAIN CLASS###

from Node import Node
#Initializing Class Linked list  
class linkedl:

    def __init__(self):
        self.head = None

   

    #creating a new TRACK node
    #getting user input for that track node
    #initilazing new node data to get data from the user
    #the new tracks points to the last head
    #the new track will be the head now
    def addATRACK(self):
        new_node = Node()
        s = input("Whats the name of the TRACK you would like to enter :")
        new_node.data = str(s)
        new_node.next = self.head
        self.head = new_node



        ## HERE IS WHERE I'M INSERTING A TRACK TO THE MIDDLE WHEN FUNCTION IS CALLED ##

    def InsertInMiddle(self, middle_node, newdata):
        if middle_node is None:
            print("The mentioned node is not found")
            return

        NewNode = Node(newdata)         # create new node
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

    # function to print the Linked list
    #varaible TRACK initilized
    #printing out the data within the console
    def printlist(self):
        TRACK = self.head
        while(TRACK):
            print(TRACK.data)
            TRACK = TRACK.next


#here I'm adding a new TRACK at the end of the list
#creating of a new node
#get the user input
#check if the new TRACK is the start of the linked list
#if its not the first then go through the list until at the end
#set TRACK as the last node
#point to this new last TRACK
        
    
    def addTRACKAtToEndOfTheList(self):
        new_node = Node()
        s = input("Which Track you'd like to add at the end of your playlist? ")
        new_node.data = str(s)
        new_node.next = None
        if(self.head == None):
            self.head = new_node
        last = self.head 
        while(last.next != None):
            last = last.next
        last.next = new_node


    #TO enter a TRACK at a particular point within the linked list#
    #Create a new TRACK
    #add data from the user and assign that to the newly created node
    #going through the list past the point of the key which was given
    def addATRACKToAParticularPoint(self,key):
        new_node = Node()
        s = input("Enter TRACK details here")
        new_node.data = str(s)
        track = self.head
        while(track != None and track.data!=key):
            track = track.next
        new_node.next = track.next
        track.next = new_node




    #Here I'm writing a function to delete a TRACK from the playlist/
    #if the head is empty then the playlist is empty 
    def RemoveNode(self, key):
        HeadVal = self.head        
        if (HeadVal is not None):
            if (HeadVal.data == key):
                self.head = HeadVal.next
                HeadVal = None
                return

        while (HeadVal is not None):
            if HeadVal.data == key:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if (HeadVal == None):
            return

        prev.next = HeadVal.next
        HeadVal = None

    # Searching through the list for a specific track in the playlist
    def findATrack(self,key):
        track = self.head
        index = 0
        while(TRACK!=None and track.data!=key):
            index += 1
            track = track.next
        return index   

     


##If name is entered in the first prompt when program is run then initialize the user menu below        
if __name__ == "__main__":
    l1 = linkedl()
    option = 0
    while(option!=8):
        print("\n")
        print("| WELCOME TO YOUR MUSIC PLAYLIST, PLEASE CHOOSE FROM THE FOLLOWING OPTIONS:  |")
        print("|                   1 : ADD A TRACK/S TO YOUR PLAYLIST                       |")
        print("|                   2 : ADD A TRACK TO THE END OF YOUR PLAYLIST              |")
        print("|                   3 : ADD A TRACK AT A PARTICULAR POINT                    |")
        print("|                   4 : REMOVE A TRACK FROM YOUR PLAYLIST                    |")
        print("|                               5 : FIND A TRACK                             |")
        print("|                          6 : LIST ALL YOUR ADDED TRACKS                    |")
        print("|                            7 : ADD TRACK TO THE MIDDLE                     |")
        print("|                                  8 : EXIT MENU                             |")



        option = int(input("| \n PLEASE MAKE A SELECTION : |"))
        if(option == 1):
            print("\n") 
            b = input("| HOW MANY TRACKS WOULD YOU LIKE TO ADD? |")
            for i in range(int(b)):
                l1.addATRACK() 
        elif(option == 2):   
            print("\n") 
            b = input("| HOW MANY TRACKS WOULD YOU LIKE TO ENTER AT THE END? |")
            for i in range(int(b)):
                l1.addTRACKToTheEndOfTheList() 
        elif(option ==3):
             b = input("| ADD A TRACK AGTER OR BEFORE ANOTHER ONE? |")
             l1.addATRACKToAParticularPoint(int(b))  
    # I didn't get this part to work correctly with the function 'removeNode'
        elif(option == 4):
             b = input("| TRACK NUMBER TO REMOVE FROM PLAYLIST? |")  
             l1.RemoveNode(int(b))
        elif(option == 5):
             b = input("| TRACK YOU WOULD LIKE TO FIND? |")
             ind = l1.findATRACK(int(b))
             print("| The key is at index " + str(ind) + " |")
        elif(option == 6) :  
            print("| ALL THE TRACKS IN YOUR PLAYLIST |")
            l1.printlist()
    # I also didn't get this part to work correctly with the function 'insertToMode'
        elif(option == 7) :  
            print("| ADD A TRACK TO THE MIDDLE |")
            l1.InsertInMiddle()
            
        
