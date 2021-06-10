import csv
import pandas as pd

grandSlamFinalists = list()
grandSlamFinals = list()


matches = list()

# ATP 2021
with open("../../data/tennis_atp/atp_matches_2021.csv", "r", encoding="utf8") as matches_file:
    first_line = next(matches_file)
    first_line = first_line.split(",")

    for line in matches_file:
        match = line.split(",")
        if match[1] == "Wimbledon" or match[1] == "Australian Open" or match[1] == "Roland Garros" or match[1] == "US Open":  #Grand Slams
            if match[25] == "F" :    # round value F means final
                matches.append([match[1], match[7], match[10], match[15], match[18]])
                print(matches)

    matches_file.close()

with open("../../data/preprocessed/bar/atp_grandSlams_2021.csv",'w', newline='', encoding="utf8") as output:
    writer = csv.writer(output, delimiter=",")
    writer_header = csv.DictWriter(output, fieldnames=["id", "name", "grandslamFinals", "grandSlamTitles", "list"])
    writer_header.writeheader()

    for m in matches:
        if not m[1] in grandSlamFinalists:      # matches[1] is the winner id, matches[2] is the winner name, matches[0] is the tournament name
            grandSlamFinalists.append(m[1])
            grandSlamFinals.append([m[1], m[2], 0, 0, ()])
        if m[1] in (y for x in grandSlamFinals for y in x):
            x = 0
            while x < len(grandSlamFinals):
                y = 0
                while y < len(grandSlamFinals[x]):
                    if grandSlamFinals[x][0] == m[1]:
                        grandSlamFinals[x][2] = int(grandSlamFinals[x][2])
                        grandSlamFinals[x][2] += 1
                        grandSlamFinals[x][3] = int(grandSlamFinals[x][3])
                        grandSlamFinals[x][3] += 1
                        grandSlamFinals[x][4] = list(grandSlamFinals[x][4])
                        grandSlamFinals[x][4].append(m[0])
                        grandSlamFinals[x][4] = tuple(grandSlamFinals[x][4])
                        break
                    y = y + 1
                x = x + 1
        if not m[3] in grandSlamFinalists:      # matches[3] is the loser id, matches[4] is the loser name, matches[0] is the tournament name
            grandSlamFinalists.append(m[3])
            grandSlamFinals.append([m[3], m[4], 0, 0, ()])
        if m[3] in (y for x in grandSlamFinals for y in x):
            x = 0
            while x < len(grandSlamFinals):
                y = 0
                while y < len(grandSlamFinals[x]):
                    if grandSlamFinals[x][0] == m[3]:
                        grandSlamFinals[x][2] = int(grandSlamFinals[x][2])
                        grandSlamFinals[x][2] += 1
                        break
                    y = y + 1
                x = x + 1

    for w in grandSlamFinals:
        writer.writerow([w[0], w[1], w[2], w[3], w[4]])
    print(grandSlamFinals)
    grandSlamFinals.clear()
    grandSlamFinalists.clear()
    matches.clear()


#ATP 2020/21
for i in range(2020, 2021):
    with open("../../data/tennis_atp/atp_matches_" + str(i) + ".csv", "r", encoding="utf8") as matches_file:
        first_line = next(matches_file)
        first_line = first_line.split(",")

        for line in matches_file:
            match = line.split(",")
            if match[1] == "Wimbledon" or match[1] == "Australian Open" or match[1] == "Roland Garros" or match[1] == "US Open":  #Grand Slams
                if match[25] == "F" :    # round value F means final
                    matches.append([match[1], match[7], match[10], match[15], match[18]])
                    print(matches)

        matches_file.close()

with open("../../data/preprocessed/bar/atp_grandSlams_2020.csv",'w', newline='', encoding="utf8") as output:
    writer = csv.writer(output, delimiter=",")
    writer_header = csv.DictWriter(output, fieldnames=["id", "name", "grandslamFinals", "grandSlamTitles", "list"])
    writer_header.writeheader()

    for m in matches:
        if not m[1] in grandSlamFinalists:      # matches[1] is the winner id, matches[2] is the winner name, matches[0] is the tournament name
            grandSlamFinalists.append(m[1])
            grandSlamFinals.append([m[1], m[2], 0, 0, ()])
        if m[1] in (y for x in grandSlamFinals for y in x):
            x = 0
            while x < len(grandSlamFinals):
                y = 0
                while y < len(grandSlamFinals[x]):
                    if grandSlamFinals[x][0] == m[1]:
                        grandSlamFinals[x][2] = int(grandSlamFinals[x][2])
                        grandSlamFinals[x][2] += 1
                        grandSlamFinals[x][3] = int(grandSlamFinals[x][3])
                        grandSlamFinals[x][3] += 1
                        grandSlamFinals[x][4] = list(grandSlamFinals[x][4])
                        grandSlamFinals[x][4].append(m[0])
                        grandSlamFinals[x][4] = tuple(grandSlamFinals[x][4])
                        break
                    y = y + 1
                x = x + 1
        if not m[3] in grandSlamFinalists:      # matches[3] is the loser id, matches[4] is the loser name, matches[0] is the tournament name
            grandSlamFinalists.append(m[3])
            grandSlamFinals.append([m[3], m[4], 0, 0, ()])
        if m[3] in (y for x in grandSlamFinals for y in x):
            x = 0
            while x < len(grandSlamFinals):
                y = 0
                while y < len(grandSlamFinals[x]):
                    if grandSlamFinals[x][0] == m[3]:
                        grandSlamFinals[x][2] = int(grandSlamFinals[x][2])
                        grandSlamFinals[x][2] += 1
                        break
                    y = y + 1
                x = x + 1

    for w in grandSlamFinals:
        writer.writerow([w[0], w[1], w[2], w[3], w[4]])
    print(grandSlamFinals)
    grandSlamFinals.clear()
    grandSlamFinalists.clear()
    matches.clear()


