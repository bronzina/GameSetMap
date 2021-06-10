import csv
import pandas as pd

players = []

#ATP All-time
players_file_atp = "../../data/preprocessed/bar/atp_grandSlams_all.csv"
database_file_atp = "../../data/preprocessed/line/atp_grandSlams_all.csv"

#Sort the origin file
db = pd.read_csv(players_file_atp, skip_blank_lines=True, names=['id','name','grandSlamFinals','grandSlamTitles', 'list'], header=0)
db.drop_duplicates(inplace=True)
db.sort_values(by=['grandSlamTitles'], ascending=False).to_csv(database_file_atp, index=False)

#Pick only the needed players
with open(database_file_atp, "r", encoding="utf8") as players_file: #player[0] = id, player[1] = name, player[2] = finals, player[3] = titles, player[4] = list
    first_line = next(players_file)
    first_line = first_line.split(",")

    i = 0
    for line in players_file:
        if i < 10:
            player = line.split(",")
            players.append(player)
        i = i+1

    print(players)
    players_file.close()

found = []
ranking = []
present = []
ticks = []
years = ["70", "80", "90", "00", "10", "20"]
for i in years:
    with open("../../data/tennis_atp/atp_rankings_" + i + "s.csv", "r", encoding="utf8") as rankings_file:
        first_line = next(rankings_file)
        first_line = first_line.split(",")

        for line in rankings_file:
            rank = line.split(",")
            for p in players:
                if rank[2] == p[0]:
                    year = int(rank[0][:4])
                    pos = int(rank[1])
                    if not p[0] in present:
                        present.append(p[0])
                        ticks.append({"id": p[0], "name": p[1], "years":[year], "position": [pos]})
                    else:
                        m = 0
                        while m < len(ticks):
                            if p[0] == ticks[m]["id"]:
                                if not year in ticks[m]["years"]:
                                    ticks[m]["years"].append(year)
                                    ticks[m]["position"].append(pos)
                                else:
                                    x = 0
                                    while x < len(ticks[m]["years"]):
                                        if p[0] == ticks[m]["id"]:
                                            if year == ticks[m]["years"][x]:
                                                if pos < ticks[m]["position"][x]:
                                                    ticks[m]["position"][x] = pos
                                                    #print(ticks[m])
                                        x = x+1
                            m = m+1
    rankings_file.close()


with open("../../data/tennis_atp/atp_rankings_current.csv", "r", encoding="utf8") as rankings_file:
    first_line = next(rankings_file)
    first_line = first_line.split(",")

    for line in rankings_file:
        rank = line.split(",")
        for p in players:
            if rank[2] == p[0]:
                year = int(rank[0][:4])
                pos = int(rank[1])
                if not p[0] in present:
                    present.append(p[0])
                    ticks.append({"id": p[0], "name": p[1], "years":[year], "position": [pos]})
                else:
                    m = 0
                    while m < len(ticks):
                        if p[0] == ticks[m]["id"]:
                            if not year in ticks[m]["years"]:
                                ticks[m]["years"].append(year)
                                ticks[m]["position"].append(pos)
                            else:
                                x = 0
                                while x < len(ticks[m]["years"]):
                                    if p[0] == ticks[m]["id"]:
                                        if year == ticks[m]["years"][x]:
                                            if pos < ticks[m]["position"][x]:
                                                ticks[m]["position"][x] = pos
                                                #print(ticks[m])
                                    x = x+1
                        m = m+1
    rankings_file.close()

    #print(ticks)
    rankings_file.close()


with open("../../data/preprocessed/line/atp_rankings_trend_all.csv",'w', newline='', encoding="utf8") as output:
    writer = csv.writer(output, delimiter=",")
    writer_header = csv.DictWriter(output, fieldnames=["id", "name", "year", "position"])
    writer_header.writeheader()

    for t in ticks:
        writer.writerow([t["id"], t["name"], t["years"], t["position"]])


players.clear()
present.clear()
ticks.clear()

#ATP

