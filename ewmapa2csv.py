import csv
import Tkinter, Tkconstants, tkFileDialog
from Tkinter import *


root = Tk()
root.baselink = tkFileDialog.askopenfilename(initialdir = "/",title = "Select ewmapa TXT",filetypes = (("all files","*.*"),))
root.csvlink = tkFileDialog.asksaveasfilename(initialdir = "/",title = "Select CSV name",defaultextension = ".csv",filetypes = (('Comma Separated values', '*.csv'),))
print root.baselink

txt=open(root.baselink,"r")
csvfile=open (root.csvlink,'w')
fieldnames=['wkt','id','operat','typlinii','tekst','datamod','usermod','datautw','userutw',"warstwa"]
spamwriter = csv.DictWriter(csvfile,fieldnames=fieldnames)
spamwriter.writeheader()
n=-1
 
for line in txt:
    if "**" in line:
        try:
            warstwa=txt.next()
            print(warstwa)
        except:
            pass
    elif "   20  5.9" in line:
        n+=1
        splted=line.split()
        wsp1=str([splted[3],splted[2]])
        wsp2=str([splted[5],splted[4]])
        wkt=str(wsp1).strip("[',',']")
        wkt=wkt.replace("', '"," ")
        wkt2=str(wsp2).strip("[',',']")
        wkt2=wkt2.replace("', '"," ")
        wktjoin=str("LINESTRING ("+wkt+","+wkt2+")")
        datamod=str(splted[9:11]).replace('"',"")
        datamod=datamod.strip("[',',']")
        datautw=str(splted[12:14]).replace('"',"")
        datautw=datautw.strip("[',',']")
        podwarstwa=warstwa[:-1]+"#"+str(splted[0])
        spamwriter.writerow({"wkt":wktjoin,"id":str(n),"typlinii":splted[6],"tekst":splted[7],"operat":splted[8],"datamod":datamod,"usermod":splted[11],"datautw":datautw,"userutw":splted[14],"warstwa":podwarstwa})
        print(splted)
csvfile.close()