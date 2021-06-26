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
    'drx': 'DRX',
    'ns': 'Nongshim RedForce',
    'gen': 'Gen.G',
    'lsb': 'Liiv SANDBOX',
    't1': 'T1',
    'kt': 'KT Rolster',
    'dk': 'DWG KIA',
    'hle': 'Hanwha Life Esports',
    'af': 'Afreeca Freecs',
    'bto': '⁠Fredit BRION'
}

get_lec_name = {
    'msf': 'Misfits Gaming',
    'xl': 'Excel Esports',
    'rge': 'Rogue',
    'vit': 'Team Vitality',
    'fnc': 'Fnatic',
    'ast': 'Astralis',
    'g2': 'G2 Esports',
    'sk': 'SK Gaming',
    's04': 'FC Schalke 04',
    'mad': 'MAD Lions'
}

get_lvp_name = {
    'bts': 'Cream Real Betis',
    'emz': 'eMonkeyz',
    'mrs': 'Movistar Riders',
    'g2ar': 'G2 Arctic',
    'vgia': 'Vodafone Giants',
    'madm': 'MAD Lions Madrid',
    'bcn': 'BCN Squad',
    's2v': 'S2V Esports',
    'ucam': 'UCAM Esports Club',
    'tq': 'Team Queso'
}

get_lco_name = {
    'lgc': 'Legacy',
    'grv': 'Gravitas',
    'mmm': 'MAMMOTH',
    'pgg': 'Pentanet.GG',
    'pce': '⁠PEACE',
    'ord': 'ORDER',
    'dw': 'Dire Wolves',
    'chf': 'Chiefs Esports Club'
}

# get_lfl_name = {
#     'msfp': 'Misfits Premier',
#     'sly': 'Solary',
#     'ldlc': 'LDLC OL',
#     'mces': 'Team MCES',
#     'go': 'GamersOrigin',
#     'gw': 'GameWard',
#     'izi': 'Izi Dream',
#     'vitb': 'Vitality.Bee'
# }

# get_pcs_name = {
#     'hka': 'Hong Kong Attitude',
#     'ahq': 'ahq eSports club',
#     'alf': 'Alpha Esports',
#     'jt': 'J Team',
#     'bjd': 'Berjaya Dragons',
#     'lyb': 'Liyab Esports',
#     'mcx': 'Machi Esports',
#     'nov': 'Nova Esports',
#     'psg': 'PSG Talon',
#     'rsg': 'Resurgence'
# }

get_lcs_name = {
    'dig': 'Dignitas',
    'imt': 'Immortals',
    'eg': 'Evil Geniuses',
    'tl': 'Team Liquid',
    'clg': 'Counter Logic Gaming',
    'c9': 'Cloud9',
    'tsm': 'Team SoloMid',
    'gg': 'Golden Guardians',
    '100': '100 Thieves',
    'fly': 'FlyQuest',
}

get_na_academy_league_name = {
    'tl.a': 'Team Liquid Academy',
    'clg.a': 'Counter Logic Gaming Academy',
    'c9.a': 'Cloud9 Academy',
    'tsm.a': 'Team SoloMid Academy',
    'gg.a': 'Golden Guardians Academy',
    'eg.a': 'Evil Geniuses Academy',
    '100.a': '100 Thieves Academy',
    'dig.a': 'Dignitas Academy',
    'fly.a': 'FlyQuest Academy',
    'imt.a': 'Immortals Academy'
}

get_lla_name = {
    'isg': 'Isurus Gaming',
    'ak': 'All Knights',
    'fg': 'Furious Gaming',
    'inf': 'Infinity Esports',
    'r7': 'Rainbow7',
    'xtn': 'XTEN Esports',
    'klg': 'Kaos Latin Gamers',
    'est': 'Estral Esports'
}

get_ultraliga_name = {
    'rgo': 'AGO ROGUE',
    'teg': 'Team ESCA Gaming',
    'pdw': 'PDW',
    'ggm': "Gentlemen's Gaming",
    'ihg': 'Illuminar Gaming',
    'knf': '⁠Komil&Friends',
    'dv1': '⁠devils.one',
    'k1': 'K1CK'
}

