#Zahran Yahia Khan
#U63179657
#This program encrypts a text file.

Encrypt_Code = {'A':')','a':'0','B':'(','b':'9','C':'*','c':'8',
 'D':'&','d':'7','E':'^','e':'6','F':'%','f':'5',
 'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2',
 'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y',
 'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v',
 'P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s',
 'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p',
 'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m',
 'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j',
 '@':'I','2':'i','#':'H','3':'h','$':'G','4':'g',
 '%':'F','5':'f','^':'E','6':'e','&':'D','7':'d',
 '*':'C','8':'c','(':'B','9':'b',')':'A','0':'a',
 ':':',',',':':','?':'.','.':'?','<':'>','>':'<',
 "'":'"','"':"'",'+':'-','-':'+','=':';',';':'=',
 '{':'[','[':'{','}':']',']':'}'}

Input_File_Name = input("What is the input file name?(text files are preferred): " )
inputfile = open(Input_File_Name, 'r') #r - read mode
input1 = inputfile.read() #read the text content and return as a string

Output_File_Name = input("What is the output file name?(text files are preferred): " )
outputfile = open(Output_File_Name, 'w') #w - write mode


def encrypt(file_contents): #file_contents to be a string
    for a in file_contents:
        if (a.isspace()) == True:
            outputfile.write(" ")

        else:
            b = Encrypt_Code.get(a)
            outputfile.write(b)

#call
encrypt(input1)


