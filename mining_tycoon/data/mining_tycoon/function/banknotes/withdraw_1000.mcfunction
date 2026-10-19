scoreboard players set @s mt_wd_1000 0
execute if score @s mt_money >= #1000 mt_math run give @s paper[custom_data={mt_banknote:1000},item_name='{"text":"Banconota da $1000","color":"aqua","bold":true,"italic":false}',enchantments={levels:{"minecraft:unbreaking":1},show_in_tooltip:false}] 1
execute if score @s mt_money >= #1000 mt_math run scoreboard players operation @s mt_money -= #1000 mt_math
execute if score @s mt_money >= #1000 mt_math run playsound minecraft:entity.item.pickup master @s ~ ~ ~ 1 1.2
