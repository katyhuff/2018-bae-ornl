import numpy as np

def read_cyclus(cyclus_file, outputfile):
    recipe = False
    with open(cyclus_file, 'r') as f:
        lines = f.readlines()
    comp_dict = {}
    for indx, line in enumerate(lines):
        print(line)
        if 'name' in line:
            name = find_between(line, '<name>', '</name>')
            comp_dict[name] = {}
        if 'id' in line and 'nuclide' not in line:
            iso = find_between(line, '<id>', '</id>')
            comp = float(find_between(lines[indx+1], '<comp>', '</comp>'))
            comp_dict[name].update({iso: comp})

    # normalize comp_dict
    for key, val in comp_dict.items():
        total = sum(val.values(), 0.0)
        comp_dict[key] = {k: v / total for k,v in val.items()}

    # comp_dict[name of recipe] = {isotope: composition}
    return comp_dict


def write_orion()

def find_between(string, first, last ):
    start = string.index(first) + len(first)
    end = string.index(last, start)
    return string[start:end]


comp_dict = cyclus_to_orion('test.xml', '')
print(comp_dict)