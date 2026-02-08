# Instructions:
**Move the files: id_gen.py and id.json to the folder with your code, then write import id_gen**

# Functions:
**symbols - Number of characters in the generated id**
*Generation with check for occupied IDs:*
id_gen.gen_w_num(symbols) - Generation with numbers
id_gen.gen(symbols) - Generation without numbers
*Generation without chek:*
id_gen.gen_ignore(symbols) or id_gen.gen_ignore_w_num(symbols) - Generation ignoring occupied ids

# Example usage:
*For example, symbols will be 10*

**id = id_gen.gen_w_num(10)**
**print(id)**
Output: hd9znonl0e
*File id.json:*
{
    "id_taken": {
        "none": 1,
        "hd9znonl0e": 1
    }
}
If hd9znonl0e was busy, the function would generate a new id
*"none":1 appears after the first generation, leave it so that "none": 1 is not generated in the future.*

**id = id_gen.gen(10)**
**print(id)**
Output: aqjpfrvoti
*File id.json:*
{
    "id_taken": {
        "none": 1,
        "hd9znonl0e": 1,
        "aqjpfrvoti": 1
    }
}

**id = id_gen.gen_ignore(symbols)**
**print(id)**
Output: acirklffvn
*File id.json:*
{
    "id_taken": {
        "none": 1,
        "hd9znonl0e": 1,
        "aqjpfrvoti": 1
    }
}

**id = id_gen.gen_ignore_w_num(symbols)**
**print(id)**
Output: 7x91z5sqg8
*File id.json:*
{
    "id_taken": {
        "none": 1,
        "hd9znonl0e": 1,
        "aqjpfrvoti": 1
    }
}
