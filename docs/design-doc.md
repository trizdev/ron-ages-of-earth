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

## Unidades genéricas e navios v1 (aprovadas pela Ana, 18/10/2026)
**Regra.** As unidades genéricas usam uma textura só para as 24 nações, então não seguem nenhuma linhagem.
- Unidades de terra: nas 3 primeiras eras usam formas da raiz comum (verme, Pikaia, Tiktaalik/Acanthostega) e outros bichos de lodaçal e margem da época. Da era seguinte em diante, cada linha usa um bicho "comum" da era que não é símbolo de nenhuma nação: anfíbios e sinápsidos primitivos, Lystrosaurus e aetossauros, dinossauros ornitísquios e saurópodes, mamíferos do Cenozoico.
- Navios: só aquáticos, por era (seres de Ediacara > Anomalocaris/Haikouichthys > placodermos e tubarões > ictiossauros > plesiossauros > mosassauros > baleias e megalodonte).
- Aviões: voadores por era (pterossauros > aves e morcegos). Mísseis viram meteoros e asteroides.
- Civis e comando: bichinhos pequenos e não ameaçadores, com textura única o jogo todo.
- Uma linha tem um bicho diferente por era, para cada degrau ficar reconhecível.
Fonte das eras: `PREQ0` em `unitrules.xml`. `none` = Ancient. General: tecnologia Mathematics (Classical). Spy: Mathematics + Medieval Age. Trireme e Bark: The Art of War (Ancient). Líderes: governo (Despotism/Republic = Classical, Monarchy/Democracy = Gunpowder, Socialism/Capitalism = Industrial).
As 48 variantes regionais de gráfico (Sherman, T34, Panzer, ME109, Mig, versões coreanas, espanholas e alemãs etc.) recebem o mesmo bicho da unidade, uma textura para cada variante.

### Infantaria de terra
| Linha | Unidade original | Era | Bicho | Nome no jogo |
|---|---|---|---|---|
| Hoplitas → antitanque | Hoplites | Pré-cambriano (Ancient) | Ikaria (verme bilateral) | Worm-lites |
| Hoplitas → antitanque | Phalanx | Cambriano (Classical) | Wiwaxia | Spine-alanx |
| Hoplitas → antitanque | Pikemen | Devoniano (Medieval) | Ventastega | Venta-pikes |
| Hoplitas → antitanque | Elite Pikemen | Carbonífero (Gunpowder) | Pholiderpeton | Elite Pike-erpetons |
| Hoplitas → antitanque | Fusiliers | Triássico (Enlightenment) | Hyperodapedon (rincossauro) | Fusi-beaks |
| Hoplitas → antitanque | Anti-tank Rifle | Jurássico (Industrial) | Kentrosaurus | Anti-tank Spike Rifle |
| Hoplitas → antitanque | Bazooka | Cretáceo (Modern) | Styracosaurus | Styra-zooka |
| Hoplitas → antitanque | Anti-Tank Missile | Cenozoico (Information) | Uintatherium | Anti-Tusk Missile |
| Fundibulários → infantaria | Slingers | Pré-cambriano (Ancient) | Spriggina | Sprig-slingers |
| Fundibulários → infantaria | Javelineers | Cambriano (Classical) | Pikaia | Pika-lineers |
| Fundibulários → infantaria | Elite Javelineers | Devoniano (Medieval) | Elginerpeton | Elite Elgin-eers |
| Fundibulários → infantaria | Arquebusiers | Carbonífero (Gunpowder) | Pederpes | Arque-pedes |
| Fundibulários → infantaria | Musketeers | Triássico (Enlightenment) | Lystrosaurus | Tusk-eteers |
| Fundibulários → infantaria | Riflemen | Jurássico (Industrial) | Dryosaurus | Dryo-Riflemen |
| Fundibulários → infantaria | Infantry | Cretáceo (Modern) | Edmontosaurus (hadrossauro) | Duck-fantry |
| Fundibulários → infantaria | Assault Infantry | Cenozoico (Information) | Entelodon | Assault Hog-fantry |
| Arqueiros | Bowmen | Pré-cambriano (Ancient) | Kimberella | Bow-slugs |
| Arqueiros | Archers | Cambriano (Classical) | Hallucigenia | Halluci-archers |
| Arqueiros | Crossbowmen | Devoniano (Medieval) | Acanthostega | Crossbow-stegans |
| Arqueiros | Heavy Archers (variante de 5 nações) | Devoniano (Medieval) | Acanthostega | Heavy Acantho-archers |
| Milícia (Tower) | Militia | Cambriano (Classical) | Aysheaia | Lobo-militia |
| Milícia (Tower) | Minuteman | Triássico (Enlightenment) | Procolophon | Minute-colophon |
| Milícia (Tower) | Partisan | Cretáceo (Modern) | Psittacosaurus | Parrot-isans |
| Metralhadoras | Machine Gun | Jurássico (Industrial) | Scutellosaurus | Machine Scute |
| Metralhadoras | Heavy Machine Gun | Cretáceo (Modern) | Protoceratops | Heavy Proto-gun |
| Metralhadoras | Advanced Machine Gun | Cenozoico (Information) | Hyaenodon | Advanced Hyaeno-gun |
| Lança-chamas | Flamethrower | Jurássico (Industrial) | Heterodontosaurus | Flame-odont |
| Batedores | Scout | Pré-cambriano (Ancient) | Yilingia (verme que deixava trilhas) | Trackworm |
| Batedores | Explorer | Devoniano (Medieval) | Tiktaalik | Shore Explorer |
| Batedores | Commando | Jurássico (Industrial) | Fruitadens (heterodontossaurídeo pequeno) | Fruit-mando |
| Batedores | Special Forces | Cretáceo (Modern) | Thescelosaurus | Special Forest |
| Batedores | Elite Special Forces | Cenozoico (Information) | Smilodon | Elite Special Fangs |

