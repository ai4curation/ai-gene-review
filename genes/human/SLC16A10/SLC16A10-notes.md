# SLC16A10 (MCT10 / TAT1, Q8TF71) — curation notes

## Identity and family
- UniProt Q8TF71, MOT10_HUMAN, 515 aa, chromosome 6q21-q22. HGNC:17027.
- Names: Monocarboxylate transporter 10 (MCT10); Aromatic amino acid transporter 1; T-type amino acid transporter 1 (TAT1) [file:human/SLC16A10/SLC16A10-uniprot.txt "AltName: Full=T-type amino acid transporter 1"].
- Member of the major facilitator superfamily, Monocarboxylate porter (TC 2.A.1.13) family [file:human/SLC16A10/SLC16A10-uniprot.txt "Belongs to the major facilitator superfamily."]. 12 predicted transmembrane helices; cryo-EM structures now exist (PDB 9GSZ, 9HHQ) [file:human/SLC16A10/SLC16A10-uniprot.txt "PDB; 9HHQ; EM"].
- Despite the "monocarboxylate transporter" family name, MCT10 does NOT transport lactate/pyruvate like MCT1–4; it is an aromatic amino acid and thyroid hormone carrier.

## Core mechanism — facilitative (equilibrative), Na+/H+/Cl−-independent
- System T is the Na+-independent transport system selective for aromatic amino acids [PMID:11827462 "System T is a Na+-independent transport system that selectively transports aromatic amino acids."].
- UniProt summarizes it as a "Sodium- and proton-independent thyroid hormones and aromatic acids transporter" that mediates both uptake and efflux, i.e. bidirectional/facilitative [file:human/SLC16A10/SLC16A10-uniprot.txt "Mediates both uptake and efflux"].
- Yeast functional analysis confirmed the facilitated-diffusion mechanism: MCT10-expressing cells were nearly unaffected by neutral pH, "consistent with the transport mechanism of MCT10 via facilitated diffusion without a need for pH gradient across the plasma membrane." [PMID:28754537 "consistent with the transport mechanism of MCT10 via facilitated diffusion without a need for pH gradient across the plasma membrane."]. This is the key distinction from the proton-coupled lactate MCTs.
- No obligate ancillary subunit (basigin/embigin) is invoked in the primary characterizations; MCT10 is functional in heterologous systems (Xenopus oocytes, COS1, HEK293T, yeast) [PMID:28754537 "Plasma membrane localization of MCT10 and the variant proteins was also verified in human embryonic kidney 293T cells."].

