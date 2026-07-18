# HAAO (P46952) — review notes

## Identity and core biochemistry

HAAO encodes **3-hydroxyanthranilate 3,4-dioxygenase** (3-HAO; also "3-hydroxyanthranilic acid dioxygenase / oxygenase"; EC 1.13.11.6), a 286-aa cytosolic enzyme of the kynurenine pathway of tryptophan degradation.

- UniProt RecName and EC: "3-hydroxyanthranilate 3,4-dioxygenase ... EC=1.13.11.6" [file:human/HAAO/HAAO-uniprot.txt].
- FUNCTION: "Catalyzes the oxidative ring opening of 3-hydroxyanthranilate to 2-amino-3-carboxymuconate semialdehyde, which spontaneously cyclizes to quinolinate." [file:human/HAAO/HAAO-uniprot.txt].
- CATALYTIC ACTIVITY: "3-hydroxyanthranilate + O2 = (2Z,4Z)-2-amino-3-carboxymuconate 6-semialdehyde" (Rhea:RHEA:17953) [file:human/HAAO/HAAO-uniprot.txt].
- COFACTOR: "Name=Fe(2+)" [file:human/HAAO/HAAO-uniprot.txt].
- PATHWAY: "Cofactor biosynthesis; NAD(+) biosynthesis; quinolinate from L-kynurenine: step 3/3." [file:human/HAAO/HAAO-uniprot.txt].
- SUBCELLULAR LOCATION: "Cytoplasm, cytosol" [file:human/HAAO/HAAO-uniprot.txt].
- SUBUNIT: "Monomer." [file:human/HAAO/HAAO-uniprot.txt].
- Family: "Belongs to the 3-HAO family." Structural fold is a bicupin (RmlC-like cupin / jelly roll), a non-heme Fe(II) extradiol ring-cleaving dioxygenase [file:human/HAAO/HAAO-uniprot.txt; PMID:28375145].

The product ACMS (2-amino-3-carboxymuconate-6-semialdehyde) cyclises non-enzymatically to quinolinate, the universal precursor of de novo NAD+ biosynthesis (via QPRT), unless it is diverted by ACMSD toward picolinate/glutaryl-CoA. Thus HAAO sits directly upstream of quinolinate and de novo NAD+ from tryptophan.

## Key experimental evidence (cited GOA references)

