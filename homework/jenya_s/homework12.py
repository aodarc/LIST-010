import os

class Cpypl:
        
    def __init__(self, directory):
        self.directory = directory
        self.extension_dict = {"c": (".c", ".h"),
                               "py": (".py", ".pyc"),
                               "pl": (".pl", ".pm"),
                              }
        
    def file_list(self):
        folder_files = os.listdir(self.directory)
        extension = self.extension_dict
        return [i for i in folder_files for j in extension if i.endswith(extension[j])]

a = Cpypl(r"C:\Users\admin\Desktop\python test")

print(a.file_list())
