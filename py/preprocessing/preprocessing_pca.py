import csv

players = list()
matches = list()
statistics = list()
writable = list()

#ATP 2021
with open("../../data/tennis_atp/atp_rankings_current.csv", "r", encoding="utf8") as ranking_file:
    first_line = next(ranking_file)
    first_line = first_line.split(",")

    for line in ranking_file:
        player = line.split(",")
        if int(player[1]) <= 20 and not player[2] in players:
            players.append(player[2])
            print(players)

    ranking_file.close()

with open("../../data/tennis_atp/atp_matches_2021.csv", "r", encoding="utf8") as matches_file:      # 0 = w_id, 1 = w_name, 2 = l_id, 3 = l_name, 4 = w_ace, 5 = w_df, 6 = w_svpt, 7 = w_1stin, 8 = w_1stwon
    first_line = next(matches_file)                                                     # 9 = w_2ndwon, 10 = w_svgms, 11 = w_bpsaved, 12 = w_bpfaced, 13 = l_ace, 14 = l_df, 15 = l_svpt
    first_line = first_line.split(",")                                                  # 16 = l_1stin, 17 = l_1stwon, 18 = l_2ndwon, 19 = l_svgms, 20 = l_bpsaved, 21 = l_bpfaced, 22 = surface
    for line in matches_file:
        match = line.split(",")
        matches.append([match[7], match[10], match[15], match[18], match[27], match[28], match[29], match[30], match[31], match[32], match[33], match[34],
                        match[35], match[36], match[37], match[38], match[39], match[40], match[41], match[42], match[43], match[44], match[2]])
        #print(matches)

    matches_file.close()

with open("../../data/preprocessed/pca/atp_players_statistics_2021.csv", "w", newline='', encoding="utf8") as output:    # 0 = id, 1 = name, 2 = surname, 3 = ace , 4 = df, 5 = 1stWon
    writer = csv.writer(output, delimiter=",")                                                                  # 6 = 2ndWon, 7 = svGames, 8 = bpSaved, 9 = matches
    writer_header = csv.DictWriter(output, fieldnames=["id", "name", "ace", "df", "1stWon", "2ndWon", "bpSaved", "bpLost", "matches", "hard", "clay", "grass"])
    writer_header.writeheader()

    inserted = list()

    # statistics: 0 = id, 1 = name, 2 = ace, 3 = df, 4 = svPoints, 5 = 1stin, 6 = 1stwon, 7 = 2ndIn, 8 = 2ndwon, 8 = svGms, 9 = bpSaved, 10 = bpFaced, 11 = opponent_bpSaved
    for m in matches:                                                              # 12 = opponent_bpFaced , 13 = matches, 14 = hard, 15 = clay, 16 = grass
        if m[0] in (y for x in statistics for y in x) and m[0] in players:
            x = 0
            while x < len(statistics):
                y = 0
                while y < len(statistics[x]):
                    if statistics[x][0] == m[0]:
                        statistics[x][13] += 1      #update matches played
                        try:
                            statistics[x][6] = str(float(statistics[x][6]) + float(m[8]))   #update 1stWon
                            statistics[x][5] = str(int(statistics[x][5]) + int(m[7]))   #update 1stIn
                            statistics[x][8] = str(int(statistics[x][8]) + int(m[9]))   #update 2ndWon
                            statistics[x][7] = str(int(statistics[x][7]) + (int(m[6]) - (int(m[7]) + int(m[5]))))   #2ndIn = svPoints - (1stIn + doubleFaults)
                            statistics[x][2] = str(int(statistics[x][2]) + int(m[4]))   #update ace
                            statistics[x][4] = str(int(statistics[x][4]) + int(m[6]))   #update servicePoints
                            statistics[x][3] = str(int(statistics[x][3]) + int(m[5]))   #update doubleFaults
                            statistics[x][9] = str(int(statistics[x][9]) + int(m[11]))  #update bpSaved
                            statistics[x][10] = str(int(statistics[x][10]) + int(m[12]))    #update bpFaced
                            statistics[x][11] = str(int(statistics[x][11]) + int(m[20]))    #update opponent_bpSaved
                            statistics[x][12] = str(int(statistics[x][12]) + int(m[21]))    #update opponent_bpFaced
                            if m[22] == "Hard":
                                statistics[x][14] = str(int(statistics[x][14]) + 1)    #update hard victories
                            elif m[22] == "Clay":
                                statistics[x][15] = str(int(statistics[x][15]) + 1)    #update clay victories
                            else:
                                statistics[x][16] = str(int(statistics[x][16]) + 1)    #update grass victories
                            print(statistics[x])
                            break
                        except:
                            break
                    y = y + 1
                x = x + 1
        if not m[0] in inserted:
            if m[0] == "" or m[1] == "" or m[4] == "" or m[5] == "" or m[6] == "" or m[7] == "" or m[8] == "" or m[9] == "" or m[10] == "" or m[11] == "" or m[12] == "" or m[20] == "" or m[21] == "":
                continue
            else:
                inserted.append(m[0])
                if m[22] == "Hard":
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 1, 0, 0])
                elif m[22] == "Clay":
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 0, 1, 0])
                else:
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 0, 0, 1])
        if m[2] in (y for x in statistics for y in x) and m[2] in players:
            x = 0
            while x < len(statistics):
                y = 0
                while y < len(statistics[x]):
                    if statistics[x][0] == m[2]:
                        statistics[x][13] += 1      #update matches played
                        try:
                            statistics[x][6] = str(float(statistics[x][6]) + float(m[17]))   #update 1stWon
                            statistics[x][5] = str(int(statistics[x][5]) + int(m[16]))   #update 1stIn
                            statistics[x][8] = str(int(statistics[x][8]) + int(m[18]))   #update 2ndWon
                            statistics[x][7] = str(int(statistics[x][7]) + (int(m[15]) - (int(m[16]) + int(m[14]))))   #2ndIn = svPoints - (1stIn + doubleFaults)
                            statistics[x][2] = str(int(statistics[x][2]) + int(m[13]))   #update ace
                            statistics[x][4] = str(int(statistics[x][4]) + int(m[15]))   #update servicePoints
                            statistics[x][3] = str(int(statistics[x][3]) + int(m[14]))   #update doubleFaults
                            statistics[x][9] = str(int(statistics[x][9]) + int(m[20]))  #update bpSaved
                            statistics[x][10] = str(int(statistics[x][10]) + int(m[21]))    #update bpFaced
                            statistics[x][11] = str(int(statistics[x][11]) + int(m[11]))    #update opponent_bpSaved
                            statistics[x][12] = str(int(statistics[x][12]) + int(m[12]))    #update opponent_bpFaced
                            break
                        except:
                            break
                    y = y + 1
                x = x + 1
        if not m[2] in inserted:
            if m[2] == "" or m[3] == "" or m[13] == "" or m[14] == "" or m[15] == "" or m[16] == "" or m[17] == "" or m[18] == "" or m[19] == "" or m[20] == "" or m[21] == "" or m[11] == "" or m[12] == "":
                continue
            else:
                inserted.append(m[2])
                statistics.append([m[2], m[3], m[13], m[14], m[15], m[16], m[17], m[18], m[19], m[20], m[21], m[11], m[12], 1, 0, 0, 0])
    x = 0
    while x < len(statistics):
        y = 0
        while y < len(statistics[x]):
            try:
                if float(statistics[x][6]) > float(statistics[x][5]):
                    firstServeWon_p = 0
                else:
                    firstServeWon_p = str(float(statistics[x][6]) / float(statistics[x][5]))
                #if firstServeWon_p > 1:
                #    firstServeWon = 0
                if int(statistics[x][8]) > int(statistics[x][7]):
                    secondServeWon_p = 0
                else:
                    secondServeWon_p = str(int(statistics[x][8]) / int(statistics[x][7]))
                #if secondServeWon_p > 1:
                #    secondServeWon_p = 0
                if int(statistics[x][2]) > int(statistics[x][4]):
                    ace_p = 0
                else:
                    ace_p = str(int(statistics[x][2]) / int(statistics[x][4]))
                #if ace_p > 1:
                #    ace_p = 0
                if int(statistics[x][3]) > int(statistics[x][4]):
                    doubleFaults_p = 0
                else:
                    doubleFaults_p = str(int(statistics[x][3]) / int(statistics[x][4]))
                #if doubleFaults_p > 1:
                #    doubleFaults_p = 0
                if not int(statistics[x][10]) == 0:
                    if int(statistics[x][9]) > int(statistics[x][10]):
                        breakPointsSaved_p = 0
                    else:
                        breakPointsSaved_p = str(int(statistics[x][9]) / int(statistics[x][10]))
                #    if breakPointsSaved_p > 1:
                #        breakPointsSaved_p = 0
                else:
                    breakPointsSaved_p = 0
                if not int(statistics[x][12]) == 0:
                    if int(statistics[x][11]) > int(statistics[x][12]):
                        opponentBreakPoints_p = 0
                    else:
                        opponentBreakPoints_p = str( 1 - (int(statistics[x][11]) / int(statistics[x][12])))
                    #if opponentBreakPoints_p > 1:
                    #    opponentBreakPoints_p = 0
                else:
                    opponentBreakPoints_p = 0
            except:
                break
            writable.append([statistics[x][0], statistics[x][1], ace_p, doubleFaults_p, firstServeWon_p, secondServeWon_p, breakPointsSaved_p, opponentBreakPoints_p, statistics[x][13], statistics[x][14], statistics[x][15], statistics[x][16]])
            break
            y = y +1
        x = x + 1

    print(writable)
    for w in writable:
        writer.writerow([w[0], w[1], w[2], w[3], w[4], w[5], w[6], w[7], w[8], w[9], w[10], w[11]])

    players.clear()
    matches.clear()
    inserted.clear()
    statistics.clear()
    writable.clear()


#ATP 2020/21
with open("../../data/tennis_atp/atp_rankings_20s.csv", "r", encoding="utf8") as ranking_file:
    first_line = next(ranking_file)
    first_line = first_line.split(",")

    for line in ranking_file:
        player = line.split(",")
        if int(player[1]) <= 20 and not player[2] in players:
            players.append(player[2])
            print(players)

    ranking_file.close()

for i in range(2020, 2021):
    with open("../../data/tennis_atp/atp_matches_" + str(i) + ".csv", "r", encoding="utf8") as matches_file:      # 0 = w_id, 1 = w_name, 2 = l_id, 3 = l_name, 4 = w_ace, 5 = w_df, 6 = w_svpt, 7 = w_1stin, 8 = w_1stwon
        first_line = next(matches_file)                                                     # 9 = w_2ndwon, 10 = w_svgms, 11 = w_bpsaved, 12 = w_bpfaced, 13 = l_ace, 14 = l_df, 15 = l_svpt
        first_line = first_line.split(",")                                                  # 16 = l_1stin, 17 = l_1stwon, 18 = l_2ndwon, 19 = l_svgms, 20 = l_bpsaved, 21 = l_bpfaced, 22 = surface
        for line in matches_file:
            match = line.split(",")
            matches.append([match[7], match[10], match[15], match[18], match[27], match[28], match[29], match[30], match[31], match[32], match[33], match[34],
                            match[35], match[36], match[37], match[38], match[39], match[40], match[41], match[42], match[43], match[44], match[2]])
            #print(matches)

        matches_file.close()

with open("../../data/preprocessed/pca/atp_players_statistics_2020.csv", "w", newline='', encoding="utf8") as output:    # 0 = id, 1 = name, 2 = surname, 3 = ace , 4 = df, 5 = 1stWon
    writer = csv.writer(output, delimiter=",")                                                                  # 6 = 2ndWon, 7 = svGames, 8 = bpSaved, 9 = matches
    writer_header = csv.DictWriter(output, fieldnames=["id", "name", "ace", "df", "1stWon", "2ndWon", "bpSaved", "bpLost", "matches", "hard", "clay", "grass"])
    writer_header.writeheader()

    inserted = list()

    # statistics: 0 = id, 1 = name, 2 = ace, 3 = df, 4 = svPoints, 5 = 1stin, 6 = 1stwon, 7 = 2ndIn, 8 = 2ndwon, 8 = svGms, 9 = bpSaved, 10 = bpFaced, 11 = opponent_bpSaved
    for m in matches:                                                              # 12 = opponent_bpFaced , 13 = matches, 14 = hard, 15 = clay, 16 = grass
        if m[0] in (y for x in statistics for y in x) and m[0] in players:
            x = 0
            while x < len(statistics):
                y = 0
                while y < len(statistics[x]):
                    if statistics[x][0] == m[0]:
                        statistics[x][13] += 1      #update matches played
                        try:
                            statistics[x][6] = str(float(statistics[x][6]) + float(m[8]))   #update 1stWon
                            statistics[x][5] = str(int(statistics[x][5]) + int(m[7]))   #update 1stIn
                            statistics[x][8] = str(int(statistics[x][8]) + int(m[9]))   #update 2ndWon
                            statistics[x][7] = str(int(statistics[x][7]) + (int(m[6]) - (int(m[7]) + int(m[5]))))   #2ndIn = svPoints - (1stIn + doubleFaults)
                            statistics[x][2] = str(int(statistics[x][2]) + int(m[4]))   #update ace
                            statistics[x][4] = str(int(statistics[x][4]) + int(m[6]))   #update servicePoints
                            statistics[x][3] = str(int(statistics[x][3]) + int(m[5]))   #update doubleFaults
                            statistics[x][9] = str(int(statistics[x][9]) + int(m[11]))  #update bpSaved
                            statistics[x][10] = str(int(statistics[x][10]) + int(m[12]))    #update bpFaced
                            statistics[x][11] = str(int(statistics[x][11]) + int(m[20]))    #update opponent_bpSaved
                            statistics[x][12] = str(int(statistics[x][12]) + int(m[21]))    #update opponent_bpFaced
                            if m[22] == "Hard":
                                statistics[x][14] = str(int(statistics[x][14]) + 1)    #update hard victories
                            elif m[22] == "Clay":
                                statistics[x][15] = str(int(statistics[x][15]) + 1)    #update clay victories
                            else:
                                statistics[x][16] = str(int(statistics[x][16]) + 1)    #update grass victories
                            print(statistics[x])
                            break
                        except:
                            break
                    y = y + 1
                x = x + 1
        if not m[0] in inserted:
            if m[0] == "" or m[1] == "" or m[4] == "" or m[5] == "" or m[6] == "" or m[7] == "" or m[8] == "" or m[9] == "" or m[10] == "" or m[11] == "" or m[12] == "" or m[20] == "" or m[21] == "":
                continue
            else:
                inserted.append(m[0])
                if m[22] == "Hard":
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 1, 0, 0])
                elif m[22] == "Clay":
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 0, 1, 0])
                else:
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 0, 0, 1])
        if m[2] in (y for x in statistics for y in x) and m[2] in players:
            x = 0
            while x < len(statistics):
                y = 0
                while y < len(statistics[x]):
                    if statistics[x][0] == m[2]:
                        statistics[x][13] += 1      #update matches played
                        try:
                            statistics[x][6] = str(float(statistics[x][6]) + float(m[17]))   #update 1stWon
                            statistics[x][5] = str(int(statistics[x][5]) + int(m[16]))   #update 1stIn
                            statistics[x][8] = str(int(statistics[x][8]) + int(m[18]))   #update 2ndWon
                            statistics[x][7] = str(int(statistics[x][7]) + (int(m[15]) - (int(m[16]) + int(m[14]))))   #2ndIn = svPoints - (1stIn + doubleFaults)
                            statistics[x][2] = str(int(statistics[x][2]) + int(m[13]))   #update ace
                            statistics[x][4] = str(int(statistics[x][4]) + int(m[15]))   #update servicePoints
                            statistics[x][3] = str(int(statistics[x][3]) + int(m[14]))   #update doubleFaults
                            statistics[x][9] = str(int(statistics[x][9]) + int(m[20]))  #update bpSaved
                            statistics[x][10] = str(int(statistics[x][10]) + int(m[21]))    #update bpFaced
                            statistics[x][11] = str(int(statistics[x][11]) + int(m[11]))    #update opponent_bpSaved
                            statistics[x][12] = str(int(statistics[x][12]) + int(m[12]))    #update opponent_bpFaced
                            break
                        except:
                            break
                    y = y + 1
                x = x + 1
        if not m[2] in inserted:
            if m[2] == "" or m[3] == "" or m[13] == "" or m[14] == "" or m[15] == "" or m[16] == "" or m[17] == "" or m[18] == "" or m[19] == "" or m[20] == "" or m[21] == "" or m[11] == "" or m[12] == "":
                continue
            else:
                inserted.append(m[2])
                statistics.append([m[2], m[3], m[13], m[14], m[15], m[16], m[17], m[18], m[19], m[20], m[21], m[11], m[12], 1, 0, 0, 0])
    x = 0
    while x < len(statistics):
        y = 0
        while y < len(statistics[x]):
            try:
                if float(statistics[x][6]) > float(statistics[x][5]):
                    firstServeWon_p = 0
                else:
                    firstServeWon_p = str(float(statistics[x][6]) / float(statistics[x][5]))
                #if firstServeWon_p > 1:
                #    firstServeWon = 0
                if int(statistics[x][8]) > int(statistics[x][7]):
                    secondServeWon_p = 0
                else:
                    secondServeWon_p = str(int(statistics[x][8]) / int(statistics[x][7]))
                #if secondServeWon_p > 1:
                #    secondServeWon_p = 0
                if int(statistics[x][2]) > int(statistics[x][4]):
                    ace_p = 0
                else:
                    ace_p = str(int(statistics[x][2]) / int(statistics[x][4]))
                #if ace_p > 1:
                #    ace_p = 0
                if int(statistics[x][3]) > int(statistics[x][4]):
                    doubleFaults_p = 0
                else:
                    doubleFaults_p = str(int(statistics[x][3]) / int(statistics[x][4]))
                #if doubleFaults_p > 1:
                #    doubleFaults_p = 0
                if not int(statistics[x][10]) == 0:
                    if int(statistics[x][9]) > int(statistics[x][10]):
                        breakPointsSaved_p = 0
                    else:
                        breakPointsSaved_p = str(int(statistics[x][9]) / int(statistics[x][10]))
                #    if breakPointsSaved_p > 1:
                #        breakPointsSaved_p = 0
                else:
                    breakPointsSaved_p = 0
                if not int(statistics[x][12]) == 0:
                    if int(statistics[x][11]) > int(statistics[x][12]):
                        opponentBreakPoints_p = 0
                    else:
                        opponentBreakPoints_p = str( 1 - (int(statistics[x][11]) / int(statistics[x][12])))
                    #if opponentBreakPoints_p > 1:
                    #    opponentBreakPoints_p = 0
                else:
                    opponentBreakPoints_p = 0
            except:
                break
            writable.append([statistics[x][0], statistics[x][1], ace_p, doubleFaults_p, firstServeWon_p, secondServeWon_p, breakPointsSaved_p, opponentBreakPoints_p, statistics[x][13], statistics[x][14], statistics[x][15], statistics[x][16]])
            break
            y = y +1
        x = x + 1

    print(writable)
    for w in writable:
        writer.writerow([w[0], w[1], w[2], w[3], w[4], w[5], w[6], w[7], w[8], w[9], w[10], w[11]])

    players.clear()
    matches.clear()
    inserted.clear()
    statistics.clear()
    writable.clear()


