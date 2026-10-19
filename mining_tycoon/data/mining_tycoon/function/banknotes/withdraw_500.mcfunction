scoreboard players set @s mt_wd_500 0
execute if score @s mt_money >= #500 mt_math run give @s paper[custom_data={mt_banknote:500},item_name='{"text":"Banconota da $500","color":"light_purple","bold":true,"italic":false}',enchantments={levels:{"minecraft:unbreaking":1},show_in_tooltip:false}] 1
execute if score @s mt_money >= #500 mt_math run scoreboard players operation @s mt_money -= #500 mt_math
execute if score @s mt_money >= #500 mt_math run playsound minecraft:entity.item.pickup master @s ~ ~ ~ 1 1.2
