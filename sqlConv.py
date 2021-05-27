import os
import time



class Convert:

    def __init__(self, fileName="India 1.txt", tableName="tablenName"):
        os.system('cls')

        self.tableName = tableName
        
        # self.fileName = 'ind.txt'       # File name from user
        self.fileName = fileName       # File name from user
        
        self.fileLoc = os.path.dirname(__file__) + "\\" + self.fileName     # Makes absolute path

        if os.path.exists(self.fileLoc):       # Checks for its existence
            self.f = open(self.fileLoc,'rt',encoding='UTF-8')
            print("\nThe file " + str(self.fileLoc) + " has been opened successfully")
        else:
            print("\nThe file " + str(self.fileLoc) + " does not exist")


    def conv(self):
        newFile = open(os.path.dirname(__file__) + "\\" + self.fileName[:-4] + ".sql",'w',encoding='UTF-8')

        lsLine = self.f.read().split("\n")      # Split By lines
        lineCount = str(len(lsLine))

        exceptionLines = 0

        for i in range(len(lsLine)-1):
            ls = lsLine[i].split(":")       # Splits the Line using --> :


            # Try catch to avoid Index Out of bounds exception
            try:
                lsn = ls[0:9]                   # Takes the first 9 elements
                lsn.append(ls[9][:-3])          # Removes the 10th element's last 3 chars (to get rid of ' 12' of the date) as its not accurate

            except:
                print("Exception at line " + str(i+1))
                exceptionLines += 1
                continue

            output = "INSERT INTO "+self.tableName+"(number, fid, fname, lname, gender, location, status, work, doj) VALUES("    # Sets the Insert Query

            for i in range(len(lsn)):   #loops through the individual elements of a single line
                if i == 0:      # For Phone number (India)
                    output = output + "'+" + lsn[i][:2] + " " + lsn[i][2:] + "', "        # Output + '+' + first 2 chars + " " + exclude the first 2 chars
                elif i == len(lsn)-1:       # if at the last element of the list, add the Quote, Rounded Bracket Close, Semicolon
                    output = output + "'" + lsn[i] + "'" + ");"
                else:       # just append the element and add a comma with a white space
                    output = output + "'" + lsn[i] + "', "

            
            newFile.write(output+"\n")
        
        print("\n" + str(exceptionLines) + " Lines were not recorded.")

        print("\nLines: " + str(lineCount))

        


c = Convert(input("File Name: "),input("Table Name: "))

start = time.time()

c.conv()

size = os.stat(os.path.dirname(__file__) + "\\" + c.fileName[:-4] + ".sql").st_size
#  OR
# size = os.path.getsize(os.path.dirname(__file__) + "\\" + c.fileName[:-4] + ".sql")

print("\nSQL file Generated with name: \"" + c.fileName[:-4] + ".sql\" (in {:.2f}".format(time.time()-start) + " secs) ({:.2f}".format(size/ (1024*1024) ) +" MBs)")
