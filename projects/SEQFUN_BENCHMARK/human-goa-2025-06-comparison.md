# Condition comparison: human-goa-2025-06

| condition | targets yes | NOT targets yes | decoys yes |
|---|---|---|---|
| agent-review claude-opus-5-5 | 10/50 | 1/1 | not asked |
| blind claude-fable-5-2 | 32/50 | 1/1 | 1/72 |
| blind-opus claude-opus-5-5 | 28/50 (5 uncertain) | 1/1 | 3/72 (6 uncertain) |
| organism claude-fable-5-2 | 31/50 (1 missing) | 1/1 | 1/72 |
| organism-opus claude-opus-5-5 | 28/50 (7 uncertain) | 1/1 | 6/72 (3 uncertain) |

## Targets yes, split by whether the baseline input already entails them

7 of 50 targets are entailed by a term (any evidence code) in the baseline GOA file that the agent-review condition was given. A review scores yes on these by keeping a row it was handed; the peptalk conditions never see that file.

| condition | in baseline input (n=7) | not in baseline input (n=43) |
|---|---|---|
| agent-review claude-opus-5-5 | 7/7 | 3/43 |
| blind claude-fable-5-2 | 7/7 | 25/43 |
| blind-opus claude-opus-5-5 | 6/7 | 22/43 (5 uncertain) |
| organism claude-fable-5-2 | 7/7 | 24/43 (1 missing) |
| organism-opus claude-opus-5-5 | 6/7 | 22/43 (7 uncertain) |

## Targets yes, by GO aspect

| condition | C | F | P |
|---|---|---|---|
| agent-review claude-opus-5-5 | 4/11 | 2/15 | 4/24 |
| blind claude-fable-5-2 | 8/11 | 11/15 | 13/24 |
| blind-opus claude-opus-5-5 | 5/11 (3 uncertain) | 10/15 | 13/24 (2 uncertain) |
| organism claude-fable-5-2 | 6/11 | 11/15 (1 missing) | 14/24 |
| organism-opus claude-opus-5-5 | 6/11 (1 uncertain) | 9/15 (2 uncertain) | 13/24 (4 uncertain) |

## Per target

Y yes, n no, ? uncertain, - missing. Columns: 1 = agent-review claude-opus-5-5; 2 = blind claude-fable-5-2; 3 = blind-opus claude-opus-5-5; 4 = organism claude-fable-5-2; 5 = organism-opus claude-opus-5-5.

