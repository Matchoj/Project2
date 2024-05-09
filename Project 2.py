import time
import datetime
import os
# DATA

re1=0
re2=0
# STAGE 1 program makes Directory and files witch are necessery for it's fuctionation
dir_path=r'c:\Projects\Timecounter'
path=r'c:\Projects\Timecounter\path_doc.txt'
os.path.isdir(dir_path) or os.makedirs(r"c:\Projects\Timecounter")
if os.path.isfile(path):
    pass
else:
    file=open(path, "w")
    file.write(r"c:\Projects\Timecounter")
    file.close()


#STAGE 2  display main manu with available fintions
def mainmanu(*args):
    values=[]
    for i in menulist:
        print("{} -- {}".format(menulist.index(i) + 1, i.__name__))


#STAGE 3  this function cheack if user choose available option and returns to it
def answer(arg,arg1):
    while True:
        try:
            chooseint=int(arg)
            break
        except:
            choose=input("You need to insert number from the Mainlist: ")
    while True:
        if chooseint >0 and chooseint <= len(arg1):
            break
        else:
            print("\n\nNumber you have choose dose not exist, try again")
            break
    return chooseint


# Stage 4 This function save starting time and retuns it aslo it create file with name of the month
def Start_learning():
    start=time.time()
    basename="{}.txt".format(datetime.date.today().strftime("%Y-%m"))
    f=open(path,"r")
    text=f.read()
    file=os.path.join(text,basename)
    f.close()
    if os.path.isfile(file):
        pass
    else:
        with open(file,'w') as f:
            f.write("{}".center(100).format(datetime.date.today().strftime("%B")))
            f.write("\n\n")
    menulist[0]=Stop_learning
    return start, file


def Stop_learning(arg1=re1,arg2=re2):
        stop=time.time()
        with open(re2,"a") as f:
            f.write("On {} th you have learn :{} minutes\n".format(datetime.date.today().strftime("%A - %d"),round((stop-re1)/60,2)))
        menulist[0]=Start_learning
        return stop,re2

def Change_Directory():
    NewPath=input("Please inseret path where you what to  storage files: ")
    try:
        comunicate="The path was Changed on :"
        os.makedirs(NewPath)
        file=open(path,'w')
        file.write(NewPath)
        file.close()
        menulist[0] = Start_learning
        return 1,2
    except:
        print("this path is impossible to create! see  exemple below and try again")
        print(r"c:\exemple")
        Change_Directory()
        return 1,2


def Show_File():
    with open(path) as f:
        text=f.read()
        files=dict(enumerate(os.listdir(text)))
        for f in files:
            print("{} - {}".format(f+1,files[f]))
        choose=input("Insert numnber of file you want to see : ")
        x=answer(choose,files)
        y=files[x-1]
        file=os.path.join(dir_path,y)
        with open(file,"r") as f:
            print(f.read())
    return 1,2

def Exit():
    Quit= False
    return Quit,1



menulist=[Start_learning,Change_Directory,Show_File,Exit]

Quit=True

while Quit:
    os.system('cls')
    mainmanu(menulist)
    choose= input("Choose option from 1 to {} : ".format(len(menulist)))
    x=answer(choose, menulist)
    y=menulist[x-1]
    re1,re2=y()
    Quit=re1