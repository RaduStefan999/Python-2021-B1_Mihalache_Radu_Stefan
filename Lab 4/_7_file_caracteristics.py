import os

def file_caracteristics (file_path) :
    caracteristics_dict = dict([])

    caracteristics_dict["full_path"] = os.path.abspath(file_path)
    caracteristics_dict["file_size"] = os.path.getsize(file_path)
    caracteristics_dict["file_exteson"] = os.path.splitext(file_path)[1]
    caracteristics_dict["can_read"] = os.access(file_path, os.W_OK)
    caracteristics_dict["can_write"] = os.access(file_path, os.R_OK)

    return caracteristics_dict

print(file_caracteristics("D:\work\\bd\Learning\Python\Lab 4\_2_records.txt"))