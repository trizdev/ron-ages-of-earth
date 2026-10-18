# Rise of Nations: Ages of Earth (Eras da Terra) — Documento de design

Status: v0.1 de textos e 13 bichos de cenário prontos (em teste); v0.2 de textos aprovada, ainda não instalada (18/10/2026). Os arquivos originais do jogo não são alterados: tudo fica numa pasta separada em `mods/`.
Repositório: github.com/trizdev/ron-ages-of-earth (privado)
Tipo: mod independente do Rise of Nations: Extended Edition (não é variante de outro mod). As 24 nações viram linhagens evolutivas pré-históricas e as 8 eras viram eras geológicas. Visual realista, sem toque fofo.

## Conceito
As 8 eras do Rise of Nations viram eras geológicas, em ordem. Pode ter animais pré-históricos. Mod próprio, para publicar no Workshop quando estiver pronto.

## Eras (proposta inicial, texto do jogo em inglês; substituída pelos Nomes das eras v2)
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
- Texturas .tga (GIMP ou geradas por script). Modelos novos são feitos no Blender e convertidos com o RoN File Converter (ver "Rota de modelos" abaixo); a ideia original de usar só o 3ds Max 5 foi substituída.

## Regras da Microsoft (Game Content Usage Rules)
Gratuito, sem anúncios, sem engenharia reversa, sem PI de terceiros, doações opcionais ok. Aviso obrigatório:
"Rise of Nations: Ages of Earth was created under Microsoft's "Game Content Usage Rules" using assets from Rise of Nations, © Microsoft Corporation."

## Perguntas em aberto
- Conferir os bônus reais de cada nação no mapeamento antes de fechar as habilidades.
- Confirmar se dá pra trocar só o texto das eras mantendo o hash.

## Nome do mod (atualizado 18/10/2026)
**Rise of Nations: Ages of Earth**
É um mod independente do Rise of Nations: Extended Edition. Não descrever como variante de outro mod.
Descartados: Rise of Animals: Ages of Earth (nome provisório de 17/10/2026); Evolution Edition; Pangaea (conflita com o tipo de mapa Pangaea do jogo e com mapas no Workshop).

## Arquivos das eras (mapeamento inicial vindo de outro projeto, só como referência; ainda não testado)
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

## Tecnologias v1 (aprovadas pela Ana, 18/10/2026)

> **Decisão:** v1 repete o mesmo nome do mod nas 8 entradas por era de `alternatenames.xml`.
**Regra.** Cada tecnologia vira uma adaptação evolutiva real ligada à função dela:
- Ciência = sentidos e cérebro.
- Comércio = simbiose, forrageio e dispersão.
- Cívica = vida em grupo (colônia, bando, manada).
- Militar = predação, mandíbulas, garras e armaduras.
- Prédios: Fort = caça e defesa; Tower = laço e território; Temple = exibição e simbiose; Lumber Mill = tocas, ninhos e florestas; Granary = pastejo e saúde; Smelter = estoque e biominerais; University = aprendizado.
Na escala de cada linha, a adaptação aparece mais ou menos na era geológica dela.
Fonte: `techrules.xml` (`<AGE>` = era em que dá para pesquisar, 0 = Ancient; `PREQ0`/`PREQ1`; `WHERE`), `typenames.xml` `<TECHS>`/`<MISC>`, `alternatenames.xml`.
**Nomes por era:** as 28 tecnologias da biblioteca têm 8 nomes cada em `alternatenames.xml` (`ALTERNATENAMES`), um por era em que o jogador está quando pesquisa. Ex.: Written Word aparece como "Education" no Classical. As tecnologias de prédio têm 8 entradas em `ALTERNATENAMES2`, quase sempre repetidas. Proposta v1: repetir o nome do mod nas 8 entradas (são 224 + 320 strings). Nomes diferentes por era ficam para depois.
As 7 tecnologias de avanço de era (Classical Age ... Information Age) estão na seção de nomes das eras.

