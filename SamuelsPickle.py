from math import ceil
class UseError(ValueError):"Raised if Get object has/is-given an inapproriate value for \"Use\"."
class UseWarning(Warning):"Raised if a function is not compatible with the value of \"Use\"."
class ReadingError(FileNotFoundError):"Raised if there was an error reading the file."
def byte(Str):
    Bytes=b""
    Mult=128
    for i in Str:
	    if Mult==128:Bytes+=b"\x00"
	    if i==("1"if isinstance(i,str)else True):Bytes=Bytes[:-1]+bytes((Bytes[-1]+Mult,))
	    Mult=Mult//2
	    if Mult==0:Mult=128
    return Bytes
def byteSplit(Bytes,*Bools):
    Bytes=bytes(Bytes)
    if Bytes==b"":raise ValueError("Expected bytes not found.")
    if Bools==(None,):Bools=(False,)*len(Bytes)*8
    elif len(Bools)!=len(Bytes)*8 or False in(isinstance(i,bool)or i==None for i in Bools):Bools=None
    outBools=tuple()
    for i in Bytes:
        N=i
        cuBools=tuple()
        for j in range(8):cuBools,N=(bool(N%2),)+cuBools,N//2
        outBools+=cuBools
    if Bools!=None:
        cuBools=tuple()
        Number=0
        Previous=True
        for i in range(len(Bools)):
            if Bools[i]:
                if not Previous:
                    cuBools+=(Number,)
                    Number=0
                    Previous=True
                cuBools+=(outBools[i],)
            else:
                if Bools[i]==None:
                    cuBools+=(Number,)
                    Number=0
                Number=Number*2+int(outBools[i])
                Previous=False
        if not Previous:
            cuBools+=(Number,)
        return cuBools if True in Bools else Number
    return outBools
