from Archived.Event_based_system.mouse_keyboard import double_click_mouse, click_mouse, type_text, press_key
from Archived.Event_based_system.capture_detect import screen_template_match
from utiles import NumbersManager
import pyautogui
from Archived.Event_based_system.fake_data import random_email
import time, re

moz = """
IMS SMS | My SMS Numbers

Range	Prefix	Number	My Payterm	My Payout	Limits
Mozambique Tmcel TF46		258823460497	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258828797237	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258823470654	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258826024887	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258824037963	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258824440385	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258824613185	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258828769825	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258823766804	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258826191932	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258829761450	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258820547820	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258825515559	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258820838729	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258825666883	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258822627602	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258829922338	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258829775798	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258820663441	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258822090581	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258820831434	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258825518959	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258826516475	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258821545361	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258821469049	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258821145092	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258821099620	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258824351295	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258829873505	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258822354650	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258823943932	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258823035209	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258821223075	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258826737657	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258825535924	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258827325549	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258826486691	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258823943052	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258829322005	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258821232041	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258823094646	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258822383034	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258827151226	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258829542726	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258826711357	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258825148783	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258827033467	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258823458187	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258827484215	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258825263137	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258827522205	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258829640767	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258825326688	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258826455237	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258824192180	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258828943740	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258827210338	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258827955285	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258822888814	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258829556366	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258823334981	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258827820893	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258829284855	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258825971879	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258824876021	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258826687384	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258821923437	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258825039182	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258824228766	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258827373643	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258825279112	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258825233446	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258828125927	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258828798442	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258821364786	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258823687444	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258821058853	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258821510675	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258823921757	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258821021653	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258829845058	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258822459765	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258821335080	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258827157925	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258827538401	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258829277475	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258822570621	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258820699157	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258826175060	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258826368112	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258822879796	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258828093103	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258824661251	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258828440137	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258824161640	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258829137109	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258826840012	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258827463779	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258821777676	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF46		258821723409	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258827778647	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258826021498	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258820659582	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258828168553	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258826517510	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258820812107	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258829081239	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258824142296	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258823968749	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258822228333	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258820374994	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258822542920	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258828595156	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258820747361	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258820171302	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258823030732	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258826839363	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258826490940	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258821442845	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258829745885	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258825259926	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258826898768	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258829211501	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258825097807	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258820759652	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258829415138	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258827773674	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258822580726	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258820236139	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258822716017	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258821731072	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258821226630	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258821738639	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258829030270	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258822599247	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258827810708	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258829728395	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258827517568	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258820950786	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258823926153	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258822026503	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258826419432	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258822711940	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258822743366	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258823493300	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258828894526	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258820662492	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258828577654	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258820082580	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258824333520	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258825385912	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258823745902	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258828363823	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258823734048	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258821695221	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258821516139	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258820561057	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258827274026	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258820586529	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258823983775	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258827279467	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258825636971	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258826835664	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258828371634	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258823824698	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258822225808	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258824298234	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258824064489	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258829226717	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258828543717	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258827928742	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258823422003	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258825889211	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258829067593	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258826994697	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258826570918	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258823617753	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258820355428	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258825434486	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258827361262	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258824982580	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258822417112	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258821091326	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258829838607	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258829747516	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258823937586	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258828416102	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258820721600	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258823770054	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258820884797	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258825478202	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258822216201	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258826518959	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258822390137	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258820441849	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258829250404	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258820853509	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258823230233	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258826216912	Weekly	$ 0	SD : 0 | SW : 0
Mozambique Tmcel TF47		258820280537	Weekly	$ 0	SD : 0 | SW : 0
"""

slov = """
    38651177654
    38651901120
    38651171308
    38651763446
    38651994406
    38651660263
    38651963339
    38651234643
    38651742016
    38651899543
    38651738025
    38651184334
    38651902204
    38651362315
    38651207541
    38651775546
    38651471021
    38651672644
    38651629227
    38651899574
    38651738093
    38651544797
    38651476992
    38651429882
    38651314635
"""

lebanon = """
IMS SMS | My SMS Numbers

Range	Prefix	Number	My Payterm	My Payout	Limits
Lebanon Alfa TF05		96181607903	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181640133	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181678829	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181666611	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181730597	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181729139	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181766135	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181685329	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181705249	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181758326	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181709780	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181611116	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181657785	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181785839	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181748532	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181693127	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181640005	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181625568	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181729205	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181733499	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181796482	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181775404	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181678841	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181766554	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181738064	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181668275	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181741895	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181757189	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181728095	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181688110	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181759869	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181658089	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181654845	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181611460	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181612980	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181604212	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181600705	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181635600	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181791760	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181785504	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181721708	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181727537	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181650533	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181777013	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181700373	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181621211	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181716956	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181795255	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181759999	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181625534	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181657789	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181716902	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181643487	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181764681	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181703698	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181671335	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181654728	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181685323	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181656284	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181646485	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181646384	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181709769	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181758142	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181680386	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181759880	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181647110	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181764312	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181758056	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181612929	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181796846	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181756761	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181746338	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181604240	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181657136	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181791721	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181758273	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181797355	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181791775	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181795234	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181634154	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181647199	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181682465	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181711093	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181757154	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181682996	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181785849	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181753675	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181668952	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181796442	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181656465	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181775388	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181753609	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181680321	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181741805	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181729254	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181601836	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181796897	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181770582	Weekly	$ 0	SD : 0 | SW : 0
Lebanon Alfa TF05		96181657181	Weekly	$ 0	SD : 0 | SW : 0
"""