| Linha | Tecnologia original | Era | Equivalente evolutivo | Nome no jogo |
|---|---|---|---|---|
| Biblioteca: Ciência (sentidos e cérebro) | Written Word | Pré-cambriano (Ancient) | primeiro sistema nervoso | Nerve Net |
| Biblioteca: Ciência (sentidos e cérebro) | Mathematics | Cambriano (Classical) | olhos compostos (explosão da visão) | Eye-rithmetic |
| Biblioteca: Ciência (sentidos e cérebro) | Chemistry | Devoniano (Medieval) | olfato e quimiorrecepção | Scent-istry |
| Biblioteca: Ciência (sentidos e cérebro) | Laws of Nature | Carbonífero (Gunpowder) | ouvido para ouvir no ar | Ears of Nature |
| Biblioteca: Ciência (sentidos e cérebro) | Electricity | Triássico (Enlightenment) | bigodes sensoriais | Whisk-tricity |
| Biblioteca: Ciência (sentidos e cérebro) | Electronics | Jurássico (Industrial) | cérebro maior e visão binocular | Neuro-tronics |
| Biblioteca: Ciência (sentidos e cérebro) | Computerization | Cretáceo (Modern) | córtex para resolver problemas | Cortex-ization |
| Biblioteca: Ciência (sentidos e cérebro) | Artificial Intelligence | Cenozoico (Information) | inteligência social complexa | Natural Intelligence |
| Biblioteca: Comércio (simbiose e forrageio) | Barter | Pré-cambriano (Ancient) | troca de nutrientes entre micróbios | Microbial Barter |
| Biblioteca: Comércio (simbiose e forrageio) | Coinage | Cambriano (Classical) | biomineralização (conchas) | Shell Coinage |
| Biblioteca: Comércio (simbiose e forrageio) | Trade | Devoniano (Medieval) | dispersão por esporos | Spore Trade |
| Biblioteca: Comércio (simbiose e forrageio) | Mercantilism | Carbonífero (Gunpowder) | rede de fungos e raízes (micorriza) | Fungal Mercantilism |
| Biblioteca: Comércio (simbiose e forrageio) | Finance | Triássico (Enlightenment) | esconderijos de comida | Cache Flow |
| Biblioteca: Comércio (simbiose e forrageio) | Assembly Line | Jurássico (Industrial) | migração de manadas | Migration Line |
| Biblioteca: Comércio (simbiose e forrageio) | Globalization | Cretáceo (Modern) | flores e polinizadores pelo mundo | Global Pollination |
| Biblioteca: Comércio (simbiose e forrageio) | Global Prosperity | Cenozoico (Information) | expansão dos campos de gramíneas | Global Grasslands |
| Biblioteca: Cívica (vida em grupo) | City State | Pré-cambriano (Ancient) | colônias de micróbios | Colony State |
| Biblioteca: Cívica (vida em grupo) | Empire | Cambriano (Classical) | primeiros recifes | Reef Empire |
| Biblioteca: Cívica (vida em grupo) | Feudalism | Devoniano (Medieval) | hierarquia de dominância | Pecking Order |
| Biblioteca: Cívica (vida em grupo) | Divine Right | Carbonífero (Gunpowder) | direito do macho alfa | Alpha Right |
| Biblioteca: Cívica (vida em grupo) | Constitution | Triássico (Enlightenment) | regras da manada | Herd Constitution |
| Biblioteca: Cívica (vida em grupo) | Great Power | Jurássico (Industrial) | caça em bando | Pack Power |
| Biblioteca: Cívica (vida em grupo) | International Law | Cretáceo (Modern) | mutualismo entre espécies | Inter-species Law |
| Biblioteca: Cívica (vida em grupo) | World Government | Cenozoico (Information) | teia alimentar global | World Food Web |
| Biblioteca: Militar (garras, dentes e armaduras) | The Art of War | Pré-cambriano (Ancient) | primeiros predadores | The Art of Predation |
| Biblioteca: Militar (garras, dentes e armaduras) | Mercenaries | Cambriano (Classical) | corrida armamentista do Cambriano | Arms Race |
| Biblioteca: Militar (garras, dentes e armaduras) | Standing Army | Devoniano (Medieval) | mandíbulas | Standing Jaws |
| Biblioteca: Militar (garras, dentes e armaduras) | Conscription | Carbonífero (Gunpowder) | garras e dentes em terra | Claw-scription |
| Biblioteca: Militar (garras, dentes e armaduras) | Levee en Masse | Triássico (Enlightenment) | escamas e placas ósseas | Scale en Masse |
| Biblioteca: Militar (garras, dentes e armaduras) | Nation-in-Arms | Jurássico (Industrial) | espinhos, placas e chifres | Nation-in-Armor |
| Biblioteca: Militar (garras, dentes e armaduras) | Selective Service | Cretáceo (Modern) | seleção natural | Natural Selective Service |
| Biblioteca: Militar (garras, dentes e armaduras) | Missile Shield | Cenozoico (Information) | espinhos de defesa (tipo porco-espinho) | Quill Shield |
| Fort: táticas | Tactics | Devoniano (Medieval) | táticas de caça em bando | Pack Tactics |
| Fort: táticas | Operations | Carbonífero (Gunpowder) | emboscada | Ambush Operations |
| Fort: táticas | Strategy | Jurássico (Industrial) | predador de topo | Apex Strategy |
| Fort: fortificação | Fortification | Devoniano (Medieval) | carapaça | Carapace Fortification |
| Fort: fortificação | Bombardment | Carbonífero (Gunpowder) | queda de rochas | Rockfall Bombardment |
| Fort: fortificação | Strategic Reserves | Jurássico (Industrial) | reservas de gordura | Fat Reserves |
| Tower: lealdade | Allegiance | Cambriano (Classical) | seleção de parentesco | Kin-legiance |
| Tower: lealdade | Oath of Fealty | Devoniano (Medieval) | casal fiel | Pair Bond |
| Tower: lealdade | Patriotism | Triássico (Enlightenment) | territorialidade | Territorialism |
| Tower: lealdade | Nationalism | Cretáceo (Modern) | marcação por cheiro | Scent Marking |
| Temple: crença | Religion | Cambriano (Classical) | rituais de exibição | Ritual Display |
| Temple: crença | Monotheism | Carbonífero (Gunpowder) | dança de corte | Courtship Dance |
| Temple: crença | Existentialism | Jurássico (Industrial) | instinto de sobrevivência | Ex-stinct-ialism |
| Temple: impostos | Taxation | Cambriano (Classical) | classificação dos seres vivos | Tax-onomy |
| Temple: impostos | Vassalage | Devoniano (Medieval) | comensalismo | Commensalism |
| Temple: impostos | Social Contract | Triássico (Enlightenment) | mutualismo | Mutualism Contract |
| Temple: impostos | Income Tax | Jurássico (Industrial) | roubo de comida (cleptoparasitismo) | Klepto-tax |
| Lumber Mill: construção | Construction | Cambriano (Classical) | construção de recifes | Reef Construction |
| Lumber Mill: construção | Architecture | Devoniano (Medieval) | arquitetura de tocas | Burrow Architecture |
| Lumber Mill: construção | Engineering | Triássico (Enlightenment) | engenharia de ninhos | Nest Engineering |
| Lumber Mill: madeira | Carpentry | Devoniano (Medieval) | primeiras florestas | First Forests |
| Lumber Mill: madeira | Logging Industry | Carbonífero (Gunpowder) | pântanos de carvão | Coal Swamps |
| Lumber Mill: madeira | Papermill | Jurássico (Industrial) | vespa que faz papel mastigando madeira | Wasp Papermill |
| Granary: saúde | Herbal Lore | Cambriano (Classical) | pastejo de algas | Algae Lore |
| Granary: saúde | Medicine | Carbonífero (Gunpowder) | imunidade | Immunity |
| Granary: saúde | Pharmaceuticals | Jurássico (Industrial) | resistência a toxinas de plantas | Detox-ceuticals |
| Granary: comida | Agriculture | Devoniano (Medieval) | pastejo | Grazing |
| Granary: comida | Crop Rotation | Carbonífero (Gunpowder) | dispersão de sementes | Seed Dispersal |
| Granary: comida | Food Industry | Jurássico (Industrial) | cultivo de fungos (cupins e formigas) | Fungus Farming |
| Smelter: suprimento | Forage | Devoniano (Medieval) | forrageio | Foraging |
| Smelter: suprimento | Supply | Carbonífero (Gunpowder) | estoque de comida | Food Stores |
| Smelter: suprimento | Logistics | Jurássico (Industrial) | rotas de migração | Migration Logistics |
| Smelter: metal | Metal Alloys | Carbonífero (Gunpowder) | biominerais | Biomineral Alloys |
| Smelter: metal | Cold Casting | Triássico (Enlightenment) | sangue frio | Cold-blood Casting |
| Smelter: metal | Steel | Jurássico (Industrial) | esmalte dos dentes | Enamel Steel |
| University | Literacy | Devoniano (Medieval) | comportamento aprendido | Learned Behaviour |
| University | Printing Press | Carbonífero (Gunpowder) | estampagem (imprinting) | Imprinting Press |
| University | Scientific Method | Triássico (Enlightenment) | tentativa e erro | Trial-and-Error Method |
| University | Institutional Research | Jurássico (Industrial) | aprendizado social | Social Learning |
| University | Supercomputers | Cretáceo (Modern) | supercórtex | Supercortex |
| Senate: governos | Despotism | Cambriano (Classical) | dominância | Dominance |
| Senate: governos | Republic | Cambriano (Classical) | bando que decide junto | Flock Republic |
| Senate: governos | Monarchy | Carbonífero (Gunpowder) | rainha da colmeia | Hive Monarchy |
| Senate: governos | Democracy | Carbonífero (Gunpowder) | abelhas que votam no ninho novo | Swarm Democracy |
| Senate: governos | Socialism | Jurássico (Industrial) | eussocialidade | Colony Socialism |
| Senate: governos | Capitalism | Jurássico (Industrial) | acumuladores | Hoarder Capitalism |

