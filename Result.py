import pandas as pd
get_info=input()

fails = pd.read_excel("PersonalData.xlsx", sheet_name="Sheet1")
info_list = fails.values.tolist()

print("Ierakstiet pilsētas nosaukumu:", get_info)
city = None
city_count = 0
total_age = 0

for x in range(len(info_list)):
    city=info_list[x][0].lower()
    if city == get_info.lower():
        city_count += 1
        total_age += info_list[x][3]

if city_count == 0:
    print(f"Pilsētas nosaukums '{get_info}' nav atrasts")
    exit()

zcode = "0"
region=[]
region_age = 0

with open("ZipCodes.csv","r") as f:
    next(f)
    for line in f:
        row=line.rstrip().split(",")
        if row[3].strip().lower()==get_info.lower():
            zcode = row[0]

if zcode != "0":
    average_age = total_age / city_count if city_count > 0 else 0
    print(f"Zip kods: {zcode}")
    print(f"Cilvēku skaits no '{get_info}': {city_count}")
    print(f"Vidējais vecums: {average_age:.2f}")
else:
    print(f"Zip kods nav atrasts")