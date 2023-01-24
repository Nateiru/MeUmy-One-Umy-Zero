import os

def find_tex_file(path):
    files = os.listdir(path)
    for filename in files:
        fullpath = os.path.join(path, filename)
        if os.path.isdir(fullpath):
            find_tex_file(fullpath)
        elif filename.endswith(".tex"):
            with open(fullpath, "r", encoding='utf-8') as f:
                content = f.read()
                content = content.replace('\t', '    ')
            with open(fullpath, "w", encoding='utf-8') as f:
                f.write(content)
                print("Replaced tabs in file: %s." % fullpath)
            

find_tex_file("./chapters") 
