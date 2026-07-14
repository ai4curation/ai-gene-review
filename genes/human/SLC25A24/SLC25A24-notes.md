# SLC25A24 (SCaMC-1 / APC1) — review notes

UniProt: Q6NUK1 (SCMC1_HUMAN). HGNC:20662. 477 aa. Human, NCBITaxon:9606.

## Identity / naming

- RecName: "Mitochondrial adenyl nucleotide antiporter SLC25A24" [file:human/SLC25A24/SLC25A24-uniprot.txt "RecName: Full=Mitochondrial adenyl nucleotide antiporter SLC25A24"].
- AltName: "Mitochondrial ATP-Mg/Pi carrier protein 1" (APC1); "Short calcium-binding mitochondrial carrier protein 1" / SCaMC-1 [file:human/SLC25A24/SLC25A24-uniprot.txt "Short=SCaMC-1"].
- Synonyms: APC1, MCSC1, SCAMC1 [file:human/SLC25A24/SLC25A24-uniprot.txt "Synonyms=APC1"].
- Member of the mitochondrial carrier (TC 2.A.29) family, SLC25 [file:human/SLC25A24/SLC25A24-uniprot.txt "Belongs to the mitochondrial carrier (TC 2.A.29) family"].

## Core molecular function — a Ca2+-regulated ATP-Mg/Pi (adenine nucleotide) antiporter

- FUNCTION: "Electroneutral antiporter that mediates the transport of adenyl nucleotides through the inner mitochondrial membrane. Originally identified as an ATP-magnesium/inorganic phosphate antiporter, it also acts as a broad specificity adenyl nucleotide antiporter. By regulating the mitochondrial matrix adenyl nucleotide pool, could adapt to changing cellular energetic demands and indirectly regulate adenyl nucleotide-dependent metabolic pathways" [file:human/SLC25A24/SLC25A24-uniprot.txt].
- In vitro also low activity with guanyl and pyrimidine nucleotides [file:human/SLC25A24/SLC25A24-uniprot.txt "In vitro, a low activity is also observed with guanyl and pyrimidine nucleotides"].
- This is a TRANSPORTER, not an enzyme — no catalytic (EC/enzymatic) MF should be assigned. The UniProt "CATALYTIC ACTIVITY" Rhea reactions are antiport half-reactions (e.g. RHEA:65840 Mg/Pi + ATP exchange), i.e. transport, not chemistry.
- PMID:15123600 (Fiermonte et al 2004): purified/reconstituted the human ATP-Mg/Pi carrier; measured KM/Vmax for AMP, ADP, ATP, ATP-Mg, Pi antiport. Abstract: "ATP-Mg is transported in exchange for phosphate... the three isoforms of the ATP-Mg/Pi carrier are most likely responsible for the net uptake or efflux of adenine nucleotides into or from the mitochondria and hence for the variation in the matrix adenine nucleotide content" [PMID:15123600]. This is the primary IDA source for the MF transporter terms (adenine nucleotide transmembrane transporter GO:0000295, ATP:phosphate antiporter GO:0140987, ADP:phosphate antiporter GO:0140988) and BP (mitochondrial ATP transmembrane transport GO:1990544, adenine nucleotide transport GO:0051503).
- PMID:22015608 (Traba et al 2012): "the mitochondrial carrier SCaMC-1/SLC25A24 mediates ATP-Mg(2-)/Pi(2-) and/or HADP(2-)/Pi(2-) uptake into the mitochondria after an increase in cytosolic [Ca(2+)]" [PMID:22015608]. Basis for GO:0005347 ATP transmembrane transporter activity (IMP) and GO:1990544 (IMP).

Best-supported core MF: GO:0005347 ATP transmembrane transporter activity (transport of ATP, the physiologically salient cargo; supported by both Fiermonte reconstitution and Traba cellular assays). The paired antiporter/phosphate terms (GO:0140987 ATP:phosphate antiporter, GO:0140988 ADP:phosphate antiporter) and adenine-nucleotide-transporter GO:0000295 capture the specific electroneutral antiport mechanism and broader substrate range; all are consistent. GO:0005509 calcium ion binding is a genuine secondary MF (regulatory EF-hands).