### Cavalaria e blindados
| Linha | Unidade original | Era | Bicho | Nome no jogo |
|---|---|---|---|---|
| Cavalaria pesada → tanques | Cataphract | Cambriano (Classical) | Olenoides (trilobita) | Trilo-phract |
| Cavalaria pesada → tanques | Knight | Devoniano (Medieval) | Ichthyostega | Ichthy-knight |
| Cavalaria pesada → tanques | Heavy Knight | Carbonífero (Gunpowder) | Arthropleura | Heavy Arthro-knight |
| Cavalaria pesada → tanques | Cuirassier | Triássico (Enlightenment) | Desmatosuchus (aetossauro) | Cuirassaur |
| Cavalaria pesada → tanques | Light Tank | Jurássico (Industrial) | Gargoyleosaurus | Light Gargoyle Tank |
| Cavalaria pesada → tanques | Tank | Cretáceo (Modern) | Sauropelta (nodossauro) | Pelta Tank |
| Cavalaria pesada → tanques | Main Battle Tank | Cenozoico (Information) | Glyptodon | Glypto-tank |
| Arqueiros montados → carros blindados | Horse Archer | Cambriano (Classical) | Leanchoilia | Whip Archer |
| Arqueiros montados → carros blindados | Heavy Horse Archer | Devoniano (Medieval) | Tulerpeton | Heavy Six-toe Archer |
| Arqueiros montados → carros blindados | Dragoon | Carbonífero (Gunpowder) | Ophiacodon | Drag-odon |
| Arqueiros montados → carros blindados | Carabineer | Triássico (Enlightenment) | Euparkeria | Euparki-neer |
| Arqueiros montados → carros blindados | Armored Car | Jurássico (Industrial) | Scelidosaurus | Armored Scale Car |
| Arqueiros montados → carros blindados | Armored Scout Car | Cretáceo (Modern) | Edmontonia (nodossauro) | Armored Scout Nodocar |
| Arqueiros montados → carros blindados | Armored Cavalry | Cenozoico (Information) | Hipparion | Armored Hippa-valry |
| Cavalaria leve | Light Horse | Cambriano (Classical) | Canadaspis | Light Horse-shrimp |
| Cavalaria leve | Light Cavalry | Devoniano (Medieval) | Hynerpeton | Light Crawl-valry |
| Cavalaria leve | Elite Light Cavalry | Carbonífero (Gunpowder) | Petrolacosaurus | Elite Light Scale-valry |
| Cavalaria leve | Hussar | Triássico (Enlightenment) | Herrerasaurus | Hussaur |

