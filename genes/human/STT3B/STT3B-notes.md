# STT3B (Q8TCJ2) — gene review notes

## Identity
- Human **STT3B**, HGNC:30611, UniProt **Q8TCJ2**, 826 aa, chromosome 3.
- RecName: *Dolichyl-diphosphooligosaccharide--protein glycosyltransferase subunit STT3B*; EC **2.4.99.18**. AltName SIMP ("Source of immunodominant MHC-associated peptides homolog").
- Multi-pass ER membrane protein; STT3 family; CAZy GT66; belongs to glycosyltransferase family 39 (GT39). [file:human/STT3B/STT3B-uniprot.txt]

## Core biology
STT3B is the **catalytic subunit of the STT3B-containing oligosaccharyltransferase (OST) complex (OST-B)**, one of the two human OST isoforms (OST-A carries STT3A). The OST catalyzes the central reaction of N-linked glycosylation: **en bloc transfer of the preassembled Glc3Man9GlcNAc2 glycan from dolichyl-pyrophosphate onto the asparagine of N-X-S/T (X≠P) sequons** in acceptor proteins in the ER lumen. STT3B contains the active site and the acceptor-peptide and donor lipid-linked-oligosaccharide (LLO) binding pockets; catalysis requires a divalent metal ion (Mg2+/Mn2+). [file:human/STT3B/STT3B-uniprot.txt; PMID:31831667 abstract]

- EC 2.4.99.18; Rhea:RHEA:22980; UniProt CATALYTIC ACTIVITY, evidence ECO:0000269|PubMed:19167329, 22607976, 31296534. [file:human/STT3B/STT3B-uniprot.txt]
- "Catalytic subunit of the oligosaccharyl transferase (OST) complex that catalyzes the initial transfer of a defined glycan (Glc(3)Man(9)GlcNAc(2) in eukaryotes) from the lipid carrier dolichol-pyrophosphate to an asparagine residue within an Asn-X-Ser/Thr consensus motif" [file:human/STT3B/STT3B-uniprot.txt]

### Two OST isoforms; STT3B = proofreading / post-translational second pass
- The two OST isoforms **cooperate and act sequentially**; STT3A does the bulk cotranslational glycosylation at the translocon, and **STT3B is not translocon-associated** and glycosylates sites STT3A skipped, either cotranslationally or post-translocationally. [PMID:19167329 "we show that the OST isoforms cooperate and act sequentially to mediate protein N-glycosylation"; PMID:31296534 "The STT3B complex is not associated with the translocon, yet glycosylates certain acceptor sites that have been skipped by the STT3A complex in either a cotranslational or posttranslocational mode"]
- STT3B efficiently mediates **posttranslational glycosylation of skipped sites in unfolded proteins**, including C-terminal sequons (e.g. Factor VII N360) and sequons adjacent to the N-terminal signal sequence. [PMID:19167329 "The STT3B isoform of the OST is less competent for cotranslational glycosylation, but has the capacity to mediate posttranslational modification of skipped glycosylation sites in unfolded proteins"; "The STT3B isoform is responsible for posttranslational glycosylation of FVII on N360"]
- New STT3B-dependent site class: **short loops of multi-spanning membrane proteins**. [PMID:31296534 abstract]
- STT3B-dependent glycosylation of a subset of sequons (cysteine-proximal) requires the OST-B oxidoreductase subunits **MAGT1/TUSC3**. [PMID:25135935 title "Oxidoreductase activity is necessary for N-glycosylation of cysteine-proximal acceptor sites in glycoproteins"; PMID:31296534 full text on MagT1/TUSC3 oxidoreductases]

### ER quality control / ERAD / surveillance
- STT3B-dependent post-translational N-glycosylation acts as a **surveillance/triage system for secretory proteins**, glycosylating cryptic sequons exposed during prolonged unfolding, marking them for **N-glycan-dependent ERAD (EDEM3-mediated)**. Demonstrated for the amyloidogenic TTR variant (Asp-38) glycosylated at Asn-118, leading to degradation. [PMID:22607976 abstract "prolonged TTR unfolding induces externalization of cryptic N-glycosylation site and triggers STT3B-dependent posttranslational N-glycosylation ... an alternative pathway for degradation, which is EDEM3-mediated N-glycan-dependent ERAD"; file:human/STT3B/STT3B-uniprot.txt "Plays a role in ER-associated degradation (ERAD) pathway"]
- Note: loss of **STT3A** (not STT3B) induces the UPR in the Ruiz-Canada study. [PMID:19167329 "Depletion of STT3A, but not STT3B, causes an induction of the unfolded protein response (UPR) pathway"]. The UniProt "response to unfolded protein" annotations (GO:0006986, IMP, PMID:19167329/22607976) are best read as STT3B participating in the ER protein-homeostasis/surveillance response rather than STT3B loss triggering the UPR; kept as non-core.

