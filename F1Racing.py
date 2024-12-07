# --- Reader functions ---
def read_results():
    file = open("results.txt", "r")
    str = file.read()
    file.close()
    return str

def read_drivers():
    file = open("drivers.txt", "r")
    str = file.read()
    file.close()
    return str

# --- Results functions ---
def individual_race_result(results_string, drivers_string, race_number):
    # Validate race
    if race_number < 1 or race_number > 2:
        print(f"No results available for Race {race_number}")
        return

    # Assign each result to a list
    results_list = results_string.splitlines()
    print(results_list)

    # Assign each driver to a list
    drivers_list = drivers_string.splitlines()
    print(drivers_list)
        
    

individual_race_result(read_results(), read_drivers(), 1)
