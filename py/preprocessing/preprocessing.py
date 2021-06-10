import csv

playersRank = list()
players = list()

###         ATP
#populate players with player's id, first name, last name and country
with open("../../data/tennis_atp/atp_players.csv", "r", encoding="utf8") as players_file:
    print("Start ATP preprocessing")
    first_line = next(players_file)
    first_line = first_line.split(",")

    for line in players_file:
        player = line.split(",")
        players.append([player[0], player[1], player[2], player[5]])
        #print(players)

    players_file.close()

# populate playersRank list with rank with current ranking and player id
with open("../../data/tennis_atp/atp_rankings_current.csv", "r", encoding="utf8") as ranking_file:
    first_line = next(ranking_file)
    first_line = first_line.split(",")

    for line in ranking_file:
        player = line.split(",")
        playersRank.append([player[1], player[2]])
        #print(playersRank)

    ranking_file.close()

for i in ["80", "90", "00", "10", "20"]:
    with open("../../data/tennis_atp/atp_rankings_"+ i +"s.csv", "r", encoding="utf8") as ranking_file:
        first_line = next(ranking_file)
        first_line = first_line.split(",")

        for line in ranking_file:
            player = line.split(",")
            playersRank.append([player[1], player[2]])
            #print(playersRank)

        ranking_file.close()

#write a csv file with countries and number of players for every country for the actual ranking
with open('../../data/preprocessed/map/atp_players_with_rank_all-time.csv', 'w', newline='', encoding="utf8") as output:
    print("Start output phase")
    writer = csv.writer(output, delimiter=",")
    writer_header = csv.DictWriter(output, fieldnames=["country", "n_players", "players"])
    writer_header.writeheader()
    top100players = list()
    countries = list()

    for r in playersRank: #r[0] = rank, r[1] = id, p[0] = id, p[1] = first name, p[2] = last name, p[3] = country
        if int(r[0]) < 101:
            if not r[1] in top100players:
                top100players.append(r[1])
                for p in players:
                    if r[1] == p[0]:
                        p[3] = p[3].replace("\n", "")
                        if p[3] in (y for x in countries for y in x):
                            x = 0
                            while x < len(countries):
                                y = 0
                                while y < len(countries[x]):
                                    if countries[x][y] == p[3]:
                                        countries[x][y+1] = int(countries[x][y+1])
                                        countries[x][y+1] += 1
                                        countries[x][y+2].append(p[1] + " " + p[2])
                                    y = y + 1
                                x = x + 1
                        else:
                            countries.append([p[3], int(1), [p[1] + " " + p[2]]])
    for c in countries:
        writer.writerow([c[0], c[1], c[2]])
    playersRank.clear()
    countries.clear()
    top100players.clear()


#ATP 2021
# populate playersRank list with rank with current ranking and player id
with open("../../data/tennis_atp/atp_rankings_current.csv", "r", encoding="utf8") as ranking_file:
    first_line = next(ranking_file)
    first_line = first_line.split(",")

    for line in ranking_file:
        player = line.split(",")
        playersRank.append([player[1], player[2]])
        #print(playersRank)

    ranking_file.close()

#write a csv file with countries and number of players for every country for the actual ranking
with open('../../data/preprocessed/map/atp_players_with_rank.csv', 'w', newline='', encoding="utf8") as output:
    print("Start output phase")
    writer = csv.writer(output, delimiter=",")
    writer_header = csv.DictWriter(output, fieldnames=["country", "n_players", "players"])
    writer_header.writeheader()
    top100players = list()
    countries = list()

    for r in playersRank: #r[0] = rank, r[1] = id, p[0] = id, p[1] = first name, p[2] = last name, p[3] = country
        if int(r[0]) < 101:
            if not r[1] in top100players:
                top100players.append(r[1])
                for p in players:
                    if r[1] == p[0]:
                        p[3] = p[3].replace("\n", "")
                        if p[3] in (y for x in countries for y in x):
                            x = 0
                            while x < len(countries):
                                y = 0
                                while y < len(countries[x]):
                                    if countries[x][y] == p[3]:
                                        countries[x][y+1] = int(countries[x][y+1])
                                        countries[x][y+1] += 1
                                        countries[x][y+2].append(p[1] + " " + p[2])
                                    y = y + 1
                                x = x + 1
                        else:
                            countries.append([p[3], int(1), [p[1] + " " + p[2]]])
    for c in countries:
        writer.writerow([c[0], c[1], c[2]])
    playersRank.clear()
    countries.clear()
    top100players.clear()


