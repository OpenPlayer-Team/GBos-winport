import os

def fix_math():
    with open('mining_tycoon/data/mining_tycoon/function/shop/success_luck.mcfunction', 'r') as f:
        content = f.read()
    if 'mt_math' not in content:
        return
    with open('mining_tycoon/data/mining_tycoon/function/shop/success_str.mcfunction', 'r') as f:
        content = f.read()

    for _id in ['str', 'eff', 'luck']:
        path = f'mining_tycoon/data/mining_tycoon/function/shop/success_{_id}.mcfunction'
        with open(path, 'r') as f:
            content = f.read()

        # Sostituzione delle operazioni con l'uso corretto delle costanti
        content = content.replace("scoreboard players operation @s mt_temp *= #30 mt_math", "scoreboard players operation @s mt_temp *= #30 mt_math")
        content = content.replace("scoreboard players operation @s mt_temp /= #100 mt_math", "scoreboard players operation @s mt_temp /= #100 mt_math")

        with open(path, 'w') as f:
            f.write(content)

fix_math()
