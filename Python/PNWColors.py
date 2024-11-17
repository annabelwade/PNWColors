import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# 1. Create the color palettes
# ::::::::::::::::::::::::::::::::::::::::::::::::::
# Complete list of palettes
pnw_palettes = {
    "Starfish": (['#24492e', '#015b58', '#2c6184', '#59629b', '#89689d', '#ba7999', '#e69b99'], [7, 4, 5, 3, 1, 6, 2]),
    "Shuksan": (['#33271e', '#74677e', '#ac8eab', '#d7b1c5', '#ebbdc8', '#f2cec7', '#f8e3d1', '#fefbe9'], [7, 2, 4, 1, 6, 3, 5, 8]),
    "Bay": (['#00496f', '#0f85a0', '#edd746', '#ed8b00', '#dd4124'], [4, 1, 3, 5, 2]),
    "Winter": (['#2d2926', '#33454e', '#537380', '#81a9ad', '#ececec'], [1, 4, 5, 2, 3]),
    "Lake": (['#362904', '#54450f', '#45681e', '#4a9152', '#64a8a8', '#85b6ce', '#cde5f9', '#eef3ff'], [4, 8, 7, 2, 6, 1, 3, 5]),
    "Sunset": (['#41476b', '#675478', '#9e6374', '#c67b6f', '#de9b71', '#efbc82', '#fbdfa2'], [3, 5, 1, 7, 4, 6, 2]),
    "Shuksan2": (['#5d74a5', '#b0cbe7', '#fef7c7', '#eba07e', '#a8554e'], [2, 4, 1, 5, 3]),
    "Cascades": (['#2d4030', '#516823', '#dec000', '#e2e260', '#677e8e', '#88a2b9'], [4, 1, 5, 2, 6, 3]),
    "Sailboat": (['#6e7cb9', '#7bbcd5', '#d0e2af', '#f5db99', '#e89c81', '#d2848d'], [1, 4, 6, 2, 5, 3]),
    "Moth": (['#4a3a3b', '#984136', '#c26a7a', '#ecc0a1', '#f0f0e4'], [4, 1, 2, 3, 5]),
    "Spring": (['#d8aedd', '#bf9bdd', '#cb74ad', '#e69e9c', '#ffc3a3', '#fbe4c6'], [1, 5, 2, 4, 3, 6]),
    "Mushroom": (['#4f412b', '#865a3c', '#ba783e', '#e69c4c', '#fbcc74', '#fffbda'], [6, 1, 4, 2, 3, 5]),
    "Sunset2": (['#1d457f', '#61599d', '#c36377', '#eb7f54', '#f2af4a'], [5, 1, 2, 4, 3]),
    "Anemone": (['#009474', '#11c2b5', '#72e1e1', '#f1f4ee', '#efddcf', '#dcbe9b', '#b0986c'], [3, 5, 1, 7, 2, 6, 4]),
}

# 2. Palette builder function
# ::::::::::::::::::::::::::::::::::::::::::::::::::
def pnw_palette(name, n=None, type="continuous"):
    if name not in pnw_palettes:
        raise ValueError("Palette not found.")
    
    colors, order = pnw_palettes[name]
    if n is None:
        n = len(colors)

    if type == "continuous":
        cmap = LinearSegmentedColormap.from_list(name, colors)
        return [cmap(i / (n - 1)) for i in range(n)]
    elif type == "discrete":
        if n > len(colors):
            raise ValueError("Number of requested colors exceeds the palette capacity. Use 'continuous' instead.")
        return [colors[i - 1] for i in order[:n]]
    else:
        raise ValueError("Type must be 'continuous' or 'discrete'.")

# 3. Palette print function
# ::::::::::::::::::::::::::::::::::::::::::::::::::
def print_palette(colors, name):
    plt.figure(figsize=(len(colors), 1))
    plt.imshow([colors], aspect='auto')
    plt.axis('off')
    plt.text(len(colors) / 2, -0.5, f"{name}, n={len(colors)}", ha='center', va='center', fontsize=16, family='sans-serif')
    plt.show()

# Example usage
# palette = pnw_palette("Winter", n=100, type="continuous")
# print_palette(palette, "Winter")

