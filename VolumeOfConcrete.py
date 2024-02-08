def calculate_concrete_volume(Building_type, L, W):
    if Building_type.lower() == 'residential':
        D = 0.25  # Residential building depth is half of commercial
    elif Building_type.lower() == 'commercial':
        D = 0.5
    else:
        return None  # Return None for invalid building types

    V = L * W * D
    return V


total_concrete_needed = 0

while True:
    building_type = input(
        "Enter building type (residential or commercial), or 'X' to stop: ")
    if building_type.upper() == 'X':
        break

    length = float(input("Enter length of the slab in meters: "))
    width = float(input("Enter width of the slab in meters: "))

    volume = calculate_concrete_volume(building_type, length, width)

    if volume is not None:
        total_concrete_needed += volume
        if building_type.lower() == 'residential':
            depth = 0.25
        elif building_type.lower() == 'commercial':
            depth = 0.5
        print(
            f"The volume of concrete required for a slab with a length of "
            f"{length} meters and width of {width} meters and a depth of "
            f"{depth} meters is {volume} cubic meters.")
    else:
        print("Invalid building type. Please enter 'residential' or "
              "'commercial'.")

print(
    f"Total amount of concrete needed for the day: {total_concrete_needed} "
    f"cubic meters.")
