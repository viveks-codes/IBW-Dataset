REPLACE = {'a': '@', 'i': '*', 'o': '*', 'u': '*', 'v': '*', 
 'l': '1', 'e': '*', 's': '$', 't': '7'}
from itertools import product




def Leet2Combos(word):
    possibles = []
    for l in word.lower():
        ll = REPLACE.get(l, l)
        possibles.append( (l,) if ll == l else (l, ll) )
    return [ ''.join(t) for t in product(*possibles) ]



s =  \
"""Chodon Boiraagi
Chodon Idli
chood
chudir bhai
Chudir Bhai
Chudir Pola
dan-da
dhon
dofla hetta
fatly
Fel
foga
foon, foondh
fungi
Futki
fuun-ga
gorur bachcha
gud
gud maranir beta
gud/guud
Guundaa
Haram jada
haram jadi
Hauwa
hetta muka ath bori dimo
hetta, bodha, shauwaa
Kalu, Calou, Kalou,Blackie, Keltu, Kelo, Kolo Toure, Djimi Traore, Kalo Hulo, Nigga
khanki
khanki chudi magir gude poka
khanki/maggi
khankir chele
Khankir Pola
khobis or goror khobis
Kuth-tar Bachcha
Kuthar Bacha
Kuththar Baiccha (Baich-cha)
Kuttar Bhaccha
kuttar chod
Kuttar gu
laora
lerr
lerr kawrar fua
Maagi
Maal
maggir putt
Moga choder bacha
mother chod
Muta kuta
nankta kuttar baccha
Nunu
nunu
pagol sagol
Pagul
pasa
podmarani
Sagul
Shauwa
shuorer baccha
Shurur Batcha
Suda-sudi
SUDAURIER FURII
SUDAURY
Suourer bachcha
SUTHH-MAROUNY
thor hetta laythum
thor maa suda
thor maar bothoy kha
thore astha gao eh sudeh
thumar futki marthum
Thumi amar nunu khoa, onek mishti
Thuuii Bandhorr
Thuuii Gaadhaa
to-mar ma hetta
Tor baaf fel Khai
Tor Bafor Boga Saat
tor ma amar fell
tor ma boga cha
Tor Maa
tor maa booni nay
tor maa ke chudi
Tor mayere chudi
Tor nanire chudi
tor nunu bouut boro
Tor pasha mota
tu ekta bandar
Tur booga sooto
tur mar booni khaa
tuy ath marros
Vogchod
Bain Chod
Bainchod
Bassa Shouko
chodnar po
Gud-marani
hagoo
Hijra
Hoga
Khankir pola
Kuthaar Baicha
Kuttar Bachcha
kuttar bachcha
Leura
Magi
Mai
makhal
muri kha
Noakhailla
randi magi
thor maa khai lai moo
thor maar bosoi khai see
Tomar maar putkey fatamu .
Tor babar bichi fatabo
Tor mar sawa kha
tor mare chudi
tur ma amar fel be
Aanguli kora
achuda
ads
Ami tor maa ke chudmu
baal
Baal chhero
Bara
Beissha Magir Pola
Bhag
Bhoda
Bokachoda
boltu chire felbo
botoi khowra
Choda
Chood
Chudanir pola
Chudi
Chudmu tor pasai sneha
Chumban
Chumu
Dhon
Dhon khecha
Gaand Maarano
Gud
Humaira
Khanki
khanki Magi
khankir pola
kuttar Baccha
lehr kawrar bachha
Mang
Naang
pod marani
Pond
Shetar bal
Shishna
Sohail
Thor heta muka ath boridimu
Tor Gaar Maari
Tor maa ke chudi
tor mar vhoda
tumi bal hagu koro!!
Vuuski magi
Aar
bahanchod
baila
baklol
bapjeth
bawaseer ho kya
bhadwa
bhethi
bhosda
bhosri wali
boor
Boor ka baal
burbak
chhinar
chhota chetan
chuchi
chutmuha
dogla
gaar marao
gaar maraye duniya
gaar me daal le
gadchat
gopal gaurav
jhatwa
kiski maiyaa kutta biyayi
laar
laar chato
laar lega
larchat
maa chudao
muth
randi ka bachha
randikhana
ravi kumar patel
tori bahin ke chodu
tori maiyaa ke chodu
maari tatoori ne chalay
Akbaruddin Owaisi
Alloo Bhosri Chaat
Anuj
Babhuchak
bai no bhosdo
bein chod
Benchod
Bhadvo
bhenchod
Bhoot
Bhopa
Bhos marina
Bhosad Pappu
bhosdo
bhosrini
bobla
Bobla Vagarni Baydi
Bosrichord
bosrina
Buckwass
Budhalal
chafu gaan
Chichi
Chod
Chod ami
Chodhru
chodkanya
Chodu
chupri lauri
Chutiya
Darshil
Dheela Lund Ni Olaad
Eapen
Fattu
gaan tari
Gaand Ghapli
Gaand Ma Ghal
gaandina, gandina
Gand nu kaanu
gandi chodina
gando
Gando salo
gel ghagharina
Ghel Chodyo
Ghelchoydi
Halki Raand na
Harsh Dalal
harshit
hopa
Huzefa
jaaro
Jhadhino!
karo loro
kem chho
kutari
Lakhota
Land
loda
lodde mari
Lowroh
luli
Lund Bhagat
Maa ne ghat bhosdina
maajaddha
maari tatoori ooper bess
maasi chodamno
Madachod
madachod
mandi susee
Manik
mara man no lado
mari bhosri chaat
meri gaan chatt
Mohit
Moht
mota jijah
nago choido
Nakhodiya
Namuno
Narender Modi
pikina
Pikina
pim pim
poom poom
Priyanshu
puchi chod
Puti
raand
rumana
sali
salu gut`ti
Sandas
suwwar jewu dachu
taari bai no aghano
Taari ma parasevo tya-reh e tuti kareh che!
Tara baap ni gaan
Taree gaar ma lowroh
Taree Ghaar Ma Doh Ladah
tari bosri kaapi karwa
tari dagri
tari gaand mare karya kutra balada
tari gandayli kari koyli dagri
Tari ma na bubla sukai-gya
tari ma ne hadi kadhto hathi chode
tari ma ni putti
tari ma no poplo
Tari maa na babla chusu
Tari maa na bhosda ma maro lodo
Tari maa na modha ma maro lodo
Tari maa ne chodu
Tari maa ni taturi
tari mai ni gand
tari mani choot ma derka bole
Taro baap tane chadeche
tere ma nu hinta kar
teree maah gaderi
thari ma ne bozro maro loro nakhides
Thari Ma Ni Ghaan
Tusat
Tutelli nirodh no aulad
bahan ke lawde
Bawali gand
Bhen ke dine
chudhu ke chodde
Dhi ke lawde
Dhichod
Domesaks danso danlo motar!
bhoor
chuttar
chuttari
gand chod
Ghunt Fala
Jhulaniya
Madhar chod
shivom lal
teri maichod
miya ka katela lund
miyan
miyan bhadvi
miyan rand
miye log madharchod
chut
chut ke baal
chut ke dhakkan
chut maarli
chutad
chutadd
chutan
chutia
chutiya
gaand
gaandfat
gaandmasti
gaandufad
gandu
gashti
gasti
ghassa
ghasti
harami
haramzade
hawas
hawas ke pujari
hijda
hijra
jhant
jhant chaatu
jhant ke baal
jhantu
kamine
kaminey
kanjar
kutta
kutta kamina
kutte ki aulad
kutte ki jat
kuttiya
loda
lodu
lund
lund choos
lund khajoor
lundtopi
lundure
maa ki chut
maal
madar chod
mooh mein le
mutth
najayaz
najayaz aulaad
najayaz paidaish
paki
pataka
patakha
raand
randi
saala
saala kutta
saali kutti
saali randi
suar
suar ki aulad
tatte
tatti
teri maa ka bhosada
teri maa ka boba chusu
teri maa ki chut
tharak
tharki
bsdk
mc
bsdk
hutiye
chakka
randwe
randve
chutiye
madarjaat
lomda
chumtiya
chumtiye
chus
tatto
goti
gotiya
gand
chuut
chodya
ke chode
chode
chodyu
boba
kutta
fakir
Jaan var
Kutta
Kuttiya
Khota
Khotey ki aulad
Kutte ki jat
Najayaz
Najayaz paidaish
Saala kutta
Saali kutti
Soover
Tatti
Hindi Swear Words
Bahen Chod
Bahen ke laude
Bahen ke takke
Beti Chod
Bhai Chod
Bhains ki aulad
Jhalla, Faggot
Jhant ke baal
Jhaant ke pissu
Kutte ka aulad
Kutte ke tatte
Maadher chod
Padma
Raand ka jamai
Randhwa (or randwa)
Rundi
Rundi ka bacha
Rundi Ki bachi
Soower ke bachche
Ullu ke pathe
Hindi Dirty Words
Bandaa
Booblay
BhonsRi-Waalaa
Carrom board
Chhed
Chut
Chut marike
Chodu
Chodra
Choochii
Gaandu
Gaand
Ing ge pan di kut teh
LavDa
Lavde
Lund 
Lavde ke bal
Lavander
Mangachinamun
Muth mar
Nimbu sharbat
Maa ke bable
Mammey mumm-aye
Tatte Masalna
Toto
Toota hua lund
Hindi Profane Words
Backar chodu
Bhand khau
Bhandwe ki aulad
Bhosad Chod
Bumchod
Bur ki chatani
Cuntmama
Chipkali ke chut ke pasine
Chipkali ke gaand ke pasine
Chipkali ke jhaat ke baal
Chippkali ke jhaant ke paseene
Chodela
Chodu bhagat
Chhola Phudakna
Chudan chudai
Chudai khana
Chunni
Choot ka baal
Choot ke bhoot
Chut ke dhakkan
Chut mari ke
Choot marani ka
Chut ke pasine mein talay huye bhajiye
Chup Ke Chut Hai
Fatey condom kay natije
Fatay huay lundtopi ka result
Gaandu
Gaandfat
Gaandmasti
Gaand ka makhan
Gaand marau
Ghondoo
Jhant chaatu
Jhaat ka bhaaji
Kutte ka beej
Lund choosu
Lund fakeer
Lundoos
Lund ka shorba
Land ka bheja
Lund pe chad ja
Lund pe thand hai
Lund Ke Pasine
Lavde ke baal
Maa ke bhadwe
Muth maar
Parichod
Phatele Nirodh ke Natije
Pucchi
Raandi baajer
Rundi ko choud
Rubber bhosda
Sadi hui gand
Tera adha Nirodh mein rah gaya
Hindi Obscene Words
Apna land choos
Apni gaand mein muthi daal
Apni ma ko ja choos
Chinaal ke gadde ke nipple ke baal ke joon
Chullu bhar muth mein doob mar
Gand Ka Khatmal
Gandkate Kutte
Gaand mein bambu
Gaand main lassan
Gaand main danda
Gaand main keera
Hazaar lund teri gaand main
Jaa Apni Bajaa
Jab tu paida hua tow aagey se ya peechey se nikla tha chutiya?
Kahe ko kha raha hai chut ki chapati aur lund ka beja?
Kali Choot Ke Safaid Jhaat
Kutte ke poot, teri maa ki choot
Lo, mera lund anpi behen ko de do, agar khud na chod paya
Lund Chus
Ma chudi
Mein teri maa ko teri bahen ki choot mein chodoonga aur tera baap laltern lekar aayega.
Mein teri maa ko liya tha uski suhaag raat pei.
Mera chunni choos
Meri lund choos
Mere Chuus Maro
Na choot, na chooche, nakhre noor jahan ke!
Raand ka pati
Rundi ko chod
Rundi ki tatti pe baithnewaali makkhi
Rundi ke tatti pe biathne wala makhi
Terey baad di gaand wich danda ghussa ker rakh dhungi.
Teri behen ka launda rubber ka 
Theri Biwi ko Tere Saamne Chodhunga
Teri Gand Mein Haathi Ka Lund
Teri gaand main kute ka lund
Tere gaand mein keede paday
Teri Jhanten Kaat kar tere mooh par laga kar unki french beard bana doonga.
Teri ma gandi rundi
Teri ma gadha ka lund choosay
Teri maa ki bimaar badboodar choot
Teri ma ki choot me hathi ka dum
Teri ma ki chut mai sabka lund
Teri maa ki phudi guy ki hai
Teri maa ka bhosda
Teri maa ki chute
Tere mai ki chut tere baap ka land
Teri mi di kussi mey tera sarra khandan ko ghussa ker rakh doonga.
Teri maa ki gaand ki baal mein jalaay hue, maarey hue chipkili ki unday.
Teri ma ki budh mein chaarpai bichhake teri bahen ko chodun.
Teri maa ki chut mein chatri leke ghus jaunga aur khol dunga.
Tere maa ko sau kutte chode - sau wa tera baap!
Tor mai ke chodho
jaanvar
kutta
kutiya
khota
auladheen
jaat
najayaz
gandpaidaish
saala
kutti
soover
tatti
potty
behnchodon
behnchod
behenchod
behenchodd
bahenchod
bahanchod
bahencho
bancho
sali
bahenke
laude
takke
betichod
bhaichod
bhains
jhalla
jhant
nabaal
pissu
kutte
maderjat
madherchod
maderchod
madaarchod
madarjaat
maachod
madharchod
maderchodo
machod
maadherchod
madarchodon
madarchodd
madarchod
maadarchod
padma
raand
jamai
randwa
randi
bachachod
bachichod
soower
bachchechod
ullu
pathe
banda
booblay
booby
suar
buble
rand
babla
bhonsriwala
bhonsdiwala
ched
chut
chod
chodu
chodra
choochi
chuchi
gaandu
gandu
gaand
lavda
lawda
lauda
lund
balchod
lavander
muth
maacho
mammey
tatte
toto
toota
backar
bhandwe
bhosadchod
bhosad
bumchod
bum
bur
chatani
cunt
cuntmama
chipkali
sale
pasine
jhaat
chodela
bhagatchod
chhola
chudai
chudaikhana
chunni
choot
bhoot
dhakkan
bhajiye
fateychu
gandnatije
lundtopi
gaandu
gaandfat
gaandmasti
makhanchudai
gaandmarau
gandu
gand
chaatu
beej
choosu
fakeerchod
lundoos
shorba
binbheja
bhadwe
parichod
nirodh
pucchi
baajer
choud
bhosda
sadi
choos
maka
chinaal
gadde
joon
chullugand
doob
khatmal
gandkate
bambu
lassan
danda
keera
keeda
hazaarchu
paidaishikeeda
kali
safaid
poot
behendi
chus
machudi
chodoonga
baapchu
laltern
suhaagchudai
raatchuda
kaalu
neech
chikna
meetha
beechka
jihaadi
chooche
patichod
rundi
makkhi
biwichod
chodhunga
haathi
kute
jhanten
kaat
gandi
gadha
bimaar
badboodar
dum
raandsaala
phudi
chute
kussi
khandanchod
ghussa
maarey
chipkili
unday
budh
chaarpai
chodun
chatri
chode
chodho
mulle
mulli
musalman
momedan
katua
chutiyapa
bc
mc
chudwaya
kutton
lodi
loda
jungli
vahiyaat
jihadi
atankvadi
atankwadi
aatanki
aatankwadi
Beti Chod
Bhai Chod
Bhains ki aulad
Jhalla, Faggot
Jhant ke baal
Jhaant ke pissu
Kutte ka aulad
Kutte ke tatte
Maadher chod
Padma
Raand ka jamai
Randhwa (or randwa)
Rundi
Rundi ka bacha
Rundi Ki bachi
Soower ke bachche
Ullu ke pathe
Hindi Dirty Words
Bandaa
Booblay
BhonsRi-Waalaa
Carrom board
Chhed
Chut
Chut marike
Chodu
Chodra
Choochii
Gaandu
Gaand
Ing ge pan di kut teh
LavDa
Lavde
Lund 
Lavde ke bal
Lavander
Mangachinamun
Muth mar
Nimbu sharbat
Maa ke bable
Mammey mumm-aye
Tatte Masalna
Toto
Toota hua lund
Hindi Profane Words
Backar chodu
Bhand khau
Bhandwe ki aulad
Bhosad Chod
Bumchod
Bur ki chatani
Cuntmama
Chipkali ke chut ke pasine
Chipkali ke gaand ke pasine
Chipkali ke jhaat ke baal
Chippkali ke jhaant ke paseene
Chodela
Chodu bhagat
Chhola Phudakna
Chudan chudai
Chudai khana
Chunni
Choot ka baal
Choot ke bhoot
Chut ke dhakkan
Chut mari ke
Choot marani ka
Chut ke pasine mein talay huye bhajiye
Chup Ke Chut Hai
Fatey condom kay natije
Fatay huay lundtopi ka result
Gaandu
Gaandfat
Gaandmasti
Gaand ka makhan
Gaand marau
Ghondoo
Jhant chaatu
Jhaat ka bhaaji
Kutte ka beej
Lund choosu
Lund fakeer
Lundoos
Lund ka shorba
Land ka bheja
Lund pe chad ja
Lund pe thand hai
Lund Ke Pasine
Lavde ke baal
Maa ke bhadwe
Muth maar
Parichod
Phatele Nirodh ke Natije
Pucchi
Raandi baajer
Rundi ko choud
Rubber bhosda
Sadi hui gand
Tera adha Nirodh mein rah gaya
Hindi Obscene Words
Apna land choos
Apni gaand mein muthi daal
Apni ma ko ja choos
Chinaal ke gadde ke nipple ke baal ke joon
Chullu bhar muth mein doob mar
Gand Ka Khatmal
Gandkate Kutte
Gaand mein bambu
Gaand main lassan
Gaand main danda
Gaand main keera
Hazaar lund teri gaand main
Jaa Apni Bajaa
Jab tu paida hua tow aagey se ya peechey se nikla tha chutiya?
Kahe ko kha raha hai chut ki chapati aur lund ka beja?
Kali Choot Ke Safaid Jhaat
Kutte ke poot, teri maa ki choot
Lo, mera lund anpi behen ko de do, agar khud na chod paya
Lund Chus
Ma chudi
Mein teri maa ko teri bahen ki choot mein chodoonga aur tera baap laltern lekar aayega.
Mein teri maa ko liya tha uski suhaag raat pei.
Mera chunni choos
Meri lund choos
Mere Chuus Maro
Na choot, na chooche, nakhre noor jahan ke!
Raand ka pati
Rundi ko chod
Rundi ki tatti pe baithnewaali makkhi
Rundi ke tatti pe biathne wala makhi
Terey baad di gaand wich danda ghussa ker rakh dhungi.
Teri behen ka launda rubber ka 
Theri Biwi ko Tere Saamne Chodhunga
Teri Gand Mein Haathi Ka Lund
Teri gaand main kute ka lund
Tere gaand mein keede paday
Teri Jhanten Kaat kar tere mooh par laga kar unki french beard bana doonga.
Teri ma gandi rundi
Teri ma gadha ka lund choosay
Teri maa ki bimaar badboodar choot
Teri ma ki choot me hathi ka dum
Teri ma ki chut mai sabka lund
Teri maa ki phudi guy ki hai
Teri maa ka bhosda
Teri maa ki chute
Tere mai ki chut tere baap ka land
Teri mi di kussi mey tera sarra khandan ko ghussa ker rakh doonga.
Teri maa ki gaand ki baal mein jalaay hue, maarey hue chipkili ki unday.
Teri ma ki budh mein chaarpai bichhake teri bahen ko chodun.
Teri maa ki chut mein chatri leke ghus jaunga aur khol dunga.
Tere maa ko sau kutte chode - sau wa tera baap!
Tor mai ke chodho
aand
aandal
aandu
aandupana
abla naari tera buble bhaari
apni gaand mein muthi daal
apni lund choos
apni ma ko ja choos
backarchodu
badboodar choot
badir
badirchand
bahen chod
bahen ka loda
bahen ke laude
bahen ke takke
bahen ki choot
bahenchod
bahinchod
bahnchod
bakland
bakri chod
bakwaas
ban chod
banchod
banchood
bandaa
bandhar
ben chod
benchod
beti chod
bhadhava
bhadkhau
bhadwa
bhadwe ka awlat
bhai chod
bhains ki aulad
bhan chhod
bhanchod
bhandava
bhen chod
bhen ke laude
bhen ke takke
bhenchod
bhenchodd
bhonsri-waalaa
bhosad chod
bhosadike
bhosdaa very
bhosdi ka
bhosdi wala
bhosdika
bol teri gand kaise maru
booblay
buddha khoosat
buhtah-nee ka
bumchod
bund
bund maraa le
bur
bur ki chatani
carrom board
char soh bis
chhaati
chhed
chhola phudakna
chinaal
chinaal ke gadde ke nipple ke baal ke joon
chipkali ke chut ke pasine
chipkali ke gaand ke pasine
chipkali ke jhaat ke baal
chipkali ke jhaat ke paseene
chipkali ki bhigi chut
chodela
chodnaa to fuck 
chodra
chodu
chodu bhagat
choochi
choochii
choot
choot ka baal
chootad
chootadchod
chootia
chootiya
chootiyapa
chootiyapanti
chudaai
chudaai khaani
chudai
chudai khana
chudan
chudi
chudwana
chull uthna
chunni
chusnawal
chusnawala
chut
chut ka bhoot
chut ka pujari
chut ke dhakkan
chut ke gulam
chut ke pasine
chut marike
chutan
chutia
chutiya
chutiyapa
cuntmama
dhee chod
dhee ka lund
dheela lund
fate condom ka natije
fuddi pussy 
gaand
gaand asshole (definition) 
gaand ka makhan
gaand maarna to fuck in the ass 
gaand main danda
gaand main keera
gaand main lassan
gaand marau
gaand marna
gaand mein bambu
gaandfat
gaandkate kutte
gaandmasti
gaandu
gaandu asshole (person) 
gashti
gastee
gasti
ghassad
ghasti
ghelchodia
goti
gotiyan
gpl (gaand pe laat)
gundmaraa ass fucked (man) 
gundmari ass fucked (lady) 
haraam ka chuda son of unknown father 
haraam ki chudi fucked by someone other then husband. 
haraam zaada
haraami
haraamjaada son of unknown father 
haraamjaadi daughter
haraamkhor
hijda
hijdaa
hijde
hijra
hug
ing ge pan di kut teh
januwar
jhaant
jhaant ka baal
jhaant ke pissu
jhaant ukhaadna
jhaat chaatu
jhaat ka bhaaji
jhalla
jhant ke baal
jhat ke baal
kaamchor
kadak maal
kali choot ke safaid jhaat
kali chut ka safaid jhaat
kamina
katla
khade lund pe dhoka
khasmanu khaani
khota
khotey ki aulad
khotey ki aulda
klpd
kutchudi
kuthi for girl
kutiya
kutiya ke pilley
kutte ka aulad
kutte ka awlat
kutte ka beej
kutte ka lund
kutte ke pilley
kutte ke poot
kutte ke tatte
kutte ki jat
kuttiya
kya kadak hai ye
kya maal hai ye
ladkichod
landait
lavander
lavda
lavde
lavde ke baal
lavde ke bal
loda
lodu
londiyachod
lund
lund choos
lund choosu
lund chus
lund fakeer
lund fakir
lund ka bheja
lund ka shorba
lund ke pasine
lund pe chad ja
lund pe thand hai
lund 
lundoos
lundtopi
ma chudi
maa chudaa
maa ka bhosda
maa ke bable
maa ke bhadve
maa ke bhadwe
maa ke laude
maa ki choot
maa ki chut
maa ki phudi
maachod
maa-chod
maa-chut
maadarchod
maadher chod
maakichut
maal semen
mader chod
maha gaandu
mammey
mangachinamun
mast maal
momme
moot
mutar
muth maar
muth mar
muth marna
mutthal
na chhot
najayaz
najayaz paidaish
netrachodan mat kar
nimbu sharbat
paad
paadu kaun
paagal choda
padma
pancho
parichod
phatele nirodh ke natije
pisaab
pucchi
raand
raand ka jamai
raand ka pati
raandi baajer
raapchik
rakhail
rand chod
randhwa
randwa
rubber bhosda
rundee
rundi
rundi apni chut leka ana
rundi ka bacha
rundi khana
rundi ki bachi
rundi ko chowd
saala
saala kutta
saali kutti
sadi hui gaand
sali kuta
sali kutti
seal bund
seal pack virgin 
sewwer ki bachi
soover
soower ke bachche
suwwar
suwwar ka bachcha
suwwar ke lund
suwwar ki bachchi
suwwariya
tatte masalna
toota hua lund
tor mai ke chodho
ulloo choda stupid
ulloo ka patthaa
ullu ke pathe
undi
randi
raandi
randwe
harami
haram khor
haramkor
maa chod
maa chuda
maa chooda
maa ki aankh
randi ke
bc
bkl
muh me lele
maa ka bhosdaa
gandwe
gandwa
bhosdi wale
c***yapa
bosdi ke
bosdike
madarchood
big boobs
shake your boobs
sex boob
suck ur boobs
maderchod
xxx
are u slut
fuckyoself
laude
bhosda
chutiyapanti
bhnchooo
fuk u
chut loda
lun pakad lo
madarchod
ma ke lode
chooth
teri ma ka bamba
suck bitch
screw u
screw you
puccy
laudagiri
bhenchodh
madarchodh
choothiye
maa chudao
gaand mara
xdesi.com
xvideos.com
b***s
chutiyaapaa
bhenchodo
maaki chut
f@#* you
f... u
nice boobs
tere maa chodunga
amma chod
chinal log
chinal
fudu
fuddu
buckchod
lauda
maa chudaye
chudaye
randi k
gandu
jhaatu
jhatu
jhatoo
chussar
chup b bhosdike
bhosdi ke
bhosdi
maa ke lodey..
gand marao
behanchod
bhossdi k
maakilaudi
muth marke soja
muth marka soja
muth mar ke so ja
muth maar
boka choda
bhosdike
bakchod
backcgod
brest
cleavage
chudna
phudi
cutyiye
pennis
chu.t
backchod
hot clevage
clevage
gand
bhosadiwaale
bokachoda
nice cleavage
jhat
thode daba do
bosid***ke
band kar lav**d
bhaag bhanchode 
bhanchode
baag bachod ladki
bachod
cu**t
ch****ye
ban**chid
chu chu
bachchod
ga**ndo
machudao
chuchi
teri maa ki ***
chusss le
chu
chuu
b*nch*d*
cutiye
bosidike
boooooobbbbbssss
muh mae le
bakchodi
bh*sdike
raan*s
lole
bhdve
bahan ki chuat
maadr chaad
ga**nd
ga**
chuchu
chusaa hua
bosidike
teri maa ka saaki
f***ing
f***off
chup mc
bhosdiwaale
bhosdikee
aaand mat kaha
aand mat kaha
aandal
aandu
aandupana
abla naari tera buble bhaari
amma ki chut
andh
apna land choos
apna lund choos
apna ma ko ja choos
apni gaand mein muthi daal
apni land choos
apni lund choos
apni ma ko ja choos
asal ka chuda
baap ke lavde
backar chodu
backarchodu
backchod
badeer
badir
badirchand
bahen chod
bahen ka loda
bahen ke laude
bahen ke takke
bahenchod
bahinchod
bahu chod
bakchod
bakchod billi
bakland
baklol
baklund
bakri chod
bakrichod
balatkaar
banchod
bc
behan chod
behen chod
behen ka laura
behen ke land
behen ke laude
behen ke lawde
behen ke lund
behen ke take
behenchod
behenkelaude
behnchod
benchod
beti chod
betichod
bhaand me jaao
bhadhava
bhadva chodika
bhadwa
bhadwe
bhadwe ka awlat
bhadwe ki nasal
bhag bhosdike
bhai chhod bhayee chod
bhai chod
bhainchod
bhains ki aulad
bhais ke lund
bhais ki poonch
bhand khau
bhandava
bhandwe ki aulad
bhen chhod bhaynchod
bhen chod
bhen di fuddi
bhen ke laude
bhen ke lode
bhen ke lode maa chuda
bhen ke takke
bhen ki choot
bhencho
bhenchod
bhodhsike
bhonsriwaalaa
bhootnee ka
bhootnik
bhosad chod
bhosad raand
bhosadchod
bhosadi k
bhosadi ke
bhosadike
bhosadiwala
bhosda
bhosdaa
bhosdee kay
bhosdi
bhosdi k
bhosdi ka
bhosdi kalam
bhosdi ke
bhosdi wala
bhosdi wale
bhosdik
bhosdika
bhosdike
bhosdivaale
bhosdiwala
bhosdiwale
bhundi
bokachoda
bol teri gand kaise maru
booblay
boor
bsdk
buddha khoosat
buhtahnee ka
bulle ke baal
bumchod
bund
bund maraa le
bur
bur ka choda
bur ki chatani
burr
burr ke baal
bursungha
camina
cha cha chod
chachunder ki aulad
chhola phudakna
chhut ka baal
chinaal
chinaal ke gadde ke nipple ke baal ke joon
chinal
chipkai ki choot ke paseene
chipkali ke chut ke pasine
chipkali ke gaand ke pasine
chipkali ke jhaat ke baal
chipkali ke jhaat ke paseene
chipkali ki bhigi chut
chippkali ke jhaant ke paseene
chod ke bal ka kida
chodela
chodu bhagat
chooche
choochi
choochii
chood
choodasi
choodpagal
choohe ki moot
choot k bhoot
choot k pakode
choot ka baal
choot ka paani
choot ka pissu
choot ke bhoot
choot ke bhoot vaginal ghost
choot ki jhilli
choot marani ka
chootad
chootadchod
chootia
chootiya
chootiyapanti
chopre he randi
chudaai
chudaai khaana
chudaai khaani
chudai khana
chudail
chudan chudai
chudase
chudasi
chude
chudi
chudpagal
chudwana
chull uthna
chullu bhar muth mein doob mar
chup ke chut hai
chusnawala
chusnawali
chut
chut k dher
chut ka bhoot
chut ka maindak
chut ka nai
chut ka pujari
chut karo
chut ke baal
chut ke dhakkan
chut ke gulam
chut ke makkhan
chut ke pakode
chut ke pasine mein talay huye bhajiye
chut khujaane vaali
chut ki andhi
chut ki pyasi
chut mari ke
chut marike
chut se latka hua laude ka moot
chutan
chute
chutia
chutiya
chutiya chootia
chutiya ka bheja ghas khane gaya hai
chutiyah
chutiye
chuttad
chuttad chod
cuntmama
cutlkat lund
dalli
dhee chod
dhee ka lund
dheela lund
dheeli choot
dheli chut
dogla
fatay huay lundtopi ka
fatay huay lundtopi ka result
fate condom ka natije
fatey condom kay natije
fuddi
fudii k
gaand
gaand chaat mera
gaand gaand
gaand k baal
gaand ka baal
gaand ka khadda
gaand ka makhan
gaand ka pilla
gaand ke dhakan
gaand ki aulaad
gaand maar bhen chod
gaand maarna
gaand main danda
gaand main keera
gaand main lassan
gaand mara
gaand marau
gaand marna
gaand mein bambu
gaand mein kida
gaandfat
gaandkate kutte
gaandmasti
gaandu
gadha
gand mein danda
gand mein louda
gandi chut mein sadta hua ganda kida
gandi fuddi ki gandi auladd
gandkate kutte
gandmare
gandmasti
gandu
gandu saala
gandue
gashti
gastee
gasti
ghassad
ghasti
ghelchodia
ghondoo
gote
gote kitne bhi bade ho lund ke niche hi rehte hai
goti muh mein hai
gundmaraa
gundmari
hamari le rahe hai
haraam ka chuda
haraam ki chudi
haraam zaada
haraami
haraamjaada
haraamjaadi
haraamkhor
haram zaadaa
harami
harami ke pille
haramkhor
haramzaada
haramzade
harazyaada
havas
hazaar lund teri gaand main
hijdaa
hijde
hijra
hrami
hugna
hugnaa
jab tu paida hua tho aagey se ya peechey se nikla tha chutiya
jab tu paida hua tow aagey se ya peechey se nikla tha chutiya
janam jala
janam jali
januwar
janwar
jhaant
jhaant ka baal
jhaant ke jhature
jhaant ke pissu
jhaant ukhaadna
jhaat
jhaat chaatu
jhaat ka bhaaji
jhaat ke baal
jhaatoon saala
jhaatu
jhad jaana
jhandu
jhant chaatu
jhant ke baal
jhantu
jhat ke baal
jhat lahergaya
jhatoo
jhund
joo ke hagge
kaala lund
kaali kutti
kadak maal
kahe ko kha raha hai chut ki chapati aur lund ka beja?
kali choot ke safaid jhaat
kali chut ka safaid jhaat
kamina
kamine
kaminee
kaminey
katla
khade lund pe dhoka
khasmanu khaani
khota
khotey ki aulad
khotey ki aulda
khujju
klpd
kukarchod
kutchudi
kutha
kutha sala
kuthi
kuthri
kuthta buraanahe kandaa nahi pattaahe
kutiya
kutiya ke pilley
kutiyaa
kutta
kutte
kutte ka aulad
kutte ka awlat
kutte ka bachha
kutte ka beej
kutte ka lund
kutte ke aulaad
kutte ke pilley
kutte ke poot
kutte ke tatte
kutte ki aulad
kutte ki jat
kutte ki olad
kutti
kuttiya
kya kadak hai ye
kya maal hai ye
ladkichod
land ka bheja
landait
landue
landure
lauda
laudap
laude
laude ke baal
laude sale
lavda
lavde
lavde ka baal
lavde ke baal
lavde ke bal
lawda
lawde
lo mera lund anpi behen ko de do agar khud na chod paya
lo mera lund apni behen ko de do agar khud na chod paya
loda
lode jesi shakal ke
lode ke baal
lodey jaise shakal teri
lodu
loduu
londiyachod
lowde ka bal
lund
lund choosu
lund chus
lund chuse
lund fakeer
lund fakir
lund fekh ke maroonga toh tera poora khandan chud jayega chutmarike
lund k laddu
lund ka baal
lund ka bheja
lund ka shorba
lund ke pasine
lund khajoor
lund luhnd
lund mera muh tera
lund pe chad ja
lund pe thand hai
lund phek ke marenge khandan chud jayega
lundfakir
lundoos
ma chudi
maa chudaa
maa ka lauda
maa ke bable
maa ke bhadve
maa ke bhadwe
maa ke laude
maa ki aankh
maa ki choot
maa ki chut
maacho
maachod
maachodh
maadar chowd
maadarchod
maadher chod
maakelaude
maal
maal chhodna
maarey hue chipkili ki unday
machod
machodh
madar chod
madar jaat
madarchod
madarchod ke aulaad
madarchodh
madarjat
mader chod
madharchod
maha gaandu
mahder chod
mahderchod
mai chod
maichod
mamme
mammey mummaye
mangachinamun
mast maal
mc
mein teri maa ko liya tha uski suhaag raat pei
mein teri maa ko teri bahen ki choot mein chodoonga aur tera baap laltern lekar aayega
mein teri maa ko teri bhen ki choot mein chodoonga aur tera baap laltern lekar aayega
mera chunni choos
mera ganna mere dil se bada hai
mera gota moo may lay
mera lund choos
mera lungi me havas ki aag lagi hai
mera muhme le
mera mume le
mere chuus maro
mere fudi kha ley
mere pass nile rang ke gend hai
meri gand ka baal
meri gand ka khatmal
meri ghand ka baal
meri lund choos
meri lundh choos
mome ka pasina chat
moo may lay mera
moot
mooth marna
mootna
mu c waale
mujhe aap ki chut chahiye
mujhe aap ko chodna hai
mujhe aap ko thokna hai
mujhe chodne ki bhukh hai
mujhe chut chahiye
mujhe chut marni hai
mujhe ko chodna hai
mujhe tumhe chodna
mujhe tumhe thokna
mujhe usko chodna hai
mutar
muth maar
muth mar
muth marna
mutth marna
mutthal
na choot na chooche nakhre noor jahan ke
naali ka keeda
najayaz
najayaz paidaish
paagal choda
paagalchoda
parichod
phatele nirodh ke natije
phuddi
pig ki tatti
pille
raand
raand codha
raand ka jamai
raand ka pati
raand whore
raandi baajer
rakhail
rand
rand chod
rand ki moot
randawa
randhwa
randi
randi baj
randi chod
randi ka bachcha
randi ka choda
randi ka larka
randi ke baal
randi ke bacche
randi ke beej
randi ke dalal
randi ke jhaant ke toote hue baal
randi ki aulaad
randi ki aulad
randi ki chut
randuaa
randwa
randwe
rubber bhosda
rundee
rundi
rundi apni chut leka ana
rundi ka bacha
rundi ke tatti pe biathne wala makhi
rundi khana
rundi ki bachi
rundi ki tatti pe baithne waali makkhi
rundi ki tatti pe baithnewaali makkhi
rundi ko chod
rundi ko choud
rundi ko chowd
saala
saala betichod
saala kutta
saale
saali kutti
sab ka lund teri ma ki chut mein
sadi hui gaand
sadi hui gand
sala
sala kuttaa
sale
sali kuta
sali kutti
sardar fuda singh
seal bund
sewwer ki bachi
shali
sooar
soover
soower ki bachi
suar
suar ki tatti
sust lund ki padaish
suvar chod
suwar ki aulad
suwwar
suwwar ka bachcha
suwwar ke lund
suwwar ki bachchi
suwwariya
suyar ke baacho
tatte masalna
tatti tatte masalna
tei maa ki gaand me bhi
tera baap ki chut aur maa ke laude
tere adha nirodh mein rah gaya
tere baap ki chut mai teri maa ka land
tere baap ki gaand teri chute mai chuglee
tere gaand mein keede paday
tere maa ka bur
tere maa ko sau kutte chode sau wa tera baap!
tere maa ko sau kutte chode – sau wa tera baap
tere mai ki chut baap teri maa ka land
terey baad di gaand wich danda ghussa ker rakh dhungi
terey baad di gaand wich dhanda gussa ker rakdhungi
teri behen ka bhosda faadu
teri behen ka lauda rubber ka
teri behen ka launda rubber ka
teri behen ka lavda rubber ka
teri bhen ki gaand me ungli karunga
teri bhosri mein aag
teri biwiko teri saamne chodhunga
teri biwiko theri saamne chodhunga
teri gaand main kute ka lund
teri gaand me danda
teri gaand mein haathi ka lund
teri gand mai ghadhe ka lund
teri gand mein haathi ka lund
teri jhanten kaat kar tere mooh par laga kar unki french beard bana doonga
teri ma chadha ka lund choos
teri ma gadha ka lund choos
teri ma gandi rundi
teri ma ki budh mein chaarpai bichhake teri bahen ko chodun
teri ma ki bund mein chaarpai bichhake teri bhen ko chodun
teri ma ki choot me hathi ka dum
teri ma ki chut mai sabka lund
teri ma ko kutta chode
teri maa ka
teri maa ka bhosda
teri maa ka bhosra
teri maa ka boba chusu
teri maa ke bable
teri maa ke bhosade ke baal
teri maa ke bobe kha jaunga bhosdi ke
teri maa ki bimaar badboodar choot
teri maa ki choot
teri maa ki choot me hathi ka dum
teri maa ki choot me kutte ka lavda
teri maa ki chut
teri maa ki chut mai sabka lund
teri maa ki chut mein chatri leke ghus jaunga aur khol dunga
teri maa ki chute
teri maa ki gaand ki baal mein jalaay hue
teri maa ki gaand ki baal mein jalaay hue maarey hue chupkili ki unday
teri maa ki maari choot
teri maa ki phudi guy ki hai
teri maa ki sukhi bhos
teri maa ko chodun
teri mi di kussi mey tera sarra khandan ko ggussa ker rakhdoungi
teri mi di kussi mey tera sarra khandan ko ghussa ker rakh doonga
teri phuphi ki choot mein
tharki
theri biwi ko tere saamne chodhunga
toota hua lund
tor mai ke chodho
tu tera maa ka lauda
tum chutiya ho
ulloo choda
ulloo ka patthaa
ullu ke pathe
aand
aaand 
aandu
bakchod
balatkar
bc
beti chod
bhadva
bhadve
bhandve
bhootni ke
bhosad
bhosadi ke
bhosda
boobe
chakke
chinaal
chinki
chod
chodu
chodu bhagat
chooche
choochi
choot
choot ke baal
chootia
chootiya
chuche
chuchi
chudai khanaa
chudan chudai
chut
chut ke baal
chut ke dhakkan
chut maarli
chutad
chutadd
chutan
chutia
chutiya
gaand
gaandfat
gaandmasti
gaandufad
gandu
gashti
gasti
ghassa
ghasti
hagga
harami
haramzade
hawas
hawas ke pujari
hijda
hijra
jhant
jhant chaatu
jhant ke baal
jhantu
kamine
kaminey
kanjar
kutta
kutta kamina
kutte ki aulad
kutte ki jat
kuttiya
loda
lodu
lund
lund choos
lund khajoor
lundtopi
lundure
maa ki chut
maal
mc
madar chod
mooh mein le
mutth
najayaz
najayaz aulaad
najayaz paidaish
paki
raand
randi
saala
saala kutta
saali kutti
saali randi
suar
suar ki aulad
tatte
tatti
teri maa ka bhosada
teri maa ka boba chusu
teri maa ki chut
tharak
tharki
madrchod
bhnchod
aaand mat kaha 
aand mat kaha 
aandal 
aandu 
aandupana 
abla naari tera buble bhaari 
amma ki chut 
andh 
apna land choos 
apna lund choos 
apna ma ko ja choos 
apni gaand mein muthi daal 
apni land choos 
apni lund choos 
apni ma ko ja choos 
asal ka chuda 
baap ke lavde 
backar chodu 
backarchodu 
back chod 
backchod 
badeer 
badir 
badirchand 
bahen chod 
bahen ka loda 
bahen ke laude 
bahen ke takke 
bahenchod 
bahinchod 
bahu chod 
bakchod 
bakchod billi 
bakland 
baklol 
baklund 
bakri chod 
bakrichod 
behen chod 
behen ka laura 
behen ke land 
behen ke laude 
behen ke lawde 
behen ke lund 
behen ke take 
behenchod 
behenkelaude 
behnchod 
benchod 
beti chod 
betichod 
bhaand me jaao 
bhadhava 
bhadva chodika 
bhadwa 
bhadwe 
bhadwe ka awlat 
bhadwe ki nasal 
bhag bhosdike 
bhai chhod bhayee chod 
bhai chod 
bhainchod 
bhais ke lund 
bhandava 
bhen chod 
bhen ke laude 
bhen ke lode 
bhen ke lode maa chuda 
bhen ke takke 
bhen ki choot 
bhencho 
bhenchod 
bhodhsike 
bhonsriwaalaa 
bhootnee ka 
bhootnik 
bhosad chod 
bhosad raand 
bhosadchod 
bhosadi k 
bhosadi ke 
bhosadike 
bhosadiwala 
bhosda 
bhosdaa 
bhosdee kay 
bhosdi 
bhosdi k 
bhosdi ka 
bhosdi kalam 
bhosdi ke 
bhosdi wala 
bhosdi wale 
bhosdik 
bhosdika 
bhosdike 
bhosdivaale 
bhosdiwala 
bhosdiwale 
bhundi 
bokachoda 
bol teri gand kaise maru 
booblay 
boor 
bsdk 
buddha khoosat 
buhtahnee ka 
bulle ke baal 
bumchod 
bund 
bund maraa le 
bur 
bur ka choda 
bur ki chatani 
burr 
burr ke baal 
bursungha 
camina 
cha cha chod 
chachunder ki aulad 
chhola phudakna 
chhut ka baal 
chinaal 
chinaal ke gadde ke nipple ke baal ke joon 
chinal 
chipkai ki choot ke paseene 
chipkali ke chut ke pasine 
chipkali ke gaand ke pasine 
chipkali ke jhaat ke baal 
chipkali ke jhaat ke paseene 
chipkali ki bhigi chut 
chippkali ke jhaant ke paseene 
chod ke bal ka kida 
chodela 
chodu bhagat 
chooche 
choochi 
choochii 
chood 
choodasi 
choodpagal 
choohe ki moot 
choot k bhoot 
choot k pakode 
choot ka baal 
choot ka paani 
choot ka pissu 
choot ke bhoot 
choot ke bhoot vaginal ghost 
choot ki jhilli 
choot marani ka 
chootad 
chootadchod 
chootia 
chootiya 
chootiyapanti 
chopre he randi 
chudaai 
chudaai khaana 
chudaai khaani 
chudai khana 
chudail 
chudan chudai 
chudase 
chudasi 
chude 
chudi 
chudpagal 
chudwana 
chull uthna 
chullu bhar muth mein doob mar 
chup ke chut hai 
chusnawala 
chusnawali 
chut 
chut k dher 
chut ka bhoot 
chut ka maindak 
chut ka nai 
chut ka pujari 
chut karo 
chut ke baal 
chut ke dhakkan 
chut ke gulam 
chut ke makkhan 
chut ke pakode 
chut ke pasine mein talay huye bhajiye 
chut khujaane vaali 
chut ki andhi 
chut ki pyasi 
chut mari ke 
chut marike 
chut se latka hua laude ka moot 
chutan 
chute 
chutia 
chutiya 
chutiya chootia 
chutiya ka bheja ghas khane gaya hai 
chutiyah 
chutiye 
chuttad 
chuttad chod 
cuntmama 
cutlkat lund 
dalli 
dhee chod 
dhee ka lund 
dheela lund 
dheeli choot 
dheli chut 
dogla 
fatay huay lundtopi ka 
fatay huay lundtopi ka result 
fate condom ka natije 
fatey condom kay natije 
fuddi 
fudii k 
gaand 
gaand chaat mera 
gaand gaand 
gaand k baal 
gaand ka baal 
gaand ka khadda 
gaand ka makhan 
gaand ka pilla 
gaand ke dhakan 
gaand ki aulaad 
gaand maar bhen chod 
gaand maarna 
gaand main danda 
gaand main keera 
gaand main lassan 
gaand mara 
gaand marau 
gaand marna 
gaand mein bambu 
gaand mein kida 
gaandfat 
gaandkate kutte 
gaandmasti 
gaandu 
gadha 
gand mein danda 
gand mein louda 
gandi chut mein sadta hua ganda kida 
gandi fuddi ki gandi auladd 
gandkate kutte 
gandmare 
gandmasti 
gandu 
gandu saala 
gandue 
gashti 
gastee 
gasti 
ghassad 
ghasti 
ghelchodia 
ghondoo 
gote 
gote kitne bhi bade ho lund ke niche hi rehte hai 
goti muh mein hai 
gundmaraa 
gundmari 
hamari le rahe hai 
haraam ka chuda 
haraam ki chudi 
haraam zaada 
haraami 
haraamjaada 
haraamjaadi 
haraamkhor 
haram zaadaa 
harami 
harami ke pille 
haramkhor 
haramzaada 
haramzade 
harazyaada 
havas 
hazaar lund teri gaand main 
hijdaa 
hijde 
hijra 
hrami 
hugna 
hugnaa 
jab tu paida hua tho aagey se ya peechey se nikla tha chutiya 
jab tu paida hua tow aagey se ya peechey se nikla tha chutiya 
janam jala 
janam jali 
januwar 
janwar 
jhaant 
jhaant ka baal 
jhaant ke jhature 
jhaant ke pissu 
jhaant ukhaadna 
jhaat 
jhaat chaatu 
jhaat ka bhaaji 
jhaat ke baal 
jhaatoon saala 
jhaatu 
jhandu 
jhant chaatu 
jhant ke baal 
jhat ke baal 
jhat lahergaya 
jhatoo 
jhund 
joo ke hagge 
kaala lund 
kaali kutti 
kadak maal 
kahe ko kha raha hai chut ki chapati aur lund ka beja? 
kali choot ke safaid jhaat 
kali chut ka safaid jhaat 
kamina 
kamine 
kaminee 
kaminey 
katla 
khade lund pe dhoka 
khasmanu khaani 
khota 
khotey ki aulad 
khotey ki aulda 
khujju 
klpd 
kukarchod 
kutchudi 
kutha 
kutha sala 
kuthi 
kuthri 
kuthta buraanahe kandaa nahi pattaahe 
kutiya 
kutiya ke pilley 
kutiyaa 
kutta 
kutte 
kutte ka aulad 
kutte ka awlat 
kutte ka bachha 
kutte ka beej 
kutte ka lund 
kutte ke aulaad 
kutte ke pilley 
kutte ke poot 
kutte ke tatte 
kutte ki aulad 
kutte ki jat 
kutte ki olad 
kutti 
kuttiya 
kya kadak hai ye 
kya maal hai ye 
ladkichod 
land ka bheja 
landait 
landue 
landure 
lauda 
laudap 
laude 
laude ke baal 
laude sale 
lavda 
lavde 
lavde ka baal 
lavde ke baal 
lavde ke bal 
lawda 
lawde 
lo mera lund anpi behen ko de do agar khud na chod paya 
lo mera lund apni behen ko de do agar khud na chod paya 
loda 
lode jesi shakal ke 
lode ke baal 
lodey jaise shakal teri 
lodu 
loduu 
londiyachod 
lowde ka bal 
lund 
lund choosu 
lund chus 
lund chuse 
lund fakeer 
lund fakir 
lund fekh ke maroonga toh tera poora khandan chud jayega chutmarike 
lund k laddu 
lund ka baal 
lund ka bheja 
lund ka shorba 
lund ke pasine 
lund khajoor 
lund luhnd 
lund mera muh tera 
lund pe chad ja 
lund pe thand hai 
lund phek ke marenge khandan chud jayega 
lundfakir 
lundoos 
ma chudi 
maa chudaa 
maa ka lauda 
maa ke bable 
maa ke bhadve 
maa ke bhadwe 
maa ke laude 
maa ki aankh 
maa ki choot 
maa ki chut 
maacho 
maachod 
maachodh 
maadar chowd 
maadarchod 
maadher chod 
maakelaude 
maal 
maal chhodna 
maarey hue chipkili ki unday 
machod 
machodh 
madar chod 
madar jaat 
madarchod 
madarchod ke aulaad 
madarchodh 
madarjat 
mader chod 
madharchod 
maha gaandu 
mahder chod 
mahderchod 
mai chod 
maichod 
mamme 
mammey mummaye 
mangachinamun 
mast maal 
mc 
mein teri maa ko liya tha uski suhaag raat pei 
mein teri maa ko teri bahen ki choot mein chodoonga aur tera baap laltern lekar aayega 
mein teri maa ko teri bhen ki choot mein chodoonga aur tera baap laltern lekar aayega 
mera chunni choos 
mera ganna mere dil se bada hai 
mera gota moo may lay 
mera lund choos 
mera lungi me havas ki aag lagi hai 
mera muhme le 
mera mume le 
mere chuus maro 
mere fudi kha ley 
mere pass nile rang ke gend hai 
meri gand ka baal 
meri gand ka khatmal 
meri ghand ka baal 
meri lund choos 
meri lundh choos 
mome ka pasina chat 
moo may lay mera 
moot 
mooth marna 
mootna 
mu c waale 
mujhe aap ki chut chahiye 
mujhe aap ko chodna hai 
mujhe aap ko thokna hai 
mujhe chodne ki bhukh hai 
mujhe chut chahiye 
mujhe chut marni hai 
mujhe ko chodna hai 
mujhe tumhe chodna 
mujhe tumhe thokna 
mujhe usko chodna hai 
mutar 
muth maar 
muth mar 
muth marna 
mutth marna 
mutthal 
na choot na chooche nakhre noor jahan ke 
naali ka keeda 
najayaz 
najayaz paidaish 
paagal choda 
paagalchoda 
parichod 
phatele nirodh ke natije 
phuddi 
pig ki tatti 
pille 
raand 
raand codha 
raand ka jamai 
raand ka pati 
raand whore 
raandi baajer 
rakhail 
rand 
rand chod 
rand ki moot 
randawa 
randhwa 
randi 
randi baj 
randi chod 
randi ka bachcha 
randi ka choda 
randi ka larka 
randi ke baal 
randi ke bacche 
randi ke beej 
randi ke dalal 
randi ke jhaant ke toote hue baal 
randi ki aulaad 
randi ki aulad 
randi ki chut 
randuaa 
randwa 
randwe 
rubber bhosda 
rundee 
rundi 
rundi apni chut leka ana 
rundi ka bacha 
rundi ke tatti pe biathne wala makhi 
rundi khana 
rundi ki bachi 
rundi ki tatti pe baithne waali makkhi 
rundi ki tatti pe baithnewaali makkhi 
rundi ko chod 
rundi ko choud 
rundi ko chowd 
saala 
saala betichod 
saala kutta 
saale 
saali kutti 
sab ka lund teri ma ki chut mein 
sadi hui gaand 
sadi hui gand 
sala 
sala kuttaa 
sale 
sali kuta 
sali kutti 
sardar fuda singh 
seal bund 
sewwer ki bachi 
sooar 
soover 
soower ki bachi 
suar 
suar ki tatti 
sust lund ki padaish 
suvar chod 
suwar ki aulad 
suwwar 
suwwar ka bachcha 
suwwar ke lund 
suwwar ki bachchi 
suwwariya 
suyar ke baacho 
tatte masalna 
tatti tatte masalna 
tei maa ki gaand me bhi 
tera baap ki chut aur maa ke laude 
tere adha nirodh mein rah gaya 
tere baap ki chut mai teri maa ka land 
tere baap ki gaand teri chute mai chuglee 
tere gaand mein keede paday 
tere maa ka bur 
tere maa ko sau kutte chode sau wa tera baap! 
tere maa ko sau kutte chode ñ sau wa tera baap 
tere mai ki chut baap teri maa ka land 
terey baad di gaand wich danda ghussa ker rakh dhungi 
terey baad di gaand wich dhanda gussa ker rakdhungi 
teri behen ka bhosda faadu 
teri behen ka lauda rubber ka 
teri behen ka launda rubber ka 
teri behen ka lavda rubber ka 
teri bhen ki gaand me ungli karunga 
teri bhosri mein aag 
teri biwiko teri saamne chodhunga 
teri biwiko theri saamne chodhunga 
teri gaand main kute ka lund 
teri gaand me danda 
teri gaand mein haathi ka lund 
teri gand mai ghadhe ka lund 
teri gand mein haathi ka lund 
teri jhanten kaat kar tere mooh par laga kar unki french beard bana doonga 
teri ma chadha ka lund choos 
teri ma gadha ka lund choos 
teri ma gandi rundi 
teri ma ki budh mein chaarpai bichhake teri bahen ko chodun 
teri ma ki bund mein chaarpai bichhake teri bhen ko chodun 
teri ma ki choot me hathi ka dum 
teri ma ki chut mai sabka lund 
teri ma ko kutta chode 
teri maa ka 
teri maa ka bhosda 
teri maa ka bhosra 
teri maa ka boba chusu 
teri maa ke bable 
teri maa ke bhosade ke baal 
teri maa ke bobe kha jaunga bhosdi ke 
teri maa ki bimaar badboodar choot 
teri maa ki choot 
teri maa ki choot me hathi ka dum 
teri maa ki choot me kutte ka lavda 
teri maa ki chut 
teri maa ki chut mai sabka lund 
teri maa ki chut mein chatri leke ghus jaunga aur khol dunga 
teri maa ki chute 
teri maa ki gaand ki baal mein jalaay hue 
teri maa ki gaand ki baal mein jalaay hue maarey hue chupkili ki unday 
teri maa ki maari choot 
teri maa ki phudi guy ki hai 
teri maa ki sukhi bhos 
teri maa ko chodun 
teri mi di kussi mey tera sarra khandan ko ggussa ker rakhdoungi 
teri mi di kussi mey tera sarra khandan ko ghussa ker rakh doonga 
teri phuphi ki choot mein 
tharki 
theri biwi ko tere saamne chodhunga 
toota hua lund 
tor mai ke chodho 
tu tera maa ka lauda 
tum chutiya ho 
ulloo choda 
ulloo ka patthaa 
ullu ke pathe
Bewarsi
Mukli muchkondu kutko
Mukli tuth
Rande
Randi magane
Saak thika muchappa
shraddha
Soole Maga
Tulla
Aab
baaz akh de
babba aasus manz choosni
babbe kache chatai
bablyaath
be lakhay beni
beni gooud
Beni lakhai
beyani goood
bh lakhai che
Brahman chaenk
Chaaan
chakij
chakjeh goud
Chapin
che chui mazze lakhnas
Choti travi marchevangan
Chotul
chwath
Dagaddalli maa de bacheio
Dawa woal
diyanawaan
duniyah che khap
Fhalaan
fis
Gaan
gaani bach
Gees
ghain
Gooid prah
Goudi Sawaer
guude
Ha kole madarchoda
Hahra
haramuk
Hasna
Haspataal
houn goudiuk
kani jung
Khade daez
khape chraethe
khapkhap
Kucher
laith
langan dimay darith
lazmai bene
lazmai goudis
Lazmaiye Mael Sinze Kori
Lazmayi babbun
lazmie lyath
Lechmayaa benzi
Lezmaye Lyaath
liyath chani goodis
lyaath
lyath kal
lyathee kale
Lyathh
Ma lakh goudis
maaji gooud
maaji lakhai
maeji guudh
maeji lyaath
maelis lakhai
mambre kalle
Meethir
Momri Kalle
MUAMD
Mumer
Mye kya zok kadkhe
Naer
Pael
phutyaa poon
ponas lakhai
ponas manz chu chout kieom
Ponne Tecczh
Poon
poonus lakhai
rath mein lyath
sa here tok mi haijla
Sabzi woal
Seel tuluai
seous good
Siiech
Sous
Taech
tche che baji bab
thapi karani
Watul
Zakal ponz
Zang
Zinhook
zoake goodh
zok
zokke poan
Zokkk
Gandah kullah pudha
Gandhu
Gandhu bastar
Hanzeer da puthar
Jannay na puthar
Kalayah
Khotah
Khotay da puthar
Kuttah
Kuttay na puthar
Kutthi
Lan choop
Lofar
Mammay
May thara pudha marsah
Nikki lan
Pahari ki aulad
Pudhu goray
Randi na puthar
Yadeenah
Aavoi Zovno
Avoichi/Maichi Fudh
baakri
babak zovnya
Babay Aand
bainik zovnya
bewarshi
Bhikarchot
Bhokan bot
Bokan bot
Chedi
Chedye kastachya
Chedyecho
Chont
Chontli
Colwont
daba daba
Fodo
Fodri
Fuddri
Fude
Gaand
Gadith
ganDi bot gaali
gandi ke bot davari
GanDi votto
Guru
kick your ass
maari
Maichi fud
masti pisso
minni
momme
momo
moshye fudd
muje bonk lew
paadu
Popoot
Potachea
Potnechya
rande puth
Randecho
Shent
shet maar pilluk
sunna manngo
sunne jati che
Tu Zovlo Khubyakarnicha chedvak
Tu Zovlo Khubyakarnik
tugile gaandi
Tujya Baye Fodo
ubyani zhovta
zhenge
Zonyachea
zov babak
Zov Bai
zov rangyak
amaa fui
Amaa fui
Amaa handhaan kurey
amaa thalhaa
Badi
Buri Loa valhu
Fada boe
Fada boey
Fada Thiki
Fatha folhi
magey foah boe
mani boe
Nagoo balhu
nagoobalhu
"Ninde ama, pati!"
Aaana kunna
aan-vedi
achante andi
Achinga Kunnan
adichu poli
Ajoli ka Thajoli
ammaudi pootil poocha
amminhnha
Andi pidiyan
anna kunna
appikunna
arraykku chuttum poorruu ullaval
avaraathi
avarathi mone
chalam nakki
Chandi
Chokka lingam
coondi
Da patti
eli kunna
Ettukali Patti Pooran
inchi mola
johninte andi
kaatu poori
kallel oouuki
kandara oli
kandi
kandi theeni
Kandu
Kanni
Kanni mola
kara vedi
karim kunna
karim pooran
katta thayoli
kazhappu perutha mairan
Keepu
Kettal
kodam nakiii
Kolekkeri
Koothara
Koothi
Koothichi
kotham
kotham kalakki
kotham nakku
Koyimani
kuch
kulamavuka
kundan
kundaroli poori mone
Kundi
Kundi mon
Kundi oota
kundimol
kunji kunnan
kunna
Kunna
kunna chappu
Kunna Oli
Kunna paal
Kunna thayoli
kunna urunji
kunnappal
kushukk
Lick Me
malayalam
Maratel ooki
Masa
Mattanga Poore
Mayiradi mon
Mlechan
mola
moonchikko
Mula Adi
mula chappu
mula kashakku
mula mol
Myir
Myre
Myrru
Naayi meedan
nayinte mone
Nayinte Mone
Nayinte Monne
ninde andi maire
Ninte ama koondi ishtima
Ninte ammakku vettu nayinte mone
Ninte ammaku vetu
ninte ammeda tar
Ninte Ammede Kothil.
ninte ammede pooru
Ninte ammede thenga mairu
ninte appante andi
Odu myre
ookki
oomban
oombi mon
Oooomb
Ootan
paara pooru
paareel ookki
Pacha tayolli
Pachila Pooran
Paik keriko myra
paiku vetti
pala thanthakkundaya thaoli
pallinedayil kanthu
pambara kutichi
pampara thayoli
panchavarna kunna
pandi kallan
panniyoli
para andi oomba
Para kutichi
para thayoli punda mon
parii
pathala poor
patti poori mon
patty theettam
Pela molichi
Pela vedi
pela vedi kandaroli
petty
Pezhachu Pettavan
Poda Thayoli
podda Patti
pola vettu
poochi
Pooranddi
poore ennayil tenni veetil poda
Poori mone
Poorri
Pooru
pooru
Pooru Montha
poottaavi
poottile mathycurry
poyi ninte kunna oombadaa
poyi oombada
praa thayolli
Puchi
pudti puliyadi
Pulayadi monae
pundachi mone
Purusha Vedi
rainayude poore
Santhosh Pandit
Shukla mughan
shuklam dheeni
shuklam nakki
Takkali pooru
Thaayoli
thabala pooran
thakara thayoli
Thallayoli
Thalleyoli
thayolee
thayoli
Thayoli
thayoli idli
Thayoli idli
Theetam
theetta moran
theettam
theettathel ookki
THENGA MYRE
Thenga pooru
Thevadichi
Thokolli kalla sami
Thukal Kunna
umman
vada
Vadam vali
vali
Vayilitto
vedi
vedi pura
vedi vekkuka
Veppatti
veshya / veshi
vettukili
Viral Iduka
vouvalinu undaya thayoli
aai chi gand
Aai ghalya
aai javada
aaichya gavat pay
Aandya
ai zawlee
akkar mashi
Aye Jhaatu
ayica dana
Badak Zawarya
Bhadavya
Bhikaar Chot
Bhosada
Bin gotyaachya
Bulli chokya
Chhaiyla
Chhinal
Chinaal maichya
chinal
chut marichya
Chut Marichya
fodri pisaat
Fodricchya
fokanchidy
Foknicha
Gand khaya
Gand phatli bhenchod
Gandit Ghuslo
Gandoo
Gav Zawadi
Hepari
Jhavadya
Kanadal
khargatya gandicha
Khullya lavdyacchya
lal gandya
Laudu
Lavadya
Lingapisat
madarchod
madarchoth
marathi
Muttha
Paadar Gandichya
pachi bota bhundyat
phodarphatya
Phodree Pisat
Pucchi Khajvya
puchi
Raandichya
Randechya
Shanya lavdyacchya
shata ki chutney
shattya
Shebnya
Telkat Randi
tondaat gay
tujha aila kutryawani zawin
tuji ai mutli madkyat phala-phala
Tuji aiee chi gaand
Tujya aaicha puchha
tuza baap dhandewala
tuzi aai padli madkyat
tuzi aai padli tuzya tondat
tuzua aaichi pucchi viskatli 40 ekrat
Tuzya aai chi Phodree
tuzya aaicha foda
tuzya aaicha lavda
tuzya aaichi gand
tuzya aaichi pucchi
tuzya aaichya gandit mungya
tuzya aaichya pucchila chavla kutra
tuzya aaichya pucchila chavla sap
tuzya aaila zavla kala kutra
Tuzya aii zavneya tuzya baapla
Tuzya bapacha pay adakla sandasat.
Tuzya gaandit paay
Yadzava
yadzavya
Yeda lavdya
zavadya
Zavkhor
zavnya
Adarsha
Bandar Ko Chaak
beshya
Bhalu
bhalu ko poi
Bhalu lai chik muji
chaak ko pwal
chahk
chahk ko dulka
chak cha
Chaman
Chick-day
Chickne
condo
condo hannay
Dhoti
dudh
fushi kha
Gadha
gand faat cha
Geda
Gidi Haps
goo kha
Goo kha
goo khai-ra morr
Gula chus randi
gula kha
Jantha
Kando
Kangres
Kukkur
kukur chikni
laando kha
lado
Lado
Lado chus
lado cocha
Lado kha
Lado ko tuppo
lamto
Lang Lang
ma shaala
maa chikney!
Maa chikni
Maa Rondi!
Machikne
Madhesi
mandale
maobadi
mero fushi kha
moot
mootday
moreko
moreko manchi
Morr Sali Morr!
morryo
Mugi
Muji
murda
muzy
pahadi
pinko
Prachanda
Puti Chat Chu
puti kha
puti ko jhol
Putin Chaat
radi ko puti
Randi ko baan
Randi ko Ban
randi ko choro
randiko choro
sungghur
turi tauke
Tutturay
ABHADRA
Baanda
Bada bou ghia
banda
Banda
banda chhod
Banda mundi
BARBARA
Batakara (pela)
bedha bia
Bedha toka
Bedha Toke
bedhei
Bedhei pua
bhauni giha
bia fata mada
bia ku darkar jaghanya gihan
Biaa
Bija
Biya chudi
Bujula
chodipua
chukiba
dana
Faizan
fusa chata
fusa kura
Gaandiaa
gandi
Gandi gia
Gandi Mara Sankara
Gandire Banda
Gayee de
gehiba
Ghoda Gehin Pua
Ghoda Ghein Bedha Toke
Ghusuri ghiaa
Goola gandha
gosti gian
Guola
Hagura magia
Han ta nalire goithe
hinjada
hinjida
Laathi biya re kaathi
Maa bia ra pua
Maa ghia
Maa gia
maagya
madarchaut
Mankada ghiya
mankada giha
mo priya ra bia re lagichi nia!!!!!
Mo Priya ra Gandi re Niya
Moro banda chaape
Mu tomo bhallo pauchu
Muuthi mara magia
naani bia re ghian
Nanna gia
PASANDA
Pela
Pela phata maada
pelei pua
Pelei pua
Pelei Puo
PUDI
randa (Pronounce Ra as robbery not as rabbit
Randa ku banda dhamakani
Randi puo
senti
Senti
Tate Gehibi
Thoola phata maada
To bhauni bia re ghia
To bou BIA
To Gandire Ghien
To Gandire Mo Banda
To Maa Bia re ghein
To Maa Biya Re Ghen
To maa ku gihe
to maa ku kukur gaheun
To Maipa Biaare gihen
To Maipa Biaare Gihen
To Maipa Gandi maribi
To Maipa Gandire gihen
bakvas
bhen chod
Choohi
Fudu
Haram Jaada
kalan
kudi chod
Kuri yani
kuri yawa
Kuthe Di Poosh
Kuthe Kambakhte
Laaaaauvre
Lan di Jhoon
lun tay charja
Lun te Waj
Momay
Pan chod
peyu di gand vich ungal
Phuddy
soor da lora
teri maa di fudi
Teri paan di chiter
Teri pan di lun
tutoo
Tutti
Bagul butcha
Bewakoof
Bhen da shola
Bhen Da Yaar
Bhenchod
Bhenchode
bhonsdu
Bibi di fudi
bokki
Bondu
bondu
bund
Bund
bund de
Bund Mara
Bund marr
chaval
Chitta Bander / Kalla Bander
Chitterchort
choos mera badaam
chutha
Chutiyaa
chuttiya
dallah
Dhila lan de padiash
Fooduu
fuddi hayon da
fudi
Fudi chut
Fudi da tataa
fudi fry karna
fudi hyounda
gand
gandu
Gandu
ganndu
Gashti
ghashti
haram da
harami saale
Haramjada
Jaa apne braah nu chod laa
kala lulla pi
kanjar
Kanjar
Kanjari
Kenjer
Khota
kissey kuti ma da puttar
Klatch
Kuta
kuta
Kutha
kuthay da puthar
Kuthi
kuti
Laan tare mow nee
lan chat
lan choos
Lauda
Lul
lula bahonder tup
lula chooshe
Lun
Lun choos
Lun Chung
Lun kurra how gaya
lun te charrh
Lund
Lund Chuss
Lunni
Ma chod
ma di podi
maa-jhouda
Maan Da Yaar
MaanChod
Mamai
Mamai Chuss
mamai patta
mango
mao ni puddi
matarchod
Mau ni yakk
Meh tera tueh vich aangliyan devan
Menu zor nal lan mar
Mera lan sakht ah
Mera lan tera tueh ki paarsi
Mera lun choos ta aangly mar
mera lund teri bund de betch
mere lund tey charr ke nach!
Meri Tutti Kha
Mume
Muth Maar
nuts ko suck kurrow
pad mar
Pan da yaar
Panchod salaa
Peshaab
phen chodtha
poo
Pud
Puddu
Pudhi avandeya
Pudi
randi
soor
Tatte
tatte chaude
tatte fad lo
tatte hayon da
taxi
Teri Bhen Dee Fuddi Mari
teri bhen di ghusi
teri bund ch lakad
Teri bund marni aa
teri fudi wich lul marya
Teri ma da ghusa
Teri ma di khali phudi
Teri ma the fudi
teri maa da fudda
teri maa da posrha
Teri maa dai ccholay
teri maa dee tutee swaad ya
Teri maa di gandi phuddi
Teri Maa Di Koosii Kay Uppar !
teri maa di pudi vich lath
teri maa nu lund
Teri Maan Dee Fuddi Mari
teri paan dee lund
Teri paan di fudi parrne
teri paen nu lan
Teri pain dha pahraya hoya phudda
teri pen da pudda
terri ma di fuid parne
topa
Topa
Topa te beja
Tu Bhen Da Yaar
Tu Maan Da Yaar
tu vich leni daa.
Tutta
Tuttay
Guddha naku
Guddha pagala dengutha
aathulu
aathulu peeku
aathulu peekutha
Aati Mokka
akka bokka lO naa sulla
akka nee pooku dengutha
amma pooku ki baanisa
amma pooku lo arati pandu
ATTHA POOKU DENGINA ALLDU
bochu
Bosudi
chilipiga thittatam
Chitthu Pooka
Dengithe dayyalu pudatai
Dengu
doola lanja
Gaadida Pichaloda
Gaja madda
golli cheeku ra kodaka
golli chekutha lanja
Gudda
gudda
gudda naaku
Hasta Prayogam chai
Jinniappa
kammani pooku
Kojja
Konamodda
kukka -pooka
kukka sulli
Kuthuru vongudu..alludu dhengudu
LANGA VIPPAVAE LANJAA
lanja
lanja - kodka
Lanja munda
lanja pooka
Lanjakodka
Marmangam
Modda
modda cheeku lanja
MODDA KUDUVU
modda naaku
modda notlo petti dengutha
modda, lavada, daddu, magatanam
muchchika, chanu mona
muddy lo velu petuko
naa modda gudu
Ne akka nu denga
ne akkan ma kukka dengha
Ne amma pukkulo naa modda
ne jathini kukka denga
ne notlo naa suli
Ne pookula na sulli
Nee aali pookulo Rampam
NEE AKKAANI DENGAA
nee akkanu denga
NEE ALINI DENGAA
nee amma guddani denga
nee amma kuttani denga
Nee amma roju na modda cheekuthundi
NEE AMMANI DENGAA
nee ammanu denga
nee ammanu dnegu
nee kooturu ni denga
nee notlo naa sulli
nee pallu super
nee pellaanni denga
nee pooku chekutha
nee pukulo naa sulli
Ni akkani pandulu denga
Ni pukla na madda
nihar
Nihar (or) banda pooku
ninnu dengutha
Nuvvu nee yendipoyina sulli
PEDDA SALLADHI
Pichi Pukoda
Pichi Pukudaana
Poi voungu ra
Pooku
pooku
pooku, dimma, pappa, bokka
Poooku chinchu
pukku naaku
Puku Peka adistha
puthhi
sachinoda
sallu dengutha
SANALO BOCHHO
shaata
Sravan (or) konda verri pooku
sulii
Sulli pattu
Teja (or) adivi pooku
Teja trivikram (or) adivi pooku
thurku valagodtha
Vattakai
vattalu
Vedhava
verri puka
vongo petti dengutha lanja
aaja choos mera lurs
Aap ka aana
apna lun cuti shur
Balal, mera noonoo na choop se
Behn ki chutar
Bhadwe Ki Nasal
bhai chode
Bhen chot
Bhen ke lorray
bosard chodi kay
Bund ke Biryani
chatt merai tattai
Choom meri Gaand
Choos Mera Lora
chooth kay pakoray
choti se luli
Chupa la lay
Chut ke chatney
dalla
dari moni pudi mari
deli mali guti
doe dolla raandee
Duffah oja
eik dolla raande
gaand chamchi
gaand ka bukhaar
Gaddha
ghandoo
Ghasti Kay Bachay
haraam salle
Haraamzada
Haraamzadi
haram salla
jhaant kay baal
kaala bandar
Kamina
kanjeri kay bachay
Khuss madri kay
kute liche ho chublo
kutee chode
kutta
Kuttay ka bacha
kutte ka ghanta
Kutti
kutti ka bacha
lalchi kutte kaa bacha
Lola/Lula
looly
lora le kay nach mera
Lula mu ki lan
lulmuah
Lun Chuse
Lund Pe Charh
Maan Chod
Maan kay laurday
madarugly
Mather chot
Mayyaada
meera loora choo so
meli mali guta
mera laan choop
monney podey
moomeh
muth ki malai
Myyaada
pancho
peasah nah mahr
Phudi
poody
Randee ka bacha
Randi ki nasal
rundi ka bacha
Shudra Lund
Tamil Lund
tari beh na puda paarsan
Tattay chooso
tattee choad
tere bhen meri chod hain
tere gand maroo
Teri Gaand Main Kutta Mutre
teri gand ma keera hai
teri gand mera lun hai
teri ma khuti
Teri Ma ki choot
Teri Ma Ko Kuttey Chodein
teri maa ki phudi
Toomaray tattay baraay pahraay heh
tu tho meri chod ki tara :P
Uloo Ki Pata
Uloo Ki Pati
ulu chod
abu gidir
Bazari
Bima khoigra
Bima khoygra
Bimani fishai
Bwitali
Cfa swlangra
Hinjao maogra (khoigra)
khilama
Khoynai
Lwdwi
Nwma shifa
Nwmani abu
Sifa gudung
Sifa jagra
sifa jagra
Sifa swlagra
Sikwmwn
maari tatoori ne chalay
Akbaruddin Owaisi
Alloo Bhosri Chaat
Anuj
Babhuchak
bai no bhosdo
bein chod
Benchod
Bhadvo
bhenchod
Bhoot
Bhopa
Bhos marina
Bhosad Pappu
bhosdo
bhosrini
bobla
Bobla Vagarni Baydi
Bosrichord
bosrina
Buckwass
Budhalal
chafu gaan
Chichi
Chod
Chod ami
Chodhru
chodkanya
Chodu
chupri lauri
Chutiya
Darshil
Dheela Lund Ni Olaad
Eapen
Fattu
gaan tari
Gaand Ghapli
Gaand Ma Ghal
gaandina, gandina
Gand nu kaanu
gandi chodina
gando
Gando salo
gel ghagharina
Ghel Chodyo
Ghelchoydi
Halki Raand na
Harsh Dalal
harshit
hopa
Huzefa
jaaro
Jhadhino!
Jignesh Mevani
karo loro
kem chho
kutari
Lakhota
Land
loda
lodde mari
Lowroh
luli
Lund Bhagat
Maa ne ghat bhosdina
maajaddha
maari tatoori ooper bess
maasi chodamno
Madachod
madachod
mandi susee
Manik
mara man no lado
mari bhosri chaat
meri gaan chatt
Mohit
Moht
mota jijah
nago choido
Nakhodiya
Namuno
Narender Modi
pikina
Pikina
pim pim
poom poom
Priyanshu
puchi chod
Puti
raand
rumana
sali
salu gut`ti
Sandas
suwwar jewu dachu
taari bai no aghano
Taari ma parasevo tya-reh e tuti kareh che!
Tara baap ni gaan
Taree gaar ma lowroh
Taree Ghaar Ma Doh Ladah
tari bosri kaapi karwa
tari dagri
tari gaand mare karya kutra balada
tari gandayli kari koyli dagri
Tari ma na bubla sukai-gya
tari ma ne hadi kadhto hathi chode
tari ma ni putti
tari ma no poplo
Tari maa na babla chusu
Tari maa na bhosda ma maro lodo
Tari maa na modha ma maro lodo
Tari maa ne chodu
Tari maa ni taturi
tari mai ni gand
tari mani choot ma derka bole
Taro baap tane chadeche
tere ma nu hinta kar
teree maah gaderi
thari ma ne bozro maro loro nakhides
Thari Ma Ni Ghaan
Tusat
Tutelli nirodh no aulad
Andoo
behenien khe yahan
Bhairain jo yaar
Bharain khe
Bharvo
Bhavesh
Bhen ja chud
Bherain khe
Budhi muhandro
Charyo
Chora
Chora / Chori
Chud
Chud Budhi jo
Chud muhandro
chutia
Chutoon
Dallo
gui jo tung
Guii / Gaand
Jadija
kakus
Kutey ja putta
lalli
Lun choop
Lun khao
Lun muhandro
Maa ja chud
maa ji teeta
Madar chot
Marhain jo yaar
Marhain khe
Marhen khe yahan
Mujhko aapka bur chahiye
neech
Pelo / Pela
Pelorray
Pirhain ji yaar
Pirhain ji yaar (adding "Jo" will make the Paramour masculine)
Pirhain khe
ran yadho
Ranayadha
Randi jo putr
Sagro muo
Teetay main
punda/pundai
poolu
ommapunda
thevdiyapaiya
okka/kokka
ommala oka
pundai
sunni
mayir/mayiru
oombu
kena pundai
akkula thukki kami di
kuthi
anaathai kaluthai
arivu ketta koothi
avuthu kami
baadu
chunni
ennoda poola oombuda 
okka kudi
kaai
kaai adithal
kala viridi
ki adi
koothi mayir
kuthi kolutha thevdia
kuthia virikira thevdia
molaikku naduvule uttu okka
molaikku naduvule utu olu da
okkala ozhi
ommala oka
ommala
onkka pundek
kunju
panni
pavadaiyathukkikamidi
pisasu
poolu
pooluarunthapundamavan
puluthi
puluthi punda
puluthinapoolaumbudi
pundamavale
pundavaaya
pundaamavane
pundainakki
pundainakki
pundayenakku
soothu
suththu
sunni
sunniyaoombu
suthaa
thaiyoli
thangathevdia
thevidiya pulla
thevidiya mavale
thotha pundai
thevadiyamavan
thevdiyakuthi
thoomiyakudiki
thevdiyakuthileuttapoolu
thevdiyapaiya
thoronthukamidi
thukkikami
ungaaayakuthi
vaaila vaangu
vesi
viruchu kaami
arippueduthakuthimavale
auvusaarikoodi
gajakkol
kalaiviridi
kandaaraoli
karungkuthimavale
keeshanappa
kenapunda
koodhi
koodhipayale
koothinuckie
kudiyabaadu
kundi
kundimudi
kunjipayalae
kusukoodhi
kuthimudiyathadavikamidi
loosukoodhi
mairupudungi
malamattupunda
mayirupoodunghi
molasappi
mollamaari
monnanaaye
mairaandi
muttaakoodhi
naarakoodhi
pudungi
nayeesoothileunkunji
oakkauttabaadu
okkalaoli
olithebengali
olmaari
oluthapundai
ongappanpundai
oogili
oombu
oora otha thevidiya
oorthevidya
oka
oththa
oolu
kuthi
paepunda
kenakuthi
potta punda
parapundamaune
padukka pottu okka
parathesi punda
patchathevidiya
pochu pundai
pochchu
poolpayya
poolu
thevudiya 
avusaari
pullusappi
puluthi
pundamavanae
pula chappu
pula umbu
oththa punda
sakkiliakoodhi
sappi
selayaithukkudi
vaaila vachuruven
sunniya umbu
pundaiya moodu
mola
molai
thevdiya
thevidiya
thevidiyapundai
molaya amukava
naara punda
okkala okka
vailevatchuko
ommala pottu okka
monna pundai
kai mutti
para punda
ommala okka
kai adiki
munda kalappa
otha
vaaila vaangu
arivu ketta mundam
Baah Khuwa
Baal
baal kela
baal khuruwa
baaperor konitu
baaperor pukorkhon
Bal
Bandor Chod
Bari
Bengena Mora
billa suda
bimakho khoigra
boinaak sudaai
boiner lalak
boithali
buch seleka
Bush
Bush mara
Bushot tel diya
Chet
ekka she duuka
fifa ni lodoi
Fuck Dang Fo!
gar mora
Gida
Gida Khua
Gu
Gu Khuwa
guu kha
guu kha mokkel
Jairir badcha
Jhaant singa
johoni jua
Johora
Jonghol
Kela
Keti
Koti Mara
Kotit bari homai dim
Kukur'or puwali
laura
Lauri ke bal
Lothou Guti
Ludoi
Maaeror Boos, maksudai
Maaeror fof khon
maak sudai
Maaror bhumikhon kela
maka dingding
maka linglang
Maksaai
mangmarani
Meeyarek Kohai
Mumu
Nagori putek
Naliya
Pel suha
Pheda cheleka
Pokorot Kothal Bhoram
pukor selek
raandii
Randir soli
Rendi Dallal
Rendir Beta
Rendy Suda
Set Suda
setor baal
sipha jagra
Sudasudi
Sudi Gida Falidim
Sudur Bhai
sut marani
syetor moila
Tez piya
Tumak sudibor mon goise
tur maak sudu
Tur Maak Sudu
Tur maraok rastat kukur logi sudam..
"""

words = s.split('\n')
for word in words:
    lst = Leet2Combos(word)
    print(''+"\n".join(lst))
