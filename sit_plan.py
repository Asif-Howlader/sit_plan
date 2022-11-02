from email.encoders import encode_base64
from encodings.utf_8 import encode
from tkinter import UNDERLINE
import PyPDF2
from fpdf import FPDF


#blank list for room capacity
room_capacity =[]
#assigning room on index

def assigning_index(room_capacity,list_of_index):
    li=[]
    #pdf file generator
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('helvetica', size = 12)
    for room_ in range(len(room_capacity)):
        print(f"room number:{room_+1}")
        r=room_capacity[room_]
        v=0        
        for sits in range(r): 
            li.append(list_of_index[v])
            print(list_of_index.pop(v),',',end='')       
        # pdf.cell(200,20,txt = f"room number:{room_+1}", ln=1, align='C')
        pdf.cell(txt = f"room number:{room_+1}")
        pdf.ln(10)
        if len(li)>15:
            for sl in range(len(li)):
                la=str(li[sl])
                pdf.cell(txt=la)
                if sl>0:
                    if sl%15==0:
                        pdf.ln(10)
                    else:
                        pass
                else:
                    pass
        else:
            for qs in range(len(li)):
                la=str(li[qs])
                pdf.cell(txt=la)
        print()
        pdf.ln(20)
        li=[]
   
    
    pdf.output("C://Users/ASIF HOWLADER/Desktop/scripts/final_sit_plan.pdf") 
if __name__=="__main__":
    #availabe rooms 
    room_no=int(input("Please input how many rooms are availabe there:"))

    #room capacity 
    for i in range (0,room_no):
        room=int(input(f"Please input total sit no for room no {i+1}:"))
        room_capacity.append(room)

    my_file = open("C://Users/ASIF HOWLADER/Desktop/scripts/index_no.txt", "r")
    data = my_file.read()
    all_index_no=list(data.split('\n'))
    l=list(map(int,all_index_no))
    l.sort()
    assigning_index(room_capacity,l)
