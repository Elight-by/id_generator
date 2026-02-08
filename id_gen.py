# gen_w_num - Generation with numbers
# gen - Generation without numbers
# gen_ingnore or gen_ingnore_w_num - Generation ignoring occupied ids


import os
import json
import random

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "id.json")

lettersEN = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
lettersENN = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','1','2','3','4','5','6','7','8','9','0']


# Load/Save functions
def load_id():
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_id(new_data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(new_data, f, indent=4, ensure_ascii=False)

# Chek function
def id_exists(id_to_check):
    id_data = load_id()
    if "id_taken" in id_data:
        return str(id_to_check) in id_data["id_taken"]
    return False

# Generation with checks of occupied IDs
def gen_w_num(symbols):
    gen_save = load_id()
    gen = "none"
    while id_exists(gen):
        gen = "none"
        gen = ''.join(random.choice(lettersENN) for _ in range(symbols))
    gen_save["id_taken"][gen] = 1
    save_id(gen_save)
    return gen

def gen(symbols):
    gen_save = load_id()
    gen = "none"
    while id_exists(gen):
        gen = "none"
        gen = ''.join(random.choice(lettersEN) for _ in range(symbols))
    gen_save["id_taken"][gen] = 1
    save_id(gen_save)
    return gen


# Generation ignoring occupied ids
def gen_ignore_w_num(symbols):
    gen = ''.join(random.choice(lettersENN) for _ in range(symbols))
    return gen

def gen_ignore(symbols):
    gen = ''.join(random.choice(lettersEN) for _ in range(symbols))
    return gen