import json as j
import inspect as i

def make_save_dict(dictionary):
    save_list = []
    for thing in dictionary.keys():
        if not str(thing).startswith('__'):
            value = dictionary.get(thing)
            mything = value

            if type(value) == str:
                template = "global {}; {} = '{}'"
                save_list.append(template.format(thing, thing, value))
            
            elif type(value) in [bool, int, float, list, dict, tuple]:
                template = "global {}; {} = {}"
                save_list.append(template.format(thing, thing, value))
        
            else:
                for possible_class in dictionary:
                    if str(value).startswith(f"<__main__.{possible_class}"):

                        save_list.append(f'{thing} = {possible_class}(')

                        for mytuple in i.getmembers(mything):
                            attribute = mytuple[0]
                            attrval = mytuple[1]
                            if not str(attribute).startswith('__'):
                                save_list[-1] += f"{attribute}='{attrval}', "
                        save_list[-1] = save_list[-1][:-2]
                        save_list[-1] += ')'
    
    return {stuff: None for stuff in save_list}

def save_game(dictionary):
    with open('savefile.json', 'w') as outfile:
        j.dump(dictionary, outfile)

def restore_game():
    with open('savefile.json', 'r') as outfile:
        dictionary = j.load(outfile)
        return dictionary