### Pontos em aberto (tecnologias)
- Nomes por era (`alternatenames.xml`): repetir um nome só (v1) ou criar 8 variantes por tecnologia?
- Os textos de ajuda em `help.xml` descrevem os efeitos com palavras do jogo original ("Taxation", "Armies"...) e precisam ser revisados junto.
- Testar se nomes longos ("Natural Selective Service", "Trial-and-Error Method") cabem no botão da biblioteca.
- Os governos ficaram com nomes de comportamento animal; os líderes de governo das unidades genéricas (Despo-trodon etc.) continuam como estão.

## Nomes das eras v2 (aprovados pela Ana, 18/10/2026)

> **Decisão:** ficam os nomes recomendados (em negrito): The Primordial Age, The Cambrian Explosion, The Age of Fins, The Coal Forest Age, The Triassic Dawn, The Jurassic Heights, The Cretaceous Bloom, The Cenozoic Rise.
Critério: trocadilho só onde soa natural. O resto usa nomes reais da geologia, que já soam épicos e combinam com o estilo realista. Nunca juntar "Jurassic" com "Park" ou "World".
**Onde fica o texto:**
- Classical a Information: `typenames.xml` `<AGES>` (7 hashes, ex.: 8843171 = Classical Age) e os mesmos hashes em `string_lookup.xml`, que também traz as formas curtas ("Classical") e frases como "Peace until Classical Age".
- Ancient não tem tecnologia nem entrada em `<AGES>`. O texto dele fica em `translated_strings.xml` (hashes 38905808, 62458517, 28576951 = "Ancient Age"; 53140139 = "0 - Ancient Age"), em `string_lookup.xml` (5622063 = "Ancient Age"; 2415994 = "Ancient") e em cerca de 20 textos de `help.xml`.
- A descrição de cada era iria nos textos de ajuda das tecnologias de era em `help.xml` (confirmar a entrada) ❓.

| # | Era RoN | Atual | Recomendado | Alternativas | Descrição no jogo |
|---|---|---|---|---|---|
| 1 | Ancient | The Pre-cram-brian Age | **The Primordial Age** | The Pre-Cambrian Dawn; The Age of Ooze | Soft-bodied life drifts and crawls over microbial mats in warm, shallow seas. |
| 2 | Classical | The Cam-bring-it Age | **The Cambrian Explosion** | The Cam-bring-it Age; The Age of Eyes | Shells, eyes and claws appear almost at once, and predator and prey race to outgrow each other. |
| 3 | Medieval | The Fin-tastic Devonian | **The Age of Fins** | The Fin-tastic Devonian; The Devonian Shore | Jawed fish rule the seas while the first forests and four-limbed pioneers reach the shore. |
| 4 | Gunpowder | The Car-bone-iferous Age | **The Coal Forest Age** | The Car-bone-iferous Age; The Age of Giant Wings | Steaming swamps of giant ferns, oxygen-rich air, metre-long dragonflies and the first reptiles. |
| 5 | Enlightenment | The Triassic Dawn | **The Triassic Dawn** (mantém) | The Age of Reptiles; The Great Recovery | Life rebuilds after the Great Dying: early dinosaurs, mammal ancestors and sea reptiles spread across one supercontinent. |
| 6 | Industrial | The Jurass-kick Age | **The Jurassic Heights** | The Jurass-kick Age; The Age of Titans | Long-necked giants browse conifer forests, while the first birds take to the air. |
| 7 | Modern | The Cre-tail-ceous Age | **The Cretaceous Bloom** | The Cre-tail-ceous Age; The Last Roar | Flowers spread across the land, horned and armored giants roam, and the skies fill with wings, until the sky falls. |
| 8 | Information | The Zen-ozoic Age | **The Cenozoic Rise** | The Zen-ozoic Age; The Age of Fur and Feather | The survivors inherit the Earth: grasslands, ice sheets, giant mammals and terror birds. |
Obs.: "The Cenozoic Rise" ecoa o "Rise of Nations". "The Primordial Age" evita "Dawn" repetido com o Triássico.

### Pontos em aberto (eras)
- ~~A seção "Eras (proposta inicial)" lá em cima continua com os nomes antigos.~~ Resolvido: valem os nomes v2 aprovados (The Primordial Age, The Cambrian Explosion, The Age of Fins, The Coal Forest Age, The Triassic Dawn, The Jurassic Heights, The Cretaceous Bloom, The Cenozoic Rise).
- Confirmar no jogo onde aparece a descrição de cada era.

## Biomas dos mapas v1 (aprovados pela Ana, 18/10/2026)
**Regra.**
- Cada um dos 17 tilesets vira um bioma pré-histórico genérico, sem época marcada, porque o terreno não muda com a era e qualquer nação joga em qualquer mapa. A biologia das unidades segue a era.
- Árvores e florestas (que dão Timber) usam só grupos de plantas que existem desde o Devoniano/Carbonífero e sobrevivem até hoje (licófitas, cavalinhas, samambaias-arbóreas, ginkgos, cicadáceas, coníferas, os "fósseis vivos" das plantas). Assim servem da era 3 à 8.
- Limitação aceita: no Pré-cambriano e no Cambriano ainda não havia plantas em terra.
- Tilesets que **dividem a mesma textura** (chão ou árvore) recebem a mesma pintura. Só o que é exclusivo de um tileset pode virar coisa própria.
- Visual realista. Nomes no jogo em inglês.

### Fontes conferidas (18/10/2026)
- Copiados do laptop da Ana só para leitura, com aprovação dela, e extraídos em `/workspace/ron-data/terrain/`: `Data/tilesets.xml`, `Data/Cliffs.xml`, `Data/rivers.xml` e 22 arquivos em `mapstyles/`.
- Lista completa da pasta `terrain art` com tamanhos: `/workspace/ron-data/terrain-art-files.tsv`, com 1070 arquivos.
- Nomes na tela dos tilesets ficam em `translated_strings.xml`. Hashes: Snowy 15002569, Dirty 14955539, South West Desert 47901748, Great Sahara Desert 57623020, Jungle 16609325, African Savannah 47634745, Arctic 17377676, Mongolian Steppe 44766474, Autumn 16821430, Dirty 2 18448526, Early Autumn 31980934, Late Autumn 28913524, Mongolian Steppe 2 50453617, Mongolian Steppe 3 50483610, Mongolian Steppe Autumn 73939619, Tropical 22031543, Tropical Wet 32368533. As chaves internas (`snowy`, `m_steppe_2`...) ficam em `string_lookup.xml` e **não** se mexe nelas.

