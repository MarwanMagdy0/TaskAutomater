from Archived.Event_based_system.mouse_keyboard import double_click_mouse, click_mouse, type_text, press_key
from Archived.Event_based_system.capture_detect import screen_template_match
from utiles import NumbersManager
import pyautogui
from Archived.Event_based_system.fake_data import random_email
import time, re
bolivia = """
IMS SMS | My SMS Numbers

Range	Prefix	Number	My Payterm	My Payout	Limits
Mauritania Chinguitel TF04		22224673008	Weekly	$ 0	SD : 0 | SW : 0
Mauritania Chinguitel TF04		22221145467	Weekly	$ 0	SD : 0 | SW : 0
Mauritania Chinguitel TF04		22227558092	Weekly	$ 0	SD : 0 | SW : 0
Mauritania Chinguitel TF04		22223162433	Weekly	$ 0	SD : 0 | SW : 0
Mauritania Chinguitel TF04		22225747437	Weekly	$ 0	SD : 0 | SW : 0
Mauritania Chinguitel TF04		22225816409	Weekly	$ 0	SD : 0 | SW : 0
Mauritania Chinguitel TF04		22229409448	Weekly	$ 0	SD : 0 | SW : 0
Mauritania Chinguitel TF04		22220208034	Weekly	$ 0	SD : 0 | SW : 0
Mauritania Chinguitel TF04		22224022818	Weekly	$ 0	SD : 0 | SW : 0
Mauritania Chinguitel TF04		22221880236	Weekly	$ 0	SD : 0 | SW : 0
Mauritania Chinguitel TF04		22226568901	Weekly	$ 0	SD : 0 | SW : 0
Mauritania Chinguitel TF04		22221572626	Weekly	$ 0	SD : 0 | SW : 0
Mauritania Chinguitel TF04		22222478998	Weekly	$ 0	SD : 0 | SW : 0
Mauritania Chinguitel TF04		22224686782	Weekly	$ 0	SD : 0 | SW : 0
Mauritania Chinguitel TF04		22223582522	Weekly	$ 0	SD : 0 | SW : 0
Mauritania Chinguitel TF04		22225107825	Weekly	$ 0	SD : 0 | SW : 0
Mauritania Chinguitel TF04		22224462401	Weekly	$ 0	SD : 0 | SW : 0
Mauritania Chinguitel TF04		22225820860	Weekly	$ 0	SD : 0 | SW : 0
Mauritania Chinguitel TF04		22221904510	Weekly	$ 0	SD : 0 | SW : 0
Mauritania Chinguitel TF04		22227066195	Weekly	$ 0	SD : 0 | SW : 0
Mauritania Chinguitel TF04		22224731728	Weekly	$ 0	SD : 0 | SW : 0
Mauritania Chinguitel TF04		22223117400	Weekly	$ 0	SD : 0 | SW : 0
Mauritania Chinguitel TF04		22224633103	Weekly	$ 0	SD : 0 | SW : 0
Mauritania Chinguitel TF04		22225408645	Weekly	$ 0	SD : 0 | SW : 0
Mauritania Chinguitel TF04		22229753297	Weekly	$ 0	SD : 0 | SW : 0
"""

Indonesia= """ 
IMS SMS | My SMS Numbers

Range	Prefix	Number	My Payterm	My Payout	Limits
Indonesia Smart TF01		6288227620674	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF01		6288135657484	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF01		6288201057559	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF01		6288161744312	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF01		6288102926188	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF01		6288163011917	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF01		6288227654457	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF01		6288281023952	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF01		6288118758821	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF01		6288135657473	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF01		6288245188903	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF01		6288124939210	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF01		6288110217811	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF01		6288140118391	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF01		6288251195999	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF01		6288218096749	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF01		6288252263389	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF01		6288224145177	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF01		6288106158204	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF01		6288124810920	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF01		6288125566618	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF01		6288222185075	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF01		6288133106722	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF01		6288229914042	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF01		6288164657955	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF54		6288740174849	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF54		6288198112502	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF54		6288844515447	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF54		6288758214616	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF54		6288141349237	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF54		6288834618676	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF54		6288118795755	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF54		6288775424820	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF54		6288257723857	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF54		6288844584983	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF54		6288133051811	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF54		6288269462848	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF54		6288216983074	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF54		6288874473842	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF54		6288724533089	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF54		6288770641224	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF54		6288125579251	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF54		6288292633525	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF54		6288285764606	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF54		6288112281909	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF54		6288882064551	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF54		6288193897243	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF54		6288180896794	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF54		6288240746720	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF54		6288773646711	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF59		6288271125462	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF59		6288277729510	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF59		6288148069282	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF59		6288108953409	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF59		6288735262514	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF59		6288753784836	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF59		6288249061457	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF59		6288217825363	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF59		6288174270998	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF59		6288175938989	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF59		6288232764725	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF59		6288704716277	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF59		6288124765322	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF59		6288889886127	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF59		6288216035091	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF59		6288146887231	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF59		6288165097201	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF59		6288242533665	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF59		6288259989022	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF59		6288722149257	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF59		6288821351866	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF59		6288735224326	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF59		6288119972624	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF59		6288827630917	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF59		6288726538220	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288867178243	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288146845760	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288192617686	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288774693268	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288773836993	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288129422935	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288890915492	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288252413448	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288206395423	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288879676262	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288857438523	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288768097603	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288124815526	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288787511414	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288181074391	Weekly	$ 0	SD : 0 | SW : 0
"""