get_lpl_name = {
    'fpx': 'FunPlus Phoenix',
    'tes': 'Top Esports',
    'rng': 'Royal Never Give Up',
    'blg': 'Bilibili Gaming',
    'sn': 'Suning',
    'edg': 'EDward Gaming',
    'ig': 'Invictus Gaming',
    'lng': 'LNG Esports',
    'we': 'Team WE',
    'jdg': 'JD Gaming',
    'ra': 'Rare Atom',
    'rw': 'Rogue Warriors',
    'v5': 'Victory Five',
    'lgd': 'LGD Gaming',
    'omg': 'Oh My God',
    'up': 'Ultra Prime',
    'tt': 'ThunderTalk Gaming'
}

get_ljl_name = {
    'v3': 'V3 Esports',
    'sg': 'Sengoku Gaming',
    'cga': 'Crest Gaming Act',
    'dfm': 'DetonatioN FocusMe',
    'shg': 'Fukuoka SoftBank Hawks gaming',
    'axz': 'AXIZ',
    'bc': 'Burning Core',
    'rj': 'Rascal Jester'
}

get_tcl_name = {
    'bjk': 'Beşiktaş Esports',
    'dp': 'Dark Passage',
    'gal': 'Galakticos',
    'iw': 'İstanbul Wildcats',
    'fb': '1907 Fenerbahçe',
    'gs': 'Galatasaray Esports',
    '5r': '5 Ronin',
    'sup': 'SuperMassive Blaze',
    'nsr': 'NASR eSports Turkey',
    'aur': 'Team AURORA'
}

# get_vcs_name = {
#     'per': 'Percent Esports',
#     'opg': 'OverPower Esports',
#     'ces': 'CERBERUS Esports',
#     'evs': 'EVOS Esports',
#     'gam': 'GAM Esports',
#     'ts': 'Team Secret',
#     'sgb': 'Saigon Buffalo',
#     'fl': 'Team Flash'
# }

get_cblol_name = {
    'vrx': 'Vorax Liberty',
    'kbm': 'KaBuM! e-Sports',
    'png': 'paiN Gaming',
    'itz': 'INTZ',
    'fla': 'Flamengo eSports',
    'fur': 'FURIA Esports',
    'red': 'RED Canids',
    'rns': 'Rensga Esports',
    'lll': '⁠LOUD',
    'nmg': 'Netshoes Miners'
}

get_league = {
    'LCS': '1',
    'LCK': '2',
    'LEC': '3',
    'LCO': '4',
    'LFL': '5',
    'LVP_SuperLiga': '6',
    'PCS': '7',
    'LLA': '8',
    'Ultraliga': '9',
    'LPL': '10',
    'NA_Academy_League': '11',
    'LJL': '12',
    'TCL': '13',
    'VCS': '14',
    'CBLOL': '15'
}

get_split = {
    'LCS': '1',
    'LCK': '2',
    'LEC': '3',
    'LCO': '4',
    'LFL': '5',
    'LVP_SuperLiga': '6',
    'PCS': '7',
    'LLA': '8',
    'Ultraliga': '9',
    'LPL': '10',
    'NA_Academy_League': '11',
    'LJL': '12',
    'TCL': '13',
    'VCS': '14',
    'CBLOL': '15'
}

get_worlds_name = {
    'gw': 'GameWard',
    'id': 'Izi Dream',
    'fnc': 'Fnatic',
    'g2': 'G2 Esports',
    'spy': 'Splyce',
    'grf': 'Griffin',
    'skt': 'SK Telecom T1',
    'dwg': 'DAMWON Gaming',
    'hka': 'Hong Kong Attitude',
    'ahq': 'ahq e-Sports club',
    'jt': 'J Team',
    'tl': 'Team Liquid',
    'c9': 'Cloud9',
    'cg': 'Clutch Gaming',
    'fpx': 'FunPlus Phoenix',
    'rng': 'Royal Never Give Up',
    'ig': 'Invictus Gaming',
    'gam': 'GAM Esports'
}