### Cerco, artilharia e antiaéreo
| Linha | Unidade original | Era | Bicho | Nome no jogo |
|---|---|---|---|---|
| Cerco → artilharia | Catapult | Cambriano (Classical) | Sidneyia | Catapod |
| Cerco → artilharia | Trebuchet | Devoniano (Medieval) | Eoarthropleura | Trebu-pede |
| Cerco → artilharia | Bombard | Carbonífero (Gunpowder) | Edaphosaurus | Sail Bombard |
| Cerco → artilharia | Cannon | Triássico (Enlightenment) | Placerias | Placer-cannon |
| Cerco → artilharia | Artillery | Jurássico (Industrial) | Shunosaurus (saurópode com clava na cauda) | Club-tillery |
| Cerco → artilharia | Howitzer | Cretáceo (Modern) | Corythosaurus (hadrossauro de crista) | Howl-itzer |
| Cerco → artilharia | Rocket Artillery | Cenozoico (Information) | Megacerops (brontotério) | Rocket Thunder-tillery |
| Antiaéreo | Anti-Aircraft Gun | Jurássico (Industrial) | Mamenchisaurus | Anti-Air Long-neck |
| Antiaéreo | Anti-Aircraft Battery | Cretáceo (Modern) | Alamosaurus (titanossauro) | Anti-Air Titan Battery |
| Antiaéreo | Anti-Aircraft Missile | Cenozoico (Information) | Sivatherium | Anti-Air Antler Missile |

### Navios
| Linha | Unidade original | Era | Bicho | Nome no jogo |
|---|---|---|---|---|
| Pesados (Trireme → Advanced Battleship) | Trireme | Pré-cambriano (Ancient) | Dickinsonia | Disc Trireme |
| Pesados (Trireme → Advanced Battleship) | Galley | Cambriano (Classical) | Anomalocaris | Anomalo-galley |
| Pesados (Trireme → Advanced Battleship) | Carrack | Devoniano (Medieval) | Dunkleosteus | Dunkle-carrack |
| Pesados (Trireme → Advanced Battleship) | Frigate | Carbonífero (Gunpowder) | Rhizodus | Frigodus |
| Pesados (Trireme → Advanced Battleship) | Man o' War | Triássico (Enlightenment) | Shonisaurus (ictiossauro) | Man o' Saur |
| Pesados (Trireme → Advanced Battleship) | Dreadnought | Jurássico (Industrial) | Liopleurodon | Dreadnodon |
| Pesados (Trireme → Advanced Battleship) | Battleship | Cretáceo (Modern) | Mosasaurus | Battlesaur |
| Pesados (Trireme → Advanced Battleship) | Advanced Battleship | Cenozoico (Information) | Livyatan | Advanced Battle-whale |
| Leves (Bark → Missile Cruiser) | Bark | Pré-cambriano (Ancient) | Eoandromeda (disco de 8 braços) | Star Bark |
| Leves (Bark → Missile Cruiser) | Dromon | Cambriano (Classical) | Haikouichthys | Fin-dromon |
| Leves (Bark → Missile Cruiser) | Caravel | Devoniano (Medieval) | Cladoselache (tubarão primitivo) | Shark-avel |
| Leves (Bark → Missile Cruiser) | Corvette | Carbonífero (Gunpowder) | Stethacanthus | Anvil Corvette |
| Leves (Bark → Missile Cruiser) | Sloop | Triássico (Enlightenment) | Mixosaurus | Mixo-sloop |
| Leves (Bark → Missile Cruiser) | Destroyer | Jurássico (Industrial) | Ophthalmosaurus | Eye-stroyer |
| Leves (Bark → Missile Cruiser) | Cruiser | Cretáceo (Modern) | Tylosaurus | Tylo-cruiser |
| Leves (Bark → Missile Cruiser) | Missile Cruiser | Cenozoico (Information) | Basilosaurus | Basilo-cruiser |
| Incendiários → submarinos | Fire Raft | Cambriano (Classical) | Burgessomedusa (água-viva) | Sting Raft |
| Incendiários → submarinos | Heavy Fire Raft | Devoniano (Medieval) | goniatita (amonoide do Devoniano) | Heavy Fire Coil-raft |
| Incendiários → submarinos | Fireship | Carbonífero (Gunpowder) | Edestus (tubarão-tesoura) | Scissor Fireship |
| Incendiários → submarinos | Heavy Fireship | Triássico (Enlightenment) | Nothosaurus | Heavy Fire-notho |
| Incendiários → submarinos | Submarine | Jurássico (Industrial) | Plesiosaurus | Plesio-marine |
| Incendiários → submarinos | Attack Submarine | Cenozoico (Information) | Otodus megalodon | Attack Megalo-sub |
| Bombardeio | Bomb Vessel | Carbonífero (Gunpowder) | Falcatus | Falca-bomb Vessel |
| Bombardeio | Bomb Ketch | Triássico (Enlightenment) | Placodus | Bomb Placo-ketch |
| Porta-aviões | Aircraft Carrier | Cretáceo (Modern) | Archelon (tartaruga marinha gigante) | Air-chelon Carrier |
| Civis do mar | Fishermen | jogo todo (textura única), textura única | náutilo | Nauti-fishers |
| Civis do mar | Merchant Fleet | Cambriano (Classical) | Waptia | Mer-shrimp Fleet |
| Civis do mar | Modern Merchant Fleet | Jurássico (Industrial) | Leedsichthys | Modern Mer-gulp Fleet |
| Civis do mar | Transport Barge | Cambriano (Classical) | Opabinia | Opa-barge |
| Civis do mar | Transport Galleon | Carbonífero (Gunpowder) | Rhabdoderma (celacanto) | Coela-galleon |
| Civis do mar | Transport Freighter | Jurássico (Industrial) | Titanites (amonite gigante) | Coil Freighter |

