import csv
import re
from os.path import exists

def initialization_of_player(player_name):
    return {"player_name": player_name, "FG": 0, "FGA": 0, "FG%": None, "3P": 0, "3PA": 0, "3P%": None, "FT": 0, "FTA": 0, "FT%": None, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0}

def fetch_data_from_file(file_name):
    rows = []
    file = open(file_name)
    csvreader = csv.reader(file, delimiter='|')
    for row in csvreader:
        rows.append(row)
    file.close()    
    return rows

def result_initialization(play_by_play_moves):
    result = {"home_team": {}, "away_team": {}}
    result["home_team"]["name"]=play_by_play_moves[0][3]
    result["away_team"]["name"]=play_by_play_moves[0][4]
    result["home_team"]["players_data"]=[]
    result["away_team"]["players_data"]=[]
    return result

def check_for_existance(player, result, team):
    for i, players in enumerate(result[team]["players_data"]):
        if player in players.values():
            position_of_player=i
            return position_of_player

    return -1

def swap_teams(team):
    if (team == "home_team"):
        return "away_team"
    else:
        return "home_team"

def print_nba_game_stats(team_dict):
    print("TEAM NAME: ", team_dict["name"])
    print("{:20} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format('Players', 'FG', 'FGA', 'FG%', '3P', '3PA',	'3P%', 'FT','FTA','FT%',	'ORB',	'DRB',	'TRB',	'AST'	,'STL'	,'BLK'	,'TOV',	'PF',	'PTS'))
    total = {"FG": 0, "FGA": 0, "FG%": None, "3P": 0, "3PA": 0, "3P%": None, "FT": 0, "FTA": 0, "FT%": None, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0}
    for player in team_dict["players_data"]:
        if player["FGA"]>0:
            player["FG%"]='{:.3f}'.format(round(player["FG"]/player["FGA"], 3))
        else:
            player["FG%"]="  "
        if player["3PA"]>0:
            player["3P%"]='{:.3f}'.format(round(player["3P"]/player["3PA"], 3))
        else:
            player["3P%"]="  "
        if player["FTA"]>0:
            player["FT%"]='{:.3f}'.format(round(player["FT"]/player["FTA"], 3))
        else:
            player["FT%"]="  "
        player["TRB"]= player["ORB"]+player["DRB"]
        player["PTS"]= (player["FG"]-player["3P"])*2+(player["3P"]*3)+player["FT"]
        total["FG"]+=player["FG"]
        total["FGA"]+=player["FGA"]
        total["3P"]+=player["3P"]
        total["3PA"]+=player["3PA"]
        total["FT"]+=player["FT"]
        total["FTA"]+=player["FTA"]
        total["ORB"]+=player["ORB"]
        total["DRB"]+=player["DRB"]
        total["TRB"]+=player["TRB"]
        total["AST"]+=player["AST"]
        total["STL"]+=player["STL"]
        total["BLK"]+=player["BLK"]
        total["TOV"]+=player["TOV"]
        total["PF"]+=player["PF"]
        total["PTS"]+=player["PTS"]
        print("{:20} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format(player["player_name"], player["FG"], player["FGA"], player["FG%"], player["3P"], player["3PA"], player["3P%"], player["FT"], player["FTA"], player["FT%"], player["ORB"], player["DRB"], player["TRB"], player["AST"], player["STL"], player["BLK"], player["TOV"], player["PF"], player["PTS"]))

    if total["FGA"]>0:
        total["FG%"]='{:.3f}'.format(round(total["FG"]/total["FGA"], 3))
    else:
        total["FG%"]="  "
    if total["3PA"]>0:
        total["3P%"]='{:.3f}'.format(round(total["3P"]/total["3PA"], 3))
    else:
        total["3P%"]="  "
    if total["FTA"]>0:
        total["FT%"]='{:.3f}'.format(round(total["FT"]/total["FTA"], 3))
    else:
        total["FT%"]="  "
    print("{:20} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}\n".format("Team Totals",total["FG"],total["FGA"], total["FG%"], total["3P"], total["3PA"], total["3P%"],total["FT"],total["FTA"],total["FT%"],total["ORB"],total["DRB"],total["TRB"],total["AST"],total["STL"], total["BLK"],total["TOV"],total["PF"],total["PTS"]))

def add_3pt(players_in_dict, position, player):
    if(position>=0):
        players_in_dict[position]["3P"]+=1
        players_in_dict[position]["3PA"]+=1
        players_in_dict[position]["FGA"]+=1
        players_in_dict[position]["FG"]+=1
    else:
        players_in_dict.append(initialization_of_player(player))
        players_in_dict[-1]["3P"]+=1
        players_in_dict[-1]["3PA"]+=1
        players_in_dict[-1]["FGA"]+=1
        players_in_dict[-1]["FG"]+=1

def add_3pta(players_in_dict, position, player):
    if(position>=0):
        players_in_dict[position]["3PA"]+=1
        players_in_dict[position]["FGA"]+=1
    else:
        players_in_dict.append(initialization_of_player(player))
        players_in_dict[-1]["3PA"]+=1
        players_in_dict[-1]["FGA"]+=1

def add_2pt(players_in_dict, position, player):
    if(position>=0):
        players_in_dict[position]["FGA"]+=1
        players_in_dict[position]["FG"]+=1
    else:
        players_in_dict.append(initialization_of_player(player))
        players_in_dict[-1]["FGA"]+=1
        players_in_dict[-1]["FG"]+=1

def add_2pta(players_in_dict, position, player):
    if(position>=0):
        players_in_dict[position]["FGA"]+=1
    else:
        players_in_dict.append(initialization_of_player(player))
        players_in_dict[-1]["FGA"]+=1

def add_ft(players_in_dict, position, player):
    if(position>=0):
        players_in_dict[position]["FTA"]+=1
        players_in_dict[position]["FT"]+=1
    else:
        players_in_dict.append(initialization_of_player(player))
        players_in_dict[-1]["FTA"]+=1
        players_in_dict[-1]["FT"]+=1

def add_fta(players_in_dict, position, player):
    if(position>=0):
        players_in_dict[position]["FTA"]+=1
    else:
        players_in_dict.append(initialization_of_player(player))
        players_in_dict[-1]["FTA"]+=1

def add_orb(players_in_dict, position, player):
    if(position>=0):
        players_in_dict[position]["ORB"]+=1
    else:
        players_in_dict.append(initialization_of_player(player))
        players_in_dict[position]["ORB"]+=1

def add_drb(players_in_dict, position, player):
    if(position>=0):
        players_in_dict[position]["DRB"]+=1
    else:
        players_in_dict.append(initialization_of_player(player))
        players_in_dict[position]["DRB"]+=1

def add_assist(players_in_dict, position, player):
    if(position>=0):
        players_in_dict[position]["AST"]+=1
    else:
        players_in_dict.append(initialization_of_player(player))
        players_in_dict[position]["AST"]+=1

def add_steal(players_in_dict, position, player):
    if(position>=0):
        players_in_dict[position]["STL"]+=1
    else:
        players_in_dict.append(initialization_of_player(player))
        players_in_dict[position]["STL"]+=1

def add_block(players_in_dict, position, player):
    if(position>=0):
        players_in_dict[position]["BLK"]+=1
    else:
        players_in_dict.append(initialization_of_player(player))
        players_in_dict[position]["BLK"]+=1

def add_TOV(players_in_dict, position, player):
    if(position>=0):
        players_in_dict[position]["TOV"]+=1
    else:
        players_in_dict.append(initialization_of_player(player))
        players_in_dict[position]["TOV"]+=1

def add_ordinary_foul(players_in_dict, position, player):
    if(position>=0):
        players_in_dict[position]["PF"]+=1
    else:
        players_in_dict.append(initialization_of_player(player))
        players_in_dict[position]["PF"]+=1

def add_opposite_foul(players_in_dict, position, player):
    if(position>=0):
        players_in_dict[position]["PF"]+=1
    else:
        players_in_dict.append(initialization_of_player(player))
        players_in_dict[position]["PF"]+=1

def search_in_description(description):
    result = {}
    three_pt_made=re.compile(r'(\w+[.]?\s+\w+([-]+\w+)?) makes( clear path)? 3-pt').search(description)
    if three_pt_made: result["three_pt_made"]=three_pt_made
    
    three_pt_missed=re.compile(r'(\w+[.]?\s+\w+([-]+\w+)?) misses 3-pt').search(description)
    if three_pt_missed: result["three_pt_missed"]=three_pt_missed

    two_pt_made=re.compile(r'(\w+[.]?\s+\w+([-]+\w+)?) makes( clear path)? 2-pt').search(description)
    if two_pt_made: result["two_pt_made"]=two_pt_made

    two_pt_missed=re.compile(r'(\w+[.]?\s+\w+([-]+\w+)?) misses 2-pt').search(description)
    if two_pt_missed: result["two_pt_missed"]=two_pt_missed

    free_throw_made = re.compile(r'(\w+[.]?\s+\w+([-]+\w+)?) makes( clear path)? free throw').search(description)
    if free_throw_made: result["free_throw_made"]=free_throw_made

    free_throw_missed = re.compile(r'(\w+[.]?\s+\w+([-]+\w+)?) misses free throw').search(description)
    if free_throw_missed: result["free_throw_missed"]=free_throw_missed

    ORB = re.compile(r'Offensive rebound by (\w+[.]?\s+\w+([-]+\w+)?)').search(description)
    if ORB: result["ORB"]=ORB

    DRB = re.compile(r'Defensive rebound by (\w+[.]?\s+\w+([-]+\w+)?)').search(description)
    if DRB: result["DRB"]=DRB

    block = re.compile(r'block by (\w+[.]?\s+\w+([-]+\w+)?)').search(description)
    if block: result["block"]=block

    ordinary_foul = re.compile(r'(Personal foul|Clear path foul|Shooting foul) by (\w+[.]?\s+\w+([-]+\w+)?)').search(description)
    if ordinary_foul: result["ordinary_foul"]=ordinary_foul

    opposite_foul = re.compile(r'(Offensive foul|Loose ball foul) by (\w+[.]?\s+\w+([-]+\w+)?)').search(description)
    if opposite_foul: result["opposite_foul"]=opposite_foul

    steal = re.compile(r'steal by (\w+[.]?\s+\w+([-]+\w+)?)').search(description)
    if steal: result["steal"]=steal

    assist = re.compile(r'assist by (\w+[.]?\s+\w+([-]+\w+)?)').search(description)
    if assist: result["assist"]=assist

    TOV = re.compile(r'Turnover by (\w+[.]?\s+\w+([-]+\w+)?)').search(description)
    if TOV: result["TOV"]=TOV
    return result

def analyse_nba_game(play_by_play_moves):
    result = result_initialization(play_by_play_moves)
    for row in play_by_play_moves:
        if(row[2]==row[3]):
            team="home_team"
        else:
            team="away_team"

        description = row[7]
        search_result = search_in_description(row[7])

        #working with 3-pt           
        if("three_pt_made" in search_result.keys()):
            player = search_result["three_pt_made"][1]
            position = check_for_existance(player, result, team)
            players_in_dict=result[team]["players_data"]
            add_3pt(players_in_dict, position, player)

        if("three_pt_missed" in search_result.keys()):
            player = search_result["three_pt_missed"][1]
            position = check_for_existance(player, result, team)
            players_in_dict=result[team]["players_data"]
            add_3pta(players_in_dict, position, player)

        #working with 2-pt
        if("two_pt_made" in search_result.keys()):
            player = search_result["two_pt_made"][1]
            position = check_for_existance(player, result, team)
            players_in_dict=result[team]["players_data"]
            add_2pt(players_in_dict, position, player)

        if("two_pt_missed" in search_result.keys()):
            player = search_result["two_pt_missed"][1]
            position = check_for_existance(player, result, team)
            players_in_dict=result[team]["players_data"]
            add_2pta(players_in_dict, position, player)
            
        #working with free throw    
        if("free_throw_made" in search_result.keys()):
            player = search_result["free_throw_made"][1]
            position = check_for_existance(player, result, team)
            players_in_dict=result[team]["players_data"]
            add_ft(players_in_dict, position, player)

        if("free_throw_missed" in search_result):
            player = search_result["free_throw_missed"][1]
            position = check_for_existance(player, result, team)
            players_in_dict=result[team]["players_data"]
            add_fta(players_in_dict, position, player)

        #working with rebounds
        if("ORB" in search_result.keys()):
            player = search_result["ORB"][1]
            position = check_for_existance(player, result, team)
            players_in_dict=result[team]["players_data"]
            add_orb(players_in_dict, position, player)

        if("DRB" in search_result.keys()):
            player = search_result["DRB"][1]
            position = check_for_existance(player, result, team)
            players_in_dict=result[team]["players_data"]
            add_drb(players_in_dict, position, player)

        #working with assists
        if("assist" in search_result.keys()):
            player = search_result["assist"][1]
            position = check_for_existance(player, result, team)
            players_in_dict=result[team]["players_data"]
            add_assist(players_in_dict, position, player)
      
        #working with steal
        if("steal" in search_result.keys()):
            team = swap_teams(team)
            player = search_result["steal"][1]
            position = check_for_existance(player, result, team)
            players_in_dict=result[team]["players_data"]
            add_steal(players_in_dict, position, player)
            team = swap_teams(team)

        #working with block
        if("block" in search_result.keys()):
            team = swap_teams(team)
            player = search_result["block"][1]
            position = check_for_existance(player, result, team)
            players_in_dict=result[team]["players_data"]
            add_block(players_in_dict, position, player)
            team = swap_teams(team)

        #working with turnovers
        if("TOV" in search_result.keys()):
            player = search_result["TOV"][1]
            position = check_for_existance(player, result, team)
            players_in_dict=result[team]["players_data"]
            add_TOV(players_in_dict, position, player)

        #working with fouls
        if("ordinary_foul" in search_result.keys()):
            team = swap_teams(team)
            player = search_result["ordinary_foul"][1]
            position = check_for_existance(player, result, team)
            players_in_dict=result[team]["players_data"]
            add_ordinary_foul(players_in_dict, position, player)
            team = swap_teams(team)

        if("opposite_foul" in search_result.keys()):
            player = search_result["opposite_foul"][1]
            position = check_for_existance(player, result, team)
            players_in_dict=result[team]["players_data"]
            add_opposite_foul(players_in_dict, position, player)

    return result

file_exists=False
while file_exists==False:
    file_name=input("Input the name of file to analyze (without quotes): ")
    file_exists = exists(file_name)
    if(file_exists):
        play_by_play_moves = fetch_data_from_file(file_name)
        result = analyse_nba_game(play_by_play_moves)
        print_nba_game_stats(result["home_team"])
        print_nba_game_stats(result["away_team"])
    else:
        print("No file with such name")