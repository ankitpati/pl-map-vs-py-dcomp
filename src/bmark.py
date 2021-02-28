#!/usr/bin/env python
'''Benchmark Runner'''

from timeit import timeit

# Data Credit: https://images-of-elements.com/element-properties.php
data = [
    ['Hydrogen', 1.008, 14.1, 20.3],
    ['Helium', 4.003, '', 4.2],
    ['Lithium', 6.941, 454, 1615],
    ['Beryllium', 9.012, 1551, 3750],
    ['Boron', 10.81, 2349, 4200],
    ['Carbon', 12.011, 3820, 5100],
    ['Nitrogen', 14.007, 63.1, 77.4],
    ['Oxygen', 15.999, 54.4, 90.2],
    ['Fluorine', 18.998, 53.5, 85],
    ['Neon', 20.18, 24.6, 27.1],
    ['Sodium', 22.99, 371, 1156],
    ['Magnesium', 24.305, 923, 1380],
    ['Aluminium', 26.92, 933, 2740],
    ['Silicon', 28.085, 1683, 2628],
    ['Phosphorus', 30.974, 317, 550],
    ['Sulphur', 62.065, 338, 718],
    ['Chlorine', 35.453, 172, 239],
    ['Argon', 39.948, 84, 87],
    ['Potassium', 39.098, 337, 1032],
    ['Calcium', 40.078, 1115, 1757],
    ['Scandium', 44.956, 1814, 3103],
    ['Titanium', 47.867, 1941, 3560],
    ['Vanadium', 50.942, 2183, 3680],
    ['Chromium', 51.996, 2130, 2945],
    ['Manganese', 54.938, 1517, 2235],
    ['Iron', 55.845, 1808, 3023],
    ['Cobalt', 58.993, 1768, 3200],
    ['Nickel', 58.693, 1738, 3186],
    ['Copper', 63.456, 1358, 2840],
    ['Zinc', 65.39, 693, 1180],
    ['Gallium', 69.723, 303, 2477],
    ['Germanium', 72.64, 1211, 3093],
    ['Arsenic', 74.922, '', 889],
    ['Selenium', 78.96, 494, 958],
    ['Bromine', 79.904, 266, 332],
    ['Krypton', 83.8, 116, 120],
    ['Rubidium', 85.468, 312, 961],
    ['Strontium', 87.62, 1050, 1655],
    ['Yttrium', 88.906, 1799, 3609],
    ['Zirconium', 91.224, 2130, 4682],
    ['Niobium', 92.906, 2750, 5017],
    ['Molybdenum', 95.94, 2896, 4912],
    ['Technetium', 98, 2430, 5150],
    ['Ruthenium', 101.07, 2607, 4423],
    ['Rhodium', 102.91, 2273, 3968],
    ['Palladium', 106.42, 1828, 3236],
    ['Silver', 107.87, 1234, 2435],
    ['Cadmium', 112.41, 594, 1040],
    ['Indium', 114.82, 430, 2345],
    ['Tin', 118.71, 505, 2875],
    ['Antimony', 121.76, 904, 1860],
    ['Tellurium', 127.6, 723, 1263],
    ['Iodine', 126.9, 387, 457],
    ['Xenon', 131.29, 161, 165],
    ['Caesium', 132.9, 302, 944],
    ['Barium', 137.33, 1000, 1913],
    ['Lanthanum', 138.91, 1193, 3730],
    ['Cerium', 140.12, 1068, 3716],
    ['Praseodymium', 140.91, 1204, 3793],
    ['Neodymium', 144.24, 1297, 3373],
    ['Promethium', 145, 1315, 3273],
    ['Samarium', 150.36, 1345, 2076],
    ['Europium', 151.96, 1099, 1800],
    ['Gadolinium', 157.25, 1585, 3523],
    ['Terbium', 158.92, 1629, 3503],
    ['Dysprosium', 162.5, 1680, 2840],
    ['Holmium', 163.93, 1747, 2963],
    ['Erbium', 167.26, 1795, 2783],
    ['Thulium', 168.93, 1818, 2220],
    ['Ytterbium', 173.04, 1097, 1467],
    ['Lutetium', 174.97, 1936, 3668],
    ['Hafnium', 178.49, 2506, 4876],
    ['Tantalum', 180.95, 3290, 5731],
    ['Tungsten', 183.84, 3695, 5828],
    ['Rhenium', 186.21, 3459, 5869],
    ['Osmium', 190.23, 3306, 5285],
    ['Iridium', 192.22, 2739, 4701],
    ['Platinum', 195.08, 2045, 4100],
    ['Gold', 196.97, 1337, 3129],
    ['Mercury', 200.59, 234, 630],
    ['Thallium', 204.38, 577, 1746],
    ['Lead', 207.2, 601, 2023],
    ['Bismuth', 208.98, 544, 1837],
    ['Polonium', 209, 527, 1235],
    ['Astatine', 210, 575, 610],
    ['Radon', 222, 202, 211],
    ['Francium', 223, 300, 950],
    ['Radium', 226, 973, 2010],
    ['Actinium', 227, 1327, 3473],
    ['Thorium', 232.04, 2028, 5061],
    ['Protactinium', 231.04, 2113, 4300],
    ['Uranium', 238.03, 1406, 4203],
    ['Neptunium', 237, 912, 4175],
    ['Plutonium', 244, 913, 3509],
    ['Americium', 243, 1449, 2880],
    ['Curium', 247, 1613, 3383],
    ['Berkelium', 247, 1259, ''],
    ['Californium', 251, 1173, 1743],
    ['Einsteinium', 252, 1133, ''],
    ['Fermium', 257, 1800, ''],
    ['Mendelevium', 258, 1100, ''],
    ['Nobelium', 259, 1100, ''],
    ['Lawrencium', 262, '', ''],
    ['Rutherfordium', 267, '', ''],
    ['Dubnium', 262, '', ''],
    ['Seaborgium', 266, '', ''],
    ['Bohrium', 264, '', ''],
    ['Hassium', 277, '', ''],
    ['Meitnerium', 268, '', ''],
    ['Darmstadtium', 281, '', ''],
    ['Roentgenium', 280, '', ''],
    ['Copernicium', 277, '', ''],
    ['Nihonium', 287, '', ''],
    ['Flerovium', 289, '', ''],
    ['Moscovium', 288, '', ''],
    ['Livermorium', 289, '', ''],
    ['Tenessine', 291, '', ''],
    ['Oganesson', 294, '', ''],
]


def regular_hash():
    '''Code being benchmarked'''
    processed = {x[0]: (x[3] - x[2]) / x[1] if x[3] and x[2] else None
                 for x in data}
    return processed


def numeric_regular_hash():
    '''Code being benchmarked'''
    processed = {x: x * x for x in range(1001)}
    return processed


def main():
    '''Entry point'''

    # Total, wallclock time for lots of runs.
    print(
        "Regular Hash:\t\t", timeit(regular_hash, number=10000), "\n",
        "Numeric Regular Hash:\t", timeit(regular_hash, number=10000), "\n",
        sep=''
    )

    # Verify correctness, and compare with other benchmarked code.
    regular_hash_ret = regular_hash()
    for key, value in sorted(regular_hash_ret.items()):
        print(str(key) + ',' + ('{:.7f}'.format(value) if value else 'N/A'))

    numeric_regular_hash_ret = numeric_regular_hash()
    for key, value in sorted(numeric_regular_hash_ret.items()):
        print(str(key) + ',' + str(value))


if __name__ == '__main__':
    main()