#ATP 2020-2021
# populate playersRank list with player id and rank with 20s ranking
with open("../../data/tennis_atp/atp_rankings_20s.csv", "r", encoding="utf8") as ranking_file:
    first_line = next(ranking_file)
    first_line = first_line.split(",")

    for line in ranking_file:
        player = line.split(",")
        playersRank.append([player[1], player[2]])
        #print(playersRank)

    ranking_file.close()

#write a csv file with countries and number of players for every country for the 20's rank
with open('../../data/preprocessed/map/atp_players_with_rank_20s.csv', 'w', newline='', encoding="utf8") as output:
    print("Start output phase")
    writer = csv.writer(output, delimiter=",")
    writer_header = csv.DictWriter(output, fieldnames=["country", "n_players", "players"])
    writer_header.writeheader()
    top100players = list()
    countries = list()

    for r in playersRank: #r[0] = rank, r[1] = id, p[0] = id, p[1] = first name, p[2] = last name, p[3] = country
        if int(r[0]) < 101:
            if not r[1] in top100players:
                top100players.append(r[1])
                for p in players:
                    if r[1] == p[0]:
                        p[3] = p[3].replace("\n", "")
                        if p[3] in (y for x in countries for y in x):
                            x = 0
                            while x < len(countries):
                                y = 0
                                while y < len(countries[x]):
                                    if countries[x][y] == p[3]:
                                        countries[x][y+1] = int(countries[x][y+1])
                                        countries[x][y+1] += 1
                                        countries[x][y+2].append(p[1] + " " + p[2])
                                    y = y + 1
                                x = x + 1
                        else:
                            countries.append([p[3], int(1), [p[1] + " " + p[2]]])
    for c in countries:
        writer.writerow([c[0], c[1], c[2]])
    playersRank.clear()
    countries.clear()
    top100players.clear()



#ATP 2010-2019
# populate playersRank list with player id and rank with 10s ranking
with open("../../data/tennis_atp/atp_rankings_10s.csv", "r", encoding="utf8") as ranking_file:
    first_line = next(ranking_file)
    first_line = first_line.split(",")

    for line in ranking_file:
        player = line.split(",")
        playersRank.append([player[1], player[2]])
        #print(playersRank)

    ranking_file.close()


#write a csv file with countries and number of players for every country for the 10's rank
with open('../../data/preprocessed/map/atp_players_with_rank_10s.csv', 'w', newline='', encoding="utf8") as output:
    print("Start output phase")
    writer = csv.writer(output, delimiter=",")
    writer_header = csv.DictWriter(output, fieldnames=["country", "n_players", "players"])
    writer_header.writeheader()
    top100players = list()
    countries = list()

    for r in playersRank: #r[0] = rank, r[1] = id, p[0] = id, p[1] = first name, p[2] = last name, p[3] = country
        if int(r[0]) < 101:
            if not r[1] in top100players:
                top100players.append(r[1])
                for p in players:
                    if r[1] == p[0]:
                        p[3] = p[3].replace("\n", "")
                        if p[3] in (y for x in countries for y in x):
                            x = 0
                            while x < len(countries):
                                y = 0
                                while y < len(countries[x]):
                                    if countries[x][y] == p[3]:
                                        countries[x][y+1] = int(countries[x][y+1])
                                        countries[x][y+1] += 1
                                        countries[x][y+2].append(p[1] + " " + p[2])
                                    y = y + 1
                                x = x + 1
                        else:
                            countries.append([p[3], int(1), [p[1] + " " + p[2]]])
    for c in countries:
        writer.writerow([c[0], c[1], c[2]])
    playersRank.clear()
    countries.clear()
    top100players.clear()