### O que cada tileset usa de verdade (`tilesets.xml`)
Todos os tilesets usam o mesmo fundo de mar (`ocean_floor_5`), as mesmas cores de mar no minimapa (`0x12aff8`/`0x064764`), a mesma decoração de chão (`T_Flat_Land_Deco_*`) e o mesmo toco (`art/doober_stumps.tga`). O minimapa da floresta é `0x425542`, menos no grupo da selva (`0x313501`).

| Tileset | Pasta (BASEDIR) | 4 texturas-base | Costa | Penhasco de montanha | Rio | Estradas Middle / Late | Fazenda | Luz (tint R,G,B) | Montanha no minimapa | Neve |
|---|---|---|---|---|---|---|---|---|---|---|
| Snowy | snowy | s_browngrass, s_browngrass_snow, s_snow_browngrass, s_snow | coastal | s_ | m_ | s_ / s_ | farm_snowy_wheat_1 | 0,9,38 (azulada) | 0xD2C9A6 | picos e prédios |
| arctic | arctic | arctic1–4 | coastal | arctic_ | arctic_ | arctic_ / arctic_ | farm_snowy_wheat_1 | 0,9,38 | 0xDDD3AF | picos e prédios |
| Dirty | dirty | grass, grass_dirt, dirt_grass, dirt | sand | t_ | d_ | d_ / d_ | farm_wheat_1 | 18,18,0 (amarelada) | 0x857f69 | picos |
| Dirty_2 | dirty | grass_2, grass_dirt_2, dirt_grass_2, dirt_2 | sand | t_ | d_ | d_ / d_ | farm_wheat_1 | 18,18,0 | 0x857f69 | picos |
| autumn | dirty | grass/dirt `_autumn` | sand | t_ | d_ | autumn_ / d_ | farm_wheat_1 | 18,18,0 | 0x857f69 | picos |
| early_autumn | dirty | grass/dirt `_early_autumn` | sand | t_ | d_ | autumn_ / d_ | farm_wheat_1 | 18,18,0 | 0x857f69 | picos |
| late_autumn | dirty | grass/dirt `_autumn_snow` | sand | t_ | d_ | autumn_ / d_ | farm_wheat_1 | 18,18,0 | 0x857f69 | picos |
| SW_Desert | sw_desert | swgrass, swgrass_dirt, swdirt_grass, swdirt | coastal | sw_ | d_ | m_ / m_ | farm_wheat_1 | 38,29,0 (quente) | 0x000000 | não |
| GS_Desert | GS_Desert | GS_desertsand, _sandgrass, _grasssand, _grass | coastal | gs_ | d_ | m_ / m_ | farm_wheat_1 | 38,29,0 | 0xB2AB8D | não |
| african_savannah | african_savannah | savannah_clear, _undergrowth, _bushes, _rocky | coastal | as_ | d_ | m_ / d_ | farm_wheat_1 | 38,29,0 | 0x926a00 | não |
| jungle | jungle | b_jungle1–4 | coastal | j_ | j_ | j_ / j_ | farm_jungle_wheat_1 | 20,20,0 | 0x857f69 | não |
| tropical | jungle | c_jungle1–4 | coastal | tropical_ | j_ | j_ / j_ | farm_jungle_wheat_1 | 20,20,0 | 0x857f69 | não |
| tropical_wet | jungle | wetlands_0–3 | coastal | tropical_ | j_ | j_ / j_ | farm_jungle_wheat_1 | 20,20,0 | 0x857f69 | não |
| m_steppe | m_steppe | mongolia1–4 | coastal | m_ | m_ | gs_ / d_ | farm_wheat_1 | 5,0,15 (fria) | 0x75705c | picos |
| m_steppe_autumn | m_steppe | mongolia1–4 `_c` | coastal | m_ | m_ | gs_ / d_ | farm_wheat_1 | 5,0,15 | 0x75705c | picos |
| m_steppe_2 | m_steppe | mongolia4_b, 2_b, 1_b, 3_b | coastal | s_ (o do Snowy) | m_ | gs_ / d_ | farm_wheat_1 | 5,0,15 | 0x75705c | picos |
| m_steppe_3 | m_steppe | mongolia4_b, 1_b, 1_b, 2_b | coastal | s_ (o do Snowy) | m_ | gs_ / d_ | farm_wheat_1 | 5,0,15 | 0x75705c | picos |

Observações:
- **Árvores.** O `tilesets.xml` não diz qual modelo de árvore cada tileset usa. A ligação abaixo vem dos nomes das pastas e arquivos ❓:
  - `dirty/dtrees`: `tree_t` serve Dirty e Dirty_2. `tree_ta`, `tree_tea` e `tree_tla` servem autumn, early_autumn e late_autumn. As árvores baixas são `dirty_`, `dirtyautumn_` e `dirtylateautumn_low_trees`.
  - `jungle/jtrees` serve jungle. `jungle/tropical_trees` serve provavelmente tropical e tropical_wet.
  - `m_steppe/mtrees`: as texturas sem `_b` servem m_steppe e m_steppe_autumn; as com `_b` servem m_steppe_2 e m_steppe_3.
  - Uma pasta cada: `snowy/strees`, `arctic/arctictrees` (`tree_a_*`), `SW_desert/swtrees` (com `TreeL_sw`), `GS_Desert/gstrees` e `african_savannah/astrees`.
- **Moitas, pedras e pedra de mina.** SW_Desert, GS_Desert, jungle, tropical, tropical_wet e african_savannah apontam para `tilesets\sw_desert\swdoobers\...`. **Essa pasta não existe na lista de arquivos** ❓. Os objetos de verdade parecem ser os de `common/common_doobers`, um jogo por prefixo: `d_`, `s_`, `sw_`, `gs_`, `as_`, `j_`, `autumn_`.
- **Plantas de flor na água.** Os enfeites de rio são taboa (`*_riverdoober_cat_texture`) e vitória-régia (`*_riverdoober_lilly_texture`), que são plantas com flor e só aparecem no Cretáceo. Trocar por cavalinhas na margem e por musgo/alga boiando.
- **Penhascos** (`Cliffs.xml`): os sprites de penhasco ficam em `cliffs/` e são **iguais para todos os tilesets**. Cada tileset só troca a textura de encosta de montanha (`common_mountains/<prefixo>_mountain_cliff`).
- **Petróleo e terreno áspero:** `common_doobers/<prefixo>_rough` e `_rough_oil`. A fazenda também usa as camadas `farm_animals`/`farm_j_animals` e `farm_wheat`/`farm_j_wheat`.
- `weatherbase` e `riverbase` (valores 0–3) variam por tileset; o efeito deles não está documentado ❓.

