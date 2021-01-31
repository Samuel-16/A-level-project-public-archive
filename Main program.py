file="KEEP THIS FILE IN THE SAME DIRECTORY AS THE PROGRAM..SVBudA"
import tkinter as GUI
import tkinter.messagebox
from os.path import dirname as Wdir
from os.path import realpath as F
from os.path import isfile as Exists
from math import log2
from SamuelsPickle import Get
from SamuelsPickle import byteSplit
from SamuelsPickle import byte
from SamuelsPickle import ID as getNumber
from datetime import date
NavArray=[]
Win=GUI.Tk()
Win.title("Spending tracker.")
Win.config(height=768,width=1024,bg="#FFFF00")
Presets=lambda:Item(Item(Item(Name="Gas.",Preset=True),Item(Name="Electricity.",Preset=True),Item(Name="Water.",Preset=True),Name="Bills.",Preset=True,Included=False),Item(Item(Item(Item(Name="Bread.",Preset=True),Item(Name="Vegetables.",Preset=True),Item(Name="Drinks.",Preset=True),Item(Name="Sweets.",Preset=True),Item(Name="Condiments.",Preset=True),Preset=True,Name="Groceries."),Item(Name="Clothes.",Preset=True),Item(Name="Games.",Preset=True),Item(Name="Furniture.",Preset=True),Name="Shopping.",Preset=True),Item(Item(Name="Golf.",Preset=True),Name="Leisure.",Preset=True),Item(Name="Eating out.",Preset=True),Name="Trip out.",Preset=True,Included=False),Item(Name="Tax.",Preset=True,Included=False),Preset=True,Included=True)
class Item():
    def __init__(self,*Cats,Preset=False,Name="",TypCost=0,Included=True):
        self._Cats=list(Cats)
        self.__Name=Name
        self._Preset=bool(Preset)
        if len(self._Cats)!=0:
            self._Multiple=True
            self.__Boxes=[]
            self._BoxVars=[]
            self._Lables=[]
            self._Buttons=[]
            for i in range(len(Cats)):
                if Cats[i]._Preset:self._BoxVars+=[GUI.BooleanVar()]
                self.__Boxes.append(GUI.Checkbutton(Win,bg="#FFFF00",variable=self._BoxVars[i])if self._Preset else GUI.Button(Win,text="-"))
                self._Lables.append((GUI.Label if self._Preset else GUI.Entry)(Win,text=str(Cats[i])if str(Cats[i])!="Energy."else"Electricity",bg="#FFFF40"))
                self._Buttons.append(GUI.Button(Win,text=("Edit"if Cats[i]._Multiple else"Add")+" contents.",command=lambda I=Cats[i]:SetupE(self,I)))
            self.__Boxes.append(GUI.Button(Win,text="+",command=self.append))
        else:self._Multiple=False
        self._TypCost=TypCost
        if self._Preset:self._Included=bool(Included)
        else:self._Included=True
    def append(Self):
        Self._Cats.append(Item(Name=""))
        Self.__Boxes.append(GUI.Button(Win,text="+",command=Self.append))
        Self._Lables.append(GUI.Entry(Win,bg="#FFFF40"))
        Self._Buttons.append(GUI.Button(Win,text="Add contents.",command=lambda:SetupE(Self,Self._Cats[len(Self._Cats)-1])))
        Self.__Boxes[len(Self.__Boxes)-2].config(text="-",command=lambda i=Self._Lables[-1]:i.delete(0,"end"))
        Self.gridPlace(32,64,32,32)
    def __iadd__(self,other):
        if isinstance(other,str):other=Item(Name=other)
        if isinstance(other,Item):
            if other._Multiple:raise ValueError("Can only append single items.")
            else:
                if self._Multiple:
                    if not self._Multiple:self.Deepen(str(self))
                    self.__Boxes+=[GUI.Button(Win,text="-")]
                    self._Lables+=[GUI.Entry(Win,text=str(other),bg="#FFFF00")]
                    self._Buttons+=[GUI.Button(Win,text="Add contents.")]
                    self._Cats+=[other]
        return self
    def __str__(self):return self.__Name
    def __del__(Self):Self.Shallow()
    def Deepen(Self,Name=""):
        "Make an item into a catagory."
        if Self._Multiple:raise ValueError("Cannot deepen an item that is already a catagory.")
        Self._Multiple=True
        Self._Cats=[Item(Name=Name)]
        Self.__Boxes=[GUI.Button(Win,text="-"),GUI.Button(Win,text="+",command=Self.append)]
        Self._Lables=[GUI.Entry(Win,text=str(Self._Cats[0]),bg="#FFFF00")]
        Self._Buttons=[GUI.Button(Win,text="Add contents.",command=lambda I=Self._Cats[0]:SetupE(Self,I))]
    def Shallow(Self):
        if not Self._Multiple:raise ValueError("Cannot shallow an item that is'nt a catagory.")
        Self._Multiple=False
        for i in Self.__Boxes:i.destroy()
        for i in Self.__Boxes:
            try:i.destroy()
            except AttributeError:pass
        for i in Self.__Boxes:
            try:i.destroy()
            except AttributeError:pass
        Self._Cats.clear()
        del Self.__Boxes
        del Self._BoxVars
        del Self._Lables
        del Self._Buttons
    def gridPlace(S,x,y,xm,ym):
        if not S._Multiple:S.Deepen("")
        for i in range(len(S.__Boxes)):
            S.__Boxes[i].place(x=x,y=y+i*ym)
            if i<len(S.__Boxes)-1:
                if S._Cats[i]._Included:
                    if isinstance(S.__Boxes[i],GUI.Checkbutton):S.__Boxes[i].select()
                    if S._Cats[i]._Multiple:S._Buttons[i].config(text="Edit contents.")
        for i in range(len(S._Lables)):S._Lables[i].place(x=x+24,y=y+i*ym)
        for i in range(len(S._Buttons)):S._Buttons[i].place(x=x+128,y=y+i*ym)
    def presetUpdate(S):
        for i in range(len(S._Cats)):
            if isinstance(S.__Boxes[i],GUI.Checkbutton):S._Cats[i]._Included=S._BoxVars[i].get()
            if isinstance(S._Lables[i],GUI.Entry):
                if not True in (i>255 for i in(ord(j)for j in Name)):S._Cats[i].__Name=S._Lables[i].get()
                if S._Lables[i].get()==""or True in (i>255 for i in(ord(j)for j in Name)):
                    if S._Cats[i]._Multiple:S._Cats[i].Shallow()
                    del S._Cats[i]
                    S.__Boxes[i].destroy()
                    del S.__Boxes[i]
                    S._Lables[i].destroy()
                    del S._Lables[i]
                    S._Buttons[i].destroy()
                    del S._Buttons[i]
    def setIncluded(S,N=True):S._Included=bool(N)if isinstance(N,bool)or(isinstance(N,int)and(N==1 or N==0))or N==None else True
    def Exists(Self,other):
        try:return Self._Lables[Self._Cats.index(other)].get()!=""
        except (ValueError,AttributeError):return isinstance(Self._Lables[Self._Cats.index(other)],GUI.Label)
