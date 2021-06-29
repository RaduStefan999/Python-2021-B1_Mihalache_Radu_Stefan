import os

def director_records(director, fisier) :
    files_in_dir = os.listdir(director)
    files_record = open(fisier, "w")

    for file_in_dir in files_in_dir :
        cale = os.path.join(director, file_in_dir)
        if os.path.isfile(cale) == True :
            files_record.write(cale)
            files_record.write("\n")

    return

director_records("D:\work\\bd\Learning\Python\Lab 4", "D:\work\\bd\Learning\Python\Lab 4\_2_records.txt")
            