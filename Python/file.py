with open('buffered_file.txt', 'w', buffering=1) as buffered_file:
    buffered_file.write("This file uses line buffering.")