#ATP 2010/2019
with open("../../data/tennis_atp/atp_rankings_10s.csv", "r", encoding="utf8") as ranking_file:
    first_line = next(ranking_file)
    first_line = first_line.split(",")

    for line in ranking_file:
        player = line.split(",")
        if int(player[1]) <= 20 and not player[2] in players:
            players.append(player[2])
            print(players)

    ranking_file.close()

for i in range(2010, 2019):
    with open("../../data/tennis_atp/atp_matches_" + str(i) + ".csv", "r", encoding="utf8") as matches_file:      # 0 = w_id, 1 = w_name, 2 = l_id, 3 = l_name, 4 = w_ace, 5 = w_df, 6 = w_svpt, 7 = w_1stin, 8 = w_1stwon
        first_line = next(matches_file)                                                     # 9 = w_2ndwon, 10 = w_svgms, 11 = w_bpsaved, 12 = w_bpfaced, 13 = l_ace, 14 = l_df, 15 = l_svpt
        first_line = first_line.split(",")                                                  # 16 = l_1stin, 17 = l_1stwon, 18 = l_2ndwon, 19 = l_svgms, 20 = l_bpsaved, 21 = l_bpfaced, 22 = surface
        for line in matches_file:
            match = line.split(",")
            matches.append([match[7], match[10], match[15], match[18], match[27], match[28], match[29], match[30], match[31], match[32], match[33], match[34],
                            match[35], match[36], match[37], match[38], match[39], match[40], match[41], match[42], match[43], match[44], match[2]])
            #print(matches)

        matches_file.close()

with open("../../data/preprocessed/pca/atp_players_statistics_2010.csv", "w", newline='', encoding="utf8") as output:    # 0 = id, 1 = name, 2 = surname, 3 = ace , 4 = df, 5 = 1stWon
    writer = csv.writer(output, delimiter=",")                                                                  # 6 = 2ndWon, 7 = svGames, 8 = bpSaved, 9 = matches
    writer_header = csv.DictWriter(output, fieldnames=["id", "name", "ace", "df", "1stWon", "2ndWon", "bpSaved", "bpLost", "matches", "hard", "clay", "grass"])
    writer_header.writeheader()

    inserted = list()

    # statistics: 0 = id, 1 = name, 2 = ace, 3 = df, 4 = svPoints, 5 = 1stin, 6 = 1stwon, 7 = 2ndIn, 8 = 2ndwon, 8 = svGms, 9 = bpSaved, 10 = bpFaced, 11 = opponent_bpSaved
    for m in matches:                                                              # 12 = opponent_bpFaced , 13 = matches, 14 = hard, 15 = clay, 16 = grass
        if m[0] in (y for x in statistics for y in x) and m[0] in players:
            x = 0
            while x < len(statistics):
                y = 0
                while y < len(statistics[x]):
                    if statistics[x][0] == m[0]:
                        statistics[x][13] += 1      #update matches played
                        try:
                            statistics[x][6] = str(float(statistics[x][6]) + float(m[8]))   #update 1stWon
                            statistics[x][5] = str(int(statistics[x][5]) + int(m[7]))   #update 1stIn
                            statistics[x][8] = str(int(statistics[x][8]) + int(m[9]))   #update 2ndWon
                            statistics[x][7] = str(int(statistics[x][7]) + (int(m[6]) - (int(m[7]) + int(m[5]))))   #2ndIn = svPoints - (1stIn + doubleFaults)
                            statistics[x][2] = str(int(statistics[x][2]) + int(m[4]))   #update ace
                            statistics[x][4] = str(int(statistics[x][4]) + int(m[6]))   #update servicePoints
                            statistics[x][3] = str(int(statistics[x][3]) + int(m[5]))   #update doubleFaults
                            statistics[x][9] = str(int(statistics[x][9]) + int(m[11]))  #update bpSaved
                            statistics[x][10] = str(int(statistics[x][10]) + int(m[12]))    #update bpFaced
                            statistics[x][11] = str(int(statistics[x][11]) + int(m[20]))    #update opponent_bpSaved
                            statistics[x][12] = str(int(statistics[x][12]) + int(m[21]))    #update opponent_bpFaced
                            if m[22] == "Hard":
                                statistics[x][14] = str(int(statistics[x][14]) + 1)    #update hard victories
                            elif m[22] == "Clay":
                                statistics[x][15] = str(int(statistics[x][15]) + 1)    #update clay victories
                            else:
                                statistics[x][16] = str(int(statistics[x][16]) + 1)    #update grass victories
                            print(statistics[x])
                            break
                        except:
                            break
                    y = y + 1
                x = x + 1
        if not m[0] in inserted:
            if m[0] == "" or m[1] == "" or m[4] == "" or m[5] == "" or m[6] == "" or m[7] == "" or m[8] == "" or m[9] == "" or m[10] == "" or m[11] == "" or m[12] == "" or m[20] == "" or m[21] == "":
                continue
            else:
                inserted.append(m[0])
                if m[22] == "Hard":
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 1, 0, 0])
                elif m[22] == "Clay":
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 0, 1, 0])
                else:
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 0, 0, 1])
        if m[2] in (y for x in statistics for y in x) and m[2] in players:
            x = 0
            while x < len(statistics):
                y = 0
                while y < len(statistics[x]):
                    if statistics[x][0] == m[2]:
                        statistics[x][13] += 1      #update matches played
                        try:
                            statistics[x][6] = str(float(statistics[x][6]) + float(m[17]))   #update 1stWon
                            statistics[x][5] = str(int(statistics[x][5]) + int(m[16]))   #update 1stIn
                            statistics[x][8] = str(int(statistics[x][8]) + int(m[18]))   #update 2ndWon
                            statistics[x][7] = str(int(statistics[x][7]) + (int(m[15]) - (int(m[16]) + int(m[14]))))   #2ndIn = svPoints - (1stIn + doubleFaults)
                            statistics[x][2] = str(int(statistics[x][2]) + int(m[13]))   #update ace
                            statistics[x][4] = str(int(statistics[x][4]) + int(m[15]))   #update servicePoints
                            statistics[x][3] = str(int(statistics[x][3]) + int(m[14]))   #update doubleFaults
                            statistics[x][9] = str(int(statistics[x][9]) + int(m[20]))  #update bpSaved
                            statistics[x][10] = str(int(statistics[x][10]) + int(m[21]))    #update bpFaced
                            statistics[x][11] = str(int(statistics[x][11]) + int(m[11]))    #update opponent_bpSaved
                            statistics[x][12] = str(int(statistics[x][12]) + int(m[12]))    #update opponent_bpFaced
                            break
                        except:
                            break
                    y = y + 1
                x = x + 1
        if not m[2] in inserted:
            if m[2] == "" or m[3] == "" or m[13] == "" or m[14] == "" or m[15] == "" or m[16] == "" or m[17] == "" or m[18] == "" or m[19] == "" or m[20] == "" or m[21] == "" or m[11] == "" or m[12] == "":
                continue
            else:
                inserted.append(m[2])
                statistics.append([m[2], m[3], m[13], m[14], m[15], m[16], m[17], m[18], m[19], m[20], m[21], m[11], m[12], 1, 0, 0, 0])
    x = 0
    while x < len(statistics):
        y = 0
        while y < len(statistics[x]):
            try:
                if float(statistics[x][6]) > float(statistics[x][5]):
                    firstServeWon_p = 0
                else:
                    firstServeWon_p = str(float(statistics[x][6]) / float(statistics[x][5]))
                #if firstServeWon_p > 1:
                #    firstServeWon = 0
                if int(statistics[x][8]) > int(statistics[x][7]):
                    secondServeWon_p = 0
                else:
                    secondServeWon_p = str(int(statistics[x][8]) / int(statistics[x][7]))
                #if secondServeWon_p > 1:
                #    secondServeWon_p = 0
                if int(statistics[x][2]) > int(statistics[x][4]):
                    ace_p = 0
                else:
                    ace_p = str(int(statistics[x][2]) / int(statistics[x][4]))
                #if ace_p > 1:
                #    ace_p = 0
                if int(statistics[x][3]) > int(statistics[x][4]):
                    doubleFaults_p = 0
                else:
                    doubleFaults_p = str(int(statistics[x][3]) / int(statistics[x][4]))
                #if doubleFaults_p > 1:
                #    doubleFaults_p = 0
                if not int(statistics[x][10]) == 0:
                    if int(statistics[x][9]) > int(statistics[x][10]):
                        breakPointsSaved_p = 0
                    else:
                        breakPointsSaved_p = str(int(statistics[x][9]) / int(statistics[x][10]))
                #    if breakPointsSaved_p > 1:
                #        breakPointsSaved_p = 0
                else:
                    breakPointsSaved_p = 0
                if not int(statistics[x][12]) == 0:
                    if int(statistics[x][11]) > int(statistics[x][12]):
                        opponentBreakPoints_p = 0
                    else:
                        opponentBreakPoints_p = str( 1 - (int(statistics[x][11]) / int(statistics[x][12])))
                    #if opponentBreakPoints_p > 1:
                    #    opponentBreakPoints_p = 0
                else:
                    opponentBreakPoints_p = 0
            except:
                break
            writable.append([statistics[x][0], statistics[x][1], ace_p, doubleFaults_p, firstServeWon_p, secondServeWon_p, breakPointsSaved_p, opponentBreakPoints_p, statistics[x][13], statistics[x][14], statistics[x][15], statistics[x][16]])
            break
            y = y +1
        x = x + 1

    print(writable)
    for w in writable:
        writer.writerow([w[0], w[1], w[2], w[3], w[4], w[5], w[6], w[7], w[8], w[9], w[10], w[11]])

    players.clear()
    matches.clear()
    inserted.clear()
    statistics.clear()
    writable.clear()


#ATP 2000/2009
with open("../../data/tennis_atp/atp_rankings_00s.csv", "r", encoding="utf8") as ranking_file:
    first_line = next(ranking_file)
    first_line = first_line.split(",")

    for line in ranking_file:
        player = line.split(",")
        if int(player[1]) <= 20 and not player[2] in players:
            players.append(player[2])
            print(players)

    ranking_file.close()

for i in range(2000, 2009):
    with open("../../data/tennis_atp/atp_matches_" + str(i) + ".csv", "r", encoding="utf8") as matches_file:      # 0 = w_id, 1 = w_name, 2 = l_id, 3 = l_name, 4 = w_ace, 5 = w_df, 6 = w_svpt, 7 = w_1stin, 8 = w_1stwon
        first_line = next(matches_file)                                                     # 9 = w_2ndwon, 10 = w_svgms, 11 = w_bpsaved, 12 = w_bpfaced, 13 = l_ace, 14 = l_df, 15 = l_svpt
        first_line = first_line.split(",")                                                  # 16 = l_1stin, 17 = l_1stwon, 18 = l_2ndwon, 19 = l_svgms, 20 = l_bpsaved, 21 = l_bpfaced, 22 = surface
        for line in matches_file:
            match = line.split(",")
            matches.append([match[7], match[10], match[15], match[18], match[27], match[28], match[29], match[30], match[31], match[32], match[33], match[34],
                            match[35], match[36], match[37], match[38], match[39], match[40], match[41], match[42], match[43], match[44], match[2]])
            #print(matches)

        matches_file.close()

