import json, re


txt = """
IMS SMS | My SMS Numbers

Range	Prefix	Number	My Payterm	My Payout	Limits
Mozambique Tmcel TF47		258821315114	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258825614735	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258828910595	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258824165412	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258820932495	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258827584828	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258822749411	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258828391858	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258826546603	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258823929449	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258827237066	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258827090536	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258823164410	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258822686333	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258824066475	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258828062623	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258823011908	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258821060728	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258827677182	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258829293425	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258825863629	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258829429405	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258826389779	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258827669669	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258821483938	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258828771634	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258828340072	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258821871131	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258821659592	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258827287624	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258827637085	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258820182907	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258829891010	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258822032572	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258825037276	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258826867461	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258822397404	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258827645342	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258821168555	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258821844929	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258823717472	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258823860677	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258825126738	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258820895049	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258821132634	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258822292767	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258824085743	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258826466671	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258826038318	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258827448995	Weekly	$ 0	SD : 0 | SW : 0
"""


with open('numbers.json', 'r') as file:
    data = json.load(file)

# Print all keys in a for loop
i = 0
for key in data.keys():
    if key in txt:
        i += 1
        print(f"[{key}] Found")

print(f"Total found: {i} from {len(data)} keys.")
if True:
    numbers = re.findall(r'\b\d{4,}\b', txt)

    # Build the dictionary
    output = {number: {"is_working": True, "last_checked": 0} for number in numbers}

    # Save to JSON
    with open("mozambique_numbers.json", "w") as f:
        json.dump(output, f, indent=4)

    print(f"Saved {len(output)} numbers to mozambique_numbers.json")