#ATP 2010/2019
for i in range(2010, 2019):
    with open("../../data/tennis_atp/atp_matches_" + str(i) + ".csv", "r", encoding="utf8") as matches_file:
        first_line = next(matches_file)
        first_line = first_line.split(",")

        for line in matches_file:
            match = line.split(",")
            if match[1] == "Wimbledon" or match[1] == "Australian Open" or match[1] == "Roland Garros" or match[1] == "US Open":  #Grand Slams
                if match[25] == "F" :    # round value F means final
                    matches.append([match[1], match[7], match[10], match[15], match[18]])
                    print(matches)

        matches_file.close()

with open("../../data/preprocessed/bar/atp_grandSlams_2010.csv",'w', newline='', encoding="utf8") as output:
    writer = csv.writer(output, delimiter=",")
    writer_header = csv.DictWriter(output, fieldnames=["id", "name", "grandslamFinals", "grandSlamTitles", "list"])
    writer_header.writeheader()

    for m in matches:
        if not m[1] in grandSlamFinalists:      # matches[1] is the winner id, matches[2] is the winner name, matches[0] is the tournament name
            grandSlamFinalists.append(m[1])
            grandSlamFinals.append([m[1], m[2], 0, 0, ()])
        if m[1] in (y for x in grandSlamFinals for y in x):
            x = 0
            while x < len(grandSlamFinals):
                y = 0
                while y < len(grandSlamFinals[x]):
                    if grandSlamFinals[x][0] == m[1]:
                        grandSlamFinals[x][2] = int(grandSlamFinals[x][2])
                        grandSlamFinals[x][2] += 1
                        grandSlamFinals[x][3] = int(grandSlamFinals[x][3])
                        grandSlamFinals[x][3] += 1
                        grandSlamFinals[x][4] = list(grandSlamFinals[x][4])
                        grandSlamFinals[x][4].append(m[0])
                        grandSlamFinals[x][4] = tuple(grandSlamFinals[x][4])
                        break
                    y = y + 1
                x = x + 1
        if not m[3] in grandSlamFinalists:      # matches[3] is the loser id, matches[4] is the loser name, matches[0] is the tournament name
            grandSlamFinalists.append(m[3])
            grandSlamFinals.append([m[3], m[4], 0, 0, ()])
        if m[3] in (y for x in grandSlamFinals for y in x):
            x = 0
            while x < len(grandSlamFinals):
                y = 0
                while y < len(grandSlamFinals[x]):
                    if grandSlamFinals[x][0] == m[3]:
                        grandSlamFinals[x][2] = int(grandSlamFinals[x][2])
                        grandSlamFinals[x][2] += 1
                        break
                    y = y + 1
                x = x + 1

    for w in grandSlamFinals:
        writer.writerow([w[0], w[1], w[2], w[3], w[4]])
    print(grandSlamFinals)
    grandSlamFinals.clear()
    grandSlamFinalists.clear()
    matches.clear()


#ATP 2000/2009
for i in range(2000, 2009):
    with open("../../data/tennis_atp/atp_matches_" + str(i) + ".csv", "r", encoding="utf8") as matches_file:
        first_line = next(matches_file)
        first_line = first_line.split(",")

        for line in matches_file:
            match = line.split(",")
            if match[1] == "Wimbledon" or match[1] == "Australian Open" or match[1] == "Roland Garros" or match[1] == "US Open":  #Grand Slams
                if match[25] == "F" :    # round value F means final
                    matches.append([match[1], match[7], match[10], match[15], match[18]])
                    print(matches)

        matches_file.close()

