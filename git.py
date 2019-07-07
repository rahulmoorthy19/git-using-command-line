import sys
import os
import os.path
def validate(filename):
    '''
    This function validates the rules defined for the document
    1.Maximum 20 lines
    2.Each line has maximum of 10 charecters
    '''
    line_count=0
    char_count=0
    with open(filename) as f:
        for line in f:
            char_count=0
            if(not line_count==0):
                char_count=char_count+1
            line_count=line_count+1
            for i in line.split(" "):
                char_count=char_count+len(list(i))
            char_count=char_count+((len(line.split(" ")))-1)
            if(char_count>10):
                return False
    if(line_count>20):
        return False
    return True

def num_operations(filename):
    '''
    This function calculates the total number of operations performed
    Validation for multiple operations performed at a single time.
    Eg-Append and Modify cannot be performed together as only one operation can be performed at a time
    '''
    append_operations=0
    delete_operations=0
    modify_operations=0
    version_find=list()
    version_number=list()
    for files in os.listdir(os.getcwd()):
        if files.endswith(".txt"):
            version_find.append(files)
    for i in version_find:
        if(len(i.split(".")[0].split("_"))==2 and i.find(filename.split(".")[0])!=-1):
            version_number.append(int(i.split(".")[0].split("_")[1]))
    version_number.sort()
    version=version_number[-1]
    filename2=filename
    filename1=filename.split(".")[0]+"_"+str(version)+"."+filename.split(".")[1]
    linecount1=0
    linecount2=0
    f1=open(filename1)
    file1=f1.readlines()
    f1.close()
    f2=open(filename2)
    file2=f2.readlines()
    f2.close()
    #If size of list 1 is greater than size of list 2
    if(len(file1)>len(file2)):
        cnt=len(file1)
        lastindx=0
        indx=0
        for line1 in file1:
            flag=0
            for line2 in file2:
                if(line2==line1):
                    lastindx=file2.index(line2)
                    flag=1
                    break
            if(flag==0):
                delete_operations=1

    # if file2 size is greater or equal
    elif(len(file2)>=len(file1)):
        cnt=len(file2)
        lastindx=0
        for line1,line2 in zip(file1,file2):
            if(not line2==line1):   #Change or modification step
                #line number of file 1 "c" line number of file 2
                modify_operations=1
                # "<" represents the first file and ">" represents of file 2
            lastindx=file2.index(line2)
            cnt=cnt-1

        if(cnt>0): # Appending the elements in file
            while(cnt>0):
                for i in range(lastindx+1,len(file2)):
                    append_operations=1
                    cnt=cnt-1
    return append_operations+delete_operations+modify_operations


def commit(filename):
    '''
    This function is used for performing the "python git.py hello.txt" statement
    Commiting or saving the version of the file
    '''
    validation=validate(filename)
    if(validation==False):
        print("File Not according to Rules Defined")
    else:
        if(os.path.exists(filename.split(".")[0]+"_"+"0"+"."+filename.split(".")[1])):
            operations=num_operations(filename)
            version_find=list()
            version_number=list()
            if(operations==1):
                for files in os.listdir(os.getcwd()):
                    if files.endswith(".txt"):
                        version_find.append(files)
                for i in version_find:
                    if(len(i.split(".")[0].split("_"))==2 and i.find(filename.split(".")[0])!=-1):
                        version_number.append(int(i.split(".")[0].split("_")[1]))
                version=max(version_number)
                file=filename.split(".")[0]+"_"+str(version+1)+"."+filename.split(".")[1]
                with open(filename) as f:
                    with open(file, "w") as f1:
                        for line in f:
                            f1.write(line)
            elif operations==0:
                print("No changes found!!!")
            else:
                print("More than one operation performed!!!!Not possible to commit")
        else:
            file=filename.split(".")[0]+"_"+"0"+"."+filename.split(".")[1]
            with open(filename) as f:
                with open(file, "w") as f1:
                    for line in f:
                        f1.write(line)


def display(filename,version):
    '''
    This is used for executing the function "python git.py hello.txt version_no"
    which is basically displaying any version of file
    '''
    if(os.path.exists(filename.split(".")[0]+"_"+str(version)+"."+filename.split(".")[1])):
        file=filename.split(".")[0]+"_"+str(version)+"."+filename.split(".")[1]
        file_reading = open(file, "r")
        print(file_reading.read())
    else:
        print("such version does not exist!!!!")


def difference(filename):
    '''
    This function is used for executing the command "python git.py diff hello.txt"
    which is basically finding difference between version N and version N-1
    '''
    version_find=list()
    version_number=list()
    for files in os.listdir(os.getcwd()):
        if files.endswith(".txt"):
            version_find.append(files)
    for i in version_find:
        if(len(i.split(".")[0].split("_"))==2 and i.find(filename.split(".")[0])!=-1):
            version_number.append(int(i.split(".")[0].split("_")[1]))
    if(len(version_number)>=2):
        version_number.sort()
        version=version_number[-1]
        version_1=version_number[-2]
        filename2=filename.split(".")[0]+"_"+str(version)+"."+filename.split(".")[1]
        filename1=filename.split(".")[0]+"_"+str(version_1)+"."+filename.split(".")[1]
        linecount1=0
        linecount2=0
        f1=open(filename1)
        file1=f1.readlines()
        f1.close()
        f2=open(filename2)
        file2=f2.readlines()
        f2.close()
        #If size of list 1 is greater than size of list 2
        if(len(file1)>len(file2)):
            cnt=len(file1)
            lastindx=0
            indx=0
            for line1 in file1:
                flag=0
                for line2 in file2:
                    if(line2==line1):
                        lastindx=file2.index(line2)
                        flag=1
                        break
                if(flag==0):
                    print(str(file1.index(line1)+1)+"d"+str(lastindx+1))
                    print("< "+line1)

    # if file2 size is greater or equal
        elif(len(file2)>=len(file1)):
            cnt=len(file2)
            lastindx=0
            for line1,line2 in zip(file1,file2):
                if(not line2==line1):   #Change or modification step
                    #line number of file 1 "c" line number of file 2
                    print(str(file1.index(line1)+1)+"c"+str(file2.index(line2)+1))
                    # "<" represents the first file and ">" represents of file 2
                    print("< "+line1)
                    print("---")
                    print("> "+line2)
                lastindx=file2.index(line2)
                cnt=cnt-1

            if(cnt>0): # Appending the elements in file
                while(cnt>0):
                    for i in range(lastindx+1,len(file2)):
                        print(str(len(file1)-1)+"a"+str(i))
                        print("> "+file2[i])
                        cnt=cnt-1
    else:
        print("No commit done so no difference found")
if __name__ == '__main__':
    if(len(sys.argv)==3 and sys.argv[1]!="diff"): ##python git.py text_file_name.txt version_no
        filename=sys.argv[1]
        version=int(sys.argv[2])
        display(filename,version)
    if(len(sys.argv)==2):                         ##python git.py text_file_name.txt
        filename=str(sys.argv[1])
        commit(filename)
    if(len(sys.argv)==3 and sys.argv[1]=="diff"):##python git.py diff text_file_name.txt
        filename=str(sys.argv[2])
        difference(filename)
