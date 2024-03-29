class FileReader:

    def __init__(self, file_path):
        self.file_path = 'tests/input.txt'
    # Step 1: Simply read from a test file
    
    def read_file(self):

        with open(self.file_path, 'r') as file:
            content_lines = file.readlines()
            
        return content_lines
