# memory_hog.py
import time

print("Memory hog started... eating RAM now.")
data = []

try:
    while True:
        # Append a large block of text (~20MB at a time) to memory
        data.append(" " * (20 * 1024 * 1024)) 
        print("Allocated more memory...")
        time.sleep(1)
except KeyboardInterrupt:
    print("Exiting cleanly.")