for j in [1980, 1990, 2000, 2010, 2020, 2021]:
    players_file_atp = "../../data/preprocessed/bar/atp_grandSlams_"+ str(j) +".csv"
    database_file_atp = "../../data/preprocessed/line/atp_grandSlams_"+ str(j) +".csv"

    #Sort the origin file
    db = pd.read_csv(players_file_atp, skip_blank_lines=True, names=['id','name','grandSlamFinals','grandSlamTitles', 'list'], header=0)
    db.drop_duplicates(inplace=True)
    db.sort_values(by=['grandSlamTitles'], ascending=False).to_csv(database_file_atp, index=False)

    #Pick only the needed players
    with open(database_file_atp, "r", encoding="utf8") as players_file: #player[0] = id, player[1] = name, player[2] = finals, player[3] = titles, player[4] = list
        first_line = next(players_file)
        first_line = first_line.split(",")

        i = 0
        for line in players_file:
            if i < 10:
                player = line.split(",")
                players.append(player)
            i = i+1

        print(players)
        players_file.close()

    found = []
    ranking = []
    present = []
    ticks = []
    years = ["70", "80", "90", "00", "10", "20"]
    for i in years:
        with open("../../data/tennis_atp/atp_rankings_" + i + "s.csv", "r", encoding="utf8") as rankings_file:
            first_line = next(rankings_file)
            first_line = first_line.split(",")

            for line in rankings_file:
                rank = line.split(",")
                for p in players:
                    if rank[2] == p[0]:
                        year = int(rank[0][:4])
                        pos = int(rank[1])
                        if not p[0] in present:
                            present.append(p[0])
                            ticks.append({"id": p[0], "name": p[1], "years":[year], "position": [pos]})
                        else:
                            m = 0
                            while m < len(ticks):
                                if p[0] == ticks[m]["id"]:
                                    if not year in ticks[m]["years"]:
                                        ticks[m]["years"].append(year)
                                        ticks[m]["position"].append(pos)
                                    else:
                                        x = 0
                                        while x < len(ticks[m]["years"]):
                                            if p[0] == ticks[m]["id"]:
                                                if year == ticks[m]["years"][x]:
                                                    if pos < ticks[m]["position"][x]:
                                                        ticks[m]["position"][x] = pos
                                                        #print(ticks[m])
                                            x = x+1
                                m = m+1
        rankings_file.close()


    with open("../../data/tennis_atp/atp_rankings_current.csv", "r", encoding="utf8") as rankings_file:
        first_line = next(rankings_file)
        first_line = first_line.split(",")

        for line in rankings_file:
            rank = line.split(",")
            for p in players:
                if rank[2] == p[0]:
                    year = int(rank[0][:4])
                    pos = int(rank[1])
                    if not p[0] in present:
                        present.append(p[0])
                        ticks.append({"id": p[0], "name": p[1], "years":[year], "position": [pos]})
                    else:
                        m = 0
                        while m < len(ticks):
                            if p[0] == ticks[m]["id"]:
                                if not year in ticks[m]["years"]:
                                    ticks[m]["years"].append(year)
                                    ticks[m]["position"].append(pos)
                                else:
                                    x = 0
                                    while x < len(ticks[m]["years"]):
                                        if p[0] == ticks[m]["id"]:
                                            if year == ticks[m]["years"][x]:
                                                if pos < ticks[m]["position"][x]:
                                                    ticks[m]["position"][x] = pos
                                                    #print(ticks[m])
                                        x = x+1
                            m = m+1
        rankings_file.close()

        #print(ticks)
        rankings_file.close()


    with open("../../data/preprocessed/line/atp_rankings_trend_"+ str(j) +".csv",'w', newline='', encoding="utf8") as output:
        writer = csv.writer(output, delimiter=",")
        writer_header = csv.DictWriter(output, fieldnames=["id", "name", "year", "position"])
        writer_header.writeheader()

        for t in ticks:
            writer.writerow([t["id"], t["name"], t["years"], t["position"]])


    players.clear()
    present.clear()
    ticks.clear()




