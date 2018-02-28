titles = []
morals = []
text = []

def grab(source):
    with open(source) as f_handle:
        lines = f_handle.readlines()
    return lines


def grab_t(lines):
    # with open("11339-8.txt") as f_handle:
    #   lines = f_handle.readlines()
    for line in lines:
        if line.upper() == line:
            stripped = line.lstrip().rstrip()
            if stripped != '':
              titles.append(stripped)
    return titles

def grab_m(lines):
    # with open("11339-8.txt") as f_handle:
    #   lines = f_handle.readlines()
    for line in lines:
        if "    " in line:
          morals.append(line)
    return morals

def grab_txt(lines):
    # with open("11339-8.txt") as f_handle:
    #     lines = f_handle.readlines()
    for line in lines:
        is_title = line.isupper()
        is_moral = "    " in line
        if is_moral == False and is_title == False:
            text.append(line)
    return text
