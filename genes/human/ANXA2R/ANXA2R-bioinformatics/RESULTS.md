# ANXA2R ortholog check (PANTHER PTHR38820)

Script: `panther_orthologs.py` (UniProt REST query `xref:panther-PTHR38820`, with each entry's NCBI taxonomic lineage tested for Mammalia; run 2026-10-04).

Purpose: test the statement in PMID:23640736 that "AXIIR gene is peculiar to human".

Output:

```
UniProt entries in PTHR38820: 92
distinct organisms: 57
organisms whose lineage includes Mammalia: 57
organisms outside Mammalia: []
  Mammalia	Balaenoptera acutorostrata (Common minke whale) (Balaena rostrata)
  Mammalia	Balaenoptera musculus (Blue whale)
  Mammalia	Balaenoptera physalus (Fin whale) (Balaena physalus)
  Mammalia	Callorhinus ursinus (Northern fur seal)
  Mammalia	Camelus ferus (Wild bactrian camel) (Camelus bactrianus ferus)
  Mammalia	Catagonus wagneri (Chacoan peccary)
  Mammalia	Ceratotherium simum simum (Southern white rhinoceros)
  Mammalia	Cercocebus atys (Sooty mangabey) (Cercocebus torquatus atys)
  Mammalia	Chlorocebus sabaeus (Green monkey) (Simia sabaea)
  Mammalia	Crocuta crocuta (Spotted hyena)
  Mammalia	Equus asinus (Donkey) (Equus africanus asinus)
  Mammalia	Equus caballus (Horse)
  Mammalia	Equus przewalskii (Przewalski's horse) (Equus caballus przewalskii)
  Mammalia	Eschrichtius robustus (California gray whale) (Eschrichtius gibbosus)
  Mammalia	Galeopterus variegatus (Malayan flying lemur) (Cynocephalus variegatus)
  Mammalia	Gorilla gorilla gorilla (Western lowland gorilla)
  Mammalia	Homo sapiens (Human)
  Mammalia	Lipotes vexillifer (Yangtze river dolphin)
  Mammalia	Loxodonta africana (African elephant)
  Mammalia	Macaca fascicularis (Crab-eating macaque) (Cynomolgus monkey)
  Mammalia	Macaca mulatta (Rhesus macaque)
  Mammalia	Mus caroli (Ryukyu mouse) (Ricefield mouse)
  Mammalia	Mus musculus (Mouse)
  Mammalia	Mus spicilegus (Mound-building mouse)
  Mammalia	Myotis davidii (David's myotis) (Vespertilio davidii)
  Mammalia	Nasalis larvatus (Proboscis monkey)
  Mammalia	Neogale vison (American mink) (Mustela vison)
  Mammalia	Neophocaena asiaeorientalis asiaeorientalis (Yangtze finless porpoise) (Neophocaena phocaenoides subsp. asiaeorientalis)
  Mammalia	Nyctereutes procyonoides (Raccoon dog) (Canis procyonoides)
  Mammalia	Odobenus rosmarus divergens (Pacific walrus)
  Mammalia	Pan paniscus (Pygmy chimpanzee) (Bonobo)
  Mammalia	Pan troglodytes (Chimpanzee)
  Mammalia	Panthera leo (Lion)
  Mammalia	Papio anubis (Olive baboon)
  Mammalia	Peromyscus maniculatus bairdii (Prairie deer mouse)
  Mammalia	Phocoena sinus (Vaquita)
  Mammalia	Phyllostomus discolor (pale spear-nosed bat)
  Mammalia	Physeter macrocephalus (Sperm whale) (Physeter catodon)
  Mammalia	Piliocolobus tephrosceles (Ugandan red Colobus)
  Mammalia	Pipistrellus nathusii (Nathusius' pipistrelle)
  Mammalia	Pongo abelii (Sumatran orangutan) (Pongo pygmaeus abelii)
  Mammalia	Prolemur simus (Greater bamboo lemur) (Hapalemur simus)
  Mammalia	Pteropus vampyrus (Large flying fox)
  Mammalia	Rhinolophus ferrumequinum (Greater horseshoe bat)
  Mammalia	Sapajus apella (Brown-capped capuchin) (Cebus apella)
  Mammalia	Sciurus carolinensis (Eastern gray squirrel)
  Mammalia	Sciurus vulgaris (Eurasian red squirrel)
  Mammalia	Semnopithecus entellus (Northern plains gray langur) (Presbytis entellus)
  Mammalia	Spermophilus dauricus (Daurian ground squirrel)
  Mammalia	Sus scrofa (Pig)
  Mammalia	Theropithecus gelada (Gelada baboon)
  Mammalia	Trichechus manatus latirostris (Florida manatee)
  Mammalia	Tupaia chinensis (Chinese tree shrew) (Tupaia belangeri chinensis)
  Mammalia	Tursiops truncatus (Atlantic bottle-nosed dolphin) (Delphinus truncatus)
  Mammalia	Ursus maritimus (Polar bear) (Thalarctos maritimus)
  Mammalia	Vicugna pacos (Alpaca) (Lama pacos)
  Mammalia	Zalophus californianus (California sealion)
```

Conclusion: ANXA2R family members are present in 57 organisms, every one of them in class Mammalia by NCBI lineage, including mouse Anxa2r. The gene is mammal-specific, not human-specific.

PAINT note: PTHR38820 has no PAINT annotations because the family has no propagatable experimental GO annotation. The only experimental row on human ANXA2R is a GO:0005515 protein binding IPI, which PAINT does not propagate. A lack of characterised non-human members is not the reason; an IBD seeded on a human experimental annotation would propagate.
