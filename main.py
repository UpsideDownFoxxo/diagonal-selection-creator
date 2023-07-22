from litemapy import Region, Schematic
import math

if __name__ == "__main__":
    step_size = int(input("step_size: "))
    thickness = step_size + int(input(f"thickness: ") or 0)
    height = int(input("height: "))
    length = int(input("'length' of the diagonal (really just the difference in the x or z coord): "))

    regions = {}

    for i in range(math.floor(length/step_size)):
        regions[str(i)] = Region(i * step_size, 0, i * step_size, step_size, height, thickness)

    name = input("schematic name: ")

    schem = Schematic(name, "made with love UwU", "", regions)
    schem.save(f"{name}.litematic")