with open("../../data/preprocessed/pca/atp_players_statistics_2000.csv", "w", newline='', encoding="utf8") as output:    # 0 = id, 1 = name, 2 = surname, 3 = ace , 4 = df, 5 = 1stWon
    writer = csv.writer(output, delimiter=",")                                                                  # 6 = 2ndWon, 7 = svGames, 8 = bpSaved, 9 = matches
    writer_header = csv.DictWriter(output, fieldnames=["id", "name", "ace", "df", "1stWon", "2ndWon", "bpSaved", "bpLost", "matches", "hard", "clay", "grass"])
    writer_header.writeheader()

    inserted = list()

    # statistics: 0 = id, 1 = name, 2 = ace, 3 = df, 4 = svPoints, 5 = 1stin, 6 = 1stwon, 7 = 2ndIn, 8 = 2ndwon, 8 = svGms, 9 = bpSaved, 10 = bpFaced, 11 = opponent_bpSaved
    for m in matches:                                                              # 12 = opponent_bpFaced , 13 = matches, 14 = hard, 15 = clay, 16 = grass
        if m[0] in (y for x in statistics for y in x) and m[0] in players:
            x = 0
            while x < len(statistics):
                y = 0
                while y < len(statistics[x]):
                    if statistics[x][0] == m[0]:
                        statistics[x][13] += 1      #update matches played
                        try:
                            statistics[x][6] = str(float(statistics[x][6]) + float(m[8]))   #update 1stWon
                            statistics[x][5] = str(int(statistics[x][5]) + int(m[7]))   #update 1stIn
                            statistics[x][8] = str(int(statistics[x][8]) + int(m[9]))   #update 2ndWon
                            statistics[x][7] = str(int(statistics[x][7]) + (int(m[6]) - (int(m[7]) + int(m[5]))))   #2ndIn = svPoints - (1stIn + doubleFaults)
                            statistics[x][2] = str(int(statistics[x][2]) + int(m[4]))   #update ace
                            statistics[x][4] = str(int(statistics[x][4]) + int(m[6]))   #update servicePoints
                            statistics[x][3] = str(int(statistics[x][3]) + int(m[5]))   #update doubleFaults
                            statistics[x][9] = str(int(statistics[x][9]) + int(m[11]))  #update bpSaved
                            statistics[x][10] = str(int(statistics[x][10]) + int(m[12]))    #update bpFaced
                            statistics[x][11] = str(int(statistics[x][11]) + int(m[20]))    #update opponent_bpSaved
                            statistics[x][12] = str(int(statistics[x][12]) + int(m[21]))    #update opponent_bpFaced
                            if m[22] == "Hard":
                                statistics[x][14] = str(int(statistics[x][14]) + 1)    #update hard victories
                            elif m[22] == "Clay":
                                statistics[x][15] = str(int(statistics[x][15]) + 1)    #update clay victories
                            else:
                                statistics[x][16] = str(int(statistics[x][16]) + 1)    #update grass victories
                            print(statistics[x])
                            break
                        except:
                            break
                    y = y + 1
                x = x + 1
        if not m[0] in inserted:
            if m[0] == "" or m[1] == "" or m[4] == "" or m[5] == "" or m[6] == "" or m[7] == "" or m[8] == "" or m[9] == "" or m[10] == "" or m[11] == "" or m[12] == "" or m[20] == "" or m[21] == "":
                continue
            else:
                inserted.append(m[0])
                if m[22] == "Hard":
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 1, 0, 0])
                elif m[22] == "Clay":
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 0, 1, 0])
                else:
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 0, 0, 1])
        if m[2] in (y for x in statistics for y in x) and m[2] in players:
            x = 0
            while x < len(statistics):
                y = 0
                while y < len(statistics[x]):
                    if statistics[x][0] == m[2]:
                        statistics[x][13] += 1      #update matches played
                        try:
                            statistics[x][6] = str(float(statistics[x][6]) + float(m[17]))   #update 1stWon
                            statistics[x][5] = str(int(statistics[x][5]) + int(m[16]))   #update 1stIn
                            statistics[x][8] = str(int(statistics[x][8]) + int(m[18]))   #update 2ndWon
                            statistics[x][7] = str(int(statistics[x][7]) + (int(m[15]) - (int(m[16]) + int(m[14]))))   #2ndIn = svPoints - (1stIn + doubleFaults)
                            statistics[x][2] = str(int(statistics[x][2]) + int(m[13]))   #update ace
                            statistics[x][4] = str(int(statistics[x][4]) + int(m[15]))   #update servicePoints
                            statistics[x][3] = str(int(statistics[x][3]) + int(m[14]))   #update doubleFaults
                            statistics[x][9] = str(int(statistics[x][9]) + int(m[20]))  #update bpSaved
                            statistics[x][10] = str(int(statistics[x][10]) + int(m[21]))    #update bpFaced
                            statistics[x][11] = str(int(statistics[x][11]) + int(m[11]))    #update opponent_bpSaved
                            statistics[x][12] = str(int(statistics[x][12]) + int(m[12]))    #update opponent_bpFaced
                            break
                        except:
                            break
                    y = y + 1
                x = x + 1
        if not m[2] in inserted:
            if m[2] == "" or m[3] == "" or m[13] == "" or m[14] == "" or m[15] == "" or m[16] == "" or m[17] == "" or m[18] == "" or m[19] == "" or m[20] == "" or m[21] == "" or m[11] == "" or m[12] == "":
                continue
            else:
                inserted.append(m[2])
                statistics.append([m[2], m[3], m[13], m[14], m[15], m[16], m[17], m[18], m[19], m[20], m[21], m[11], m[12], 1, 0, 0, 0])
    x = 0
    while x < len(statistics):
        y = 0
        while y < len(statistics[x]):
            try:
                if float(statistics[x][6]) > float(statistics[x][5]):
                    firstServeWon_p = 0
                else:
                    firstServeWon_p = str(float(statistics[x][6]) / float(statistics[x][5]))
                #if firstServeWon_p > 1:
                #    firstServeWon = 0
                if int(statistics[x][8]) > int(statistics[x][7]):
                    secondServeWon_p = 0
                else:
                    secondServeWon_p = str(int(statistics[x][8]) / int(statistics[x][7]))
                #if secondServeWon_p > 1:
                #    secondServeWon_p = 0
                if int(statistics[x][2]) > int(statistics[x][4]):
                    ace_p = 0
                else:
                    ace_p = str(int(statistics[x][2]) / int(statistics[x][4]))
                #if ace_p > 1:
                #    ace_p = 0
                if int(statistics[x][3]) > int(statistics[x][4]):
                    doubleFaults_p = 0
                else:
                    doubleFaults_p = str(int(statistics[x][3]) / int(statistics[x][4]))
                #if doubleFaults_p > 1:
                #    doubleFaults_p = 0
                if not int(statistics[x][10]) == 0:
                    if int(statistics[x][9]) > int(statistics[x][10]):
                        breakPointsSaved_p = 0
                    else:
                        breakPointsSaved_p = str(int(statistics[x][9]) / int(statistics[x][10]))
                #    if breakPointsSaved_p > 1:
                #        breakPointsSaved_p = 0
                else:
                    breakPointsSaved_p = 0
                if not int(statistics[x][12]) == 0:
                    if int(statistics[x][11]) > int(statistics[x][12]):
                        opponentBreakPoints_p = 0
                    else:
                        opponentBreakPoints_p = str( 1 - (int(statistics[x][11]) / int(statistics[x][12])))
                    #if opponentBreakPoints_p > 1:
                    #    opponentBreakPoints_p = 0
                else:
                    opponentBreakPoints_p = 0
            except:
                break
            writable.append([statistics[x][0], statistics[x][1], ace_p, doubleFaults_p, firstServeWon_p, secondServeWon_p, breakPointsSaved_p, opponentBreakPoints_p, statistics[x][13], statistics[x][14], statistics[x][15], statistics[x][16]])
            break
            y = y +1
        x = x + 1

    print(writable)
    for w in writable:
        writer.writerow([w[0], w[1], w[2], w[3], w[4], w[5], w[6], w[7], w[8], w[9], w[10], w[11]])

    players.clear()
    matches.clear()
    inserted.clear()
    statistics.clear()
    writable.clear()


#ATP 1990/1999
with open("../../data/tennis_atp/atp_rankings_90s.csv", "r", encoding="utf8") as ranking_file:
    first_line = next(ranking_file)
    first_line = first_line.split(",")

    for line in ranking_file:
        player = line.split(",")
        if int(player[1]) <= 20 and not player[2] in players:
            players.append(player[2])
            print(players)

    ranking_file.close()

for i in range(1990, 1999):
    with open("../../data/tennis_atp/atp_matches_" + str(i) + ".csv", "r", encoding="utf8") as matches_file:      # 0 = w_id, 1 = w_name, 2 = l_id, 3 = l_name, 4 = w_ace, 5 = w_df, 6 = w_svpt, 7 = w_1stin, 8 = w_1stwon
        first_line = next(matches_file)                                                     # 9 = w_2ndwon, 10 = w_svgms, 11 = w_bpsaved, 12 = w_bpfaced, 13 = l_ace, 14 = l_df, 15 = l_svpt
        first_line = first_line.split(",")                                                  # 16 = l_1stin, 17 = l_1stwon, 18 = l_2ndwon, 19 = l_svgms, 20 = l_bpsaved, 21 = l_bpfaced, 22 = surface
        for line in matches_file:
            match = line.split(",")
            matches.append([match[7], match[10], match[15], match[18], match[27], match[28], match[29], match[30], match[31], match[32], match[33], match[34],
                            match[35], match[36], match[37], match[38], match[39], match[40], match[41], match[42], match[43], match[44], match[2]])
            #print(matches)

        matches_file.close()

with open("../../data/preprocessed/pca/atp_players_statistics_1990.csv", "w", newline='', encoding="utf8") as output:    # 0 = id, 1 = name, 2 = surname, 3 = ace , 4 = df, 5 = 1stWon
    writer = csv.writer(output, delimiter=",")                                                                  # 6 = 2ndWon, 7 = svGames, 8 = bpSaved, 9 = matches
    writer_header = csv.DictWriter(output, fieldnames=["id", "name", "ace", "df", "1stWon", "2ndWon", "bpSaved", "bpLost", "matches", "hard", "clay", "grass"])
    writer_header.writeheader()

    inserted = list()

    # statistics: 0 = id, 1 = name, 2 = ace, 3 = df, 4 = svPoints, 5 = 1stin, 6 = 1stwon, 7 = 2ndIn, 8 = 2ndwon, 8 = svGms, 9 = bpSaved, 10 = bpFaced, 11 = opponent_bpSaved
    for m in matches:                                                              # 12 = opponent_bpFaced , 13 = matches, 14 = hard, 15 = clay, 16 = grass
        if m[0] in (y for x in statistics for y in x) and m[0] in players:
            x = 0
            while x < len(statistics):
                y = 0
                while y < len(statistics[x]):
                    if statistics[x][0] == m[0]:
                        statistics[x][13] += 1      #update matches played
                        try:
                            statistics[x][6] = str(float(statistics[x][6]) + float(m[8]))   #update 1stWon
                            statistics[x][5] = str(int(statistics[x][5]) + int(m[7]))   #update 1stIn
                            statistics[x][8] = str(int(statistics[x][8]) + int(m[9]))   #update 2ndWon
                            statistics[x][7] = str(int(statistics[x][7]) + (int(m[6]) - (int(m[7]) + int(m[5]))))   #2ndIn = svPoints - (1stIn + doubleFaults)
                            statistics[x][2] = str(int(statistics[x][2]) + int(m[4]))   #update ace
                            statistics[x][4] = str(int(statistics[x][4]) + int(m[6]))   #update servicePoints
                            statistics[x][3] = str(int(statistics[x][3]) + int(m[5]))   #update doubleFaults
                            statistics[x][9] = str(int(statistics[x][9]) + int(m[11]))  #update bpSaved
                            statistics[x][10] = str(int(statistics[x][10]) + int(m[12]))    #update bpFaced
                            statistics[x][11] = str(int(statistics[x][11]) + int(m[20]))    #update opponent_bpSaved
                            statistics[x][12] = str(int(statistics[x][12]) + int(m[21]))    #update opponent_bpFaced
                            if m[22] == "Hard":
                                statistics[x][14] = str(int(statistics[x][14]) + 1)    #update hard victories
                            elif m[22] == "Clay":
                                statistics[x][15] = str(int(statistics[x][15]) + 1)    #update clay victories
                            else:
                                statistics[x][16] = str(int(statistics[x][16]) + 1)    #update grass victories
                            print(statistics[x])
                            break
                        except:
                            break
                    y = y + 1
                x = x + 1
        if not m[0] in inserted:
            if m[0] == "" or m[1] == "" or m[4] == "" or m[5] == "" or m[6] == "" or m[7] == "" or m[8] == "" or m[9] == "" or m[10] == "" or m[11] == "" or m[12] == "" or m[20] == "" or m[21] == "":
                continue
            else:
                inserted.append(m[0])
                if m[22] == "Hard":
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 1, 0, 0])
                elif m[22] == "Clay":
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 0, 1, 0])
                else:
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 0, 0, 1])
        if m[2] in (y for x in statistics for y in x) and m[2] in players:
            x = 0
            while x < len(statistics):
                y = 0
                while y < len(statistics[x]):
                    if statistics[x][0] == m[2]:
                        statistics[x][13] += 1      #update matches played
                        try:
                            statistics[x][6] = str(float(statistics[x][6]) + float(m[17]))   #update 1stWon
                            statistics[x][5] = str(int(statistics[x][5]) + int(m[16]))   #update 1stIn
                            statistics[x][8] = str(int(statistics[x][8]) + int(m[18]))   #update 2ndWon
                            statistics[x][7] = str(int(statistics[x][7]) + (int(m[15]) - (int(m[16]) + int(m[14]))))   #2ndIn = svPoints - (1stIn + doubleFaults)
                            statistics[x][2] = str(int(statistics[x][2]) + int(m[13]))   #update ace
                            statistics[x][4] = str(int(statistics[x][4]) + int(m[15]))   #update servicePoints
                            statistics[x][3] = str(int(statistics[x][3]) + int(m[14]))   #update doubleFaults
                            statistics[x][9] = str(int(statistics[x][9]) + int(m[20]))  #update bpSaved
                            statistics[x][10] = str(int(statistics[x][10]) + int(m[21]))    #update bpFaced
                            statistics[x][11] = str(int(statistics[x][11]) + int(m[11]))    #update opponent_bpSaved
                            statistics[x][12] = str(int(statistics[x][12]) + int(m[12]))    #update opponent_bpFaced
                            break
                        except:
                            break
                    y = y + 1
                x = x + 1
        if not m[2] in inserted:
            if m[2] == "" or m[3] == "" or m[13] == "" or m[14] == "" or m[15] == "" or m[16] == "" or m[17] == "" or m[18] == "" or m[19] == "" or m[20] == "" or m[21] == "" or m[11] == "" or m[12] == "":
                continue
            else:
                inserted.append(m[2])
                statistics.append([m[2], m[3], m[13], m[14], m[15], m[16], m[17], m[18], m[19], m[20], m[21], m[11], m[12], 1, 0, 0, 0])
    x = 0
    while x < len(statistics):
        y = 0
        while y < len(statistics[x]):
            try:
                if float(statistics[x][6]) > float(statistics[x][5]):
                    firstServeWon_p = 0
                else:
                    firstServeWon_p = str(float(statistics[x][6]) / float(statistics[x][5]))
                #if firstServeWon_p > 1:
                #    firstServeWon = 0
                if int(statistics[x][8]) > int(statistics[x][7]):
                    secondServeWon_p = 0
                else:
                    secondServeWon_p = str(int(statistics[x][8]) / int(statistics[x][7]))
                #if secondServeWon_p > 1:
                #    secondServeWon_p = 0
                if int(statistics[x][2]) > int(statistics[x][4]):
                    ace_p = 0
                else:
                    ace_p = str(int(statistics[x][2]) / int(statistics[x][4]))
                #if ace_p > 1:
                #    ace_p = 0
                if int(statistics[x][3]) > int(statistics[x][4]):
                    doubleFaults_p = 0
                else:
                    doubleFaults_p = str(int(statistics[x][3]) / int(statistics[x][4]))
                #if doubleFaults_p > 1:
                #    doubleFaults_p = 0
                if not int(statistics[x][10]) == 0:
                    if int(statistics[x][9]) > int(statistics[x][10]):
                        breakPointsSaved_p = 0
                    else:
                        breakPointsSaved_p = str(int(statistics[x][9]) / int(statistics[x][10]))
                #    if breakPointsSaved_p > 1:
                #        breakPointsSaved_p = 0
                else:
                    breakPointsSaved_p = 0
                if not int(statistics[x][12]) == 0:
                    if int(statistics[x][11]) > int(statistics[x][12]):
                        opponentBreakPoints_p = 0
                    else:
                        opponentBreakPoints_p = str( 1 - (int(statistics[x][11]) / int(statistics[x][12])))
                    #if opponentBreakPoints_p > 1:
                    #    opponentBreakPoints_p = 0
                else:
                    opponentBreakPoints_p = 0
            except:
                break
            writable.append([statistics[x][0], statistics[x][1], ace_p, doubleFaults_p, firstServeWon_p, secondServeWon_p, breakPointsSaved_p, opponentBreakPoints_p, statistics[x][13], statistics[x][14], statistics[x][15], statistics[x][16]])
            break
            y = y +1
        x = x + 1

    print(writable)
    for w in writable:
        writer.writerow([w[0], w[1], w[2], w[3], w[4], w[5], w[6], w[7], w[8], w[9], w[10], w[11]])

    players.clear()
    matches.clear()
    inserted.clear()
    statistics.clear()
    writable.clear()

#ATP 1980/1989
with open("../../data/tennis_atp/atp_rankings_80s.csv", "r", encoding="utf8") as ranking_file:
    first_line = next(ranking_file)
    first_line = first_line.split(",")

    for line in ranking_file:
        player = line.split(",")
        if int(player[1]) <= 20 and not player[2] in players:
            players.append(player[2])
            print(players)

    ranking_file.close()

for i in range(1980, 1989):
    with open("../../data/tennis_atp/atp_matches_" + str(i) + ".csv", "r", encoding="utf8") as matches_file:      # 0 = w_id, 1 = w_name, 2 = l_id, 3 = l_name, 4 = w_ace, 5 = w_df, 6 = w_svpt, 7 = w_1stin, 8 = w_1stwon
        first_line = next(matches_file)                                                     # 9 = w_2ndwon, 10 = w_svgms, 11 = w_bpsaved, 12 = w_bpfaced, 13 = l_ace, 14 = l_df, 15 = l_svpt
        first_line = first_line.split(",")                                                  # 16 = l_1stin, 17 = l_1stwon, 18 = l_2ndwon, 19 = l_svgms, 20 = l_bpsaved, 21 = l_bpfaced, 22 = surface
        for line in matches_file:
            match = line.split(",")
            matches.append([match[7], match[10], match[15], match[18], match[27], match[28], match[29], match[30], match[31], match[32], match[33], match[34],
                            match[35], match[36], match[37], match[38], match[39], match[40], match[41], match[42], match[43], match[44], match[2]])
            #print(matches)

        matches_file.close()

