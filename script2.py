def staircase(n,res=""):
    tab = ""
    if (n>0):
        for i in range(0, n):
            if i == n-1:
                char = ""
            else:
                char = "\n" 
            val = "_" *(n-i-1) + "#" *(i+1)+ char 
            tab = tab + val  
    elif (n<0):
        for i in range(0, -n):
            if i == -n-1:
                char = ""
            else:
                char = "\n" 
            val = "_" * (i) + "#" * (-n-i) + char
            tab = tab + val  
    return tab


print(staircase(3))