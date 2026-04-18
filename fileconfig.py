import sys
import os
import webbrowser

def translate_to_html(input_file):
    if not input_file.endswith('.zewpolbin'):
        print("Error: File must be a .zewpolbin format")
        return

    with open(input_file, 'r') as f:
        lines = f.readlines()

    html_content = "<html><body style='font-family: sans-serif; padding: 20px;'>"
    
    for line in lines:
        line = line.strip()
        if not line or line.startswith('-'): continue # Ignore comments

        # Handle Binary (Text)
        if all(c in '01 ' for c in line):
            binary_str = line.replace(" ", "")
            text = "".join([chr(int(binary_str[i:i+8], 2)) for i in range(0, len(binary_str), 8)])
            html_content += f"<p>{text}</p>"

        # Handle Buttons
        elif line.startswith('/'):
            label = line[1:].strip()
            html_content += f"<button onclick='alert(\"{label} clicked\")'>{label}</button><br><br>"

        # Handle Textareas
        elif line.startswith('+'):
            label = line[1:].strip()
            html_content += f"<label>{label}:</label><br><textarea></textarea><br><br>"

    html_content += "</body></html>"

    # Save and open the result
    output_path = "output.html"
    with open(output_path, "w") as f:
        f.write(html_content)
    
    webbrowser.open('file://' + os.path.realpath(output_path))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        translate_to_html(sys.argv[1])
    else:
        print("Usage: python dmc.py yourfile.zewpolbin")
