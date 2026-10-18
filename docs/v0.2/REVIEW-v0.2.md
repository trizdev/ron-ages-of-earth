# Ages of Earth v0.2 (só texto): proposta para revisão

**Status:** só proposta. Nada foi instalado no laptop e nada foi commitado.
**Base:** cópia da v0.1, com os nomes curtos das nações já corrigidos. A pasta v0.1 não foi alterada nem refeita.
**Como refazer:** rode `python3 build/build_v02.py`. O script recopia `v0.1/Data` e `v0.1/tribes` e aplica as regras de `build/help_rules.py` e `build/ts_map.py`. Para conferir, rode `build/verify.py`.

## Contagens
- **527 strings mudaram, todas listadas em `changes-v0.2.csv`.**
  - `help.xml`: 364 strings. Por seção: UNITS 245, TIPS 54, BUILDINGS 29, TRIBES 14, LIBRARY 9, ACHIEVECHART 9, GAMESPYQM 2, STATS 1, GOODS 1.
  - `translated_strings.xml`: 163 strings.
  - `typenames.xml`, `string_lookup.xml`, `alternatenames.xml` e `tribes/`: iguais à v0.1, sem nenhuma mudança.
- **Lista de ajuda pendente (`help-todo.csv`):** 230 das 233 entradas foram reescritas. As 3 que ficaram foram mantidas de propósito:
  - TRIBE2 ("Power of Gold"): os títulos de poder ainda não foram decididos.
  - TRIBE4 e LIBRARY/COMMERCE: "Caravan Limit" é o nome de um indicador da interface.
- **Validação:**
  - Todos os XML fazem parse.
  - Fora do texto dentro de `<STRING>`, os arquivos são idênticos byte a byte aos da v0.1. As tags internas (`<BULLET/>`, comentários) seguem na mesma ordem.
  - Não há BOM, e todas as quebras de linha continuam CRLF.
  - Variáveis `$...`, `#ICON..` e `%` foram preservadas em todas as strings.
  - A única diferença de `{}` é proposital, na dica T29: "{Siege} and {Artillery} units" virou "{Siege Beasts}".

## 1. Bichos de cenário
Os 12 nomes do doc **já estavam na v0.1** (`typenames.xml`) e foram conferidos um por um com a tabela:

| Original | No jogo |
|---|---|
| Wild Bird | Wild Pterowing |
| Flock Bird | Ptero Flock |
| Gull Bird | Gull-hanguera |
| Farm Pig | Diicto-hog |
| Farm Chicken | Mei-hen |
| Herd Horse | Wild Meso-herd |
| Herd Sheep | Lepto-flock |
| Herd Bison | Kanne-grazer |
| Herd Bear | Feather-bear |
| Herd Peacock | Plume-tail |
| Herd Fish | Bait Shoal (o jogo tem um nome só por tipo, então Belemnite Swarm e Coil Shoal não têm onde entrar) |
| Herd Whales | Steno-pod |

O que a v0.2 acrescenta é o texto em volta deles:
- "Build Fishermen (at a Dock) to gather Fish and Whale resources." → "Build Nauti-fishers (at a Tide-dock) to gather Plankton and Ichthyosaur Pod resources."
- "Fish/Whale Sparsity:" → "Plankton/Pod Sparsity:" (opção da tela de configuração).
- "Fishermen:" e "Idle Fishermen:" → "Nauti-fishers:" e "Idle Nauti-fishers:".
- Dica T5: "Silk, Wine, and Horses" → "Spider Silk, Fermented Fruit, and Wild Herds".

**Recursos raros:** batem com o doc (Grazer Herds, Wild Herds, Down, Feathers, Courtship Plumes, Ichthyosaur Pods etc.). Os 6 que o doc manda manter (Sulphur, Amber, Diamonds, Obsidian, Coal, Gypsum) continuam como estão. O help.xml não tem texto próprio para cada recurso raro.

**Keicho-pup (foca):** continua sem lugar, porque não existe string para ela.

