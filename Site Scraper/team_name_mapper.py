import json

get_month = {
    'January': '01',
    'February': '02',
    'March': '03',
    'April': '04',
    'May': '05',
    'June': '06',
    'July': '07',
    'August': '08',
    'September': '09',
    'October': '10',
    'November': '11',
    'December': '12'
}

get_lck_name = {
    # 2022
    'gen': 'Gen.G',
    't1': 'T1',
    'drx': 'DRX',
    'lsb': 'Liiv SANDBOX',
    'dk': 'DWG KIA',
    'kdf': 'Kwangdong Freecs',
    'kt': 'KT Rolster',
    'ns': 'Nongshim RedForce',
    'hle': 'Hanwha Life Esports',
    'bro': 'Fredit BRION',

    # 2021
    # 'drx': 'DRX',
    # 'ns': 'Nongshim RedForce',
    # 'gen': 'Gen.G',
    # 'lsb': 'Liiv SANDBOX',
    # 't1': 'T1',
    # 'kt': 'KT Rolster',
    # 'dk': 'DWG KIA',
    # 'hle': 'Hanwha Life Esports',
    # 'af': 'Afreeca Freecs',
    # 'bto': '⁠Fredit BRION'
}

get_lec_name = {
    # 2022
    'xl': 'Excel Esports',
    'fnc': 'Fnatic',
    'rge': 'Rogue',
    'g2': 'G2 Esports',
    'mad': 'MAD Lions',
    'vit': 'Team Vitality',
    'ast': 'Astralis',
    'msf': 'Misfits Gaming',
    'sk': 'SK Gaming',
    'bds': 'Team BDS',

    # 2021
    # 'msf': 'Misfits Gaming',
    # 'xl': 'Excel Esports',
    # 'rge': 'Rogue',
    # 'vit': 'Team Vitality',
    # 'fnc': 'Fnatic',
    # 'ast': 'Astralis',
    # 'g2': 'G2 Esports',
    # 'sk': 'SK Gaming',
    # 's04': 'FC Schalke 04',
    # 'mad': 'MAD Lions'
}

get_lvp_name = {
    # 2022
    'hrts': 'Team Heretics',
    'fntq': 'Fnatic TQ',
    'bso': 'BISONS ECLUB',
    'g2ar': 'G2 Arctic',
    'gia': 'Giants',
    'bar': 'Barça eSports',
    'koi': 'KOI',
    'madm': 'MAD Lions Madrid',
    'ucam': 'UCAM Tokiers',
    'mrs': 'Movistar Riders',

    # 2021
    # 'bts': 'Cream Real Betis',
    # 'emz': 'eMonkeyz',
    # 'mrs': 'Movistar Riders',
    # 'g2ar': 'G2 Arctic',
    # 'vgia': 'Vodafone Giants',
    # 'madm': 'MAD Lions Madrid',
    # 'bcn': 'BCN Squad',
    # 's2v': 'S2V Esports',
    # 'ucam': 'UCAM Esports Club',
    # 'tq': 'Team Queso'
}

get_lco_name = {
    # 2022
    'chf': 'Chiefs Esports Club',
    'dw': 'Dire Wolves',
    'ord': 'ORDER',
    'pce': 'PEACE',
    'pgg': 'Pentanet.GG',
    'kng': 'Kanga Esports',
    'mec': 'MAMMOTH',
    'grv': 'Gravitas',

    # 2021
    # 'lgc': 'Legacy',
    # 'grv': 'Gravitas',
    # 'mmm': 'MAMMOTH',
    # 'pgg': 'Pentanet.GG',
    # 'pce': '⁠PEACE',
    # 'ord': 'ORDER',
    # 'dw': 'Dire Wolves',
    # 'chf': 'Chiefs Esports Club'
}