#WTA All-time
players_file_wta = "../../data/preprocessed/bar/wta_grandSlams_all.csv"
database_file_wta = "../../data/preprocessed/line/wta_grandSlams_all.csv"

#Sort the origin file
db = pd.read_csv(players_file_wta, skip_blank_lines=True, names=['id','name','grandSlamFinals','grandSlamTitles', 'list'], header=0)
db.drop_duplicates(inplace=True)
db.sort_values(by=['grandSlamTitles'], ascending=False).to_csv(database_file_wta, index=False)

#Pick only the needed players
with open(database_file_wta, "r", encoding="utf8") as players_file: #player[0] = id, player[1] = name, player[2] = finals, player[3] = titles, player[4] = list
    first_line = next(players_file)
    first_line = first_line.split(",")

    i = 0
    for line in players_file:
        if i < 10:
            player = line.split(",")
            players.append(player)
        i = i+1

    print(players)
    players_file.close()

found = []
ranking = []
present = []
ticks = []
years = ["80", "90", "00", "10", "20"]
for i in years:
    with open("../../data/tennis_wta/wta_rankings_" + i + "s.csv", "r", encoding="utf8") as rankings_file:
        first_line = next(rankings_file)
        first_line = first_line.split(",")

        for line in rankings_file:
            rank = line.split(",")
            for p in players:
                if rank[2] == p[0]:
                    year = int(rank[0][:4])
                    pos = int(rank[1])
                    if not p[0] in present:
                        present.append(p[0])
                        ticks.append({"id": p[0], "name": p[1], "years":[year], "position": [pos]})
                    else:
                        m = 0
                        while m < len(ticks):
                            if p[0] == ticks[m]["id"]:
                                if not year in ticks[m]["years"]:
                                    ticks[m]["years"].append(year)
                                    ticks[m]["position"].append(pos)
                                else:
                                    x = 0
                                    while x < len(ticks[m]["years"]):
                                        if p[0] == ticks[m]["id"]:
                                            if year == ticks[m]["years"][x]:
                                                if pos < ticks[m]["position"][x]:
                                                    ticks[m]["position"][x] = pos
                                                    #print(ticks[m])
                                        x = x+1
                            m = m+1
    rankings_file.close()

with open("../../data/tennis_wta/wta_rankings_current.csv", "r", encoding="utf8") as rankings_file:
    first_line = next(rankings_file)
    first_line = first_line.split(",")

    for line in rankings_file:
        rank = line.split(",")
        for p in players:
            if rank[2] == p[0]:
                year = int(rank[0][:4])
                pos = int(rank[1])
                if not p[0] in present:
                    present.append(p[0])
                    ticks.append({"id": p[0], "name": p[1], "years":[year], "position": [pos]})
                else:
                    m = 0
                    while m < len(ticks):
                        if p[0] == ticks[m]["id"]:
                            if not year in ticks[m]["years"]:
                                ticks[m]["years"].append(year)
                                ticks[m]["position"].append(pos)
                            else:
                                x = 0
                                while x < len(ticks[m]["years"]):
                                    if p[0] == ticks[m]["id"]:
                                        if year == ticks[m]["years"][x]:
                                            if pos < ticks[m]["position"][x]:
                                                ticks[m]["position"][x] = pos
                                                #print(ticks[m])
                                    x = x+1
                        m = m+1
    rankings_file.close()

with open("../../data/preprocessed/line/wta_rankings_trend_all.csv",'w', newline='', encoding="utf8") as output:
    writer = csv.writer(output, delimiter=",")
    writer_header = csv.DictWriter(output, fieldnames=["id", "name", "year", "position"])
    writer_header.writeheader()

    for t in ticks:
        writer.writerow([t["id"], t["name"], t["years"], t["position"]])

    ranking.clear()
    found.clear()
    players.clear()
    present.clear()
    ticks.clear()


#WTA

