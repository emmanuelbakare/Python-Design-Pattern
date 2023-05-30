import os

class FileManagementFacade:
    def create_folder(self):
        folder_path = input("Enter the Folder Path to Create: ")
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    def delete_folder(self):
        folder_path = input("Enter the Folder Path: ")
        if os.path.exists(folder_path):
            os.rmdir(folder_path)

    def list_files(self):
        folder_path = input("Enter the Folder Path: ")
        if os.path.exists(folder_path):
            os.listdir(os.path.pardir)
        else:
            return []
        
   
        

class FileMenu:
    def __init__(self):
        self.file = FileManagementFacade()

    def menu(self):
        print("Create folder: \t\t [1] : ")
        print("Delete folder: \t\t [2] : ")
        print("List Files: \t\t [3] : ")
        print()
        choice = int(input("Enter your Choice: "))   
        if choice == 1:
            self.file.create_folder()
        elif choice == 2:
            self.file.delete_folder()
        else:
            self.file.list_files()
            
        

    
file = FileMenu()
file.menu()

    