get_lfl_name = {
    # 2022
    'ldlc': 'LDLC OL',
    'gw': 'GameWard',
    'vitb': 'Vitality.Bee',
    'kc': 'Karmine Corp',
    'msfp': 'Misfits Premier',
    'bds.a': 'Team BDS Academy',
    'go': 'Team GO',
    'sly': 'Solary',
    'opl': 'Team Oplon',
    'me': 'Mirage Elyandra',

    # 2021
    # 'msfp': 'Misfits Premier',
    # 'sly': 'Solary',
    # 'ldlc': 'LDLC OL',
    # 'mces': 'Team MCES',
    # 'go': 'GamersOrigin',
    # 'gw': 'GameWard',
    # 'izi': 'Izi Dream',
    # 'vitb': 'Vitality.Bee'
}

get_pcs_name = {
    # 2022
    'byg': 'Beyond Gaming',
    'jt': 'J Team',
    'cfo': 'CTBC Flying Oyster',
    'psg': 'PSG Talon',
    'dcg': 'Deep Cross Gaming',
    'fak': 'Frank Esports',
    'imp': 'Impunity',
    'mft': 'Meta Falcon Team',
    'dwt': 'Dewish Team',
    's9': 'SEM9',

    # 2021
    # 'hka': 'Hong Kong Attitude',
    # 'imp': '⁠Impunity',
    # 'alf': 'Alpha Esports',
    # 'jt': 'J Team',
    # 'bjd': 'Berjaya Dragons',
    # 'lyb': 'Liyab Esports',
    # 'mcx': 'Machi Esports',
    # 'byg': 'Beyond Gaming',
    # 'psg': 'PSG Talon',
    # 'bme': 'BOOM Esports'
}

get_lcs_name = {
    # 2022
    'Evil Geniuses.NA': 'eg',
    '100 Thieves': '100',
    'Team Liquid': 'tl',
    'Counter Logic Gaming': 'clg',
    'FlyQuest': 'fly',
    'Cloud9': 'c9',
    'Golden Guardians': 'gg',
    'Dignitas': 'dig',
    'TSM': 'tsm',
    'Immortals': 'imt',

    # 'eg': 'Evil Geniuses',
    # '100': '100 Thieves',
    # 'tl': 'Team Liquid',
    # 'clg': 'Counter Logic Gaming',
    # 'fly': 'FlyQuest',
    # 'c9': 'Cloud9',
    # 'gg': 'Golden Guardians',
    # 'dig': 'Dignitas',
    # 'tsm': 'Team SoloMid',
    # 'imt': 'Immortals',

    # 2021    
    # 'dig': 'Dignitas',
    # 'imt': 'Immortals',
    # 'eg': 'Evil Geniuses',
    # 'tl': 'Team Liquid',
    # 'clg': 'Counter Logic Gaming',
    # 'c9': 'Cloud9',
    # 'tsm': 'Team SoloMid',
    # 'gg': 'Golden Guardians',
    # '100': '100 Thieves',
    # 'fly': 'FlyQuest',
}

get_na_academy_league_name = {
    # 2022
    'tl.a': 'Team Liquid Academy',
    '100.a': '100 Thieves Academy',
    'dig.a': 'Dignitas Academy',
    'clg.a': 'Counter Logic Gaming Academy',
    'imt.a': 'Immortals Academy',
    'c9.a': 'Cloud9 Academy',
    'fly.a': 'FlyQuest Academy',
    'eg.a': 'Evil Geniuses Academy',
    'gg.a': 'Golden Guardians Academy',
    'tsm.a': 'Team SoloMid Academy',

    # 2021    
    # 'tl.a': 'Team Liquid Academy',
    # 'clg.a': 'Counter Logic Gaming Academy',
    # 'c9.a': 'Cloud9 Academy',
    # 'tsm.a': 'Team SoloMid Academy',
    # 'gg.a': 'Golden Guardians Academy',
    # 'eg.a': 'Evil Geniuses Academy',
    # '100.a': '100 Thieves Academy',
    # 'dig.a': 'Dignitas Academy',
    # 'fly.a': 'FlyQuest Academy',
    # 'imt.a': 'Immortals Academy'
}