#ATP 2000-2009
# populate playersRank list with player id and rank with 00s ranking
with open("../../data/tennis_atp/atp_rankings_00s.csv", "r", encoding="utf8") as ranking_file:
    first_line = next(ranking_file)
    first_line = first_line.split(",")

    for line in ranking_file:
        player = line.split(",")
        playersRank.append([player[1], player[2]])
        #print(playersRank)

    ranking_file.close()

#write a csv file with countries and number of players for every country for the 00's rank
with open('../../data/preprocessed/map/atp_players_with_rank_00s.csv', 'w', newline='', encoding="utf8") as output:
    print("Start output phase")
    writer = csv.writer(output, delimiter=",")
    writer_header = csv.DictWriter(output, fieldnames=["country", "n_players", "players"])
    writer_header.writeheader()
    top100players = list()
    countries = list()

    for r in playersRank: #r[0] = rank, r[1] = id, p[0] = id, p[1] = first name, p[2] = last name, p[3] = country
        if int(r[0]) < 101:
            if not r[1] in top100players:
                top100players.append(r[1])
                for p in players:
                    if r[1] == p[0]:
                        p[3] = p[3].replace("\n", "")
                        if p[3] in (y for x in countries for y in x):
                            x = 0
                            while x < len(countries):
                                y = 0
                                while y < len(countries[x]):
                                    if countries[x][y] == p[3]:
                                        countries[x][y+1] = int(countries[x][y+1])
                                        countries[x][y+1] += 1
                                        countries[x][y+2].append(p[1] + " " + p[2])
                                    y = y + 1
                                x = x + 1
                        else:
                            countries.append([p[3], int(1), [p[1] + " " + p[2]]])
    for c in countries:
        writer.writerow([c[0], c[1], c[2]])
    playersRank.clear()
    countries.clear()
    top100players.clear()


#ATP 1990-1999
# populate playersRank list with player id and rank with 90s ranking
with open("../../data/tennis_atp/atp_rankings_90s.csv", "r", encoding="utf8") as ranking_file:
    first_line = next(ranking_file)
    first_line = first_line.split(",")

    for line in ranking_file:
        player = line.split(",")
        playersRank.append([player[1], player[2]])
        #print(playersRank)

    ranking_file.close()

#write a csv file with countries and number of players for every country for the 90's rank
with open('../../data/preprocessed/map/atp_players_with_rank_90s.csv', 'w', newline='', encoding="utf8") as output:
    print("Start output phase")
    writer = csv.writer(output, delimiter=",")
    writer_header = csv.DictWriter(output, fieldnames=["country", "n_players", "players"])
    writer_header.writeheader()
    top100players = list()
    countries = list()

    for r in playersRank: #r[0] = rank, r[1] = id, p[0] = id, p[1] = first name, p[2] = last name, p[3] = country
        if int(r[0]) < 101:
            if not r[1] in top100players:
                top100players.append(r[1])
                for p in players:
                    if r[1] == p[0]:
                        p[3] = p[3].replace("\n", "")
                        if p[3] in (y for x in countries for y in x):
                            x = 0
                            while x < len(countries):
                                y = 0
                                while y < len(countries[x]):
                                    if countries[x][y] == p[3]:
                                        countries[x][y+1] = int(countries[x][y+1])
                                        countries[x][y+1] += 1
                                        countries[x][y+2].append(p[1] + " " + p[2])
                                    y = y + 1
                                x = x + 1
                        else:
                            countries.append([p[3], int(1), [p[1] + " " + p[2]]])
    for c in countries:
        writer.writerow([c[0], c[1], c[2]])
    playersRank.clear()
    countries.clear()
    top100players.clear()