## Calcium regulation (secondary MF: Ca2+ binding via EF-hands)

- N-terminal regulatory domain (residues 1–173) with four EF-hands facing the intermembrane space; binds Ca2+; regulates the C-terminal carrier/transmembrane domain [file:human/SLC25A24/SLC25A24-uniprot.txt "The regulatory N-terminal domain/NTD, formed of two pairs of fused calcium-binding EF-hands, binds calcium in the mitochondrial intermembrane space"].
- Activated by a rise in cytosolic Ca2+ that induces a conformational change uncapping the channel [file:human/SLC25A24/SLC25A24-uniprot.txt "Activated by an increase in cytosolic calcium levels that induces a conformational change of the N-terminal regulatory domain, uncapping the channel and allowing transport"].
- PMID:24332718 (Yang, Brüschweiler, Chou 2014): crystal structure (2.1 Å; PDB 4N5X) of the Ca2+-bound NTD (residues 1–193); NMR + SPR. Ca2+ binding drives a conformational switch: apo NTD caps/binds TMD (inhibits transport); Ca2+-bound NTD is self-sequestered and releases TMD. Abstract: "The short Ca²⁺-binding mitochondrial carrier (SCaMC) transports ATP-Mg in exchange for Pi... Crystal structure of the Ca²⁺-bound NTD reveals a compact architecture in which the functional EF hands are sequestered by an endogenous helical segment... Ca²⁺ binding drastically weakened the interaction. Our results together provide a molecular explanation for Ca²⁺-dependent ATP-Mg flux in mitochondria" [PMID:24332718]. Primary IDA/EXP source for GO:0005509 calcium ion binding and for GO:0071277-type Ca2+ responsiveness.
- Additional structural support (not in GOA/local pubs): PMID:26164100 (Harborne et al 2015, PDB 4ZCU/4ZCV), PMID:28350015 (Harborne et al 2017, locking-pin mechanism) — cited in UniProt but not in the review set.

## Localization

- SUBCELLULAR LOCATION: "Mitochondrion inner membrane ... Multi-pass membrane protein" [file:human/SLC25A24/SLC25A24-uniprot.txt "Mitochondrion inner membrane"]. Six TM helices (TRANSMEM 198–465 region); N-terminal EF-hand domain in the intermembrane space.
- IDA localization to mitochondrion from PMID:15123600, PMID:15054102, PMID:22015608, PMID:29100093 (all human SLC25A24). PMID:15054102 (del Arco & Satrústegui 2004): "All SCaMC proteins were found to be located exclusively in mitochondria" [PMID:15054102].
- GO:0016020 membrane (IDA, PMID:24332718) is a less-informative parent of mitochondrial inner membrane — over-annotation given inner-membrane evidence.
- Core location term: GO:0005743 mitochondrial inner membrane (IEA UniProtKB-SubCell, consistent with the multi-pass carrier + literature).

## Biological process / physiology / disease