with open("../../data/preprocessed/pca/atp_players_statistics_1980.csv", "w", newline='', encoding="utf8") as output:    # 0 = id, 1 = name, 2 = surname, 3 = ace , 4 = df, 5 = 1stWon
    writer = csv.writer(output, delimiter=",")                                                                  # 6 = 2ndWon, 7 = svGames, 8 = bpSaved, 9 = matches
    writer_header = csv.DictWriter(output, fieldnames=["id", "name", "ace", "df", "1stWon", "2ndWon", "bpSaved", "bpLost", "matches", "hard", "clay", "grass"])
    writer_header.writeheader()

    inserted = list()

    # statistics: 0 = id, 1 = name, 2 = ace, 3 = df, 4 = svPoints, 5 = 1stin, 6 = 1stwon, 7 = 2ndIn, 8 = 2ndwon, 8 = svGms, 9 = bpSaved, 10 = bpFaced, 11 = opponent_bpSaved
    for m in matches:                                                              # 12 = opponent_bpFaced , 13 = matches, 14 = hard, 15 = clay, 16 = grass
        if m[0] in (y for x in statistics for y in x) and m[0] in players:
            x = 0
            while x < len(statistics):
                y = 0
                while y < len(statistics[x]):
                    if statistics[x][0] == m[0]:
                        statistics[x][13] += 1      #update matches played
                        try:
                            statistics[x][6] = str(float(statistics[x][6]) + float(m[8]))   #update 1stWon
                            statistics[x][5] = str(int(statistics[x][5]) + int(m[7]))   #update 1stIn
                            statistics[x][8] = str(int(statistics[x][8]) + int(m[9]))   #update 2ndWon
                            statistics[x][7] = str(int(statistics[x][7]) + (int(m[6]) - (int(m[7]) + int(m[5]))))   #2ndIn = svPoints - (1stIn + doubleFaults)
                            statistics[x][2] = str(int(statistics[x][2]) + int(m[4]))   #update ace
                            statistics[x][4] = str(int(statistics[x][4]) + int(m[6]))   #update servicePoints
                            statistics[x][3] = str(int(statistics[x][3]) + int(m[5]))   #update doubleFaults
                            statistics[x][9] = str(int(statistics[x][9]) + int(m[11]))  #update bpSaved
                            statistics[x][10] = str(int(statistics[x][10]) + int(m[12]))    #update bpFaced
                            statistics[x][11] = str(int(statistics[x][11]) + int(m[20]))    #update opponent_bpSaved
                            statistics[x][12] = str(int(statistics[x][12]) + int(m[21]))    #update opponent_bpFaced
                            if m[22] == "Hard":
                                statistics[x][14] = str(int(statistics[x][14]) + 1)    #update hard victories
                            elif m[22] == "Clay":
                                statistics[x][15] = str(int(statistics[x][15]) + 1)    #update clay victories
                            else:
                                statistics[x][16] = str(int(statistics[x][16]) + 1)    #update grass victories
                            print(statistics[x])
                            break
                        except:
                            break
                    y = y + 1
                x = x + 1
        if not m[0] in inserted:
            if m[0] == "" or m[1] == "" or m[4] == "" or m[5] == "" or m[6] == "" or m[7] == "" or m[8] == "" or m[9] == "" or m[10] == "" or m[11] == "" or m[12] == "" or m[20] == "" or m[21] == "":
                continue
            else:
                inserted.append(m[0])
                if m[22] == "Hard":
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 1, 0, 0])
                elif m[22] == "Clay":
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 0, 1, 0])
                else:
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 0, 0, 1])
        if m[2] in (y for x in statistics for y in x) and m[2] in players:
            x = 0
            while x < len(statistics):
                y = 0
                while y < len(statistics[x]):
                    if statistics[x][0] == m[2]:
                        statistics[x][13] += 1      #update matches played
                        try:
                            statistics[x][6] = str(float(statistics[x][6]) + float(m[17]))   #update 1stWon
                            statistics[x][5] = str(int(statistics[x][5]) + int(m[16]))   #update 1stIn
                            statistics[x][8] = str(int(statistics[x][8]) + int(m[18]))   #update 2ndWon
                            statistics[x][7] = str(int(statistics[x][7]) + (int(m[15]) - (int(m[16]) + int(m[14]))))   #2ndIn = svPoints - (1stIn + doubleFaults)
                            statistics[x][2] = str(int(statistics[x][2]) + int(m[13]))   #update ace
                            statistics[x][4] = str(int(statistics[x][4]) + int(m[15]))   #update servicePoints
                            statistics[x][3] = str(int(statistics[x][3]) + int(m[14]))   #update doubleFaults
                            statistics[x][9] = str(int(statistics[x][9]) + int(m[20]))  #update bpSaved
                            statistics[x][10] = str(int(statistics[x][10]) + int(m[21]))    #update bpFaced
                            statistics[x][11] = str(int(statistics[x][11]) + int(m[11]))    #update opponent_bpSaved
                            statistics[x][12] = str(int(statistics[x][12]) + int(m[12]))    #update opponent_bpFaced
                            break
                        except:
                            break
                    y = y + 1
                x = x + 1
        if not m[2] in inserted:
            if m[2] == "" or m[3] == "" or m[13] == "" or m[14] == "" or m[15] == "" or m[16] == "" or m[17] == "" or m[18] == "" or m[19] == "" or m[20] == "" or m[21] == "" or m[11] == "" or m[12] == "":
                continue
            else:
                inserted.append(m[2])
                statistics.append([m[2], m[3], m[13], m[14], m[15], m[16], m[17], m[18], m[19], m[20], m[21], m[11], m[12], 1, 0, 0, 0])
    x = 0
    while x < len(statistics):
        y = 0
        while y < len(statistics[x]):
            try:
                if float(statistics[x][6]) > float(statistics[x][5]):
                    firstServeWon_p = 0
                else:
                    firstServeWon_p = str(float(statistics[x][6]) / float(statistics[x][5]))
                #if firstServeWon_p > 1:
                #    firstServeWon = 0
                if int(statistics[x][8]) > int(statistics[x][7]):
                    secondServeWon_p = 0
                else:
                    secondServeWon_p = str(int(statistics[x][8]) / int(statistics[x][7]))
                #if secondServeWon_p > 1:
                #    secondServeWon_p = 0
                if int(statistics[x][2]) > int(statistics[x][4]):
                    ace_p = 0
                else:
                    ace_p = str(int(statistics[x][2]) / int(statistics[x][4]))
                #if ace_p > 1:
                #    ace_p = 0
                if int(statistics[x][3]) > int(statistics[x][4]):
                    doubleFaults_p = 0
                else:
                    doubleFaults_p = str(int(statistics[x][3]) / int(statistics[x][4]))
                #if doubleFaults_p > 1:
                #    doubleFaults_p = 0
                if not int(statistics[x][10]) == 0:
                    if int(statistics[x][9]) > int(statistics[x][10]):
                        breakPointsSaved_p = 0
                    else:
                        breakPointsSaved_p = str(int(statistics[x][9]) / int(statistics[x][10]))
                #    if breakPointsSaved_p > 1:
                #        breakPointsSaved_p = 0
                else:
                    breakPointsSaved_p = 0
                if not int(statistics[x][12]) == 0:
                    if int(statistics[x][11]) > int(statistics[x][12]):
                        opponentBreakPoints_p = 0
                    else:
                        opponentBreakPoints_p = str( 1 - (int(statistics[x][11]) / int(statistics[x][12])))
                    #if opponentBreakPoints_p > 1:
                    #    opponentBreakPoints_p = 0
                else:
                    opponentBreakPoints_p = 0
            except:
                break
            writable.append([statistics[x][0], statistics[x][1], ace_p, doubleFaults_p, firstServeWon_p, secondServeWon_p, breakPointsSaved_p, opponentBreakPoints_p, statistics[x][13], statistics[x][14], statistics[x][15], statistics[x][16]])
            break
            y = y +1
        x = x + 1

    print(writable)
    for w in writable:
        writer.writerow([w[0], w[1], w[2], w[3], w[4], w[5], w[6], w[7], w[8], w[9], w[10], w[11]])

    players.clear()
    matches.clear()
    inserted.clear()
    statistics.clear()
    writable.clear()


#ATP All-time
years = ["80", "90", "00", "10"]
for i in years:
    with open("../../data/tennis_atp/atp_rankings_" + i + "s.csv", "r", encoding="utf8") as ranking_file:
        first_line = next(ranking_file)
        first_line = first_line.split(",")

        for line in ranking_file:
            player = line.split(",")
            if int(player[1]) <= 20 and not player[2] in players:
                players.append(player[2])
                print(players)

        ranking_file.close()

for i in range(1980, 2021):
    with open("../../data/tennis_atp/atp_matches_" + str(i) + ".csv", "r", encoding="utf8") as matches_file:      # 0 = w_id, 1 = w_name, 2 = l_id, 3 = l_name, 4 = w_ace, 5 = w_df, 6 = w_svpt, 7 = w_1stin, 8 = w_1stwon
        first_line = next(matches_file)                                                     # 9 = w_2ndwon, 10 = w_svgms, 11 = w_bpsaved, 12 = w_bpfaced, 13 = l_ace, 14 = l_df, 15 = l_svpt
        first_line = first_line.split(",")                                                  # 16 = l_1stin, 17 = l_1stwon, 18 = l_2ndwon, 19 = l_svgms, 20 = l_bpsaved, 21 = l_bpfaced, 22 = surface
        for line in matches_file:
            match = line.split(",")
            matches.append([match[7], match[10], match[15], match[18], match[27], match[28], match[29], match[30], match[31], match[32], match[33], match[34],
                            match[35], match[36], match[37], match[38], match[39], match[40], match[41], match[42], match[43], match[44], match[2]])
            #print(matches)

        matches_file.close()

with open("../../data/preprocessed/pca/atp_players_statistics_all.csv", "w", newline='', encoding="utf8") as output:    # 0 = id, 1 = name, 2 = surname, 3 = ace , 4 = df, 5 = 1stWon
    writer = csv.writer(output, delimiter=",")                                                                  # 6 = 2ndWon, 7 = svGames, 8 = bpSaved, 9 = matches
    writer_header = csv.DictWriter(output, fieldnames=["id", "name", "ace", "df", "1stWon", "2ndWon", "bpSaved", "bpLost", "matches", "hard", "clay", "grass"])
    writer_header.writeheader()

    inserted = list()

    # statistics: 0 = id, 1 = name, 2 = ace, 3 = df, 4 = svPoints, 5 = 1stin, 6 = 1stwon, 7 = 2ndIn, 8 = 2ndwon, 8 = svGms, 9 = bpSaved, 10 = bpFaced, 11 = opponent_bpSaved
    for m in matches:                                                              # 12 = opponent_bpFaced , 13 = matches, 14 = hard, 15 = clay, 16 = grass
        if m[0] in (y for x in statistics for y in x) and m[0] in players:
            x = 0
            while x < len(statistics):
                y = 0
                while y < len(statistics[x]):
                    if statistics[x][0] == m[0]:
                        statistics[x][13] += 1      #update matches played
                        try:
                            statistics[x][6] = str(float(statistics[x][6]) + float(m[8]))   #update 1stWon
                            statistics[x][5] = str(int(statistics[x][5]) + int(m[7]))   #update 1stIn
                            statistics[x][8] = str(int(statistics[x][8]) + int(m[9]))   #update 2ndWon
                            statistics[x][7] = str(int(statistics[x][7]) + (int(m[6]) - (int(m[7]) + int(m[5]))))   #2ndIn = svPoints - (1stIn + doubleFaults)
                            statistics[x][2] = str(int(statistics[x][2]) + int(m[4]))   #update ace
                            statistics[x][4] = str(int(statistics[x][4]) + int(m[6]))   #update servicePoints
                            statistics[x][3] = str(int(statistics[x][3]) + int(m[5]))   #update doubleFaults
                            statistics[x][9] = str(int(statistics[x][9]) + int(m[11]))  #update bpSaved
                            statistics[x][10] = str(int(statistics[x][10]) + int(m[12]))    #update bpFaced
                            statistics[x][11] = str(int(statistics[x][11]) + int(m[20]))    #update opponent_bpSaved
                            statistics[x][12] = str(int(statistics[x][12]) + int(m[21]))    #update opponent_bpFaced
                            if m[22] == "Hard":
                                statistics[x][14] = str(int(statistics[x][14]) + 1)    #update hard victories
                            elif m[22] == "Clay":
                                statistics[x][15] = str(int(statistics[x][15]) + 1)    #update clay victories
                            else:
                                statistics[x][16] = str(int(statistics[x][16]) + 1)    #update grass victories
                            print(statistics[x])
                            break
                        except:
                            break
                    y = y + 1
                x = x + 1
        if not m[0] in inserted:
            if m[0] == "" or m[1] == "" or m[4] == "" or m[5] == "" or m[6] == "" or m[7] == "" or m[8] == "" or m[9] == "" or m[10] == "" or m[11] == "" or m[12] == "" or m[20] == "" or m[21] == "":
                continue
            else:
                inserted.append(m[0])
                if m[22] == "Hard":
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 1, 0, 0])
                elif m[22] == "Clay":
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 0, 1, 0])
                else:
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 0, 0, 1])
        if m[2] in (y for x in statistics for y in x) and m[2] in players:
            x = 0
            while x < len(statistics):
                y = 0
                while y < len(statistics[x]):
                    if statistics[x][0] == m[2]:
                        statistics[x][13] += 1      #update matches played
                        try:
                            statistics[x][6] = str(float(statistics[x][6]) + float(m[17]))   #update 1stWon
                            statistics[x][5] = str(int(statistics[x][5]) + int(m[16]))   #update 1stIn
                            statistics[x][8] = str(int(statistics[x][8]) + int(m[18]))   #update 2ndWon
                            statistics[x][7] = str(int(statistics[x][7]) + (int(m[15]) - (int(m[16]) + int(m[14]))))   #2ndIn = svPoints - (1stIn + doubleFaults)
                            statistics[x][2] = str(int(statistics[x][2]) + int(m[13]))   #update ace
                            statistics[x][4] = str(int(statistics[x][4]) + int(m[15]))   #update servicePoints
                            statistics[x][3] = str(int(statistics[x][3]) + int(m[14]))   #update doubleFaults
                            statistics[x][9] = str(int(statistics[x][9]) + int(m[20]))  #update bpSaved
                            statistics[x][10] = str(int(statistics[x][10]) + int(m[21]))    #update bpFaced
                            statistics[x][11] = str(int(statistics[x][11]) + int(m[11]))    #update opponent_bpSaved
                            statistics[x][12] = str(int(statistics[x][12]) + int(m[12]))    #update opponent_bpFaced
                            break
                        except:
                            break
                    y = y + 1
                x = x + 1
        if not m[2] in inserted:
            if m[2] == "" or m[3] == "" or m[13] == "" or m[14] == "" or m[15] == "" or m[16] == "" or m[17] == "" or m[18] == "" or m[19] == "" or m[20] == "" or m[21] == "" or m[11] == "" or m[12] == "":
                continue
            else:
                inserted.append(m[2])
                statistics.append([m[2], m[3], m[13], m[14], m[15], m[16], m[17], m[18], m[19], m[20], m[21], m[11], m[12], 1, 0, 0, 0])
    x = 0
    while x < len(statistics):
        y = 0
        while y < len(statistics[x]):
            try:
                if float(statistics[x][6]) > float(statistics[x][5]):
                    firstServeWon_p = 0
                else:
                    firstServeWon_p = str(float(statistics[x][6]) / float(statistics[x][5]))
                #if firstServeWon_p > 1:
                #    firstServeWon = 0
                if int(statistics[x][8]) > int(statistics[x][7]):
                    secondServeWon_p = 0
                else:
                    secondServeWon_p = str(int(statistics[x][8]) / int(statistics[x][7]))
                #if secondServeWon_p > 1:
                #    secondServeWon_p = 0
                if int(statistics[x][2]) > int(statistics[x][4]):
                    ace_p = 0
                else:
                    ace_p = str(int(statistics[x][2]) / int(statistics[x][4]))
                #if ace_p > 1:
                #    ace_p = 0
                if int(statistics[x][3]) > int(statistics[x][4]):
                    doubleFaults_p = 0
                else:
                    doubleFaults_p = str(int(statistics[x][3]) / int(statistics[x][4]))
                #if doubleFaults_p > 1:
                #    doubleFaults_p = 0
                if not int(statistics[x][10]) == 0:
                    if int(statistics[x][9]) > int(statistics[x][10]):
                        breakPointsSaved_p = 0
                    else:
                        breakPointsSaved_p = str(int(statistics[x][9]) / int(statistics[x][10]))
                #    if breakPointsSaved_p > 1:
                #        breakPointsSaved_p = 0
                else:
                    breakPointsSaved_p = 0
                if not int(statistics[x][12]) == 0:
                    if int(statistics[x][11]) > int(statistics[x][12]):
                        opponentBreakPoints_p = 0
                    else:
                        opponentBreakPoints_p = str( 1 - (int(statistics[x][11]) / int(statistics[x][12])))
                    #if opponentBreakPoints_p > 1:
                    #    opponentBreakPoints_p = 0
                else:
                    opponentBreakPoints_p = 0
            except:
                break
            writable.append([statistics[x][0], statistics[x][1], ace_p, doubleFaults_p, firstServeWon_p, secondServeWon_p, breakPointsSaved_p, opponentBreakPoints_p, statistics[x][13], statistics[x][14], statistics[x][15], statistics[x][16]])
            break
            y = y +1
        x = x + 1

    print(writable)
    for w in writable:
        writer.writerow([w[0], w[1], w[2], w[3], w[4], w[5], w[6], w[7], w[8], w[9], w[10], w[11]])

    players.clear()
    matches.clear()
    inserted.clear()
    statistics.clear()
    writable.clear()



