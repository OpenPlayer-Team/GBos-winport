scoreboard players set @s mt_prestige_t 0

tellraw @s ["",{"text":"\n=========","color":"dark_gray"},{"text":"[ PRESTIGIO ]","color":"light_purple","bold":true},{"text":"=========\n","color":"dark_gray"}]
tellraw @s ["",{"text":"Il Prestigio azzera i tuoi Livelli, Upgrade e Denaro per darti un ","color":"white"},{"text":"moltiplicatore permanente x2","color":"gold","bold":true},{"text":"!\n","color":"white"}]
tellraw @s ["",{"text":"Requisito: Livello Scavo 100\n","color":"red"}]
tellraw @s ["",{"text":"[ESEGUI PRESTIGIO]","color":"dark_red","bold":true,"clickEvent":{"action":"run_command","value":"/trigger mt_do_prestige set 1"}}]
tellraw @s ["",{"text":"\n[TORNA AL NEGOZIO]","color":"yellow","clickEvent":{"action":"run_command","value":"/trigger mt_menu set 1"}}]
tellraw @s ["",{"text":"=================================\n","color":"dark_gray"}]
