# Incrementa Moltiplicatore Prestigio
scoreboard players operation @s mt_prestige_mul += #1 mt_math

# Azzera Livelli e Upgrade
scoreboard players set @s mt_lvl_mining 0
scoreboard players set @s mt_lvl_str 0
scoreboard players set @s mt_lvl_eff 0
scoreboard players set @s mt_lvl_luck 0

# Azzera Economia
scoreboard players set @s mt_money 0
scoreboard players set @s mt_xp 0
scoreboard players set @s mt_xp_req 50

# Azzera Costi
scoreboard players set @s mt_c_str 100
scoreboard players set @s mt_c_eff 500
scoreboard players set @s mt_c_luck 1000

# Notifica Globale
tellraw @a ["",{"text":"⭐ ","color":"yellow"},{"score":{"name":"@s","objective":"mt_prestige_mul"},"color":"light_purple"},{"text":"° PRESTIGIO RAGGIUNTO DA ","color":"gold"},{"selector":"@s","color":"white"},{"text":"! ⭐","color":"yellow"}]
playsound minecraft:ui.toast.challenge_complete master @a ~ ~ ~ 1 1
