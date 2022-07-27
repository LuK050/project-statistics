import os


def main():
    filepath = input("> Укажите прямой путь до папки проекта: ")
    result = counter(filepath)
    print(f"\n- Количество файлов: {result['files']}\n- Количество строк: {result['lines']}\n- Чистых строк: ≈{result['clear_lines']}\n- Расширения: <{', '.join(sorted(list(set(result['extensions'])), key = lambda x: result['extensions'].count(x), reverse = True))}>\n")
    input("Для завершения нажмите любую клавишу...")
       
            
def counter(filepath: str) -> dict:
    os.chdir(filepath)
    clear_lines, lines, files = 0, 0, 0
    extensions = []
    
    for filename in os.listdir(os.getcwd()):
        try:
            if "." in filename:
                files += 1
                lines += sum(1 for _ in open(filepath + "\\" + filename))
                
                for line in open(filepath + "\\" + filename):
                    line = line.replace(" ", "").replace("\n", "")
                    clear_lines += 1 if "import" not in line and "package" not in line and "include" not in line and line not in ("", "}", "{", ")", "(", "]", "[") else 0
                    
                extensions.append(filename.split(".")[len(filename.split(".")) - 1])
            else:
                result = counter(filepath + "\\" + filename)
                lines += result["lines"]
                clear_lines += result["clear_lines"]
                files += result["files"]
                extensions += result["extensions"]
        except:
            continue
    return {
        "lines": lines,
        "clear_lines": clear_lines,
        "files": files,
        "extensions": extensions,
    }
        
main()