### Que tipo de mapa usa qual tileset (`mapstyles/*.xml`, campo TILECHANCE)
| Tipo de mapa | Tilesets (chance %) |
|---|---|
| SAHARA | GS_Desert 100 |
| NILEDELTA | GS_Desert 100 (mapa com muita água) |
| SOUTHWESTMESA | SW_Desert 100 |
| HIMALAYAS | Snowy 50, arctic 50 |
| AFRICA | african_savannah 100 |
| AMAZON | jungle, tropical e tropical_wet (100 cada; sorteio entre os três ❓) |
| BRITISHISLES | Dirty 60, Snowy 40 |
| COLONIALPOWERS | Dirty, Snowy, SW_Desert, jungle (25 cada) |
| EASTINDIES | jungle 20, tropical 15, tropical_wet 15, SW_Desert 25, Dirty 25 |
| OUTBACK | autumn, SW_Desert, Dirty, jungle (25 cada) |
| SEAPOWER | Dirty, Snowy, GS_Desert, SW_Desert, jungle (20 cada) |
| WARRINGSTATES | Dirty, african_savannah, arctic, Snowy (25 cada) |
| GREATLAKES e NEWWORLD | autumn, early_autumn, late_autumn, Dirty_2, Dirty, Snowy, m_steppe (10 cada); m_steppe_2, m_steppe_3, arctic, jungle, SW_Desert, GS_Desert (5 cada) |
| default | Dirty, Snowy, jungle, SW_Desert, GS_Desert (18 cada), arctic 10 |
| greatlakes_trial | Dirty 100 |
| MEDITERRANEAN, OLDWORLD, EASTWEST, CONQUESTMAP, CONQUESTMAPSEA, EDITORMAP | sem TILECHANCE; provavelmente usam o default ou o tileset vem de fora ❓ |

O que isso mostra:
- **Dirty** é o tileset mais visto (está em 9 tipos de mapa). Snowy, jungle e SW_Desert vêm logo atrás. Esses quatro são a prioridade de arte.
- **m_steppe_autumn não aparece em nenhum tipo de mapa** (talvez só em cenário ou no editor ❓). m_steppe, m_steppe_2, m_steppe_3, early_autumn, late_autumn e Dirty_2 só aparecem no sorteio de GREATLAKES e NEWWORLD. tropical e tropical_wet aparecem só em AMAZON e EASTINDIES. Esses podem esperar.
- O jogo tem mais tipos de mapa do que os 22 arquivos; os que não têm arquivo próprio provavelmente usam o default ❓.

### Os 17 biomas (corrigido com os dados reais)
| Tileset (interno) | Nome atual na tela | Onde aparece | Bioma pré-histórico | Florestas (Timber) | Nome no jogo |
|---|---|---|---|---|---|
| Snowy | Snowy | Himalayas, British Isles, Colonial, Sea Power, Warring States, default | litoral de gelo derretendo, lama com geada | Glossopteris e coníferas baixas | Frost Flats |
| arctic | Arctic | Himalayas, Warring States, default | manto de gelo | coníferas anãs e musgo congelado | Glacial Waste |
| Dirty | Dirty | o mais comum | lodaçal de maré com tapete de micróbios e margens verdes | bosques de Archaeopteris e Calamites (a mesma árvore do Dirty_2) | Primordial Mudflats |
| Dirty_2 | Dirty 2 | Great Lakes, New World | planície de inundação de delta | a mesma do Dirty | River Delta |
| autumn | Autumn | Outback, Great Lakes, New World | bosque de ginkgos dourados | ginkgos | Ginkgo Woodland |
| early_autumn | Early Autumn | Great Lakes, New World | planalto seco com cicadáceas | cicadáceas e bennettitales | Cycad Uplands |
| late_autumn | Late Autumn | Great Lakes, New World | bosque coberto de cinza vulcânica (a textura original é de neve; a cinza cinzenta aproveita isso) | ginkgos queimados | Ashfall Woodland |
| SW_Desert | South West Desert | Southwest Mesa e mais 5 | mesetas de rocha vermelha do interior do supercontinente | coníferas esparsas tipo araucária | Red Bed Mesas (era "Red Bed Desert") |
| GS_Desert | Great Sahara Desert | Sahara, Nile Delta, Sea Power, default | mar de dunas com oásis | araucárias em oásis | Great Dune Sea |
| african_savannah | African Savannah | Africa, Warring States | savana de samambaias (antes do capim) | araucárias espalhadas | Fern Savanna |
| jungle | Jungle | Amazon, East Indies, Colonial, Outback, Sea Power, default | pântano da floresta de carvão | Lepidodendron e Sigillaria | Coal Forest Swamp |
| tropical | Tropical | Amazon, East Indies | litoral quente de samambaias-arbóreas | samambaias-arbóreas (Psaronius) | Tree Fern Coast |
| tropical_wet | Tropical Wet | Amazon, East Indies | brejo de cavalinhas gigantes | samambaias-arbóreas, as mesmas do tropical (a árvore é dividida); as cavalinhas ficam no chão e na margem | Horsetail Marsh |
| m_steppe | Mongolian Steppe | Great Lakes, New World | planalto seco com moitas de cicadáceas | cicadáceas e coníferas baixas (a mesma árvore do Moss Steppe) | Cycad Steppe |
| m_steppe_autumn | Mongolian Steppe Autumn | nenhum tipo de mapa | estepe fria de musgo | a mesma do m_steppe | Moss Steppe |
| m_steppe_2 | Mongolian Steppe 2 | Great Lakes, New World | planalto de lava basáltica | coníferas resistentes | Basalt Plateau |
| m_steppe_3 | Mongolian Steppe 3 | Great Lakes, New World | encosta de basalto, a mesma pintura do Basalt Plateau | as mesmas do m_steppe_2 | Basalt Foothills (era "Salt Lake Shore") |
Obs.: nenhum bioma tem capim, porque as gramíneas só se espalham no Cenozoico. Pedras ficam pedras. Moitas viram touceiras de samambaia. Tocos viram tocos de licófita (Stigmaria). Taboa e vitória-régia saem dos rios.

### Estradas e chão das cidades por etapa (corrigido)
O que os arquivos mostram:
- **Chão embaixo dos prédios (ALPHAELEM) não muda com a era.** Os 7 tamanhos (TwoByTwo até SevenBySeven e NineByFive) usam `age0_22.tga` em `age0`, `age1` e `age2`. Uma textura só para o jogo inteiro.
- **Calçamento em volta (WEATHERELEM) tem 3 etapas:** Rough (`base_0_0/0_1`, age 0), Cobble (`base_1_0/1_1`, age 1) e Modern (`Modern_Weathering`, age 2).
- **Estradas têm 4 nomes de etapa:**
  - Early: `Roads/Early_Road` e `Early_Road_Pieces`, uma para todos os tilesets.
  - Middle e Late: uma de cada por grupo de tileset, em `common_roads`. Os prefixos de Middle são 7 (`s`, `d`, `autumn`, `m`, `gs`, `j`, `arctic`) e os de Late são 5 (`s`, `d`, `m`, `j`, `arctic`). Existem ainda `Roads/Middle_Road`, `Late_Road` e `SW_Middle_Road` genéricas.
  - Modern: só peças, `Modern_Road_Pieces`.
  - As caravanas têm peças Middle, Late e Modern.
