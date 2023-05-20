import os
import subprocess
from config import * 
import glob

def build_packages():
    for i in FILEMAP:
        filename = os.path.basename(i[1]).split(".")[0]
        if not os.path.exists(f'{DIRPATH}/build_packages/'):
            os.makedirs(f'{DIRPATH}/build_packages/')
        # command = f'docker run --volume {DIRPATH}:/local wework/speccy resolve /local{i[1]} -o /local/build_packages/{filename}.yaml'
        command = f'speccy resolve {i[1]} -o {DIRPATH}/build_packages/{filename}.yaml'
        print(command)
        output = subprocess.run(command.split(), shell=True)
        print(output)
        print(glob.glob(f"{DIRPATH}/build_packages/*"))


if __name__ == "__main__":
    print(DIRPATH)
    build_packages()