#Copyright 2013 Bill Dengler
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#http://www.apache.org/licenses/LICENSE-2.0
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or #implied.
#See the License for the specific language governing permissions and
#limitations under the License.

#python menu functions
def numbered(*arg):
    count=0
    #display choices
    for a in arg:
        count = count + 1
        #we have a zeroedcount variable because lists start at 0, not 1.
        zeroedcount=count-1
        print(count," : ",arg[zeroedcount] )
    #prompt
    num = input("enter your selection followed by enter : ")
    return num
def lettered(*arg):
    icount=0
    #return if we have more than 26 options, because we only have 26 letters in the alphabet
    if (len(arg) > 26 ):
        print("error : lettered menu can have a maximum of 26 items")
        return 0
    letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    count=0
    #display options

    for a in arg:
        count=count+1
        #we have a zeroedcount variable because lists start at 0, not 1.
        zeroedcount=count-1
        print(letters[zeroedcount]," : ",arg[zeroedcount])
    #prompt
    opt = input("enter your selection followed by enter : ")
    #translate our letter into a number that we return
    for l in letters:
        icount = icount + 1
        if (l == opt):
                return icount