with open("../../data/preprocessed/bar/atp_grandSlams_2000.csv",'w', newline='', encoding="utf8") as output:
    writer = csv.writer(output, delimiter=",")
    writer_header = csv.DictWriter(output, fieldnames=["id", "name", "grandslamFinals", "grandSlamTitles", "list"])
    writer_header.writeheader()

    for m in matches:
        if not m[1] in grandSlamFinalists:      # matches[1] is the winner id, matches[2] is the winner name, matches[0] is the tournament name
            grandSlamFinalists.append(m[1])
            grandSlamFinals.append([m[1], m[2], 0, 0, ()])
        if m[1] in (y for x in grandSlamFinals for y in x):
            x = 0
            while x < len(grandSlamFinals):
                y = 0
                while y < len(grandSlamFinals[x]):
                    if grandSlamFinals[x][0] == m[1]:
                        grandSlamFinals[x][2] = int(grandSlamFinals[x][2])
                        grandSlamFinals[x][2] += 1
                        grandSlamFinals[x][3] = int(grandSlamFinals[x][3])
                        grandSlamFinals[x][3] += 1
                        grandSlamFinals[x][4] = list(grandSlamFinals[x][4])
                        grandSlamFinals[x][4].append(m[0])
                        grandSlamFinals[x][4] = tuple(grandSlamFinals[x][4])
                        break
                    y = y + 1
                x = x + 1
        if not m[3] in grandSlamFinalists:      # matches[3] is the loser id, matches[4] is the loser name, matches[0] is the tournament name
            grandSlamFinalists.append(m[3])
            grandSlamFinals.append([m[3], m[4], 0, 0, ()])
        if m[3] in (y for x in grandSlamFinals for y in x):
            x = 0
            while x < len(grandSlamFinals):
                y = 0
                while y < len(grandSlamFinals[x]):
                    if grandSlamFinals[x][0] == m[3]:
                        grandSlamFinals[x][2] = int(grandSlamFinals[x][2])
                        grandSlamFinals[x][2] += 1
                        break
                    y = y + 1
                x = x + 1

    for w in grandSlamFinals:
        writer.writerow([w[0], w[1], w[2], w[3], w[4]])
    print(grandSlamFinals)
    grandSlamFinals.clear()
    grandSlamFinalists.clear()
    matches.clear()


#ATP 1990/1999
for i in range(1990, 1999):
    with open("../../data/tennis_atp/atp_matches_" + str(i) + ".csv", "r", encoding="utf8") as matches_file:
        first_line = next(matches_file)
        first_line = first_line.split(",")

        for line in matches_file:
            match = line.split(",")
            if match[1] == "Wimbledon" or match[1] == "Australian Open" or match[1] == "Roland Garros" or match[1] == "US Open":  #Grand Slams
                if match[25] == "F" :    # round value F means final
                    matches.append([match[1], match[7], match[10], match[15], match[18]])
                    print(matches)

        matches_file.close()

with open("../../data/preprocessed/bar/atp_grandSlams_1990.csv",'w', newline='', encoding="utf8") as output:
    writer = csv.writer(output, delimiter=",")
    writer_header = csv.DictWriter(output, fieldnames=["id", "name", "grandslamFinals", "grandSlamTitles", "list"])
    writer_header.writeheader()

    for m in matches:
        if not m[1] in grandSlamFinalists:      # matches[1] is the winner id, matches[2] is the winner name, matches[0] is the tournament name
            grandSlamFinalists.append(m[1])
            grandSlamFinals.append([m[1], m[2], 0, 0, ()])
        if m[1] in (y for x in grandSlamFinals for y in x):
            x = 0
            while x < len(grandSlamFinals):
                y = 0
                while y < len(grandSlamFinals[x]):
                    if grandSlamFinals[x][0] == m[1]:
                        grandSlamFinals[x][2] = int(grandSlamFinals[x][2])
                        grandSlamFinals[x][2] += 1
                        grandSlamFinals[x][3] = int(grandSlamFinals[x][3])
                        grandSlamFinals[x][3] += 1
                        grandSlamFinals[x][4] = list(grandSlamFinals[x][4])
                        grandSlamFinals[x][4].append(m[0])
                        grandSlamFinals[x][4] = tuple(grandSlamFinals[x][4])
                        break
                    y = y + 1
                x = x + 1
        if not m[3] in grandSlamFinalists:      # matches[3] is the loser id, matches[4] is the loser name, matches[0] is the tournament name
            grandSlamFinalists.append(m[3])
            grandSlamFinals.append([m[3], m[4], 0, 0, ()])
        if m[3] in (y for x in grandSlamFinals for y in x):
            x = 0
            while x < len(grandSlamFinals):
                y = 0
                while y < len(grandSlamFinals[x]):
                    if grandSlamFinals[x][0] == m[3]:
                        grandSlamFinals[x][2] = int(grandSlamFinals[x][2])
                        grandSlamFinals[x][2] += 1
                        break
                    y = y + 1
                x = x + 1

    for w in grandSlamFinals:
        writer.writerow([w[0], w[1], w[2], w[3], w[4]])
    print(grandSlamFinals)
    grandSlamFinals.clear()
    grandSlamFinalists.clear()
    matches.clear()


#ATP 1980/1989
for i in range(1980, 1989):
    with open("../../data/tennis_atp/atp_matches_" + str(i) + ".csv", "r", encoding="utf8") as matches_file:
        first_line = next(matches_file)
        first_line = first_line.split(",")

        for line in matches_file:
            match = line.split(",")
            if match[1] == "Wimbledon" or match[1] == "Australian Open" or match[1] == "Roland Garros" or match[1] == "US Open":  #Grand Slams
                if match[25] == "F" :    # round value F means final
                    matches.append([match[1], match[7], match[10], match[15], match[18]])
                    print(matches)

        matches_file.close()

