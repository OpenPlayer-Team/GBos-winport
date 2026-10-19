scoreboard players set @s mt_do_prestige 0

execute if score @s mt_lvl_mining matches 100.. run function mining_tycoon:prestige/success
execute if score @s mt_lvl_mining matches ..99 run tellraw @s {"text":"❌ Devi essere almeno Livello Scavo 100 per eseguire il Prestigio!","color":"red"}
