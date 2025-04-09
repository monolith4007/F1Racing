# Credits: W3Schools, GeeksforGeeks, Stack Overflow

# --- Libraries ---
import statistics

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

# --- Helper functions ---
def calculate_points(place):
    if place == 1:
        return 25
    elif place == 2:
        return 18
    elif place == 3:
        return 15
    elif place == 4:
        return 12
    elif place == 5:
        return 10
    elif place == 6:
        return 8
    elif place == 7:
        return 6
    elif place == 8:
        return 4
    elif place == 9:
        return 2
    elif place == 10:
        return 1
    elif place > 10:
        return 0

def calculate_total_time(laps):
    # Check if crashed or retired
    if "retired" in laps or "crashed" in laps:
        # Copy laps and remove "retired"/"crashed" index
        # Retiring or crashing ends the race instantly, so we can safely remove the last index
        successful_laps = laps.copy()
        successful_laps.pop()
        return statistics.mean(successful_laps)

    return statistics.mean(laps)

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
    total_times = []
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
        
        # Loop through lap times
        for x in range(len(lap_times[n])):
            lap_index = lap_times[n][x]

            # Convert valid lap times to floats
            # Check for the presence of a number; the first character should suffice
            if lap_index[0].isdigit():
                lap_times[n][x] = float(lap_index)

        # Calculate total times
        total_times.append(calculate_total_time(lap_times[n]))

    total_times.sort()
    print(total_times)
    #print(total_times)
    
    # Assign drivers to a list
    #drivers_list = drivers_string.splitlines()
    
    

individual_race_result(read_results(), read_drivers(), 1)