with open("../../data/preprocessed/bar/atp_grandSlams_1980.csv",'w', newline='', encoding="utf8") as output:
    writer = csv.writer(output, delimiter=",")
    writer_header = csv.DictWriter(output, fieldnames=["id", "name", "grandslamFinals", "grandSlamTitles", "list"])
    writer_header.writeheader()

    for m in matches:
        if not m[1] in grandSlamFinalists:      # matches[1] is the winner id, matches[2] is the winner name, matches[0] is the tournament name
            grandSlamFinalists.append(m[1])
            grandSlamFinals.append([m[1], m[2], 0, 0, ()])
        if m[1] in (y for x in grandSlamFinals for y in x):
            x = 0
            while x < len(grandSlamFinals):
                y = 0
                while y < len(grandSlamFinals[x]):
                    if grandSlamFinals[x][0] == m[1]:
                        grandSlamFinals[x][2] = int(grandSlamFinals[x][2])
                        grandSlamFinals[x][2] += 1
                        grandSlamFinals[x][3] = int(grandSlamFinals[x][3])
                        grandSlamFinals[x][3] += 1
                        grandSlamFinals[x][4] = list(grandSlamFinals[x][4])
                        grandSlamFinals[x][4].append(m[0])
                        grandSlamFinals[x][4] = tuple(grandSlamFinals[x][4])
                        break
                    y = y + 1
                x = x + 1
        if not m[3] in grandSlamFinalists:      # matches[3] is the loser id, matches[4] is the loser name, matches[0] is the tournament name
            grandSlamFinalists.append(m[3])
            grandSlamFinals.append([m[3], m[4], 0, 0, ()])
        if m[3] in (y for x in grandSlamFinals for y in x):
            x = 0
            while x < len(grandSlamFinals):
                y = 0
                while y < len(grandSlamFinals[x]):
                    if grandSlamFinals[x][0] == m[3]:
                        grandSlamFinals[x][2] = int(grandSlamFinals[x][2])
                        grandSlamFinals[x][2] += 1
                        break
                    y = y + 1
                x = x + 1

    for w in grandSlamFinals:
        writer.writerow([w[0], w[1], w[2], w[3], w[4]])
    print(grandSlamFinals)
    grandSlamFinals.clear()
    grandSlamFinalists.clear()
    matches.clear()

#ATP All-time
for i in range(1980, 2021):
    with open("../../data/tennis_atp/atp_matches_" + str(i) + ".csv", "r", encoding="utf8") as matches_file:
        first_line = next(matches_file)
        first_line = first_line.split(",")

        for line in matches_file:
            match = line.split(",")
            if match[1] == "Wimbledon" or match[1] == "Australian Open" or match[1] == "Roland Garros" or match[1] == "US Open":  #Grand Slams
                if match[25] == "F" :    # round value F means final
                    matches.append([match[1], match[7], match[10], match[15], match[18]])
                    print(matches)

        matches_file.close()

with open("../../data/preprocessed/bar/atp_grandSlams_all.csv",'w', newline='', encoding="utf8") as output:
    writer = csv.writer(output, delimiter=",")
    writer_header = csv.DictWriter(output, fieldnames=["id", "name", "grandslamFinals", "grandSlamTitles", "list"])
    writer_header.writeheader()

    for m in matches:
        if not m[1] in grandSlamFinalists:      # matches[1] is the winner id, matches[2] is the winner name, matches[0] is the tournament name
            grandSlamFinalists.append(m[1])
            grandSlamFinals.append([m[1], m[2], 0, 0, ()])
        if m[1] in (y for x in grandSlamFinals for y in x):
            x = 0
            while x < len(grandSlamFinals):
                y = 0
                while y < len(grandSlamFinals[x]):
                    if grandSlamFinals[x][0] == m[1]:
                        grandSlamFinals[x][2] = int(grandSlamFinals[x][2])
                        grandSlamFinals[x][2] += 1
                        grandSlamFinals[x][3] = int(grandSlamFinals[x][3])
                        grandSlamFinals[x][3] += 1
                        grandSlamFinals[x][4] = list(grandSlamFinals[x][4])
                        grandSlamFinals[x][4].append(m[0])
                        grandSlamFinals[x][4] = tuple(grandSlamFinals[x][4])
                        break
                    y = y + 1
                x = x + 1
        if not m[3] in grandSlamFinalists:      # matches[3] is the loser id, matches[4] is the loser name, matches[0] is the tournament name
            grandSlamFinalists.append(m[3])
            grandSlamFinals.append([m[3], m[4], 0, 0, ()])
        if m[3] in (y for x in grandSlamFinals for y in x):
            x = 0
            while x < len(grandSlamFinals):
                y = 0
                while y < len(grandSlamFinals[x]):
                    if grandSlamFinals[x][0] == m[3]:
                        grandSlamFinals[x][2] = int(grandSlamFinals[x][2])
                        grandSlamFinals[x][2] += 1
                        break
                    y = y + 1
                x = x + 1

    for w in grandSlamFinals:
        writer.writerow([w[0], w[1], w[2], w[3], w[4]])
    print(grandSlamFinals)
    grandSlamFinals.clear()
    grandSlamFinalists.clear()
    matches.clear()


