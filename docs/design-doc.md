# Rise of Animals: Ages of Earth (Eras da Terra) — Documento de design

Status: fase de ideias (nenhum arquivo do jogo alterado)
Repositório: github.com/trizdev/ron-ages-of-earth (privado)
Base: Rise of Animals (24 nações viram espécies; visual fiel ao RoN com toque fofo)

## Conceito
As 8 eras do Rise of Nations viram eras geológicas, em ordem. Pode ter animais pré-históricos. Possível mod separado no Workshop.

## Eras (proposta inicial, texto do jogo em inglês)
| # | Era do RoN | Era geológica | Nome no jogo |
|---|---|---|---|
| 1 | Ancient | Pré-cambriano | The Pre-cram-brian Age |
| 2 | Classical | Cambriano | The Cam-bring-it Age |
| 3 | Medieval | Devoniano | The Fin-tastic Devonian |
| 4 | Gunpowder | Carbonífero | The Car-bone-iferous Age |
| 5 | Enlightenment | Triássico | The Triassic Dawn |
| 6 | Industrial | Jurássico | The Jurass-kick Age |
| 7 | Modern | Cretáceo | The Cre-tail-ceous Age |
| 8 | Information | Cenozoico | The Zen-ozoic Age |

## Restrições técnicas
- Publicação via gerenciador de mods do jogo (pasta mods, layout data/*.xml).
- Só substituir: sem nações, unidades ou tecnologias novas.
- Texturas .tga (GIMP); modelos novos só com 3ds Max 5, então o padrão é reaproveitar modelos com textura, nome e ícone novos.

## Regras da Microsoft (Game Content Usage Rules)
Gratuito, sem anúncios, sem engenharia reversa, sem PI de terceiros, doações opcionais ok. Aviso obrigatório:
"Rise of Animals: Ages of Earth was created under Microsoft's "Game Content Usage Rules" using assets from Rise of Nations, © Microsoft Corporation."

## Perguntas em aberto
- Conferir os bônus reais de cada nação no mapeamento antes de fechar as habilidades.
- Confirmar se dá pra trocar só o texto das eras mantendo o hash.

## Nome do mod (decidido 17/10/2026)
**Rise of Animals: Ages of Earth**
Descartados: Evolution Edition; Pangaea (conflita com o tipo de mapa Pangaea do jogo e com mapas no Workshop).

## Arquivos das eras (segundo o mapeamento do bot Rise of Animals, ainda não testado)
- Nomes das eras: Data/typenames.xml; menus de partida: Data/string_lookup.xml.
- Ancient Age não tem identificador próprio; Classical a Information ficam em techrules.xml.
- Hipótese: manter o hash e trocar só o texto (precisa testar).
- Referências: /workspace/rise-of-animals/mapeamento-jogo.md e design-doc.md (seção 26 tem as eras "natureza" da versão principal).

## Decisão: unidades evoluem com as eras (17/10/2026)
Igual ao Rise of Nations, cada linha de unidade troca de visual a cada era. Cada espécie continua a mesma, mas a "roupinha" muda conforme a era geológica (ex.: carapaça de trilobita no Cambriano, folhas de samambaia gigante no Carbonífero, escamas e espinhos no Jurássico). Tudo via textura nova nos modelos existentes.

## Decisão: espécies são bichos pré-históricos (17/10/2026; lista abaixo substituída pelas Nações v1)
Rascunho v0.1 (aguardando a Ana):
Trilobite (The Trilo-bite Empire), Anomalocaris (Anomalo-carisma), Ammonite (The Ammo-nite Republic), Dunkleosteus (Dunk-leosteus Dynasty), Tiktaalik (Tik-Tok-taalik), Meganeura (The Mega-neura Hive), Arthropleura (Arthro-pleura Legion), Dimetrodon (Dime-trodon Bank), Coelophysis (Coelo-physics Academy), Plateosaurus (Plate-osaurus Kitchen), Ichthyosaurus (Ichthyo-sore-us Navy), Stegosaurus (The Steg-gosaurus Spikes), Brachiosaurus (Brachio-sore-us Heights), Pterodactyl (Ptero-dactyl Wings), Archaeopteryx (Archae-opteryx Air), Triceratops (Tri-cera-tops), T. rex (The T-Rex-public), Velociraptor (Veloci-rapture), Ankylosaurus (Ankylo-sore-us Fortress), Mosasaurus (Mosa-sore-us Tides), Mammoth (The Mam-moth Kingdom), Saber-tooth (Saber-tooth Sultanate), Giant sloth (Sloth-topia), Glyptodon (Glypto-dome).
Atenção: evitar "Tik-Tok" no nome final se parecer PI de terceiros.

## Como as espécies evoluem (resolvido: linhagens evolutivas, ver abaixo)
- Opção A, linhagens evolutivas: cada nação é uma linhagem real, e as unidades viram o descendente seguinte a cada era (ex.: peixe com mandíbula, Tiktaalik, réptil, dinossauro, ave). Ideia: agrupar as 24 nações em 6 a 8 grandes linhagens.
- Opção B, bichos fora do tempo: a espécie é a mesma do começo ao fim, e só a roupinha da era muda.
A Ana escolheu a opção A.

### Exemplo comparativo (linhagem até as aves)
| Era | A: linhagem | B: fora do tempo (T. rex) |
|---|---|---|
| Pré-cambriano | bichinho mole tipo verme | pele de tapete microbiano |
| Cambriano | Haikouichthys | carapaça de trilobita |
| Devoniano | peixe encouraçado com mandíbula | placas ósseas e barbatanas |
| Carbonífero | anfíbio primitivo | folhas de samambaia gigante |
| Triássico | Coelophysis | escamas simples |
| Jurássico | Archaeopteryx | espinhos e placas |
| Cretáceo | raptor de penas | forma clássica |
| Cenozoico | ave-do-terror | pelagem estilo era do gelo |

## O mapa tem que fazer sentido com as eras (resolvido pela regra de coerência biológica)
O terreno do RoN não muda com a era (a confirmar com o mapeamento). Ideias: (1) terreno "de praia" primitivo (rochas, lagoas rasas, algas, tapetes microbianos) que serve pra todas as eras, com a vegetação nova só nas unidades e construções; (2) nas primeiras eras as unidades ficam perto da água, e a vida em terra firme só fica forte a partir do Devoniano e Carbonífero. Sugestão: combinar os dois. Visual: realista, sem toque fofo.

### Achados no Data/tilesets.xml (leitura no laptop, 17/10/2026)
- O terreno base é fixo por tileset (17: Snowy, Dirty, Dirty_2, autumn, early_autumn, late_autumn, SW_Desert, GS_Desert, jungle, tropical, tropical_wet, african_savannah, arctic, m_steppe, m_steppe_2, m_steppe_3, m_steppe_autumn), escolhido por mapa; não muda com a era.
- Mudam com a era, mas só em 3 estágios: estradas (Early/Middle/Late_Road), o chão embaixo das construções (ALPHAELEM age0/age1/age2) e o calçamento em volta (WEATHERELEM com atributo age).
- Ideia: repintar os 17 tilesets como biomas pré-históricos (mar raso, pântano carbonífero, deserto triássico, floresta de coníferas jurássica, campos com flores do Cretáceo, estepe gelada do Cenozoico) e usar os 3 estágios das estradas e do chão das cidades pra mostrar a vida tomando a terra.

## Regra de coerência biológica (17/10/2026, aprovada pela Ana)
- Bichos aquáticos (peixes, amonites, répteis marinhos) viram só unidades navais, nunca de terra.
- Nas primeiras eras, as unidades de terra são bichos que se arrastavam fora d'água: artrópodes, vermes de lama e depois anfíbios primitivos.
- Como qualquer nação pode jogar em qualquer mapa: a biologia segue a era, não o mapa; os tilesets viram biomas pré-históricos genéricos (litoral rochoso, lodaçal, deserto, floresta de samambaias, tundra), que não são presos a uma época; as 3 etapas das estradas e do chão das cidades mostram a vida colonizando o terreno.
- Limitação aceita: não é 100% fiel à ciência, porque nações em eras diferentes convivem na mesma partida.

## Decisão: linhagens evolutivas (17/10/2026)
Rascunho v0.1 de 8 linhagens × 3 nações, todas sobreviventes até o Cenozoico:
1. Aves: verme > peixinho primitivo > peixe encouraçado > anfíbio primitivo > Coelophysis > Archaeopteryx > raptor de penas > ave-do-terror
2. Mamíferos: verme > cordado > peixe de nadadeiras carnudas > anfíbio > cinodonte > mamífero pequeno > Repenomamus > mamute/dentes-de-sabre
3. Crocodilos: raiz comum > répteis do Triássico > crocodilos terrestres > Sarcosuchus
4. Tartarugas: répteis primitivos > tartarugas gigantes
5. Lagartos e cobras
6. Anfíbios: salamandras gigantes do Carbonífero > primeiras rãs
7. Insetos: Pré-cambriano > trilobita > Meganeura > besouros > formigas e abelhas
8. Aracnídeos: escorpiões-do-mar > escorpiões gigantes > aranhas
Grandes dinossauros como unidades especiais (Jurássico/Cretáceo). Navios: peixes, tubarões, amonites, répteis marinhos.

## Distribuição das nações v2 (aprovada pela Ana, 18/10/2026, conferida com os poderes reais)
1. Aves: Mongols, Lakota, Bantu (migração + caças Hawk/Eagle Fighter)
2. Mamíferos: Russians, Indians, Persians (os dois dividem a mesma unidade de elefante e textura)
3. Crocodilos: Egyptians, Nubians, Dutch (comércio de rio e navios)
4. Tartarugas: Chinese, Koreans, Maya (prédios mais resistentes)
5. Lagartos e cobras: Aztecs, Incas, Iroquois (unidades escondidas no território)
6. Anfíbios: British, Japanese, Spanish
7. Insetos: Romans, Germans, Americans
8. Aracnídeos: Turks, Greeks, French

## Nações v2: bicho-símbolo e nome (18/10/2026)
| Linhagem | Nação RoN | Bicho-símbolo | Nome no jogo |
|---|---|---|---|
| Aves | Mongols | Velociraptor | The Veloci-Horde |
| Aves | Lakota | Ave-do-terror | The Terror-tory |
| Aves | Bantu | Argentavis (ave gigante voadora) | The Wing-tu Kingdom |
| Mamíferos | Russians | Mamute | The Mam-moth-erland |
| Mamíferos | Indians | Deinotherium (elefante pré-histórico) | The Tusk Raj |
| Mamíferos | Persians | Paraceratherium (rinoceronte gigante) | The Im-mammal Empire |
| Crocodilos | Egyptians | Sarcosuchus | The Nile-osaurus Dynasty |
| Crocodilos | Nubians | Deinosuchus | The Deino-Nubian Kingdom |
| Crocodilos | Dutch | Purussaurus | The Nether-snaps |
| Tartarugas | Chinese | Meiolania (tartaruga com chifres) | The Great Shell of China |
| Tartarugas | Koreans | Proganochelys | The Turtle-ship Kingdom |
| Tartarugas | Maya | Stupendemys | The Maya Shell-ter |
| Lagartos e cobras | Aztecs | Titanoboa | The Boa-ztec Empire |
| Lagartos e cobras | Incas | Megalania | The In-claw Empire |
| Lagartos e cobras | Iroquois | Gigantophis | The Hiss-roquois League |
| Anfíbios | British | Mastodonsaurus | The United King-frog |
| Anfíbios | Japanese | Salamandra-gigante | The Salamander Shogunate |
| Anfíbios | Spanish | Beelzebufo (rã gigante) | The Frog-quistadors |
| Insetos | Romans | Titanomyrma (formiga gigante) | The Ant-perium Romanum |
| Insetos | Germans | Besouro | The Beetle Confederation |
| Insetos | Americans | Abelha | The United Bee-states |
| Aracnídeos | Turks | Escorpião gigante | The Scorpi-Ottoman Empire |
| Aracnídeos | Greeks | Escorpião-do-mar | Arachn-Athens |
| Aracnídeos | French | Aranha | The Web-public of France |
Obs.: a unidade de elefante compartilhada por Indians e Persians vira o Deinotherium nas duas nações.

## Linhagens era por era v1 (aprovadas pela Ana, 18/10/2026)
Ordem: Pré-cambriano | Cambriano | Devoniano | Carbonífero | Triássico | Jurássico | Cretáceo | Cenozoico
Raiz comum dos vertebrados: verme bilateral primitivo | Pikaia | Tiktaalik/Acanthostega (primeiros a sair na margem)
1. Aves: verme | Pikaia | Tiktaalik | Hylonomus (1º réptil) | Coelophysis | Archaeopteryx | Velociraptor | ave-do-terror/Argentavis
2. Mamíferos: verme | Pikaia | Acanthostega | Archaeothyris (1º sinapsídeo) | Thrinaxodon (cinodonte) | Morganucodon | Repenomamus | mamute/Deinotherium/Paraceratherium
3. Crocodilos: verme | Pikaia | Tiktaalik | Hylonomus | Postosuchus | Protosuchus | Sarcosuchus/Deinosuchus | Purussaurus
4. Tartarugas: verme | Pikaia | Tiktaalik | Hylonomus | Proganochelys | Kayentachelys | Basilemys | Meiolania/Stupendemys
5. Lagartos e cobras: verme | Pikaia | Tiktaalik | Hylonomus | Megachirella (1º escamado) | Eichstaettisaurus | Najash (cobra com patas) | Titanoboa/Megalania/Gigantophis
6. Anfíbios: verme | Pikaia | Acanthostega | Proterogyrinus | Triadobatrachus (proto-rã) | Prosalirus (1ª rã saltadora) | Beelzebufo | salamandra-gigante
7. Insetos: artrópode primitivo de lama | Marrella | Rhyniognatha (1º inseto) | Meganeura | besouro primitivo | vespa primitiva | primeiras formigas e abelhas | Titanomyrma
8. Aracnídeos: artrópode primitivo de lama | Sanctacaris | trigonotarbídeo (1º aracnídeo terrestre) | Pulmonoscorpius | aranha primitiva | Mongolarachne | aranha tecelã | escorpiões e tarântulas
Pré-cambriano e Cambriano: toda a vida era marinha; as unidades de terra dessas eras são bichos de poça de maré e litoral, e o terreno da cidade nessas etapas é lodaçal úmido.
Textura: as 6 linhagens de vertebrados dividem as 3 primeiras eras (verme, Pikaia, Tiktaalik/Acanthostega), o que economiza arte; insetos e aracnídeos dividem a primeira.
Pikaia no Cambriano (aprovado pela Ana, 18/10/2026): todas as linhagens de vertebrados usam a Pikaia (cordado tipo enguia que se arrasta no lodo de maré) nas unidades de terra do Cambriano. O Haikouichthys fica só para navios e uso naval.

## Unidades únicas v1 (aprovadas pela Ana, 18/10/2026)
Fonte das eras: `PREQ0` de cada unidade em `unitrules.xml` (cópia em /workspace/ron-data). `none` = disponível desde o início (Ancient = Pré-cambriano). Armed Caravan/Merchant saem do Market, que só pede Barter (tecnologia Ancient). Regras: navios só bichos aquáticos; unidades de terra do Pré-cambriano e Cambriano são bichos de poça de maré e lodaçal (no Cambriano dos vertebrados, Pikaia; Haikouichthys só em navios); voadores usam bicho voador da linhagem quando existe.

### Aves
| Nação | Unidade original | Era | Bicho | Nome no jogo |
|---|---|---|---|---|
| Mongols | Nomad | Cambriano (Classical) | Pikaia | Mud-omads |
| Mongols | Steppe Nomad | Devoniano (Medieval) | Tiktaalik | First Steppe Nomad |
| Mongols | Horde | Carbonífero (Gunpowder) | Hylonomus | Hylo-Horde |
| Mongols | Golden Horde | Triássico (Enlightenment) | Coelophysis | Golden Coelo-Horde |
| Lakota | Sunka Wakan | Cambriano (Classical) | Pikaia | Sunka Wa-slime |
| Lakota | Eagle Feather Horse | Devoniano (Medieval) | Tiktaalik | Eagle Fin-ger Crawler |
| Lakota | Musket Horse | Carbonífero (Gunpowder) | Hylonomus | Musk-scute Runner |
| Lakota | Repeating Rifle Horse | Triássico (Enlightenment) | Coelophysis | Repeating Rifle-physis |
| Bantu | Umpakati | Pré-cambriano (Ancient) | verme | Wormpakati |
| Bantu | Yangombi Umpakati | Cambriano (Classical) | Pikaia | Yangombi Pikakati |
| Bantu | Impi | Devoniano (Medieval) | Tiktaalik | Limb-pi |
| Bantu | Hawk Fighter (avião) | Cretáceo (Modern) | Ichthyornis (ave voadora) | Ichthy-Hawk Fighter |
| Bantu | Eagle Fighter (avião) | Cenozoico (Information) | Argentavis | Argent Eagle Fighter |
Obs.: no Cretáceo a linhagem tem Velociraptor, que não voa; o Hawk Fighter usa Ichthyornis, ave voadora da mesma linhagem e época.

### Mamíferos
| Nação | Unidade original | Era | Bicho | Nome no jogo |
|---|---|---|---|---|
| Russians | Rusiny Lancer | Devoniano (Medieval) | Acanthostega | Ru-spiny Lancer |
| Russians | Cossack | Carbonífero (Gunpowder) | Archaeothyris | Archaeo-Cossack |
| Russians | Don Cossack | Triássico (Enlightenment) | Thrinaxodon | Thrinaxo-Don Cossack |
| Russians | Red Guards Infantry | Cretáceo (Modern) | Repenomamus | Repeno-Red Guards |
| Russians | Katyusha Rocket (artilharia) | Cretáceo (Modern) | Repenomamus | Repeno-Katyusha |
| Russians | Shock Infantry | Cenozoico (Information) | mamute | Woolly Shock Infantry |
| Russians | T80 Tank | Cenozoico (Information) | mamute | T-80 Tusk |
| Indians + Persians | War Elephant | Cambriano (Classical) | Deinotherium | War Deinophant |
| Indians + Persians | Mahout | Devoniano (Medieval) | Deinotherium | Deino-Mahout |
| Indians + Persians | Gun Mahout | Carbonífero (Gunpowder) | Deinotherium | Gun Deino-Mahout |
| Indians + Persians | Culverin Mahout | Triássico (Enlightenment) | Deinotherium | Culverin Deino-Mahout |
| Persians | Immortals | Pré-cambriano (Ancient) | verme | Im-wormtals |
| Persians | Anusiya | Cambriano (Classical) | Pikaia | Anu-silt-ya |
| Persians | Athanatoi | Devoniano (Medieval) | Acanthostega | Acanthanatoi |
| Persians | Arqimmortal (na tela: Arquebus Immortal) | Carbonífero (Gunpowder) | Archaeothyris | Archaeo-Immortal |
Obs.: a linha de elefantes é uma unidade só, com uma textura só, para as duas nações. Fica Deinotherium em todos os degraus, como exceção (igual aos grandes dinossauros especiais), porque nenhum ancestral pequeno faz papel de elefante.

### Crocodilos
| Nação | Unidade original | Era | Bicho | Nome no jogo |
|---|---|---|---|---|
| Egyptians | Chariot | Cambriano (Classical) | Pikaia | Char-eel-ot |
| Egyptians | Heavy Chariot | Devoniano (Medieval) | Tiktaalik | Heavy Crawl-iot |
| Egyptians | Mameluke | Carbonífero (Gunpowder) | Hylonomus | Scale-meluke |
| Egyptians | Royal Mameluke | Triássico (Enlightenment) | Postosuchus | Royal Mamelu-suchus |
| Egyptians | Light Camel | Cambriano (Classical) | Pikaia | Light Wriggle-camel |
| Egyptians | Camel Warrior | Devoniano (Medieval) | Tiktaalik | Camel Wader |
| Egyptians | Elite Camel Warrior | Carbonífero (Gunpowder) | Hylonomus | Elite Camel Scaler |
| Nubians | Kushite Archers | Cambriano (Classical) | Pikaia | Pikushite Archers |
| Nubians | Royal Kushite Archers | Devoniano (Medieval) | Tiktaalik | Royal Kush-taalik Archers |
| Nubians | Apedemak Archers | Carbonífero (Gunpowder) | Hylonomus | Hylo-demak Archers |
| Nubians | Camel Archer | Cambriano (Classical) | Pikaia | Cam-eel Archer |
| Nubians | Heavy Camel Archer | Devoniano (Medieval) | Tiktaalik | Heavy Tik-camel Archer |
| Nubians | Camel Raider | Carbonífero (Gunpowder) | Hylonomus | Camel Scale-raider |
| Nubians | Camel Corps | Triássico (Enlightenment) | Postosuchus | Camel Corp-suchus |
| Dutch | Armed Caravan (civil) | Pré-cambriano (Ancient) | verme | Armed Crawl-avan |
| Dutch | Armed Merchant (civil) | Pré-cambriano (Ancient) | verme | Armed Wormchant |
| Dutch | Armed Supply Wagon (civil) | Devoniano (Medieval) | Tiktaalik | Armed Supply Waddler |
| Dutch | Brig (navio) | Devoniano (Medieval) | Tiktaalik (peixe de águas rasas) | Brig-fin |
| Dutch | Fluyt (navio) | Carbonífero (Gunpowder) | Crassigyrinus (tetrápode aquático) | Crassi-Fluyt |
| Dutch | Clipper (navio) | Triássico (Enlightenment) | Mystriosuchus (fitossauro marinho) | Clip-snapper |
Obs.: o Hylonomus e o Postosuchus da linhagem são terrestres, então o Fluyt e o Clipper usam aquáticos da época. O Mystriosuchus tem cara de crocodilo, mas o Crassigyrinus é de fora da linhagem.

### Tartarugas
| Nação | Unidade original | Era | Bicho | Nome no jogo |
|---|---|---|---|---|
| Chinese | Fire Lances | Devoniano (Medieval) | Tiktaalik | Fire Fin-Lances |
| Chinese | Heavy Fire Lances | Carbonífero (Gunpowder) | Hylonomus | Heavy Fire Scale-lances |
| Chinese | Manchu Musketeers | Triássico (Enlightenment) | Proganochelys | Manchu Mus-shell-teers |
| Chinese | Manchu Riflemen | Jurássico (Industrial) | Kayentachelys | Manchu Rifle-shells |
| Chinese | Manchu Infantry | Cretáceo (Modern) | Basilemys | Manchu Shell-fantry |
| Koreans | Hwarang | Pré-cambriano (Ancient) | verme | Worm-rang |
| Koreans | Elite Hwarang | Cambriano (Classical) | Pikaia | Elite Eel-rang |
| Koreans | Royal Hwarang | Devoniano (Medieval) | Tiktaalik | Royal Limb-rang |
| Koreans | Elite Royal Hwarang | Carbonífero (Gunpowder) | Hylonomus | Elite Royal Scale-rang |
| Koreans | Flaming Arrow (artilharia) | Cambriano (Classical) | Pikaia | Flaming Arrow-wriggler |
| Koreans | Heavy Flaming Arrow (artilharia) | Devoniano (Medieval) | Tiktaalik | Heavy Flaming Tik-arrow |
| Maya | Balamob Slingers | Pré-cambriano (Ancient) | verme | Bala-mud Slingers |
| Maya | Royal Balamob Slingers | Cambriano (Classical) | Pikaia | Royal Bala-slime Slingers |
| Maya | Eagle Balamob Slingers | Devoniano (Medieval) | Tiktaalik | Eagle-fin Balamob Slingers |
| Maya | Recoilless Gun | Cretáceo (Modern) | Basilemys | Recoilless Shell Gun |
| Maya | Dragon AT Missile | Cenozoico (Information) | Stupendemys | Stupen-Dragon Missile |

### Lagartos e cobras
| Nação | Unidade original | Era | Bicho | Nome no jogo |
|---|---|---|---|---|
| Aztecs | Atl-Atls | Pré-cambriano (Ancient) | verme | Squirm-Atls |
| Aztecs | Royal Atl-Atls | Cambriano (Classical) | Pikaia | Royal Wriggl-Atls |
| Aztecs | Xopilli Atl-Atls | Devoniano (Medieval) | Tiktaalik | Xopilli Crawl-Atls |
| Aztecs | Jaguar Infantry | Cretáceo (Modern) | Najash | Na-jaguar Infantry |
| Aztecs | Jaguar Assault Infantry | Cenozoico (Information) | Titanoboa | Jagua-boa Assault Infantry |
| Incas | Inti Clubmen | Cambriano (Classical) | Pikaia | Inti Mud-clubbers |
| Incas | Inti Macemen | Devoniano (Medieval) | Tiktaalik | Inti Mace-crawlers |
| Incas | Mortar (artilharia) | Triássico (Enlightenment) | Megachirella | Mor-tail |
| Incas | Siege Mortar (artilharia) | Jurássico (Industrial) | Eichstaettisaurus | Siege Mor-tail |
| Iroquois | Takohs (batedor) | Pré-cambriano (Ancient) | verme | Ta-coils |
| Iroquois | Akweks (batedor) | Devoniano (Medieval) | Tiktaalik | Aqua-weks |
| Iroquois | Okwari (batedor) | Triássico (Enlightenment) | Megachirella | Okwa-chirella |
| Iroquois | Spearmen | Pré-cambriano (Ancient) | verme | Spear-worms |
| Iroquois | Mohawk Spearmen | Cambriano (Classical) | Pikaia | Mohawk Spear-eels |
| Iroquois | Heavy Mohawk Spearmen | Devoniano (Medieval) | Tiktaalik | Heavy Mohawk Spear-crawlers |
| Iroquois | Elite Mohawk Spearmen | Carbonífero (Gunpowder) | Hylonomus | Elite Mohawk Spear-scales |

### Anfíbios
| Nação | Unidade original | Era | Bicho | Nome no jogo |
|---|---|---|---|---|
| British | Longbowmen | Cambriano (Classical) | Pikaia | Long-eel-men |
| British | King's Longbowmen | Devoniano (Medieval) | Acanthostega | King's Longlimbmen |
| British | King's Yeomanry | Carbonífero (Gunpowder) | Proterogyrinus | King's Newt-omanry |
| British | Highlanders | Triássico (Enlightenment) | Triadobatrachus | Hop-landers |
| British | Black Watch | Jurássico (Industrial) | Prosalirus | Black Watch Leapers |
| British | Lancaster Bomber (avião) | Cretáceo (Modern) | pterossauro (Quetzalcoatlus), exceção | Ptero-caster Bomber |
| Japanese | Ashigaru Spearmen | Pré-cambriano (Ancient) | verme | Ashi-goo Spearmen |
| Japanese | Bushi | Cambriano (Classical) | Pikaia | Squishi |
| Japanese | Elite Bushi | Devoniano (Medieval) | Acanthostega | Elite Toe-shi |
| Japanese | Samurai | Carbonífero (Gunpowder) | Proterogyrinus | Sala-murai |
| Japanese | Gun Samurai | Triássico (Enlightenment) | Triadobatrachus | Gun Hop-murai |
| Spanish | Scutari | Cambriano (Classical) | Pikaia | Squirm-utari |
| Spanish | Royal Scutari | Devoniano (Medieval) | Acanthostega | Royal Scute-stega |
| Spanish | Tercios | Carbonífero (Gunpowder) | Proterogyrinus | Tercio-gyrinus |
| Spanish | Royal Tercios | Triássico (Enlightenment) | Triadobatrachus | Royal Ter-croaks |
Obs.: nunca existiu anfíbio voador, então o Lancaster Bomber usa um pterossauro do Cretáceo com as marcas de guerra britânicas (a decidir).

### Insetos
| Nação | Unidade original | Era | Bicho | Nome no jogo |
|---|---|---|---|---|
| Romans | Legions | Cambriano (Classical) | Marrella | Hundred-Leg-ions |
| Romans | Caesar's Legions | Devoniano (Medieval) | Rhyniognatha | Caesar's Mandib-legions |
| Romans | Praetorian Guards | Carbonífero (Gunpowder) | Meganeura | Praeto-wing Guards |
| Germans | Solduri | Pré-cambriano (Ancient) | artrópode de lama | Mudduri |
| Germans | Barbarians | Cambriano (Classical) | Marrella | Barba-rellas |
| Germans | Vandals | Devoniano (Medieval) | Rhyniognatha | Mandi-vandals |
| Germans | Landsknechts | Carbonífero (Gunpowder) | Meganeura | Wingsknechts |
| Germans | Volksgrenadiers | Cretáceo (Modern) | primeiras formigas | Volksgrenadi-ants |
| Germans | MG42 | Cretáceo (Modern) | primeiras abelhas | MG42 Stinger |
| Germans | Tiger Tank | Cretáceo (Modern) | besouro do Cretáceo | Tiger Beetle Tank |
| Germans | Leopard Tank | Cenozoico (Information) | besouro grande do Cenozoico | Leo-hard Beetle Tank |
| Americans | Continental Marines (na tela: Marines) | Triássico (Enlightenment) | besouro primitivo | Continental Ma-beetles |
| Americans | Marine Riflemen | Jurássico (Industrial) | vespa primitiva | Marine Rifle-stingers |
| Americans | Marine Infantry | Cretáceo (Modern) | primeiras abelhas | Bee-rine Infantry |
| Americans | Assault Marines | Cenozoico (Information) | abelha | Assault Bee-rines |
Obs.: os tanques alemães usam besouro (bicho-símbolo, existe no Cretáceo e no Cenozoico) no lugar de formiga; os Assault Marines usam abelha (bicho-símbolo) no lugar da Titanomyrma.

### Aracnídeos
| Nação | Unidade original | Era | Bicho | Nome no jogo |
|---|---|---|---|---|
| Turks | Janissaries | Carbonífero (Gunpowder) | Pulmonoscorpius | Jani-stingers |
| Turks | Royal Janissaries | Triássico (Enlightenment) | aranha primitiva | Royal Spin-issaries |
| Turks | Basilica Bombard (artilharia) | Carbonífero (Gunpowder) | Pulmonoscorpius | Basilica Bom-barb |
| Turks | Basilica Cannon (artilharia) | Triássico (Enlightenment) | aranha primitiva | Basilica Web Cannon |
| Greeks | Companion | Cambriano (Classical) | Sanctacaris | Claw-panion |
| Greeks | Royal Companion | Devoniano (Medieval) | trigonotarbídeo | Royal Trigo-panion |
| Greeks | Stratiotai | Carbonífero (Gunpowder) | Pulmonoscorpius | Sting-iotai |
| Greeks | Royal Stratiotai | Triássico (Enlightenment) | aranha primitiva | Royal Strati-spinners |
| French | Chevalier | Cambriano (Classical) | Sanctacaris | Chela-valier |
| French | Heavy Chevalier | Devoniano (Medieval) | trigonotarbídeo | Heavy Chela-valier |
| French | Horse Grenadier | Carbonífero (Gunpowder) | Pulmonoscorpius | Sting Grenadier |
| French | Horse Guard Grenadier | Triássico (Enlightenment) | aranha primitiva | Web Guard Grenadier |

### Pontos em aberto
- ~~Cambriano dos vertebrados: peixe em unidade de terra.~~ Resolvido (Ana, 18/10/2026): todas as unidades de terra do Cambriano usam Pikaia; Haikouichthys só no mar.
- Elefantes com Deinotherium desde o Cambriano: anacronismo assumido como exceção.
- Lancaster Bomber (pterossauro), Fluyt (Crassigyrinus) e Katyusha (Repenomamus como artilharia) são encaixes forçados.
- Nomes com palavras de povos reais (Sunka Wakan, Mohawk, Xopilli, Inti): conferir se o tom fica respeitoso.
