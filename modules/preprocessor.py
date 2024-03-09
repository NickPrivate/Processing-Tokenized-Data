from modules.file_reader import FileReader
import re

class Preprocessor:
    def preprocess(self, lines):
        """Remove comments and excessive whitespace from a list of lines."""
        processed_lines = []
        for line in lines:
            # Remove comments
            cleaned_line = re.sub(r'#.*', '', line)
            # Remove leading and trailing whitespace, then collapse multiple spaces into one
            cleaned_line = ' '.join(cleaned_line.strip().split())
            # Only add non-empty lines to the result
            if cleaned_line:
                processed_lines.append(cleaned_line)
        return processed_lines
