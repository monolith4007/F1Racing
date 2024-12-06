# Reader functions
def read_results():
    file = open("results.txt", "r")
    str = file.read()
    file.close()
    return str
    
results_string = read_results()
print(results_string)

def read_drivers():
    file = open("drivers.txt", "r")
    str = file.read()
    file.close()
    return str

# Good start so far...
