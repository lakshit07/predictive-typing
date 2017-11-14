def process(f, s):
    t = s.split()
    done = False
    for i in t:
        if i.isalpha():
            f.write(i.lower() + " ")
            done = True
    return done

def main():
    f = open("conversations.txt" , 'r')
    g = open("4", 'w')
    for line in f:
        s = line.split()
        t = ''.join(w + " " for w in s[9:])
        if process(g, t):
            g.write('\n')
              
            
if __name__ == "__main__":
    main()  