# WTA 2021
with open("../../data/tennis_wta/wta_matches_2021.csv", "r", encoding="utf8") as matches_file:
    first_line = next(matches_file)
    first_line = first_line.split(",")

    for line in matches_file:
        match = line.split(",")
        if match[1] == "Wimbledon" or match[1] == "Australian Open" or match[1] == "Roland Garros" or match[1] == "US Open":  #Grand Slams
            if match[25] == "F" :    # round value F means final
                matches.append([match[1], match[7], match[10], match[15], match[18]])
                print(matches)

    matches_file.close()

with open("../../data/preprocessed/bar/wta_grandSlams_2021.csv",'w', newline='', encoding="utf8") as output:
    writer = csv.writer(output, delimiter=",")
    writer_header = csv.DictWriter(output, fieldnames=["id", "name", "grandslamFinals", "grandSlamTitles", "list"])
    writer_header.writeheader()

    for m in matches:
        if not m[1] in grandSlamFinalists:      # matches[1] is the winner id, matches[2] is the winner name, matches[0] is the tournament name
            grandSlamFinalists.append(m[1])
            grandSlamFinals.append([m[1], m[2], 0, 0, ()])
        if m[1] in (y for x in grandSlamFinals for y in x):
            x = 0
            while x < len(grandSlamFinals):
                y = 0
                while y < len(grandSlamFinals[x]):
                    if grandSlamFinals[x][0] == m[1]:
                        grandSlamFinals[x][2] = int(grandSlamFinals[x][2])
                        grandSlamFinals[x][2] += 1
                        grandSlamFinals[x][3] = int(grandSlamFinals[x][3])
                        grandSlamFinals[x][3] += 1
                        grandSlamFinals[x][4] = list(grandSlamFinals[x][4])
                        grandSlamFinals[x][4].append(m[0])
                        grandSlamFinals[x][4] = tuple(grandSlamFinals[x][4])
                        break
                    y = y + 1
                x = x + 1
        if not m[3] in grandSlamFinalists:      # matches[3] is the loser id, matches[4] is the loser name, matches[0] is the tournament name
            grandSlamFinalists.append(m[3])
            grandSlamFinals.append([m[3], m[4], 0, 0, ()])
        if m[3] in (y for x in grandSlamFinals for y in x):
            x = 0
            while x < len(grandSlamFinals):
                y = 0
                while y < len(grandSlamFinals[x]):
                    if grandSlamFinals[x][0] == m[3]:
                        grandSlamFinals[x][2] = int(grandSlamFinals[x][2])
                        grandSlamFinals[x][2] += 1
                        break
                    y = y + 1
                x = x + 1

    for w in grandSlamFinals:
        writer.writerow([w[0], w[1], w[2], w[3], w[4]])
    print(grandSlamFinals)
    grandSlamFinals.clear()
    grandSlamFinalists.clear()
    matches.clear()


#WTA 2020/21
for i in range(2020, 2021):
    with open("../../data/tennis_wta/wta_matches_" + str(i) + ".csv", "r", encoding="utf8") as matches_file:
        first_line = next(matches_file)
        first_line = first_line.split(",")

        for line in matches_file:
            match = line.split(",")
            if match[1] == "Wimbledon" or match[1] == "Australian Open" or match[1] == "Roland Garros" or match[1] == "US Open":  #Grand Slams
                if match[25] == "F" :    # round value F means final
                    matches.append([match[1], match[7], match[10], match[15], match[18]])
                    print(matches)

        matches_file.close()

with open("../../data/preprocessed/bar/wta_grandSlams_2020.csv",'w', newline='', encoding="utf8") as output:
    writer = csv.writer(output, delimiter=",")
    writer_header = csv.DictWriter(output, fieldnames=["id", "name", "grandslamFinals", "grandSlamTitles", "list"])
    writer_header.writeheader()

    for m in matches:
        if not m[1] in grandSlamFinalists:      # matches[1] is the winner id, matches[2] is the winner name, matches[0] is the tournament name
            grandSlamFinalists.append(m[1])
            grandSlamFinals.append([m[1], m[2], 0, 0, ()])
        if m[1] in (y for x in grandSlamFinals for y in x):
            x = 0
            while x < len(grandSlamFinals):
                y = 0
                while y < len(grandSlamFinals[x]):
                    if grandSlamFinals[x][0] == m[1]:
                        grandSlamFinals[x][2] = int(grandSlamFinals[x][2])
                        grandSlamFinals[x][2] += 1
                        grandSlamFinals[x][3] = int(grandSlamFinals[x][3])
                        grandSlamFinals[x][3] += 1
                        grandSlamFinals[x][4] = list(grandSlamFinals[x][4])
                        grandSlamFinals[x][4].append(m[0])
                        grandSlamFinals[x][4] = tuple(grandSlamFinals[x][4])
                        break
                    y = y + 1
                x = x + 1
        if not m[3] in grandSlamFinalists:      # matches[3] is the loser id, matches[4] is the loser name, matches[0] is the tournament name
            grandSlamFinalists.append(m[3])
            grandSlamFinals.append([m[3], m[4], 0, 0, ()])
        if m[3] in (y for x in grandSlamFinals for y in x):
            x = 0
            while x < len(grandSlamFinals):
                y = 0
                while y < len(grandSlamFinals[x]):
                    if grandSlamFinals[x][0] == m[3]:
                        grandSlamFinals[x][2] = int(grandSlamFinals[x][2])
                        grandSlamFinals[x][2] += 1
                        break
                    y = y + 1
                x = x + 1

    for w in grandSlamFinals:
        writer.writerow([w[0], w[1], w[2], w[3], w[4]])
    print(grandSlamFinals)
    grandSlamFinals.clear()
    grandSlamFinalists.clear()
    matches.clear()


