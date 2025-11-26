import os

def check_ascii_files(folder_path="votes"):
    IGNORED_CHARS = {'★', '☆', ' ', '☒', '☐'}
    
    for entry in os.listdir(folder_path):
        filepath = os.path.join(folder_path, entry)
        
        if not os.path.isfile(filepath):
            continue
        
        try:
            with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
                for line_number, line in enumerate(f, 1):
                    
                    for char in line:
                        if ord(char) > 127:
                            if char not in IGNORED_CHARS:
                                print(f"\n found {char} in {filepath}")
                
        except Exception as e:
            print(f"Could not process {entry}: {e}")

if __name__ == "__main__":
    check_ascii_files()