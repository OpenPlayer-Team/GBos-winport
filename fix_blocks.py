import os
import glob

# Script per aggiornare i blocchi con il moltiplicatore Prestigio e l'abilità Fortuna.

def update_blocks():
    block_files = glob.glob('mining_tycoon/data/mining_tycoon/function/economy/blocks/*.mcfunction')

    luck_logic = """
# 4. Abilità Fortuna (Luck)
# Generiamo un numero da 1 a 100
execute store result score @s mt_temp_rand run random value 1..100
# Calcoliamo la soglia di fortuna: mt_lvl_luck * 2 (2% a livello)
scoreboard players operation @s mt_temp_luck = @s mt_lvl_luck
scoreboard players operation @s mt_temp_luck *= #2 mt_math
# Se random <= soglia fortuna, raddoppia mt_temp e notifica
execute if score @s mt_temp_rand <= @s mt_temp_luck run scoreboard players operation @s mt_temp *= #2 mt_math
execute if score @s mt_temp_rand <= @s mt_temp_luck run playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 1 1.5
execute if score @s mt_temp_rand <= @s mt_temp_luck run tellraw @s {"text":"🍀 Colpo Fortunato! Guadagno raddoppiato!","color":"light_purple"}

# 5. Moltiplicatore Prestigio
execute if score @s mt_prestige_mul matches 2.. run scoreboard players operation @s mt_temp *= @s mt_prestige_mul

# 6. Assegna Denaro e XP
"""

    for fpath in block_files:
        with open(fpath, 'r') as f:
            content = f.read()

        # Pulisci e rimpiazza per sicurezza
        if "# 4. Abilità Fortuna" in content:
            # taglia la vecchia logica
            content = content.split("# 4. Abilità Fortuna")[0] + "\n# 4. Assegna Denaro e XP\n" + content.split("# 6. Assegna Denaro e XP\n")[1]

        # Sostituiamo il pezzo finale per inserire la nostra logica
        content = content.replace("# 4. Assegna Denaro e XP\n", luck_logic)

        with open(fpath, 'w') as f:
            f.write(content)

update_blocks()
