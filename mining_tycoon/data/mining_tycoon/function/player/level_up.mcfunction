scoreboard players add @s mt_lvl_mining 1
scoreboard players operation @s mt_xp -= @s mt_xp_req

# Incrementa XP Req (Moltiplica per 1.5)
scoreboard players operation @s mt_temp = @s mt_xp_req
scoreboard players operation @s mt_temp /= #2 mt_math
scoreboard players operation @s mt_xp_req += @s mt_temp

# Reward Livello
tellraw @s ["",{"text":"⭐ HAI RAGGIUNTO IL LIVELLO SCAVO ","color":"gold"},{"score":{"name":"@s","objective":"mt_lvl_mining"},"color":"white"},{"text":"! ⭐","color":"gold"}]
playsound minecraft:entity.player.levelup master @s ~ ~ ~ 1 1
