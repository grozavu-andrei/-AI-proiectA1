import os
def separare_chei(text_citit,folder_produs):
    file1 = open(text_citit,"r",encoding='utf-8')

    target=os.path.basename(os.path.normpath(text_citit)).replace("text","")

    file2= open(folder_produs+target+".txt","w",encoding='utf-8')

    text_1 = file1.read()

    text_1 = text_1.replace('\n'," ")
    text_1 = " ".join(text_1.split())
    text_1 = text_1.replace("|","l")
    text_list=list(text_1)

    for i in range(len(text_list)):
        if (ord(text_list[i])>=65 and ord(text_list[i])<=90) or text_list[i]=="Ş" or text_list[i]=="Ț" or text_list[i]=="Î":
            text_list[i]='\n'+text_list[i]
        elif text_list[i] in "!@#$%^&*()_+-={};:\'.,?/[]„\"":
            text_list[i]=""

    text_1 = "".join(text_list)

    file2.write(text_1)

    file1.close()
    file2.close()