| gene | term | role | aspect | in baseline input | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|---|---|---|
| LRP4 | GO:0001618 virus receptor activity | TARGET | F |  | n | n | n | - | n |
| TGDS | GO:0005794 Golgi apparatus | TARGET | C |  | n | n | n | n | ? |
| TGDS | GO:0006024 glycosaminoglycan biosynthetic process | TARGET | P |  | n | n | n | n | ? |
| TGDS | GO:0008460 dTDP-glucose 4,6-dehydratase activity | NEGATED_TARGET | F | yes | Y | Y | Y | Y | Y |
| TGDS | GO:0050377 UDP-glucose 4,6-dehydratase activity | TARGET | F |  | n | Y | n | Y | n |
| ALDOA | GO:0035774 positive regulation of insulin secretion involved in cellular response to glucose stimulus | TARGET | P |  | n | n | n | n | n |
| MPO | GO:0006337 nucleosome disassembly | TARGET | P |  | n | Y | Y | Y | Y |
| MPO | GO:0031491 nucleosome binding | TARGET | F |  | n | Y | Y | Y | ? |
| MPO | GO:0140776 protein-containing complex destabilizing activity | TARGET | F |  | n | Y | Y | Y | Y |
| LAMP2 | GO:0160020 positive regulation of ferroptosis | TARGET | P |  | n | Y | Y | Y | Y |
| SLC25A16 | GO:1990559 mitochondrial coenzyme A transmembrane transport | TARGET | P | yes | Y | Y | Y | Y | Y |
| SYK | GO:0034165 positive regulation of toll-like receptor 9 signaling pathway | TARGET | P |  | n | Y | Y | Y | Y |
| ARRB1 | GO:0001678 intracellular glucose homeostasis | TARGET | P |  | n | n | ? | n | n |
| ARRB1 | GO:0007166 cell surface receptor signaling pathway | TARGET | P |  | n | Y | Y | Y | Y |
| ARRB1 | GO:0035721 intraciliary retrograde transport | TARGET | P |  | n | n | n | n | Y |
| ARRB1 | GO:1903568 negative regulation of protein localization to ciliary membrane | TARGET | P |  | n | Y | Y | Y | Y |
| GSK3B | GO:0032374 regulation of cholesterol transport | TARGET | P |  | n | n | ? | n | ? |
| WHR1 | GO:0000993 RNA polymerase II complex binding | TARGET | F |  | n | Y | Y | Y | Y |
| WHR1 | GO:0006283 transcription-coupled nucleotide-excision repair | TARGET | P |  | Y | Y | Y | Y | Y |
| WHR1 | GO:0008023 transcription elongation factor complex | TARGET | C |  | n | Y | ? | Y | n |
| WHR1 | GO:0062058 transcription factor TFIIH holo complex binding | TARGET | F |  | n | Y | Y | Y | Y |
| IDH3G | GO:0001917 photoreceptor inner segment | TARGET | C |  | n | n | ? | n | n |
| SUCLG1 | GO:0004776 succinate-CoA ligase (GDP-forming) activity | TARGET | F | yes | Y | Y | Y | Y | Y |
| SUCLG1 | GO:0006108 malate metabolic process | TARGET | P |  | n | n | n | n | n |
| SUCLG1 | GO:0016878 acid-thiol ligase activity | TARGET | F | yes | Y | Y | Y | Y | Y |
| SUCLG1 | GO:0050074 malate-CoA ligase activity | TARGET | F |  | n | n | n | n | Y |
| SUCLG1 | GO:0110052 toxic metabolite repair | TARGET | P |  | n | Y | n | n | n |
| VLDLR | GO:0001618 virus receptor activity | TARGET | F |  | n | Y | Y | Y | Y |
| TRIM28 | GO:0000785 chromatin | TARGET | C | yes | Y | Y | Y | Y | Y |
| TRIM28 | GO:0043124 negative regulation of canonical NF-kappaB signal transduction | TARGET | P |  | n | n | Y | n | ? |
| SKIC2 | GO:0070481 nuclear-transcribed mRNA catabolic process, non-stop decay | TARGET | P |  | Y | Y | Y | Y | Y |
| ZFYVE26 | GO:0042802 identical protein binding | TARGET | F |  | n | n | n | n | n |
| MRGPRE | GO:0001678 intracellular glucose homeostasis | TARGET | P |  | n | n | n | Y | ? |
| MRGPRE | GO:0005886 plasma membrane | TARGET | C | yes | Y | Y | Y | Y | Y |
| MRGPRE | GO:0007166 cell surface receptor signaling pathway | TARGET | P |  | n | Y | Y | Y | Y |
| MRGPRE | GO:0007189 adenylate cyclase-activating G protein-coupled receptor signaling pathway | TARGET | P |  | n | n | n | n | n |
| MRGPRE | GO:0035774 positive regulation of insulin secretion involved in cellular response to glucose stimulus | TARGET | P |  | n | n | n | Y | n |
| MRGPRE | GO:0038182 G protein-coupled bile acid receptor activity | TARGET | F |  | n | n | n | n | n |
| MRGPRE | GO:0038184 adenylate cyclase-activating G protein-coupled bile acid receptor signaling pathway | TARGET | P |  | n | n | n | n | n |
| STING1 | GO:0015485 cholesterol binding | TARGET | F |  | n | Y | Y | Y | Y |
| STING1 | GO:0036020 endolysosome membrane | TARGET | C |  | n | Y | Y | n | Y |
| STING1 | GO:0080025 phosphatidylinositol-3,5-bisphosphate binding | TARGET | F |  | n | Y | Y | Y | Y |
| PLD5 | GO:0005739 mitochondrion | TARGET | C |  | n | n | n | n | n |
| ULK4 | GO:0030674 protein-macromolecule adaptor activity | TARGET | F |  | n | Y | Y | Y | ? |
| ULK4 | GO:0045880 positive regulation of smoothened signaling pathway | TARGET | P |  | n | Y | Y | Y | Y |
| ULK4 | GO:0097542 ciliary tip | TARGET | C |  | n | Y | Y | Y | Y |
| ERLEC1 | GO:0000836 Hrd1p ubiquitin ligase complex | TARGET | C |  | Y | Y | Y | Y | Y |
| ERLEC1 | GO:0034099 luminal surveillance complex | TARGET | C |  | n | Y | ? | n | Y |
| MYD88 | GO:0034162 toll-like receptor 9 signaling pathway | TARGET | P |  | n | Y | Y | Y | Y |
| POPDC2 | GO:0002027 regulation of heart rate | TARGET | P | yes | Y | Y | Y | Y | Y |
| KLK11 | GO:0005794 Golgi apparatus | TARGET | C | yes | Y | Y | n | Y | n |