#ATP 1980-1989
# populate playersRank list with player id and rank with 80s ranking
with open("../../data/tennis_atp/atp_rankings_80s.csv", "r", encoding="utf8") as ranking_file:
    first_line = next(ranking_file)
    first_line = first_line.split(",")

    for line in ranking_file:
        player = line.split(",")
        playersRank.append([player[1], player[2]])
        #print(playersRank)
    ranking_file.close()

#write a csv file with countries and number of players for every country for the 80's rank
with open('../../data/preprocessed/map/atp_players_with_rank_80s.csv', 'w', newline='', encoding="utf8") as output:
    print("Start output phase")
    writer = csv.writer(output, delimiter=",")
    writer_header = csv.DictWriter(output, fieldnames=["country", "n_players", "players"])
    writer_header.writeheader()
    top100players = list()
    countries = list()

    for r in playersRank: #r[0] = rank, r[1] = id, p[0] = id, p[1] = first name, p[2] = last name, p[3] = country
        if int(r[0]) < 101:
            if not r[1] in top100players:
                top100players.append(r[1])
                for p in players:
                    if r[1] == p[0]:
                        p[3] = p[3].replace("\n", "")
                        if p[3] in (y for x in countries for y in x):
                            x = 0
                            while x < len(countries):
                                y = 0
                                while y < len(countries[x]):
                                    if countries[x][y] == p[3]:
                                        countries[x][y+1] = int(countries[x][y+1])
                                        countries[x][y+1] += 1
                                        countries[x][y+2].append(p[1] + " " + p[2])
                                    y = y + 1
                                x = x + 1
                        else:
                            countries.append([p[3], int(1), [p[1] + " " + p[2]]])
    for c in countries:
        writer.writerow([c[0], c[1], c[2]])
    playersRank.clear()
    countries.clear()
    top100players.clear()
    players.clear()


print("Finished ATP preprocessing")



###     WTA
#populate players with player's id, first name, last name and country
with open("../../data/tennis_wta/wta_players.csv", "r", encoding="utf8") as players_file:
    print("Start WTA preprocessing")
    first_line = next(players_file)
    first_line = first_line.split(",")

    for line in players_file:
        player = line.split(",")
        players.append([player[0], player[1], player[2], player[5]])
        #print(players)

    players_file.close()

# populate playersRank list with rank with current ranking and player id
with open("../../data/tennis_wta/wta_rankings_current.csv", "r", encoding="utf8") as ranking_file:
    first_line = next(ranking_file)
    first_line = first_line.split(",")

    for line in ranking_file:
        player = line.split(",")
        playersRank.append([player[1], player[2]])
        #print(playersRank)

    ranking_file.close()

for i in ["80", "90", "00", "10", "20"]:
    with open("../../data/tennis_wta/wta_rankings_"+ i +"s.csv", "r", encoding="utf8") as ranking_file:
        first_line = next(ranking_file)
        first_line = first_line.split(",")

        for line in ranking_file:
            player = line.split(",")
            playersRank.append([player[1], player[2]])
            #print(playersRank)

        ranking_file.close()

