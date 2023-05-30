import os
import shutil
import zipfile 

class FileHelper:

    def __init__(self):
        self.path = os.getcwd()
        self.file = None

    def change_dir(self):
        text = input("Enter the Path: ")
        if len(text) == 0:
            text = os.getcwd() 
        else:
            text.replace("\\", "/")
            os.chdir(text)
            self.path = text
        return text
    


    def write_file(self, filename):
        with open(filename, 'w') as file:
            content = ''
            writeFile = True
            while writeFile:
                content = input('Enter Content: ')
                if len(content) == 0:
                    print("End of writing to file", filename)
                    writeFile = False
                content += content
            file.write(f'{content}\n')
        current_file_path = os.path.join(os.getcwd(),filename)
        self.file = current_file_path
                 


    def make_folders(self, path,  swap_to_path=True): 
        path = os.path.join(os.getcwd(),path)

        if not os.path.exists(path):
            os.makedirs(path)
        else:
            print("Folder Already Exists")

        if swap_to_path:
            os.chdir(path)
            self.path = path

    def copy_to(self, dest):
        shutil.copy2(self.file, dest)


    def move_to(self, dest):
        shutil.move(self.file, dest)
        self.file = os.path.join(dest, self.file)

    def delete(self):
        os.remove(self.file)

    def zip(self, archive_name):
        with zipfile.ZipFile(archive_name,'w') as zip_file:
            zip_file.write(self.file)
    