Senegal = """
IMS SMS | My SMS Numbers

Range	Prefix	Number	My Payterm	My Payout	Limits
Senegal Tigo TF84		221765117260	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF84		221762357580	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF84		221767841815	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF84		221764897106	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF84		221765034518	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF84		221767815580	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF84		221768840312	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF84		221764077670	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF84		221769228672	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF84		221769545774	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF84		221763470771	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF84		221761646726	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF84		221764323559	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF84		221765378829	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF84		221768082935	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF84		221767834616	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF84		221763359247	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF84		221768782821	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF84		221766354615	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF84		221766865315	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF84		221762320887	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF84		221765651933	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF84		221767585564	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF84		221767736484	Weekly	$ 0	SD : 0 | SW : 0
Senegal Tigo TF84		221763415407	Weekly	$ 0	SD : 0 | SW : 0
"""

tan_num = """
IMS SMS | My SMS Numbers

Range	Prefix	Number	My Payterm	My Payout	Limits
Tanzania Zantel TO122		255658680579	Weekly	$ 0	SD : 0 | SW : 0
Tanzania Zantel TO122		255679262625	Weekly	$ 0	SD : 0 | SW : 0
Tanzania Zantel TO122		255774573889	Weekly	$ 0	SD : 0 | SW : 0
Tanzania Zantel TO122		255714077520	Weekly	$ 0	SD : 0 | SW : 0
Tanzania Zantel TO122		255653095430	Weekly	$ 0	SD : 0 | SW : 0
Tanzania Zantel TO122		255774405242	Weekly	$ 0	SD : 0 | SW : 0
Tanzania Zantel TO122		255778076551	Weekly	$ 0	SD : 0 | SW : 0
Tanzania Zantel TO122		255716026870	Weekly	$ 0	SD : 0 | SW : 0
Tanzania Zantel TO122		255678187008	Weekly	$ 0	SD : 0 | SW : 0
Tanzania Zantel TO122		255659285311	Weekly	$ 0	SD : 0 | SW : 0
Tanzania Zantel TO122		255676226646	Weekly	$ 0	SD : 0 | SW : 0
Tanzania Zantel TO122		255677101934	Weekly	$ 0	SD : 0 | SW : 0
Tanzania Zantel TO122		255659606779	Weekly	$ 0	SD : 0 | SW : 0
Tanzania Zantel TO122		255714892886	Weekly	$ 0	SD : 0 | SW : 0
Tanzania Zantel TO122		255717522217	Weekly	$ 0	SD : 0 | SW : 0
Tanzania Zantel TO122		255655439756	Weekly	$ 0	SD : 0 | SW : 0
Tanzania Zantel TO122		255654235620	Weekly	$ 0	SD : 0 | SW : 0
Tanzania Zantel TO122		255653573696	Weekly	$ 0	SD : 0 | SW : 0
Tanzania Zantel TO122		255672241506	Weekly	$ 0	SD : 0 | SW : 0
Tanzania Zantel TO122		255677984013	Weekly	$ 0	SD : 0 | SW : 0
Tanzania Zantel TO122		255777705477	Weekly	$ 0	SD : 0 | SW : 0
Tanzania Zantel TO122		255716405763	Weekly	$ 0	SD : 0 | SW : 0
Tanzania Zantel TO122		255673138874	Weekly	$ 0	SD : 0 | SW : 0
Tanzania Zantel TO122		255656298880	Weekly	$ 0	SD : 0 | SW : 0
Tanzania Zantel TO122		255712702691	Weekly	$ 0	SD : 0 | SW : 0
"""
burkinaFaso= """ 
IMS SMS | My SMS Numbers

Range	Prefix	Number	My Payterm	My Payout	Limits
Burkina Faso Onatel TF03		22673122746	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Onatel TF03		22651840981	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Onatel TF03		22673560639	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Onatel TF03		22662406113	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Onatel TF03		22670145161	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Onatel TF03		22652496000	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Onatel TF03		22671328916	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Onatel TF03		22672725039	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Onatel TF03		22660924620	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Onatel TF03		22602552206	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Onatel TF03		22663803410	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Onatel TF03		22671512444	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Onatel TF03		22670232520	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Onatel TF03		22661631751	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Onatel TF03		22651389118	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Onatel TF03		22672725055	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Onatel TF03		22652942218	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Onatel TF03		22663368142	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Onatel TF03		22651310795	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Onatel TF03		22673299808	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Onatel TF03		22672942613	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Onatel TF03		22601817923	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Onatel TF03		22651318596	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Onatel TF03		22673829763	Weekly	$ 0	SD : 0 | SW : 0
Burkina Faso Onatel TF03		22670205965	Weekly	$ 0	SD : 0 | SW : 0
"""

# find all numbers starting with 258 and remove the prefix
moz_numbers = [num[3:] for num in re.findall(r"\b258\d+\b", moz)]
slov_numbers = [num[3:] for num in re.findall(r"\b386\d+\b", slov)]
leb_numbers = [num[3:] for num in re.findall(r"\b961\d+\b", lebanon)]
# my_numbers = [num[2:] for num in re.findall(r"\b95\d+\b", my)]
Indonesia_numbers = [num[3:] for num in re.findall(r"\b221\d+\b", Senegal)]
burkinaNumber = [num[3:] for num in re.findall(r"\b226\d+\b", burkinaFaso)]




sub = "ch_"
verify =        f"Archived/IMGS/hdfc/{sub}verify_mobile.png"
change_number = f"Archived/IMGS/hdfc/{sub}change_number.png"
number_input =  f"Archived/IMGS/hdfc/{sub}number_input.png"
print(burkinaNumber)
for i, number in enumerate(burkinaNumber):
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