moz = """
IMS SMS | My SMS Numbers

Range	Prefix	Number	My Payterm	My Payout	Limits
Senegal Tigo TF30		221768050312	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF30		221763232656	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF30		221764334670	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF30		221763533518	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF30		221767726773	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF30		221768436067	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF30		221764612340	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF30		221763606990	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF30		221765062304	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF30		221761092667	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF30		221766427367	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF30		221767266593	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF30		221763776142	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF30		221768123163	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF30		221766233556	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF30		221766297682	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF30		221767962868	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF30		221768142326	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF30		221766017546	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF30		221769306548	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF30		221761433016	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF30		221763994202	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF30		221764690663	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF30		221768331937	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF30		221764108591	Weekly	$ 0	SD : 0 | SW : 0
"""
leb = """
IMS SMS | My SMS Numbers

Range	Prefix	Number	My Payterm	My Payout	Limits
Lebanon Alfa TF01		96176661888	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF01		96181976818	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF01		96176623734	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF01		96176405958	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF01		96176372046	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF01		9613311541	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF01		9613398870	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF01		9613551007	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF01		96170444050	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF01		9613547963	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF01		96181127934	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF01		96170619119	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF01		96181564203	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF01		9613565745	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF01		96170303276	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF01		9613394393	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF01		9613544088	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF01		96170814780	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF01		9613592735	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF01		96176853696	Weekly	$ 0	SD : 0 | SW : 0
"""

pal = """
IMS SMS | My SMS Numbers

Range	Prefix	Number	My Payterm	My Payout	Limits
Palestine Jawwal GO21		972598237333	Weekly	$ 0	SD : 0 | SW : 0
Palestine Jawwal GO21		972595679573	Weekly	$ 0	SD : 0 | SW : 0
Palestine Jawwal GO21		972594006332	Weekly	$ 0	SD : 0 | SW : 0
Palestine Jawwal GO21		972596433891	Weekly	$ 0	SD : 0 | SW : 0
Palestine Jawwal GO21		972597810271	Weekly	$ 0	SD : 0 | SW : 0
Palestine Jawwal GO21		972598682984	Weekly	$ 0	SD : 0 | SW : 0
Palestine Jawwal GO21		972598972604	Weekly	$ 0	SD : 0 | SW : 0
Palestine Jawwal GO21		972596087513	Weekly	$ 0	SD : 0 | SW : 0
Palestine Jawwal GO21		972598847887	Weekly	$ 0	SD : 0 | SW : 0
Palestine Jawwal GO21		972593486008	Weekly	$ 0	SD : 0 | SW : 0
Palestine Jawwal GO21		972597309609	Weekly	$ 0	SD : 0 | SW : 0
Palestine Jawwal GO21		972591667117	Weekly	$ 0	SD : 0 | SW : 0
Palestine Jawwal GO21		972598057478	Weekly	$ 0	SD : 0 | SW : 0
Palestine Jawwal GO21		972598802316	Weekly	$ 0	SD : 0 | SW : 0
Palestine Jawwal GO21		972592374936	Weekly	$ 0	SD : 0 | SW : 0
Palestine Jawwal GO21		972591683606	Weekly	$ 0	SD : 0 | SW : 0
Palestine Jawwal GO21		972594436602	Weekly	$ 0	SD : 0 | SW : 0
Palestine Jawwal GO21		972594613705	Weekly	$ 0	SD : 0 | SW : 0
Palestine Jawwal GO21		972597830646	Weekly	$ 0	SD : 0 | SW : 0
Palestine Jawwal GO21		972596817054	Weekly	$ 0	SD : 0 | SW : 0
"""



# find all numbers starting with 258 and remove the prefix
bol_numbers = [num[3:] for num in re.findall(r"\b222\d+\b", bolivia)]
Indonesia_numbers = [num[2:] for num in re.findall(r"\b62\d+\b", Indonesia)]
moz_numbers = [num[3:] for num in re.findall(r"\b221\d+\b", moz)]
pal_numbers = [num[3:] for num in re.findall(r"\b972\d+\b", pal)]
leb_numbers = [num[3:] for num in re.findall(r"\b961\d+\b", leb)]



sub = "ch_"
verify =        f"Archived/IMGS/hdfc/{sub}verify_mobile.png"
change_number = f"Archived/IMGS/hdfc/{sub}change_number.png"
number_input =  f"Archived/IMGS/hdfc/{sub}number_input.png"
for i, number in enumerate(bol_numbers):
    print(f"[{i}] {number}")
    ret, pos = screen_template_match(number_input)
    click_mouse(pos[0]-200, pos[1]+40)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press("delete")
    type_text("1")
    # time.sleep(5)
    click_mouse(pos[0]-200, pos[1]+40)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press("delete")
    type_text(str(number))
    # time.sleep(5)
    ret, pos = screen_template_match(verify)
    
    click_mouse(pos[0], pos[1])

    ret, pos = screen_template_match(change_number)
    click_mouse(pos[0], pos[1])

    time.sleep(0.5)

