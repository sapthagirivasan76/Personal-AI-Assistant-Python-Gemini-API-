import tkinter as tk
from tkinter import scrolledtext
from google import genai


#----------------------------------------------------api key 

api_key = "AIzaSyCiXLlGjyCoV1Vr44FmHRAPpUgSfi8Jb-E"

#----------------------------------------------------access gemini client

client= genai.Client(api_key=api_key)

#-----------------------------------------fn to send msg to gemini

def send_msg():
    user_msg = entry.get()
    if user_msg.strip()== "":
        return
    
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, "YOU : " + user_msg + "\n", "user")
    
    
#------------------------------------------------------------------gemini response

    response= client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_msg
    )
    
    
    chat_area.insert(tk.END, "Response from my side : " + response.text + "\n\n", "ai")
    
    entry.delete(0, tk.END)
    
    
    
#-------------------------------------------------------------------------fn to clear chat
def clear_chat():
    chat_area.config(state=tk.NORMAL)
    chat_area.delete(1.0,tk.END)
    chat_area.config(state=tk.DISABLED)
    
    
#----------------------------------------------------------------------- UI windwo



root=tk.Tk()
root.title("gemini powered SAP AI")
root.geometry("520x620")
root.config(bg="#4ea9bd")

#-------------------------------------------------------------------------------chat display

chat_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    font=("arial",12),
    bg="#e2e8ea",
    fg="white"
)

chat_area.pack(padx=10 , pady=10, fill=tk.BOTH, expand=True)
chat_area.config(state=tk.DISABLED)

chat_area.tag_config("user",foreground="#de301d")
chat_area.tag_config("ai" , foreground="#0b120c")

#--------------------------------------------------------------------------entry box

entry=tk.Entry(root,font=("Arial", 14), bg="#ecf0f1", fg="black")
entry.pack(padx=10, pady=8,fill=tk.X)

#-------------------------------------------------------------------------------button framee

btn_frame =tk.Frame(root, bg="#d6dbe0")
btn_frame.pack(pady=5)

#-----------------------------------------------------------------------------------send button
send_btn=tk.Button(
    btn_frame,
    text="Go",
    font=("arial" ,12,"bold"),
    bg="#27ae60",
    fg="white",
    width=12,
    command=send_msg

)
send_btn.pack(side=tk.LEFT, padx=5)

#-----------------------------------------------------------------------------------clear chat button
clear_btn=tk.Button(
    btn_frame,
    text="Clear Chat",
    font=("arial",12,"bold"),
    bg="#e74c3c",
    fg="white",
    width=12,
    command=clear_chat

    
)
clear_btn.pack(side=tk.LEFT,padx=5)

root.mainloop()