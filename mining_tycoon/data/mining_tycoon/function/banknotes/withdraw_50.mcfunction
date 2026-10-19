scoreboard players set @s mt_wd_50 0
execute if score @s mt_money >= #50 mt_math run give @s paper[custom_data={mt_banknote:50},item_name='{"text":"Banconota da $50","color":"yellow","italic":false}',enchantments={levels:{"minecraft:unbreaking":1},show_in_tooltip:false}] 1
execute if score @s mt_money >= #50 mt_math run scoreboard players operation @s mt_money -= #50 mt_math
execute if score @s mt_money >= #50 mt_math run playsound minecraft:entity.item.pickup master @s ~ ~ ~ 1 1.2
