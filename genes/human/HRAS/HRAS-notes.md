# HRAS notes

Initial Falcon pass, 2026-05-12. HRAS is a fully pending review, so I kept the
first curation pass focused on the most defensible core biology rather than
attempting all 258 annotations at once.

Core function: HRAS is a Ras-family small GTPase. UniProt summarizes that Ras
proteins bind GDP/GTP and have intrinsic GTPase activity [file:human/HRAS/HRAS-uniprot.txt
"Ras proteins bind GDP/GTP and possess intrinsic GTPase activity
(PubMed:12740440, PubMed:14500341, PubMed:9020151)."]. Falcon likewise frames
HRAS as a GDP/GTP molecular switch [file:human/HRAS/HRAS-deep-research-falcon.md
"RAS proteins (including HRAS) are **GTP hydrolases** that function as
**binary molecular switches**: GDP-bound is “OFF,” GTP-bound is “ON,” and
the ON state supports binding to downstream effector proteins."].

Core processes: Ras protein signal transduction and positive regulation of the
MAPK cascade are central. Falcon specifically recommends these as core HRAS
terms but warns against defaulting distal outcomes to core annotations
[file:human/HRAS/HRAS-deep-research-falcon.md "“Ras protein signal
transduction” and “positive regulation of MAPK cascade” are generally **core**
for HRAS, but very specific outcome terms (e.g., “cell cycle progression” as a
default) should be restricted to contexts with strong, direct, wild-type
evidence."].

Localization: HRAS membrane association is driven by CAAX processing and
palmitoylation, so plasma membrane and Golgi membrane are the safest core
locations in this first pass [file:human/HRAS/HRAS-deep-research-falcon.md
"HRAS contains a C-terminal **CAAX motif** that is post-translationally
processed by a canonical sequence: **farnesylation → AAX proteolysis (RCE1)
→ carboxymethylation (ICMT)**."].

Non-core and over-annotation cautions: proliferation, senescence, cell-cycle,
motility, transcriptional, and developmental terms are often downstream or
mutant/oncogenic-context phenotypes. PMID:9054499 is explicit that its senescence
evidence used oncogenic Ras [PMID:9054499 "Here we show that expression of
oncogenic ras in primary human or rodent cells results in a permanent G1
arrest."]. PMID:23027131 likewise uses a malignant transformation model
[PMID:23027131 "By using a model of malignant transformation induced by Ras, we
identified Wnt4 as an early target of Ras oncogenic signaling."].

PLCE1 effector branch: PMID:11022048 supports direct GTP-dependent HRAS binding
and activation of PLCepsilon, so I kept GO:0160185 as a non-core effector branch
rather than core function [PMID:11022048 "The Ras-associating domain of
PLCepsilon specifically binds to the GTP-bound forms of Ha-Ras and Rap1A."].

Left for later: most generic protein binding annotations remain PENDING. The
right follow-up is to replace individual generic protein-binding rows with
specific effector-binding terms only where there is direct, nucleotide-state
dependent binding evidence.