## Substrates and kinetics
- Aromatic amino acids: tryptophan, tyrosine, phenylalanine, and L-dopa, Na+-independent [PMID:11827462 "demonstrated the Na+-independent transport of tryptophan, tyrosine, phenylalanine, and L-dopa"].
- Low-affinity, bidirectional aromatic amino acid transport; UniProt KM values (Xenopus oocytes): Tyr 636 µM, Phe 740 µM, L-dopa 1212 µM, Trp 452 µM [file:human/SLC16A10/SLC16A10-uniprot.txt "KM=452 uM for L-tryptophan"].
- ChEBI substrates (from UniProt Rhea catalytic-activity lines): L-tryptophan CHEBI:57912, L-tyrosine CHEBI:58315, L-phenylalanine CHEBI:58095.
- Thyroid hormones (T3, T4): MCT10 is an efficient iodothyronine transporter. "hMCT10 facilitates both cellular uptake and efflux of T(4) and T(3)" and is "at least as active a thyroid hormone transporter as hMCT8" [PMID:18337592 "hMCT10 facilitates both cellular uptake and efflux of T(4) and T(3)"] [PMID:18337592 "hMCT10 is at least as active a thyroid hormone transporter as hMCT8"]. T3 uptake is inhibited by Phe, Tyr, Trp, indicating shared substrate pathway [PMID:18337592 "a significant inhibition of T(3) uptake by phenylalanine, tyrosine, and tryptophan"]. ChEBI: T3 (3,3',5-triiodo-L-thyronine) CHEBI:533015, T4 (L-thyroxine) CHEBI:58448.
- MCT10 transports the affinity label BrAc[125I]T3 but is not covalently modified by it (further confirming it is a bona fide TH transporter) [PMID:21315799 "hMCT8 and hMCT10 both facilitate BrAc[(125)I]T3 transport, but are not labeled by BrAc[(125)I]T3."].

## Structure/function residue
- N81 lines the putative substrate trajectory; the N81K SNP variant abolishes tryptophan import without altering expression or localization [PMID:28754537 "the N81K mutation completely abrogated tryptophan import without any abnormalities in the expression or localization."]. (UniProt MUTAGEN 81: "Abolishes tryptophan import activity.")

## Subcellular localization and physiology
- Plasma membrane / basolateral. In human kidney, immunohistochemistry shows LAT2 (SLC7A8) and TAT1 coexist in the basolateral membrane of the renal proximal tubule [PMID:15918515 "the hLAT2 and hTAT1 proteins coexist in the basolateral membrane of the renal proximal tubules."].
- Functional coupling: TAT1 (efflux of aromatic AAs at the basolateral side) works with apical uptake systems and basolateral LAT2 to complete transepithelial (re)absorption of aromatic/neutral amino acids in intestine and kidney [PMID:15918515 "these transporters contribute to the renal reabsorption of neutral and aromatic amino acids in the basolateral domain of epithelial proximal tubule cells"]. Apical counterpart on the uptake side is B0AT1/SLC6A19 (reviewed in batch 10).
- UniProt records basolateral cell membrane localization [file:human/SLC16A10/SLC16A10-uniprot.txt "Basolateral cell membrane"].
- Tissue specificity: strongly expressed in kidney and skeletal muscle, lower in placenta and heart [file:human/SLC16A10/SLC16A10-uniprot.txt "Strongly expressed in kidney and skeletal muscle"].
- Physiological role proposed in efficient absorption of aromatic amino acids from intestine and kidney; defects hypothesized (not proven) in aromatic amino-acid transport disorders [PMID:11827462 "crucial to the efficient absorption of aromatic amino acids from intestine and kidney"].

## Interactions (GOA IPI rows)
- Three protein-binding IPI rows come from the HuRI high-throughput binary interactome (PMID:32296183): FUNDC2 (Q9BWH2), TMEM14B (Q9NUH8), INSIG2 (Q9Y5U4). These are untargeted Y2H screen hits with no functional characterization tying them to MCT10 transport. Bare GO:0005515 protein binding is uninformative → removed per protein-binding policy.

## Curation decisions summary
- Core MF: GO:0015173 aromatic amino acid transmembrane transporter activity (IDA, PMID:11827462). QuickGO is_a children of GO:0015173 are the three substrate terms the gene carries (GO:0015196 Trp, GO:0005302 Tyr, GO:0015192 Phe); GO:0015173 is_a parent is GO:0046943 carboxylic acid transmembrane transporter activity (NOT GO:0015171). So GO:0015171 amino acid transmembrane transporter activity is a lateral, broader class, not a strict ancestor.
- Second core MF: GO:0015349 thyroid hormone transmembrane transporter activity (IDA, PMID:18337592, PMID:21315799).
- Core BP: GO:0015801 aromatic amino acid transport (IDA) and GO:0070327 thyroid hormone transport (IDA).
- Core CC: GO:0005886 plasma membrane (EXP/IDA) refined to GO:0016323 basolateral plasma membrane (IDA, PMID:15918515) in polarized epithelia.
- Substrate-level terms (Phe/Trp/Tyr MF and transport, aromatic AA transport, TH transport) accepted as directly demonstrated.
- General umbrella terms: bare GO:0022857 transmembrane transporter activity and GO:0055085 transmembrane transport are TOO_GENERAL (a specific transporter activity/process is asserted). GO:0015171 amino acid transmembrane transporter activity, GO:0003333 amino acid transmembrane transport and GO:0006865 amino acid transport are correct but broader than the demonstrated aromatic-AA selectivity → MODIFY to the aromatic-specific terms the gene already carries.
- IBA rows (GO:0005886, GO:0022857, GO:0016323, GO:0070327): the GO:0016323 and GO:0070327 IBAs carry UniProtKB:Q8TF71 in WITH/FROM — self-reference is expected (own experimental annotation seeded the IBD node), not circular.
- GO:0030054 cell junction: single HPA immunofluorescence dataset; plausible for a basolateral epithelial protein but peripheral and uncorroborated → KEEP_AS_NON_CORE.

All cited publications in this review are abstract-only in the cache except PMID:32296183 (full text). Experimental annotations (IDA/EXP) from PMID:11827462, PMID:15918515, PMID:18337592, PMID:21315799, PMID:28754537 are deferred to as curator-read full text where the abstract already supports the function.
