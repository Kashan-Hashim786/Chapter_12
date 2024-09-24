with (
   open('file1.txt',"w") as f1,
   open('file2.txt',"w") as f2
):
    f1.write("File No 1")
    f2.write("File No 2")
