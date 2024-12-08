# Credits: W3Schools, GeeksforGeeks, Stack Overflow

# --- Reader functions ---
def read_results():
    file = open("results.txt", "r")
    contents = file.read()
    file.close()
    return contents

def read_drivers():
    file = open("drivers.txt", "r")
    contents = file.read()
    file.close()
    return contents

# --- Results functions ---
def individual_race_result(results_string, drivers_string, race_number):
    # Validate race
    if race_number < 1 or race_number > 2:
        print(f"No results available for Race {race_number}")
        return

    # Assign results to a list
    results_list = results_string.splitlines()
    #print(results_list[0])

    # Initialize driver lap times
    lap_times = []
    opening = -1
    ending = -1

    # Loop through races
    for n in range(len(results_list)):
        results_index = results_list[n]

        # Ignore if race numbers don't match
        if int(results_index[0]) != race_number:
            continue

        # Confine lap times
        opening = results_index.find("[") + 1 # Get index of "["
        ending = results_index.find("]") # Get index of "]"
        lap_times.append(results_index[opening:ending]) # Append everything between the "[]"
        lap_times[n] = lap_times[n].split(", ") # Separate lap times individually
        
        # Convert valid lap times to floats
        for x in range(len(lap_times[n])):
            lap_index = lap_times[n][x]

            # Check for the presence of a number; the first character should suffice
            if lap_index[0].isdigit():
                lap_times[n][x] = float(lap_index)
            else:
                # Crashed or retired; let's default to -1
                lap_times[n][x] = -1
        
    print(lap_times[3])
    # Assign drivers to a list
    #drivers_list = drivers_string.splitlines()
    
    

individual_race_result(read_results(), read_drivers(), 1)