def ID(Input,Set="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    if isinstance(Input,int):
        ret=type(Set)()
        Inp=Input
        while Inp>0:
            try:ret=type(Set)(Set[(Inp%len(Set))-1])+ret
            except TypeError:ret=type(Set)((Set[(Inp%len(Set))-1],))+ret
            Inp=Inp/len(Set)-1
            Inp=ceil(Inp)
        return ret
    else:
        Number=0
        for i in Input:
            Number=Number*len(Set)
            Number+=Set.index(i)+1
        return Number
class Get():
    "Gets the binary file you want to use.\n\
Loc: The adress of the file.\nUse=0: What is to be done with the file.\n\
(0=Open later. 1=Open now for writing.\n2=Open now for reading. 3=Open now for appending.)"
    def __init__(self,Loc,Use=0):
        "Gets the binary file you want to use.\n\
Loc: The adress of the file.\nUse=0: What is to be done with the file.\
(0=Open later. 1=Open now for writing. 2=Open now for reading.  3=Open now for appending.)"
        if Use not in[0,1,2,3]:raise UseError("0, 1, 2, or 3 expected. "+str(Use)+" was given.")
        if  Use==0:self.__Loc=Loc
        else:
            self.__pointer=0
            self.__File=open(Loc,"wb"if Use==1 else("rb"if Use==2 else"ab"))
            self.__rePointer={}
        self.__Use=Use
        self.__End=False
    def Read(self,*Count):
        "Reads the contents of the file.\
 Will read the whole thing if Use=0.\n\
 Count, ...,: Bytes to read at once.\n\
 Read(2,3,1) will obtain a 16 bit int from the next/first 2 bytes,\n\
 a 24 bit int from the next 3 bytes, and an 8 bit int from the next byte.\n\
 Two's complement is not used."
        Count=list(Count)
        self.__End=False
        if len(Count)==0:Count=[1]
        if 1 in (i<=0 for i in Count):raise ValueError("Was not expecting value 0 or lower.")
        if self.__Use==0:File=open(self.__Loc,"rb")
        else:File=self.__File
        intArray=[]
        for i in File.read():intArray.append(i)
        File.seek(0)
        if self.__Use==0:
            Count+=[1]*(len(intArray)-sum(Count))
            File.close()
        Array=[]
        L=1
        count=Count[0]
        Cpos=0
        for i in range(0 if self.__Use==0 else self.__pointer,len(intArray) if self.__Use==0 else self.__pointer+sum(Count)):
            if L==1:
                try:Array.append(intArray[i])
                except IndexError:raise ReadingError("There was an error reading the file.")
                count-=1
                if count==0:
                    Cpos+=1
                    if Cpos<len(Count):count=Count[Cpos]
                else:L=0
            else:
                Array[len(Array)-1]=Array[len(Array)-1]*256+intArray[i]
                count-=1
                if count==0:
                    Cpos+=1
                    if Cpos<len(Count):count=Count[Cpos]
                    L=1
            if self.__Use!=0:
                self.__pointer+=1
#                print(self.__pointer)
                if self.__pointer==len(File.read()):
                    File.seek(0)
                    self.__End=True
                    self.__pointer=0
                    break
#                print(self.__pointer,end="\n\n")
                File.seek(0)
        try:Array=bytes(Array)
        except ValueError:pass
        try:return(Array if len(Array)>1 or len(Count)>1 or self.__Use==0 else Array[0])
        except IndexError:return 0
    def Bookmark(Self,ID=None):
        "Stores the current position within a file.\nWhen the function is called with the same argument; it will return to that position.\nOnly for when Use=2."
        if Self.__Use!=2:raise UseError("Can only use bookmarks when Use=2.")
        if ID in Self.__rePointer:
            Self.__pointer=Self.__rePointer[ID]
            self.__End=False
        elif not Self.__End:Self.__rePointer[ID]=Self.__pointer
    def EoF(self):
        "Returnes true if the end of file was reached. Does not work if Use=0"
        if self.__Use in[0,1,3]:raise UseWarning("Cannot use EoF() properly if Use=0, 1 or 3.")
        return self.__End
    def Close(self):
        "Closes an open file. Does not work if Use=0"
        if self.__Use==0:raise UseWarning("Trying to close file that closes automaticaly.")
        else:self.__File.close()
    def Transfer(Self,Mode=None):
        if Self.__Use==0:
            Return=open(Self.__Loc,(("w"if Mode==1 else("r"if Mode==2 else"a"))if isinstance(Mode,int)else str(Mode))+"b")
            del Self
            return Return
        else:
            if Self.__Use==2:
#                print(Self.__pointer)
                Self.__File.seek(Self.__pointer)
            Return=Self.__File
            del Self
            return Return
    def Write(self,*INTarray,Min=1,Overwrite=False,Position=-1):
        "Writes to a binary file.\n\
INTarray, ...,: Numbers to write.\n\
Min=1: Minimum number of bytes to use per number.\n\
Overwrite=False: Wether bytes shall be overwritten.\n\
Only relevent if Use=0 and Position!=-1.\n\
Position=-1: The position in the file to start writing to from.\n\
Only relevent if Use=0."
        if self.__Use==2:raise UseError("Cannot write to a file that was opened for reading.")
        if type(INTarray[0]) in (bytes,bytearray,list,tuple):INTarray=INTarray[0]
        INTarray=list(INTarray)
        Array=[]
        for i in INTarray:
            MINarray=[i]
            while len(MINarray)<Min or 1 in(j>255 for j in MINarray):
                if MINarray[0]>255:MINarray=[MINarray[0]//256]+[MINarray[0]%256]+(MINarray[1:]if len(MINarray)>1 else [])
                else:MINarray=[0]+MINarray
            Array+=MINarray
        if self.__Use==0:
            try:
                File=open(self.__Loc,"rb")
                MINarray=File.read()
                File.close()
                File=open(self.__Loc,"wb")
                File.write((MINarray[:Position+(1 if Position<0 else 0)]if Position!=-1 else MINarray)+bytes(Array)+(MINarray[Position+(1 if Position<0 else 0)+(len(Array)if Overwrite else 0):]if Position+(len(Array)if Overwrite else 0)<(-1 if Position<0 else len(MINarray)) else b""))
            except FileNotFoundError:
                File=open(self.__Loc,"wb")
                File.write(bytes(Array))
            except IndexError:File.write(bytes(Array))
            File.close()
        else:self.__File.write(bytes(Array))
    def ReWrite(Self):
        "Deletes the contents of the file."
        if Self.__Use!=0:raise UseWarning("Can only rewrite if Use=0.")
        else:open(Self.__Loc,"wb").close()
