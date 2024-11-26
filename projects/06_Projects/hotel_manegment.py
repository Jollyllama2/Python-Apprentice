from tkinter import messagebox, simpledialog, Tk  
import random


"Make a dictonary  """""  

" make list """"make Tupil"

"make Boolean """

rooms = [1,2,3,4,5,6,7]

hotel = { }

for room in rooms:
     hotel[room] = ''

def check_in():
     for room, n in hotel.items() :
          if not n:
               name =  simpledialog.askstring(title= 'hi', prompt = ' whats your name')
               hotel[room] = name  
               break 

def check_out(name):
     for room, n in hotel.items() :
          if name == n:
               hotel[room] = ''

if __name__ == '__main__':
     simpledialog.askstring(title= 'hello', prompt = ' Do you want to check in or ceheck out  ')
     if all(not names for names in hotel.values()):
          check_in()
     else:
          messagebox.showinfo(title= '', message =  ' there are no availble rooms')

             

          




                     
    
                     
        

  
       
    
        


        