class ReadItem():
    _TypCost=0 # This is a default value. These don't have to be defind in __init__.
    def __init__(self,Set):
        if "IDidntWantToUseThisGlobal"in globals():
            if isinstance(Set,Item):
                self.__Multiple=Set._Multiple
                self.__Name=str(Set)
                if len(self.__Name)>235:self.__Name=self.__Name[:235]
                self.__Preset=Set._Preset
                self._TypCost=Set._TypCost
                self.__Cats=[]
                if Set._Multiple:
                    for i in Set._Cats:
                        if i._Included:self.__Cats+=[type(self)(i)]
            elif isinstance(Set,tuple):
                if 3!=len(Set):raise IndexError("A set given as a tuple should have exactly 3 values. "+str(len(Set))+" given.")
                self.__Name=str(Set[0])
                self.__Preset=bool(Set[1])
                if isinstance(Set[2],int):
                    self.__Multiple=False
                    self._TypCost=Set[2]
                elif isinstance(Set,__ReadItem):
                    self.__Multiple=True
                    self.__Cats=Set[2]
                else:raise TypeError(str(Set[2])+" is not an int, or ReadItem.")
            elif not isinstance(Set,type(None)):raise TypeError(str(Set)+" is not an item, or tuple.")
        else:
            ID=byte((True,))
            if isinstance(Set,Item):
                global IDidntWantToUseThisGlobal
                globals()["IDidntWantToUseThisGlobal"]=None
                self.__Multiple=Set._Multiple
                self.__Name=str(Set)
                if len(self.__Name)>235:self.__Name=self.__Name[:235]
                self.__Preset=Set._Preset
                self._TypCost=Set._TypCost
                self.__Cats=[]
                if Set._Multiple:
                    for i in Set._Cats:
                        if i._Included:self.__Cats+=[ReadItem(i)]
                self.getID(ID)
                self.__SetupWrite()
            elif isinstance(Set,str): # This is where the file is read from.
                File=Get(file,2)
                if File.Read(1,1,1)!=b"S\x08\x00":raise FileNotFoundError("File \""+file+"\" has been flagged as corrupt, due to an incorrect check-prefix.")
                global Name
                Name=""
                for i in range(File.Read()):Name+=chr(File.Read())
                global payDay
                payDay=File.Read()
                global Pay
                Pay=File.Read()*65536+File.Read()*256+File.Read()
                global IDidntWantToUseThisGlobal
                IDidntWantToUseThisGlobal=None
                self.__ExtATR(File)
                self.getID(ID)
                File=File.Transfer()
                self.__BKmark=File.seek(0,1)
                global Cash
                global increment
                global FiInc
                increment=0
                FiInc=0
                try:Cash,Lday,Lmonth=self.Scan(File,False)
                except ValueError as Error:raise FileNotFoundError("File \""+file+"\" has been flagged as corrupt, due to the following error:\n"+str(Error)+"\nIncrement="+str(increment)+".\nFiInc="+str(FiInc))
                present=date.today()
                File.close()
                File=open(file,"ab")
                while ((Lday<payDay and present.day>=payDay)or(Lmonth<present.month and present.day>=payDay)or Lmonth<present.month-1 or Lmonth>present.month or Lday>present.day)and payDay>0:
                    if Lday<payDay and present.day>=payDay:
                        print("1:","Lday=payDay",Lday,"=",payDay)
                        Lday=payDay
                    elif (Lmonth<present.month and present.day>=payDay)or Lmonth<present.month+1:
                        print("2:","Lmonth,Lday=Lmonth+1,payDay",Lmonth,",",Lday,"=",Lmonth+1,",",payDay)
                        Lmonth,Lday=Lmonth+1,payDay
                    elif Lmonth==12:
                        print("3:")
                        Lmonth,Lday=1,payDay
                    else:
                        print("4:","Lmonth,Lday=Lmonth+1,payDay",Lmonth,",",Lday,"=",Lmonth+1,",",payDay)
                        Lmonth,Lday=Lmonth+1,payDay
                    Cash+=Pay
                    Initial=bytes((96+Lmonth*2+Lday//32,Lday%32*8+2,192+(int(log2(Pay))//8+1 if Pay<=9223372036854775807 else 63)))+"Monthly income.".encode("utf8")#"0-1-1-? ???-? ???? ?-??? ??-?? ????". (Spending or reminder,type,add or sdubtract,Month,Day,Text length,Number length)
                    Nbytes=b""
                    Amount=Pay
                    Nbytes=bytes((Amount%256,))+Nbytes
                    Initial+=Nbytes
                    File.write(Initial)
                File.close()
#    def __getitem__(Self,index):return Self._Cats[index]
    def getID(self,ID=None):
        if not'_ReadItem__ID'in self.__dict__:
            if not isinstance(ID,bytes):
                raise TypeError(str(self)+" does not yet have an ID. Expecting \"bytes\" not "+str(type(ID)))
            self.__ID=ID
            if self.__Multiple:
                for i in range(len(self.__Cats)):
                    oldid=byteSplit(self.__ID)
                    while not oldid[-1]:oldid=oldid[:-1]
                    self.__Cats[i].getID(byte(oldid+(False,)*(i+1)+(True,)))
        return self.__ID
    def Retu(Self):return Self.__Name,Self.__Multiple,Self.__Preset,Self._TypCost,Self.__ID,(Self.__Cats if "_ReadItem__Cats"in Self.__dict__ else ((),))
    def Scan(self,File,Detail=True,Tag=None):
        File.seek(self.__BKmark)
        Cash=0
        Repeat=True
        if Detail:
            List=[]
            Zoom=["Data for "+(getNumber(Tag)if Tag!=None else"most recent spending")+" not found."]
            Spendings=0
        global FiInc#REMOVE
        while Repeat:
            Initial=File.read(3)
            try:Addition,Type,Sign,Month,UseLessVar,Day,Ccount,Ncount=byteSplit(Initial,True,True,True,False,False,False,False,True,False,False,False,False,False,None,False,False,False,False,None,False,False,False,False,False)
            except ValueError:Repeat=False
#            if Repeat:print("\nAddition="+str(Addition),"Type="+str(Type),"Sign="+str(Sign),"Month="+str(Month),"Day="+str(Day),"Ccount="+str(Ccount),"Ncount="+str(Ncount),sep="\n",end="\n\n")
            if Addition and Repeat:#REMINDER.
                if Type:
                    pass
                else:
                    pass
            elif Repeat:
                if Type:#MANUAL ADJUSTMENT.
                    Cstr=File.read(Ccount+4).decode("utf8")
                    Nint=byteSplit(File.read(Ncount),None)
                    if Detail:
                        if isinstance(Cash,int):List.append(str(Day)+" "+("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")[Month-1]+": "+Cstr+" £"+str(Cash)+" "+("+"if Sign else"-")+" £"+str(Nint)+" = £"+str(Cash+Nint*(1 if Sign else -1)))
                        else:List.append(str(Day)+" "+("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")[Month-1]+": "+Cstr+" £"+str(Cash)+" "+("+"if Sign else"-")+" £"+str(Nint)+" = £"+str(Cash+Nint*(1 if Sign else -1))+("0"if str(Cash+Nint*(1 if Sign else -1))[-2]=="."else""))
                    Cash+=Nint*(1 if Sign else -1)
                else:
                    if Detail:Spendings+=1
                    ID=File.read(Ncount)
                    CatScan=[0]
                    ID=byteSplit(ID)
                    Flawless=True
                    Main=self
                    Indset=[]
                    while Main.getID()!=byte(ID):
                        Main=self
                        try:
                            for i in Indset:Main=Main.__Cats[i]
                        except IndexError:
                            del Indset[-1]
                            Indset[-1]+=1
                            Flawless=False
                        if Main.__Multiple and Flawless:
                            Indset.append(0)
                        elif Flawless:Indset[-1]+=1
                        Flawless=True
                    Indset.clear()
                    Indset.append(0)
                    if Detail:
                        if Tag in (Spendings,None):
                            Zoom.clear()
                            Zoom.append("Data for "+(getNumber(Tag)if Tag!=None else"most recent spending")+" on "+str(Day)+"/"+str(Month)+":")
                    Second=Main
                    preCash=Cash
                    try:N,Cash=Second.Stepin(Cash,File,Detail,Tag,Zoom,Spendings)
                    except UnboundLocalError as e:
                        if not Detail:N,Cash=Second.Stepin(Cash,File,Detail,Tag)
                        else:raise Exception(str(e)+" Detail was true.")
                    if int(Cash*100)/100!=Cash:Cash=int(Cash*100+0.5)/100
                    if Detail:
                        if isinstance(Cash,int):List.append("Spending on "+str(Main)+": ID=\""+getNumber(Spendings)+"\" "+str(Day)+" "+("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")[Month-1]+": £"+str(preCash)+" - £"+str(preCash-Cash)+" =\t£"+str(Cash))
                        else:List.append("Spending on "+str(Main)+": ID=\""+getNumber(Spendings)+"\" "+str(Day)+" "+("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")[Month-1]+": £"+str(preCash)+" - £"+str(int((preCash-Cash)*100+0.5)/100)+" =\t£"+str(Cash)+("0"if str(Cash)[-2]=="."else""))
        if not isinstance(Cash,int):Cash=int(Cash*100+0.5)/100
        if Detail:return Cash,List,Zoom
        else:
            if Cash<0:GUI.messagebox.showwarning("Overdrawn.","You currently have a negative amount of cash!")
            return Cash,Day,Month
    def Stepin(Self,Cost,File,Detail,Tag,Zoom=None,Spendings=None):
        R=(str(Self),byteSplit(File.read(5),None)/100)
        if Detail:
            if Tag in (Spendings,None):Zoom.append(str(Self)+" Extra=£"+str(R[-1])+("0"if str(R[-1])[-2]=="."else""))
        Cost-=R[-1]
        if Self.__Multiple:
            for i in Self.__Cats:
                app,c=i.Stepin(Cost,File,Detail,Tag,Zoom,Spendings)
                Cost=int(c*100+0.5)/100
                R+=app
        else:
            It=tuple(File.read(1))
            for i in range(It[0]):
                It+=(byteSplit(File.read(5),None)/100,byteSplit(File.read(2),None))
                if Detail:
                    if Tag in (Spendings,None)and It[-2]*It[-1]:Zoom.append("\t"+str(Self)+" Set"+str(i+1)+"=£"+str(It[-2])+("0"if str(It[-2])[-2]=="."else"")+" X "+str(It[-1])+" = £"+str(It[-2]*It[-1])+("0"if str(It[-2]*It[-1])[-2]=="."else""))
                Cost-=It[-1]*It[-2]
            R+=It[1:]
        return R,Cost
    def __ExtATR(Self,File):
        Len=File.Read()
        if Len>=235:Title,Self.__Preset=("","Bills.","Trip out.","Tax.","Gas.","Electricity.","Water.","Shopping.","Leisure.","Eating out.","Groceries.","Clothes.","Games.","Furniture.","Golf.","Bread.","Vegetables.","Drinks.","Sweets.","Condiments.",)[Len-235],True
        else:
            Self.__Preset=False
            Title=""
            for i in range(Len+1):Title+=chr(File.Read())
        Self.__Name=Title
        Len=File.Read(3)
        if Len>8388607:Self._TypCost,Self.__Multiple=Len-8388608,False
        else:
            Self.__Cats=[]
            Self.__Multiple=True
            for i in range(Len):
                Self.__Cats.append(ReadItem(None))
                Self.__Cats[-1].__ExtATR(File)
    def __str__(self):return self.__Name
    def __SetupWrite(Self): # This is where the file is initially written to.
        File=Get(file)
        File.ReWrite()
        BYTESET=b"S\x08\x00"+bytes([len(Name)]+[ord(i)for i in Name])
        File.Write(BYTESET)
        File.Write(payDay)
        File.Write(PAy,Min=3)
        Self.__ExtINT(File)
        File=File.Transfer("a")
        Self.__BKmark=File.seek(0,1)
        global Cash
        global startMon
        Cash=0
        if startMon==0:return
        present=date.today()
        Initial=bytes([96+present.month*2+present.day//32,present.day%32*8+2,128+(int(log2(startMon))//8+1 if startMon<=9223372036854775807 else 63)])+b'Initial setup.'#"0-1-1-? ???-? | ???? ?-010 | 10-?? ????". (Spending or reminder,type)
        if startMon>9223372036854775807:
            startMon=9223372036854775807
            GUI.messagebox.showwarning("Overflow.","The amount you entered as a starting amount of cash exceeds the limit.\nIt has been lowered to 9223372036854775807.")
        Nbytes=b""
        Cash=startMon
        while startMon>0:
            Nbytes=bytes((startMon%256,))+Nbytes
            startMon=startMon//256
        Initial+=Nbytes
        File.write(Initial)
    def __ExtINT(Self,File):
        if Self.__Preset:File.Write(235+("","Bills.","Trip out.","Tax.","Gas.","Electricity.","Water.","Shopping.","Leisure.","Eating out.","Groceries.","Clothes.","Games.","Furniture.","Golf.","Bread.","Vegetables.","Drinks.","Sweets.","Condiments.",).index(Self.__Name))
        else:File.Write(bytes((len(Self.__Name)-1,)+(*(ord(i)for i in Self.__Name),)))
        if Self.__Multiple:
            File.Write(len(Self.__Cats),Min=3)
            for i in Self.__Cats:i.__ExtINT(File)
        else:File.Write(Self._TypCost+8388608 if Self._TypCost<=8388607 else 0,Min=3)
    def __iter__(Self):#This makes this object an iterable object.
        Self.__i=-1
        return Self
    def __next__(Self):
        Self.__i+=1
        try:return Self.__iterItem(Self.__Cats[Self.__i])
        except IndexError:raise StopIteration
    def Recursion(Self,Level=0):
        if len(Self.__Cats)==0:return Self._TypCost
        else:
            R=sum(i.Recursion(Level)for i in Self.__Cats)
            if Level>63:Self._TypCost=R
            elif Level>0:pass
            else:Self._TypCost=(R*Level+Self._TypCost*(64-Level))/64
            return Self._TypCost
    __bool__=lambda s:s.__Multiple and len(s.__Cats)>0
    class __iterItem():
        _recording=False
        def __init__(Self,Item):
            if not isinstance(Item,ReadItem):raise TypeError("__iterItem expects ReadItem not "+str(type(Item))+".")
            Self._Name,Self._Multiple,Self._Preset,Self._TypCost,Self.__ID,Self.__Cats=Item.Retu()
            Self._Entries=[]
        def __str__(self):return self._Name
        def __iter__(Self):#This makes this object an iterable object.
            Self.__i=-1
            if Self._recording and not"_iterItem__Kittens"in Self.__dict__:raise StopIteration
            return Self
        def __next__(Self):
            Self.__i+=1
            if Self._recording:
                try:return Self.__Kittens[Self.__i]
                except IndexError:raise StopIteration
            else:
                try:return type(Self)(Self.__Cats[Self.__i])
                except (IndexError,AttributeError):raise StopIteration
        def __len__(Self):
            try:
                if Self.__Cats==((),):return 0
                return len(Self.__Cats)
            except AttributeError:return 0
        def __bool__(Self):
            if'_iterItem__parent' in Self.__dict__:
                if Self.__parent!=None:return True
            return False
        def record(Self,parent=None):
            Self._recording=True
            Self.Cost=0
            if Self._Multiple:
                Self.__Kittens=[]
                for i in Self.__Cats:
                    Self.__Kittens.append(type(Self)(i))
                    Self.__Kittens[-1].record(Self)
            else:Self.__Kittens=[Self.__Terminal(Self)]
            Self.__parent=parent
        def Step(Self,other=None):
            if other==None:other=Self.__parent
            DelSet=set()
            try:
                for i in range(len(Self.__Kittens)):
                    if not Self._Entries[i]==None:
                        try:
                            if int(float((Self._Entries[i][0]if isinstance(Self._Entries[i],tuple)else Self._Entries[i]).get())*100)<0:
                                GUI.messagebox.showerror("Invalid data.","Negative values are forbiden.")
                                return
                            Self.__Kittens[i].Cost=int(float((Self._Entries[i][0]if isinstance(Self._Entries[i],tuple)else Self._Entries[i]).get())*100)
                            if isinstance(Self._Entries[i],tuple):
                                Self.__Kittens[i].Quan=int(Self._Entries[i][1].get())
                                if Self.__Kittens[i].Cost*Self.__Kittens[i].Quan==0 and i>0:
                                    print(Self.__Kittens[i],"will be deleated £"+str(Self.__Kittens[i].Cost),Self.__Kittens[i].Quan)
                                    DelSet.add(i)
                        except ValueError as e:
                            GUI.messagebox.showerror("Invalid data.",str(e))
                            return
                for i in DelSet:del Self.__Kittens[i]
                try:
                    if int(float(Self._Entries[-1].get())*100)<0:
                        GUI.messagebox.showerror("Invalid data.","Negative values are forbiden.")
                        return
                    Self.Cost=int(float(Self._Entries[-1].get())*100)
                except ValueError as e:
                    GUI.messagebox.showerror("Invalid data.",str(e))
                    return
            except IndexError:
                Can=False
                while not Can:
                    Sol=GUI.messagebox.askretrycancel("An unexpected error has occured.","An error has occured.\nRetrying will reset this catagory.\nCanceling will delete this record.",icon="error")
                    if Sol:
                        Can=True
                        Self.__Kittens=[Self.__Terminal(Self)]
                    else:
                        Can=Cancel(Self)
                        if Can:return
            Self._Entries.clear()
#            print("len: ",Self.__Kittens,"==",len(Self.__Kittens))
#            if len(Self.__Kittens)==0:Self.__Kittens.append(Self.__Terminal(Self))
            if not"_iterItem__Kittens"in other.__dict__:other.__Kittens=[Self.__Terminal(Self)]
            SpendingAdj(other)
        def getCost(Self):return Self.Cost+sum(i.getCost()for i in Self.__Kittens)
        def NewTerminal(Self,X,y,Add,Lab,Am):
            y-=28
            Self.__Kittens.append(Self.__Terminal(Self))
            Label=GUI.Label(Win,text="Set "+str(int((y-4)//28))+" £",bg="#FFC0FF")
            Label.place(x=X,y=y)
            Amount=GUI.Entry(Win)
            Amount.place(x=X+Label.winfo_reqwidth(),y=y)
            Amount.insert(0,str(Self.__Kittens[-1].Cost/100)+("0"if str(Self.__Kittens[-1].Cost/100)[-2]=="." else""))
            Open=GUI.Label(Win,text=" X ",bg="#FFC0FF")
            Open.place(x=X+Label.winfo_reqwidth()+Amount.winfo_reqwidth(),y=y)
            Quan=GUI.Entry(Win)
            Quan.place(x=X+Label.winfo_reqwidth()+Amount.winfo_reqwidth()+Open.winfo_reqwidth(),y=y)
            Quan.insert(0,"1")
            Self._Entries.append(Self._Entries[-1])
            Self._Entries[-2]=(Amount,Quan)
            y+=56
            Add.config(command=lambda:Self.NewTerminal(X,y,Add,Lab,Am))
            Add.place(x=X,y=y-28)
            Lab.place(x=X,y=y)
            Am.place(x=X+Label.winfo_reqwidth(),y=y)
        class __Terminal():
            Cost=0
            Quan=1
            _recording=True
            def __init__(Self,parent,Count=1):
                Self.__parent=parent
                Self._Name="Set "+str(Count)+":"
            def __str__(self):return self._Name
            def __bool__(Self):return True
            def getCost(Self):return Self.Cost*Self.Quan
        def Save(Self):
            if not GUI.messagebox.askyesno("Finalize?","Are you sure everything is correct?\nYou won't be able to undo."):return

            DelSet=set()
            try:
                for i in range(len(Self.__Kittens)):
                    if not Self._Entries[i]==None:
                        try:
                            if int(float((Self._Entries[i][0]if isinstance(Self._Entries[i],tuple)else Self._Entries[i]).get())*100)<0:
                                GUI.messagebox.showerror("Invalid data.","Negative values are forbiden.")
                                return
                            Self.__Kittens[i].Cost=int(float((Self._Entries[i][0]if isinstance(Self._Entries[i],tuple)else Self._Entries[i]).get())*100)
                            if isinstance(Self._Entries[i],tuple):
                                Self.__Kittens[i].Quan=int(Self._Entries[i][1].get())
                                if Self.__Kittens[i].Cost*Self.__Kittens[i].Quan==0 and i>0:DelSet.add(i)
                        except ValueError as e:
                            GUI.messagebox.showerror("Invalid data.",str(e))
                            return
                for i in DelSet:del Self.__Kittens[i]
                try:
                    if int(float(Self._Entries[-1].get())*100)<0:
                        GUI.messagebox.showerror("Invalid data.","Negative values are forbiden.")
                        return
                    Self.Cost=int(float(Self._Entries[-1].get())*100)
                except ValueError as e:
                    GUI.messagebox.showerror("Invalid data.",str(e))
                    return
            except IndexError:
                Can=False
                while not Can:
                    Sol=GUI.messagebox.askretrycancel("An unexpected error has occured.","An error has occured.\nRetrying will reset this catagory.\nCanceling will delete this record.",icon="error")
                    if Sol:
                        Can=True
                        Self.__Kittens=[Self.__Terminal(Self)]
                    else:
                        Can=Cancel(Self)
                        if Can:return
            Self._Entries.clear()

            Move()
            Win.config(bg="#FF80C0")
            PleaseWait=GUI.Label(Win,text="Please wait.\nSaving.",bg="#FF80C0")
            PleaseWait.place(x=12,y=12)
            Win.update()
            Self.__Save()
        def __Save(Self):
            if isinstance(Self.__parent,type(Self)):
                Self.__parent.__Save()
                return
            global Cash
            Cash-=Self.getCost()/100
            if Cash<0:GUI.messagebox.showwarning("Overdrawn.","You now have a negative amount of cash!")
            present=date.today()
            File=open(file,"ab")
            global Fincr
            if len(Self.__ID)>63:raise Exception
            File.write(bytes((present.month*2+present.day//32,present.day%32*8,len(Self.__ID))))
            Fincr=3
            File.write(Self.__ID)
            Fincr+=1
            Self.__Savestep(File)
            MainMenu()
        def __Savestep(Self,File):
            global Fincr
            File.write(bytes(((int(Self.Cost//2**(8*4))),(int(Self.Cost//2**(8*3)))%256,(int(Self.Cost//2**(8*2)))%256,(int(Self.Cost//2**8))%256,(int(Self.Cost)%256)))if Self.Cost<1099511627775 else b"\xFF\xFF\xFF\xFF\xFF")
            Fincr+=5
            if Self._Multiple:
                for i in Self.__Kittens:i.__Savestep(File)
            else:
                File.write(bytes((len(Self.__Kittens),)),)
                Fincr+=1
                for i in Self.__Kittens:
                    File.write(bytes(((int(i.Cost//2**(8*4))),(int(i.Cost//2**(8*3)))%256,(int(i.Cost//2**(8*2)))%256,(int(i.Cost//2**8))%256,(int(i.Cost)%256)))if i.Cost<1099511627775 else b"\xFF\xFF\xFF\xFF\xFF")
                    Fincr+=5
                    File.write(bytes(((int(i.Quan//2**8))%256,(int(i.Quan)%256)))if i.Quan<65535 else b"\xFF\xFF\xFF\xFF\xFF")
                    Fincr+=2
class Scroll():
    def __init__(Self,Array,Length):
        Self.__Array=Array
        if Length>len(Array):Self.__Top=0
        else:Self.__Top=len(Array)-Length
        Self.__Bottom=len(Array)
    def Up(Self):
        if Self.__Top>0:
            Self.__Top-=1
            Self.__Bottom-=1
    def Down(Self):
        if Self.__Bottom<len(Self.__Array):
            Self.__Top+=1
            Self.__Bottom+=1
    def __str__(Self):
        Str=""
        for i in Self.__Array[Self.__Top:Self.__Bottom]:Str+=str(i)+"\n"
        return Str
def Configure(Widget,Obsx,Obsy):
    "(Widget,Widget),((If width<=#: xwidth+l,x=#,l=#),(If width<=#: xwidth+l,x=#,l=#)),((If width<=#: ywidth+l,y=#,l=#),(If width<=#: ywidth+l,y=#,l=#))),(((If width<=#: ywidth+l,y=#,l=#),(If width<=#: ywidth+l,y=#,l=#)),((If width<=#: ywidth+l,y=#,l=#),(If width<=#: ywidth+l,y=#,l=#)))"# This line is a comment.
    IF=lambda T,Tup:T*Tup[0][1]+Tup[0][2]if T<=Tup[0][0]else IF(T,Tup[1:])
    if len(Widget)!=len(Obsx)or len(Widget)!=len(Obsy):raise ValueError(len(Widget),len(Obsx),len(Obsy),"are not the same.")
    for i in range(len(Obsx)):
        try:Widget[i].place(x=IF(Win.winfo_width(),Obsx[i]))
        except IndexError:Widget[i].place(x=Win.winfo_width()*Obsx[i][-1][-2]+Obsx[i][-1][-1])
    for i in range(len(Obsy)):
        try:Widget[i].place(y=IF(Win.winfo_height(),Obsy[i]))
        except IndexError:Widget[i].place(y=Win.winfo_height()*Obsy[i][-1][-2]+Obsy[i][-1][-1])
def Manadd(Name,Amount,sign):
    try:Amount=int(Amount)
    except ValueError:
        GUI.messagebox.showerror("Invalid amount.","The number you have entered is invalid.\nNaN error: Not an integer.")
        Amount=0
    if len(Name)>3 and len(Name)<36 and int(Amount)>0 and not True in (i>255 for i in(ord(j)for j in Name)):
        present=date.today()
        Initial=bytes([64+(32 if sign else 0)+present.month*2+present.day//32,present.day%32*8+int((len(Name)-4)//4),((len(Name)-4)%4)*64+(int(log2(Amount))//8+1 if Amount<=9223372036854775807 else 63)])+Name.encode("utf8")#"0-1-1-? ???-? ???? ?-??? ??-?? ????". (Spending or reminder,type,add or sdubtract,Month,Day,Text length,Number length)
        print("Initial="+str(tuple(Initial)))
        Nbytes=b""
        if Amount>9223372036854775807:
            Amount=9223372036854775807
            GUI.messagebox.showwarning("Overflow.","You have entered an amount that exceeds the limit.\nIt has been lowered to 9223372036854775807.")
        global Cash
        try:Cash+=Amount*(1 if sign else -1)
        except OverflowError as e:return GUI.messagebox.showerror("An exception has occured.",str(type(e))+"\n"+str(e))
        if Cash<0:GUI.messagebox.showwarning("Overdrawn.","You now have a negative amount of cash!")
        while Amount>0:
            Nbytes=bytes((Amount%256,))+Nbytes
            Amount=Amount//256
        Initial+=Nbytes
        File=open(file,"ab")
        File.write(Initial)
        File.close()
        MainMenu()
    else:
        if len(Name)<4 or len(Name)>35:GUI.messagebox.showerror("Invalid name.","Refference text is too "+("short"if len(Name)<4 else"long")+".\nPlease re-enter.")
        if Amount<1:GUI.messagebox.showerror("Invalid amount.","The number you have entered is invalid.\nSize error: Must be bigger than 0.")
        if True in (i>255 for i in(ord(j)for j in Name)):GUI.messagebox.showerror("Invalid name.","Refference text containes an invalid character.\nPlease re-enter.")
def MainMenu():
    Win.title("Spending tracker.")
    Move()
    Win.unbind("<Up>")
    Win.unbind("<Down>")
    Win.unbind("<Return>")
    Win.config(bg="#E0E000")
    try:Welcome=GUI.Label(Win,text="Welcome "+Name+("."if Name[-1]!="."else"")+"\nYou should have £"+str(Cash)+("0"if str(Cash)[-2]=="."else"")+".\n What would you like to do?",bg="#E0E000")
    except IndexError:Welcome=GUI.Label(Win,text="Welcome "+Name+".\nYou should have £"+str(Cash)+".\n What would you like to do?",bg="#E0E000")
    Welcome.place(x=0,y=0)
    ManualButton=GUI.Button(Win,text="Manual adjustment.",width=96,height=4,command=ManualChange,bg="#FFFF00",highlightbackground="#E0E000")
    ManualButton.place(x=0,y=0)
    RecButton=GUI.Button(Win,text="Recall.",width=96,height=4,command=Recall,bg="#00FF00",highlightbackground="#00FF00")
    RecButton.place(x=0,y=0)
    Setti=GUI.Button(Win,text="Settings",command=Settings,bg="#FFFF00",width=96,height=4,highlightbackground="#E0E000")
    Setti.place(x=4,y=4)
    if Set:
        RecoButton=GUI.Button(Win,text="Record spending.",width=96,height=4,command=Spending,bg="#FF80C0",highlightbackground="#FF80C0")
        RecoButton.place(x=256,y=14)
    Win.update_idletasks()
    Welcome.place(x=Win.winfo_width()//2-Welcome.winfo_width()//2,y=16)
    ManualButton.place(x=Win.winfo_width()//2-ManualButton.winfo_width()//2,y=256)
    RecButton.place(x=Win.winfo_width()//2-ManualButton.winfo_width()//2,y=192)
    if Set:RecoButton.place(x=Win.winfo_width()//2-ManualButton.winfo_width()//2,y=128)
    Setti.place(x=Win.winfo_width()//2-ManualButton.winfo_width()//2,y=340)
    Win.update()
def Settings():
    Move()
    Label=GUI.Label(Win,text="Settings are not responding. An error may have occured.",bg="#FF0000")
    Label.place(x=Win.winfo_width()//2-Label.winfo_reqwidth()//2,y=16)
    File=open(file,"r+b")
    if File.read(3)!=b"S\x08\x00":raise FileNotFoundError("File \""+file+"\" has been flagged as corrupt, due to an incorrect check-prefix.")
    Back=GUI.Button(Win,text="Back.",command=lambda:(File.close(),MainMenu()),highlightbackground="#E0E000")
    Back.place(x=16,y=576)
    Name=GUI.Button(Win,text="Change name.",command=lambda:SetupA2(File),width=24,height=2,highlightbackground="#E0E000")
    Name.place(x=Win.winfo_width()//2-Name.winfo_reqwidth()//2,y=96)
    PayDay=GUI.Button(Win,text="Change PayDay.",command=lambda:SetupB2(File),width=24,height=2,highlightbackground="#E0E000")
    Amount=GUI.Button(Win,text="Change income amount.",command=lambda:SetupC2(File),width=24,height=2,highlightbackground="#E0E000")
    PayDay.place(x=Win.winfo_width()//2-PayDay.winfo_reqwidth()//2,y=144)
    Amount.place(x=Win.winfo_width()//2-Amount.winfo_reqwidth()//2,y=192)
    Label.config(text="Name: "+globals()["Name"]+"\nPay day: "+(str(payDay)if payDay>0 else"None")+"\nMonthly income: "+str(Pay)+"\nChoose a setting.",bg="#E0E000")
    Label.place(x=Win.winfo_width()//2-Label.winfo_reqwidth()//2,y=16)
def Cancel(Cat=None,Prompt=True):
    if Prompt:
        if not GUI.messagebox.askyesno("Quit without saving?","Are you suer you want to cancel?",icon="warning"):return False
    if Cat==None:MainMenu()
    else:
        Next=Cat.__dict__["_iterItem__parent"]
        Cat._Entries.clear()
        del Cat
        Cancel(Next,False)
    return True
def Spending(Cat=None):
    Move()
    if Cat==None:Cat=Set
    Back=GUI.Button(Win,text="Back.",command=MainMenu,highlightbackground="#FF80C0")
    Back.place(x=16,y=576)
    X=12 # Constant.
    y=32
    for i in Cat:
        Label=GUI.Label(Win,text=str(i),bg="#E0E000")
        Label.place(x=X,y=y)
        Forward=GUI.Button(Win,text="Record.",command=lambda i=i:SpendingAdj(i),highlightbackground="#FF80C0")
        Forward.place(x=X+Label.winfo_reqwidth(),y=y)
        if len(i)>0:
            Entry=GUI.Button(Win,text="Open.",command=lambda i=i:(Spending(i),Win.title(str(i))),highlightbackground="#FF80C0")
            Entry.place(x=X+Label.winfo_reqwidth()+Forward.winfo_reqwidth(),y=y)
        y+=24
def SpendingAdj(Cat):
    Win.title(str(Cat))
    Move()
    if not Cat._recording:Cat.record()
    Inst=GUI.Label(Win,text="Choose how much money you spent on each item.\nIf you don't wan't to be specific, or you don't know exactly where the money went, then use the \"extra\" field.",bg="#FFC0FF")
    Win.config(bg="#FFC0FF")
    Inst.place(x=0,y=0)
    Back=GUI.Button(Win,text="Return."if bool(Cat)else"Cancel.",command=Cat.Step if bool(Cat)else Cancel,highlightbackground="#FFC0FF")
    Back.place(x=16,y=576)
    Save=GUI.Button(Win,text="Save.",command=Cat.Save,highlightbackground="#FFC0FF")
    Save.place(x=256,y=576)
    X=12 # Constant.
    y=32
    Term=False
    for i in Cat:
        Label=GUI.Label(Win,text=(str(i)if isinstance(i,type(Cat))else "Set "+str(int((y-4)//28)))+" £",bg="#FFC0FF")
        Label.place(x=X,y=y)
        Amount=GUI.Entry(Win)
        Amount.place(x=X+Label.winfo_reqwidth(),y=y)
        Amount.insert(0,str(i.Cost/100)+("0"if str(i.Cost/100)[-2]=="." else""))
        Cat._Entries.append(Amount)
        if isinstance(i,type(Cat)):
            Open=GUI.Button(Win,text="Enter.",command=lambda i=i:Cat.Step(i),highlightbackground="#FFC0FF")
            Open.place(x=X+Label.winfo_reqwidth()+Amount.winfo_reqwidth(),y=y)
            Total=GUI.Label(Win,text="Total: £"+str(i.getCost()/100)+("0"if str(i.getCost()/100)[-2]=="." else""),bg="#FFC0FF")
            Total.place(x=X+Label.winfo_reqwidth()+Amount.winfo_reqwidth()+Open.winfo_reqwidth(),y=y)
        else:
            Term=True
            Open=GUI.Label(Win,text=" X ",bg="#FFC0FF")
            Open.place(x=X+Label.winfo_reqwidth()+Amount.winfo_reqwidth(),y=y)
            Quan=GUI.Entry(Win)
            Quan.place(x=X+Label.winfo_reqwidth()+Amount.winfo_reqwidth()+Open.winfo_reqwidth(),y=y)
            Quan.insert(0,str(i.Quan))
            Cat._Entries[-1]=(Cat._Entries[-1],Quan)
        y+=28
    if Term:
        Add=GUI.Button(Win,text="+",command=lambda:Cat.NewTerminal(X,y,Add,Label,Amount),highlightbackground="#FFC0FF")
        Add.place(x=X,y=y)
        y+=28
    Label=GUI.Label(Win,text="Extra: £",bg="#FFC0FF")
    Label.place(x=X,y=y)
    Amount=GUI.Entry(Win)
    Amount.place(x=X+Label.winfo_reqwidth(),y=y)
    Amount.insert(0,str(Cat.Cost/100)+("0"if str(Cat.Cost/100)[-2]=="." else""))
    Cat._Entries.append(Amount)
def Recall(Tag=None): # Amounts should be lined up.
    Move()
    Back=GUI.Button(Win,text="Back.",command=MainMenu,highlightbackground="#00FF00")
    Back.place(x=16,y=576)
    Label=GUI.Label(Win,text="Your history:\nPlease wait.",bg="#E0E000")
    Label.place(x=Win.winfo_width()//2-Label.winfo_reqwidth()//2,y=8)
    Win.update()
    File=open(file,"rb")
    Cash,ListAr,ListSp=Set.Scan(File,Tag=Tag)
    File.close()
    try:Label.config(text="Current cash = £"+str(Cash)+("0"if str(Cash)[-2]=="."else"")+".\nYour history:",bg="#00FF00")
    except IndexError:Label.config(text="Current cash = £"+str(Cash)+".\nYour history:",bg="#00FF00")
    Str=""
    for i in ListAr[max(0,len(ListAr)-24):len(ListAr)]:Str+=i+"\n"
    Str=Str[:-1]
    Stri=""
    for i in ListSp[max(0,len(ListSp)-16):len(ListSp)]:Stri+=i+"\n"
    Stri=Stri[:-1]
    ListVar=Scroll(ListAr,24)
    SpVar=Scroll(ListSp,16)
    List=GUI.Label(Win,text=Str,bg="#00FF00",justify="left")
    List.place(x=48,y=48)
    Spwn=GUI.Label(Win,text=Stri,bg="#00FF00",justify="left")
    Spwn.place(x=Win.winfo_width()//2,y=64)
    Win.config(bg="#00FF00")
    ScrUp=lambda x=None:(ListVar.Up(),List.config(text=str(ListVar)),SpVar.Up(),Spwn.config(text=str(SpVar)))
    ScrDown=lambda x=None:(ListVar.Down(),List.config(text=str(ListVar)),SpVar.Down(),Spwn.config(text=str(SpVar)))
    UpButton=GUI.Button(Win,text="Up.",command=ScrUp,highlightbackground="#00FF00")
    DownButton=GUI.Button(Win,text="Down.",command=ScrDown,highlightbackground="#00FF00")
    UpButton.place(x=392,y=534)
    DownButton.place(x=392,y=576)
    Win.bind("<Up>",ScrUp)
    Win.bind("<Down>",ScrDown)
    if Set:
        Serch=GUI.Entry(Win)
        Serch.place(x=160,y=576)
        def F():
            try:Recall(getNumber(Serch.get().upper().strip()))
            except ValueError as e:GUI.messagebox.showerror("An exception has occured.",str(type(e))+"\n"+str(e))
        Find=GUI.Button(Win,text="Find by ID.",command=F,highlightbackground="#00FF00")
        Find.place(x=312,y=576)
def ManualChange():
    Move()
    Back=GUI.Button(Win,text="Back.",command=MainMenu,highlightbackground="#E0E000")
    Back.place(x=16,y=576)
    Label=GUI.Label(Win,text="How much?",bg="#E0E000")
    Label.place(x=Win.winfo_width()//2-Label.winfo_reqwidth()//2,y=8)
    NLabel=GUI.Label(Win,text="Reference text (4-35 characters.):",bg="#E0E000")
    CLabel=GUI.Label(Win,text="Actual amount. £",bg="#E0E000")
    NLabel.place(x=Win.winfo_width()//2-208,y=48)
    CLabel.place(x=Win.winfo_width()//2-128,y=72)
    AdSub=GUI.BooleanVar()
    AdSub.set(True)
    Plus=GUI.Radiobutton(Win,text="+",variable=AdSub,value=True,bg="#E0E000")
    Subt=GUI.Radiobutton(Win,text="-",variable=AdSub,value=False,bg="#E0E000")
    Name=GUI.Entry(Win)
    Amount=GUI.Entry(Win)
    Plus.place(x=Win.winfo_width()//2+Plus.winfo_reqwidth()//2,y=128)
    Subt.place(x=Win.winfo_width()//2+Subt.winfo_reqwidth()//2,y=192)
    Name.place(x=Win.winfo_width()//2,y=48)
    Amount.place(x=Win.winfo_width()//2,y=72)
    go=GUI.Button(Win,text="Set.",command=lambda:Manadd(Name.get(),Amount.get(),AdSub.get()),highlightbackground="#E0E000")
    go.place(x=976,y=576)
    Amount.focus_set()
    Win.bind("<Return>",lambda x:Manadd(Name.get(),Amount.get(),AdSub.get()))
def SetupA(Error="Resetting."):
    Move()
    Name=GUI.Entry(Win)
    Next=GUI.Button(Win)
    Label=GUI.Label(Win,text=Error,bg="#FF0000")
    Next.config(text="Next.",command=lambda:SetupB(Name.get()))
    Instructions=GUI.Label(Win,text="If the file got corrupted, see if you have a backup.\n\nThe data file needs to be in the same directory as the program to be read.\n\nThis error may be because you are simply using the file for the first time. If that is the case; you will now need to setup the file.\nPlease start by entering your name.",justify="left",bg="#FFFF00")
    Instructions.place(x=16,y=16+Label.winfo_reqheight())
    Name.place(x=16,y=32+Label.winfo_reqheight()+Instructions.winfo_reqheight())
    Next.place(x=976,y=704)
    Label.place(x=16,y=8)
    Name.focus_set()
    Win.bind("<Return>",lambda x:SetupB(Name.get()))
#    Configure((Label,Name,Next),(((1024,0.0,0),(0.0,16)),((800,0.0,0),(0.0,16)),((800,1.0,-148),(1024,0.5,256),(0.0,976)),),((((768,0.0,0),(0.0,8)),((768,0.0,0),(0.0,64)),((512,1.0,-16),(768,0.5,240),(0.0,704)),)))
def SetupA2(File):
    Move()
    Length=File.read(1)[0]
    Label=GUI.Label(Win,text="Choose a new name.",bg="#E0E000",highlightbackground="#E0E000")
    Label.place(x=16,y=8)
    Back=GUI.Button(Win,text="Back.",command=lambda:(File.close(),Settings()),highlightbackground="#E0E000")
    Back.place(x=16,y=576)
    Name=GUI.Entry(Win)
    Name.place(x=16,y=32+Label.winfo_reqheight())
    Next=GUI.Button(Win,text="Next.",command=lambda:SetupA3(File,Name.get(),Length),highlightbackground="#E0E000")
    Next.place(x=976,y=640)
    Win.bind("<Return>",lambda x:SetupA3(File,Name.get(),Length))
def SetupA3(File,Name,Length):
    if True in (i>255 for i in(ord(j)for j in Name)):
        GUI.messagebox.showerror("Invalid name.","The name you have entered contains an invalid character.")
        return
    if len(Name)!=Length:
        GUI.messagebox.showerror("Invalid name.","The name you have entered is too "+("short"if len(Name)<Length else"long")+".\nName must be exactly "+str(Length)+" character"+("s"if Length>1 else"")+".")
        return
    File.write(bytes(Name,"utf-8"))
    globals()["Name"]=Name
    Win.unbind("<Return>")
    File.close()
    Settings()
def SetupB(name):
    if len(name)>255 or len(name)==0:
        GUI.messagebox.showerror("Invalid name.","The name you have entered is too short/long.\nName must be from 1 to 255 characters.")
        return
    if True in (i>255 for i in(ord(j)for j in name)):
        GUI.messagebox.showerror("Invalid name.","The name you have entered contains an invalid character.")
        return
    Move()
    Win.unbind("<Return>")
    Label=GUI.Label(Win,text="Hello "+name+". Please click your day of pay.",bg="#FFFF00")
    Label.place(x=8,y=8)
    global Name
    Name=name
    Days=[]
    for i in range(28):
        Days.append(GUI.Button(Win))
        Days[i].config(text=str(i+1),command=lambda i=i:SetupC(i+1))
        Days[i].place(x=48+(i%7)*64,y=48+(i//7)*64)
    Skip=GUI.Button(Win,text="I'll enter my income manually for each month.",command=lambda:SetupC(0))
    Skip.place(x=48,y=320)
def SetupB2(File):
    Move()
    File.seek(File.read(1)[0],1)
    Back=GUI.Button(Win,text="Back.",command=lambda:(File.close(),Settings()),highlightbackground="#E0E000")
    Back.place(x=16,y=576)
    Label=GUI.Label(Win,text="Please click your new day of pay.",bg="#E0E000")
    Label.place(x=8,y=8)
    Days=[]
    for i in range(28):
        Days.append(GUI.Button(Win))
        Days[i].config(text=str(i+1),command=lambda i=i:SetupB3(File,i+1),highlightbackground="#E0E000")
        Days[i].place(x=48+(i%7)*64,y=48+(i//7)*64)
    Skip=GUI.Button(Win,text="I'll enter my income manually for each month.",command=lambda:SetupB3(File,0),highlightbackground="#E0E000")
    Skip.place(x=48,y=320)
def SetupB3(File,Day):
    File.write(bytes((Day,),))
    globals()["payDay"]=Day
    File.close()
    Settings()
def SetupC(Day):
    global payDay
    payDay=Day
    if Day==0:return SetupD(0)
    Move()
    Label=GUI.Label(Win,text="How much do you get paid on this day?",bg="#FFFF00")
    Label.place(x=8,y=8)
    PLabel=GUI.Label(Win,text="£",bg="#FFFF00")
    PLabel.place(x=16,y=32)
    Pay=GUI.Entry(Win)
    Next=GUI.Button(Win,text="Next.",command=lambda:SetupD(Pay.get()))
    Pay.place(x=32,y=32)
    Next.place(x=976,y=704)
    Pay.focus_set()
    Win.bind("<Return>",lambda x:SetupD(Pay.get()))
def SetupC2(File):
    Move()
    File.seek(File.read(1)[0]+1,1)
    Label=GUI.Label(Win,text="How much is your new monthly pay?",bg="#E0E000")
    Label.place(x=8,y=8)
    Back=GUI.Button(Win,text="Back.",command=lambda:(File.close(),Settings()),highlightbackground="#E0E000")
    Back.place(x=16,y=576)
    PLabel=GUI.Label(Win,text="£",bg="#E0E000")
    PLabel.place(x=16,y=32)
    Pay=GUI.Entry(Win)
    Next=GUI.Button(Win,text="Next.",command=lambda:SetupC3(File,Pay.get()),highlightbackground="#E0E000")
    Pay.place(x=32,y=32)
    Next.place(x=976,y=704)
    Pay.focus_set()
    Win.bind("<Return>",lambda x:SetupC3(File,Pay.get()))
def SetupC3(File,Pay):
    try:
        Pay=int(Pay)
        if Pay<0:
            GUI.messagebox.showerror("Invalid amount.","Pay must be greater than 0.")
            return
    except ValueError as e:
        GUI.messagebox.showerror("An exception has occured.",str(type(e))+"\n"+str(e))
        return
    File.write((bytes(((int(Pay//2**(8*2)))%256,(int(Pay//2**8))%256,(int(Pay)%256)),))if Pay<16777215 else b"\xFF\xFF\xFF")
    File.close()
    globals()["Pay"]=Pay if Pay<16777215 else 16777215
    if Pay>16777215:GUI.messagebox.showwarning("Data has been automatically adjusted.","The number you have entered is too large.\nIt has been reduced to 16777215.")
    Win.unbind("<Return>")
    Settings()
def SetupD(pay):
    try:
        global PAy
        PAy=int(pay)
        if PAy>16777215:raise ValueError("Pay is too big. It should be 16777215 or smaller.")
        elif PAy<0:raise ValueError("Pay is too small. It should be 0 or bigger.")
    except ValueError as e:
        GUI.messagebox.showerror("An exception has occured.",str(type(e))+"\n"+str(e))
        return
    Move()
    Win.unbind("<Return>")
    Label=GUI.Label(Win,text="How much money do you currently have?",bg="#FFFF00")
    Label.place(x=8,y=8)
    PLabel=GUI.Label(Win,text="£",bg="#FFFF00")
    PLabel.place(x=16,y=32)
    Pay=GUI.Entry(Win)
    Next=GUI.Button(Win,text="Next.",command=lambda:SetupD2(Pay.get()))
    Pay.place(x=32,y=32)
    Next.place(x=976,y=704)
    Pay.focus_set()
    Win.bind("<Return>",lambda x:SetupD2(Pay.get()))
def SetupD2(pay):
    global startMon
    try:
        if int(pay)<0:raise ValueError("Starting amount must be positive.\nIf you would like to start at a negative amount, please make a manual adjustment later.")
        startMon=int(pay)
    except ValueError as e:
        GUI.messagebox.showerror("An exception has occured.",str(type(e))+"\n"+str(e))
        return
    Move()
    global M
    global Pay
    M=Presets()
    Pay=PAy
    M.gridPlace(32,64,32,32)
    Win.unbind("<Return>")
def SetupE(self,other):
    if not self.Exists(other):
        GUI.messagebox.showerror("Error.","There was an error performing this action.")
        return
    global NavArray
    self.presetUpdate()
    other.setIncluded()
    Move(True)
    other.gridPlace(32,64,32,32)
    NavArray+=[self]
    GUI.Button(Win,text="Back.",command=lambda:SetupBack(self,other)).place(x=976,y=704)
def SetupBack(self,other):
    global NavArray
    other.presetUpdate()
    Move(True)
    self.gridPlace(32,64,32,32)
    NavArray=NavArray[:-1]
    if len(NavArray)>0:GUI.Button(Win,text="Back.",command=lambda:SetupBack(NavArray[-1],self)).place(x=976,y=704)
    else:GUI.Button(Win,text="Next.",command=lambda:SetupF(M,True)).place(x=976,y=704)
def SetupF(M,original=False):
    M.presetUpdate()
    if not GUI.messagebox.askyesno("Continue?","The file will now be created.\nYou will not be able to change these categories later without resetting the program.\nAre you sure that you want to continue?"):return
    Move()
    PleaseWait=GUI.Label(Win,text="Creating \""+file+"\". Please wait.",bg="#00FF00")
    PleaseWait.place(x=Win.winfo_width()//2-PleaseWait.winfo_reqwidth()//2,y=Win.winfo_height()//2-PleaseWait.winfo_reqwidth()//2)
    global Set
    if "IDidntWantToUseThisGlobal"in globals():del globals()["IDidntWantToUseThisGlobal"]
    Win.update()
    Set=ReadItem(M)
    del globals()["PleaseWait"]
    MainMenu()
def Move(Keep=False):
    for widget in Win.winfo_children():#Line imported from stackoverflow and adapted.
        (widget.place_forget if Keep else widget.destroy)()
Win.update()
PleaseWait=GUI.Label(Win,text="Reading data from \""+file+"\". Please wait.",bg="#00FF00")
PleaseWait.place(x=Win.winfo_width()//2-PleaseWait.winfo_reqwidth()//2,y=Win.winfo_height()//2-PleaseWait.winfo_reqwidth()//2)
Win.update()
try:
    Set=ReadItem(file)
    PleaseWait.destroy()
    MainMenu()
except FileNotFoundError as Error:
    if"PleaseWait"in globals():PleaseWait.destroy()
    SetupA(str(Error))
Win.mainloop()
