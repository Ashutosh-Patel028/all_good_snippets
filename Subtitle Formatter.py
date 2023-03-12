#Remove unwanted language or gibberish text from subtitle srt file.
import langid
# this langid library classifies text to their language based like "en" for English
# Detects total of 97 languages

# Read input srt and write to output srt
f_read=open("D:\input.srt","r")
f_write=open("D:\output.srt","w")

for line in f_read:
    ans=langid.classify(line) #classify return tuple
    if(ans[0]=="en"):
        f_write.write(line)

# CLose both read and write file
f_read.close()
f_write.close()

#logic to remove gibberish text from subtitle is that line is not english simple dont put in output srt file
#like numbers are also counted as english language(en)