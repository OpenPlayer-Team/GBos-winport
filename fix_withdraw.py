import glob

# Script per fixare l'ordine di esecuzione nei prelievi:
# dobbiamo dare l'oggetto PRIMA di sottrarre il denaro,
# oppure usare un temporary score. Useremo l'ordine corretto: prima give, poi subtract.

files = glob.glob('mining_tycoon/data/mining_tycoon/function/banknotes/withdraw_*.mcfunction')

for fpath in files:
    with open(fpath, 'r') as f:
        lines = f.readlines()

    new_lines = []
    give_line = ""
    sub_line = ""
    play_line = ""

    for line in lines:
        if line.startswith("scoreboard players set"):
            new_lines.append(line)
        elif "give @s paper" in line:
            give_line = line
        elif "-=" in line:
            sub_line = line
        elif "playsound" in line:
            play_line = line

    if give_line and sub_line and play_line:
        new_lines.append(give_line)
        new_lines.append(sub_line)
        new_lines.append(play_line)

        with open(fpath, 'w') as f:
            f.writelines(new_lines)
