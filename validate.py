import os
import glob
import re

def validate():
    print("Inizio Validazione...")

    # 1. Controlla che in load ci siano tutte le variabili
    with open('mining_tycoon/data/mining_tycoon/function/load.mcfunction', 'r') as f:
        load_content = f.read()

    required_objectives = [
        'mt_money', 'mt_total', 'mt_spent', 'mt_m_stone', 'mt_m_dpslt', 'mt_m_coal',
        'mt_xp', 'mt_xp_req', 'mt_lvl_mining', 'mt_lvl_str', 'mt_lvl_eff', 'mt_lvl_luck',
        'mt_c_str', 'mt_c_eff', 'mt_c_luck', 'mt_menu', 'mt_deposit', 'mt_buy_str',
        'mt_temp', 'mt_math', 'mt_wd_10', 'mt_wd_100', 'mt_wd_50', 'mt_wd_500', 'mt_wd_1000',
        'mt_prestige_mul', 'mt_prestige_t', 'mt_do_prestige'
    ]

    for obj in required_objectives:
        if obj not in load_content:
            print(f"ERRORE: Obiettivo {obj} non trovato in load.mcfunction")
            return False

    # 2. Sintassi mcfunction di base
    files = glob.glob('mining_tycoon/data/**/*.mcfunction', recursive=True)
    for fpath in files:
        with open(fpath, 'r') as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '{' in line and '}' not in line:
                print(f"AVVISO (Possibile Errore JSON): in {fpath}:{i+1} -> {line}")

    print("Validazione completata con successo. Nessun errore critico trovato.")
    return True

validate()
