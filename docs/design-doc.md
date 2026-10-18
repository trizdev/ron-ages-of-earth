# Rise of Animals: Ages of Earth (Eras da Terra) — Documento de design

Status: fase de ideias (nenhum arquivo do jogo alterado)
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
- As espécies das nações mudam por era (ex.: trilobitas no Cambriano) ou só nomes de eras/tecnologias/unidades?
- Mod separado ou opção dentro do Rise of Animals?

## Pendências
- Receber do bot Rise of Animals o documento de design e o mapeamento dos arquivos.

## Nome do mod (decidido 17/10/2026)
**Rise of Animals: Ages of Earth**
Descartados: Evolution Edition; Pangaea (conflita com o tipo de mapa Pangaea do jogo e com mapas no Workshop).

## Arquivos das eras (segundo o mapeamento do bot Rise of Animals, ainda não testado)
- Nomes das eras: Data/typenames.xml; menus de partida: Data/string_lookup.xml.
- Ancient Age não tem identificador próprio; Classical a Information ficam em techrules.xml.
- Hipótese: manter o hash e trocar só o texto (precisa testar).
- Referências: /workspace/rise-of-animals/mapeamento-jogo.md e design-doc.md (seção 26 tem as eras "natureza" da versão principal).
