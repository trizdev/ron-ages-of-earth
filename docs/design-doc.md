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

## Distribuição das nações v0.1 (aprovada pela Ana, 17/10/2026; conferir bônus reais no mapeamento)
1. Aves: Mongols, Lakota, Persians
2. Mamíferos: Russians, Bantu, Iroquois
3. Crocodilos: Egyptians, Nubians, Maya
4. Tartarugas: Chinese, Koreans, Dutch
5. Lagartos e cobras: Aztecs, Incas, Indians
6. Anfíbios: British, Japanese, Spanish
7. Insetos: Romans, Germans, Americans
8. Aracnídeos: Turks, Greeks, French

## Nações v1: bicho-símbolo e nome (aprovadas pela Ana, 17/10/2026)
| Linhagem | Nação RoN | Bicho-símbolo | Nome no jogo |
|---|---|---|---|
| Aves | Mongols | Velociraptor | The Veloci-Horde |
| Aves | Lakota | Ave-do-terror | The Terror-tory |
| Aves | Persians | Archaeopteryx | The Feather-sian Empire |
| Mamíferos | Russians | Mamute | The Mam-moth-erland |
| Mamíferos | Bantu | Dentes-de-sabre | The Fang-tu Kingdom |
| Mamíferos | Iroquois | Castor gigante (Castoroides) | The Beaver-quois League |
| Crocodilos | Egyptians | Sarcosuchus | The Nile-osaurus Dynasty |
| Crocodilos | Nubians | Deinosuchus | The Deino-Nubian Kingdom |
| Crocodilos | Maya | Postosuchus | The Croco-Maya |
| Tartarugas | Chinese | Meiolania (tartaruga com chifres) | The Great Shell of China |
| Tartarugas | Koreans | Proganochelys | The Turtle-ship Kingdom |
| Tartarugas | Dutch | Stupendemys | The Shell-lands |
| Lagartos e cobras | Aztecs | Titanoboa | The Boa-ztec Empire |
| Lagartos e cobras | Incas | Megalania | The In-claw Empire |
| Lagartos e cobras | Indians | Gigantophis | The Hiss-tory Raj |
| Anfíbios | British | Mastodonsaurus | The United King-frog |
| Anfíbios | Japanese | Salamandra-gigante | The Salamander Shogunate |
| Anfíbios | Spanish | Beelzebufo (rã gigante) | The Frog-quistadors |
| Insetos | Romans | Titanomyrma (formiga gigante) | The Ant-perium Romanum |
| Insetos | Germans | Besouro | The Beetle Confederation |
| Insetos | Americans | Abelha | The United Bee-states |
| Aracnídeos | Turks | Escorpião gigante | The Scorpi-Ottoman Empire |
| Aracnídeos | Greeks | Escorpião-do-mar | Arachn-Athens |
| Aracnídeos | French | Aranha | The Web-public of France |
