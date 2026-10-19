scoreboard players set @s mt_buy_str 0

# Controlla Fondi
execute if score @s mt_money >= @s mt_c_str run function mining_tycoon:shop/success_str
execute if score @s mt_money < @s mt_c_str run tellraw @s {"text":"❌ Non hai abbastanza banconote!","color":"red"}