#WTA 2010/2019
for i in range(2010, 2019):
    with open("../../data/tennis_wta/wta_matches_" + str(i) + ".csv", "r", encoding="utf8") as matches_file:
        first_line = next(matches_file)
        first_line = first_line.split(",")

        for line in matches_file:
            match = line.split(",")
            if match[1] == "Wimbledon" or match[1] == "Australian Open" or match[1] == "Roland Garros" or match[1] == "US Open":  #Grand Slams
                if match[25] == "F" :    # round value F means final
                    matches.append([match[1], match[7], match[10], match[15], match[18]])
                    print(matches)

        matches_file.close()

with open("../../data/preprocessed/bar/wta_grandSlams_2010.csv",'w', newline='', encoding="utf8") as output:
    writer = csv.writer(output, delimiter=",")
    writer_header = csv.DictWriter(output, fieldnames=["id", "name", "grandslamFinals", "grandSlamTitles", "list"])
    writer_header.writeheader()

    for m in matches:
        if not m[1] in grandSlamFinalists:      # matches[1] is the winner id, matches[2] is the winner name, matches[0] is the tournament name
            grandSlamFinalists.append(m[1])
            grandSlamFinals.append([m[1], m[2], 0, 0, ()])
        if m[1] in (y for x in grandSlamFinals for y in x):
            x = 0
            while x < len(grandSlamFinals):
                y = 0
                while y < len(grandSlamFinals[x]):
                    if grandSlamFinals[x][0] == m[1]:
                        grandSlamFinals[x][2] = int(grandSlamFinals[x][2])
                        grandSlamFinals[x][2] += 1
                        grandSlamFinals[x][3] = int(grandSlamFinals[x][3])
                        grandSlamFinals[x][3] += 1
                        grandSlamFinals[x][4] = list(grandSlamFinals[x][4])
                        grandSlamFinals[x][4].append(m[0])
                        grandSlamFinals[x][4] = tuple(grandSlamFinals[x][4])
                        break
                    y = y + 1
                x = x + 1
        if not m[3] in grandSlamFinalists:      # matches[3] is the loser id, matches[4] is the loser name, matches[0] is the tournament name
            grandSlamFinalists.append(m[3])
            grandSlamFinals.append([m[3], m[4], 0, 0, ()])
        if m[3] in (y for x in grandSlamFinals for y in x):
            x = 0
            while x < len(grandSlamFinals):
                y = 0
                while y < len(grandSlamFinals[x]):
                    if grandSlamFinals[x][0] == m[3]:
                        grandSlamFinals[x][2] = int(grandSlamFinals[x][2])
                        grandSlamFinals[x][2] += 1
                        break
                    y = y + 1
                x = x + 1

    for w in grandSlamFinals:
        writer.writerow([w[0], w[1], w[2], w[3], w[4]])
    print(grandSlamFinals)
    grandSlamFinals.clear()
    grandSlamFinalists.clear()
    matches.clear()


#WTA 2000/2009
for i in range(2000, 2009):
    with open("../../data/tennis_wta/wta_matches_" + str(i) + ".csv", "r", encoding="utf8") as matches_file:
        first_line = next(matches_file)
        first_line = first_line.split(",")

        for line in matches_file:
            match = line.split(",")
            if match[1] == "Wimbledon" or match[1] == "Australian Open" or match[1] == "Roland Garros" or match[1] == "US Open":  #Grand Slams
                if match[25] == "F" :    # round value F means final
                    matches.append([match[1], match[7], match[10], match[15], match[18]])
                    print(matches)

        matches_file.close()

