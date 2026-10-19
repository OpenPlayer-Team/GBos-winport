# Inizializzazione Scoreboard Economia
scoreboard objectives add mt_money dummy "Banconote"
scoreboard objectives add mt_total dummy "Guadagni Totali"
scoreboard objectives add mt_spent dummy "Denaro Speso"

# Inizializzazione Statistiche Mining
scoreboard objectives add mt_m_stone minecraft.mined:minecraft.stone
scoreboard objectives add mt_m_dpslt minecraft.mined:minecraft.deepslate
scoreboard objectives add mt_m_coal minecraft.mined:minecraft.coal_ore
scoreboard objectives add mt_m_cop minecraft.mined:minecraft.copper_ore
scoreboard objectives add mt_m_iron minecraft.mined:minecraft.iron_ore
scoreboard objectives add mt_m_gold minecraft.mined:minecraft.gold_ore
scoreboard objectives add mt_m_reds minecraft.mined:minecraft.redstone_ore
scoreboard objectives add mt_m_lapis minecraft.mined:minecraft.lapis_ore
scoreboard objectives add mt_m_dia minecraft.mined:minecraft.diamond_ore
scoreboard objectives add mt_m_eme minecraft.mined:minecraft.emerald_ore
scoreboard objectives add mt_m_obs minecraft.mined:minecraft.obsidian

# Abilità e XP
scoreboard objectives add mt_xp dummy "Esperienza"
scoreboard objectives add mt_xp_req dummy "XP Richiesta"
scoreboard objectives add mt_lvl_mining dummy "Livello Minatore"
scoreboard objectives add mt_lvl_str dummy "Livello Forza"
scoreboard objectives add mt_lvl_eff dummy "Livello Efficienza"
scoreboard objectives add mt_lvl_luck dummy "Livello Fortuna"

# Costi Upgrade
scoreboard objectives add mt_c_str dummy "Costo Forza"
scoreboard objectives add mt_c_eff dummy "Costo Efficienza"
scoreboard objectives add mt_c_luck dummy "Costo Fortuna"

# Triggers per l'interazione dei giocatori non-admin
scoreboard objectives add mt_menu trigger
scoreboard objectives add mt_deposit trigger
scoreboard objectives add mt_buy_str trigger
scoreboard objectives add mt_buy_eff trigger
scoreboard objectives add mt_buy_luck trigger
scoreboard objectives add mt_wd_10 trigger
scoreboard objectives add mt_wd_100 trigger

# Variabili Temporanee e Costanti
scoreboard objectives add mt_temp dummy
scoreboard objectives add mt_math dummy
scoreboard players set #100 mt_math 100
scoreboard players set #30 mt_math 30

tellraw @a {"text":"[Mining Tycoon] Datapack Caricato con Successo!","color":"green","bold":true}
scoreboard players set #2 mt_math 2
scoreboard objectives add mt_wd_50 trigger
scoreboard objectives add mt_wd_500 trigger
scoreboard objectives add mt_wd_1000 trigger
scoreboard players set #50 mt_math 50
scoreboard players set #500 mt_math 500
scoreboard players set #1000 mt_math 1000
scoreboard objectives add mt_prestige_mul dummy "Prestigio"
scoreboard objectives add mt_prestige_t trigger
scoreboard objectives add mt_do_prestige trigger
scoreboard players set #1 mt_math 1

# Deepslate Variants
scoreboard objectives add mt_m_d_coal minecraft.mined:minecraft.deepslate_coal_ore
scoreboard objectives add mt_m_d_cop minecraft.mined:minecraft.deepslate_copper_ore
scoreboard objectives add mt_m_d_iron minecraft.mined:minecraft.deepslate_iron_ore
scoreboard objectives add mt_m_d_gold minecraft.mined:minecraft.deepslate_gold_ore
scoreboard objectives add mt_m_d_reds minecraft.mined:minecraft.deepslate_redstone_ore
scoreboard objectives add mt_m_d_lapis minecraft.mined:minecraft.deepslate_lapis_ore
scoreboard objectives add mt_m_d_dia minecraft.mined:minecraft.deepslate_diamond_ore
scoreboard objectives add mt_m_d_eme minecraft.mined:minecraft.deepslate_emerald_ore
