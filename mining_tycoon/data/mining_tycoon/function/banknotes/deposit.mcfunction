scoreboard players set @s mt_deposit 0

# Deposita 10
execute store result score @s mt_temp clear @s paper[custom_data~{mt_banknote:10}]
scoreboard players operation @s mt_temp *= #10 mt_math
scoreboard players operation @s mt_money += @s mt_temp

# Deposita 50
execute store result score @s mt_temp clear @s paper[custom_data~{mt_banknote:50}]
scoreboard players operation @s mt_temp *= #50 mt_math
scoreboard players operation @s mt_money += @s mt_temp

# Deposita 100
execute store result score @s mt_temp clear @s paper[custom_data~{mt_banknote:100}]
scoreboard players operation @s mt_temp *= #100 mt_math
scoreboard players operation @s mt_money += @s mt_temp

# Deposita 500
execute store result score @s mt_temp clear @s paper[custom_data~{mt_banknote:500}]
scoreboard players operation @s mt_temp *= #500 mt_math
scoreboard players operation @s mt_money += @s mt_temp

# Deposita 1000
execute store result score @s mt_temp clear @s paper[custom_data~{mt_banknote:1000}]
scoreboard players operation @s mt_temp *= #1000 mt_math
scoreboard players operation @s mt_money += @s mt_temp

tellraw @s {"text":"✅ Tutte le banconote sono state depositate sul conto!","color":"gold"}
playsound minecraft:block.amethyst_block.chime master @s ~ ~ ~ 1 1