#write a csv file with countries and number of players for every country for the actual ranking
with open('../../data/preprocessed/map/wta_players_with_rank_all-time.csv', 'w', newline='', encoding="utf8") as output:
    print("Start output phase")
    writer = csv.writer(output, delimiter=",")
    writer_header = csv.DictWriter(output, fieldnames=["country", "n_players", "players"])
    writer_header.writeheader()
    top100players = list()
    countries = list()

    for r in playersRank: #r[0] = rank, r[1] = id, p[0] = id, p[1] = first name, p[2] = last name, p[3] = country
        if int(r[0]) < 101:
            if not r[1] in top100players:
                top100players.append(r[1])
                for p in players:
                    if r[1] == p[0]:
                        p[3] = p[3].replace("\n", "")
                        if p[3] in (y for x in countries for y in x):
                            x = 0
                            while x < len(countries):
                                y = 0
                                while y < len(countries[x]):
                                    if countries[x][y] == p[3]:
                                        countries[x][y+1] = int(countries[x][y+1])
                                        countries[x][y+1] += 1
                                        countries[x][y+2].append(p[1] + " " + p[2])
                                    y = y + 1
                                x = x + 1
                        else:
                            countries.append([p[3], int(1), [p[1] + " " + p[2]]])
    for c in countries:
        writer.writerow([c[0], c[1], c[2]])
    playersRank.clear()
    countries.clear()
    top100players.clear()


#WTA 2021
# populate playersRank list with player id and rank with current ranking
with open("../../data/tennis_wta/wta_rankings_current.csv", "r", encoding="utf8") as ranking_file:
    first_line = next(ranking_file)
    first_line = first_line.split(",")

    for line in ranking_file:
        player = line.split(",")
        playersRank.append([player[1], player[2]])
        #print(playersRank)

    ranking_file.close()

#write a csv file with countries and number of players for every country for the actual ranking
with open('../../data/preprocessed/map/wta_players_with_rank.csv', 'w', newline='', encoding="utf8") as output:
    print("Start output phase")
    writer = csv.writer(output, delimiter=",")
    writer_header = csv.DictWriter(output, fieldnames=["country", "n_players", "players"])
    writer_header.writeheader()
    top100players = list()
    countries = list()

    for r in playersRank: #r[0] = rank, r[1] = id, p[0] = id, p[1] = first name, p[2] = last name, p[3] = country
        if int(r[0]) < 101:
            if not r[1] in top100players:
                top100players.append(r[1])
                for p in players:
                    if r[1] == p[0]:
                        p[3] = p[3].replace("\n", "")
                        if p[3] in (y for x in countries for y in x):
                            x = 0
                            while x < len(countries):
                                y = 0
                                while y < len(countries[x]):
                                    if countries[x][y] == p[3]:
                                        countries[x][y+1] = int(countries[x][y+1])
                                        countries[x][y+1] += 1
                                        countries[x][y+2].append(p[1] + " " + p[2])
                                    y = y + 1
                                x = x + 1
                        else:
                            countries.append([p[3], int(1), [p[1] + " " + p[2]]])
    for c in countries:
        writer.writerow([c[0], c[1], c[2]])
    playersRank.clear()
    countries.clear()
    top100players.clear()


#WTA 2020-2021
# populate playersRank list with player id and rank with 20s ranking
with open("../../data/tennis_wta/wta_rankings_20s.csv", "r", encoding="utf8") as ranking_file:
    first_line = next(ranking_file)
    first_line = first_line.split(",")

    for line in ranking_file:
        player = line.split(",")
        playersRank.append([player[1], player[2]])
        #print(playersRank)

    ranking_file.close()

#write a csv file with countries and number of players for every country for the 20's rank
with open('../../data/preprocessed/map/wta_players_with_rank_20s.csv', 'w', newline='', encoding="utf8") as output:
    print("Start output phase")
    writer = csv.writer(output, delimiter=",")
    writer_header = csv.DictWriter(output, fieldnames=["country", "n_players", "players"])
    writer_header.writeheader()
    top100players = list()
    countries = list()

    for r in playersRank: #r[0] = rank, r[1] = id, p[0] = id, p[1] = first name, p[2] = last name, p[3] = country
        if int(r[0]) < 101:
            if not r[1] in top100players:
                top100players.append(r[1])
                for p in players:
                    if r[1] == p[0]:
                        p[3] = p[3].replace("\n", "")
                        if p[3] in (y for x in countries for y in x):
                            x = 0
                            while x < len(countries):
                                y = 0
                                while y < len(countries[x]):
                                    if countries[x][y] == p[3]:
                                        countries[x][y+1] = int(countries[x][y+1])
                                        countries[x][y+1] += 1
                                        countries[x][y+2].append(p[1] + " " + p[2])
                                    y = y + 1
                                x = x + 1
                        else:
                            countries.append([p[3], int(1), [p[1] + " " + p[2]]])
    for c in countries:
        writer.writerow([c[0], c[1], c[2]])
    playersRank.clear()
    countries.clear()
    top100players.clear()


