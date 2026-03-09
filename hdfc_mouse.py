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
Indonesia Smart JV28		6288737941077	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart JV28		6288784776826	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart JV28		6288946830640	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart JV28		6288130210564	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart JV28		6288133140971	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart JV28		6288847335337	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart JV28		6288950623665	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart JV28		6288951538578	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart JV28		6288826786248	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart JV28		6288836074444	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart JV28		6288984480894	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart JV28		6288224794346	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart JV28		6288257678919	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart JV28		6288740140715	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart JV28		6288927851730	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart JV28		6288133162032	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart JV28		6288147882100	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart JV28		6288764830999	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart JV28		6288789869695	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart JV28		6288191491257	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart JV28		6288879348129	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart JV28		6288788265542	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart JV28		6288268099918	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart JV28		6288233885379	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart JV28		6288119561720	Weekly	$ 0	SD : 0 | SW : 0
"""

moz = """
IMS SMS | My SMS Numbers

Range	Prefix	Number	My Payterm	My Payout	Limits
Tajikistan Indigo TF06		992935708849	Weekly	$ 0	SD : 0 | SW : 0
Tajikistan Indigo TF06		992935708802	Weekly	$ 0	SD : 0 | SW : 0
Tajikistan Indigo TF06		992935709006	Weekly	$ 0	SD : 0 | SW : 0
Tajikistan Indigo TF06		992935708927	Weekly	$ 0	SD : 0 | SW : 0
Tajikistan Indigo TF06		992935708827	Weekly	$ 0	SD : 0 | SW : 0
Tajikistan Indigo TF06		992935708767	Weekly	$ 0	SD : 0 | SW : 0
Tajikistan Indigo TF06		992935708881	Weekly	$ 0	SD : 0 | SW : 0
Tajikistan Indigo TF06		992935708936	Weekly	$ 0	SD : 0 | SW : 0
Tajikistan Indigo TF06		992935709011	Weekly	$ 0	SD : 0 | SW : 0
Tajikistan Indigo TF06		992935708962	Weekly	$ 0	SD : 0 | SW : 0
Tajikistan Indigo TF06		992935708818	Weekly	$ 0	SD : 0 | SW : 0
Tajikistan Indigo TF06		992935708879	Weekly	$ 0	SD : 0 | SW : 0
Tajikistan Indigo TF06		992935708992	Weekly	$ 0	SD : 0 | SW : 0
Tajikistan Indigo TF06		992935708955	Weekly	$ 0	SD : 0 | SW : 0
Tajikistan Indigo TF06		992935708944	Weekly	$ 0	SD : 0 | SW : 0
Tajikistan Indigo TF06		992935708842	Weekly	$ 0	SD : 0 | SW : 0
Tajikistan Indigo TF06		992935709031	Weekly	$ 0	SD : 0 | SW : 0
Tajikistan Indigo TF06		992935708819	Weekly	$ 0	SD : 0 | SW : 0
Tajikistan Indigo TF06		992935708859	Weekly	$ 0	SD : 0 | SW : 0
Tajikistan Indigo TF06		992935708923	Weekly	$ 0	SD : 0 | SW : 0
Tajikistan Indigo TF06		992935708800	Weekly	$ 0	SD : 0 | SW : 0
Tajikistan Indigo TF06		992935708869	Weekly	$ 0	SD : 0 | SW : 0
Tajikistan Indigo TF06		992935708939	Weekly	$ 0	SD : 0 | SW : 0
Tajikistan Indigo TF06		992935708740	Weekly	$ 0	SD : 0 | SW : 0
Tajikistan Indigo TF06		992935708856	Weekly	$ 0	SD : 0 | SW : 0
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
Slovenia Ipko TF25		38651064247	Weekly	$ 0	SD : 0 | SW : 0
Slovenia Ipko TF25		38641233629	Weekly	$ 0	SD : 0 | SW : 0
Slovenia Ipko TF25		38641088144	Weekly	$ 0	SD : 0 | SW : 0
Slovenia Ipko TF25		38651198742	Weekly	$ 0	SD : 0 | SW : 0
Slovenia Ipko TF25		38641470801	Weekly	$ 0	SD : 0 | SW : 0
Slovenia Ipko TF25		38651921426	Weekly	$ 0	SD : 0 | SW : 0
Slovenia Ipko TF25		38641970336	Weekly	$ 0	SD : 0 | SW : 0
Slovenia Ipko TF25		38651737478	Weekly	$ 0	SD : 0 | SW : 0
Slovenia Ipko TF25		38641715578	Weekly	$ 0	SD : 0 | SW : 0
Slovenia Ipko TF25		38651039345	Weekly	$ 0	SD : 0 | SW : 0
Slovenia Ipko TF25		38651009205	Weekly	$ 0	SD : 0 | SW : 0
Slovenia Ipko TF25		38641141041	Weekly	$ 0	SD : 0 | SW : 0
Slovenia Ipko TF25		38641041578	Weekly	$ 0	SD : 0 | SW : 0
Slovenia Ipko TF25		38651767572	Weekly	$ 0	SD : 0 | SW : 0
Slovenia Ipko TF25		38641879484	Weekly	$ 0	SD : 0 | SW : 0
Slovenia Ipko TF25		38651561714	Weekly	$ 0	SD : 0 | SW : 0
Slovenia Ipko TF25		38651335240	Weekly	$ 0	SD : 0 | SW : 0
Slovenia Ipko TF25		38651229677	Weekly	$ 0	SD : 0 | SW : 0
Slovenia Ipko TF25		38651505262	Weekly	$ 0	SD : 0 | SW : 0
Slovenia Ipko TF25		38651706076	Weekly	$ 0	SD : 0 | SW : 0
Slovenia Ipko TF25		38651594805	Weekly	$ 0	SD : 0 | SW : 0
Slovenia Ipko TF25		38651009293	Weekly	$ 0	SD : 0 | SW : 0
Slovenia Ipko TF25		38641908653	Weekly	$ 0	SD : 0 | SW : 0
Slovenia Ipko TF25		38651025809	Weekly	$ 0	SD : 0 | SW : 0
Slovenia Ipko TF25		38641917882	Weekly	$ 0	SD : 0 | SW : 0
"""



# find all numbers starting with 258 and remove the prefix
bol_numbers = [num[3:] for num in re.findall(r"\b222\d+\b", bolivia)]
Indonesia_numbers = [num[2:] for num in re.findall(r"\b62\d+\b", Indonesia)]
moz_numbers = [num[3:] for num in re.findall(r"\b992\d+\b", moz)]
pal_numbers = [num[3:] for num in re.findall(r"\b386\d+\b", pal)]
leb_numbers = [num[3:] for num in re.findall(r"\b961\d+\b", leb)]



sub = "ch_"
verify =        f"Archived/IMGS/hdfc/{sub}verify_mobile.png"
change_number = f"Archived/IMGS/hdfc/{sub}change_number.png"
number_input =  f"Archived/IMGS/hdfc/{sub}number_input.png"
for i, number in enumerate(moz_numbers):
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

