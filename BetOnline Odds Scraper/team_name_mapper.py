import json

get_month = {
  'January' : '01',
  'February' : '02',
  'March' : '03',
  'April' : '04',
  'May' : '05',
  'June' : '06',
  'July' : '07',
  'August' : '08',
  'September': '09',
  'October' : '10',
  'November' : '11',
  'December' : '12'
}

get_lck_name = {
  'grf' : 'Griffin',
  'sb' : 'SANDBOX Gaming',
  'gen' : 'Gen.G',
  'jag' : 'Jin Air Green Wings',
  'kz' : 'KINGZONE DragonX',
  'skt' : 'SK Telecom T1',
  'kt' : 'KT Rolster',
  'dwg' : 'DAMWON Gaming',
  'hle' : 'Hanwha Life Esports',
  'af' : 'Afreeca Freecs',
  'apk' : 'APK Prince',
  'dyn' : 'Team Dynamics'
}

get_lec_name = {
  'msf' : 'Misfits',
  'xl' : 'Excel Esports',
  'rge' : 'Rogue',
  'vit' : 'Team Vitality',
  'fnc' : 'Fnatic',
  'og' : 'Origen',
  'g2' : 'G2 Esports',
  'sk' : 'SK Gaming',
  'spy' : 'Splyce',
  's04' : 'Schalke 04'
}

get_lvp_name = {
  'svp' : 'Splyce Vipers',
  'emz' : 'eMonkeyz',
  'mrs' : 'Movistar Riders',
  'x6' : 'x6tence',
  'gia' : 'Vodafone Giants',
  'pgm' : 'Penguins',
  'mad' : 'MAD Lions',
  'g2h' : 'G2 Heretics',
  's2v' : 'S2V Esports',
  'ogb' : 'Origen BCN',
  'tq' : 'Team Queso'
}

get_opl_name = {
  'lgc' : 'Legacy',
  'grv' : 'Gravitas',
  'mmm' : 'MAMMOTH',
  'bmr' : 'Bombers',
  'av' : 'Avant Gaming',
  'ord' : 'ORDER',
  'dw' : 'Dire Wolves',
  'chf' : 'Chiefs Esports Club'
}

get_lfl_name = {
  'msf.p' : 'Misfits Premier',
  'sly' : 'Solary',
  'ldlc' : 'LDLC',
  'mces' : 'Team MCES',
  'go' : 'Gamers Origin',
  'aaa' : 'against All authority',
  'rog' : 'ROG Esport',
  'vit.b' : 'Vitality.Bee'
}

get_lms_name = {
  'hka' : 'Hong Kong Attitude',
  'mad' : 'MAD Team',
  'fw' : 'Flash Wolves',
  'ahq' : 'ahq e-Sports club',
  'alf' : 'Alpha Esports',
  'jt' : 'J Team',
  'grx' : 'G-Rex',
  'dg' : 'Dragon Gate'
}

get_lcs_name = {
  'tl' : 'Team Liquid',
  'clg' : 'Counter Logic Gaming',
  'c9' : 'Cloud9',
  'tsm' : 'Team SoloMid',
  'ggs' : 'Golden Guardians',
  'opt' : 'OpTic Gaming',
  '100' : '100 Thieves',
  'cg' : 'Clutch Gaming',
  'fly' : 'FlyQuest',
  'fox' : 'Echo Fox'
}

get_na_academy_league_name = {
  'tl.a' : 'Team Liquid Academy',
  'clg.a' : 'Counter Logic Gaming Academy',
  'c9.a' : 'Cloud9 Academy',
  'tsm.a' : 'Team SoloMid Academy',
  'ggs.a' : 'Golden Guardians Academy',
  'opt.a' : 'OpTic Gaming Academy',
  '100.a' : '100 Thieves Academy',
  'cg.a' : 'Clutch Gaming Academy',
  'fly.a' : 'FlyQuest Academy',
  'fox.a' : 'Echo Fox Academy'
}