get_lla_name = {
    # 2022
    'isg': 'Isurus',
    'est': 'Estral Esports',
    'ak': 'All Knights',
    'inf': 'Infinity Esports',
    'r7': 'Rainbow7',
    'aze': 'Team Aze',
    'xtn': 'XTEN Esports',
    'get': 'Globant Emerald',

    # 2021
    # 'isg': 'Isurus Gaming',
    # 'ak': 'All Knights',
    # 'fg': 'Furious Gaming',
    # 'inf': 'Infinity Esports',
    # 'r7': 'Rainbow7',
    # 'xtn': 'XTEN Esports',
    # 'klg': 'Kaos Latin Gamers',
    # 'est': 'Estral Esports'
}

get_ultraliga_name = {
    # 2022
    'rgo': 'AGO ROGUE',
    'ihg': 'Illuminar Gaming',
    'z10': 'Zero Tenacity',
    'gsk': 'Goskilla',
    'fsk': 'Forsaken',
    'wolf': 'Iron Wolves',
    'dv1': 'devils.one',
    'knf': 'Komil&Friends',
    'esca': 'Team ESCA Gaming',
    'ggm': "Gentlemen's Gaming",

    # 2021
    # 'rgo': 'AGO ROGUE',
    # 'teg': 'Team ESCA Gaming',
    # 'pdw': 'PDW',
    # 'ggm': "Gentlemen's Gaming",
    # 'ihg': 'Illuminar Gaming',
    # 'knf': '⁠Komil&Friends',
    # 'dv1': '⁠devils.one',
    # 'k1': 'K1CK'
}

get_lpl_name = {
    # 2022
    'v5': 'Victory Five',
    'jdg': 'JD Gaming',
    'tes': 'Top Esports',
    'edg': 'EDward Gaming',
    'rng': 'Royal Never Give Up',
    'lng': 'LNG Esports',
    'al': "Anyone's Legend",
    'omg': 'Oh My God',
    'wbg': 'Weibo Gaming',
    'fpx': 'FunPlus Phoenix',
    'up': 'Ultra Prime',
    'tt': 'ThunderTalk Gaming',
    'blg': 'Bilibili Gaming',
    'ra': 'Rare Atom',
    'lgd': 'LGD Gaming',
    'ig': 'Invictus Gaming',
    'we': 'Team WE',

    # 2021
    # 'fpx': 'FunPlus Phoenix',
    # 'tes': 'Top Esports',
    # 'rng': 'Royal Never Give Up',
    # 'blg': 'Bilibili Gaming',
    # 'sn': 'Suning',
    # 'edg': 'EDward Gaming',
    # 'ig': 'Invictus Gaming',
    # 'lng': 'LNG Esports',
    # 'we': 'Team WE',
    # 'jdg': 'JD Gaming',
    # 'ra': 'Rare Atom',
    # 'rw': 'Rogue Warriors',
    # 'v5': 'Victory Five',
    # 'lgd': 'LGD Gaming',
    # 'omg': 'Oh My God',
    # 'up': 'Ultra Prime',
    # 'tt': 'ThunderTalk Gaming'
}

get_ljl_name = {
    # 2022
    'sg': 'Sengoku Gaming',
    'dfm': 'DetonatioN FocusMe',
    'shg': 'Fukuoka SoftBank Hawks gaming',
    'bc': 'Burning Core',
    'cga': 'Crest Gaming Act',
    'rj': 'Rascal Jester',
    'axz': 'AXIZ',
    'v3': 'V3 Esports',

    # 2021
    # 'v3': 'V3 Esports',
    # 'sg': 'Sengoku Gaming',
    # 'cga': 'Crest Gaming Act',
    # 'dfm': 'DetonatioN FocusMe',
    # 'shg': 'Fukuoka SoftBank Hawks gaming',
    # 'axz': 'AXIZ',
    # 'bc': 'Burning Core',
    # 'rj': 'Rascal Jester'
}