#WTA 2021
with open("../../data/tennis_wta/wta_rankings_current.csv", "r", encoding="utf8") as ranking_file:
    first_line = next(ranking_file)
    first_line = first_line.split(",")

    for line in ranking_file:
        player = line.split(",")
        if int(player[1]) <= 20 and not player[2] in players:
            players.append(player[2])
            print(players)

    ranking_file.close()

with open("../../data/tennis_wta/wta_matches_2021.csv", "r", encoding="utf8") as matches_file:      # 0 = w_id, 1 = w_name, 2 = l_id, 3 = l_name, 4 = w_ace, 5 = w_df, 6 = w_svpt, 7 = w_1stin, 8 = w_1stwon
    first_line = next(matches_file)                                                     # 9 = w_2ndwon, 10 = w_svgms, 11 = w_bpsaved, 12 = w_bpfaced, 13 = l_ace, 14 = l_df, 15 = l_svpt
    first_line = first_line.split(",")                                                  # 16 = l_1stin, 17 = l_1stwon, 18 = l_2ndwon, 19 = l_svgms, 20 = l_bpsaved, 21 = l_bpfaced, 22 = surface
    for line in matches_file:
        match = line.split(",")
        matches.append([match[7], match[10], match[15], match[18], match[27], match[28], match[29], match[30], match[31], match[32], match[33], match[34],
                        match[35], match[36], match[37], match[38], match[39], match[40], match[41], match[42], match[43], match[44], match[2]])
        #print(matches)

    matches_file.close()

with open("../../data/preprocessed/pca/wta_players_statistics_2021.csv", "w", newline='', encoding="utf8") as output:    # 0 = id, 1 = name, 2 = surname, 3 = ace , 4 = df, 5 = 1stWon
    writer = csv.writer(output, delimiter=",")                                                                  # 6 = 2ndWon, 7 = svGames, 8 = bpSaved, 9 = matches
    writer_header = csv.DictWriter(output, fieldnames=["id", "name", "ace", "df", "1stWon", "2ndWon", "bpSaved", "bpLost", "matches", "hard", "clay", "grass"])
    writer_header.writeheader()

    inserted = list()

    # statistics: 0 = id, 1 = name, 2 = ace, 3 = df, 4 = svPoints, 5 = 1stin, 6 = 1stwon, 7 = 2ndIn, 8 = 2ndwon, 8 = svGms, 9 = bpSaved, 10 = bpFaced, 11 = opponent_bpSaved
    for m in matches:                                                              # 12 = opponent_bpFaced , 13 = matches, 14 = hard, 15 = clay, 16 = grass
        if m[0] in (y for x in statistics for y in x) and m[0] in players:
            x = 0
            while x < len(statistics):
                y = 0
                while y < len(statistics[x]):
                    if statistics[x][0] == m[0]:
                        statistics[x][13] += 1      #update matches played
                        try:
                            statistics[x][6] = str(float(statistics[x][6]) + float(m[8]))   #update 1stWon
                            statistics[x][5] = str(int(statistics[x][5]) + int(m[7]))   #update 1stIn
                            statistics[x][8] = str(int(statistics[x][8]) + int(m[9]))   #update 2ndWon
                            statistics[x][7] = str(int(statistics[x][7]) + (int(m[6]) - (int(m[7]) + int(m[5]))))   #2ndIn = svPoints - (1stIn + doubleFaults)
                            statistics[x][2] = str(int(statistics[x][2]) + int(m[4]))   #update ace
                            statistics[x][4] = str(int(statistics[x][4]) + int(m[6]))   #update servicePoints
                            statistics[x][3] = str(int(statistics[x][3]) + int(m[5]))   #update doubleFaults
                            statistics[x][9] = str(int(statistics[x][9]) + int(m[11]))  #update bpSaved
                            statistics[x][10] = str(int(statistics[x][10]) + int(m[12]))    #update bpFaced
                            statistics[x][11] = str(int(statistics[x][11]) + int(m[20]))    #update opponent_bpSaved
                            statistics[x][12] = str(int(statistics[x][12]) + int(m[21]))    #update opponent_bpFaced
                            if m[22] == "Hard":
                                statistics[x][14] = str(int(statistics[x][14]) + 1)    #update hard victories
                            elif m[22] == "Clay":
                                statistics[x][15] = str(int(statistics[x][15]) + 1)    #update clay victories
                            else:
                                statistics[x][16] = str(int(statistics[x][16]) + 1)    #update grass victories
                            print(statistics[x])
                            break
                        except:
                            break
                    y = y + 1
                x = x + 1
        if not m[0] in inserted:
            if m[0] == "" or m[1] == "" or m[4] == "" or m[5] == "" or m[6] == "" or m[7] == "" or m[8] == "" or m[9] == "" or m[10] == "" or m[11] == "" or m[12] == "" or m[20] == "" or m[21] == "":
                continue
            else:
                inserted.append(m[0])
                if m[22] == "Hard":
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 1, 0, 0])
                elif m[22] == "Clay":
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 0, 1, 0])
                else:
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 0, 0, 1])
        if m[2] in (y for x in statistics for y in x) and m[2] in players:
            x = 0
            while x < len(statistics):
                y = 0
                while y < len(statistics[x]):
                    if statistics[x][0] == m[2]:
                        statistics[x][13] += 1      #update matches played
                        try:
                            statistics[x][6] = str(float(statistics[x][6]) + float(m[17]))   #update 1stWon
                            statistics[x][5] = str(int(statistics[x][5]) + int(m[16]))   #update 1stIn
                            statistics[x][8] = str(int(statistics[x][8]) + int(m[18]))   #update 2ndWon
                            statistics[x][7] = str(int(statistics[x][7]) + (int(m[15]) - (int(m[16]) + int(m[14]))))   #2ndIn = svPoints - (1stIn + doubleFaults)
                            statistics[x][2] = str(int(statistics[x][2]) + int(m[13]))   #update ace
                            statistics[x][4] = str(int(statistics[x][4]) + int(m[15]))   #update servicePoints
                            statistics[x][3] = str(int(statistics[x][3]) + int(m[14]))   #update doubleFaults
                            statistics[x][9] = str(int(statistics[x][9]) + int(m[20]))  #update bpSaved
                            statistics[x][10] = str(int(statistics[x][10]) + int(m[21]))    #update bpFaced
                            statistics[x][11] = str(int(statistics[x][11]) + int(m[11]))    #update opponent_bpSaved
                            statistics[x][12] = str(int(statistics[x][12]) + int(m[12]))    #update opponent_bpFaced
                            break
                        except:
                            break
                    y = y + 1
                x = x + 1
        if not m[2] in inserted:
            if m[2] == "" or m[3] == "" or m[13] == "" or m[14] == "" or m[15] == "" or m[16] == "" or m[17] == "" or m[18] == "" or m[19] == "" or m[20] == "" or m[21] == "" or m[11] == "" or m[12] == "":
                continue
            else:
                inserted.append(m[2])
                statistics.append([m[2], m[3], m[13], m[14], m[15], m[16], m[17], m[18], m[19], m[20], m[21], m[11], m[12], 1, 0, 0, 0])
    x = 0
    while x < len(statistics):
        y = 0
        while y < len(statistics[x]):
            try:
                if float(statistics[x][6]) > float(statistics[x][5]):
                    firstServeWon_p = 0
                else:
                    firstServeWon_p = str(float(statistics[x][6]) / float(statistics[x][5]))
                #if firstServeWon_p > 1:
                #    firstServeWon = 0
                if int(statistics[x][8]) > int(statistics[x][7]):
                    secondServeWon_p = 0
                else:
                    secondServeWon_p = str(int(statistics[x][8]) / int(statistics[x][7]))
                #if secondServeWon_p > 1:
                #    secondServeWon_p = 0
                if int(statistics[x][2]) > int(statistics[x][4]):
                    ace_p = 0
                else:
                    ace_p = str(int(statistics[x][2]) / int(statistics[x][4]))
                #if ace_p > 1:
                #    ace_p = 0
                if int(statistics[x][3]) > int(statistics[x][4]):
                    doubleFaults_p = 0
                else:
                    doubleFaults_p = str(int(statistics[x][3]) / int(statistics[x][4]))
                #if doubleFaults_p > 1:
                #    doubleFaults_p = 0
                if not int(statistics[x][10]) == 0:
                    if int(statistics[x][9]) > int(statistics[x][10]):
                        breakPointsSaved_p = 0
                    else:
                        breakPointsSaved_p = str(int(statistics[x][9]) / int(statistics[x][10]))
                #    if breakPointsSaved_p > 1:
                #        breakPointsSaved_p = 0
                else:
                    breakPointsSaved_p = 0
                if not int(statistics[x][12]) == 0:
                    if int(statistics[x][11]) > int(statistics[x][12]):
                        opponentBreakPoints_p = 0
                    else:
                        opponentBreakPoints_p = str( 1 - (int(statistics[x][11]) / int(statistics[x][12])))
                    #if opponentBreakPoints_p > 1:
                    #    opponentBreakPoints_p = 0
                else:
                    opponentBreakPoints_p = 0
            except:
                break
            writable.append([statistics[x][0], statistics[x][1], ace_p, doubleFaults_p, firstServeWon_p, secondServeWon_p, breakPointsSaved_p, opponentBreakPoints_p, statistics[x][13], statistics[x][14], statistics[x][15], statistics[x][16]])
            break
            y = y +1
        x = x + 1

    print(writable)
    for w in writable:
        writer.writerow([w[0], w[1], w[2], w[3], w[4], w[5], w[6], w[7], w[8], w[9], w[10], w[11]])

    players.clear()
    matches.clear()
    inserted.clear()
    statistics.clear()
    writable.clear()


#WTA 2020/21
with open("../../data/tennis_wta/wta_rankings_20s.csv", "r", encoding="utf8") as ranking_file:
    first_line = next(ranking_file)
    first_line = first_line.split(",")

    for line in ranking_file:
        player = line.split(",")
        if int(player[1]) <= 20 and not player[2] in players:
            players.append(player[2])
            print(players)

    ranking_file.close()

for i in range(2020, 2021):
    with open("../../data/tennis_wta/wta_matches_" + str(i) + ".csv", "r", encoding="utf8") as matches_file:      # 0 = w_id, 1 = w_name, 2 = l_id, 3 = l_name, 4 = w_ace, 5 = w_df, 6 = w_svpt, 7 = w_1stin, 8 = w_1stwon
        first_line = next(matches_file)                                                     # 9 = w_2ndwon, 10 = w_svgms, 11 = w_bpsaved, 12 = w_bpfaced, 13 = l_ace, 14 = l_df, 15 = l_svpt
        first_line = first_line.split(",")                                                  # 16 = l_1stin, 17 = l_1stwon, 18 = l_2ndwon, 19 = l_svgms, 20 = l_bpsaved, 21 = l_bpfaced, 22 = surface
        for line in matches_file:
            match = line.split(",")
            matches.append([match[7], match[10], match[15], match[18], match[27], match[28], match[29], match[30], match[31], match[32], match[33], match[34],
                            match[35], match[36], match[37], match[38], match[39], match[40], match[41], match[42], match[43], match[44], match[2]])
            #print(matches)

        matches_file.close()

with open("../../data/preprocessed/pca/wta_players_statistics_2020.csv", "w", newline='', encoding="utf8") as output:    # 0 = id, 1 = name, 2 = surname, 3 = ace , 4 = df, 5 = 1stWon
    writer = csv.writer(output, delimiter=",")                                                                  # 6 = 2ndWon, 7 = svGames, 8 = bpSaved, 9 = matches
    writer_header = csv.DictWriter(output, fieldnames=["id", "name", "ace", "df", "1stWon", "2ndWon", "bpSaved", "bpLost", "matches", "hard", "clay", "grass"])
    writer_header.writeheader()

    inserted = list()

    # statistics: 0 = id, 1 = name, 2 = ace, 3 = df, 4 = svPoints, 5 = 1stin, 6 = 1stwon, 7 = 2ndIn, 8 = 2ndwon, 8 = svGms, 9 = bpSaved, 10 = bpFaced, 11 = opponent_bpSaved
    for m in matches:                                                              # 12 = opponent_bpFaced , 13 = matches, 14 = hard, 15 = clay, 16 = grass
        if m[0] in (y for x in statistics for y in x) and m[0] in players:
            x = 0
            while x < len(statistics):
                y = 0
                while y < len(statistics[x]):
                    if statistics[x][0] == m[0]:
                        statistics[x][13] += 1      #update matches played
                        try:
                            statistics[x][6] = str(float(statistics[x][6]) + float(m[8]))   #update 1stWon
                            statistics[x][5] = str(int(statistics[x][5]) + int(m[7]))   #update 1stIn
                            statistics[x][8] = str(int(statistics[x][8]) + int(m[9]))   #update 2ndWon
                            statistics[x][7] = str(int(statistics[x][7]) + (int(m[6]) - (int(m[7]) + int(m[5]))))   #2ndIn = svPoints - (1stIn + doubleFaults)
                            statistics[x][2] = str(int(statistics[x][2]) + int(m[4]))   #update ace
                            statistics[x][4] = str(int(statistics[x][4]) + int(m[6]))   #update servicePoints
                            statistics[x][3] = str(int(statistics[x][3]) + int(m[5]))   #update doubleFaults
                            statistics[x][9] = str(int(statistics[x][9]) + int(m[11]))  #update bpSaved
                            statistics[x][10] = str(int(statistics[x][10]) + int(m[12]))    #update bpFaced
                            statistics[x][11] = str(int(statistics[x][11]) + int(m[20]))    #update opponent_bpSaved
                            statistics[x][12] = str(int(statistics[x][12]) + int(m[21]))    #update opponent_bpFaced
                            if m[22] == "Hard":
                                statistics[x][14] = str(int(statistics[x][14]) + 1)    #update hard victories
                            elif m[22] == "Clay":
                                statistics[x][15] = str(int(statistics[x][15]) + 1)    #update clay victories
                            else:
                                statistics[x][16] = str(int(statistics[x][16]) + 1)    #update grass victories
                            print(statistics[x])
                            break
                        except:
                            break
                    y = y + 1
                x = x + 1
        if not m[0] in inserted:
            if m[0] == "" or m[1] == "" or m[4] == "" or m[5] == "" or m[6] == "" or m[7] == "" or m[8] == "" or m[9] == "" or m[10] == "" or m[11] == "" or m[12] == "" or m[20] == "" or m[21] == "":
                continue
            else:
                inserted.append(m[0])
                if m[22] == "Hard":
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 1, 0, 0])
                elif m[22] == "Clay":
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 0, 1, 0])
                else:
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 0, 0, 1])
        if m[2] in (y for x in statistics for y in x) and m[2] in players:
            x = 0
            while x < len(statistics):
                y = 0
                while y < len(statistics[x]):
                    if statistics[x][0] == m[2]:
                        statistics[x][13] += 1      #update matches played
                        try:
                            statistics[x][6] = str(float(statistics[x][6]) + float(m[17]))   #update 1stWon
                            statistics[x][5] = str(int(statistics[x][5]) + int(m[16]))   #update 1stIn
                            statistics[x][8] = str(int(statistics[x][8]) + int(m[18]))   #update 2ndWon
                            statistics[x][7] = str(int(statistics[x][7]) + (int(m[15]) - (int(m[16]) + int(m[14]))))   #2ndIn = svPoints - (1stIn + doubleFaults)
                            statistics[x][2] = str(int(statistics[x][2]) + int(m[13]))   #update ace
                            statistics[x][4] = str(int(statistics[x][4]) + int(m[15]))   #update servicePoints
                            statistics[x][3] = str(int(statistics[x][3]) + int(m[14]))   #update doubleFaults
                            statistics[x][9] = str(int(statistics[x][9]) + int(m[20]))  #update bpSaved
                            statistics[x][10] = str(int(statistics[x][10]) + int(m[21]))    #update bpFaced
                            statistics[x][11] = str(int(statistics[x][11]) + int(m[11]))    #update opponent_bpSaved
                            statistics[x][12] = str(int(statistics[x][12]) + int(m[12]))    #update opponent_bpFaced
                            break
                        except:
                            break
                    y = y + 1
                x = x + 1
        if not m[2] in inserted:
            if m[2] == "" or m[3] == "" or m[13] == "" or m[14] == "" or m[15] == "" or m[16] == "" or m[17] == "" or m[18] == "" or m[19] == "" or m[20] == "" or m[21] == "" or m[11] == "" or m[12] == "":
                continue
            else:
                inserted.append(m[2])
                statistics.append([m[2], m[3], m[13], m[14], m[15], m[16], m[17], m[18], m[19], m[20], m[21], m[11], m[12], 1, 0, 0, 0])
    x = 0
    while x < len(statistics):
        y = 0
        while y < len(statistics[x]):
            try:
                if float(statistics[x][6]) > float(statistics[x][5]):
                    firstServeWon_p = 0
                else:
                    firstServeWon_p = str(float(statistics[x][6]) / float(statistics[x][5]))
                #if firstServeWon_p > 1:
                #    firstServeWon = 0
                if int(statistics[x][8]) > int(statistics[x][7]):
                    secondServeWon_p = 0
                else:
                    secondServeWon_p = str(int(statistics[x][8]) / int(statistics[x][7]))
                #if secondServeWon_p > 1:
                #    secondServeWon_p = 0
                if int(statistics[x][2]) > int(statistics[x][4]):
                    ace_p = 0
                else:
                    ace_p = str(int(statistics[x][2]) / int(statistics[x][4]))
                #if ace_p > 1:
                #    ace_p = 0
                if int(statistics[x][3]) > int(statistics[x][4]):
                    doubleFaults_p = 0
                else:
                    doubleFaults_p = str(int(statistics[x][3]) / int(statistics[x][4]))
                #if doubleFaults_p > 1:
                #    doubleFaults_p = 0
                if not int(statistics[x][10]) == 0:
                    if int(statistics[x][9]) > int(statistics[x][10]):
                        breakPointsSaved_p = 0
                    else:
                        breakPointsSaved_p = str(int(statistics[x][9]) / int(statistics[x][10]))
                #    if breakPointsSaved_p > 1:
                #        breakPointsSaved_p = 0
                else:
                    breakPointsSaved_p = 0
                if not int(statistics[x][12]) == 0:
                    if int(statistics[x][11]) > int(statistics[x][12]):
                        opponentBreakPoints_p = 0
                    else:
                        opponentBreakPoints_p = str( 1 - (int(statistics[x][11]) / int(statistics[x][12])))
                    #if opponentBreakPoints_p > 1:
                    #    opponentBreakPoints_p = 0
                else:
                    opponentBreakPoints_p = 0
            except:
                break
            writable.append([statistics[x][0], statistics[x][1], ace_p, doubleFaults_p, firstServeWon_p, secondServeWon_p, breakPointsSaved_p, opponentBreakPoints_p, statistics[x][13], statistics[x][14], statistics[x][15], statistics[x][16]])
            break
            y = y +1
        x = x + 1

    print(writable)
    for w in writable:
        writer.writerow([w[0], w[1], w[2], w[3], w[4], w[5], w[6], w[7], w[8], w[9], w[10], w[11]])

    players.clear()
    matches.clear()
    inserted.clear()
    statistics.clear()
    writable.clear()


