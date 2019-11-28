
import os,json
from jsons2json.merger import json_merger
def file_write(user_input,base_name):
    write_into_file=json_merger.merger(user_input,base_name)
    with open(out_fname+'.json', 'w') as outfile:
        json.dump(write_into_file, outfile)

def check_size(out_fname,extension,size_limit):
        
    file_size=os.stat(out_fname+'.json').st_size
    if file_size>(size_limit*(10**(3*(extension-1)))):
        check=input("Output file exceeds the limit.. \n Wanna still keep (y/n)?")
        
        if check.lower() == 'n':
            print("removing.....")
            os.remove(os.getcwd()+"/"+out_fname+".json")
        
if __name__ == "__main__":
        
    user_input=input("enter the folder location : EX: <directory>:/<folder name>/<sub folder name> ")
    base_name=input("enter the base name : ")
    out_fname=input("Enter the merged file name w/o extension ")
    extension=int(input("File size in \n1.bytes \n2.Kb \n3.Mb \n==> "))
    size_limit=int(input("Enter the file size"))
    assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)
    
    file_write(user_input,base_name)
    check_size(out_fname,extension,size_limit)