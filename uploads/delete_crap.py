import time, csv, sys, os

def main():
    print 'starting..'
    f = open(sys.argv[1], 'rt')
    list = []
    try:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            list.append(row[0])
    finally:
        f.close()
        deleteImages(list)
        print 'completed..'

def deleteImages(list):
    for root, dirs, files in os.walk(sys.argv[2]):      
        for file in files:
            path = os.path.join(root, file)
            if file == '.DS_Store':
                continue  # skip the file
            if file in list:
                print 'keeping ---', file
            else:
                print 'deleting ---', file
                os.remove(path)
                
            
if __name__ == "__main__":
    main()