import os


def text_to_useable(dir_path):
    order_spec = []
    with open(dir_path) as f:
        lines = f.readlines()

        for i in range(0, len(lines)):
            if lines[i] == '***start***\n':

                try:
                    if lines[i + 2]:
                        code = lines[i + 2].replace("\n", "")
                    else:
                        code = ''
                except:
                    code = ''

                try:
                    if lines[i+3]:
                        name_org = lines[i + 3].replace("\n", "")
                    else:
                        name_org = ''
                except:
                    name_org = ''

                try:
                    if lines[i + 4]:
                        new_colour = lines[i + 4].replace("colour: ", "")
                        new_colour = new_colour.replace("\n", "")
                    else:
                        new_colour = ''
                except:
                    new_colour = ''

                order_spec.append((code, name_org, new_colour))
                return order_spec

