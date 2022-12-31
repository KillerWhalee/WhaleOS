import os

def checkDuplicate(srclist, dup, errorLog):
    
    for src in srclist:
        for file in os.listdir(src):
            #for debugging
            #print(f"search {src}/{file}...")
            
            if os.path.isdir(f"{src}/{file}"):
                if "##" in file:
                    continue
                dup = checkDuplicate(f"{src}/{file}", dup, errorLog)
            
            name, ext = os.path.splitext(file)

            if "화2_" in name and ext in [".hwp", ".HWP"]:
                if file in dup:
                    errorLog.write(f"DUPLICATON for <{file}>\n")
                    errorLog.write(f"{dup[file]}\n")
                    errorLog.write(f"{src}/{file}\n\n")
                else:
                    dup[file] = f"{src}/{file}"
    
    return dup