#WTA 2010-2019
# populate playersRank list with player id and rank with 10s ranking
with open("../../data/tennis_wta/wta_rankings_10s.csv", "r", encoding="utf8") as ranking_file:
    first_line = next(ranking_file)
    first_line = first_line.split(",")

    for line in ranking_file:
        player = line.split(",")
        playersRank.append([player[1], player[2]])
        #print(playersRank)

    ranking_file.close()

#write a csv file with countries and number of players for every country for the 10's rank
with open('../../data/preprocessed/map/wta_players_with_rank_10s.csv', 'w', newline='', encoding="utf8") as output:
    print("Start output phase")
    writer = csv.writer(output, delimiter=",")
    writer_header = csv.DictWriter(output, fieldnames=["country", "n_players", "players"])
    writer_header.writeheader()
    top100players = list()
    countries = list()

    for r in playersRank: #r[0] = rank, r[1] = id, p[0] = id, p[1] = first name, p[2] = last name, p[3] = country
        if int(r[0]) < 101:
            if not r[1] in top100players:
                top100players.append(r[1])
                for p in players:
                    if r[1] == p[0]:
                        p[3] = p[3].replace("\n", "")
                        if p[3] in (y for x in countries for y in x):
                            x = 0
                            while x < len(countries):
                                y = 0
                                while y < len(countries[x]):
                                    if countries[x][y] == p[3]:
                                        countries[x][y+1] = int(countries[x][y+1])
                                        countries[x][y+1] += 1
                                        countries[x][y+2].append(p[1] + " " + p[2])
                                    y = y + 1
                                x = x + 1
                        else:
                            countries.append([p[3], int(1), [p[1] + " " + p[2]]])
    for c in countries:
        writer.writerow([c[0], c[1], c[2]])
    playersRank.clear()
    countries.clear()
    top100players.clear()


#WTA 2000-2009
# populate playersRank list with player id and rank with 00s ranking
with open("../../data/tennis_wta/wta_rankings_00s.csv", "r", encoding="utf8") as ranking_file:
    first_line = next(ranking_file)
    first_line = first_line.split(",")

    for line in ranking_file:
        player = line.split(",")
        playersRank.append([player[1], player[2]])
        #print(playersRank)

    ranking_file.close()

#write a csv file with countries and number of players for every country for the 00's rank
with open('../../data/preprocessed/map/wta_players_with_rank_00s.csv', 'w', newline='', encoding="utf8") as output:
    print("Start output phase")
    writer = csv.writer(output, delimiter=",")
    writer_header = csv.DictWriter(output, fieldnames=["country", "n_players", "players"])
    writer_header.writeheader()
    top100players = list()
    countries = list()

    for r in playersRank: #r[0] = rank, r[1] = id, p[0] = id, p[1] = first name, p[2] = last name, p[3] = country
        if int(r[0]) < 101:
            if not r[1] in top100players:
                top100players.append(r[1])
                for p in players:
                    if r[1] == p[0]:
                        p[3] = p[3].replace("\n", "")
                        if p[3] in (y for x in countries for y in x):
                            x = 0
                            while x < len(countries):
                                y = 0
                                while y < len(countries[x]):
                                    if countries[x][y] == p[3]:
                                        countries[x][y+1] = int(countries[x][y+1])
                                        countries[x][y+1] += 1
                                        countries[x][y+2].append(p[1] + " " + p[2])
                                    y = y + 1
                                x = x + 1
                        else:
                            countries.append([p[3], int(1), [p[1] + " " + p[2]]])
    for c in countries:
        writer.writerow([c[0], c[1], c[2]])
    playersRank.clear()
    countries.clear()
    top100players.clear()


