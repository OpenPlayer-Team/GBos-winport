# 1. Imposta valore base in mt_temp
scoreboard players set @s mt_temp 75

# 2. Moltiplicatore Forza (5% in più per livello)
# mt_math è usato come variabile per il calcolo del moltiplicatore base 100
scoreboard players set @s mt_math 100
scoreboard players operation @s mt_math += @s mt_lvl_str
scoreboard players operation @s mt_math += @s mt_lvl_str
scoreboard players operation @s mt_math += @s mt_lvl_str
scoreboard players operation @s mt_math += @s mt_lvl_str
scoreboard players operation @s mt_math += @s mt_lvl_str

scoreboard players operation @s mt_temp *= @s mt_math
scoreboard players operation @s mt_temp /= #100 mt_math

# 3. Moltiplicatore Efficienza (Aumenta il totale del 10% per livello)
scoreboard players set @s mt_math 100
scoreboard players operation @s mt_math += @s mt_lvl_eff
scoreboard players operation @s mt_math += @s mt_lvl_eff
scoreboard players operation @s mt_math += @s mt_lvl_eff
scoreboard players operation @s mt_math += @s mt_lvl_eff
scoreboard players operation @s mt_math += @s mt_lvl_eff
scoreboard players operation @s mt_math += @s mt_lvl_eff
scoreboard players operation @s mt_math += @s mt_lvl_eff
scoreboard players operation @s mt_math += @s mt_lvl_eff
scoreboard players operation @s mt_math += @s mt_lvl_eff
scoreboard players operation @s mt_math += @s mt_lvl_eff
scoreboard players operation @s mt_temp *= @s mt_math
scoreboard players operation @s mt_temp /= #100 mt_math




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

scoreboard players operation @s mt_money += @s mt_temp
scoreboard players operation @s mt_total += @s mt_temp

# Notifica su actionbar del guadagno
tellraw @s {"text":"+ $","color":"green","extra":[{"score":{"name":"@s","objective":"mt_temp"},"color":"gold"}]}

# Gestione XP
scoreboard players add @s mt_xp 20
execute if score @s mt_xp >= @s mt_xp_req run function mining_tycoon:player/level_up

# Azzera il contatore per non ripetere all'infinito
scoreboard players set @s mt_m_eme 0
scoreboard players set @s mt_m_d_eme 0
