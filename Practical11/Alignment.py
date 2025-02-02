cat=''.join('''MSGSFWLLLSFAALTAAQSTTEELAKTFLEKFNHEAEELSYQSSLASWNYNTNITDENV
QKMNEAGAKWSAFYEEQSKLAKTYPLAEIHNTTVKRQLQALQQSGSSVLSADKSQRLN
TILNAMSTIYSTGKACNPNNPQECLLLEPGLDDIMENSKDYNERLWAWEGWRAEVGK
QLRPLYEEYVALKNEMARANNYEDYGDYWRGDYEEEWTDGYNYSRSQLIKDVEHTFT
QIKPLYQHLHAYVRAKLMDTYPSRISPTGCLPAHLLGDMWGRFWTNLYPLTVPFGQKP
NIDVTDAMVNQSWDARRIFKEAEKFFVSVGLPNMTQGFWENSMLTEPGDSRKVVCHP
TAWDLGKGDFRIKMCTKVTMDDFLTAHHEMGHIQYDMAYAVQPFLLRNGANEGFHE
AVGEIMSLSAATPNHLKTIGLLSPGFSEDSETEINFLLKQALTIVGTLPFTYMLEKWRW
MVFKGEIPKEQWMQKWWEMKREIVGVVEPVPHDETYCDPASLFHVANDYSFIRYYTR
TIYQFQFQEALCRIAKHEGPLHKCDISNSSEAGKKLLQMLTLGKSKPWTLALEHVVGEK
KMNVTPLLKYFEPLFTWLKEQNRNSFVGWNTDWRPYADQSIKVRISLKSALGDEAYE
WNDNEMYLFRSSVAYAMREYFSKVKNQTIPFVEDNVWVSNLKPRISFNFFVTASKNVS
DVIPRSEVEEAIRMSRSRINDAFRLDDNSLEFLGIQPTLSPPYQPPVTIWLIVFGVVMGVV
VVGIVLLIVSGIRNRRKNNQARSEENPYASVDLSKGENNPGFQHADDVQTSF'''.split())
human=''.join('''MSSSSWLLLSLVAVTAAQSTIEEQAKTFLDKFNHEAEDLFYQSSLASWNYNTNITEENV
QNMNNAGDKWSAFLKEQSTLAQMYPLQEIQNLTVKLQLQALQQNGSSVLSEDKSKRL
NTILNTMSTIYSTGKVCNPDNPQECLLLEPGLNEIMANSLDYNERLWAWESWRSEVGK
QLRPLYEEYVVLKNEMARANHYEDYGDYWRGDYEVNGVDGYDYSRGQLIEDVEHTFE
EIKPLYEHLHAYVRAKLMNAYPSYISPIGCLPAHLLGDMWGRFWTNLYSLTVPFGQKPN
IDVTDAMVDQAWDAQRIFKEAEKFFVSVGLPNMTQGFWENSMLTDPGNVQKAVCHP
TAWDLGKGDFRILMCTKVTMDDFLTAHHEMGHIQYDMAYAAQPFLLRNGANEGFHE
AVGEIMSLSAATPKHLKSIGLLSPDFQEDNETEINFLLKQALTIVGTLPFTYMLEKWRW
MVFKGEIPKDQWMKKWWEMKREIVGVVEPVPHDETYCDPASLFHVSNDYSFIRYYTR
TLYQFQFQEALCQAAKHEGPLHKCDISNSTEAGQKLFNMLRLGKSEPWTLALENVVGA
KNMNVRPLLNYFEPLFTWLKDQNKNSFVGWSTDWSPYADQSIKVRISLKSALGDKAYE
WNDNEMYLFRSSVAYAMRQYFLKVKNQMILFGEEDVRVANLKPRISFNFFVTAPKNVS
DIIPRTEVEKAIRMSRSRINDAFRLNDNSLEFLGIQPTLGPPNQPPVSIWLIVFGVVMGVI
VVGIVILIFTGIRDRKKKNKARSGENPYASIDISKGENNPGFQNTDDVQTSF'''.split())
mouse=''.join('''MSSSSWLLLSLVAVTTAQSLTEENAKTFLNNFNQEAEDLSYQSSLASWNYNTNITEENA
QKMSEAAAKWSAFYEEQSKTAQSFSLQEIQTPIIKRQLQALQQSGSSALSADKNKQLNTI
LNTMSTIYSTGKVCNPKNPQECLLLEPGLDEIMATSTDYNSRLWAWEGWRAEVGKQLR
PLYEEYVVLKNEMARANNYNDYGDYWRGDYEAEGADGYNYNRNQLIEDVERTFAEIK
PLYEHLHAYVRRKLMDTYPSYISPTGCLPAHLLGDMWGRFWTNLYPLTVPFAQKPNID
VTDAMMNQGWDAERIFQEAEKFFVSVGLPHMTQGFWANSMLTEPADGRKVVCHPTA
WDLGHGDFRIKMCTKVTMDNFLTAHHEMGHIQYDMAYARQPFLLRNGANEGFHEAV
GEIMSLSAATPKHLKSIGLLPSDFQEDSETEINFLLKQALTIVGTLPFTYMLEKWRWMVF
RGEIPKEQWMKKWWEMKREIVGVVEPLPHDETYCDPASLFHVSNDYSFIRYYTRTIYQ
FQFQEALCQAAKYNGSLHKCDISNSTEAGQKLLKMLSLGNSEPWTKALENVVGARNMD
VKPLLNYFQPLFDWLKEQNRNSFVGWNTEWSPYADQSIKVRISLKSALGANAYEWTN
NEMFLFRSSVAYAMRKYFSIIKNQTVPFLEEDVRVSDLKPRVSFYFFVTSPQNVSDVIPR
SEVEDAIRMSRGRINDVFGLNDNSLEFLGIHPTLEPPYQPPVTIWLIIFGVVMALVVVGIII
LIVTGIKGRKKKNETKREENPYDSMDIGKGESNAGFQNSDDAQTSF'''.split())