### Aviões e mísseis
| Linha | Unidade original | Era | Bicho | Nome no jogo |
|---|---|---|---|---|
| Caças | Biplane | Jurássico (Industrial) | Rhamphorhynchus | Rhampho-plane |
| Caças | Fighter | Cretáceo (Modern) | Pteranodon | Fight-anodon |
| Caças | Jet Fighter | Cenozoico (Information) | águia-de-Haast | Haast Jet |
| Caças | Advanced Fighter | Cenozoico (Information) | Pelagornis | Advanced Pelago-fighter |
| Bombardeiros | Bomber | Cretáceo (Modern) | Quetzalcoatlus | Bomb-coatlus |
| Bombardeiros | Strategic Bomber | Cenozoico (Information) | Teratornis | Strategic Tera-bomber |
| Bombardeiros | Stealth Bomber | Cenozoico (Information) | Icaronycteris (morcego) | Stealth Bomb-bat |
| Caças de porta-aviões | Fighter Bomber | Cretáceo (Modern) | Nyctosaurus (pterossauro marinho) | Fighter Nycto-bomber |
| Caças de porta-aviões | Jet Fighter Bomber | Cenozoico (Information) | Limnofregata (fragata primitiva) | Jet Frigate-bird Bomber |
| Helicópteros | Helicopter | Cretáceo (Modern) | libélula do Cretáceo | Dragonfly-copter |
| Helicópteros | Attack Helicopter | Cenozoico (Information) | Eurotrochilus (beija-flor primitivo) | Attack Hum-copter |
| Mísseis | V2 Rocket | Cretáceo (Modern) | meteoro | Meteo-rocket |
| Mísseis | Cruise Missile | Cenozoico (Information) | meteoro | Cruise Meteor |
| Mísseis | Nuclear Missile | Cretáceo (Modern) | asteroide | Extinction Event |
| Mísseis | Nuclear ICBM | Cenozoico (Information) | asteroide | Extinction ICBM |

