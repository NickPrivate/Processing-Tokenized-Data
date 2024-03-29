from modules.file_reader import FileReader
import re

class Preprocessor:
        # Step 2: Remove Comments and excess whitespace outputs a list of strings
    def preprocess(self, lines):
        processed_lines = []
        for line in lines:

            cleaned_line = re.sub(r'#.*', '', line)

            cleaned_line = ' '.join(cleaned_line.strip().split())
            if cleaned_line:
                processed_lines.append(cleaned_line)
        return processed_lines
