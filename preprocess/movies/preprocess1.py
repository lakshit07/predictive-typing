def process(f, s):
    t = s.split()
    done = False
    for i in t:
        if i.isalpha():
            f.write(i.lower() + " ")
            done = True
    return done

def main():
    f = open("quote" , 'r')
    g = open("2", 'w')
    i = 1
    for line in f:
        if i%4 == 0:
            if process(g, line):
                g.write('\n')
        i += 1        
            
if __name__ == "__main__":
    main()  
