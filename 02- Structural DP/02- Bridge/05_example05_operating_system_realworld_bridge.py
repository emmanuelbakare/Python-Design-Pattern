class FileApp:
    def __init__(self, os_impl):
        self.os_impl = os_impl

    def open_file(self, path):
        self.os_impl.open_file(path) 

    def close_file(self, path):
        self.os_impl.close_file(path) 

    def rename_file(self, path, new_path):
        self.os_impl.rename_file(path, new_path) 

#===========IMPLEMENTATION============================
class OperatingSystemImplementation:
    def open_file(self, path):
        pass
    
    def close_file(self, path):
        pass
    
    def rename_file(self, path, new_path):
        pass  

class WindowsImplementation(OperatingSystemImplementation):
    def open_file(self, path):
        print(f'Opening {path} in Windows')
    
    def close_file(self, path):
        print(f'Closing {path} in Windows')
    
    def rename_file(self, path, new_path):
        print(f'Renaming {path} to {new_path} in Windows')  

class LinuxImplementation(OperatingSystemImplementation):
    def open_file(self, path):
        print(f'Opening {path} in Linux')
        
    def close_file(self, path):
        print(f'Closing {path} in Linux')
        
    def rename_file(self, path, new_path):
        print(f'Renaming {path} to {new_path} in Linux')

class MacOSImplementation(OperatingSystemImplementation):
    def open_file(self, path):
        print(f'Opening {path} in MacOS')
        
    def close_file(self, path):
        print(f'Closing {path} in MacOS')
        
    def rename_file(self, path, new_path):
        print(f'Renaming {path} to {new_path} in MacOS')


windows = WindowsImplementation()
linux = LinuxImplementation()
macos = MacOSImplementation()

file = FileApp(macos)
file.open_file("example.txt")
file.close_file("example.txt")
file.rename_file("example.txt", "example_renamed.txt")