#WTA 2010/2019
with open("../../data/tennis_wta/wta_rankings_10s.csv", "r", encoding="utf8") as ranking_file:
    first_line = next(ranking_file)
    first_line = first_line.split(",")

    for line in ranking_file:
        player = line.split(",")
        if int(player[1]) <= 20 and not player[2] in players:
            players.append(player[2])
            print(players)

    ranking_file.close()

for i in range(2010, 2019):
    with open("../../data/tennis_wta/wta_matches_" + str(i) + ".csv", "r", encoding="utf8") as matches_file:      # 0 = w_id, 1 = w_name, 2 = l_id, 3 = l_name, 4 = w_ace, 5 = w_df, 6 = w_svpt, 7 = w_1stin, 8 = w_1stwon
        first_line = next(matches_file)                                                     # 9 = w_2ndwon, 10 = w_svgms, 11 = w_bpsaved, 12 = w_bpfaced, 13 = l_ace, 14 = l_df, 15 = l_svpt
        first_line = first_line.split(",")                                                  # 16 = l_1stin, 17 = l_1stwon, 18 = l_2ndwon, 19 = l_svgms, 20 = l_bpsaved, 21 = l_bpfaced, 22 = surface
        for line in matches_file:
            match = line.split(",")
            matches.append([match[7], match[10], match[15], match[18], match[27], match[28], match[29], match[30], match[31], match[32], match[33], match[34],
                            match[35], match[36], match[37], match[38], match[39], match[40], match[41], match[42], match[43], match[44], match[2]])
            #print(matches)

        matches_file.close()

with open("../../data/preprocessed/pca/wta_players_statistics_2010.csv", "w", newline='', encoding="utf8") as output:    # 0 = id, 1 = name, 2 = surname, 3 = ace , 4 = df, 5 = 1stWon
    writer = csv.writer(output, delimiter=",")                                                                  # 6 = 2ndWon, 7 = svGames, 8 = bpSaved, 9 = matches
    writer_header = csv.DictWriter(output, fieldnames=["id", "name", "ace", "df", "1stWon", "2ndWon", "bpSaved", "bpLost", "matches", "hard", "clay", "grass"])
    writer_header.writeheader()

    inserted = list()

    # statistics: 0 = id, 1 = name, 2 = ace, 3 = df, 4 = svPoints, 5 = 1stin, 6 = 1stwon, 7 = 2ndIn, 8 = 2ndwon, 8 = svGms, 9 = bpSaved, 10 = bpFaced, 11 = opponent_bpSaved
    for m in matches:                                                              # 12 = opponent_bpFaced , 13 = matches, 14 = hard, 15 = clay, 16 = grass
        if m[0] in (y for x in statistics for y in x) and m[0] in players:
            x = 0
            while x < len(statistics):
                y = 0
                while y < len(statistics[x]):
                    if statistics[x][0] == m[0]:
                        statistics[x][13] += 1      #update matches played
                        try:
                            statistics[x][6] = str(float(statistics[x][6]) + float(m[8]))   #update 1stWon
                            statistics[x][5] = str(int(statistics[x][5]) + int(m[7]))   #update 1stIn
                            statistics[x][8] = str(int(statistics[x][8]) + int(m[9]))   #update 2ndWon
                            statistics[x][7] = str(int(statistics[x][7]) + (int(m[6]) - (int(m[7]) + int(m[5]))))   #2ndIn = svPoints - (1stIn + doubleFaults)
                            statistics[x][2] = str(int(statistics[x][2]) + int(m[4]))   #update ace
                            statistics[x][4] = str(int(statistics[x][4]) + int(m[6]))   #update servicePoints
                            statistics[x][3] = str(int(statistics[x][3]) + int(m[5]))   #update doubleFaults
                            statistics[x][9] = str(int(statistics[x][9]) + int(m[11]))  #update bpSaved
                            statistics[x][10] = str(int(statistics[x][10]) + int(m[12]))    #update bpFaced
                            statistics[x][11] = str(int(statistics[x][11]) + int(m[20]))    #update opponent_bpSaved
                            statistics[x][12] = str(int(statistics[x][12]) + int(m[21]))    #update opponent_bpFaced
                            if m[22] == "Hard":
                                statistics[x][14] = str(int(statistics[x][14]) + 1)    #update hard victories
                            elif m[22] == "Clay":
                                statistics[x][15] = str(int(statistics[x][15]) + 1)    #update clay victories
                            else:
                                statistics[x][16] = str(int(statistics[x][16]) + 1)    #update grass victories
                            print(statistics[x])
                            break
                        except:
                            break
                    y = y + 1
                x = x + 1
        if not m[0] in inserted:
            if m[0] == "" or m[1] == "" or m[4] == "" or m[5] == "" or m[6] == "" or m[7] == "" or m[8] == "" or m[9] == "" or m[10] == "" or m[11] == "" or m[12] == "" or m[20] == "" or m[21] == "":
                continue
            else:
                inserted.append(m[0])
                if m[22] == "Hard":
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 1, 0, 0])
                elif m[22] == "Clay":
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 0, 1, 0])
                else:
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 0, 0, 1])
        if m[2] in (y for x in statistics for y in x) and m[2] in players:
            x = 0
            while x < len(statistics):
                y = 0
                while y < len(statistics[x]):
                    if statistics[x][0] == m[2]:
                        statistics[x][13] += 1      #update matches played
                        try:
                            statistics[x][6] = str(float(statistics[x][6]) + float(m[17]))   #update 1stWon
                            statistics[x][5] = str(int(statistics[x][5]) + int(m[16]))   #update 1stIn
                            statistics[x][8] = str(int(statistics[x][8]) + int(m[18]))   #update 2ndWon
                            statistics[x][7] = str(int(statistics[x][7]) + (int(m[15]) - (int(m[16]) + int(m[14]))))   #2ndIn = svPoints - (1stIn + doubleFaults)
                            statistics[x][2] = str(int(statistics[x][2]) + int(m[13]))   #update ace
                            statistics[x][4] = str(int(statistics[x][4]) + int(m[15]))   #update servicePoints
                            statistics[x][3] = str(int(statistics[x][3]) + int(m[14]))   #update doubleFaults
                            statistics[x][9] = str(int(statistics[x][9]) + int(m[20]))  #update bpSaved
                            statistics[x][10] = str(int(statistics[x][10]) + int(m[21]))    #update bpFaced
                            statistics[x][11] = str(int(statistics[x][11]) + int(m[11]))    #update opponent_bpSaved
                            statistics[x][12] = str(int(statistics[x][12]) + int(m[12]))    #update opponent_bpFaced
                            break
                        except:
                            break
                    y = y + 1
                x = x + 1
        if not m[2] in inserted:
            if m[2] == "" or m[3] == "" or m[13] == "" or m[14] == "" or m[15] == "" or m[16] == "" or m[17] == "" or m[18] == "" or m[19] == "" or m[20] == "" or m[21] == "" or m[11] == "" or m[12] == "":
                continue
            else:
                inserted.append(m[2])
                statistics.append([m[2], m[3], m[13], m[14], m[15], m[16], m[17], m[18], m[19], m[20], m[21], m[11], m[12], 1, 0, 0, 0])
    x = 0
    while x < len(statistics):
        y = 0
        while y < len(statistics[x]):
            try:
                if float(statistics[x][6]) > float(statistics[x][5]):
                    firstServeWon_p = 0
                else:
                    firstServeWon_p = str(float(statistics[x][6]) / float(statistics[x][5]))
                #if firstServeWon_p > 1:
                #    firstServeWon = 0
                if int(statistics[x][8]) > int(statistics[x][7]):
                    secondServeWon_p = 0
                else:
                    secondServeWon_p = str(int(statistics[x][8]) / int(statistics[x][7]))
                #if secondServeWon_p > 1:
                #    secondServeWon_p = 0
                if int(statistics[x][2]) > int(statistics[x][4]):
                    ace_p = 0
                else:
                    ace_p = str(int(statistics[x][2]) / int(statistics[x][4]))
                #if ace_p > 1:
                #    ace_p = 0
                if int(statistics[x][3]) > int(statistics[x][4]):
                    doubleFaults_p = 0
                else:
                    doubleFaults_p = str(int(statistics[x][3]) / int(statistics[x][4]))
                #if doubleFaults_p > 1:
                #    doubleFaults_p = 0
                if not int(statistics[x][10]) == 0:
                    if int(statistics[x][9]) > int(statistics[x][10]):
                        breakPointsSaved_p = 0
                    else:
                        breakPointsSaved_p = str(int(statistics[x][9]) / int(statistics[x][10]))
                #    if breakPointsSaved_p > 1:
                #        breakPointsSaved_p = 0
                else:
                    breakPointsSaved_p = 0
                if not int(statistics[x][12]) == 0:
                    if int(statistics[x][11]) > int(statistics[x][12]):
                        opponentBreakPoints_p = 0
                    else:
                        opponentBreakPoints_p = str( 1 - (int(statistics[x][11]) / int(statistics[x][12])))
                    #if opponentBreakPoints_p > 1:
                    #    opponentBreakPoints_p = 0
                else:
                    opponentBreakPoints_p = 0
            except:
                break
            writable.append([statistics[x][0], statistics[x][1], ace_p, doubleFaults_p, firstServeWon_p, secondServeWon_p, breakPointsSaved_p, opponentBreakPoints_p, statistics[x][13], statistics[x][14], statistics[x][15], statistics[x][16]])
            break
            y = y +1
        x = x + 1

    print(writable)
    for w in writable:
        writer.writerow([w[0], w[1], w[2], w[3], w[4], w[5], w[6], w[7], w[8], w[9], w[10], w[11]])

    players.clear()
    matches.clear()
    inserted.clear()
    statistics.clear()
    writable.clear()


#WTA 2000/2009
with open("../../data/tennis_wta/wta_rankings_00s.csv", "r", encoding="utf8") as ranking_file:
    first_line = next(ranking_file)
    first_line = first_line.split(",")

    for line in ranking_file:
        player = line.split(",")
        if int(player[1]) <= 20 and not player[2] in players:
            players.append(player[2])
            print(players)

    ranking_file.close()

for i in range(2000, 2009):
    with open("../../data/tennis_wta/wta_matches_" + str(i) + ".csv", "r", encoding="utf8") as matches_file:      # 0 = w_id, 1 = w_name, 2 = l_id, 3 = l_name, 4 = w_ace, 5 = w_df, 6 = w_svpt, 7 = w_1stin, 8 = w_1stwon
        first_line = next(matches_file)                                                     # 9 = w_2ndwon, 10 = w_svgms, 11 = w_bpsaved, 12 = w_bpfaced, 13 = l_ace, 14 = l_df, 15 = l_svpt
        first_line = first_line.split(",")                                                  # 16 = l_1stin, 17 = l_1stwon, 18 = l_2ndwon, 19 = l_svgms, 20 = l_bpsaved, 21 = l_bpfaced, 22 = surface
        for line in matches_file:
            match = line.split(",")
            matches.append([match[7], match[10], match[15], match[18], match[27], match[28], match[29], match[30], match[31], match[32], match[33], match[34],
                            match[35], match[36], match[37], match[38], match[39], match[40], match[41], match[42], match[43], match[44], match[2]])
            #print(matches)

        matches_file.close()

