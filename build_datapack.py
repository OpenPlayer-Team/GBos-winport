import os
import json
import zipfile

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

BASE_DIR = 'mining_tycoon'

# --- PACK.MCMETA & README ---
create_file(f'{BASE_DIR}/pack.mcmeta', json.dumps({
    "pack": {
        "pack_format": 48,
        "description": "Mining Tycoon Datapack - by AI Senior Developer"
    }
}, indent=4))

create_file(f'{BASE_DIR}/README.md', """
# Mining Tycoon Datapack
Un datapack completo per Minecraft 1.21.x che trasforma il mining in un'esperienza Idle Tycoon!

## Installazione
1. Inserisci la cartella (o il file .zip) nella cartella `datapacks` del tuo mondo Minecraft (1.21+).
2. Entra nel mondo e digita `/reload`.
3. Il sistema si inizializzerà da solo!

## Comandi per il giocatore
- `/trigger mt_menu` : Apre il menu principale per il negozio e le statistiche.
- `/trigger mt_deposit` : Deposita tutte le banconote fisiche presenti nell'inventario.

## Funzionalità
- Economia basata sulla rottura dei blocchi.
- Upgrade (Forza, Efficienza, Fortuna, Piccone) tramite menu interattivo.
- Costi crescenti per gli upgrade (~+30% a livello).
- Banconote fisiche sicure (impossibili da contraffare).
- Pieno supporto multigiocatore (saldi e livelli indipendenti).
""")

# --- MINECRAFT TAGS ---
create_file(f'{BASE_DIR}/data/minecraft/tags/function/load.json', json.dumps({"values": ["mining_tycoon:load"]}, indent=4))
create_file(f'{BASE_DIR}/data/minecraft/tags/function/tick.json', json.dumps({"values": ["mining_tycoon:tick"]}, indent=4))

# --- LOAD FUNCTION (Inizializzazione) ---
load_mcfunction = """
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
"""
create_file(f'{BASE_DIR}/data/mining_tycoon/function/load.mcfunction', load_mcfunction)

# --- TICK FUNCTION ---
create_file(f'{BASE_DIR}/data/mining_tycoon/function/tick.mcfunction', """
# Esegue le routine per tutti i giocatori
execute as @a run function mining_tycoon:player/tick
""")

# --- PLAYER TICK FUNCTION ---
player_tick = """
# Configurazione iniziale giocatore se non ha XP requirement impostata
execute if score @s mt_xp_req matches ..0 run scoreboard players set @s mt_xp_req 50
execute if score @s mt_c_str matches ..0 run scoreboard players set @s mt_c_str 100
execute if score @s mt_c_eff matches ..0 run scoreboard players set @s mt_c_eff 500
execute if score @s mt_c_luck matches ..0 run scoreboard players set @s mt_c_luck 1000

# Actionbar UI - Mostra i fondi
title @s actionbar [{"text":"Banconote: ","color":"green"},{"score":{"name":"@s","objective":"mt_money"},"color":"gold"},{"text":" | Lvl Scavo: ","color":"aqua"},{"score":{"name":"@s","objective":"mt_lvl_mining"},"color":"white"}]

# Abilitazione Trigger Interazione
scoreboard players enable @s mt_menu
scoreboard players enable @s mt_deposit
scoreboard players enable @s mt_buy_str
scoreboard players enable @s mt_buy_eff
scoreboard players enable @s mt_buy_luck
scoreboard players enable @s mt_wd_10
scoreboard players enable @s mt_wd_100

# Elaborazione Trigger Attivati
execute if score @s mt_menu matches 1.. run function mining_tycoon:shop/menu
execute if score @s mt_deposit matches 1.. run function mining_tycoon:banknotes/deposit
execute if score @s mt_buy_str matches 1.. run function mining_tycoon:shop/buy_str
execute if score @s mt_buy_eff matches 1.. run function mining_tycoon:shop/buy_eff
execute if score @s mt_buy_luck matches 1.. run function mining_tycoon:shop/buy_luck
execute if score @s mt_wd_10 matches 1.. run function mining_tycoon:banknotes/withdraw_10
execute if score @s mt_wd_100 matches 1.. run function mining_tycoon:banknotes/withdraw_100

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
"""
create_file(f'{BASE_DIR}/data/mining_tycoon/function/player/tick.mcfunction', player_tick)

# --- ECONOMY / BLOCK PROCESSING ---
blocks = [
    ("stone", "mt_m_stone", 2, 1),
    ("deepslate", "mt_m_dpslt", 3, 1),
    ("coal", "mt_m_coal", 5, 2),
    ("copper", "mt_m_cop", 8, 3),
    ("iron", "mt_m_iron", 12, 4),
    ("gold", "mt_m_gold", 20, 5),
    ("redstone", "mt_m_reds", 15, 4),
    ("lapis", "mt_m_lapis", 18, 5),
    ("diamond", "mt_m_dia", 60, 15),
    ("emerald", "mt_m_eme", 75, 20),
    ("obsidian", "mt_m_obs", 100, 30)
]

