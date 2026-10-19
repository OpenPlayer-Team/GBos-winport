scoreboard players set @s mt_buy_eff 0

# Controlla Fondi
execute if score @s mt_money >= @s mt_c_eff run function mining_tycoon:shop/success_eff
execute if score @s mt_money < @s mt_c_eff run tellraw @s {"text":"❌ Non hai abbastanza banconote!","color":"red"}