get_lla_name = {
  'isg' : 'Isurus Gaming',
  'ak' : 'All Knights',
  'fg' : 'Furious Gaming',
  'inf' : 'Infinity Esports',
  'r7' : 'Rainbow7',
  'xten' : 'XTEN Esports',
  'klg' : 'Kaos Latin Gamers',
  'pix' : 'Pixel Esports Club'
}

get_ultraliga_name = {
  'rec' : 'Rogue Esports Club',
  'dv1' : 'devils.one',
  'prd' : 'PRIDE',
  'ave' : 'AVEZ Esport',
  'ihg' : 'Illuminar Gaming',
  'apr' : 'piratesports',
  'pct' : 'ACTINA PACT',
  'wp' : 'Wisla Plock eSports'
}

get_lpl_name = {
  'fpx' : 'FunPlus Phoenix',
  'tes' : 'Top Esports',
  'rng' : 'Royal Never Give Up',
  'blg' : 'Bilibili Gaming',
  'sn' : 'Suning',
  'edg' : 'EDward Gaming',
  'ig' : 'Invictus Gaming',
  'lng' : 'LNG Esports',
  'we' : 'Team WE',
  'jdg' : 'JD Gaming',  
  'dmo' : 'Dominus Esports',
  'rw' : 'Rogue Warriors',
  'v5' : 'Victory Five',
  'lgd' : 'LGD Gaming', 
  'omg' : 'Oh My God',
  'vg' : 'Vici Gaming'
}

get_league = {
  'LCK' : '1',
  'LEC' : '2',
  'OPL' : '3',
  'LFL' : '4',
  'LVP_SuperLiga_Orange' : '5',
  'LMS' : '6',
  'LCS' : '7',
  'LLA' : '8',
  'Ultraliga' : '9',
  'LPL' : '10',
  'NA_Academy_League' : '11',
  '2019_Season_World_Championship' : '12'
}

get_split = {
  'LCK' : '1',
  'LEC' : '2',
  'OPL' : '3',
  'LFL' : '4',
  'LVP_SuperLiga_Orange' : '5',
  'LMS' : '6',
  'LCS' : '7',
  'LLA' : '8',
  'Ultraliga' : '9',
  'LPL' : '10',
  'NA_Academy_League' : '11',
  '2019_Season_World_Championship' : '12'
}

get_worlds_name = {
  'fnc' : 'Fnatic',
  'g2' : 'G2 Esports',
  'spy' : 'Splyce',
  'grf' : 'Griffin',
  'skt' : 'SK Telecom T1',
  'dwg' : 'DAMWON Gaming',
  'hka' : 'Hong Kong Attitude',
  'ahq' : 'ahq e-Sports club',
  'jt' : 'J Team',
  'tl' : 'Team Liquid',
  'c9' : 'Cloud9',
  'cg' : 'Clutch Gaming',
  'fpx' : 'FunPlus Phoenix',
  'rng' : 'Royal Never Give Up',
  'ig' : 'Invictus Gaming',
  'gam' : 'GAM Esports'
}