### Civis e comando (uma textura cada, o jogo todo)
| Linha | Unidade original | Era | Bicho | Nome no jogo |
|---|---|---|---|---|
| Civis | Citizen | Pré-cambriano (Ancient), textura única | caramujo | Citi-snail |
| Civis | Scholar | Pré-cambriano (Ancient), textura única | verme-aveludado | Bookworm |
| Civis | Merchant | Pré-cambriano (Ancient), textura única | milípede | Milli-peddler |
| Civis | Caravan | Pré-cambriano (Ancient), textura única | tatuzinho-de-jardim (isópode) | Roly-Poly Caravan |
| Civis | Supply Wagon | Devoniano (Medieval), textura única | límulo (caranguejo-ferradura) | Horseshoe Supply Wagon |
| Comando | General | Cambriano (Classical), textura única | tuatara | General Tua-tactics |
| Comando | Spy | Devoniano (Medieval), textura única | camaleão | Chamele-spy |
| Líderes de governo | The Despot | Cambriano (Classical), textura única | Dimetrodon | The Despo-trodon |
| Líderes de governo | The Senator | Cambriano (Classical), textura única | Mantellisaurus (iguanodonte com espinho no polegar) | The Thumb Senator |
| Líderes de governo | The Monarch | Carbonífero (Gunpowder), textura única | Ctenosauriscus (arcossauro de vela do Triássico) | The Monarchosaur |
| Líderes de governo | The President | Carbonífero (Gunpowder), textura única | Megatherium | The Mega-President |
| Líderes de governo | The Comrade | Jurássico (Industrial), textura única | Lystrosaurus | The Comrade Lystro |
| Líderes de governo | The CEO | Jurássico (Industrial), textura única | Cetiosaurus | The CEO-tiosaurus |

### Grandes dinossauros reservados para unidades especiais (decisão da Ana, 18/10/2026)
Não usar em unidades genéricas: Tyrannosaurus rex, Triceratops, Stegosaurus, Ankylosaurus, Brachiosaurus, Diplodocus, Apatosaurus/Brontosaurus, Argentinosaurus, Spinosaurus, Allosaurus, Parasaurolophus, Iguanodon, Pachycephalosaurus, Compsognathus.
Velociraptor fica fora da reserva: continua símbolo dos Mongols e bicho do Cretáceo na linhagem das Aves (Ana, 18/10/2026).

### Pontos em aberto
- ~~Tricerátops e outros dinossauros grandes nas genéricas?~~ Resolvido: grandes dinossauros reservados como especiais, decisão da Ana 18/10/2026. Trocados: Triceratops, Diplodocus, Brachiosaurus, Parasaurolophus, Argentinosaurus, Compsognathus, Iguanodon, Spinosaurus, Allosaurus.
- Algumas genéricas coincidem com linhagens de nações (sem ser bicho-símbolo): Archelon (tartarugas), aves e morcegos do Cenozoico (aves e mamíferos), libélula (insetos), mamíferos do Cenozoico em terra.
- Civis e líderes têm textura única o jogo todo, então ficam fora da época em parte da partida (fósseis vivos foram escolhidos para minimizar isso).
- Líderes de governo: confirmar se a Ana quer bichos ou se eles seguem a nação.

## Construções, maravilhas e recursos v1 (18/10/2026, aprovado)

> **Decisão (18/10/2026):** v1 usa um visual único de prédios para todas as linhagens (3 fases visuais). Visual por linhagem (via `BUILD_CONTINENT`, 9 estilos) fica para a v2.
**Regra.** Prédios viram habitats e estruturas naturais pré-históricas (poças de maré, estromatólitos, recifes, tocas, ninhos, cupinzeiros, leitos de fósseis), em estilo realista. As 3 etapas visuais de cada prédio contam a vida tomando a terra:
- Etapa 1 (Pré-cambriano a Devoniano): rocha úmida, tapete de micróbios, poças e recifes.
- Etapa 2 (Carbonífero e Triássico): samambaias, troncos, tocas na lama.
- Etapa 3 (Jurássico a Cenozoico): ninhos, cupinzeiros, florestas de coníferas e de flores.
Maravilhas viram formações geológicas e fenômenos pré-históricos genéricos, sem nomes de lugares reais. Recursos ganham equivalentes naturais; o Oil continua Oil.
Fonte: `buildingrules.xml` (`PREQ0`/`PREQ1`, `FROM`), `building_graphics.xml`, `typenames.xml` (`<BUILDS>`, `<GOODS>`), `rules.xml`. Era da tecnologia exigida: The Art of War, Barter e Written Word = Ancient; Mathematics e Mercenaries = Classical; Chemistry = Medieval; Electronics = Industrial.