get_name = {
    'drx': 'DRX',
    'ns': 'Nongshim RedForce',
    'gen': 'Gen.G',
    'lsb': 'Liiv SANDBOX',
    't1': 'T1',
    'kt': 'KT Rolster',
    'dk': 'DWG KIA',
    'hle': 'Hanwha Life Esports',
    'af': 'Afreeca Freecs',
    'bto': '⁠Fredit BRION',
    'msf': 'Misfits Gaming',
    'xl': 'Excel Esports',
    'rge': 'Rogue',
    'vit': 'Team Vitality',
    'fnc': 'Fnatic',
    'ast': 'Astralis',
    'g2': 'G2 Esports',
    'sk': 'SK Gaming',
    's04': 'FC Schalke 04',
    'mad': 'MAD Lions',
    'bts': 'Cream Real Betis',
    'emz': 'eMonkeyz',
    'mrs': 'Movistar Riders',
    'g2ar': 'G2 Arctic',
    'vgia': 'Vodafone Giants',
    'madm': 'MAD Lions Madrid',
    'bcn': 'BCN Squad',
    's2v': 'S2V Esports',
    'ucam': 'UCAM Esports Club',
    'tq': 'Team Queso',
    'lgc': 'Legacy',
    'grv': 'Gravitas',
    'mmm': 'MAMMOTH',
    'pgg': 'Pentanet.GG',
    'pce': '⁠PEACE',
    'ord': 'ORDER',
    'dw': 'Dire Wolves',
    'chf': 'Chiefs Esports Club',
    'dig': 'Dignitas',
    'imt': 'Immortals',
    'eg': 'Evil Geniuses',
    'tl': 'Team Liquid',
    'clg': 'Counter Logic Gaming',
    'c9': 'Cloud9',
    'tsm': 'Team SoloMid',
    'gg': 'Golden Guardians',
    '100': '100 Thieves',
    'fly': 'FlyQuest',
    'tl.a': 'Team Liquid Academy',
    'clg.a': 'Counter Logic Gaming Academy',
    'c9.a': 'Cloud9 Academy',
    'tsm.a': 'Team SoloMid Academy',
    'gg.a': 'Golden Guardians Academy',
    'eg.a': 'Evil Geniuses Academy',
    '100.a': '100 Thieves Academy',
    'dig.a': 'Dignitas Academy',
    'fly.a': 'FlyQuest Academy',
    'imt.a': 'Immortals Academy',
    'isg': 'Isurus Gaming',
    'ak': 'All Knights',
    'fg': 'Furious Gaming',
    'inf': 'Infinity Esports',
    'r7': 'Rainbow7',
    'xtn': 'XTEN Esports',
    'klg': 'Kaos Latin Gamers',
    'est': 'Estral Esports',
    'rgo': 'AGO ROGUE',
    'teg': 'Team ESCA Gaming',
    'pdw': 'PDW',
    'ggm': "Gentlemen's Gaming",
    'ihg': 'Illuminar Gaming',
    'knf': '⁠Komil&Friends',
    'dv1': '⁠devils.one',
    'k1': 'K1CK',
    'fpx': 'FunPlus Phoenix',
    'tes': 'Top Esports',
    'rng': 'Royal Never Give Up',
    'blg': 'Bilibili Gaming',
    'sn': 'Suning',
    'edg': 'EDward Gaming',
    'ig': 'Invictus Gaming',
    'lng': 'LNG Esports',
    'we': 'Team WE',
    'jdg': 'JD Gaming',
    'ra': 'Rare Atom',
    'rw': 'Rogue Warriors',
    'v5': 'Victory Five',
    'lgd': 'LGD Gaming',
    'omg': 'Oh My God',
    'up': 'Ultra Prime',
    'tt': 'ThunderTalk Gaming',
    'v3': 'V3 Esports',
    'sg': 'Sengoku Gaming',
    'cga': 'Crest Gaming Act',
    'dfm': 'DetonatioN FocusMe',
    'shg': 'Fukuoka SoftBank Hawks gaming',
    'axz': 'AXIZ',
    'bc': 'Burning Core',
    'rj': 'Rascal Jester',
    'bjk': 'Beşiktaş Esports',
    'dp': 'Dark Passage',
    'gal': 'Galakticos',
    'iw': 'İstanbul Wildcats',
    'fb': '1907 Fenerbahçe',
    'gs': 'Galatasaray Esports',
    '5r': '5 Ronin',
    'sup': 'SuperMassive Blaze',
    'nsr': 'NASR eSports Turkey',
    'aur': 'Team AURORA',
    'vrx': 'Vorax Liberty',
    'kbm': 'KaBuM! e-Sports',
    'png': 'paiN Gaming',
    'itz': 'INTZ',
    'fla': 'Flamengo eSports',
    'fur': 'FURIA Esports',
    'red': 'RED Canids',
    'rns': 'Rensga Esports',
    'lll': '⁠LOUD',
    'nmg': 'Netshoes Miners'
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
