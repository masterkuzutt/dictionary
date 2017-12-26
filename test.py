def main():
    input_lines = input()
    n,k,m = input_lines.split(" ")
   
    nl = []

    for i in range(int(n)):
        nl.append(i)

    kl = []
    for i in range(int(k)):
        kl.append(input().rstrip())
    
    pc = 0
    wcl = []
    lst = ""

    for i in range(int(m)):
        w = input().rstrip()
        if pc >= len(nl):
            pc = 0 
        if w.endswith("z") or w not in kl or w in wcl :
            nl.pop(pc)
            lst = ""
        
        elif i != 0 and lst != "" and  w.startswith(lst) == False:
            nl.pop(pc)
            lst = ""
        
        else:
            wcl.append(w)
            pc =  pc + 1
        
            
    print(len(nl))
    for i in nl:
        print(i + 1)

if __name__ == '__main__':
    main()