get_tcl_name = {
    # 2022
    'nsr': 'NASR eSports Turkey',
    'dp': 'Dark Passage',
    'iw': 'İstanbul Wildcats',
    'gal': 'Galakticos',
    'smb': 'SuperMassive Blaze',
    'bjk': 'Beşiktaş Esports',
    'gs': 'Galatasaray Esports',
    'aur': 'Team AURORA',
    'fb': 'Fenerbahçe Esports',
    '5r': '5 Ronin',

    # 2021
    # 'bjk': 'Beşiktaş Esports',
    # 'dp': 'Dark Passage',
    # 'gal': 'Galakticos',
    # 'iw': 'İstanbul Wildcats',
    # 'fb': '1907 Fenerbahçe',
    # 'gs': 'Galatasaray Esports',
    # '5r': '5 Ronin',
    # 'smb': 'SuperMassive Blaze',
    # 'nsr': 'NASR eSports Turkey',
    # 'aur': 'Team AURORA'
}

get_vcs_name = { 
    # 2022
    'ces': 'CERBERUS Esports',
    'tw': 'Team Whales',
    'se': 'SBTC Esports',
    'ts': 'Team Secret',
    'gam': 'GAM Esports',
    'ge': 'Genius Esports',
    'ase': 'AS Esports',
    'sgb': 'Saigon Buffalo',

    # 2021
    # 'per': 'Percent Esports',
    # 'opg': 'OverPower Esports',
    # 'ces': 'CERBERUS Esports',
    # 'evs': 'EVOS Esports',
    # 'gam': 'GAM Esports',
    # 'ts': 'Team Secret',
    # 'sgb': 'Saigon Buffalo',
    # 'fl': 'Team Flash'
}

get_cblol_name = {
    # 2022
    'red': 'RED Canids',
    'fur': 'FURIA Esports',
    'png': 'paiN Gaming',
    'lll': 'LOUD',
    'kbm': 'KaBuM! e-Sports',
    'lbr': 'Liberty',
    'fla': 'Flamengo Los Grandes',
    'nmg': 'Miners',
    'itz': 'INTZ',
    'rns': 'Rensga Esports',

    # 2021
    # 'vrx': 'Vorax Liberty',
    # 'kbm': 'KaBuM! e-Sports',
    # 'png': 'paiN Gaming',
    # 'itz': 'INTZ',
    # 'fla': 'Flamengo eSports',
    # 'fur': 'FURIA Esports',
    # 'red': 'RED Canids',
    # 'rns': 'Rensga Esports',
    # 'lll': '⁠LOUD',
    # 'nmg': 'Netshoes Miners'
}

get_league = {
    'LCK': '1',
    'LEC': '2',
    'LVP SuperLiga': '3',
    'LCO': '4',
    'LFL': '5',
    'PCS': '6',
    'LCS': '7',
    'NA Academy League': '8',
    'LLA': '9',
    'Ultraliga': '10',
    'LPL': '11',
    'LJL': '12',
    'TCL': '13',
    'VCS': '14',
    'CBLOL': '15'
}

get_split = {
    'LCK': '1',
    'LEC': '2',
    'LVP SuperLiga': '3',
    'LCO': '4',
    'LFL': '5',
    'PCS': '6',
    'LCS': '7',
    'NA Academy League': '8',
    'LLA': '9',
    'Ultraliga': '10',
    'LPL': '11',
    'LJL': '12',
    'TCL': '13',
    'VCS': '14',
    'CBLOL': '15'
}

get_worlds_name = {
    # 'gw': 'GameWard',
    # 'id': 'Izi Dream',
    # 'fnc': 'Fnatic',
    # 'g2': 'G2 Esports',
    # 'spy': 'Splyce',
    # 'grf': 'Griffin',
    # 'skt': 'SK Telecom T1',
    # 'dwg': 'DAMWON Gaming',
    # 'hka': 'Hong Kong Attitude',
    # 'ahq': 'ahq e-Sports club',
    # 'jt': 'J Team',
    # 'tl': 'Team Liquid',
    # 'c9': 'Cloud9',
    # 'cg': 'Clutch Gaming',
    # 'fpx': 'FunPlus Phoenix',
    # 'rng': 'Royal Never Give Up',
    # 'ig': 'Invictus Gaming',
    # 'gam': 'GAM Esports'
}