- **PMID:7514594** (Malherbe et al. 1994, JBC) — molecular cloning and functional expression of human 3-HAO; recombinant enzyme active; "The Km value of 3-HANA for recombinant h3-HAO (approximately 2 microM)"; catalyzes "the synthesis of QUIN from 3-hydroxyanthranilic acid" [PMID:7514594]. Supports catalytic MF (GO:0000334), quinolinate biosynthesis (GO:0019805), and cytosolic location (basis for UniProt's ECO:0000305 cytosol call). Abstract-only in cache (full_text_available: false); curator (UniProtKB) read the full paper.

- **PMID:12007609** (Calderone et al. 2002, BBA) — E. coli-expressed purified human 3-HAO; "3-hydroxyanthranilic acid oxygenase (3-HAO) catalyses the conversion of 3-hydroxyanthranilic acid to quinolinic acid"; "enzymatic activity which can occur only in the presence of Fe(II); several other metals have been tested but in no case the formation of the product has been observed"; "two of the ions tested inhibit the catalytic reaction and one of them, Zn2+, could be of physiological relevance" [PMID:12007609]. Supports catalytic MF (GO:0000334), Fe(II)/ferrous iron binding (GO:0008198), and Zn2+ inhibition (basis of the GOA "response to zinc ion" and "response to cadmium ion" IDA calls — see caveats below).

- **PMID:28375145** (Pidugu et al. 2017, Acta Cryst D) — first crystal structures of human 3HAO with native iron and with zinc (an inhibitor); "3HAO is a non-heme iron-containing, ring-cleaving extradiol dioxygenase that catalyzes the addition of both atoms of O2 to ... 3-hydroxyanthranilic acid (3-HANA) to form quinolinic acid (QUIN)" [PMID:28375145]. Supports ferrous iron binding (GO:0008198, IDA) and the extradiol dioxygenase mechanism. Active-site Fe residues His47/His91/Glu53 (BINDING features) [file:human/HAAO/HAAO-uniprot.txt].

- **PMID:28792876** (Shi/Dunwoodie et al. 2017, NEJM) — biallelic loss-of-function HAAO (and KYNU) variants cause a congenital NAD-deficiency malformation syndrome (VCRL1). "Variants were identified in two genes that encode enzymes of the kynurenine pathway, 3-hydroxyanthranilic acid 3,4-dioxygenase (HAAO) and kynureninase (KYNU)"; "The mutant enzymes had greatly reduced activity in vitro"; "NAD is synthesized de novo from tryptophan through the kynurenine pathway"; "The patients had reduced levels of circulating NAD"; Haao-null and Kynu-null mice reproduce the defects; "Niacin supplementation during gestation prevented the malformations in mice" [PMID:28792876]. Supports catalytic MF IDA (in-vitro enzyme assay of variants), quinolinate biosynthesis IDA, and NAD+ biosynthetic process IMP. UniProt DISEASE: "Vertebral, cardiac, renal, and limb defects syndrome 1 (VCRL1) [MIM:617660]" [file:human/HAAO/HAAO-uniprot.txt].

- **PMID:2967497** (Schwarcz et al. 1988, PNAS) — 3-hydroxyanthranilate oxygenase activity detected in human brain and increased in Huntington disease striatum: "The activity of 3-hydroxyanthranilate oxygenase is increased in Huntington disease brains as compared to control brains" [PMID:2967497]. This is the basis of the GOA IMP "neuron cellular homeostasis" (GO:0070050) call — a correlational disease-association observation, not a demonstration that HAAO participates in maintaining neuronal homeostasis. Weak support for that specific BP term; kept as non-core.

## Protein-binding IPI annotations (GO:0005515)

All five bare "protein binding" (GO:0005515) IPI annotations come from high-throughput interactome/screen datasets, per GOA WITH/FROM and UniProt INTERACTION block (partners GAD1 = Q99259/Q8IVA8, POT1 = Q9NUX5):
- PMID:16189514 — Rual et al. 2005, first CCSB Y2H human interactome map (CCSB-HI1) [PMID:16189514].
- PMID:21044950 — Lee et al. 2011, genome-wide split-Venus BiFC telomere-interactome screen; POT1 (Q9NUX5) among six telomere baits [PMID:21044950].
- PMID:25416956 — Rolland et al. 2014, HI-II-14 systematic binary interactome map [PMID:25416956].
- PMID:31515488 — Fragoza et al. 2019, ExAC-variant Y2H interaction screen [PMID:31515488].
- PMID:32296183 — Luck et al. 2020, HuRI reference binary interactome [PMID:32296183].

None assigns a specific molecular function; the GAD1/POT1 pairings have no established biological rationale for a cytosolic kynurenine-pathway enzyme. Per policy, bare "protein binding" IPI is not removed but marked as over-annotated (uninformative for MF).

## Metal-response BP annotations (from PMID:12007609)

GO:0010043 (response to zinc ion) and GO:0046686 (response to cadmium ion) IDA both trace to PMID:12007609, which showed that Zn2+ (and another tested ion) **inhibit** the enzyme in vitro. This is an in-vitro inhibitor-sensitivity result, not evidence that HAAO participates in a cellular "response to zinc/cadmium ion" process. These are over-interpretations of an inhibition assay; kept but flagged as over-annotated (Zn) / mark-as-over-annotated (Cd).

## Electron transfer activity (NAS, PMID:7514594)

GO:0009055 (electron transfer activity) NAS is mechanistically wrong: 3-HAO is a non-heme Fe(II) dioxygenase that incorporates both O2 atoms into the substrate (extradiol ring cleavage) — it is not an electron carrier/electron transfer protein. UniProt itself retains the NAS DR line but the assignment does not reflect the current mechanistic understanding (PMID:28375145 "ring-cleaving extradiol dioxygenase") [PMID:28375145]. NAS (author statement) — mark as over-annotated rather than accept.

## Summary of core functions

- MF: 3-hydroxyanthranilate 3,4-dioxygenase activity (GO:0000334) with ferrous iron (Fe2+) as catalytic cofactor (GO:0008198).
- BP: quinolinate biosynthetic process (GO:0019805) / de novo NAD+ biosynthesis from L-tryptophan (GO:0034354); the enzyme's product feeds de novo NAD+ synthesis.
- CC: cytosol (GO:0005829).

Disease: biallelic LoF causes congenital NAD-deficiency malformation syndrome (VCRL1), rescuable in mice by gestational niacin (PMID:28792876).
</content>
</invoke>