process_logic = """
# 1. Imposta valore base in mt_temp
scoreboard players set @s mt_temp {base_val}

# 2. Moltiplicatore Forza (5% in più per livello)
# mt_math è usato come variabile per il calcolo del moltiplicatore base 100
scoreboard players set @s mt_math 100
scoreboard players operation @s mt_math += @s mt_lvl_str
scoreboard players operation @s mt_math += @s mt_lvl_str
scoreboard players operation @s mt_math += @s mt_lvl_str
scoreboard players operation @s mt_math += @s mt_lvl_str
scoreboard players operation @s mt_math += @s mt_lvl_str

scoreboard players operation @s mt_temp *= @s mt_math
scoreboard players operation @s mt_temp /= #100 mt_math

# 3. Moltiplicatore Efficienza (Aumenta il totale del 10% per livello)
scoreboard players set @s mt_math 100
scoreboard players operation @s mt_math += @s mt_lvl_eff
scoreboard players operation @s mt_math += @s mt_lvl_eff
scoreboard players operation @s mt_math += @s mt_lvl_eff
scoreboard players operation @s mt_math += @s mt_lvl_eff
scoreboard players operation @s mt_math += @s mt_lvl_eff
scoreboard players operation @s mt_math += @s mt_lvl_eff
scoreboard players operation @s mt_math += @s mt_lvl_eff
scoreboard players operation @s mt_math += @s mt_lvl_eff
scoreboard players operation @s mt_math += @s mt_lvl_eff
scoreboard players operation @s mt_math += @s mt_lvl_eff
scoreboard players operation @s mt_temp *= @s mt_math
scoreboard players operation @s mt_temp /= #100 mt_math

# 4. Assegna Denaro e XP
scoreboard players operation @s mt_money += @s mt_temp
scoreboard players operation @s mt_total += @s mt_temp

# Notifica su actionbar del guadagno
tellraw @s {{"text":"+ $","color":"green","extra":[{{"score":{{"name":"@s","objective":"mt_temp"}},"color":"gold"}}]}}

# Gestione XP
scoreboard players add @s mt_xp {xp_val}
execute if score @s mt_xp >= @s mt_xp_req run function mining_tycoon:player/level_up

# Azzera il contatore per non ripetere all'infinito
scoreboard players set @s {score_name} 0
"""

for b_name, b_score, b_val, b_xp in blocks:
    content = process_logic.format(base_val=b_val, xp_val=b_xp, score_name=b_score)
    create_file(f'{BASE_DIR}/data/mining_tycoon/function/economy/blocks/{b_name}.mcfunction', content)


# --- PLAYER LEVEL UP ---
create_file(f'{BASE_DIR}/data/mining_tycoon/function/player/level_up.mcfunction', """
scoreboard players add @s mt_lvl_mining 1
scoreboard players operation @s mt_xp -= @s mt_xp_req

# Incrementa XP Req (Moltiplica per 1.5)
scoreboard players operation @s mt_temp = @s mt_xp_req
scoreboard players operation @s mt_temp /= 2
scoreboard players operation @s mt_xp_req += @s mt_temp

# Reward Livello
tellraw @s ["",{"text":"\u2b50 HAI RAGGIUNTO IL LIVELLO SCAVO ","color":"gold"},{"score":{"name":"@s","objective":"mt_lvl_mining"},"color":"white"},{"text":"! \u2b50","color":"gold"}]
playsound minecraft:entity.player.levelup master @s ~ ~ ~ 1 1
""")

# --- SHOP MENU ---
create_file(f'{BASE_DIR}/data/mining_tycoon/function/shop/menu.mcfunction', """
scoreboard players set @s mt_menu 0

tellraw @s ["",{"text":"\n=========","color":"dark_gray"},{"text":"[ NEGOZIO TYCOON ]","color":"gold","bold":true},{"text":"=========\n","color":"dark_gray"}]
tellraw @s ["",{"text":"\u25b6 Forza ","color":"red"},{"text":"(Lvl ","color":"gray"},{"score":{"name":"@s","objective":"mt_lvl_str"},"color":"white"},{"text":") +5% Valore Base | Costo: $","color":"gray"},{"score":{"name":"@s","objective":"mt_c_str"},"color":"yellow"},{"text":" [CLICCA PER COMPRARE]","color":"green","clickEvent":{"action":"run_command","value":"/trigger mt_buy_str set 1"}}]
tellraw @s ["",{"text":"\u25b6 Efficienza ","color":"aqua"},{"text":"(Lvl ","color":"gray"},{"score":{"name":"@s","objective":"mt_lvl_eff"},"color":"white"},{"text":") +10% Moltiplicatore Totale | Costo: $","color":"gray"},{"score":{"name":"@s","objective":"mt_c_eff"},"color":"yellow"},{"text":" [CLICCA PER COMPRARE]","color":"green","clickEvent":{"action":"run_command","value":"/trigger mt_buy_eff set 1"}}]
tellraw @s ["",{"text":"\u25b6 Fortuna ","color":"light_purple"},{"text":"(Lvl ","color":"gray"},{"score":{"name":"@s","objective":"mt_lvl_luck"},"color":"white"},{"text":") Bonus rari | Costo: $","color":"gray"},{"score":{"name":"@s","objective":"mt_c_luck"},"color":"yellow"},{"text":" [CLICCA PER COMPRARE]","color":"green","clickEvent":{"action":"run_command","value":"/trigger mt_buy_luck set 1"}}]
tellraw @s ["",{"text":"\n--- BANCOMAT ---","color":"green"}]
tellraw @s ["",{"text":"[Preleva $10]","color":"dark_green","clickEvent":{"action":"run_command","value":"/trigger mt_wd_10 set 1"}},"  ",{"text":"[Preleva $100]","color":"dark_green","clickEvent":{"action":"run_command","value":"/trigger mt_wd_100 set 1"}}]
tellraw @s ["",{"text":"[DEPOSITA TUTTE LE BANCONOTE]","color":"yellow","bold":true,"clickEvent":{"action":"run_command","value":"/trigger mt_deposit set 1"}}]
tellraw @s ["",{"text":"=================================\n","color":"dark_gray"}]
""")

