w1 = "buy now"
w2 = "try it"
w3 = "subscibe now"
w4= "best"
a = input("enter your comment: ")
if(w1 in a or w2 in a or w3 in a or w4 in a):
    print("spam detected")
else:
    print(a)
