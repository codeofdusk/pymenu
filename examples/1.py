import pymenu
print("Please select your condition : ")
condition=pymenu.lettered("body aches","headaches","common cold","cough","other")
if ( condition == 5 ):
    print("be more descriptive!")
    print("enter one line of text : ")
    desc=input("go ahead : ")
level = pymenu.numbered("my condition is slight","my condition is mild","my condition is moderate","my condition is average","my condition is slightly above average","my condition is above average","my condition is significantly above average")

