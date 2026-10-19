# Detrai Denaro e Segna Spesa
scoreboard players operation @s mt_money -= @s mt_c_luck
scoreboard players operation @s mt_spent += @s mt_c_luck

# Aumenta Livello
scoreboard players add @s mt_lvl_luck 1

# Aumenta Costo (+35%) - approssimazione intera
scoreboard players operation @s mt_temp = @s mt_c_luck
scoreboard players operation @s mt_temp *= #30 mt_math
scoreboard players operation @s mt_temp /= #100 mt_math
scoreboard players operation @s mt_c_luck += @s mt_temp

# Notifica e Riapri Menu
playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 1 1
tellraw @s {"text":"✅ Upgrade Fortuna Acquistato!","color":"green"}
function mining_tycoon:shop/menu