with open("../../data/preprocessed/bar/wta_grandSlams_2000.csv",'w', newline='', encoding="utf8") as output:
    writer = csv.writer(output, delimiter=",")
    writer_header = csv.DictWriter(output, fieldnames=["id", "name", "grandslamFinals", "grandSlamTitles", "list"])
    writer_header.writeheader()

    for m in matches:
        if not m[1] in grandSlamFinalists:      # matches[1] is the winner id, matches[2] is the winner name, matches[0] is the tournament name
            grandSlamFinalists.append(m[1])
            grandSlamFinals.append([m[1], m[2], 0, 0, ()])
        if m[1] in (y for x in grandSlamFinals for y in x):
            x = 0
            while x < len(grandSlamFinals):
                y = 0
                while y < len(grandSlamFinals[x]):
                    if grandSlamFinals[x][0] == m[1]:
                        grandSlamFinals[x][2] = int(grandSlamFinals[x][2])
                        grandSlamFinals[x][2] += 1
                        grandSlamFinals[x][3] = int(grandSlamFinals[x][3])
                        grandSlamFinals[x][3] += 1
                        grandSlamFinals[x][4] = list(grandSlamFinals[x][4])
                        grandSlamFinals[x][4].append(m[0])
                        grandSlamFinals[x][4] = tuple(grandSlamFinals[x][4])
                        break
                    y = y + 1
                x = x + 1
        if not m[3] in grandSlamFinalists:      # matches[3] is the loser id, matches[4] is the loser name, matches[0] is the tournament name
            grandSlamFinalists.append(m[3])
            grandSlamFinals.append([m[3], m[4], 0, 0, ()])
        if m[3] in (y for x in grandSlamFinals for y in x):
            x = 0
            while x < len(grandSlamFinals):
                y = 0
                while y < len(grandSlamFinals[x]):
                    if grandSlamFinals[x][0] == m[3]:
                        grandSlamFinals[x][2] = int(grandSlamFinals[x][2])
                        grandSlamFinals[x][2] += 1
                        break
                    y = y + 1
                x = x + 1

    for w in grandSlamFinals:
        writer.writerow([w[0], w[1], w[2], w[3], w[4]])
    print(grandSlamFinals)
    grandSlamFinals.clear()
    grandSlamFinalists.clear()
    matches.clear()


#WTA 1990/1999
for i in range(1990, 1999):
    with open("../../data/tennis_wta/wta_matches_" + str(i) + ".csv", "r", encoding="utf8") as matches_file:
        first_line = next(matches_file)
        first_line = first_line.split(",")

        for line in matches_file:
            match = line.split(",")
            if match[1] == "Wimbledon" or match[1] == "Australian Open" or match[1] == "Roland Garros" or match[1] == "US Open":  #Grand Slams
                if match[25] == "F" :    # round value F means final
                    matches.append([match[1], match[7], match[10], match[15], match[18]])
                    print(matches)

        matches_file.close()

with open("../../data/preprocessed/bar/wta_grandSlams_1990.csv",'w', newline='', encoding="utf8") as output:
    writer = csv.writer(output, delimiter=",")
    writer_header = csv.DictWriter(output, fieldnames=["id", "name", "grandslamFinals", "grandSlamTitles", "list"])
    writer_header.writeheader()

    for m in matches:
        if not m[1] in grandSlamFinalists:      # matches[1] is the winner id, matches[2] is the winner name, matches[0] is the tournament name
            grandSlamFinalists.append(m[1])
            grandSlamFinals.append([m[1], m[2], 0, 0, ()])
        if m[1] in (y for x in grandSlamFinals for y in x):
            x = 0
            while x < len(grandSlamFinals):
                y = 0
                while y < len(grandSlamFinals[x]):
                    if grandSlamFinals[x][0] == m[1]:
                        grandSlamFinals[x][2] = int(grandSlamFinals[x][2])
                        grandSlamFinals[x][2] += 1
                        grandSlamFinals[x][3] = int(grandSlamFinals[x][3])
                        grandSlamFinals[x][3] += 1
                        grandSlamFinals[x][4] = list(grandSlamFinals[x][4])
                        grandSlamFinals[x][4].append(m[0])
                        grandSlamFinals[x][4] = tuple(grandSlamFinals[x][4])
                        break
                    y = y + 1
                x = x + 1
        if not m[3] in grandSlamFinalists:      # matches[3] is the loser id, matches[4] is the loser name, matches[0] is the tournament name
            grandSlamFinalists.append(m[3])
            grandSlamFinals.append([m[3], m[4], 0, 0, ()])
        if m[3] in (y for x in grandSlamFinals for y in x):
            x = 0
            while x < len(grandSlamFinals):
                y = 0
                while y < len(grandSlamFinals[x]):
                    if grandSlamFinals[x][0] == m[3]:
                        grandSlamFinals[x][2] = int(grandSlamFinals[x][2])
                        grandSlamFinals[x][2] += 1
                        break
                    y = y + 1
                x = x + 1

    for w in grandSlamFinals:
        writer.writerow([w[0], w[1], w[2], w[3], w[4]])
    print(grandSlamFinals)
    grandSlamFinals.clear()
    grandSlamFinalists.clear()
    matches.clear()


#WTA 1980/1989
for i in range(1980, 1989):
    with open("../../data/tennis_wta/wta_matches_" + str(i) + ".csv", "r", encoding="utf8") as matches_file:
        first_line = next(matches_file)
        first_line = first_line.split(",")

        for line in matches_file:
            match = line.split(",")
            if match[1] == "Wimbledon" or match[1] == "Australian Open" or match[1] == "Roland Garros" or match[1] == "US Open":  #Grand Slams
                if match[25] == "F" :    # round value F means final
                    matches.append([match[1], match[7], match[10], match[15], match[18]])
                    print(matches)

        matches_file.close()