- **Qual era liga cada etapa não está em nenhum arquivo copiado** ❓. Isso deve estar no executável. Hipótese, como nos prédios: etapa 1 = Ancient–Medieval, 2 = Gunpowder–Enlightenment, 3 = Industrial–Information. Confirmar numa partida.

| Etapa | Estrada | Calçamento em volta (WEATHERELEM) | Placas de rua |
|---|---|---|---|
| Early | Mud Trail: rastros de arraste e trilhas de vermes na lama | Rough: rocha nua com tapete de micróbios | sem placa (ou pedras empilhadas) |
| Middle | Game Trail: trilha batida com pegadas | Cobble: lama pisoteada com pegadas | pedras marcadas com cheiro |
| Late | Migration Route: corredor largo de terra compactada | Cobble (a mesma da etapa anterior) | pilhas de ossos |
| Modern | Migration Route larga, com cascalho de ossos | Modern: terra batida com fragmentos de osso e concha | pilhas de ossos |
| (todas) | — | Chão embaixo dos prédios (`age0_22`): uma pintura só, tapete de musgo e folhiço | — |
Os nomes das estradas não aparecem na tela (só arte); "Mud Trail", "Game Trail" e "Migration Route" são nomes de trabalho.

### Repintar ou só renomear
- **Só renomear (texto):** os 17 nomes de tileset em `translated_strings.xml`.
- **Contagem real da pasta `terrain art`:** 1070 arquivos. São 730 TGA (569 de cor e 161 `_mtrl` de material), 16 PNG, 323 modelos `.bh3` e 1 arquivo de dados de ponte.

| Subpasta | Arquivos | Texturas de cor | `_mtrl` | Modelos .bh3 | MB |
|---|---|---|---|---|---|
| raiz | 57 | 38 | 19 | 0 | 12,8 |
| Roads/ | 22 | 13 | 9 | 0 | 5,6 |
| cliffs/ | 124 | 124 | 0 | 0 | 0,3 |
| transitions/ | 32 | 32 (16 TGA + 16 PNG) | 0 | 0 | 1,6 |
| rivers/ | 54 | 9 | 0 | 45 (enfeites de rio) | 1,4 |
| newwater/ | 32 | 32 | 0 | 0 | 2,1 |
| tilesets/ (raiz) | 14 | 8 | 6 | 0 | 9,8 |
| tilesets/common/common_doobers | 64 | 64 | 0 | 0 | 6,3 |
| tilesets/common/common_mountains | 69 | 35 | 34 | 0 | 18,1 |
| tilesets/common/common_rivers | 16 | 16 | 0 | 0 | 3,2 |
| tilesets/common/common_roads | 24 | 12 | 12 | 0 | 6,3 |
| tilesets/dirty (+ dtrees) | 115 | 61 | 23 | 30 | 57,9 |
| tilesets/jungle (+ jtrees, tropical_trees) | 108 | 34 | 14 | 60 | 38,0 |
| tilesets/m_steppe (+ mtrees) | 74 | 30 | 14 | 30 | 32,4 |
| tilesets/snowy (+ strees) | 51 | 15 | 6 | 30 | 13,1 |
| tilesets/arctic (+ arctictrees) | 51 | 15 | 6 | 30 | 13,7 |
| tilesets/SW_desert (+ swtrees) | 59 | 17 | 6 | 36 | 12,3 |
| tilesets/GS_Desert (+ gstrees) | 48 | 15 | 6 | 27 | 13,2 |
| tilesets/african_savannah (+ astrees) | 56 | 15 | 6 | 35 | 13,4 |
| **Total** | **1070** | **585** | **161** | **323** | **~262** |

- **Riscos de textura dividida:**
  - A pasta `dirty/` serve 5 tilesets (Dirty, Dirty_2 e os três autumn). `jungle/` serve 3 e `m_steppe/` serve 4.
  - Dirty e Dirty_2 dividem a árvore. tropical e tropical_wet dividem a árvore e o penhasco.
  - m_steppe_2 e m_steppe_3 dividem quase todo o chão (três texturas `_b` iguais) e a árvore. Por isso a ideia de "lago salgado" saiu: ela pediria um chão branco, que mudaria o Basalt Plateau também.
  - O penhasco `s_mountain_cliff` serve Snowy, m_steppe_2 e m_steppe_3, então tem que ser neutro, de rocha escura com pouca neve. `t_mountain_cliff` serve os 5 tilesets da pasta `dirty/`.
  - As estradas Late `d_` servem Dirty, autumn, savana e os quatro m_steppe. As estradas `m_` servem os dois desertos e a savana. As `gs_` Middle servem os m_steppe.
  - Os rios `d_` servem Dirty e os desertos e a savana. Os rios `m_` servem Snowy e os m_steppe.
  - Comuns a todos os tilesets: `ocean_floor_5`, decoração `T_Flat_Land_*`, `doober_stumps`, sprites de penhasco, `age0_22`, `base_*`, `Modern_Weathering`.
- **Outros riscos:**
  - Os modelos de árvore (`.bh3`) mantêm o formato (copa redonda); só a pintura muda, então "samambaia-arbórea" fica limitada pela silhueta.
  - Legibilidade: floresta, água rasa e terreno aberto precisam continuar fáceis de distinguir.
  - Formato e tamanho dos TGA e canal alfa têm que ser os mesmos.
  - Não está confirmado se um mod consegue sobrescrever `terrain art/`.
  - Cores de minimapa e luz estão no `tilesets.xml` e dá para ajustar, mas isso é editar dado do jogo, que fica para a fase de mod, não agora.

### Bichos de caça e cenário

> **Decisão da Ana (18/10/2026):** os bichos de cenário usam **modelos novos** (feitos no Blender, ver "Rota de modelos") com as espécies da tabela, incluindo os bípedes Mei long, Caudipteryx e Beipiaosaurus; não é só repintura. Aves e baleia podem começar repintando os modelos existentes.
O que os dados mostram (`unitrules.xml` e `unit_graphics.xml`):
- São 12 bichos com máscara de nação 0 (nenhuma nação produz), 1 de vida, sem ataque.
- **O RoN não tem caça.** Comida vem de fazenda e de pesca. Os rebanhos são enfeite em volta dos recursos raros. A ligação recurso → bicho vem só dos nomes; não está em nenhum XML da caixa e deve estar no executável ❓.
- O peixe fica no ponto de pesca (BONUS "Fish" dos mapstyles). Os barcos de pesca tiram comida dali.
- Existe ainda `HERDSEALS` (foca) em `unit_graphics.xml`, mas sem linha em `unitrules.xml`. Talvez não seja usado ❓.
- Nenhum bicho abaixo é dinossauro reservado, bicho-símbolo de nação ou unidade já usada.
- A arte é uma só para o jogo inteiro, então a escolha vai para bichos "de fundo" que não marcam uma era famosa.

