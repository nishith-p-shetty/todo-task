import sys

if(len(sys.argv) > 1):

    open("task.txt", "a")
    open("completed.txt", "a")
    
    if(sys.argv[1] == "add"):                                             #ADD
        tskf = open("task.txt", "r")
        tlno = 0
        for line in tskf:
            if line != "\n":
                tlno += 1                                                 #NUMBER OF LINES IN TASK.TXT
        tskf.close()
        try:
            prno = sys.argv[2]                                            #PRIORITY NUMBER FROM INPUT
            tsk = ((sys.argv[3])+"\n")                                    #TASK FROM INPUT
            fstr = (prno + " " + tsk)                                     #FINAL STRING TO BE ADDED
            if(tlno == 0):                       
                tskf = open("task.txt", "a")                       
                tskf.write(fstr)                                          #ADD THE TASK TO TASK.TXT
                tskf.close()
                print("Added task: \"", tsk.strip() , "\" with priority ", prno, end ="", sep="")
            elif(tlno > 0):
                tskf = open("task.txt", "r")
                lines = tskf.readlines()                                  #READ ALL LINES IN TASK.TXT
                tskf.close()
                tskf = open("task.txt", "r")
                for tmp in (tskf.readlines() [-1:]):
                    lstno = int(tmp[0:2])                                 #PRIORITY OF LAST LINE
                tskf.close()                 
                tskf = open("task.txt", "r")                 
                if(int(prno) > lstno):                 
                    lines.append(fstr)                                    #ADDING TASK TO LIST AT LAST WHEN GIVEN PRIORITY IS LARGER THAN END OF FILE
                for x in range(tlno):                 
                    index = int((tskf.readline()[0:2]))                 
                    if(int(prno) < index):                 
                        lines.insert(x, fstr)                             #ADDING TASK TO LIST WHEN GIVEN PRIORITY IS LESS THAN CURRENT LINE
                        break                                    
                    elif(int(prno) == index):                 
                        lines.insert(x+1, fstr)                           #ADDING TASK TO LIST WHEN GIVEN PRIORITY IS SAME AS CURRENT LINE
                        break
                tskf.close()
                tskf = open("task.txt", "w+")
                for line in lines:
                    tskf.write(line)                                      #OVERWRITE THE FILE AFTER ADDING COMPLETED TASK
                tskf.close()
                print("Added task: \"", tsk.strip() , "\" with priority ", prno, end ="", sep="")
        except:
            print("Error: Missing tasks string. Nothing added!")          #NOTHING ENTERED IN DOUBLE QUOTES

    elif(sys.argv[1] == "ls"):                                            #LIST
        tskf = open("task.txt", "r")
        tlno = 0
        for line in tskf:
            if line != "\n":
                tlno += 1                                                 #NUMBER OF LINES IN TASK.TXT
        tskf.close()
        if(tlno == 0):
            print("There are no pending tasks!")                          #NO TASK
        else:
            tskf = open("task.txt", "r")
            for x in range(tlno):
                tkstr = tskf.readline()                                   #READING A SINGLE LINE
                pri = int(tkstr[0:2])                                     #PRIORITY NUMBER OF THIS LINE
                tkstr = tkstr[2:(len(tkstr))].strip()                     #REMOVING PRIORITY AND SPACES
                stri = (str(x+1) + ". " + tkstr + " [" + str(pri) + "]\n")
                sys.stdout.buffer.write((stri).encode('utf8'))
            tskf.close()
    
    elif(sys.argv[1] == "del"):                                           #DELETE
        try:
            index = int(sys.argv[2])                                      #INDEX OR LINE NUMBER
            tskf = open("task.txt", "r")
            tlno = 0
            for line in tskf:
                if line != "\n":
                    tlno += 1                                             #NUMBER OF LINES IN TASK.TXT
            tskf.close()
            if(tlno <=  0):
                print("Error: task with index #", index, " does not exist. Nothing deleted.", end ="", sep="")
            elif(index > 0):
                if(index <= tlno):                                        #IF INDEX NUMBER IS WITHIN NUMBER OF LINES
                    dell = open("task.txt", "r")
                    lines = dell.readlines()                              #READ ALL LINES IN TASK.TXT
                    dell.close()                   
                    del lines[index-1]                                    #DELETE THE INDEX'ED LINE
                    dell = open("task.txt", "w+")                   
                    for line in lines:                   
                        dell.write(line)                                  #OVERWRITE THE FILE AFTER DELETING
                    dell.close()
                    print("Deleted task #",index, end ="", sep="")
                else:                                                     #ERROR LINE NUMBER DOES NOT EXIST
                    print("Error: task with index #", index, " does not exist. Nothing deleted.", end ="", sep="")
            else:
                print("Error: task with index #", index, " does not exist. Nothing deleted.", end ="", sep="")
        except:
            print("Error: Missing NUMBER for deleting tasks.")

    elif(sys.argv[1] == "done"):                                          #DONE
        try:
            if(int(sys.argv[2]) == 0):
                print("Error: no incomplete item with index #", int(sys.argv[2]), " exists.", end ="", sep="")
            else:
                index = int(sys.argv[2])                                  #INDEX OR LINE NUMBER
                tskf = open("task.txt", "r")                   
                tlno = 0                   
                for line in tskf:                   
                    if line != "\n":                   
                        tlno += 1                                         #NUMBER OF LINES IN TASK.TXT
                tskf.close()                   
                if(index <= tlno):                                        #IF INDEX NUMBER IS WITHIN NUMBER OF LINES
                   dell = open("task.txt", "r")                   
                   lines = dell.readlines()                               #READ ALL LINES IN TASK.TXT
                   dell.close()                   
                   compln = lines[index-1]                                #LINE SHOULD BE ADDED TO COMPLTED.TXT
                   del lines[index-1]                                     #DELETE THE INDEX'ED LINE
                   dell = open("task.txt", "w+")                   
                   for line in lines:                   
                       dell.write(line)                                   #OVERWRITE THE FILE AFTER DELETING
                   dell.close()                   
                   compll = open("completed.txt", "r")                   
                   lines = compll.readlines()                             #READ ALL LINES IN COMPLETED.TXT
                   compll.close()                   
                   compln = compln[2:].lstrip()                           #REMOVING PRIROITY AND LEFT SPACE
                   lines.append(compln)                                #ADDING COMPLETED TASK TO LIST
                   print(lines)                   
                   compll = open("completed.txt", "w+")                   
                   for line in lines:                   
                       compll.write(line)                                 #OVERWRITE THE FILE AFTER ADDING COMPLETED TASK
                   compll.close()
                   print("Marked item as done.", end ="", sep="")
                else:                                                     #ERROR LINE NUMBER DOES NOT EXIST
                    print("Error: no incomplete item with index  ", index, " exists.", end ="", sep="")
        except:
            print("Error: Missing NUMBER for marking tasks as done.")
    
    elif(sys.argv[1] == "help"):                                          #HELP
        sys.stdout.buffer.write(("Usage :-\n").encode('utf8'))
        sys.stdout.buffer.write(("$ ./task add 2 hello world    # Add a new item with priority 2 and text \"hello world\" to the list\n").encode('utf8'))
        sys.stdout.buffer.write(("$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order\n").encode('utf8'))
        sys.stdout.buffer.write(("$ ./task del INDEX            # Delete the incomplete item with the given index\n").encode('utf8'))
        sys.stdout.buffer.write(("$ ./task done INDEX           # Mark the incomplete item with the given index as complete\n").encode('utf8'))
        sys.stdout.buffer.write(("$ ./task help                 # Show usage\n").encode('utf8'))
        sys.stdout.buffer.write(("$ ./task report               # Statistics\n").encode('utf8'))
    
    elif(sys.argv[1] == "report"):                                        #REPORT
        tskf = open("task.txt", "r")
        tlno = 0
        for line in tskf:
            if line != "\n":
                tlno += 1                                                 #NUMBER OF LINES IN TASK.TXT
        tskf.close()

        comf = open("completed.txt", "r")
        clno = 0
        for line in comf:
            if line != "\n":
                clno += 1                                                 #NUMBER OF LINES IN COMPLETED.TXT
        comf.close()
        stri = ("Pending : " + str(tlno) + "\n") 
        sys.stdout.buffer.write((stri).encode('utf8'))
        tskf = open("task.txt", "r")
        for x in range(tlno):
            tkstr = tskf.readline()                                       #READING A SINGLE LINE
            pri = int(tkstr[0:2])                                         #PRIORITY NUMBER OF THIS LINE
            tkstr = tkstr[2:(len(tkstr))].strip()                         #REMOVING PRIORITY AND SPACES
            stri = (str(x+1) + ". " + tkstr + " [" + str(pri) + "]\n")
            sys.stdout.buffer.write((stri).encode('utf8'))
        tskf.close()
        comf = open("completed.txt", "r")
        stri = ("\nCompleted : " + (str(clno).strip()) + "\n")
        sys.stdout.buffer.write((stri).encode('utf8'))
        for x in range(clno):
            compstr = comf.readline()                                     #READING A SINGLE LINE
            compstr = compstr.strip()                                     #REMOVING SPACES
            stri = (str(x+1) +". " + (compstr.strip()) + "\n")
            sys.stdout.buffer.write((stri).encode('utf8'))
        comf.close()

    else:                                                                 #DEFAULT HELP
        sys.stdout.buffer.write(("Usage :-\n").encode('utf8'))
        sys.stdout.buffer.write(("$ ./task add 2 hello world    # Add a new item with priority 2 and text \"hello world\" to the list\n").encode('utf8'))
        sys.stdout.buffer.write(("$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order\n").encode('utf8'))
        sys.stdout.buffer.write(("$ ./task del INDEX            # Delete the incomplete item with the given index\n").encode('utf8'))
        sys.stdout.buffer.write(("$ ./task done INDEX           # Mark the incomplete item with the given index as complete\n").encode('utf8'))
        sys.stdout.buffer.write(("$ ./task help                 # Show usage\n").encode('utf8'))
        sys.stdout.buffer.write(("$ ./task report               # Statistics\n").encode('utf8'))

else:                                                                     #DEFAULT
    sys.stdout.buffer.write(("Usage :-\n").encode('utf8'))
    sys.stdout.buffer.write(("$ ./task add 2 hello world    # Add a new item with priority 2 and text \"hello world\" to the list\n").encode('utf8'))
    sys.stdout.buffer.write(("$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order\n").encode('utf8'))
    sys.stdout.buffer.write(("$ ./task del INDEX            # Delete the incomplete item with the given index\n").encode('utf8'))
    sys.stdout.buffer.write(("$ ./task done INDEX           # Mark the incomplete item with the given index as complete\n").encode('utf8'))
    sys.stdout.buffer.write(("$ ./task help                 # Show usage\n").encode('utf8'))
    sys.stdout.buffer.write(("$ ./task report               # Statistics\n").encode('utf8'))