with open("../../data/preprocessed/bar/wta_grandSlams_1980.csv",'w', newline='', encoding="utf8") as output:
    writer = csv.writer(output, delimiter=",")
    writer_header = csv.DictWriter(output, fieldnames=["id", "name", "grandslamFinals", "grandSlamTitles", "list"])
    writer_header.writeheader()

    for m in matches:
        if not m[1] in grandSlamFinalists:      # matches[1] is the winner id, matches[2] is the winner name, matches[0] is the tournament name
            grandSlamFinalists.append(m[1])
            grandSlamFinals.append([m[1], m[2], 0, 0, ()])
        if m[1] in (y for x in grandSlamFinals for y in x):
            x = 0
            while x < len(grandSlamFinals):
                y = 0
                while y < len(grandSlamFinals[x]):
                    if grandSlamFinals[x][0] == m[1]:
                        grandSlamFinals[x][2] = int(grandSlamFinals[x][2])
                        grandSlamFinals[x][2] += 1
                        grandSlamFinals[x][3] = int(grandSlamFinals[x][3])
                        grandSlamFinals[x][3] += 1
                        grandSlamFinals[x][4] = list(grandSlamFinals[x][4])
                        grandSlamFinals[x][4].append(m[0])
                        grandSlamFinals[x][4] = tuple(grandSlamFinals[x][4])
                        break
                    y = y + 1
                x = x + 1
        if not m[3] in grandSlamFinalists:      # matches[3] is the loser id, matches[4] is the loser name, matches[0] is the tournament name
            grandSlamFinalists.append(m[3])
            grandSlamFinals.append([m[3], m[4], 0, 0, ()])
        if m[3] in (y for x in grandSlamFinals for y in x):
            x = 0
            while x < len(grandSlamFinals):
                y = 0
                while y < len(grandSlamFinals[x]):
                    if grandSlamFinals[x][0] == m[3]:
                        grandSlamFinals[x][2] = int(grandSlamFinals[x][2])
                        grandSlamFinals[x][2] += 1
                        break
                    y = y + 1
                x = x + 1

    for w in grandSlamFinals:
        writer.writerow([w[0], w[1], w[2], w[3], w[4]])
    print(grandSlamFinals)
    grandSlamFinals.clear()
    grandSlamFinalists.clear()
    matches.clear()


# WTA
for i in range(1980, 2021):
    with open("../../data/tennis_wta/wta_matches_" + str(i) + ".csv", "r", encoding="utf8") as matches_file:
        first_line = next(matches_file)
        first_line = first_line.split(",")

        for line in matches_file:
            match = line.split(",")
            if match[1] == "Wimbledon" or match[1] == "Australian Open" or match[1] == "Roland Garros" or match[1] == "US Open":   # draw_size value 128 means the tournament is a Grand Slam
                if match[25] == "F" :    # round value F means final
                    matches.append([match[1], match[7], match[10], match[15], match[18]])
                    print(matches)

        matches_file.close()

with open("../../data/preprocessed/bar/wta_grandSlams_all.csv",'w', newline='', encoding="utf8") as output:
    writer = csv.writer(output, delimiter=",")
    writer_header = csv.DictWriter(output, fieldnames=["id", "name", "grandslamFinals", "grandSlamTitles", "list"])
    writer_header.writeheader()

    for m in matches:
        if not m[1] in grandSlamFinalists:      # matches[1] is the winner id, matches[2] is the winner name, matches[0] is the tournament name
            grandSlamFinalists.append(m[1])
            grandSlamFinals.append([m[1], m[2], 0, 0, ()])
        if m[1] in (y for x in grandSlamFinals for y in x):
            x = 0
            while x < len(grandSlamFinals):
                y = 0
                while y < len(grandSlamFinals[x]):
                    if grandSlamFinals[x][0] == m[1]:
                        grandSlamFinals[x][2] = int(grandSlamFinals[x][2])
                        grandSlamFinals[x][2] += 1
                        grandSlamFinals[x][3] = int(grandSlamFinals[x][3])
                        grandSlamFinals[x][3] += 1
                        grandSlamFinals[x][4] = list(grandSlamFinals[x][4])
                        grandSlamFinals[x][4].append(m[0])
                        grandSlamFinals[x][4] = tuple(grandSlamFinals[x][4])
                        break
                    y = y + 1
                x = x + 1
        if not m[3] in grandSlamFinalists:      # matches[3] is the loser id, matches[4] is the loser name, matches[0] is the tournament name
            grandSlamFinalists.append(m[3])
            grandSlamFinals.append([m[3], m[4], 0, 0, ()])
        if m[3] in (y for x in grandSlamFinals for y in x):
            x = 0
            while x < len(grandSlamFinals):
                y = 0
                while y < len(grandSlamFinals[x]):
                    if grandSlamFinals[x][0] == m[3]:
                        grandSlamFinals[x][2] = int(grandSlamFinals[x][2])
                        grandSlamFinals[x][2] += 1
                        break
                    y = y + 1
                x = x + 1

    for w in grandSlamFinals:
        writer.writerow([w[0], w[1], w[2], w[3], w[4]])
    print(grandSlamFinals)
    grandSlamFinals.clear()
    grandSlamFinalists.clear()
    matches.clear()