### Visual por linhagem (o que o building_graphics.xml permite)
- Cada prédio tem entradas `NOME-ESTILO-AGEn` para 9 estilos (DEFAULT, NEUROPE, ASIAN, KOREAN, AMERICAN, ARAB, EINDIAN, IROQUOIS, COLONIAL) e 3 etapas: AGE0, AGE3, AGE5. As torres e fortes têm AGE0/3/4/6.
- AGE é o índice da era (0 = Ancient). AGE4 e AGE6 coincidem com Stockade (Enlightenment) e Bunker (Modern), então AGE3 = Gunpowder e AGE5 = Industrial. As etapas são Ancient–Medieval, Gunpowder–Enlightenment e Industrial–Information. Dedução, confirmar no jogo ❓.
- O estilo vem de `BUILD_CONTINENT` em `tribes/<nação>.xml`, que é texto. Com 9 estilos e 8 linhagens, dá para dar um estilo para cada linhagem: troca-se o `BUILD_CONTINENT` das 3 nações e repinta-se o estilo. Não testado ❓.
- Limites:
  - Hoje os estilos dividem texturas (ex.: `barracks_0s.tga` em AMERICAN/ARAB/EINDIAN; `barracks_6.tga` em todos na AGE5). No mod, o `building_graphics.xml` teria que apontar cada estilo para um arquivo novo.
  - Os prédios são sprites 2D pré-renderizados, então a forma fica a do estilo; só a pintura muda.
  - Farm, Woodcutter's Camp, Mine, Oil, Airbase, Missile Silo, defesas antiaéreas e maravilhas têm arte única para todos.
  - KOREAN usa ASIAN como reserva quando falta arte.
- Volume: cerca de 30 prédios × 3 etapas × 8 estilos, ou seja, centenas de texturas. Sugestão: começar com um visual só para todos e deixar o visual por linhagem para uma versão 2.
- Sugestão de estilo por linhagem: Aves = IROQUOIS, Mamíferos = EINDIAN, Crocodilos = ARAB, Tartarugas = ASIAN, Lagartos e cobras = AMERICAN, Anfíbios = NEUROPE, Insetos = DEFAULT, Aracnídeos = COLONIAL. KOREAN fica sem uso.

