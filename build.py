import os
from config import * 

def build_packages():
    for i in FILEMAP:
        filename = os.path.basename(i[1]).split(".")[0]
        if not os.path.exists(f'{DIRPATH}/build_packages/'):
            os.makedirs(f'{DIRPATH}/build_packages/')
        command = f'speccy resolve {i[1]} -o {DIRPATH}/build_packages/{filename}.yaml'
        import subprocess
        output = subprocess.run(command.split(), shell=True)

if __name__ == "__main__":
    build_packages()