BLOSUM62 = '''A  4  0 -2 -1 -2  0 -2 -1 -1 -1 -1 -2 -1 -1 -1  1  0  0 -3 -2
C  0  9 -3 -4 -2 -3 -3 -1 -3 -1 -1 -3 -3 -3 -3 -1 -1 -1 -2 -2
D -2 -3  6  2 -3 -1 -1 -3 -1 -4 -3  1 -1  0 -2  0 -1 -3 -4 -3
E -1 -4  2  5 -3 -2  0 -3  1 -3 -2  0 -1  2  0  0 -1 -2 -3 -2
F -2 -2 -3 -3  6 -3 -1  0 -3  0  0 -3 -4 -3 -3 -2 -2 -1  1  3
G  0 -3 -1 -2 -3  6 -2 -4 -2 -4 -3  0 -2 -2 -2  0 -2 -3 -2 -3
H -2 -3 -1  0 -1 -2  8 -3 -1 -3 -2  1 -2  0  0 -1 -2 -3 -2  2
I -1 -1 -3 -3  0 -4 -3  4 -3  2  1 -3 -3 -3 -3 -2 -1  3 -3 -1
K -1 -3 -1  1 -3 -2 -1 -3  5 -2 -1  0 -1  1  2  0 -1 -2 -3 -2
L -1 -1 -4 -3  0 -4 -3  2 -2  4  2 -3 -3 -2 -2 -2 -1  1 -2 -1
M -1 -1 -3 -2  0 -3 -2  1 -1  2  5 -2 -2  0 -1 -1 -1  1 -1 -1
N -2 -3  1  0 -3  0  1 -3  0 -3 -2  6 -2  0  0  1  0 -3 -4 -2
P -1 -3 -1 -1 -4 -2 -2 -3 -1 -3 -2 -2  7 -1 -2 -1 -1 -2 -4 -3
Q -1 -3  0  2 -3 -2  0 -3  1 -2  0  0 -1  5  1  0 -1 -2 -2 -1
R -1 -3 -2  0 -3 -2  0 -3  2 -2 -1  0 -2  1  5 -1 -1 -3 -3 -2
S  1 -1  0  0 -2  0 -1 -2  0 -2 -1  1 -1  0 -1  4  1 -2 -3 -2
T  0 -1 -1 -1 -2 -2 -2 -1 -1 -1 -1  0 -1 -1 -1  1  5  0 -2 -2
V  0 -1 -3 -2 -1 -3 -3  3 -2  1  1 -3 -2 -2 -3 -2  0  4 -3 -1
W -3 -2 -4 -3  1 -2 -2 -3 -3 -2 -1 -4 -4 -2 -3 -3 -2 -3 11  2
Y -2 -2 -3 -2  3 -3  2 -1 -2 -1 -1 -2 -3 -1 -2 -2 -2 -1  2  7'''.split('\n')