### Prédios
| Linha | Prédio original | Era | Visual (habitat) | Nome no jogo |
|---|---|---|---|---|
| Cidade | Small City | Pré-cambriano (Ancient) | colônia de estromatólitos e poças de maré | Hatch-ville |
| Cidade | Large City | Devoniano (Medieval) | viveiro grande (rookery) na margem | Grand Rookery |
| Cidade | Major City | Jurássico (Industrial) | megacolônia de ninhos e tocas | Megalo-polis |
| Economia | Farm | Pré-cambriano (Ancient) | campo de samambaias e cavalinhas (textura única) | Fern-tile Field |
| Economia | Woodcutter's Camp | Pré-cambriano (Ancient) | troncos de samambaia-arbórea roídos | Wood-chewer's Camp |
| Economia | Mine | Cambriano (Classical) | afloramento de rocha escavado | Geo-dig |
| Economia | Granary | Cambriano (Classical) | esconderijo de esporos e sementes | Spore-ary |
| Economia | Lumber Mill | Cambriano (Classical) | tronco caído oco cheio de cupins | Timber Gnaw-mill |
| Economia | Smelter | Devoniano (Medieval) | fonte hidrotermal | Lava-smelter |
| Economia | Oil Well | Jurássico (Industrial) | poço de piche | Tar Pit |
| Economia | Oil Platform | Jurássico (Industrial) | exsudação de piche no mar | Tar Seep Platform |
| Economia | Refinery | Jurássico (Industrial) | turfeira fumegante | Bog-finery |
| Comércio e saber | Market | Pré-cambriano (Ancient) | banco de conchas | Shell Exchange |
| Comércio e saber | Library | Pré-cambriano (Ancient) | paredão de camadas com fósseis | Fossil Record |
| Comércio e saber | Temple | Pré-cambriano (Ancient) | santuário de âmbar | Amber Shrine |
| Comércio e saber | University | Cambriano (Classical) | caverna de cristais | Paleo-versity |
| Comércio e saber | Senate | Cambriano (Classical) | clareira do conselho do bando | Herd Senate |
| Militares | Barracks | Pré-cambriano (Ancient) | tocas de ninhada | Burrow-acks |
| Militares | Stable | Cambriano (Classical) | bebedouro de manada | Stampede Pen |
| Militares | Auto Plant | Jurássico (Industrial) | casulos de muda de carapaça | Armor Molt Plant |
| Militares | Siege Factory | Cambriano (Classical) | pedreira de desmoronamento | Rockfall Works |
| Militares | Factory | Jurássico (Industrial) | leito de fósseis industrial | Fossil Factory |
| Militares | Dock | Pré-cambriano (Ancient) | poça de maré | Tide-dock |
| Militares | Anchorage | Carbonífero (Gunpowder) | recife de coral | Reef Anchorage |
| Militares | Shipyard | Jurássico (Industrial) | floresta de algas | Kelp-yard |
| Militares | Airbase | Jurássico (Industrial) | penhasco de pouso de pterossauros | Cliff Roost |
| Militares | Missile Silo | Cretáceo (Modern) | cratera de impacto | Impact Silo |
| Defesas | Tower | Pré-cambriano (Ancient) | torre de estromatólito | Stroma-tower |
| Defesas | Keep | Devoniano (Medieval) | cúpula de concha | Shell Keep |
| Defesas | Stockade | Triássico (Enlightenment) | cerca de espinhos de cicadácea | Thorn Stockade |
| Defesas | Bunker | Cretáceo (Modern) | toca blindada | Burrow Bunker |
| Defesas | Fort | Cambriano (Classical) | fortaleza de recife | Reef Fort |
| Defesas | Castle | Devoniano (Medieval) | castelo de coral | Coral Castle |
| Defesas | Fortress | Triássico (Enlightenment) | muralha de rocha fossilífera | Fossil Fortress |
| Defesas | Redoubt | Cretáceo (Modern) | bastião de basalto | Basalt Redoubt |
| Defesas | Lookout | Pré-cambriano (Ancient) | afloramento rochoso | Look-out-crop |
| Defesas | Observation Post | Carbonífero (Gunpowder) | poleiro no dossel | Canopy Perch |
| Defesas | Air Defense Gun | Jurássico (Industrial) | ninho de mandíbulas | Sky Snapper |
| Defesas | Radar Air Defense | Cretáceo (Modern) | colônia de ecolocalização | Echo-location Station |
| Defesas | SAM Installation | Cenozoico (Information) | campo de gêiseres | Geyser Launcher |
Obs.: casas, apartamentos, escritórios e a Courtyard Fountain são decoração das cidades e ficaram fora. "Capital" é texto de interface (`translated_strings.xml`); sugestão: **Alpha Nest**.

### Maravilhas (arte única cada)
| Maravilha original | Era | Visual | Nome no jogo |
|---|---|---|---|
| Pyramids | Cambriano (Classical) | recife de estromatólitos gigantes | Great Stroma-mids |
| Colossus | Cambriano (Classical) | pilar de rocha no mar | Colossal Sea Stack |
| Hanging Gardens | Cambriano (Classical) | primeiras plantas em penhascos úmidos | Hanging Moss Gardens |
| Terra Cotta Army | Devoniano (Medieval) | leito de fósseis em massa | Terra Fossil Army |
| Colosseum | Devoniano (Medieval) | anel de cratera | Crater Colosseum |
| Forbidden City | Devoniano (Medieval) | atol fechado | Forbidden Reef |
| Temple of Tikal | Carbonífero (Gunpowder) | pântano do primeiro tetrápode | Temple of Tiktaalik |
| Porcelain Tower | Carbonífero (Gunpowder) | torre de madrepérola | Mother-of-Pearl Tower |
| Red Fort | Carbonífero (Gunpowder) | camadas vermelhas | Red Rock Fort |
| Angkor Wat | Triássico (Enlightenment) | floresta petrificada | Angkor Wood |
| Versailles | Triássico (Enlightenment) | lagoa dos dorsos-de-vela | Ver-sails Lagoon |
| Statue of Liberty | Jurássico (Industrial) | estalagmite gigante | Stalagmite of Liberty |
| Taj Mahal | Jurássico (Industrial) | caverna de cristais gigantes | Crystal Mahal |
| Kremlin | Cretáceo (Modern) | falésias de giz do Cretáceo | Chalk-remlin |
| Eiffel Tower | Cretáceo (Modern) | cupinzeiro gigante | Eiffel Mound |
| Supercollider | Cenozoico (Information) | cratera de asteroide | Super-collision Crater |
| Space Program | Cenozoico (Information) | aurora e chuva de meteoros | Aurora Program |
Obs.: El Dorado, Washington Monument e Lenin Statue estão desativadas (`disable`), são de cenário e ficaram fora.

