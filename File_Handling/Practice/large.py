import time

# Create file
with open("Practice/largefile.txt", 'w') as file:
    for i in range(20000000):
        file.write("hello\n")  # added \n for clarity

# Read whole file at once
start = time.time()
with open("Practice/largefile.txt", 'r') as file:
    ans = file.read()  # no print
end = time.time()
print("Time if we load together:", end - start)

# Read file in chunks safely
start = time.time()
with open("Practice/largefile.txt", 'r') as file:
    chunk_size = 100  # smaller chunk for testing
    while True:
        chunk = file.read(chunk_size)
        if not chunk:
            break
        # process chunk (here we do nothing, no print)
end = time.time()
print("Time if we read in chunks:", end - start)
