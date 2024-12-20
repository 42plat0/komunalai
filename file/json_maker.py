import json
from datetime import datetime
filename = "utilities_log.json"

def form_json(dct):
    return json.dumps(dct, indent=4)

def get_dict_f_json(j):
    return json.loads(j)

def write_json_file(j):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(j)

# Return content of json file
def read_json_file():
    content = None

    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read(-1)
    except FileNotFoundError:
        return 0

    return content

# Updates json with a new value from content 
def update_dct(f_dct, content):
    key = list(content.keys())[0]  # Get key of content, date
    f_dct[key] = content[key]
    return

# Checks if there are values that we could use in GUI
def log_exists():
    return bool(read_json_file())