### Recursos básicos
| Recurso original | Nome no jogo |
|---|---|
| Food | Grub |
| Timber | Fernwood |
| Metal | Minerals |
| Wealth | Shells |
| Knowledge | Instinct |
| Oil | Oil (continua: é combustível fóssil) |
| Fish (recurso do mar) | Plankton |
| Relics | Fossils |

### Recursos raros
| Recurso original | Efeito (rules.xml) | Nome no jogo |
|---|---|---|
| Wine | melhoria de unidades | Fermented Fruit |
| Papyrus | ciência militar | Horsetail Reeds |
| Dye | comércio cívico | Ink Sacs |
| Silk | comércio e caravanas | Spider Silk |
| Spice | renda de caravana | Ginkgo Nuts |
| Salt | Barracks mais barato | Salt Flats |
| Horses | Stable mais barato | Wild Herds |
| Rubber | Auto Plant mais barato | Resin |
| Sulphur | cerco mais barato | Sulphur |
| Amber | mercado | Amber |
| Silver | custo de era | Pyrite |
| Tobacco | velocidade de construção | Peat |
| Marble | maravilhas mais baratas | Limestone |
| Furs | militar e visão | Feathers |
| Cotton | velocidade de criação | Moss |
| Bison | Granary mais barato | Grazer Herds |
| Copper | vida das fábricas | Native Copper |
| Peacocks | população | Courtship Plumes |
| Citrus | — | Wild Berries |
| Sugar | comida mais barata | Nectar |
| Diamonds | comércio | Diamonds |
| Gems | bônus de território | Geodes |
| Aluminum | aviões mais baratos e rápidos | Hollow Bones |
| Whales | navios mais rápidos | Ichthyosaur Pods |
| Obsidian | alcance e ataque de arqueiros | Obsidian |
| Wool | Citizens mais baratos e rápidos | Down |
| Coal | madeira mais barata | Coal |
| Uranium | nukes mais baratas e rápidas | Iridium |
| Titanium | atrito | Chitin |
| Cattle ❓ | armadura de Citizen | Egg Clutches |
| Dogs ❓ | visão de batedores | Scent Trails |
| Incense ❓ | pesquisa no Temple | Copal |
| Olive Oil ❓ | fazendas | Cycad Oil |
| Gypsum ❓ | custo | Gypsum |
| Beaver Pelts ❓ | batedor/mercador grátis | Giant Beaver Lodges |
| Gold ❓ | riqueza mais barata | Gold Nuggets |
| Rum ❓ | alcance naval | Fermented Sap |
| Coffee ❓ | renda | Buzz Berries |
| Bananas ❓ | vida das unidades | Cycad Fruit |
| Salmon ❓ | navios mais baratos | Coelacanth Runs |
| Iron Ore ❓ | metal mais barato | Bog Iron |
| Maize ❓ | bônus crescente | Seed Ferns |
| Huskies ❓ | sem regra em rules.xml | Snow Runners |
❓ = aparece em `typenames.xml` e em `rules.xml` (menos Huskies), mas parece vir de campanha ou expansão; confirmar se aparece em partida normal.

### Pontos em aberto
- Visual por linhagem (9 estilos, não testado) ou um visual só para todos na v1?
- Nomes de recurso dentro de textos: os textos de `help.xml` dizem "food", "timber" etc. e precisariam ser revisados.
- Ícones dos recursos (`icon_texs.xml`) também teriam que ser repintados.
- A etapa visual dos prédios por era foi deduzida (AGE3 = Gunpowder, AGE5 = Industrial) e precisa ser confirmada numa partida.