| Original (gráfico) | O que faz no jogo | Variantes por tileset hoje | Substituto pré-histórico | Nome no jogo | Neve / variantes novas |
|---|---|---|---|---|---|
| Wild Bird (WILDBIRD) | pássaro solto voando, só cenário | dirty, snow (Snowy e arctic), african (savana e GS), amer (jungle) | pterossauro pequeno comedor de insetos (anurognatídeo) | Wild Pterowing | 4 pinturas, como hoje: marrom, cinza-claro (neve), areia, verde |
| Flock Bird (FLOCKBIRD) | bando voando, só cenário | normal, african | bando de pterossauros pequenos (Eudimorphodon) | Ptero Flock | normal e savana; na neve usa a normal |
| Gull Bird (GULLBIRD) | gaivota da costa, só cenário (voa em rasantes) | nenhuma | pterossauro pescador de costa (Anhanguera, do Ceará) | Gull-hanguera | não precisa |
| Farm Pig (FARMPIG, 2 tipos) | porco da fazenda, só enfeite | nenhuma (camada `farm_animals`/`farm_j_animals` no chão) | dicinodonte pequeno (Diictodon) | Diicto-hog | não precisa; repintar as 2 camadas de fazenda |
| Farm Chicken (FARMCHICKEN, galinha e galo) | galinha da fazenda, só enfeite | nenhuma | dinossauro emplumado pequeno (Mei long) | Mei-hen | fêmea apagada e macho colorido, como galinha e galo |
| Herd Horse (HERDHORSES, 3 tipos) | rebanho do recurso Horses → **Wild Herds** (Stable mais barato) | nenhuma | cavalo de três dedos (Mesohippus) | Wild Meso-herd | não precisa |
| Herd Sheep (HERDSHEEP, 3 tipos) | rebanho do recurso Wool → **Down** (Citizens mais baratos e rápidos) ❓ | nenhuma | ceratopsiano pequeno de quatro patas (Leptoceratops) | Lepto-flock | não precisa |
| Herd Bison (HERDBISON, 3 tipos) | rebanho do recurso Bison → **Grazer Herds** (Granary mais barato) | nenhuma | dicinodonte grande (Kannemeyeria) | Kanne-grazer | não precisa |
| Herd Bear (HERDBLACKBEAR, filhote + 2 adultos) | bicho do recurso Furs → **Feathers** (militar e visão) ❓ | arctic (`blackbear_snowy`) | terizinossauro pequeno emplumado (Beipiaosaurus) | Feather-bear | versão de neve com plumagem clara e grossa |
| Herd Peacock (HERDPEACOCKS, 3 tipos) | bando do recurso Peacocks → **Courtship Plumes** (população) | nenhuma | dinossauro emplumado com leque na cauda (Caudipteryx) | Plume-tail | não precisa |
| Herd Fish (HERDFISH, 3 tipos) | cardume no ponto de pesca (comida dos barcos de pesca) → recurso **Plankton** | normal (Dirty), salmon (Snowy e arctic), mahi (savana, GS, jungle) | normal: cardume de peixinhos (Leptolepis); frio: belemnites; quente: amonites pequenas | Bait Shoal / Belemnite Swarm / Coil Shoal | 3 pinturas, como hoje; só na água |
| Herd Whales (HERDWHALES) | grupo do recurso Whales → **Ichthyosaur Pods** (navios mais rápidos) | nenhuma | ictiossauro comum (Stenopterygius) | Steno-pod | só na água |
| (Herd Seals, sem regra) | foca, uso incerto ❓ | nenhuma | paquipleurossauro pequeno (Keichousaurus), na água ou na beira | Keicho-pup | só água e beira |

Observações:
- **Modelos.** Os pássaros e a baleia podem ser repintados em cima do modelo atual (asas e corpo de nadador batem). Porco, bisão e cavalo têm silhueta de quadrúpede parecida com dicinodonte, Kannemeyeria e Mesohippus, mas o resto precisa de modelo novo.
- **Bípedes.** Galinha, pavão e urso viram dinossauros de duas patas, e o urso é o caso mais difícil. Se a Ana quiser só repintar, o urso pode virar Amphicyon (cão-urso do Cenozoico, silhueta igual), mas aí não combina com "Feathers".
- **Fazenda.** A plantação da fazenda (`farm_wheat`, `farm_j_wheat`, `farm_*_wheat_1`) é trigo, ou seja, capim. Isso é da seção de construções (já aprovada); só registro aqui.

### Pontos em aberto
- Ligação era → etapa das estradas e do calçamento: não está nos arquivos; confirmar numa partida.
- A pasta `sw_desert/swdoobers`, citada por 6 tilesets, não existe na lista de arquivos. Ver no jogo quais moitas e pedras aparecem nesses tilesets.
- Qual pasta de árvore cada tileset usa (inferido pelos nomes) e se tropical e tropical_wet usam `tropical_trees`.
- Os 6 mapstyles sem TILECHANCE (Mediterranean, Old World, East-West, Conquest, Editor) e os tipos de mapa sem arquivo próprio: de onde vem o tileset?
- m_steppe_autumn não aparece em nenhum tipo de mapa: vale repintar agora?
- Ligação recurso raro → bicho (Wool = ovelha, Furs = urso) e se a foca é usada.
- ~~Bichos de cenário: só repintar ou fazer modelos novos para os bípedes?~~ Resolvido: modelos novos para os 13, incluindo os bípedes (ver "Bichos de cenário prontos").
- Versões de neve das unidades genéricas (Citizen, Caravan, Merchant, Scout, Commando...): fazer arte de neve ou apontar para a normal.

## Bichos de cenário prontos (aprovados pela Ana, 18/10/2026)
Todos os 13 foram feitos no Blender, aprovados pela Ana pelas prévias e instalados no mod de teste `mods/Ages of Earth - Model Test/` (pasta `art/` com 50 arquivos + `Data/unit_graphics.xml`). Cada modelo mantém o esqueleto original (nomes, ordem e pose de descanso dos ossos), 1 osso por vértice, 1 textura e malha triangulada, para as animações originais (.BHa) continuarem servindo. O teste no jogo dos modelos novos ainda está pendente ❓ (o bisão de ida e volta já foi visto funcionando no jogo).