get_name = {
    'gen': 'Gen.G',
    't1': 'T1',
    'drx': 'DRX',
    'lsb': 'Liiv SANDBOX',
    'dk': 'DWG KIA',
    'kdf': 'Kwangdong Freecs',
    'kt': 'KT Rolster',
    'ns': 'Nongshim RedForce',
    'hle': 'Hanwha Life Esports',
    'bro': 'Fredit BRION',
    'xl': 'Excel Esports',
    'fnc': 'Fnatic',
    'rge': 'Rogue',
    'g2': 'G2 Esports',
    'mad': 'MAD Lions',
    'vit': 'Team Vitality',
    'ast': 'Astralis',
    'msf': 'Misfits Gaming',
    'sk': 'SK Gaming',
    'bds': 'Team BDS',
    'hrts': 'Team Heretics',
    'fntq': 'Fnatic TQ',
    'bso': 'BISONS ECLUB',
    'g2ar': 'G2 Arctic',
    'gia': 'Giants',
    'bar': 'Barça eSports',
    'koi': 'KOI',
    'madm': 'MAD Lions Madrid',
    'ucam': 'UCAM Tokiers',
    'mrs': 'Movistar Riders',
    'chf': 'Chiefs Esports Club',
    'dw': 'Dire Wolves',
    'ord': 'ORDER',
    'pce': 'PEACE',
    'pgg': 'Pentanet.GG',
    'kng': 'Kanga Esports',
    'mec': 'MAMMOTH',
    'grv': 'Gravitas',
    'ldlc': 'LDLC OL',
    'gw': 'GameWard',
    'vitb': 'Vitality.Bee',
    'kc': 'Karmine Corp',
    'msfp': 'Misfits Premier',
    'bds.a': 'Team BDS Academy',
    'go': 'Team GO',
    'sly': 'Solary',
    'opl': 'Team Oplon',
    'me': 'Mirage Elyandra',
    'byg': 'Beyond Gaming',
    'jt': 'J Team',
    'cfo': 'CTBC Flying Oyster',
    'psg': 'PSG Talon',
    'dcg': 'Deep Cross Gaming',
    'fak': 'Frank Esports',
    'imp': 'Impunity',
    'mft': 'Meta Falcon Team',
    'dwt': 'Dewish Team',
    's9': 'SEM9',
    'eg': 'Evil Geniuses',
    '100': '100 Thieves',
    'tl': 'Team Liquid',
    'clg': 'Counter Logic Gaming',
    'fly': 'FlyQuest',
    'c9': 'Cloud9',
    'gg': 'Golden Guardians',
    'dig': 'Dignitas',
    'tsm': 'Team SoloMid',
    'imt': 'Immortals',
    'tl.a': 'Team Liquid Academy',
    '100.a': '100 Thieves Academy',
    'dig.a': 'Dignitas Academy',
    'clg.a': 'Counter Logic Gaming Academy',
    'imt.a': 'Immortals Academy',
    'c9.a': 'Cloud9 Academy',
    'fly.a': 'FlyQuest Academy',
    'eg.a': 'Evil Geniuses Academy',
    'gg.a': 'Golden Guardians Academy',
    'tsm.a': 'Team SoloMid Academy',
    'isg': 'Isurus',
    'est': 'Estral Esports',
    'ak': 'All Knights',
    'inf': 'Infinity Esports',
    'r7': 'Rainbow7',
    'aze': 'Team Aze',
    'xtn': 'XTEN Esports',
    'get': 'Globant Emerald',
    'rgo': 'AGO ROGUE',
    'ihg': 'Illuminar Gaming',
    'z10': 'Zero Tenacity',
    'gsk': 'Goskilla',
    'fsk': 'Forsaken',
    'wolf': 'Iron Wolves',
    'dv1': 'devils.one',
    'knf': 'Komil&Friends',
    'esca': 'Team ESCA Gaming',
    'ggm': "Gentlemen's Gaming",
    'v5': 'Victory Five',
    'jdg': 'JD Gaming',
    'tes': 'Top Esports',
    'edg': 'EDward Gaming',
    'rng': 'Royal Never Give Up',
    'lng': 'LNG Esports',
    'al': "Anyone's Legend",
    'omg': 'Oh My God',
    'wbg': 'Weibo Gaming',
    'fpx': 'FunPlus Phoenix',
    'up': 'Ultra Prime',
    'tt': 'ThunderTalk Gaming',
    'blg': 'Bilibili Gaming',
    'ra': 'Rare Atom',
    'lgd': 'LGD Gaming',
    'ig': 'Invictus Gaming',
    'we': 'Team WE',
    'sg': 'Sengoku Gaming',
    'dfm': 'DetonatioN FocusMe',
    'shg': 'Fukuoka SoftBank Hawks gaming',
    'bc': 'Burning Core',
    'cga': 'Crest Gaming Act',
    'rj': 'Rascal Jester',
    'axz': 'AXIZ',
    'v3': 'V3 Esports',
    'nsr': 'NASR eSports Turkey',
    'dp': 'Dark Passage',
    'iw': 'İstanbul Wildcats',
    'gal': 'Galakticos',
    'smb': 'SuperMassive Blaze',
    'bjk': 'Beşiktaş Esports',
    'gs': 'Galatasaray Esports',
    'aur': 'Team AURORA',
    'fb': 'Fenerbahçe Esports',
    '5r': '5 Ronin',
    'ces': 'CERBERUS Esports',
    'tw': 'Team Whales',
    'se': 'SBTC Esports',
    'ts': 'Team Secret',
    'gam': 'GAM Esports',
    'ge': 'Genius Esports',
    'ase': 'AS Esports',
    'sgb': 'Saigon Buffalo',
    'red': 'RED Canids',
    'fur': 'FURIA Esports',
    'png': 'paiN Gaming',
    'lll': 'LOUD',
    'kbm': 'KaBuM! e-Sports',
    'lbr': 'Liberty',
    'fla': 'Flamengo Los Grandes',
    'nmg': 'Miners',
    'itz': 'INTZ',
    'rns': 'Rensga Esports',
}