- Regulates the mitochondrial matrix adenine nucleotide pool → adapts to energetic demand; supports adenine-nucleotide-dependent processes (gluconeogenesis, mitochondrial biogenesis, mtDNA maintenance per PMID:24332718 full text).
- Ca2+-dependent matrix Ca2+ buffering via ATP/ADP: PMID:22015608 — SCaMC-1 imports ATP-Mg/ADP after cytosolic Ca2+ rise; ATP/ADP buffer matrix Ca2+, desensitizing mitochondrial permeability transition (mPT); knockdown sensitizes cells to mPT-mediated necrotic death by oxidative stress and Ca2+ overload [PMID:22015608 "Knockdown of the transporter led to vast reduction of mitochondrial Ca(2+) buffering capacity and sensitized cells to mPT-mediated necrotic death triggered by oxidative stress and Ca(2+) overload"]. Supports GO:0071277 cellular response to calcium ion (IMP).
- Oxidative stress protection: PMID:29100093 — patient fibroblasts with R217H/R217C show mitochondrial swelling exacerbated by H2O2, lower matrix ATP, increased sensitivity to oxidative stress [PMID:29100093 "mitochondrial dysfunction with increased sensitivity to oxidative stress is due to the SLC25A24 mutations"]. Supports GO:0034599 cellular response to oxidative stress (IMP) and GO:0006839 mitochondrial transport (IMP; the assayed defect is altered mitochondrial ATP transport).
- DISEASE: Fontaine progeroid syndrome (FPS) [MIM:612289] = Gorlin-Chaudhry-Moss syndrome; autosomal dominant, de novo recurrent p.Arg217His / p.Arg217Cys; gain-of-pathological-function [file:human/SLC25A24/SLC25A24-uniprot.txt "Fontaine progeroid syndrome (FPS)"] [PMID:29100093 "identified the recurrent de novo mutations c.650G>A (p.Arg217His) and c.649C>T (p.Arg217Cys) in SLC25A24 in five unrelated girls diagnosed with GCMS"].

## Annotation-by-annotation decisions (summary)

MF:
- GO:0005347 ATP transmembrane transporter activity (IMP, PMID:22015608): ACCEPT — core.
- GO:0000295 adenine nucleotide transmembrane transporter activity (IDA, PMID:15123600): ACCEPT — core (broad-specificity adenine nucleotide antiport).
- GO:0140987 ATP:phosphate antiporter activity (IDA, PMID:15123600): ACCEPT — core (specific mechanism; matches Rhea reactions in UniProt).
- GO:0140988 ADP:phosphate antiporter activity (IDA, PMID:15123600): ACCEPT — core (ADP/Pi antiport measured).
- GO:0140987 ATP:phosphate antiporter (IEA, GO_REF:0000117 ARBA): ACCEPT (redundant with IDA; keep).
- GO:0140988 ADP:phosphate antiporter (IBA, GO_REF:0000033): ACCEPT (phylogenetic, consistent).
- GO:0005509 calcium ion binding (IDA PMID:24332718; EXP PMID:24332718; IEA InterPro): ACCEPT — genuine secondary MF (EF-hands).

BP:
- GO:1990544 mitochondrial ATP transmembrane transport (IDA PMID:15123600; IMP PMID:22015608; IBA): ACCEPT — core.
- GO:0051503 adenine nucleotide transport (IDA PMID:15123600): ACCEPT — core (broader parent BP).
- GO:0015866 ADP transport (IBA GO_REF:0000033): ACCEPT / KEEP — consistent.
- GO:0071277 cellular response to calcium ion (IMP PMID:22015608): KEEP_AS_NON_CORE — downstream Ca2+-triggered activation, not the transporter's own core function.
- GO:0034599 cellular response to oxidative stress (IMP PMID:29100093): KEEP_AS_NON_CORE — physiological/disease phenotype.
- GO:0006839 mitochondrial transport (IMP PMID:29100093): KEEP_AS_NON_CORE — correct but a general parent of the specific ATP transport term.
- GO:0055085 transmembrane transport (IEA GO_REF:0000002 InterPro): KEEP_AS_NON_CORE — correct but very general (root-ish transport term).

CC:
- GO:0005743 mitochondrial inner membrane (IEA UniProtKB-SubCell): ACCEPT — core location.
- GO:0005739 mitochondrion (multiple IDA PMID:15123600/15054102/22015608/29100093; IBA; IEA; IDA HPA; HTP PMID:34800366): ACCEPT one representative as location; the rest KEEP_AS_NON_CORE (redundant with, and less specific than, inner membrane).
- GO:0016020 membrane (IDA PMID:24332718): MARK_AS_OVER_ANNOTATED — uninformative parent; the paper localizes/works on the mitochondrial inner-membrane carrier.

No annotation warrants REMOVE. IEA terms present are biologically correct (transporter/calcium/mitochondrion), so none is "clearly-wrong IEA."