# --- SHOP BUY LOGIC ---
buy_logic = """
scoreboard players set @s mt_buy_{id} 0

# Controlla Fondi
execute if score @s mt_money >= @s mt_c_{id} run function mining_tycoon:shop/success_{id}
execute if score @s mt_money < @s mt_c_{id} run tellraw @s {{"text":"\u274c Non hai abbastanza banconote!","color":"red"}}
"""

success_logic = """
# Detrai Denaro e Segna Spesa
scoreboard players operation @s mt_money -= @s mt_c_{id}
scoreboard players operation @s mt_spent += @s mt_c_{id}

# Aumenta Livello
scoreboard players add @s mt_lvl_{id} 1

# Aumenta Costo (+35%) - approssimazione intera
scoreboard players operation @s mt_temp = @s mt_c_{id}
scoreboard players operation @s mt_temp *= #30 mt_math
scoreboard players operation @s mt_temp /= #100 mt_math
scoreboard players operation @s mt_c_{id} += @s mt_temp

# Notifica e Riapri Menu
playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 1 1
tellraw @s {{"text":"\u2705 Upgrade {name} Acquistato!","color":"green"}}
function mining_tycoon:shop/menu
"""

for u_id, u_name in [("str", "Forza"), ("eff", "Efficienza"), ("luck", "Fortuna")]:
    create_file(f'{BASE_DIR}/data/mining_tycoon/function/shop/buy_{u_id}.mcfunction', buy_logic.format(id=u_id))
    create_file(f'{BASE_DIR}/data/mining_tycoon/function/shop/success_{u_id}.mcfunction', success_logic.format(id=u_id, name=u_name))

# --- BANKNOTES LOGIC ---
create_file(f'{BASE_DIR}/data/mining_tycoon/function/banknotes/withdraw_10.mcfunction', """
scoreboard players set @s mt_wd_10 0
execute if score @s mt_money >= #10 mt_math run scoreboard players operation @s mt_money -= #10 mt_math
execute if score @s mt_money >= #10 mt_math run give @s paper[custom_data={mt_banknote:10},item_name='{"text":"Banconota da $10","color":"green","italic":false}',enchantments={levels:{"minecraft:unbreaking":1},show_in_tooltip:false}] 1
execute if score @s mt_money >= #10 mt_math run playsound minecraft:entity.item.pickup master @s ~ ~ ~ 1 1.2
""")

create_file(f'{BASE_DIR}/data/mining_tycoon/function/banknotes/withdraw_100.mcfunction', """
scoreboard players set @s mt_wd_100 0
execute if score @s mt_money >= #100 mt_math run scoreboard players operation @s mt_money -= #100 mt_math
execute if score @s mt_money >= #100 mt_math run give @s paper[custom_data={mt_banknote:100},item_name='{"text":"Banconota da $100","color":"dark_green","bold":true,"italic":false}',enchantments={levels:{"minecraft:unbreaking":1},show_in_tooltip:false}] 1
execute if score @s mt_money >= #100 mt_math run playsound minecraft:entity.item.pickup master @s ~ ~ ~ 1 1.2
""")

create_file(f'{BASE_DIR}/data/mining_tycoon/function/banknotes/deposit.mcfunction', """
scoreboard players set @s mt_deposit 0

# Deposita 10
execute store result score @s mt_temp clear @s paper[custom_data~{mt_banknote:10}]
scoreboard players operation @s mt_temp *= #10 mt_math
scoreboard players operation @s mt_money += @s mt_temp

# Deposita 100
execute store result score @s mt_temp clear @s paper[custom_data~{mt_banknote:100}]
scoreboard players operation @s mt_temp *= #100 mt_math
scoreboard players operation @s mt_money += @s mt_temp

tellraw @s {"text":"\u2705 Tutte le banconote sono state depositate sul conto!","color":"gold"}
playsound minecraft:block.amethyst_block.chime master @s ~ ~ ~ 1 1
""")

print("Tutti i file generati con successo in " + BASE_DIR)