get_name = {
  'msf' : 'Misfits',
  'xl' : 'Excel Esports',
  'rge' : 'Rogue',
  'vit' : 'Team Vitality',
  'fnc' : 'Fnatic',
  'og' : 'Origen',
  'g2' : 'G2 Esports',
  'sk' : 'SK Gaming',
  'spy' : 'Splyce',
  's04' : 'Schalke 04',
  'lgc' : 'Legacy',
  'grv' : 'Gravitas',
  'mmm' : 'MAMMOTH',
  'bmr' : 'Bombers',
  'av' : 'Avant Gaming',
  'ord' : 'ORDER',
  'dw' : 'Dire Wolves',
  'chf' : 'Chiefs Esports Club',
  'svp' : 'Splyce Vipers',
  'emz' : 'eMonkeyz',
  'mrs' : 'Movistar Riders',
  'x6' : 'x6tence',
  'gia' : 'Vodafone Giants',
  'pgm' : 'Penguins',
  'mad' : 'MAD Lions',
  'g2h' : 'G2 Heretics',
  's2v' : 'S2V Esports',
  'ogb' : 'Origen BCN',
  'tq' : 'Team Queso',
  'grf' : 'Griffin',
  'sb' : 'SANDBOX Gaming',
  'gen' : 'Gen.G',
  'jag' : 'Jin Air Green Wings',
  'kz' : 'KINGZONE DragonX',
  'skt' : 'SK Telecom T1',
  'kt' : 'KT Rolster',
  'dwg' : 'DAMWON Gaming',
  'hle' : 'Hanwha Life Esports',
  'af' : 'Afreeca Freecs',
  'apk' : 'APK Prince',
  'dyn' : 'Team Dynamics',
  'msf.p' : 'Misfits Premier',
  'sly' : 'Solary',
  'ldlc' : 'LDLC',
  'mces' : 'Team MCES',
  'go' : 'Gamers Origin',
  'aaa' : 'against All authority',
  'rog' : 'ROG Esport',
  'vit.b' : 'Vitality.Bee',
  'hka' : 'Hong Kong Attitude',
  'mad' : 'MAD Team',
  'fw' : 'Flash Wolves',
  'ahq' : 'ahq e-Sports club',
  'alf' : 'Alpha Esports',
  'jt' : 'J Team',
  'grx' : 'G-Rex',
  'dg' : 'Dragon Gate',
  'tl' : 'Team Liquid',
  'clg' : 'Counter Logic Gaming',
  'c9' : 'Cloud9',
  'tsm' : 'Team SoloMid',
  'ggs' : 'Golden Guardians',
  'opt' : 'OpTic Gaming',
  '100' : '100 Thieves',
  'cg' : 'Clutch Gaming',
  'fly' : 'FlyQuest',
  'fox' : 'Echo Fox',
  'tl.a' : 'Team Liquid Academy',
  'clg.a' : 'Counter Logic Gaming Academy',
  'c9.a' : 'Cloud9 Academy',
  'tsm.a' : 'Team SoloMid Academy',
  'ggs.a' : 'Golden Guardians Academy',
  'opt.a' : 'OpTic Gaming Academy',
  '100.a' : '100 Thieves Academy',
  'cg.a' : 'Clutch Gaming Academy',
  'fly.a' : 'FlyQuest Academy',
  'fox.a' : 'Echo Fox Academy',
  'isg' : 'Isurus Gaming',
  'ak' : 'All Knights',
  'fg' : 'Furious Gaming',
  'inf' : 'Infinity Esports',
  'r7' : 'Rainbow7',
  'xten' : 'XTEN Esports',
  'klg' : 'Kaos Latin Gamers',
  'pix' : 'Pixel Esports Club',
  'rec' : 'Rogue Esports Club',
  'dv1' : 'devils.one',
  'prd' : 'PRIDE',
  'ave' : 'AVEZ Esport',
  'ihg' : 'Illuminar Gaming',
  'apr' : 'piratesports',
  'pct' : 'ACTINA PACT',
  'wp' : 'Wisla Plock eSports',
  'fpx' : 'FunPlus Phoenix',
  'tes' : 'Top Esports',
  'rng' : 'Royal Never Give Up',
  'blg' : 'Bilibili Gaming',
  'sn' : 'Suning',
  'edg' : 'EDward Gaming',
  'ig' : 'Invictus Gaming',
  'lng' : 'LNG Esports',
  'we' : 'Team WE',
  'jdg' : 'JD Gaming',  
  'dmo' : 'Dominus Esports',
  'rw' : 'Rogue Warriors',
  'v5' : 'Victory Five',
  'lgd' : 'LGD Gaming', 
  'omg' : 'Oh My God',
  'vg' : 'Vici Gaming',
  'gam' : 'GAM Esports'
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
          'first_blood_team_id' : None,
          'first_turret_team_id' : None,
          'first_dragon_team_id' : None,
          'first_baron_team_id' : None,
          'winner_id' : None,
          'loser_id' : None,
          'red_side_team_id' : None,
          'blue_side_team_id' : None,
          'game_number' : None,
          'date' : None,
          'league_id' : None,
          'split_id' : None,
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