## 2. Descrições das eras
**Onde ficam:** `help.xml` LIBRARY/AGES, nas entradas `AGE0` a `AGE7`. São os tooltips dos botões de avanço de era na Fossil Record. Cada entrada já citava o ícone e o nome da era em questão, então é quase certo que é esse texto que aparece ao passar o mouse no botão. **Ainda falta confirmar no jogo** ❓.

A primeira frase das entradas antigas era repetida e falava em "history". Ela virou: "{Age} advances carry your lineage through deep time; each one unlocks new creatures and habitats." Depois dela vem o texto abaixo, que junta a descrição do doc com o efeito real no jogo:

1. **AGE0, The Primordial Age:** Most games begin in the {Primordial Age}: soft-bodied life drifts and crawls over microbial mats in warm, shallow seas. Research at the Fossil Record to evolve onward.
2. **AGE1, The Cambrian Explosion:** Advancing to the #ICON28 {Cambrian Explosion}: shells, eyes and claws appear almost at once, and predator and prey race to outgrow each other. New resources become available (#ICON4 Instinct and #ICON5 Minerals), along with the Herd Senate for government powers, Reef Forts for defense, and Stampede Pens and Rockfall Works for powerful new kinds of units.
3. **AGE2, The Age of Fins:** Advancing to the #ICON29 {Age of Fins}: jawed fish rule the seas while the first forests and four-limbed pioneers reach the shore. Your creatures gain stronger jaws and armor, and you can raise Horseshoe Supply Wagons to support them and Chamele-spies to subvert your enemies.
4. **AGE3, The Coal Forest Age:** Advancing to the #ICON30 {Coal Forest Age}: steaming swamps of giant ferns, oxygen-rich air, metre-long dragonflies and the first reptiles. Powerful spine-shooting creatures become available.
5. **AGE4, The Triassic Dawn:** Advancing to the #ICON31 {Triassic Dawn}: life rebuilds after the Great Dying; early dinosaurs, mammal ancestors and sea reptiles spread across one supercontinent. New spine-shooters and heavy siege beasts become available.
6. **AGE5, The Jurassic Heights:** Advancing to the #ICON32 {Jurassic Heights}: long-necked giants browse conifer forests, while the first birds take to the air. Gives you access to a new resource #ICON12 (Oil) and brings Armorbacks and Flyers for the first time.
7. **AGE6, The Cretaceous Bloom:** Advancing to the #ICON33 {Cretaceous Bloom}: flowers spread across the land, horned and armored giants roam, and the skies fill with wings, until the sky falls. Unlocks powerful late-age creatures and habitats, including the power to call down Extinction Events.
8. **AGE7, The Cenozoic Rise:** Advancing to the #ICON34 {Cenozoic Rise}: the survivors inherit the Earth, with grasslands, ice sheets, giant mammals and terror birds. The game's most powerful units and buildings at last become available.

**Outros textos de era:**
- `AGETECH` (o texto genérico do botão "Age").
- Os 7 tempos de era da tabela de conquistas (ACHIEVECHART).
- O "Deathmatch" do Quick Match: "Ancient Age" virou "Primordial Age", e o "Information Age Deathmatch" virou "Cenozoic Rise Deathmatch".

## 3. Glossário de classes de unidade (decisão nova, peço sua aprovação)
O help e o painel de "bom contra / fraco contra" do jogo usavam nomes de classe militares. Troquei todos pelo mesmo glossário, tanto no help quanto nos rótulos do `translated_strings`:

| Original | Novo |
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

Também troquei algumas palavras soltas:
- troops/soldiers → creatures
- foot troops → ground creatures
- mounted troops → runners
- armies → herds
- cannon(s) → sharp teeth / crushing jaws
- mortars → spine volleys
- explosive shells/rockets → rock volleys/barrages
- arrows/bullets → spines/stingers
- weapons of mass destruction → falling space rocks
- General → General Tua-tactics (heróis únicos e o Patriot viram "leader")

Se preferir manter as classes originais, que ficam mais claras para quem já joga RoN, é só reverter esse bloco.

