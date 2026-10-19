# Detrai Denaro e Segna Spesa
scoreboard players operation @s mt_money -= @s mt_c_eff
scoreboard players operation @s mt_spent += @s mt_c_eff

# Aumenta Livello
scoreboard players add @s mt_lvl_eff 1

# Aumenta Costo (+35%) - approssimazione intera
scoreboard players operation @s mt_temp = @s mt_c_eff
scoreboard players operation @s mt_temp *= #30 mt_math
scoreboard players operation @s mt_temp /= #100 mt_math
scoreboard players operation @s mt_c_eff += @s mt_temp

# Notifica e Riapri Menu
playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 1 1
tellraw @s {"text":"✅ Upgrade Efficienza Acquistato!","color":"green"}
function mining_tycoon:shop/menu
