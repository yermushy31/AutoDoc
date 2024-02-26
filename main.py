import os
import sys
import time
import re

from ressources import *

FilePath = "./output/"
TITLE = "C File"
FileName = "output.adoc"
updated_lines = []

def create_adoc_file(file_path: str, file_content: str):
    try:
        file = open(file_path + FileName, 'w+')
        return file 
    except Exception as e:
        print("{-} Error creating file: ", e)
        sys.exit(1)
   
   
def delete_all_lines(file_path):
    with open(file_path, 'w'):
        pass



    

def process_python():
    pass

def process_php():
    pass

def process_java():
    pass

def process_c(file_content: str):
    newFile = create_adoc_file(FilePath, file_content)
    
    file_content = file_content.split("\n")
    h1 = asciidoc["titles"]["h1"][0] + " "
    title =  h1 + TITLE + "\n\n"
    newFile.write(title)
    for line in file_content:
    
        if "/*" in line:
            #get comment content
            comment = re.findall(r'/\*(.*?)\*/', line, re.DOTALL)
            boldsyntax = "".join(asciidoc["syntax"]["bold"][0])
            #remove all whitespaces
            comment[0] = comment[0].strip()

            newline = boldsyntax + comment[0] + boldsyntax
            updated_lines.append(newline + "\n\n")   
            #then remove the comment from the line
            line = line.replace("/*", "").replace("*/", "")
            
            
        if any(directive in line for directive in c["Preprocessor Directives"]):
            # get the directive name
            directive_name = next((directive for directive in c["Preprocessor Directives"] if directive in line), None)
            if directive_name:
                # extract the content after the library name
                content = line.split(directive_name)[1].strip()
                newline = f"This Program is using {asciidoc['syntax']['monospace'][0]}{content}{asciidoc['syntax']['monospace'][0]} directive: {directive_name}\n"
                updated_lines.append(newline + "\n\n")
                

        if any (type in line for type in c["Types"]):
            # get the type name
            type_name = next((type for type in c["Types"] if type in line), None)
            if type_name:
                for c_type in c["Types"]:
                    #detect if function 
                    if re.search(r'\b{}\s+\w+\s*\([^)]*\)\s*{{'.format(re.escape(c_type)), line):
                        # extract the content after the type name
                        content = line.split(c_type)[1].strip()
                        # remove rest after content
                        content = content.split("(")[0]
                        newline = f"This Program is using the Function {asciidoc['syntax']['monospace'][0]}{content}{asciidoc['syntax']['monospace'][0]} type: {c_type}\n"
                        updated_lines.append(newline + "\n\n")
                    #detect if variable
                    elif re.search(r'\b{}\s+\w+\s*;'.format(re.escape(c_type)), line):
                        # extract the content after the type name
                        content = line.split(c_type)[1].strip()
                        # remove rest after content
                        content = content.split(";")[0]
                        newline = f"This Program is using the Variable {asciidoc['syntax']['monospace'][0]}{content}{asciidoc['syntax']['monospace'][0]} type: {c_type}\n"
                        updated_lines.append(newline + "\n\n")
                       
              
    delete_all_lines(FilePath + FileName)
    newFile.writelines(updated_lines)
    
def process_cpp():
    pass
        

def process_csharp():
    pass


extensions = {".py": process_python , 
              ".php": process_php, 
              ".java": process_java, 
              ".c": process_c, 
              ".cpp": process_cpp, 
              ".cs": process_csharp
}


def read_file(file_path: str):
    with open(file_path, 'r+') as file:
        return file.read()


def detect_language(file_path: str):
    file_content = read_file(file_path)
    file_extension = os.path.splitext(file_path)[1] 
    print("{+} File extension is :", file_extension)
    
    file_extension.split(".")
    if file_extension in extensions:
        print("{+} Language supported calling function ", extensions[file_extension].__name__ + "()")
        extensions[file_extension](file_content)  
    else:
        print("{-} Language not supported")
        return None


if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
    except IndexError:
        print("{-} Usage: python3 main.py <file_path>")
        sys.exit(1)
    else:
        print("{+} Detecting language...")
        process_function = detect_language(file_path)