import json, re


txt = """
IMS SMS | My SMS Numbers

Range	Prefix	Number	My Payterm	My Payout	Limits
Mozambique Tmcel TF47		258823421617	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258821985654	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258824747665	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258828185507	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258822864301	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258822880146	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258822393403	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258825472534	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258829845353	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258828890666	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258825854508	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258829131924	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258824496236	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258825632134	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258826328381	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258823017825	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258827291538	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258821727391	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258829130133	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258825436589	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258822575581	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258823560602	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258823572094	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258824735070	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258820131977	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258825498820	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258826516114	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258828929435	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258829338783	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258824977528	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258822425031	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258824166133	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258827810970	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258823142579	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258829439493	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258827345206	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258824622973	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258822975705	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258826365710	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258826498500	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258824292847	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258822790578	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258824591241	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258828950249	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258825794511	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258829822179	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258824068256	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258824366709	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258828924757	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258825272667	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258825766808	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258822568945	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258828310470	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258828687711	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258821897042	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258825589545	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258826665408	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258822896052	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258827992742	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258828181824	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258827946607	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258829691357	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258829368533	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258827582433	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258826093927	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258828490063	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258826242519	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258829777241	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258823597529	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258826648587	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258822073258	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258822255802	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258827247642	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258821170409	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258822465782	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258822917675	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258824484348	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258828415602	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258821946678	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258829637545	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258829667261	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258820125008	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258829142424	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258824453313	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258824026678	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258824010547	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258822716429	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258827567963	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258829318140	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258829559427	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258822421326	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258825856575	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258821131818	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258829546574	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258820385448	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258828081874	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258823533194	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258821363131	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258826231019	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258824995201	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258828395882	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258822911875	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258829516517	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258825571087	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258822539487	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258827164294	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258827158124	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258828573424	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258826845643	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258824012784	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258827322514	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258826783332	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258820423655	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258829989175	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258822048453	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258827457072	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258829523864	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258824987297	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258821017974	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258821990120	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258821341827	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258825138674	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258825894977	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258822237060	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258822186989	Weekly	$ 0	SD : 0 | SW : 0
"""


with open('numbers.json', 'r') as file:
    data = json.load(file)

# Print all keys in a for loop
i = 0
for key in data.keys():
    if key in txt:
        i += 1
        print(f"[{key}] Found")

print(f"Total found: {i}")
if True:
    numbers = re.findall(r'\b\d{4,}\b', txt)

    # Build the dictionary
    output = {number: {"is_working": True, "last_checked": 0} for number in numbers}

    # Save to JSON
    with open("mozambique_numbers.json", "w") as f:
        json.dump(output, f, indent=4)

    print(f"Saved {len(output)} numbers to mozambique_numbers.json")