with open("../../data/preprocessed/pca/wta_players_statistics_2000.csv", "w", newline='', encoding="utf8") as output:    # 0 = id, 1 = name, 2 = surname, 3 = ace , 4 = df, 5 = 1stWon
    writer = csv.writer(output, delimiter=",")                                                                  # 6 = 2ndWon, 7 = svGames, 8 = bpSaved, 9 = matches
    writer_header = csv.DictWriter(output, fieldnames=["id", "name", "ace", "df", "1stWon", "2ndWon", "bpSaved", "bpLost", "matches", "hard", "clay", "grass"])
    writer_header.writeheader()

    inserted = list()

    # statistics: 0 = id, 1 = name, 2 = ace, 3 = df, 4 = svPoints, 5 = 1stin, 6 = 1stwon, 7 = 2ndIn, 8 = 2ndwon, 8 = svGms, 9 = bpSaved, 10 = bpFaced, 11 = opponent_bpSaved
    for m in matches:                                                              # 12 = opponent_bpFaced , 13 = matches, 14 = hard, 15 = clay, 16 = grass
        if m[0] in (y for x in statistics for y in x) and m[0] in players:
            x = 0
            while x < len(statistics):
                y = 0
                while y < len(statistics[x]):
                    if statistics[x][0] == m[0]:
                        statistics[x][13] += 1      #update matches played
                        try:
                            statistics[x][6] = str(float(statistics[x][6]) + float(m[8]))   #update 1stWon
                            statistics[x][5] = str(int(statistics[x][5]) + int(m[7]))   #update 1stIn
                            statistics[x][8] = str(int(statistics[x][8]) + int(m[9]))   #update 2ndWon
                            statistics[x][7] = str(int(statistics[x][7]) + (int(m[6]) - (int(m[7]) + int(m[5]))))   #2ndIn = svPoints - (1stIn + doubleFaults)
                            statistics[x][2] = str(int(statistics[x][2]) + int(m[4]))   #update ace
                            statistics[x][4] = str(int(statistics[x][4]) + int(m[6]))   #update servicePoints
                            statistics[x][3] = str(int(statistics[x][3]) + int(m[5]))   #update doubleFaults
                            statistics[x][9] = str(int(statistics[x][9]) + int(m[11]))  #update bpSaved
                            statistics[x][10] = str(int(statistics[x][10]) + int(m[12]))    #update bpFaced
                            statistics[x][11] = str(int(statistics[x][11]) + int(m[20]))    #update opponent_bpSaved
                            statistics[x][12] = str(int(statistics[x][12]) + int(m[21]))    #update opponent_bpFaced
                            if m[22] == "Hard":
                                statistics[x][14] = str(int(statistics[x][14]) + 1)    #update hard victories
                            elif m[22] == "Clay":
                                statistics[x][15] = str(int(statistics[x][15]) + 1)    #update clay victories
                            else:
                                statistics[x][16] = str(int(statistics[x][16]) + 1)    #update grass victories
                            print(statistics[x])
                            break
                        except:
                            break
                    y = y + 1
                x = x + 1
        if not m[0] in inserted:
            if m[0] == "" or m[1] == "" or m[4] == "" or m[5] == "" or m[6] == "" or m[7] == "" or m[8] == "" or m[9] == "" or m[10] == "" or m[11] == "" or m[12] == "" or m[20] == "" or m[21] == "":
                continue
            else:
                inserted.append(m[0])
                if m[22] == "Hard":
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 1, 0, 0])
                elif m[22] == "Clay":
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 0, 1, 0])
                else:
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 0, 0, 1])
        if m[2] in (y for x in statistics for y in x) and m[2] in players:
            x = 0
            while x < len(statistics):
                y = 0
                while y < len(statistics[x]):
                    if statistics[x][0] == m[2]:
                        statistics[x][13] += 1      #update matches played
                        try:
                            statistics[x][6] = str(float(statistics[x][6]) + float(m[17]))   #update 1stWon
                            statistics[x][5] = str(int(statistics[x][5]) + int(m[16]))   #update 1stIn
                            statistics[x][8] = str(int(statistics[x][8]) + int(m[18]))   #update 2ndWon
                            statistics[x][7] = str(int(statistics[x][7]) + (int(m[15]) - (int(m[16]) + int(m[14]))))   #2ndIn = svPoints - (1stIn + doubleFaults)
                            statistics[x][2] = str(int(statistics[x][2]) + int(m[13]))   #update ace
                            statistics[x][4] = str(int(statistics[x][4]) + int(m[15]))   #update servicePoints
                            statistics[x][3] = str(int(statistics[x][3]) + int(m[14]))   #update doubleFaults
                            statistics[x][9] = str(int(statistics[x][9]) + int(m[20]))  #update bpSaved
                            statistics[x][10] = str(int(statistics[x][10]) + int(m[21]))    #update bpFaced
                            statistics[x][11] = str(int(statistics[x][11]) + int(m[11]))    #update opponent_bpSaved
                            statistics[x][12] = str(int(statistics[x][12]) + int(m[12]))    #update opponent_bpFaced
                            break
                        except:
                            break
                    y = y + 1
                x = x + 1
        if not m[2] in inserted:
            if m[2] == "" or m[3] == "" or m[13] == "" or m[14] == "" or m[15] == "" or m[16] == "" or m[17] == "" or m[18] == "" or m[19] == "" or m[20] == "" or m[21] == "" or m[11] == "" or m[12] == "":
                continue
            else:
                inserted.append(m[2])
                statistics.append([m[2], m[3], m[13], m[14], m[15], m[16], m[17], m[18], m[19], m[20], m[21], m[11], m[12], 1, 0, 0, 0])
    x = 0
    while x < len(statistics):
        y = 0
        while y < len(statistics[x]):
            try:
                if float(statistics[x][6]) > float(statistics[x][5]):
                    firstServeWon_p = 0
                else:
                    firstServeWon_p = str(float(statistics[x][6]) / float(statistics[x][5]))
                #if firstServeWon_p > 1:
                #    firstServeWon = 0
                if int(statistics[x][8]) > int(statistics[x][7]):
                    secondServeWon_p = 0
                else:
                    secondServeWon_p = str(int(statistics[x][8]) / int(statistics[x][7]))
                #if secondServeWon_p > 1:
                #    secondServeWon_p = 0
                if int(statistics[x][2]) > int(statistics[x][4]):
                    ace_p = 0
                else:
                    ace_p = str(int(statistics[x][2]) / int(statistics[x][4]))
                #if ace_p > 1:
                #    ace_p = 0
                if int(statistics[x][3]) > int(statistics[x][4]):
                    doubleFaults_p = 0
                else:
                    doubleFaults_p = str(int(statistics[x][3]) / int(statistics[x][4]))
                #if doubleFaults_p > 1:
                #    doubleFaults_p = 0
                if not int(statistics[x][10]) == 0:
                    if int(statistics[x][9]) > int(statistics[x][10]):
                        breakPointsSaved_p = 0
                    else:
                        breakPointsSaved_p = str(int(statistics[x][9]) / int(statistics[x][10]))
                #    if breakPointsSaved_p > 1:
                #        breakPointsSaved_p = 0
                else:
                    breakPointsSaved_p = 0
                if not int(statistics[x][12]) == 0:
                    if int(statistics[x][11]) > int(statistics[x][12]):
                        opponentBreakPoints_p = 0
                    else:
                        opponentBreakPoints_p = str( 1 - (int(statistics[x][11]) / int(statistics[x][12])))
                    #if opponentBreakPoints_p > 1:
                    #    opponentBreakPoints_p = 0
                else:
                    opponentBreakPoints_p = 0
            except:
                break
            writable.append([statistics[x][0], statistics[x][1], ace_p, doubleFaults_p, firstServeWon_p, secondServeWon_p, breakPointsSaved_p, opponentBreakPoints_p, statistics[x][13], statistics[x][14], statistics[x][15], statistics[x][16]])
            break
            y = y +1
        x = x + 1

    print(writable)
    for w in writable:
        writer.writerow([w[0], w[1], w[2], w[3], w[4], w[5], w[6], w[7], w[8], w[9], w[10], w[11]])

    players.clear()
    matches.clear()
    inserted.clear()
    statistics.clear()
    writable.clear()


#WTA 1990/1999
with open("../../data/tennis_wta/wta_rankings_90s.csv", "r", encoding="utf8") as ranking_file:
    first_line = next(ranking_file)
    first_line = first_line.split(",")

    for line in ranking_file:
        player = line.split(",")
        if int(player[1]) <= 20 and not player[2] in players:
            players.append(player[2])
            print(players)

    ranking_file.close()

for i in range(1990, 1999):
    with open("../../data/tennis_wta/wta_matches_" + str(i) + ".csv", "r", encoding="utf8") as matches_file:      # 0 = w_id, 1 = w_name, 2 = l_id, 3 = l_name, 4 = w_ace, 5 = w_df, 6 = w_svpt, 7 = w_1stin, 8 = w_1stwon
        first_line = next(matches_file)                                                     # 9 = w_2ndwon, 10 = w_svgms, 11 = w_bpsaved, 12 = w_bpfaced, 13 = l_ace, 14 = l_df, 15 = l_svpt
        first_line = first_line.split(",")                                                  # 16 = l_1stin, 17 = l_1stwon, 18 = l_2ndwon, 19 = l_svgms, 20 = l_bpsaved, 21 = l_bpfaced, 22 = surface
        for line in matches_file:
            match = line.split(",")
            matches.append([match[7], match[10], match[15], match[18], match[27], match[28], match[29], match[30], match[31], match[32], match[33], match[34],
                            match[35], match[36], match[37], match[38], match[39], match[40], match[41], match[42], match[43], match[44], match[2]])
            #print(matches)

        matches_file.close()

with open("../../data/preprocessed/pca/wta_players_statistics_1990.csv", "w", newline='', encoding="utf8") as output:    # 0 = id, 1 = name, 2 = surname, 3 = ace , 4 = df, 5 = 1stWon
    writer = csv.writer(output, delimiter=",")                                                                  # 6 = 2ndWon, 7 = svGames, 8 = bpSaved, 9 = matches
    writer_header = csv.DictWriter(output, fieldnames=["id", "name", "ace", "df", "1stWon", "2ndWon", "bpSaved", "bpLost", "matches", "hard", "clay", "grass"])
    writer_header.writeheader()

    inserted = list()

    # statistics: 0 = id, 1 = name, 2 = ace, 3 = df, 4 = svPoints, 5 = 1stin, 6 = 1stwon, 7 = 2ndIn, 8 = 2ndwon, 8 = svGms, 9 = bpSaved, 10 = bpFaced, 11 = opponent_bpSaved
    for m in matches:                                                              # 12 = opponent_bpFaced , 13 = matches, 14 = hard, 15 = clay, 16 = grass
        if m[0] in (y for x in statistics for y in x) and m[0] in players:
            x = 0
            while x < len(statistics):
                y = 0
                while y < len(statistics[x]):
                    if statistics[x][0] == m[0]:
                        statistics[x][13] += 1      #update matches played
                        try:
                            statistics[x][6] = str(float(statistics[x][6]) + float(m[8]))   #update 1stWon
                            statistics[x][5] = str(int(statistics[x][5]) + int(m[7]))   #update 1stIn
                            statistics[x][8] = str(int(statistics[x][8]) + int(m[9]))   #update 2ndWon
                            statistics[x][7] = str(int(statistics[x][7]) + (int(m[6]) - (int(m[7]) + int(m[5]))))   #2ndIn = svPoints - (1stIn + doubleFaults)
                            statistics[x][2] = str(int(statistics[x][2]) + int(m[4]))   #update ace
                            statistics[x][4] = str(int(statistics[x][4]) + int(m[6]))   #update servicePoints
                            statistics[x][3] = str(int(statistics[x][3]) + int(m[5]))   #update doubleFaults
                            statistics[x][9] = str(int(statistics[x][9]) + int(m[11]))  #update bpSaved
                            statistics[x][10] = str(int(statistics[x][10]) + int(m[12]))    #update bpFaced
                            statistics[x][11] = str(int(statistics[x][11]) + int(m[20]))    #update opponent_bpSaved
                            statistics[x][12] = str(int(statistics[x][12]) + int(m[21]))    #update opponent_bpFaced
                            if m[22] == "Hard":
                                statistics[x][14] = str(int(statistics[x][14]) + 1)    #update hard victories
                            elif m[22] == "Clay":
                                statistics[x][15] = str(int(statistics[x][15]) + 1)    #update clay victories
                            else:
                                statistics[x][16] = str(int(statistics[x][16]) + 1)    #update grass victories
                            print(statistics[x])
                            break
                        except:
                            break
                    y = y + 1
                x = x + 1
        if not m[0] in inserted:
            if m[0] == "" or m[1] == "" or m[4] == "" or m[5] == "" or m[6] == "" or m[7] == "" or m[8] == "" or m[9] == "" or m[10] == "" or m[11] == "" or m[12] == "" or m[20] == "" or m[21] == "":
                continue
            else:
                inserted.append(m[0])
                if m[22] == "Hard":
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 1, 0, 0])
                elif m[22] == "Clay":
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 0, 1, 0])
                else:
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 0, 0, 1])
        if m[2] in (y for x in statistics for y in x) and m[2] in players:
            x = 0
            while x < len(statistics):
                y = 0
                while y < len(statistics[x]):
                    if statistics[x][0] == m[2]:
                        statistics[x][13] += 1      #update matches played
                        try:
                            statistics[x][6] = str(float(statistics[x][6]) + float(m[17]))   #update 1stWon
                            statistics[x][5] = str(int(statistics[x][5]) + int(m[16]))   #update 1stIn
                            statistics[x][8] = str(int(statistics[x][8]) + int(m[18]))   #update 2ndWon
                            statistics[x][7] = str(int(statistics[x][7]) + (int(m[15]) - (int(m[16]) + int(m[14]))))   #2ndIn = svPoints - (1stIn + doubleFaults)
                            statistics[x][2] = str(int(statistics[x][2]) + int(m[13]))   #update ace
                            statistics[x][4] = str(int(statistics[x][4]) + int(m[15]))   #update servicePoints
                            statistics[x][3] = str(int(statistics[x][3]) + int(m[14]))   #update doubleFaults
                            statistics[x][9] = str(int(statistics[x][9]) + int(m[20]))  #update bpSaved
                            statistics[x][10] = str(int(statistics[x][10]) + int(m[21]))    #update bpFaced
                            statistics[x][11] = str(int(statistics[x][11]) + int(m[11]))    #update opponent_bpSaved
                            statistics[x][12] = str(int(statistics[x][12]) + int(m[12]))    #update opponent_bpFaced
                            break
                        except:
                            break
                    y = y + 1
                x = x + 1
        if not m[2] in inserted:
            if m[2] == "" or m[3] == "" or m[13] == "" or m[14] == "" or m[15] == "" or m[16] == "" or m[17] == "" or m[18] == "" or m[19] == "" or m[20] == "" or m[21] == "" or m[11] == "" or m[12] == "":
                continue
            else:
                inserted.append(m[2])
                statistics.append([m[2], m[3], m[13], m[14], m[15], m[16], m[17], m[18], m[19], m[20], m[21], m[11], m[12], 1, 0, 0, 0])
    x = 0
    while x < len(statistics):
        y = 0
        while y < len(statistics[x]):
            try:
                if float(statistics[x][6]) > float(statistics[x][5]):
                    firstServeWon_p = 0
                else:
                    firstServeWon_p = str(float(statistics[x][6]) / float(statistics[x][5]))
                #if firstServeWon_p > 1:
                #    firstServeWon = 0
                if int(statistics[x][8]) > int(statistics[x][7]):
                    secondServeWon_p = 0
                else:
                    secondServeWon_p = str(int(statistics[x][8]) / int(statistics[x][7]))
                #if secondServeWon_p > 1:
                #    secondServeWon_p = 0
                if int(statistics[x][2]) > int(statistics[x][4]):
                    ace_p = 0
                else:
                    ace_p = str(int(statistics[x][2]) / int(statistics[x][4]))
                #if ace_p > 1:
                #    ace_p = 0
                if int(statistics[x][3]) > int(statistics[x][4]):
                    doubleFaults_p = 0
                else:
                    doubleFaults_p = str(int(statistics[x][3]) / int(statistics[x][4]))
                #if doubleFaults_p > 1:
                #    doubleFaults_p = 0
                if not int(statistics[x][10]) == 0:
                    if int(statistics[x][9]) > int(statistics[x][10]):
                        breakPointsSaved_p = 0
                    else:
                        breakPointsSaved_p = str(int(statistics[x][9]) / int(statistics[x][10]))
                #    if breakPointsSaved_p > 1:
                #        breakPointsSaved_p = 0
                else:
                    breakPointsSaved_p = 0
                if not int(statistics[x][12]) == 0:
                    if int(statistics[x][11]) > int(statistics[x][12]):
                        opponentBreakPoints_p = 0
                    else:
                        opponentBreakPoints_p = str( 1 - (int(statistics[x][11]) / int(statistics[x][12])))
                    #if opponentBreakPoints_p > 1:
                    #    opponentBreakPoints_p = 0
                else:
                    opponentBreakPoints_p = 0
            except:
                break
            writable.append([statistics[x][0], statistics[x][1], ace_p, doubleFaults_p, firstServeWon_p, secondServeWon_p, breakPointsSaved_p, opponentBreakPoints_p, statistics[x][13], statistics[x][14], statistics[x][15], statistics[x][16]])
            break
            y = y +1
        x = x + 1

    print(writable)
    for w in writable:
        writer.writerow([w[0], w[1], w[2], w[3], w[4], w[5], w[6], w[7], w[8], w[9], w[10], w[11]])

    players.clear()
    matches.clear()
    inserted.clear()
    statistics.clear()
    writable.clear()

#WTA 1980/1989
with open("../../data/tennis_wta/wta_rankings_80s.csv", "r", encoding="utf8") as ranking_file:
    first_line = next(ranking_file)
    first_line = first_line.split(",")

    for line in ranking_file:
        player = line.split(",")
        if int(player[1]) <= 20 and not player[2] in players:
            players.append(player[2])
            print(players)

    ranking_file.close()

for i in range(1980, 1989):
    with open("../../data/tennis_wta/wta_matches_" + str(i) + ".csv", "r", encoding="utf8") as matches_file:      # 0 = w_id, 1 = w_name, 2 = l_id, 3 = l_name, 4 = w_ace, 5 = w_df, 6 = w_svpt, 7 = w_1stin, 8 = w_1stwon
        first_line = next(matches_file)                                                     # 9 = w_2ndwon, 10 = w_svgms, 11 = w_bpsaved, 12 = w_bpfaced, 13 = l_ace, 14 = l_df, 15 = l_svpt
        first_line = first_line.split(",")                                                  # 16 = l_1stin, 17 = l_1stwon, 18 = l_2ndwon, 19 = l_svgms, 20 = l_bpsaved, 21 = l_bpfaced, 22 = surface
        for line in matches_file:
            match = line.split(",")
            matches.append([match[7], match[10], match[15], match[18], match[27], match[28], match[29], match[30], match[31], match[32], match[33], match[34],
                            match[35], match[36], match[37], match[38], match[39], match[40], match[41], match[42], match[43], match[44], match[2]])
            #print(matches)

        matches_file.close()