## 4. Amostra de reescritas do help (antes → depois)
1. **Barracks:** "Creates foot soldiers to attack your enemies." → "Creates ground creatures to attack your enemies."
2. **Auto Plant:** "Creates Tanks, Armored Cars, and other vehicle units." → "Creates Armorbacks, Armored Scale Cars, and other armored beasts."
3. **Missile Silo:** "Researches new types of missiles, including Nuclear Missiles and ICBM's." → "Researches new types of meteors, including Extinction Events and Extinction ICBMs."
4. **Maya (TRIBE1):** "fire extra arrows/bullets" → "fire extra spines/stingers".
5. **França (TRIBE10):** "Receive a free General… Horseshoe Supply Wagons heal your troops." → "Receive a free General Tua-tactics… Horseshoe Supply Wagons heal your creatures."
6. **War Deinophant:** "unique {Elephant,}… Good against close-order foot; vulnerable to light, scattered troops." → "unique {Tusker,}… Good against close-packed ground creatures; vulnerable to light, scattered creatures."
7. **Fusiliers:** "{Heavy Infantry}… short-ranged gunpowder units" → "{Heavy Brawlers}… short-ranged spine-shooters".
8. **Minuteman:** "Upgraded Militia armed with muskets." → "Upgraded Lobo-militia with sharper spines."
9. **Frigate:** "{Heavy Ships}… armed with cannons" → "{Heavy Swimmers}… armed with crushing jaws".
10. **Howitzer:** "{Artillery Weapons}… powerful explosive shells… against enemy buildings and foot troops." → "{Siege Beasts}… powerful rock volleys… against enemy buildings and ground creatures."
11. **Nuclear Missile:** "{Nuclear Missiles}… weapons of mass destruction capable of flattening several enemy buildings" → "{Extinction Events}… falling space rocks capable of flattening several enemy buildings".
12. **Helicopter:** "versatile aircraft… hunting Submarines and Tanks." → "versatile flyers… hunting Plesio-marines and Armorbacks."
13. **Manchu Infantry:** "rapid fire, small arms with excellent firepower" → "rapid, snapping jaws with excellent bite force".
14. **Athanatoi:** corrigi a era. Estava "the Cambrian Explosion #ICON29" e virou "the Age of Fins #ICON29", que é a era certa pelo ícone. Arqimmortal e os "Medieval #ICON29" que sobravam foram corrigidos do mesmo jeito.
15. **Junkers e Bandeirantes:** "Prussian Unique" e "Portuguese Unique" viraram "Scenario Unique". Os Barbarian viraram "Feral Unique".
16. **Dica T36:** "Logistics, bureaucracy, and food supply have presented significant challenges to nations throughout history." → "Feeding, sheltering, and moving a growing swarm has challenged every lineage through deep time."
17. **Dica T73:** "Senates are new buildings in Rise of Nations: Thrones and Patriots. They can be constructed after you reach the Classical Age." → "Herd Senates can be built once you reach the Cambrian Explosion."

## 5. Textos da interface (`translated_strings.xml`, 163)
- **Avisos que citam prédios, recursos ou unidades:** Fossil Record, Shell Exchange, Tide-dock, Cliff Roost, Geo-dig, Wood-chewer's Camp, Tar Pit, Paleo-versity, Herd Senate, Fern-tile Field, Hatch-ville/Grand Rookery/Megalo-polis, Citi-snail, Bookworm, Milli-peddler, Roly-Poly Caravan, Chamele-spy, Trackworm, Horseshoe Supply Wagon, Grub/Fernwood/Minerals/Shells/Instinct.
- **Vitórias:** "World Government" → "World Food Web" (19 strings). "Nuclear Victory!" → "Extinction Victory!".
- **Grupos de atalhos:** "Library Commands" → "Fossil Record Commands" etc. Os 2 espaços no começo foram mantidos.
- **Sabor:**
  - "Russian Winter" → "Ice Age" (no território da Mam-moth-erland).
  - "Egyptian City" → "Nile-osaurus City".
  - "the Terra Cotta Army." → "the Terra Fossil Army.".
  - "your troops" → "your herds" e "peaceful people" → "peaceful flock" (diplomacia).
  - O texto da Conquest "Information Age" → "Cenozoic Rise".
