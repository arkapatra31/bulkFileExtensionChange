import os

#Scanning for files
print("###Processing files and subdirectories###")
contents = os.listdir(os.curdir)


def convertFileExtension (dir):
    tsExt = ".ts"
    jsExt = ".js"

    lc = os.listdir(dir)
    dirs = []
    if len(lc)>1:
         for each in lc :
            #check file
            if os.path.isfile(each):
                if jsExt in each:
                    newfile = each.replace(jsExt,tsExt)
                    os.rename(each,newfile)
            
            #Check dir
            elif os.path.isdir(each):
                dirs.append(os.getcwd()+'/'+each)

    elif len(lc) == 1:
        if os.path.isfile(lc[0]):
            lc = lc[0]
            if jsExt in lc:
                newfile = lc.replace(jsExt,tsExt)
                os.rename(lc,newfile)
        elif os.path.isdir(lc):
            dirs.append(os.getcwd()+'/'+lc)

    if len(dirs)==0:
        print("Directory processing complete or empty directory")

    elif len(dirs)==1 :
        os.chdir(dirs[0])
        print("Moving into Directory --->" + dirs[0])
        convertFileExtension(dirs[0])
        print("Moving out of Directory --->" + dirs[0])

    else:
        for everyDir in dirs:
            os.chdir(everyDir)
            print("Moving into Directory --->" + everyDir)
            convertFileExtension(everyDir)
            print("Moving out of Directory --->" + everyDir)

#Invoking conversion function
convertFileExtension(os.getcwd())



    