with open("../../data/preprocessed/pca/wta_players_statistics_1980.csv", "w", newline='', encoding="utf8") as output:    # 0 = id, 1 = name, 2 = surname, 3 = ace , 4 = df, 5 = 1stWon
    writer = csv.writer(output, delimiter=",")                                                                  # 6 = 2ndWon, 7 = svGames, 8 = bpSaved, 9 = matches
    writer_header = csv.DictWriter(output, fieldnames=["id", "name", "ace", "df", "1stWon", "2ndWon", "bpSaved", "bpLost", "matches", "hard", "clay", "grass"])
    writer_header.writeheader()

    inserted = list()

    # statistics: 0 = id, 1 = name, 2 = ace, 3 = df, 4 = svPoints, 5 = 1stin, 6 = 1stwon, 7 = 2ndIn, 8 = 2ndwon, 8 = svGms, 9 = bpSaved, 10 = bpFaced, 11 = opponent_bpSaved
    for m in matches:                                                              # 12 = opponent_bpFaced , 13 = matches, 14 = hard, 15 = clay, 16 = grass
        if m[0] in (y for x in statistics for y in x) and m[0] in players:
            x = 0
            while x < len(statistics):
                y = 0
                while y < len(statistics[x]):
                    if statistics[x][0] == m[0]:
                        statistics[x][13] += 1      #update matches played
                        try:
                            statistics[x][6] = str(float(statistics[x][6]) + float(m[8]))   #update 1stWon
                            statistics[x][5] = str(int(statistics[x][5]) + int(m[7]))   #update 1stIn
                            statistics[x][8] = str(int(statistics[x][8]) + int(m[9]))   #update 2ndWon
                            statistics[x][7] = str(int(statistics[x][7]) + (int(m[6]) - (int(m[7]) + int(m[5]))))   #2ndIn = svPoints - (1stIn + doubleFaults)
                            statistics[x][2] = str(int(statistics[x][2]) + int(m[4]))   #update ace
                            statistics[x][4] = str(int(statistics[x][4]) + int(m[6]))   #update servicePoints
                            statistics[x][3] = str(int(statistics[x][3]) + int(m[5]))   #update doubleFaults
                            statistics[x][9] = str(int(statistics[x][9]) + int(m[11]))  #update bpSaved
                            statistics[x][10] = str(int(statistics[x][10]) + int(m[12]))    #update bpFaced
                            statistics[x][11] = str(int(statistics[x][11]) + int(m[20]))    #update opponent_bpSaved
                            statistics[x][12] = str(int(statistics[x][12]) + int(m[21]))    #update opponent_bpFaced
                            if m[22] == "Hard":
                                statistics[x][14] = str(int(statistics[x][14]) + 1)    #update hard victories
                            elif m[22] == "Clay":
                                statistics[x][15] = str(int(statistics[x][15]) + 1)    #update clay victories
                            else:
                                statistics[x][16] = str(int(statistics[x][16]) + 1)    #update grass victories
                            print(statistics[x])
                            break
                        except:
                            break
                    y = y + 1
                x = x + 1
        if not m[0] in inserted:
            if m[0] == "" or m[1] == "" or m[4] == "" or m[5] == "" or m[6] == "" or m[7] == "" or m[8] == "" or m[9] == "" or m[10] == "" or m[11] == "" or m[12] == "" or m[20] == "" or m[21] == "":
                continue
            else:
                inserted.append(m[0])
                if m[22] == "Hard":
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 1, 0, 0])
                elif m[22] == "Clay":
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 0, 1, 0])
                else:
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 0, 0, 1])
        if m[2] in (y for x in statistics for y in x) and m[2] in players:
            x = 0
            while x < len(statistics):
                y = 0
                while y < len(statistics[x]):
                    if statistics[x][0] == m[2]:
                        statistics[x][13] += 1      #update matches played
                        try:
                            statistics[x][6] = str(float(statistics[x][6]) + float(m[17]))   #update 1stWon
                            statistics[x][5] = str(int(statistics[x][5]) + int(m[16]))   #update 1stIn
                            statistics[x][8] = str(int(statistics[x][8]) + int(m[18]))   #update 2ndWon
                            statistics[x][7] = str(int(statistics[x][7]) + (int(m[15]) - (int(m[16]) + int(m[14]))))   #2ndIn = svPoints - (1stIn + doubleFaults)
                            statistics[x][2] = str(int(statistics[x][2]) + int(m[13]))   #update ace
                            statistics[x][4] = str(int(statistics[x][4]) + int(m[15]))   #update servicePoints
                            statistics[x][3] = str(int(statistics[x][3]) + int(m[14]))   #update doubleFaults
                            statistics[x][9] = str(int(statistics[x][9]) + int(m[20]))  #update bpSaved
                            statistics[x][10] = str(int(statistics[x][10]) + int(m[21]))    #update bpFaced
                            statistics[x][11] = str(int(statistics[x][11]) + int(m[11]))    #update opponent_bpSaved
                            statistics[x][12] = str(int(statistics[x][12]) + int(m[12]))    #update opponent_bpFaced
                            break
                        except:
                            break
                    y = y + 1
                x = x + 1
        if not m[2] in inserted:
            if m[2] == "" or m[3] == "" or m[13] == "" or m[14] == "" or m[15] == "" or m[16] == "" or m[17] == "" or m[18] == "" or m[19] == "" or m[20] == "" or m[21] == "" or m[11] == "" or m[12] == "":
                continue
            else:
                inserted.append(m[2])
                statistics.append([m[2], m[3], m[13], m[14], m[15], m[16], m[17], m[18], m[19], m[20], m[21], m[11], m[12], 1, 0, 0, 0])
    x = 0
    while x < len(statistics):
        y = 0
        while y < len(statistics[x]):
            try:
                if float(statistics[x][6]) > float(statistics[x][5]):
                    firstServeWon_p = 0
                else:
                    firstServeWon_p = str(float(statistics[x][6]) / float(statistics[x][5]))
                #if firstServeWon_p > 1:
                #    firstServeWon = 0
                if int(statistics[x][8]) > int(statistics[x][7]):
                    secondServeWon_p = 0
                else:
                    secondServeWon_p = str(int(statistics[x][8]) / int(statistics[x][7]))
                #if secondServeWon_p > 1:
                #    secondServeWon_p = 0
                if int(statistics[x][2]) > int(statistics[x][4]):
                    ace_p = 0
                else:
                    ace_p = str(int(statistics[x][2]) / int(statistics[x][4]))
                #if ace_p > 1:
                #    ace_p = 0
                if int(statistics[x][3]) > int(statistics[x][4]):
                    doubleFaults_p = 0
                else:
                    doubleFaults_p = str(int(statistics[x][3]) / int(statistics[x][4]))
                #if doubleFaults_p > 1:
                #    doubleFaults_p = 0
                if not int(statistics[x][10]) == 0:
                    if int(statistics[x][9]) > int(statistics[x][10]):
                        breakPointsSaved_p = 0
                    else:
                        breakPointsSaved_p = str(int(statistics[x][9]) / int(statistics[x][10]))
                #    if breakPointsSaved_p > 1:
                #        breakPointsSaved_p = 0
                else:
                    breakPointsSaved_p = 0
                if not int(statistics[x][12]) == 0:
                    if int(statistics[x][11]) > int(statistics[x][12]):
                        opponentBreakPoints_p = 0
                    else:
                        opponentBreakPoints_p = str( 1 - (int(statistics[x][11]) / int(statistics[x][12])))
                    #if opponentBreakPoints_p > 1:
                    #    opponentBreakPoints_p = 0
                else:
                    opponentBreakPoints_p = 0
            except:
                break
            writable.append([statistics[x][0], statistics[x][1], ace_p, doubleFaults_p, firstServeWon_p, secondServeWon_p, breakPointsSaved_p, opponentBreakPoints_p, statistics[x][13], statistics[x][14], statistics[x][15], statistics[x][16]])
            break
            y = y +1
        x = x + 1

    print(writable)
    for w in writable:
        writer.writerow([w[0], w[1], w[2], w[3], w[4], w[5], w[6], w[7], w[8], w[9], w[10], w[11]])

    players.clear()
    matches.clear()
    inserted.clear()
    statistics.clear()
    writable.clear()

#WTA All-time
years = ["80", "90", "00", "10"]
for i in years:
    with open("../../data/tennis_wta/wta_rankings_" + i + "s.csv", "r", encoding="utf8") as ranking_file:
        first_line = next(ranking_file)
        first_line = first_line.split(",")

        for line in ranking_file:
            player = line.split(",")
            if int(player[1]) <= 20 and not player[2] in players:
                players.append(player[2])
                print(players)

        ranking_file.close()

for i in range(1980, 2021):
    with open("../../data/tennis_wta/wta_matches_" + str(i) + ".csv", "r", encoding="utf8") as matches_file:      # 0 = w_id, 1 = w_name, 2 = l_id, 3 = l_name, 4 = w_ace, 5 = w_df, 6 = w_svpt, 7 = w_1stin, 8 = w_1stwon
        first_line = next(matches_file)                                                     # 9 = w_2ndwon, 10 = w_svgms, 11 = w_bpsaved, 12 = w_bpfaced, 13 = l_ace, 14 = l_df, 15 = l_svpt
        first_line = first_line.split(",")                                                  # 16 = l_1stin, 17 = l_1stwon, 18 = l_2ndwon, 19 = l_svgms, 20 = l_bpsaved, 21 = l_bpfaced, 22 = surface
        for line in matches_file:
            match = line.split(",")
            matches.append([match[7], match[10], match[15], match[18], match[27], match[28], match[29], match[30], match[31], match[32], match[33], match[34],
                            match[35], match[36], match[37], match[38], match[39], match[40], match[41], match[42], match[43], match[44], match[2]])
            #print(matches)

        matches_file.close()

with open("../../data/preprocessed/pca/wta_players_statistics_all.csv", "w", newline='', encoding="utf8") as output:    # 0 = id, 1 = name, 2 = surname, 3 = ace , 4 = df, 5 = 1stWon
    writer = csv.writer(output, delimiter=",")                                                                  # 6 = 2ndWon, 7 = svGames, 8 = bpSaved, 9 = matches
    writer_header = csv.DictWriter(output, fieldnames=["id", "name", "ace", "df", "1stWon", "2ndWon", "bpSaved", "bpLost", "matches", "hard", "clay", "grass"])
    writer_header.writeheader()

    inserted = list()

    # statistics: 0 = id, 1 = name, 2 = ace, 3 = df, 4 = svPoints, 5 = 1stin, 6 = 1stwon, 7 = 2ndIn, 8 = 2ndwon, 8 = svGms, 9 = bpSaved, 10 = bpFaced, 11 = opponent_bpSaved
    for m in matches:                                                              # 12 = opponent_bpFaced , 13 = matches, 14 = hard, 15 = clay, 16 = grass
        if m[0] in (y for x in statistics for y in x) and m[0] in players:
            x = 0
            while x < len(statistics):
                y = 0
                while y < len(statistics[x]):
                    if statistics[x][0] == m[0]:
                        statistics[x][13] += 1      #update matches played
                        try:
                            statistics[x][6] = str(float(statistics[x][6]) + float(m[8]))   #update 1stWon
                            statistics[x][5] = str(int(statistics[x][5]) + int(m[7]))   #update 1stIn
                            statistics[x][8] = str(int(statistics[x][8]) + int(m[9]))   #update 2ndWon
                            statistics[x][7] = str(int(statistics[x][7]) + (int(m[6]) - (int(m[7]) + int(m[5]))))   #2ndIn = svPoints - (1stIn + doubleFaults)
                            statistics[x][2] = str(int(statistics[x][2]) + int(m[4]))   #update ace
                            statistics[x][4] = str(int(statistics[x][4]) + int(m[6]))   #update servicePoints
                            statistics[x][3] = str(int(statistics[x][3]) + int(m[5]))   #update doubleFaults
                            statistics[x][9] = str(int(statistics[x][9]) + int(m[11]))  #update bpSaved
                            statistics[x][10] = str(int(statistics[x][10]) + int(m[12]))    #update bpFaced
                            statistics[x][11] = str(int(statistics[x][11]) + int(m[20]))    #update opponent_bpSaved
                            statistics[x][12] = str(int(statistics[x][12]) + int(m[21]))    #update opponent_bpFaced
                            if m[22] == "Hard":
                                statistics[x][14] = str(int(statistics[x][14]) + 1)    #update hard victories
                            elif m[22] == "Clay":
                                statistics[x][15] = str(int(statistics[x][15]) + 1)    #update clay victories
                            else:
                                statistics[x][16] = str(int(statistics[x][16]) + 1)    #update grass victories
                            print(statistics[x])
                            break
                        except:
                            break
                    y = y + 1
                x = x + 1
        if not m[0] in inserted:
            if m[0] == "" or m[1] == "" or m[4] == "" or m[5] == "" or m[6] == "" or m[7] == "" or m[8] == "" or m[9] == "" or m[10] == "" or m[11] == "" or m[12] == "" or m[20] == "" or m[21] == "":
                continue
            else:
                inserted.append(m[0])
                if m[22] == "Hard":
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 1, 0, 0])
                elif m[22] == "Clay":
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 0, 1, 0])
                else:
                    statistics.append([m[0], m[1], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[20], m[21], 1, 0, 0, 1])
        if m[2] in (y for x in statistics for y in x) and m[2] in players:
            x = 0
            while x < len(statistics):
                y = 0
                while y < len(statistics[x]):
                    if statistics[x][0] == m[2]:
                        statistics[x][13] += 1      #update matches played
                        try:
                            statistics[x][6] = str(float(statistics[x][6]) + float(m[17]))   #update 1stWon
                            statistics[x][5] = str(int(statistics[x][5]) + int(m[16]))   #update 1stIn
                            statistics[x][8] = str(int(statistics[x][8]) + int(m[18]))   #update 2ndWon
                            statistics[x][7] = str(int(statistics[x][7]) + (int(m[15]) - (int(m[16]) + int(m[14]))))   #2ndIn = svPoints - (1stIn + doubleFaults)
                            statistics[x][2] = str(int(statistics[x][2]) + int(m[13]))   #update ace
                            statistics[x][4] = str(int(statistics[x][4]) + int(m[15]))   #update servicePoints
                            statistics[x][3] = str(int(statistics[x][3]) + int(m[14]))   #update doubleFaults
                            statistics[x][9] = str(int(statistics[x][9]) + int(m[20]))  #update bpSaved
                            statistics[x][10] = str(int(statistics[x][10]) + int(m[21]))    #update bpFaced
                            statistics[x][11] = str(int(statistics[x][11]) + int(m[11]))    #update opponent_bpSaved
                            statistics[x][12] = str(int(statistics[x][12]) + int(m[12]))    #update opponent_bpFaced
                            break
                        except:
                            break
                    y = y + 1
                x = x + 1
        if not m[2] in inserted:
            if m[2] == "" or m[3] == "" or m[13] == "" or m[14] == "" or m[15] == "" or m[16] == "" or m[17] == "" or m[18] == "" or m[19] == "" or m[20] == "" or m[21] == "" or m[11] == "" or m[12] == "":
                continue
            else:
                inserted.append(m[2])
                statistics.append([m[2], m[3], m[13], m[14], m[15], m[16], m[17], m[18], m[19], m[20], m[21], m[11], m[12], 1, 0, 0, 0])
    x = 0
    while x < len(statistics):
        y = 0
        while y < len(statistics[x]):
            try:
                if float(statistics[x][6]) > float(statistics[x][5]):
                    firstServeWon_p = 0
                else:
                    firstServeWon_p = str(float(statistics[x][6]) / float(statistics[x][5]))
                #if firstServeWon_p > 1:
                #    firstServeWon = 0
                if int(statistics[x][8]) > int(statistics[x][7]):
                    secondServeWon_p = 0
                else:
                    secondServeWon_p = str(int(statistics[x][8]) / int(statistics[x][7]))
                #if secondServeWon_p > 1:
                #    secondServeWon_p = 0
                if int(statistics[x][2]) > int(statistics[x][4]):
                    ace_p = 0
                else:
                    ace_p = str(int(statistics[x][2]) / int(statistics[x][4]))
                #if ace_p > 1:
                #    ace_p = 0
                if int(statistics[x][3]) > int(statistics[x][4]):
                    doubleFaults_p = 0
                else:
                    doubleFaults_p = str(int(statistics[x][3]) / int(statistics[x][4]))
                #if doubleFaults_p > 1:
                #    doubleFaults_p = 0
                if not int(statistics[x][10]) == 0:
                    if int(statistics[x][9]) > int(statistics[x][10]):
                        breakPointsSaved_p = 0
                    else:
                        breakPointsSaved_p = str(int(statistics[x][9]) / int(statistics[x][10]))
                #    if breakPointsSaved_p > 1:
                #        breakPointsSaved_p = 0
                else:
                    breakPointsSaved_p = 0
                if not int(statistics[x][12]) == 0:
                    if int(statistics[x][11]) > int(statistics[x][12]):
                        opponentBreakPoints_p = 0
                    else:
                        opponentBreakPoints_p = str( 1 - (int(statistics[x][11]) / int(statistics[x][12])))
                    #if opponentBreakPoints_p > 1:
                    #    opponentBreakPoints_p = 0
                else:
                    opponentBreakPoints_p = 0
            except:
                break
            writable.append([statistics[x][0], statistics[x][1], ace_p, doubleFaults_p, firstServeWon_p, secondServeWon_p, breakPointsSaved_p, opponentBreakPoints_p, statistics[x][13], statistics[x][14], statistics[x][15], statistics[x][16]])
            break
            y = y +1
        x = x + 1

    print(writable)
    for w in writable:
        writer.writerow([w[0], w[1], w[2], w[3], w[4], w[5], w[6], w[7], w[8], w[9], w[10], w[11]])

    players.clear()
    matches.clear()
    inserted.clear()
    statistics.clear()
    writable.clear()
