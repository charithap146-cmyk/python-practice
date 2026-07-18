#step1:open the file'feat_python1.txt'in read mode
with open('feat_python1.txt','r')as file1:
    #step2:read the entire contents of 'feat_python1.txt'
    content=file1.read()
    #step3:open the new file 'feat_python2.txt'in write mode
    with open('feat_python2.txt','w')as file2:
        #step4:write the contents from'feat_python1.txt'to'feat_python2.txt'
        file2.write(content)
        print("contents of 'feat_python1.txt'have been successfully copied to'feat_python2.txt'.")
        

