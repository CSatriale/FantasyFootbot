import csv 
import json 
import decimal

jsonFilePath = 'players.json'
data = {}

with open('FantasyPros_2020_Overall_ADP_Rankings.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        id = row[0]  
        data[id] = row

with open(jsonFilePath, 'w') as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))

f = open('players.json',)
data = json.load(f)

first = ['1','24','25','48','49','72','73','96','97']
second = ['2','23','26','47','50','71','74','95','98']
third = ['3','22','27','46','51','70','75','94','99']
fourth = ['4','21','28','45','52','69','76','93','100']
fifth = ['5','20','29','44','53','68','77','92','101']
sixth = ['6','19','30','43','54','67','78','91','102']
seventh = ['7','18','31','42','55','66','79','90','103']
eighth = ['8','17','32','41','56','65','80','89','104']
ninth = ['9','16','33','40','57','64','81','88','105']
tenth = ['10','15','34','39','58','63','82','87','106']
eleventh = ['11','14','35','38','59','62','83','86','107']
twelfth = ['12','13','36','37','60','61','84','85','108']


i = 0
#pickNumber = [firstPick, secondPick, thirdPick, fourthPick, fifthPick, sixthPick, seventhPick, eighthPick, ninthPick, tenthPick, eleventhPick, twelfthPick
totalPoints = []
pickNumber = second
for i in range(9):
    print(data[pickNumber[i]][1])
    totalPoints.append(data[pickNumber[i]][2])

print(sum(decimal.Decimal(x) for x in totalPoints))