for i in range(len(BLOSUM62)):
    BLOSUM62[i] = BLOSUM62[i].split()

m={}
for i in range(len(BLOSUM62)):
    for j in range(1, len(BLOSUM62[0])):
        m[BLOSUM62[i][0] + '\t' + BLOSUM62[j-1][0]] = BLOSUM62[i][j]

#calculate scores
#human and mouse
t=[[0]]
for n in range(1, len(human)+1):
    t[0].append(n*(-5))
for i in range(1, len(mouse)+1):
    t.append([i*(-5)] + [0]*len(human))
    for j in range(1, len(human)+1):
        if mouse[i-1] == human[j-1]:
            t[i][j] = t[i-1][j-1] + int(m[mouse[i-1]+'\t'+human[j-1]])
        else:
            t[i][j] = max(t[i-1][j]-5, t[i][j-1]-5, t[i-1][j-1]+int(m[mouse[i-1]+'\t'+human[j-1]]))
print("mouse and human:", t[len(mouse)][len(human)])

#human and cat
t=[[0]]
for n in range(1, len(human)+1):
    t[0].append(n*(-5))
for i in range(1, len(cat)+1):
    t.append([i*(-5)] + [0]*len(human))
    for j in range(1, len(human)+1):
        if cat[i-1] == human[j-1]:
            t[i][j] = t[i-1][j-1] + int(m[cat[i-1]+'\t'+human[j-1]])
        else:
            t[i][j] = max(t[i-1][j]-5, t[i][j-1]-5, t[i-1][j-1]+int(m[cat[i-1]+'\t'+human[j-1]]))
print("cat and human:", t[len(cat)][len(human)])

#cat and mouse
t=[[0]]
for n in range(1, len(cat)+1):
    t[0].append(n*(-5))
for i in range(1, len(mouse)+1):
    t.append([i*(-5)] + [0]*len(cat))
    for j in range(1, len(cat)+1):
        if mouse[i-1] == cat[j-1]:
            t[i][j] = t[i-1][j-1] + int(m[mouse[i-1]+'\t'+cat[j-1]])
        else:
            t[i][j] = max(t[i-1][j]-5, t[i][j-1]-5, t[i-1][j-1]+int(m[mouse[i-1]+'\t'+cat[j-1]]))
print("mouse and cat:", t[len(mouse)][len(cat)])

#calculate percentages
iden = 0
for i in range(len(mouse)):
    if mouse[i]==human[i]:
        iden+=1
print("mouse and human:", iden/len(human))

iden = 0
for i in range(len(mouse)):
    if mouse[i]==cat[i]:
        iden+=1
print("mouse and cat:", iden/len(human))

iden = 0
for i in range(len(cat)):
    if cat[i]==human[i]:
        iden+=1
print("human and cat:", iden/len(human))
