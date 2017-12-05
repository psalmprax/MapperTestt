# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 00:32:44 2017

@author: User
"""
import os



def read(file,data1,data2,addition,check,keys,values):
    for columns1 in ( raw1.strip().split() for raw1 in file ):  
        key_in , value_in = columns1[0].split(",")
        addition(key_in,value_in,data1,data2,check,keys,values)


def addition(key,val,dicts,dicts2,check,keys,values):
    if not val.isdigit():
        dicts2[key] = val
        keys.append(key)
        values.append(val)
       
    else:
        if check(key,dicts) == 1:
           dicts[key] += int(val)
        else:
           dicts[key] = int(val)
           

def check(keys, dicts):
    counter = 0
    for key , value in dicts.items():
        if keys == key:
            counter = 1
            return counter
            break
    return counter    

def tempWriteFile(folderName, fileName, keys, values, dirCreate, dicts):
    dest_Folder = dirCreate(folderName)
    
    out  = open(dest_Folder + fileName, 'a+')
    for key2 , value2 in zip(keys,values):
        if value2 == "CNO":
            for key1 , value1 in dicts.items():
                if key2 == key1:
                    out.write('%s,%s\n' % (key2,value1))
    return out

def dirCreate(newFoldername):
    """Creating a new Folder in the Current Directory"""
    current_directory = os.getcwd()
    new_directory = os.path.join(current_directory,newFoldername)
    
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)
    return new_directory

def getCreate(newFoldername):
    """Creating a new Folder in the Current Directory"""
    current_directory = os.getcwd()
    new_directory = os.path.join(current_directory,newFoldername)
    
    if os.path.exists(new_directory):
        return new_directory


def readnoduplicate(obj,nodup):
    for columns1 in ( raw1.strip().split() for raw1 in obj ):
        key_in , value_in = columns1[0].split(",")
        if check(key_in,nodup) != 1:
            nodup[key_in] = value_in
            print(key_in, nodup[key_in])

def writenoduplicate(obj,dicts):
    for key , value in dicts.items():  
        #print(key, "--------", value)
        obj.write( '%s\t%s\n' % (key, value) )

def main():
    keys = []
    values = []

    dicts = {}
    dicts2 = {}
    nodup ={}
    nodup_copy = {}
    
    for f in os.listdir('.'):
        
        if f.endswith('.txt'):
            crs1 = open(f, "r")
            read(crs1,dicts,dicts2,addition,check,keys,values)
    
    
    dest_Folder = "Result_Folder"
    fileName = "\\testfile3.txt"
    fileName2 = "\\testfile4.txt"
    out  = tempWriteFile(dest_Folder, fileName, keys, values, dirCreate, dicts)
    
    #print(out)
    nodup_copy = nodup
    lines2 = open(dirCreate(dest_Folder)+fileName2, 'w')
    lines = open(getCreate(dest_Folder)+fileName, 'r+')
    readnoduplicate(lines,nodup)
    writenoduplicate(lines2,nodup_copy)



if __name__ == "__main__":
    main()