### Regulated N-glycosylation (Rohatgi 2024)
- N-glycosylation by OST-A is **regulated by specificity factors**: an N-terminal peptide of HSP90B1 (GRP94) templates a translocon complex containing CCDC134 + OST-A that protects HSP90B1 during folding, preventing hyperglycosylation and degradation; disruption impairs WNT/IGF1R signaling and causes **osteogenesis imperfecta**. STT3B is the paralogous catalytic subunit and is used here as one of the two OSTs; the GRP94 hyperglycosylation phenotype is chiefly STT3B-dependent (GRP94 hyperglycosylated in STT3A-deficient cells by STT3B). [PMID:39509507 abstract; PMID:31296534 "GRP94 was hyperglycosylated"/"hyperglycosylated in STT3A-deficient cells"]

## Localization / complex
- **ER membrane**, multi-pass (13 predicted TM helices in UniProt topology). [file:human/STT3B/STT3B-uniprot.txt SUBCELLULAR LOCATION "Endoplasmic reticulum ... Endoplasmic reticulum membrane; Multi-pass membrane protein"]
- Component of the **oligosaccharyltransferase complex**; two complexes OST-A/OST-B; core subunits RPN1, RPN2, OST48, OST4, DAD1, TMEM258; OST-B adds MAGT1 or TUSC3. Modeled as membership of GO:0008250 (and the more specific GO:0160227 oligosaccharyltransferase complex B) via `in_complex`. [file:human/STT3B/STT3B-uniprot.txt SUBUNIT; ComplexPortal CPX-5622 / CPX-8738]
- Cryo-EM structure 6S7T (OST-B). [file:human/STT3B/STT3B-uniprot.txt; PMID:31831667]

## Disease
- **CDG1X / STT3B-CDG** (MIM:615597), a congenital disorder of glycosylation. [file:human/STT3B/STT3B-uniprot.txt DISEASE; PMID:23842455 (not cached; UniProt INVOLVEMENT IN CDG1X)]

## Annotation review reasoning highlights
- Core MF: **GO:0004579** dolichyl-diphosphooligosaccharide-protein glycotransferase activity (multiple IDA/IMP: PMID:19167329, 22607976, 31296534, 39509507). ACCEPT the experimental ones; redundant IEA/ISS/IBA of the same term also ACCEPT (own correct core MF).
- **GO:0004576** oligosaccharyl transferase activity (IEA, InterPro): parent/less-informative than GO:0004579 → MODIFY to GO:0004579.
- Core BP: **GO:0006487** protein N-linked glycosylation (IDA/IMP). Also the two dolichol-transfer children GO:0180057 (post-translational) and GO:0180058 (co-translational) capture STT3B's specific mechanistic roles (FlyBase IMP, PMID:19167329) — ACCEPT (post-translational is the more distinctive STT3B role; co-translational is genuine but secondary).
- **GO:0043687** post-translational protein modification: retained as non-core (it is a high-level parent; the specific STT3B post-translational role is GO:0180057).
- **GO:0009101** glycoprotein biosynthetic process (IEA InterPro): true but less-informative parent of N-linked glycosylation → non-core.
- **GO:0036503** ERAD pathway (IMP, PMID:22607976) and **GO:0006516** glycoprotein catabolic process (IMP, PMID:22607976): supported by the TTR surveillance work; STT3B contributes indirectly (glycan-tagging for ERAD) → non-core.
- **GO:0006986** response to unfolded protein (IMP): keep as non-core; STT3B participates in ER protein-homeostasis surveillance, but UPR induction in Ruiz-Canada is specifically STT3A-dependent.
- CC: **GO:0005789** ER membrane (correct core location, many redundant sources incl. experimental EXP/IDA for GO:0005783 ER) → ACCEPT. **GO:0016020** membrane (IEA/HDA): correct but uninformative parent → non-core.
- **GO:0008250** oligosaccharyltransferase complex (many sources) and **GO:0160227** oligosaccharyltransferase complex B (IDA, PMID:31831667): ACCEPT (core complex membership; B-specific term is the most precise).
- **GO:0032991** protein-containing complex (IDA, PMID:28246125, ZMPSTE24 paper): uninformative high-level complex term → non-core / over-annotated.
- **GO:0005515** protein binding (4 × IPI): bare, uninformative. RPN1 (P04843) partner (PMID:19167329, 35271311) is a bona fide OST subunit interaction; INCA1 (Q0VD86, PMID:32296183) and histone (PMID:30021884) interactions are HT screens. Per policy, MARK_AS_OVER_ANNOTATED (never REMOVE IPI protein binding).