#WTA 1990-1999
# populate playersRank list with player id and rank with 90s ranking
with open("../../data/tennis_wta/wta_rankings_90s.csv", "r", encoding="utf8") as ranking_file:
    first_line = next(ranking_file)
    first_line = first_line.split(",")

    for line in ranking_file:
        player = line.split(",")
        playersRank.append([player[1], player[2]])
        #print(playersRank)

    ranking_file.close()

#write a csv file with countries and number of players for every country for the 90's rank
with open('../../data/preprocessed/map/wta_players_with_rank_90s.csv', 'w', newline='', encoding="utf8") as output:
    print("Start output phase")
    writer = csv.writer(output, delimiter=",")
    writer_header = csv.DictWriter(output, fieldnames=["country", "n_players", "players"])
    writer_header.writeheader()
    top100players = list()
    countries = list()

    for r in playersRank: #r[0] = rank, r[1] = id, p[0] = id, p[1] = first name, p[2] = last name, p[3] = country
        if int(r[0]) < 101:
            if not r[1] in top100players:
                top100players.append(r[1])
                for p in players:
                    if r[1] == p[0]:
                        p[3] = p[3].replace("\n", "")
                        if p[3] in (y for x in countries for y in x):
                            x = 0
                            while x < len(countries):
                                y = 0
                                while y < len(countries[x]):
                                    if countries[x][y] == p[3]:
                                        countries[x][y+1] = int(countries[x][y+1])
                                        countries[x][y+1] += 1
                                        countries[x][y+2].append(p[1] + " " + p[2])
                                    y = y + 1
                                x = x + 1
                        else:
                            countries.append([p[3], int(1), [p[1] + " " + p[2]]])
    for c in countries:
        writer.writerow([c[0], c[1], c[2]])
    playersRank.clear()
    countries.clear()
    top100players.clear()


#WTA 1980-1989
# populate playersRank list with player id and rank with 80s ranking
with open("../../data/tennis_wta/wta_rankings_80s.csv", "r", encoding="utf8") as ranking_file:
    first_line = next(ranking_file)
    first_line = first_line.split(",")

    for line in ranking_file:
        player = line.split(",")
        playersRank.append([player[1], player[2]])
        #print(playersRank)
    ranking_file.close()

#write a csv file with countries and number of players for every country for the 80's rank
with open('../../data/preprocessed/map/wta_players_with_rank_80s.csv', 'w', newline='', encoding="utf8") as output:
    print("Start output phase")
    writer = csv.writer(output, delimiter=",")
    writer_header = csv.DictWriter(output, fieldnames=["country", "n_players", "players"])
    writer_header.writeheader()
    top100players = list()
    countries = list()

    for r in playersRank: #r[0] = rank, r[1] = id, p[0] = id, p[1] = first name, p[2] = last name, p[3] = country
        if int(r[0]) < 101:
            if not r[1] in top100players:
                top100players.append(r[1])
                for p in players:
                    if r[1] == p[0]:
                        p[3] = p[3].replace("\n", "")
                        if p[3] in (y for x in countries for y in x):
                            x = 0
                            while x < len(countries):
                                y = 0
                                while y < len(countries[x]):
                                    if countries[x][y] == p[3]:
                                        countries[x][y+1] = int(countries[x][y+1])
                                        countries[x][y+1] += 1
                                        countries[x][y+2].append(p[1] + " " + p[2])
                                    y = y + 1
                                x = x + 1
                        else:
                            countries.append([p[3], int(1), [p[1] + " " + p[2]]])
    for c in countries:
        writer.writerow([c[0], c[1], c[2]])
    playersRank.clear()
    countries.clear()
    top100players.clear()

print("Finished WTA preprocessing")
