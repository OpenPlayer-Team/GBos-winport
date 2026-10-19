scoreboard players set @s mt_buy_luck 0

# Controlla Fondi
execute if score @s mt_money >= @s mt_c_luck run function mining_tycoon:shop/success_luck
execute if score @s mt_money < @s mt_c_luck run tellraw @s {"text":"❌ Non hai abbastanza banconote!","color":"red"}
