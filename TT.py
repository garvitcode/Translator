
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from textblob import TextBlob


root = Tk()
 
root.title('TRANSLATOR')
root.geometry('600x300')
root.resizable(0,0)
 
root.config(bg='light green')
root.iconbitmap(r'C:\\Users\\hp\\OneDrive\\Pictures\\translator.ico')


#------------------------------------------------------------------------------------------------------------------------------------------


lan_dict = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'iw', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu', 'Filipino': 'fil', 'Hebrew': 'he'}


#------------------------------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------FUNCTIONS


def main(event=None):
    try:
        word3 = TextBlob(varname1.get())
        lan = word3.detect_language()
        lan_todict = languages.get()
        lan_to = lan_dict[lan_todict]
        word3 = word3.translate(from_lang=lan,to=lan_to)
        label3.configure(text=word3)
        varname2.set(word3)
    except:
        varname2.set('try another keyword')


def diff_lans():
    global languages
    languages = StringVar()
    font_box = ttk.Combobox(root,width=10,textvariable=languages,state='readonly')
    font_box['values'] = [e for e in lan_dict.keys()]
    font_box.current(37)
    font_box.place(x=0,y=0)


def about_us():
    messagebox.showinfo('TRANSLATOR','This is a translation tool viz. build using Python Tkinter.')


#---------------------------------------------------------------------------CREATING_MENU_BAR


menubar = Menu(root)
root.config(menu=menubar)


#----------------------------------------------------------------------------CREATING_SUBMENU


subMenu = Menu(menubar, tearoff = 0)

menubar.add_cascade(label="Choose Output Languages",menu=subMenu)
subMenu.add_command(label="AVAILABLE LANGUAGE", command=diff_lans)
subMenu.add_command(label="Exit", command=root.destroy)

subMenu = Menu(menubar,tearoff = 0)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About Us", command=about_us)


#-----------------------------------------------------------------------------ENTRY_BOX


varname1 = StringVar()
entry1 = Entry(root,width=30,textvariable=varname1,font=('times',20,'italic bold'))
entry1.place(x=150,y=40)

varname2 = StringVar()
entry2 = Entry(root,width=30,textvariable=varname2,font=('times',20,'italic bold'))
entry2.place(x=150,y=200)


#-----------------------------------------------------------------------------LABELS


label1 = Label(root,text='Latin Text  : ',font=('times',15,'italic bold'),bg='light green')
label1.place(x=5,y=40)

label2 = Label(root,text='Translated  : ',font=('times',15,'italic bold'),bg='light green')
label2.place(x=5,y=200)

label3 = Label(root,text='',font=('times',15,'italic bold'),bg='turquoise1')


#-----------------------------------------------------------------------------BUTTONS


btn = Button(root,text=' Translate ',bd=10,bg='yellow',activebackground= 'red',width='10',font=('times',15,'italic bold'),command=main)
btn.place(x=287,y=110)

root.bind('<Return>',main)


#-----------------------------------------------------------------------------BINDING_FUNCTION


def on_enterentry1(e):
    entry1['bg'] = 'powder blue'
def on_leaveentry1(e):
    entry1['bg'] = 'white'

def on_enterentry2(e):
    entry2['bg'] = 'powder blue'
def on_leaveentry2(e):
    entry2['bg'] = 'white'

def on_enterbtn(e):
    btn['bg'] = 'red'
def on_leavebtn(e):
    btn['bg'] = 'yellow'


#-----------------------------------------------------------------------------BINDING


entry1.bind('<Enter>',on_enterentry1)
entry1.bind('<Leave>',on_leaveentry1)

entry2.bind('<Enter>',on_enterentry2)
entry2.bind('<Leave>',on_leaveentry2)

btn.bind('<Enter>',on_enterbtn)
btn.bind('<Leave>',on_leavebtn)


#-----------------------------------------------------------------------------STATUS_BAR


statusbar = ttk.Label(root, text="Welcome to TRANSLATOR", relief=SUNKEN, anchor=W, font=('times',10))
statusbar.pack(side=BOTTOM, fill=X)

#----------------------------------------------------------------------------------------------------------------------------


root.mainloop()