from Archived.Event_based_system.mouse_keyboard import double_click_mouse, click_mouse, type_text, press_key
from Archived.Event_based_system.capture_detect import screen_template_match
from utiles import NumbersManager
import pyautogui
from Archived.Event_based_system.fake_data import random_email
import time, re
bolivia = """
IMS SMS | My SMS Numbers

Range	Prefix	Number	My Payterm	My Payout	Limits
Bolivia Viva TF07		59179351660	Weekly	$ 0	SD : 0 | SW : 0
Bolivia Viva TF07		59179351941	Weekly	$ 0	SD : 0 | SW : 0
Bolivia Viva TF07		59179351679	Weekly	$ 0	SD : 0 | SW : 0
Bolivia Viva TF07		59179351897	Weekly	$ 0	SD : 0 | SW : 0
Bolivia Viva TF07		59179351919	Weekly	$ 0	SD : 0 | SW : 0
Bolivia Viva TF07		59179351927	Weekly	$ 0	SD : 0 | SW : 0
Bolivia Viva TF07		59179351779	Weekly	$ 0	SD : 0 | SW : 0
Bolivia Viva TF07		59179351721	Weekly	$ 0	SD : 0 | SW : 0
Bolivia Viva TF07		59179351711	Weekly	$ 0	SD : 0 | SW : 0
Bolivia Viva TF07		59179351908	Weekly	$ 0	SD : 0 | SW : 0
Bolivia Viva TF07		59179351652	Weekly	$ 0	SD : 0 | SW : 0
Bolivia Viva TF07		59179351676	Weekly	$ 0	SD : 0 | SW : 0
Bolivia Viva TF07		59179351784	Weekly	$ 0	SD : 0 | SW : 0
Bolivia Viva TF07		59179351831	Weekly	$ 0	SD : 0 | SW : 0
Bolivia Viva TF07		59179351702	Weekly	$ 0	SD : 0 | SW : 0
Bolivia Viva TF07		59179351728	Weekly	$ 0	SD : 0 | SW : 0
Bolivia Viva TF07		59179351849	Weekly	$ 0	SD : 0 | SW : 0
Bolivia Viva TF07		59179352017	Weekly	$ 0	SD : 0 | SW : 0
Bolivia Viva TF07		59179351656	Weekly	$ 0	SD : 0 | SW : 0
Bolivia Viva TF07		59179351688	Weekly	$ 0	SD : 0 | SW : 0
Bolivia Viva TF07		59179351780	Weekly	$ 0	SD : 0 | SW : 0
Bolivia Viva TF07		59179351692	Weekly	$ 0	SD : 0 | SW : 0
Bolivia Viva TF07		59179351934	Weekly	$ 0	SD : 0 | SW : 0
Bolivia Viva TF07		59179351952	Weekly	$ 0	SD : 0 | SW : 0
Bolivia Viva TF07		59179351781	Weekly	$ 0	SD : 0 | SW : 0
"""

Indonesia= """ 
IMS SMS | My SMS Numbers

Range	Prefix	Number	My Payterm	My Payout	Limits
Indonesia Smart TF62		6288282964606	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288181035139	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288284778708	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288285732212	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288100693491	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288892580524	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288161794935	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288256734588	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288263423175	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288252032010	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288750264885	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288205686134	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288843536067	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288883299013	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288781759444	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288192638367	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288115524189	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288258310434	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288721962829	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288210354030	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288155020675	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288897956755	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288271890455	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288894172815	Weekly	$ 0	SD : 0 | SW : 0
Indonesia Smart TF62		6288272510889	Weekly	$ 0	SD : 0 | SW : 0
"""

moz = """
IMS SMS | My SMS Numbers

Range	Prefix	Number	My Payterm	My Payout	Limits
Burkina Faso Orange TF03		22675535348	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Orange TF03		22655901749	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Orange TF03		22676473286	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Orange TF03		22667394275	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Orange TF03		22676631089	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Orange TF03		22664782422	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Orange TF03		22654224213	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Orange TF03		22657431596	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Orange TF03		22675670570	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Orange TF03		22675993601	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Orange TF03		22675236534	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Orange TF03		22666708916	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Orange TF03		22676629944	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Orange TF03		22676309659	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Orange TF03		22655442339	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Orange TF03		22657894413	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Orange TF03		22665129509	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Orange TF03		22654815454	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Orange TF03		22655446346	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Orange TF03		22654117747	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Orange TF03		22654015883	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Orange TF03		22667937247	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Orange TF03		22676629941	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Orange TF03		22676604138	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Orange TF03		22677052352	Weekly	$ 0	SD : 0 | SW : 0
"""


# find all numbers starting with 258 and remove the prefix
bol_numbers = [num[3:] for num in re.findall(r"\b591\d+\b", bolivia)]
Indonesia_numbers = [num[2:] for num in re.findall(r"\b62\d+\b", Indonesia)]
moz_numbers = [num[3:] for num in re.findall(r"\b226\d+\b", moz)]


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

