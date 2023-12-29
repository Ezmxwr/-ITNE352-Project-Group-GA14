import socket
from tkinter import *
from tkinter import ttk, simpledialog, messagebox
from threading import Thread
import json

<<<<<<< HEAD
socket_c = None 
response_data=""
def receive_data_from_server(option):
=======
def receive_data_from_server():
>>>>>>> c623c8078523dde56f5c9a5a7c6e8a7bcff665c4
    global response_data
    while True:
        try:
            Response= socket_c.recv(20400).decode("utf-8")
            
    
            # Update the text label with the server response
            response_text.config(state=NORMAL)
            response_text.delete('1.0', END)
            response_text.insert(END, Response )
            response_text.config(state=DISABLED)

        except Exception as e:
            print("Error receiving data from the server:", e)
            break 
#-------------------------------------------------------------------------------------------------------------
def show_options_after_username_entry():
    # This function is called when the user clicks one of the option buttons after entering the username
    username = username_entry.get()

    if username:
        # If the username is entered, show the options buttons and hide the username entry button
        options_frame.pack(side=TOP, pady=10)
        username_entry_button.pack_forget()

        # Send the username and option to the server
        socket_c.sendall(username.encode("utf-8"))
    else:
        # If the username is not entered, show a message asking the user to enter the username
        messagebox.showinfo("Username Required", "Please enter your username.")


def communicate_with_server(option , user_input= None):
    try:
        
        if option=="1" or option== "2":
            data_to_send = {"option": option, "user_input": user_input}
            socket_c.send(json.dumps(data_to_send).encode("utf-8"))
            
        if option=="5":
            confirmation = messagebox.askyesno("Goodbye server", "Are you sure you want to close the client? (yes/no)")
            if not confirmation:
                return 
            else:
                print("\nconnection with server closed.\n")
                root.destroy()
                
                

        if option == "3":
            # For option 3, tell the user to enter a depature ICAO code
            user_input = simpledialog.askstring( "Enter Departure IATA code","Please enter the departure IATA      :") 
            data_to_send = {"option": option, "user_input": user_input}
            socket_c.send(json.dumps(data_to_send).encode("utf-8"))

        elif option == "4":
            # For option 4,tell the user to enter a flight number
            user_input = simpledialog.askstring("Enter Flight IATA code ", "Please enter the flight IATA code:")
            data_to_send = {"option": option, "user_input": user_input}
            socket_c.send(json.dumps(data_to_send).encode("utf-8"))
      

        # Start a thread to continuously receive data from the server
<<<<<<< HEAD
        receive_thread = Thread(target=receive_data_from_server, args=(option,), daemon=True)
=======
        #look the why file
        receive_thread = Thread(target=receive_data_from_server, daemon=True)
>>>>>>> c623c8078523dde56f5c9a5a7c6e8a7bcff665c4
        receive_thread.start()          
        
       
    except Exception as e:
        print("Error communicating with the server:", e)

# controlling the frame size here
root = Tk()
root.title("Flight Information Client")
root.geometry("800x600")
root.minsize(600, 500)
# Create Label, Entry, and Button widgets for the username
username_label = Label(root, text="Enter Username:",font=("Helvetica", 10 , "bold"))
username_label.pack(side=TOP, pady=10)
username_entry = Entry(root, width=30)
username_entry.pack(side=TOP, pady=0)
# Button to submit the username and show options
username_entry_button = ttk.Button(root, text=" Enter ",width=10, command=lambda: show_options_after_username_entry())
username_entry_button.pack(side=TOP, pady=10)
# Create Button widgets for options and associate them with corresponding functions
options_frame = Frame(root)
option1 = ttk.Button(options_frame, text="Arrived flights", width=30, command=lambda: communicate_with_server("1",None))
option1.pack(side=TOP, pady=5)
option2 = ttk.Button(options_frame, text="Delayed flights", width=30, command=lambda: communicate_with_server("2",None))
option2.pack(side=TOP, pady=5)
option3 = ttk.Button(options_frame, text="All flights from a specific city", width=30, command=lambda: communicate_with_server("3"))
option3.pack(side=TOP, pady=5)
option4 = ttk.Button(options_frame, text="Details of a particular flight", width=30, command=lambda: communicate_with_server("4"))
option4.pack(side=TOP, pady=5)
option5 = ttk.Button(root, text="Quit", style="B5.TButton", command=lambda: communicate_with_server("5") )
option5.pack(side="top", anchor=NE, padx=(0, 100), pady=0)

# Create a Text widget with scroller to display server responses
response_frame = Frame(root)
response_frame.pack(side=TOP, pady=0)
#  Text widget with a scroller to display server responses
response_text = Text(options_frame, wrap=WORD, width=90, height=150)
response_text.pack(side=LEFT, pady=0)
scrollbar = Scrollbar(options_frame, command=response_text.yview)
scrollbar.pack(side=RIGHT, fill=Y)
response_text.config(yscrollcommand=scrollbar.set)
response_text.config(state=DISABLED)
style = ttk.Style()
style.theme_use("alt")
style.configure("TButton", background="lightgray", font=("Helvetica", 10))
style.configure("B5.TButton", foreground="white", background="red", font=("Helvetica", 10, "bold"))
root.update()
socket_c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# Connect to the server
socket_c.connect(("127.0.0.1", 49993))

root.mainloop() # Start the Tkinter event loop