def get_league_id(league):
    return get_league[league]

def get_split_id(league):
    return get_split[league]

def convert_name(short_name):
    return get_name[short_name.lower()]

def get_team_id_by_name(short_name):

    currentTeam = convert_name(short_name.lower())

    with open('teams.json') as json_file:
        data = json.load(json_file)

        for team in data:
            if currentTeam == team['name']:
                return team['id']

def create_game():
    return {
        'first_blood_team_id': None,
        'first_turret_team_id': None,
        'first_dragon_team_id': None,
        'first_baron_team_id': None,
        'winner_id': None,
        'loser_id': None,
        'red_side_team_id': None,
        'blue_side_team_id': None,
        'game_number': None,
        'date': None,
        'league_id': None,
        'split_id': None,
    }

def process_game(game):
    game_data = create_game()
    data = game.split(',')

    game_data['league_id'] = data[0]
    game_data['split_id'] = data[1]
    game_data['date'] = data[2]
    game_data['game_number'] = data[3]
    game_data['blue_side_team_id'] = get_team_id_by_name(data[4])
    game_data['red_side_team_id'] = get_team_id_by_name(data[5])
    if data[6] != '':
        game_data['first_blood_team_id'] = get_team_id_by_name(data[6])
    if data[7] != '':
        game_data['first_turret_team_id'] = get_team_id_by_name(data[7])
    if data[8] != '':
        game_data['first_dragon_team_id'] = get_team_id_by_name(data[8])
    if data[10] != '':
        game_data['first_baron_team_id'] = get_team_id_by_name(data[10])
    game_data['winner_id'] = get_team_id_by_name(data[11])
    game_data['loser_id'] = get_team_id_by_name(data[12])
    return game_data
