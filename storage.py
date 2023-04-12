import os 

import os

directory = "/Users/jeffreyfernandez/GitHub/face-recognition"  # replace with your directory path

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path):
        file_size = os.path.getsize(file_path)
        print(f"{filename}: {file_size} bytes")
