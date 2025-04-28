from classes.questions.Question import Question
from classes.questions.MultipleChoiceQuestion import MultipleChoiceQuestion
from classes.questions.ExclusiveQuestion import ExclusiveQuestion
from classes.questions.AnswerOption import AnswerOption

from classes.Gender import Gender
from classes.Timeframe import Timeframe


def choices_for_69th_q() -> list[AnswerOption]: return [
	AnswerOption(Gender.same_for_all("a vă îndepărta foarte mult de casă"), 1),
	AnswerOption(Gender.same_for_all("a vă afla în locuri aglomerate"), 1),
	AnswerOption(Gender.same_for_all("a sta la coadă"), 1),
	AnswerOption(Gender.same_for_all("a vă afla pe un pod sau într-un tunel"), 1),
	AnswerOption(Gender.same_for_all("a călătorit cu autobuzul, trenul sau avionul"), 1),
	AnswerOption(Gender.same_for_all("a conduce sau a călători cu maşina"), 1),
	AnswerOption({Gender.F: "a fi singură acasă", Gender.M: "a fi singur acasă"}, 1),
	AnswerOption(Gender.same_for_all("a vă afla în spaţii deschise (cum ar fi un parc)"), 1),
]

def choices_for_77th_q() -> list[AnswerOption]: return [
	AnswerOption(Gender.same_for_all("a vorbi în public"), 1),
	AnswerOption(Gender.same_for_all("a mânca în faţa altor oameni"), 1),
	AnswerOption(Gender.same_for_all("a folosi toalete publice"), 1),
	AnswerOption(Gender.same_for_all("a scrie în faţa altor persoane"), 1),
	AnswerOption(Gender.same_for_all("a spune ceva prostesc când vă aflaţi într-un grup de oameni"), 1),
	AnswerOption(Gender.same_for_all("a pune o întrebare când vă aflaţi într-un grup de oameni"), 1),
	AnswerOption(Gender.same_for_all("a participa la întâlniri de afaceri"), 1),
	AnswerOption(Gender.same_for_all("a participa la petreceri sau alte întâlniri"), 1),
]


