# Configurazione iniziale giocatore se non ha XP requirement impostata
execute if score @s mt_xp_req matches ..0 run scoreboard players set @s mt_xp_req 50
execute if score @s mt_c_str matches ..0 run scoreboard players set @s mt_c_str 100
execute if score @s mt_c_eff matches ..0 run scoreboard players set @s mt_c_eff 500
execute if score @s mt_c_luck matches ..0 run scoreboard players set @s mt_c_luck 1000

# Actionbar UI - Mostra i fondi
title @s actionbar [{"text":"Banconote: ","color":"green"},{"score":{"name":"@s","objective":"mt_money"},"color":"gold"},{"text":" | Lvl Scavo: ","color":"aqua"},{"score":{"name":"@s","objective":"mt_lvl_mining"},"color":"white"}]

# Abilitazione Trigger Interazione
scoreboard players enable @s mt_prestige_t
scoreboard players enable @s mt_do_prestige
scoreboard players enable @s mt_menu
scoreboard players enable @s mt_deposit
scoreboard players enable @s mt_buy_str
scoreboard players enable @s mt_buy_eff
scoreboard players enable @s mt_buy_luck
scoreboard players enable @s mt_wd_10
scoreboard players enable @s mt_wd_100
scoreboard players enable @s mt_wd_50
scoreboard players enable @s mt_wd_500
scoreboard players enable @s mt_wd_1000

# Elaborazione Trigger Attivati
execute if score @s mt_prestige_t matches 1.. run function mining_tycoon:prestige/menu
execute if score @s mt_do_prestige matches 1.. run function mining_tycoon:prestige/do_prestige
execute if score @s mt_menu matches 1.. run function mining_tycoon:shop/menu
execute if score @s mt_deposit matches 1.. run function mining_tycoon:banknotes/deposit
execute if score @s mt_buy_str matches 1.. run function mining_tycoon:shop/buy_str
execute if score @s mt_buy_eff matches 1.. run function mining_tycoon:shop/buy_eff
execute if score @s mt_buy_luck matches 1.. run function mining_tycoon:shop/buy_luck
execute if score @s mt_wd_10 matches 1.. run function mining_tycoon:banknotes/withdraw_10
execute if score @s mt_wd_100 matches 1.. run function mining_tycoon:banknotes/withdraw_100
execute if score @s mt_wd_50 matches 1.. run function mining_tycoon:banknotes/withdraw_50
execute if score @s mt_wd_500 matches 1.. run function mining_tycoon:banknotes/withdraw_500
execute if score @s mt_wd_1000 matches 1.. run function mining_tycoon:banknotes/withdraw_1000

# Controlli rottura blocchi (Richiama gli script dedicati)
execute if score @s mt_m_stone matches 1.. run function mining_tycoon:economy/blocks/stone
execute if score @s mt_m_dpslt matches 1.. run function mining_tycoon:economy/blocks/deepslate
execute if score @s mt_m_coal matches 1.. run function mining_tycoon:economy/blocks/coal
execute if score @s mt_m_cop matches 1.. run function mining_tycoon:economy/blocks/copper
execute if score @s mt_m_iron matches 1.. run function mining_tycoon:economy/blocks/iron
execute if score @s mt_m_gold matches 1.. run function mining_tycoon:economy/blocks/gold
execute if score @s mt_m_reds matches 1.. run function mining_tycoon:economy/blocks/redstone
execute if score @s mt_m_lapis matches 1.. run function mining_tycoon:economy/blocks/lapis
execute if score @s mt_m_dia matches 1.. run function mining_tycoon:economy/blocks/diamond
execute if score @s mt_m_eme matches 1.. run function mining_tycoon:economy/blocks/emerald
execute if score @s mt_m_obs matches 1.. run function mining_tycoon:economy/blocks/obsidian
execute if score @s mt_prestige_mul matches ..0 run scoreboard players set @s mt_prestige_mul 1

execute if score @s mt_m_d_coal matches 1.. run function mining_tycoon:economy/blocks/coal
execute if score @s mt_m_d_cop matches 1.. run function mining_tycoon:economy/blocks/copper
execute if score @s mt_m_d_iron matches 1.. run function mining_tycoon:economy/blocks/iron
execute if score @s mt_m_d_gold matches 1.. run function mining_tycoon:economy/blocks/gold
execute if score @s mt_m_d_reds matches 1.. run function mining_tycoon:economy/blocks/redstone
execute if score @s mt_m_d_lapis matches 1.. run function mining_tycoon:economy/blocks/lapis
execute if score @s mt_m_d_dia matches 1.. run function mining_tycoon:economy/blocks/diamond
execute if score @s mt_m_d_eme matches 1.. run function mining_tycoon:economy/blocks/emerald
