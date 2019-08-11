from tkinter import *
import easygui
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import requests
from pystray import MenuItem as item
import pystray

from PIL import Image
def action():
    conversation=[
        "hello",
        "Hi there!",
        "How are you doing",
        "I am doing great",
        "That is good to hear",
        "Thank you"
        ]
    chatbot=ChatBot("Bisp")

    trainer = ChatterBotCorpusTrainer(chatbot)

    trainer.train(
        "chatterbot.corpus.english.greetings",
        "chatterbot.corpus.english.conversations"
    )
    apiemp='http://127.0.0.1:5000'
    jsonemp=requests.get(apiemp).json()
    api_address='https://api.openweathermap.org/data/2.5/weather?appid=6e47f682a6c6a11adaf2df87a1812a96&q=Jamshedpur'
    json_data=requests.get(api_address).json()
    f=json_data['main']['temp']

    t=(f-272.15)
    f1=json_data['weather'][0]['main']
    f2=json_data['weather'][0]['description']
    x=[]
    column=["Id","First Name","Middle Name","Last Name","Address","Email","Mobile Number","Vehicle","Vehicle Number"]

    colum=["id","fn","mn","ln","address","Email","Mobile","Vehicle","Vehicle_Number"]

    window = Tk()
    window.title("Amps")
    window.configure(background='black')
    
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window.geometry("500x500+{0}+{1}".format(screen_width-500, screen_height-570))
    


    messages = Text(window,background='lightgreen')
    messages.pack()
    messages.tag_config('amps',foreground="blue")
    messages.tag_config('you',foreground="red")
    input_user = StringVar()
    input_field = Entry(window, text=input_user,font=(None,20),background='lightblue')
    input_field.insert(0,'Type something here')
    input_field.pack(side=BOTTOM, fill=X)
    label=Label(window,text="Amps : Type information if you want to rummage through the database",height="20",background='lightyellow')
    label.pack()
    def Enter_pressed(event):
        userInput = input_field.get()
        messages.insert(INSERT, 'You:%s\n' % userInput,'you')
        input_user.set('')
        

        messages.see(END)
        if userInput.strip()=='bye' or userInput.strip()=='goodbye':
            messages.insert(INSERT, 'Amps:Bye\n','amps')
            messages.see(END)
            exit
        elif('weather' in userInput.strip()):
            messages.insert(INSERT, "The weather is "+f1+" and described as "+f2+"\n",'amps')
            messages.see(END)
        elif('temperature' in userInput.strip()):
            messages.insert(INSERT, "The temperature is "+str(t)+"\n",'amps')
            messages.see(END)
        elif('information' in userInput.strip()):
            messages.insert(INSERT, "Give me something to work with:\n",'amps')
            messages.insert(INSERT, "1 for Full Name\n2 for ID\n3 for Email\n4 for Mobile Number\n5 for Vehicle\n6 for Vehicle Number\n",'amps')
            messages.see(END)
            ch=int(easygui.enterbox("Your Choice?"))
            c=[]
            if(ch==1):
                messages.insert(INSERT, "Enter the full name:\n",'amps')
                messages.see(END)
                
                names=easygui.enterbox("Enter full name").split()
                
                
                for i in range(len(jsonemp["myCollection"])):
                    if(jsonemp["myCollection"][i]["fn"]==names[0] and jsonemp["myCollection"][i]["mn"]==names[1] and jsonemp["myCollection"][i]["ln"]==names[2]):
                        
                        z={}
                        for j in range(len(column)):
                            z[colum[j].lower()]=jsonemp["myCollection"][i][colum[j].lower()]
                        c.append(z)
            elif(ch==2):
                messages.insert(INSERT,"Enter id:\n",'amps')
                messages.see(END)
                
                name=int(easygui.enterbox("Enter ID"))
                for i in range(len(jsonemp["myCollection"])):
                    if(jsonemp["myCollection"][i]["id"]==name):
                        
                        z={}
                        for j in range(len(column)):
                            z[colum[j].lower()]=jsonemp["myCollection"][i][colum[j].lower()]
                        c.append(z)
            elif(ch==3):
                messages.insert(INSERT,"Enter Email:\n",'amps')
                messages.see(END)
                
                name=easygui.enterbox("Enter Email")
                for i in range(len(jsonemp["myCollection"])):
                    if(jsonemp["myCollection"][i]["email"]==name):
                        
                        z={}
                        for j in range(len(column)):
                            z[colum[j].lower()]=jsonemp["myCollection"][i][colum[j].lower()]
                        c.append(z)
            elif(ch==4):
                messages.insert(INSERT,"Enter Mobile Number:\n",'amps')
                messages.see(END)
                
                name=easygui.enterbox("Enter Mobile Number")
                for i in range(len(jsonemp["myCollection"])):
                    if(jsonemp["myCollection"][i]["mobile"]==name):
                        
                        z={}
                        for j in range(len(column)):
                            z[colum[j].lower()]=jsonemp["myCollection"][i][colum[j].lower()]
                        c.append(z)
            elif(ch==5):
                messages.insert(INSERT,"Enter Vehicle:\n",'amps')
                messages.see(END)
                
                name=easygui.enterbox("Enter Vehicle Name")
                for i in range(len(jsonemp["myCollection"])):
                    if(jsonemp["myCollection"][i]["vehicle"]==name):
                        
                        z={}
                        for j in range(len(column)):
                            z[colum[j].lower()]=jsonemp["myCollection"][i][colum[j].lower()]
                        c.append(z)
            elif(ch==6):
                messages.insert(INSERT,"Enter Vehicle Number:\n",'amps')
                messages.see(END)
                
                name=easygui.enterbox("Enter Vehicle Number")
                for i in range(len(jsonemp["myCollection"])):
                    if(jsonemp["myCollection"][i]["vehicle_number"]==name):
                        
                        z={}
                        for j in range(len(column)):
                            z[colum[j].lower()]=jsonemp["myCollection"][i][colum[j].lower()]
                        c.append(z)
            messages.insert(INSERT,"These are the results I found.\n",'amps')
            messages.see(END)
            
            for i in range(len(c)):
                messages.insert(INSERT,"%s" % c[i]["id"]+" "+c[i]["fn"]+" "+c[i]["ln"]+"\n")
                messages.see(END)
            messages.insert(INSERT,"Enter the id of the person : \n",'amps')
            messages.see(END)
            id=int(easygui.enterbox("Enter ID of the person you want details on"))
            for i in range(len(c)):
                if(c[i]["id"]==id):
                    for j in range(len(column)):
                        messages.insert(INSERT,"%s" % column[j]+" : "+str(c[i][colum[j].lower()])+"\n")
                        messages.see(END)
            messages.see(END)
        else:
            response=chatbot.get_response(userInput)
            messages.configure(foreground='red')
            messages.insert(INSERT,'Amps: %s\n' % response,'amps')
            messages.see(END)

        return "break"

    frame = Frame(window,background="black")  # , width=300, height=300)
    input_field.bind("<Return>", Enter_pressed)
    frame.pack()

    window.mainloop()

image = Image.open("chat.jpg")
menu = (item('Chat', lambda:action()),)
icon = pystray.Icon("Chat", image, "AMPS", menu)
icon.run()