questions_by_subscale: dict[str, list[Question]] = {
	"Tulburare depresivă majoră": [
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi simţit tristă sau deprimată?",
				Gender.M: "v-aţi simţit trist sau deprimat?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
				AnswerOption(Gender.same_for_all("da, în cea mai mare parte a zilei, aproape în fiecare zi"), 0),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi bucurat mai puţin de aproape toate lucrurile care înainte, în mod normal, vă făceau plăcere?",
				Gender.M: "v-aţi bucurat mai puţin de aproape toate lucrurile care înainte, în mod normal, vă făceau plăcere?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi pierdut interesul pentru aproape toate activităţile de care, în mod normal, eraţi interesată?",
				Gender.M: "v-aţi pierdut interesul pentru aproape toate activităţile de care, în mod normal, eraţi interesat?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "aţi avut, aproape în fiecare zi, o poftă de mâncare semnificativ mai scăzută sau mai crescută decât de obicei?",
				Gender.M: "aţi avut, aproape în fiecare zi, o poftă de mâncare semnificativ mai scăzută sau mai crescută decât de obicei?",
			},
			[
				AnswerOption.no(),
				AnswerOption(Gender.same_for_all("da (mai scăzută decât de obicei)"), 1),
				AnswerOption(Gender.same_for_all("da (mai crescută decât de obicei)"), 1),
				AnswerOption(Gender.same_for_all("da (variază semnificativ)"), 2),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "aţi dormit, aproape în fiecare zi, semnificativ mai puţin sau mai mult decât de obicei?",
				Gender.M: "aţi dormit, aproape în fiecare zi, semnificativ mai puţin sau mai mult decât de obicei?",
			},
			[
				AnswerOption.no(),
				AnswerOption(Gender.same_for_all("da (cu cel puţin una sau două ore mai puţin)"), 1),
				AnswerOption(Gender.same_for_all("da (cu cel puţin una sau două ore mai mult)"), 1),
				AnswerOption(Gender.same_for_all("da (variază semnificativ)"), 2),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi simţit foarte agitată, fără astâmpăr şi vi s-a părut dificil să staţi liniştită, într-un loc, aproape în fiecare zi?",
				Gender.M: "v-aţi simţit foarte agitat, fără astâmpăr şi vi s-a părut dificil să staţi liniştit, într-un loc, aproape în fiecare zi?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi simţit obosită aproape în fiecare zi?",
				Gender.M: "v-aţi simţit obosit aproape în fiecare zi?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi simţit vinovată în mod frecvent pentru lucrurile pe care le-aţi făcut?",
				Gender.M: "v-aţi simţit vinovat în mod frecvent pentru lucrurile pe care le-aţi făcut?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi învinovăţit sau aţi avut gânduri negative despre dumneavoastră, aproape în fiecare zi?",
				Gender.M: "v-aţi învinovăţit sau aţi avut gânduri negative despre dumneavoastră, aproape în fiecare zi?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi simţit ca o ratată, aproape în fiecare zi?",
				Gender.M: "v-aţi simţit ca un ratat, aproape în fiecare zi?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "luarea unei decizii vi s-a părut mai grea decât de obicei, aproape în fiecare zi?",
				Gender.M: "luarea unei decizii vi s-a părut mai grea decât de obicei, aproape în fiecare zi?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi gândit în mod frecvent la ideea de a muri fără să faceţi dumneavoastră ceva, cum ar fi să muriţi în timpul somnului?",
				Gender.M: "v-aţi gândit în mod frecvent la ideea de a muri fără să faceţi dumneavoastră ceva, cum ar fi să muriţi în timpul somnului?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi dorit să fi murit?",
				Gender.M: "v-aţi dorit să fi murit?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi gândit că v-ar fi mai bine să fi murit?",
				Gender.M: "v-aţi gândit că v-ar fi mai bine să fi murit?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "aţi avut gânduri de sinucidere, chiar dacă nu aţi face cu adevărat acest lucru?",
				Gender.M: "aţi avut gânduri de sinucidere, chiar dacă nu aţi face cu adevărat acest lucru?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi gândit în mod serios să vă luaţi viaţa?",
				Gender.M: "v-aţi gândit în mod serios să vă luaţi viaţa?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi gândit la un mod anume în care să vă luaţi viaţa?",
				Gender.M: "v-aţi gândit la un mod anume în care să vă luaţi viaţa?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_2_weeks,
		),
	],
	"Tulburare de stres posttraumatic": [
		ExclusiveQuestion(
			{
				Gender.F: "Aţi trăit vreodată un eveniment traumatic cum ar fi: război, viol, atac fizic, abuz sexual sau orice alt eveniment traumatic extrem de supărător?",
				Gender.M: "Aţi trăit vreodată un eveniment traumatic cum ar fi: război, viol, atac fizic, abuz sexual sau orice alt eveniment traumatic extrem de supărător?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
		),
		ExclusiveQuestion(
			{
				Gender.F: "Aţi fost vreodată martor la un eveniment traumatic cum ar fi un viol, atac fizic, accident soldat cu deces sau orice alt eveniment extrem de supărător?",
				Gender.M: "Aţi fost vreodată martor la un eveniment traumatic cum ar fi un viol, atac fizic, accident soldat cu deces sau orice alt eveniment extrem de supărător?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
		),
		ExclusiveQuestion(
			{
				Gender.F: "v-au venit frecvent în minte gânduri referitoare la un eveniment traumatic?",
				Gender.M: "v-au venit frecvent în minte gânduri referitoare la un eveniment traumatic?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi supărat în mod frecvent pentru că v-aţi gândit la un eveniment traumatic?",
				Gender.M: "v-aţi supărat în mod frecvent pentru că v-aţi gândit la un eveniment traumatic?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "aţi fost frecvent deranjată de prezenţa unor amintiri sau vise legate de un eveniment traumatic?",
				Gender.M: "aţi fost frecvent deranjat de prezenţa unor amintiri sau vise legate de un eveniment traumatic?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "amintirile despre un eveniment traumatic v-au produs o suferinţă puternică?",
				Gender.M: "amintirile despre un eveniment traumatic v-au produs o suferinţă puternică?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "aţi încercat să blocaţi gândurile sau sentimentele legate de un eveniment traumatic?",
				Gender.M: "aţi încercat să blocaţi gândurile sau sentimentele legate de un eveniment traumatic?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "aţi încercat să evitaţi activităţile, locurile sau oamenii care vă aminteau de un eveniment traumatic?",
				Gender.M: "aţi încercat să evitaţi activităţile, locurile sau oamenii care vă aminteau de un eveniment traumatic?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "aţi avut amintiri (flashback-uri) în care să aveţi senzaţia că retrăiţi un eveniment traumatic?",
				Gender.M: "aţi avut amintiri (flashback-uri) în care să aveţi senzaţia că retrăiţi un eveniment traumatic?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "lucrurile care vă amintesc de un eveniment traumatic v-au făcut să tremuraţi, să transpiraţi sau v-au accelerat ritmul cardiac?",
				Gender.M: "lucrurile care vă amintesc de un eveniment traumatic v-au făcut să tremuraţi, să transpiraţi sau v-au accelerat ritmul cardiac?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi simţit distantă sau „ruptă” de ceilalţi oameni din cauză că aţi trăit un eveniment traumatic?",
				Gender.M: "v-aţi simţit distant sau „rupt” de ceilalţi oameni din cauză că aţi trăit un eveniment traumatic?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi simţit „amorţită” emoţional din cauză că aţi trăit un eveniment traumatic?",
				Gender.M: "v-aţi simţit „amorţit” emoţional din cauză că aţi trăit un eveniment traumatic?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "aţi renunţat la planurile dumneavoastră de viitor din cauză că aţi trăit un eveniment traumatic?",
				Gender.M: "aţi renunţat la planurile dumneavoastră de viitor din cauză că aţi trăit un eveniment traumatic?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "aţi fost excesiv de prudentă din cauză că aţi trăit un eveniment traumatic?",
				Gender.M: "aţi fost excesiv de prudent din cauză că aţi trăit un eveniment traumatic?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "aţi fost mai irascibilă sau v-aţi speriat mai uşor din cauză că aţi trăit un eveniment traumatic?",
				Gender.M: "aţi fost mai irascibil sau v-aţi speriat mai uşor din cauză că aţi trăit un eveniment traumatic?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_2_weeks,
		),
	],
    
	"Bulimie/Alimentație compulsivă": [
		ExclusiveQuestion(
			{
				Gender.F: "s-a întâmplat adesea să mâncaţi compulsiv (să mâncaţi foarte repede, o cantitate foarte mare de alimente, într-un timp foarte scurt)?",
				Gender.M: "s-a întâmplat adesea să mâncaţi compulsiv (să mâncaţi foarte repede, o cantitate foarte mare de alimente, într-un timp foarte scurt)?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "aţi avut adesea senzaţia că nu aveţi control asupra cantităţii de alimente pe care le consumaţi în timpul unui episod de mâncat compulsiv?",
				Gender.M: "aţi avut adesea senzaţia că nu aveţi control asupra cantităţii de alimente pe care le consumaţi în timpul unui episod de mâncat compulsiv?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "aţi avut episoade de mâncat compulsiv în care aţi mâncat atât de mult încât v-aţi simţit inconfortabil de plină?",
				Gender.M: "aţi avut episoade de mâncat compulsiv în care aţi mâncat atât de mult încât v-aţi simţit inconfortabil de plin?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "aţi avut episoade de mâncat compulsiv în care aţi mâncat o cantitate mare de alimente, chiar dacă nu vă era foame?",
				Gender.M: "aţi avut episoade de mâncat compulsiv în care aţi mâncat o cantitate mare de alimente, chiar dacă nu vă era foame?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "s-a întâmplat să mâncaţi compulsiv de una singură deoarece vă era jenă de cât de mult mâncaţi?",
				Gender.M: "s-a întâmplat să mâncaţi compulsiv de unul singur deoarece vă era jenă de cât de mult mâncaţi?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "s-a întâmplat să mâncaţi compulsiv şi apoi să vă fie silă de dumneavoastră?",
				Gender.M: "s-a întâmplat să mâncaţi compulsiv şi apoi să vă fie silă de dumneavoastră?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi supărat foarte tare pe dumneavoastră pentru că aţi mâncat compulsiv?",
				Gender.M: "v-aţi supărat foarte tare pe dumneavoastră pentru că aţi mâncat compulsiv?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "aţi recurs la diete foarte stricte sau la exerciţii fizice excesive pentru a nu lua în greutate ca urmare a mâncatului compulsiv?",
				Gender.M: "aţi recurs la diete foarte stricte sau la exerciţii fizice excesive pentru a nu lua în greutate ca urmare a mâncatului compulsiv?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "aţi luat laxative, diuretice sau v-aţi provocat voma pentru a nu lua în greutate ca urmare a mâncatului compulsiv?",
				Gender.M: "aţi luat laxative, diuretice sau v-aţi provocat voma pentru a nu lua în greutate ca urmare a mâncatului compulsiv?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "greutatea sau forma corpului dumneavostră au fost unele dintre cele mai importante lucruri care au influenţat felul în care gândiţi despre dumneavoastră?",
				Gender.M: "greutatea sau forma corpului dumneavostră au fost unele dintre cele mai importante lucruri care au influenţat felul în care gândiţi despre dumneavoastră?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_2_weeks,
		),
	],
	"Tulburare obsesiv-compulsivă": [
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi îngrijorat în mod obsesiv în legătură cu mizeria, microbii sau produsele chimice?",
				Gender.M: "v-aţi îngrijorat în mod obsesiv în legătură cu mizeria, microbii sau produsele chimice?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi îngrijorat în mod obsesiv că s-ar putea întâmpla ceva rău, pentru că aţi uitat să faceţi ceva important - cum ar fi să încuiaţi uşa, să opriţi gazul, să scoateţi aparatele electrice din priză?",
				Gender.M: "v-aţi îngrijorat în mod obsesiv că s-ar putea întâmpla ceva rău, pentru că aţi uitat să faceţi ceva important - cum ar fi să încuiaţi uşa, să opriţi gazul, să scoateţi aparatele electrice din priză?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "au fost lucruri pe care v-aţi simţit constrânsă să le faceţi în mod repetat (pentru cel puţin o jumătate de oră pe zi), fără a vă putea opri atunci când v-aţi propus acest lucru?",
				Gender.M: "au fost lucruri pe care v-aţi simţit constrâns să le faceţi în mod repetat (pentru cel puţin o jumătate de oră pe zi), fără a vă putea opri atunci când v-aţi propus acest lucru?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "au fost lucruri pe care v-aţi simţit constrânsă să le faceţi în mod repetat, în ciuda faptului că acestea vă împiedicau să finalizaţi alte lucruri pe care le aveaţi de făcut?",
				Gender.M: "au fost lucruri pe care v-aţi simţit constrâns să le faceţi în mod repetat, în ciuda faptului că acestea vă împiedicau să finalizaţi alte lucruri pe care le aveaţi de făcut?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "aţi spălat sau aţi curăţat în mod obsesiv şi excesiv lucrurile din jurul dumneavoastră?",
				Gender.M: "aţi spălat sau aţi curăţat în mod obsesiv şi excesiv lucrurile din jurul dumneavoastră?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "aţi verificat anumite lucruri sau aţi repetat diferite acţiuni la nesfârşit, în mod obsesiv şi excesiv?",
				Gender.M: "aţi verificat anumite lucruri sau aţi repetat diferite acţiuni la nesfârşit, în mod obsesiv şi excesiv?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "aţi numărat lucruri în mod obsesiv şi excesiv?",
				Gender.M: "aţi numărat lucruri în mod obsesiv şi excesiv?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_2_weeks,
		),
	],
	"Tulburare de panică": [
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi speriat foarte tare din cauză că inima vă bătea repede?",
				Gender.M: "v-aţi speriat foarte tare din cauză că inima vă bătea repede?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi speriat foarte tare din cauză că respiraţi cu dificultate?",
				Gender.M: "v-aţi speriat foarte tare din cauză că respiraţi cu dificultate?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi speriat foarte tare din cauză că v-aţi simţit slăbită sau pe punctul de a leşina?",
				Gender.M: "v-aţi speriat foarte tare din cauză că v-aţi simţit slăbit sau pe punctul de a leşina?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "aţi avut stări de teamă intensă sau de disconfort puternic (atacuri de panică), care au apărut pe neaşteptate, fără nici un motiv?",
				Gender.M: "aţi avut stări de teamă intensă sau de disconfort puternic (atacuri de panică), care au apărut pe neaşteptate, fără nici un motiv?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "aţi avut stări de teamă intensă sau de disconfort puternic, în timpul cărora v-aţi gândit că ceva groaznic se poate întâmpla, că aţi putea muri, că aţi putea înnebuni sau că aţi putea pierde controlul?",
				Gender.M: "aţi avut stări de teamă intensă sau de disconfort puternic, în timpul cărora v-aţi gândit că ceva groaznic se poate întâmpla, că aţi putea muri, că aţi putea înnebuni sau că aţi putea pierde controlul?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "aţi avut stări de teamă intensă sau de disconfort puternic, în timpul cărora aţi avut trei sau mai multe din următoarele simptome: bătăi accelerate ale inimii, transpiraţie, tremur, dificultăţi de respiraţie, greaţă, ameţeli sau senzaţia de leşin?",
				Gender.M: "aţi avut stări de teamă intensă sau de disconfort puternic, în timpul cărora aţi avut trei sau mai multe din următoarele simptome: bătăi accelerate ale inimii, transpiraţie, tremur, dificultăţi de respiraţie, greaţă, ameţeli sau senzaţia de leşin?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi îngrijorat foarte mult în legătură cu a avea atacuri de panică neaşteptate?",
				Gender.M: "v-aţi îngrijorat foarte mult în legătură cu a avea atacuri de panică neaşteptate?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "aţi avut atacuri de panică din cauza cărora aţi evitat anumite situaţii sau v-aţi modificat comportamentul sau activităţile zilnice?",
				Gender.M: "aţi avut atacuri de panică din cauza cărora aţi evitat anumite situaţii sau v-aţi modificat comportamentul sau activităţile zilnice?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_2_weeks,
		),
	],
	"Tulburări psihotice": [
		ExclusiveQuestion(
			{
				Gender.F: "s-au întâmplat lucruri despre care ştiaţi că sunt adevărate, dar despre care ceilalţi v-au spus că sunt doar în imaginaţia dumneavoastră?",
				Gender.M: "s-au întâmplat lucruri despre care ştiaţi că sunt adevărate, dar despre care ceilalţi v-au spus că sunt doar în imaginaţia dumneavoastră?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "s-a întâmplat să fiţi convins că ceilalţi se uită la dumneavoastră, vorbesc despre dumneavoastră sau vă spionează?",
				Gender.M: "s-a întâmplat să fiţi convins că ceilalţi se uită la dumneavoastră, vorbesc despre dumneavoastră sau vă spionează?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi gândit că sunteţi în pericol deoarece cineva plănuieşte să vă facă rău?",
				Gender.M: "v-aţi gândit că sunteţi în pericol deoarece cineva plănuieşte să vă facă rău?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "aţi considerat că aveţi puteri speciale, pe care alţi oameni nu le au?",
				Gender.M: "aţi considerat că aveţi puteri speciale, pe care alţi oameni nu le au?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi gândit că o forţă exterioară vă controlează corpul sau mintea?",
				Gender.M: "v-aţi gândit că o forţă exterioară vă controlează corpul sau mintea?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_2_weeks,
		),
		ExclusiveQuestion(
			{
				Gender.F: "aţi auzit voci pe care ceilalţi nu le aud sau aţi văzut lucruri pe care ceilalţi nu le văd?",
				Gender.M: "aţi auzit voci pe care ceilalţi nu le aud sau aţi văzut lucruri pe care ceilalţi nu le văd?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_2_weeks,
		),
	],
	"Agorafobie": [
		ExclusiveQuestion(
			{
				Gender.F: "aţi evitat în mod regulat anumite situaţii deoarece v-a fost teamă că acestea vă vor provoca un atac de panică?",
				Gender.M: "aţi evitat în mod regulat anumite situaţii deoarece v-a fost teamă că acestea vă vor provoca un atac de panică?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_6_months,
		),
		MultipleChoiceQuestion(
			{
				Gender.F: "v-au făcut să vă simţiţi speriată, neliniştită sau agitată că veţi avea un atac de panică vreuna din următoarele situaţii?",
				Gender.M: "v-au făcut să vă simţiţi speriat, neliniştit sau agitat că veţi avea un atac de panică vreuna din următoarele situaţii?",
			},
			choices_for_69th_q(),
			Timeframe.last_6_months,
		),
		MultipleChoiceQuestion(
			{
				Gender.F: "aţi devenit foarte neliniştită aproape de fiecare dată când v-aţi aflat într-una din următoarele situaţii?",
				Gender.M: "aţi devenit foarte neliniştit aproape de fiecare dată când v-aţi aflat într-una din următoarele situaţii?",
			},
			choices_for_69th_q(),
			Timeframe.last_6_months,
			lambda l: int(len(l) > 0),
		),
		MultipleChoiceQuestion(
			{
				Gender.F: "aţi evitat vreuna din următoarele situaţii din cauză că v-au făcut să vă simţiţi neliniştită sau speriată?",
				Gender.M: "aţi evitat vreuna din următoarele situaţii din cauză că v-au făcut să vă simţiţi neliniştit sau speriat?",
			},
			choices_for_69th_q(),
			Timeframe.last_6_months,
			lambda l: int(len(l) > 0),
		),
	],
	"Fobie socială": [
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi îngrijorat foarte mult că vă veţi face de râs în faţa celorlalţi?",
				Gender.M: "v-aţi îngrijorat foarte mult că vă veţi face de râs în faţa celorlalţi?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_6_months,
		),
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi îngrijorat foarte mult că s-ar putea să faceţi ceva care i-ar determina pe ceilalţi să vă considere proastă sau ridicolă?",
				Gender.M: "v-aţi îngrijorat foarte mult că s-ar putea să faceţi ceva care i-ar determina pe ceilalţi să vă considere prost sau ridicol?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_6_months,
		),
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi simţit foarte agitată în situaţiile în care era posibil ca oamenii să fie atenţi la dumneavoastră?",
				Gender.M: "v-aţi simţit foarte agitat în situaţiile în care era posibil ca oamenii să fie atenţi la dumneavoastră?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_6_months,
		),
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi simţit extrem de agitată în situaţii sociale?",
				Gender.M: "v-aţi simţit extrem de agitat în situaţii sociale?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_6_months,
		),
		ExclusiveQuestion(
			{
				Gender.F: "aţi evitat cu regularitate anumite situaţii deoarece v-a fost teamă că aţi putea face sau spune ceva prin care să vă faceţi de râs?",
				Gender.M: "aţi evitat cu regularitate anumite situaţii deoarece v-a fost teamă că aţi putea face sau spune ceva prin care să vă faceţi de râs?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_6_months,
		),
		MultipleChoiceQuestion(
			{
				Gender.F: "v-aţi îngrijorat foarte mult că veţi face sau spune ceva prin care să vă faceţi de râs în oricare din următoarele situaţii?",
				Gender.M: "v-aţi îngrijorat foarte mult că veţi face sau spune ceva prin care să vă faceţi de râs în oricare din următoarele situaţii?",
			},
			choices_for_77th_q(),
			Timeframe.last_6_months,
		),
		MultipleChoiceQuestion(
			{
				Gender.F: "aţi devenit brusc foarte neliniştită aproape de fiecare dată când v-aţi aflat într-una din următoarele situaţii?",
				Gender.M: "aţi devenit brusc foarte neliniştit aproape de fiecare dată când v-aţi aflat într-una din următoarele situaţii?",
			},
			choices_for_77th_q(),
			Timeframe.last_6_months,
			lambda l: int(len(l) > 0),
		),
		MultipleChoiceQuestion(
			{
				Gender.F: "aţi evitat vreuna din următoarele situaţii din cauză că v-au făcut să vă simţiţi neliniştită sau speriată?",
				Gender.M: "aţi evitat vreuna din următoarele situaţii din cauză că v-au făcut să vă simţiţi neliniştit sau speriat?",
			},
			choices_for_77th_q(),
			Timeframe.last_6_months,
			lambda l: int(len(l) > 0),
		),
	],
	"Abuz/dependență de alcool": [
		ExclusiveQuestion(
			{
				Gender.F: "aţi considerat că aţi consumat prea mult alcool?",
				Gender.M: "aţi considerat că aţi consumat prea mult alcool?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_6_months,
		),
		ExclusiveQuestion(
			{
				Gender.F: "cineva din familia dumneavoastră a considerat sau a susţinut că aţi consumat prea mult alcool sau că aveţi o problemă cu alcoolul?",
				Gender.M: "cineva din familia dumneavoastră a considerat sau a susţinut că aţi consumat prea mult alcool sau că aveţi o problemă cu alcoolul?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_6_months,
		),
		ExclusiveQuestion(
			{
				Gender.F: "prietenii, un medic sau orice altă persoană a considerat sau a susţinut că aţi consumat prea mult alcool?",
				Gender.M: "prietenii, un medic sau orice altă persoană a considerat sau a susţinut că aţi consumat prea mult alcool?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_6_months,
		),
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi gândit să renunţaţi sau să reduceţi cantitatea de alcool pe care o consumaţi?",
				Gender.M: "v-aţi gândit să renunţaţi sau să reduceţi cantitatea de alcool pe care o consumaţi?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_6_months,
		),
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi gândit că aveţi o problemă cu alcoolul?",
				Gender.M: "v-aţi gândit că aveţi o problemă cu alcoolul?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_6_months,
		),
		ExclusiveQuestion(
			{
				Gender.F: "consumul de alcool v-a cauzat probleme în căsnicie, la locul de muncă, cu prietenii sau în familie, în îndeplinirea sarcinilor casnice sau în alt domeniu important al vieţii dumneavoastră?",
				Gender.M: "consumul de alcool v-a cauzat probleme în căsnicie, la locul de muncă, cu prietenii sau în familie, în îndeplinirea sarcinilor casnice sau în alt domeniu important al vieţii dumneavoastră?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_6_months,
		),
	],
	"Abuz/dependență de medicamente": [
		ExclusiveQuestion(
			{
				Gender.F: "aţi considerat că aţi luat prea multe medicamente?",
				Gender.M: "aţi considerat că aţi luat prea multe medicamente?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_6_months,
		),
		ExclusiveQuestion(
			{
				Gender.F: "cineva din familia dumneavoastră a considerat sau a susţinut că aţi luat prea multe medicamente sau că aveţi o problemă cu acestea?",
				Gender.M: "cineva din familia dumneavoastră a considerat sau a susţinut că aţi luat prea multe medicamente sau că aveţi o problemă cu acestea?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_6_months,
		),
		ExclusiveQuestion(
			{
				Gender.F: "prietenii, un medic, sau oricine altcineva a considerat sau a susţinut că aţi luat prea multe medicamente?",
				Gender.M: "prietenii, un medic, sau oricine altcineva a considerat sau a susţinut că aţi luat prea multe medicamente?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_6_months,
		),
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi gândit să renunţaţi sau să reduceţi consumul de medicamente?",
				Gender.M: "v-aţi gândit să renunţaţi sau să reduceţi consumul de medicamente?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_6_months,
		),
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi gândit că aveţi o problemă cu medicamentele?",
				Gender.M: "v-aţi gândit că aveţi o problemă cu medicamentele?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_6_months,
		),
		ExclusiveQuestion(
			{
				Gender.F: "din cauza consumului de medicamente aţi avut probleme în căsnicie, la locul de muncă, cu prietenii sau în familie, în îndeplinirea sarcinilor casnice sau în orice alt segment important al vieţii dumneavoastră?",
				Gender.M: "din cauza consumului de medicamente aţi avut probleme în căsnicie, la locul de muncă, cu prietenii sau în familie, în îndeplinirea sarcinilor casnice sau în orice alt segment important al vieţii dumneavoastră?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_6_months,
		),
	],
	"Tulburare de anxietate generalizată": [
		ExclusiveQuestion(
			{
				Gender.F: "aţi fost o persoană agitată în majoritatea zilelor?",
				Gender.M: "aţi fost o persoană agitată în majoritatea zilelor?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_6_months,
		),
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi îngrijorat foarte mult că s-ar putea întâmpla ceva rău cu dumneavoastră sau cuiva apropiat?",
				Gender.M: "v-aţi îngrijorat foarte mult că s-ar putea întâmpla ceva rău cu dumneavoastră sau cuiva apropiat?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_6_months,
		),
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi îngrijorat în legătură cu lucruri despre care ceilalţi v-au spus că nu merită să vă faceţi griji?",
				Gender.M: "v-aţi îngrijorat în legătură cu lucruri despre care ceilalţi v-au spus că nu merită să vă faceţi griji?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_6_months,
		),
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi îngrijorat sau aţi fost neliniştită în legătură cu mai multe lucruri din viaţa dumneavoastră, în majoritatea zilelor?",
				Gender.M: "v-aţi îngrijorat sau aţi fost neliniştit în legătură cu mai multe lucruri din viaţa dumneavoastră, în majoritatea zilelor?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_6_months,
		),
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi simţit adesea neliniştită sau la limită din cauza grijilor pe care vi le-aţi făcut?",
				Gender.M: "v-aţi simţit adesea neliniştit sau la limită din cauza grijilor pe care vi le-aţi făcut?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_6_months,
		),
		ExclusiveQuestion(
			{
				Gender.F: "aţi adormit adesea cu greu din cauză că v-aţi îngrijorat pentru tot felul de lucruri?",
				Gender.M: "aţi adormit adesea cu greu din cauză că v-aţi îngrijorat pentru tot felul de lucruri?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_6_months,
		),
		ExclusiveQuestion(
			{
				Gender.F: "aţi simţit adesea tensiune musculară din cauza neliniştii sau a stresului?",
				Gender.M: "aţi simţit adesea tensiune musculară din cauza neliniştii sau a stresului?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_6_months,
		),
		ExclusiveQuestion(
			{
				Gender.F: "aţi avut adesea probleme de concentrare din cauză că eraţi preocupată de grijile dumneavoastră?",
				Gender.M: "aţi avut adesea probleme de concentrare din cauză că eraţi preocupat de grijile dumneavoastră?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_6_months,
		),
		ExclusiveQuestion(
			{
				Gender.F: "s-a întâmplat să fiţi adesea certăreaţă sau irascibilă din cauză că eraţi îngrijorată sau stresată?",
				Gender.M: "s-a întâmplat să fiţi adesea certăreţ sau irascibil din cauză că eraţi îngrijorat sau stresat?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_6_months,
		),
		ExclusiveQuestion(
			{
				Gender.F: "v-a fost greu să vă controlaţi grijile sau să nu vă mai îngrijoraţi deloc, în majoritatea zilelor?",
				Gender.M: "v-a fost greu să vă controlaţi grijile sau să nu vă mai îngrijoraţi deloc, în majoritatea zilelor?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_6_months,
		),
	],
	"Tulburare de somatizare": [
		ExclusiveQuestion(
			{
				Gender.F: "aţi avut multe probleme cu stomacul sau cu intestinele, cum ar fi greaţă, vomă, gaze în exces, balonare sau diaree?",
				Gender.M: "aţi avut multe probleme cu stomacul sau cu intestinele, cum ar fi greaţă, vomă, gaze în exces, balonare sau diaree?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_6_months,
		),
		ExclusiveQuestion(
			{
				Gender.F: "aţi avut dureri în mai multe părţi diferite ale corpului?",
				Gender.M: "aţi avut dureri în mai multe părţi diferite ale corpului?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_6_months,
		),
		ExclusiveQuestion(
			{
				Gender.F: "Vă îmbolnăviţi mai des decât majoritatea oamenilor?",
				Gender.M: "Vă îmbolnăviţi mai des decât majoritatea oamenilor?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
		),
		ExclusiveQuestion(
			{
				Gender.F: "Aţi avut o sănătate fizică precară aproape toată viaţa?",
				Gender.M: "Aţi avut o sănătate fizică precară aproape toată viaţa?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
		),
		ExclusiveQuestion(
			{
				Gender.F: "De obicei, medicii nu reuşesc să identifice o cauză fizică pentru simptomele dumneavoastră?",
				Gender.M: "De obicei, medicii nu reuşesc să identifice o cauză fizică pentru simptomele dumneavoastră?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
		),
	],
	"Ipohondrie": [
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi făcut adesea griji că s-ar putea să suferiţi de o boală fizică gravă?",
				Gender.M: "v-aţi făcut adesea griji că s-ar putea să suferiţi de o boală fizică gravă?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(is_critical=True),
			],
			Timeframe.last_6_months,
		),
		ExclusiveQuestion(
			{
				Gender.F: "v-a fost greu să nu vă mai îngrijoraţi că suferiţi de o boală fizică gravă?",
				Gender.M: "v-a fost greu să nu vă mai îngrijoraţi că suferiţi de o boală fizică gravă?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_6_months,
		),
		ExclusiveQuestion(
			{
				Gender.F: "v-a fost greu să nu vă îngrijoraţi în ciuda faptului că medicul v-a spus că nu suferiţi de nicio boală gravă?",
				Gender.M: "v-a fost greu să nu vă îngrijoraţi în ciuda faptului că medicul v-a spus că nu suferiţi de nicio boală gravă?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_6_months,
		),
		ExclusiveQuestion(
			{
				Gender.F: "v-aţi îngrijorat atât de mult că suferiţi de o boală fizică gravă, încât acest lucru a interferat cu activităţile dumneavoastră zilnice sau v-a cauzat probleme?",
				Gender.M: "v-aţi îngrijorat atât de mult că suferiţi de o boală fizică gravă, încât acest lucru a interferat cu activităţile dumneavoastră zilnice sau v-a cauzat probleme?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_6_months,
		),
		ExclusiveQuestion(
			{
				Gender.F: "aţi fost la doctor în mod frecvent deoarece eraţi îngrijorată că suferiţi de o boală fizică gravă?",
				Gender.M: "aţi fost la doctor în mod frecvent deoarece eraţi îngrijorat că suferiţi de o boală fizică gravă?",
			},
			[
				AnswerOption.no(),
				AnswerOption.yes(),
			],
			Timeframe.last_6_months,
		),
	],
}