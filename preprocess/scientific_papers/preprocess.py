import csv

def process(f, s):
    t = s.split()
    done = False
    for i in t:
        if i.isalpha():
            f.write(i + " ")
            done = True
    return done        

def main():
    reader = csv.reader(open('sentences.csv'))
    f = open("1", "w")
    for r in reader:
        if r[2] is not None:
            if(process(f, r[2])):
                f.write('\n')
            
if __name__ == "__main__":
    main()  
