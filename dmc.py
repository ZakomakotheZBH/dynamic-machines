import re

class DynamicMachineCode:
    def __init__(self):
        self.functions = {}

    def binary_to_text(self, binary_str):
        # Removes spaces and converts binary blocks to text
        binary_str = binary_str.replace(" ", "")
        ascii_text = ""
        for i in range(0, len(binary_str), 8):
            byte = binary_str[i:i+8]
            ascii_text += chr(int(byte, 2))
        return ascii_text

    def run(self, code):
        # 1. Remove Comments (lines starting with -)
        lines = [l for l in code.split('\n') if not l.strip().startswith('-')]
        
        for line in lines:
            line = line.strip()
            if not line: continue

            # 2. Handle Binary Text
            if all(c in '01 ' for c in line):
                print(self.binary_to_text(line))

            # 3. Handle Buttons
            elif line.startswith('/'):
                label = line[1:].strip()
                print(f"[ UI Button: {label} ]")

            # 4. Handle Textareas
            elif line.startswith('+'):
                label = line[1:].strip()
                print(f"| Textarea: {label} | ________________")

            # 5. Handle Functions
            elif line.startswith('('):
                func_name = line[1:].strip()
                print(f"Defining Function: {func_name}")