| Bicho | Nome no jogo | Unidade original (arquivos em art/) | Observações |
|---|---|---|---|
| Kannemeyeria | Kanne-grazer | Herd Bison (`bison.BH3`, `bison2.BH3`, `Bison.tga`) | os dois modelos de bisão trocados; a maioria dos rebanhos usa o `bison2` (macho) |
| Diictodon | Diicto-hog | Farm Pig (`pig.BH3`, `pig_black.BH3`, `pig.tga`, `pig_black.tga`) | 2 pelagens |
| Mesohippus | Wild Meso-herd | Herd Horse (`Wildhorse_1/3/4.BH3`, `WildHorses.tga`) | v2 aprovada; escala no `unit_graphics.xml` de 0.9 para **0.55** (cavalo de três dedos é pequeno) |
| Leptoceratops | Lepto-flock | Herd Sheep (`sheep1-3.BH3`, `sheep.tga`) | v2 aprovada (a v1 parecia lontra) |
| anurognatídeo | Wild Pterowing | Wild Bird (`bird_dirty/snow/african.BH3` + 4 texturas, incluindo `bird_amer.tga`) | 4 pinturas por tileset, como no original |
| Eudimorphodon | Ptero Flock | Flock Bird (`flock.BH3`, `flock.tga`, `flock_african.tga`) | normal e savana |
| Anhanguera | Gull-hanguera | Gull Bird (`bird_gul.BH3`, `bird_gul.tga`) | pterossauro pescador do Ceará |
| Leptolepis / belemnites / amonites | Bait Shoal | Herd Fish (`fish1.BH3`, `fish2.BH3`, `fish_belem.bh3`, `fish_coil.bh3`, 3 texturas) | o jogo tem um nome só por tipo, então os 3 cardumes ficam como Bait Shoal; belemnites (neve/ártico) e amonites (savana, GS, selva) usam modelos novos via `unit_graphics.xml`; só na água |
| Stenopterygius | Steno-pod | Herd Whales (`whale.bh3`, `whale.tga`) | sem o jato do respiradouro (`WHALE_BLOWHOLE_BLOW` tirado), porque ictiossauro não tinha; só na água |
| Mei long | Mei-hen | Farm Chicken (`hen.BH3`, `rooster.BH3`, `fowls.tga`) | fêmea apagada e macho colorido |
| Caudipteryx | Plume-tail | Herd Peacock (`Peacock.BH3`, `Peahen.BH3`, `peafowl.tga`) | leque de penas na cauda |
| Beipiaosaurus | Feather-bear | Herd Bear (`blackbear.BH3`, `blackbear_cub.BH3`, `blackbear_snowy.bh3`, `blackbear_cub_snowy.bh3` + 4 texturas) | v2 aprovada; feito no **esqueleto do peahen** e o `unit_graphics.xml` aponta o HERDBLACKBEAR para as animações do Peahen (escala 1 no filhote e 1.3 nos adultos, sombra de bípede); versão de neve nova; **troca de animação não testada no jogo** ❓ |

Obs.: Keicho-pup (foca) continua sem lugar: o HERDSEALS não tem regra em `unitrules.xml` nem string própria.
Arquivos de trabalho (scripts do Blender, MAPPING e prévias finais) ficam no repositório em `art-src/`.

## Rota de modelos: Blender + RoN File Converter (18/10/2026)
- Converter BH3/BHa para glTF e de volta com o **RoN File Converter** (código público do ptasev no GitHub). A Ana baixa e compila por conta própria; o conversor **nunca** é redistribuído nem entra no mod ou no repositório.
- Não fazemos engenharia reversa de formato nenhum: só usamos a ferramenta pública.
- No laptop: `~/.dotnet/dotnet ~/tools/ron-file-converter/ron-file-converter/ron-file-converter.dll bh3|gltf <arquivo>`.
- Blender roda sem interface, por script: `flatpak run --filesystem=home org.blender.Blender -b --python <caminho absoluto>`. A Ana preferiu manter assim, sem o MCP do Blender.
- Regras do modelo: mesmo esqueleto do original (nomes, ordem e pose de descanso), 1 osso por vértice, 1 textura, malha triangulada. O export do Blender reordena ossos irmãos, então a ordem original é restaurada antes de converter, e cada BH3 é relido para conferir.
- Um bicho pode usar animações de outro esqueleto pelas entradas ANIM do `unit_graphics.xml` (caso do Feather-bear).
- Arte entra no mod por nome de arquivo em `mods/<mod>/art/`, com a mesma caixa de letra do jogo. O jogo precisa ser reiniciado para ler as mudanças.

## Textos v0.2 (aprovados pela Ana, 18/10/2026; instalação adiada)
- 527 strings mudaram (`help.xml` 364, `translated_strings.xml` 163); 230 das 233 dicas e ajudas pendentes reescritas; as 8 descrições das eras escritas (help.xml LIBRARY/AGES, `AGE0`–`AGE7`, local a confirmar no jogo ❓).
- Só o texto muda: hashes e IDs mantidos, arquivos idênticos byte a byte fora do texto, CRLF, sem BOM.
- Detalhes em `docs/v0.2/REVIEW-v0.2.md` e `docs/v0.2/changes-v0.2.csv` no repositório.

### Glossário de classes de unidade (aprovado pela Ana, 18/10/2026: usar os nomes temáticos)
Vale para o help e para os rótulos de "bom contra / fraco contra" do `translated_strings.xml`.

| Original | No jogo |
|---|---|
| Light Infantry | Light Biters |
| Heavy Infantry | Heavy Brawlers |
| Infantry (sozinho) | Foot Beasts |
| Gunpowder / Musket Infantry | Spine-shooters |
| Modern Infantry | Modern Shooters |
| Foot Archers / Archers | Foot Spitters / Spitters |
| Light / Heavy / Ranged Cavalry | Light Runners / Heavy Chargers / Ranged Runners |
| Artillery (Weapons) | Siege Beasts |
| Tanks | Armorbacks |
| Machine Guns | Rapid Spitters |
| Fighter / Bomber Aircraft | Fighter Flyers / Bomber Flyers |
| Helicopters | Hoverers |
| Anti-Aircraft | Anti-Air |
| Nuclear Missiles | Extinction Events |
| Nuclear Embargo | Extinction Embargo |
| Light / Heavy / Bombardment Ships | Light / Heavy / Bombard Swimmers |
| Subs | Divers |
| Elephant | Tusker |
Palavras soltas: troops/soldiers → creatures; foot troops → ground creatures; mounted troops → runners; armies → herds; cannon(s) → sharp teeth / crushing jaws; mortars → spine volleys; explosive shells/rockets → rock volleys/barrages; arrows/bullets → spines/stingers; weapons of mass destruction → falling space rocks; General → General Tua-tactics.
Risco: rótulos mais longos podem cortar na interface; se cortar no teste, encurtar.

### Pontos em aberto (v0.2)
- Instalar a v0.2 no laptop junto com o teste dos 13 bichos (a Ana pediu para deixar para depois).
- Ainda sem tema: títulos de poder, líderes, cidades, heróis, seções AIR/SPELLS/CAPS/LANDS, mapas, Conquest, fim de jogo e campanha.