- "Rise of Nations: Tips" → "Ages of Earth: Tips" (título da janela de dicas, que agora são temáticas).

### "Rise of Nations" que eu mantive (são o nome do jogo de verdade)
- **translated_strings:** About Rise of Nations / Trial, lobby, Staging Room, Quick Match, Online, "Playing Rise of Nations", os títulos "Rise of Nations: Thrones and Patriots" / "Extended Edition", avisos de placa de vídeo e de som, modo 256 cores, permissão de escrita para patch, Script Editor, chat commands, o tutorial que "showcases the features of Rise of Nations", 3 títulos soltos "Rise of Nations" (39929889, 39281901, 33375419; o contexto não é claro, então não mexi) e o aviso do Steam Workshop (texto legal, não mexer).
- **Caminhos de pasta** `\Rise of Nations` e `\Rise of Nations Trial` (70843480, 103217285): **não mexer nunca**.
- **help.xml:** tutoriais e desafios ("teach you how to play Rise of Nations"), créditos ("people who created Rise of Nations"), salvar senha, lobby e a descrição do mod no Workshop.
- **Comandos que eu também não mudei:** o cheat "tech Shaggy Phalanx show", "human playername" e "Cannon Time" (nome de recurso do multiplayer).

## 6. O que ficou de fora ou está em aberto
- **Capital → "Alpha Nest":** continua "Capital" em toda parte. Falta decidir.
- **Líderes e cidades das nações, nos tribes:** não foram projetados.
- **Títulos de poder** (Power of Gold/Architecture/Trade/Empire/the Horde…): continuam os originais.
- **Heróis de campanha** (Alexander, Napoleon, Darius, Porus…) e unidades sem nação (Greek Mercenaries, Patriot, Conquistador…): o nome continua o original. Só tematizei as palavras em volta.
- **Seções do help que ainda não processei:** AIR, SPELLS, STATS (fora o Armageddon Clock), CAPS, LANDS, SETUPWIN (descrição dos mapas), EJECTS, toda a Conquest e os textos de fim de jogo (ARMAGEDDON, ALLIED_NUKE…).
- **string_lookup.xml:** campanhas e cenários com nações reais. Não mexi por causa da colisão de hashes.
- **translated_strings que sobraram:** os textos da Conquest sobre nuclear missile, "Construction"/"Supply Center", os rótulos de editor ("Base arrows"), "Ruins", "Caravan Limit", "Trade Route" e as falas de diplomacia.
- **Unidade "Transport":** continua "Transport".

## 7. Riscos
- **Rótulos curtos do painel de unidade:** alguns ficaram maiores e podem cortar na tela. Por exemplo:
  - "Tanks, Artillery, Subs" (22) → "Armorbacks, Siege Beasts, Divers" (32)
  - "Tanks, Infantry" (15) → "Armorbacks, Foot Beasts" (23)
  - "Gunpowder Infantry, Cavalry" → "Spine-shooters, Runners" (este ficou menor)

  Testar no jogo. Se cortar, encurto, por exemplo "Armor, Siege, Divers".
- **Mensagens de aviso maiores:** algumas cresceram de 10 a 23 caracteres, como "Build Nauti-fishers (at a Tide-dock) to gather Plankton and Ichthyosaur Pod resources." Elas costumam caber em uma linha, mas é bom conferir.
- **Grupos de atalho mais longos:** "Stampede Pen/Armor Molt Plant Commands" e "Rockfall Works/Fossil Factory Commands" são os maiores.
- **Glossário de classes:** se o jogo montar algum texto de classe sozinho, a partir do executável, ele vai continuar com "Infantry" e misturar com o help novo.
- **Descrições das eras:** a ligação AGE0–7 → tooltip do botão é dedução e ainda falta confirmar numa partida ❓.
- **Linhas do help.xml:** ficou com 2 linhas a menos que a v0.1, porque o texto das eras foi reescrito. Isso fica só dentro do texto e não muda a estrutura.