for j in [1980, 1990, 2000, 2010, 2020, 2021]:
    players_file_wta = "../../data/preprocessed/bar/wta_grandSlams_"+ str(j) +".csv"
    database_file_wta = "../../data/preprocessed/line/wta_grandSlams_"+ str(j) +".csv"

    #Sort the origin file
    db = pd.read_csv(players_file_wta, skip_blank_lines=True, names=['id','name','grandSlamFinals','grandSlamTitles', 'list'], header=0)
    db.drop_duplicates(inplace=True)
    db.sort_values(by=['grandSlamTitles'], ascending=False).to_csv(database_file_wta, index=False)

    #Pick only the needed players
    with open(database_file_wta, "r", encoding="utf8") as players_file: #player[0] = id, player[1] = name, player[2] = finals, player[3] = titles, player[4] = list
        first_line = next(players_file)
        first_line = first_line.split(",")

        i = 0
        for line in players_file:
            if i < 10:
                player = line.split(",")
                players.append(player)
            i = i+1

        print(players)
        players_file.close()

    found = []
    ranking = []
    present = []
    ticks = []
    years = ["80", "90", "00", "10", "20"]
    for i in years:
        with open("../../data/tennis_wta/wta_rankings_" + i + "s.csv", "r", encoding="utf8") as rankings_file:
            first_line = next(rankings_file)
            first_line = first_line.split(",")

            for line in rankings_file:
                rank = line.split(",")
                for p in players:
                    if rank[2] == p[0]:
                        year = int(rank[0][:4])
                        pos = int(rank[1])
                        if not p[0] in present:
                            present.append(p[0])
                            ticks.append({"id": p[0], "name": p[1], "years":[year], "position": [pos]})
                        else:
                            m = 0
                            while m < len(ticks):
                                if p[0] == ticks[m]["id"]:
                                    if not year in ticks[m]["years"]:
                                        ticks[m]["years"].append(year)
                                        ticks[m]["position"].append(pos)
                                    else:
                                        x = 0
                                        while x < len(ticks[m]["years"]):
                                            if p[0] == ticks[m]["id"]:
                                                if year == ticks[m]["years"][x]:
                                                    if pos < ticks[m]["position"][x]:
                                                        ticks[m]["position"][x] = pos
                                                        #print(ticks[m])
                                            x = x+1
                                m = m+1
        rankings_file.close()

    with open("../../data/tennis_wta/wta_rankings_current.csv", "r", encoding="utf8") as rankings_file:
        first_line = next(rankings_file)
        first_line = first_line.split(",")

        for line in rankings_file:
            rank = line.split(",")
            for p in players:
                if rank[2] == p[0]:
                    year = int(rank[0][:4])
                    pos = int(rank[1])
                    if not p[0] in present:
                        present.append(p[0])
                        ticks.append({"id": p[0], "name": p[1], "years":[year], "position": [pos]})
                    else:
                        m = 0
                        while m < len(ticks):
                            if p[0] == ticks[m]["id"]:
                                if not year in ticks[m]["years"]:
                                    ticks[m]["years"].append(year)
                                    ticks[m]["position"].append(pos)
                                else:
                                    x = 0
                                    while x < len(ticks[m]["years"]):
                                        if p[0] == ticks[m]["id"]:
                                            if year == ticks[m]["years"][x]:
                                                if pos < ticks[m]["position"][x]:
                                                    ticks[m]["position"][x] = pos
                                                    #print(ticks[m])
                                        x = x+1
                            m = m+1
        rankings_file.close()

    with open("../../data/preprocessed/line/wta_rankings_trend_"+ str(j) +".csv",'w', newline='', encoding="utf8") as output:
        writer = csv.writer(output, delimiter=",")
        writer_header = csv.DictWriter(output, fieldnames=["id", "name", "year", "position"])
        writer_header.writeheader()

        for t in ticks:
            writer.writerow([t["id"], t["name"], t["years"], t["position"]])

        ranking.clear()
        found.clear()
        players.clear()
        present.clear()
        ticks.clear()
