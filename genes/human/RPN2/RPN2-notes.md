# RPN2 (Ribophorin II) — Gene Review Notes

UniProt: P04844 (RPN2_HUMAN). HGNC:10382. 631 aa precursor; chain 23–631.
Gene product: Dolichyl-diphosphooligosaccharide--protein glycosyltransferase subunit 2
(a.k.a. ribophorin II, RIBIIR, RPN-II, DDOST 63 kDa subunit).

## Summary of function

RPN2 is a **non-catalytic subunit of the oligosaccharyltransferase (OST) complex**, the
ER-membrane enzyme that performs the central committed step of N-linked protein
glycosylation: en-bloc transfer of the pre-assembled Glc3Man9GlcNAc2 glycan from the
dolichol-pyrophosphate lipid carrier onto asparagine residues in Asn-X-Ser/Thr sequons of
nascent secretory and membrane proteins.

- OST subunit / function: `[file:human/RPN2/RPN2-uniprot.txt "Subunit of the oligosaccharyl transferase (OST) complex that"]`,
  which `[file:human/RPN2/RPN2-uniprot.txt "consensus motif in nascent polypeptide chains, the first step in"]`
  `[file:human/RPN2/RPN2-uniprot.txt "protein N-glycosylation (PubMed:31831667). N-glycosylation occurs"]`.
- Pathway: `[file:human/RPN2/RPN2-uniprot.txt "PATHWAY: Protein modification; protein glycosylation."]`
- All subunits required for maximal activity: `[file:human/RPN2/RPN2-uniprot.txt "translocation across the endoplasmic reticulum (ER). All subunits are"]`
  `[file:human/RPN2/RPN2-uniprot.txt "required for a maximal enzyme activity."]`

## Complex membership (core subunit of both OST-A and OST-B)

Human cells express two OST complexes that share a common set of non-catalytic core
subunits and differ in the catalytic subunit (STT3A in the co-translational OST-A;
STT3B in the post-translocational OST-B) and accessory subunits.

- Core subunits shared by both forms:
  `[file:human/RPN2/RPN2-uniprot.txt "different complex forms which contain common core subunits RPN1, RPN2,"]`
  (RPN1, RPN2, OST48, OST4, DAD1, TMEM258).
- In STT3A-complex assembly RPN2 is part of subcomplex 3:
  `[file:human/RPN2/RPN2-uniprot.txt "subunit OST4, and subcomplex 3 contains RPN2, DAD1, and OST48. The"]`
- Cryo-EM of both human OST complexes (OST-A / OST-B): [PMID:31831667 "Here, we present high-resolution cryo-electron microscopy structures of human OST-A and OST-B."]
  — RPN2 (ribophorin-II) is a subunit of both; the paper notes ribophorin-I forms a
  four-helix bundle that can bind a translating ribosome in OST-A.
- OST-A is the co-translational, SEC61-associated form; the SEC61–OSTA–TRAP translocon is
  the most abundant ER-membrane translocon: [PMID:36697828 "the most populated SEC61–OSTA–TRAP (69% of ER-bound particles)"]
  and [PMID:36697828 "OSTA, which is responsible for co-translational N-glycosylation of substrates"].
- The GOA `part_of` annotations to **oligosaccharyltransferase complex A (GO:0160226)** and
  **oligosaccharyltransferase complex B (GO:0160227)** are the specific, structurally-supported
  refinements of the generic OST-complex term.

## Location

- ER / ER membrane, multi-pass membrane protein:
  `[file:human/RPN2/RPN2-uniprot.txt "SUBCELLULAR LOCATION: Endoplasmic reticulum"]`;
  topology in the UniProt record: large lumenal domain (23–540), then three
  C-terminal transmembrane helices (541–561, 572–592, 597–617). Historically ribophorins
  were defined as rough-ER-specific glycoproteins (Crimaudo et al. 1987, EMBO J).
- The ER membrane TAS annotations come from Reactome N-glycosylation reaction records
  (e.g. Reactome:R-HSA-446209 "Transfer of N-glycan to the protein").

## Historical / biochemical evidence

- Purification of human lymphocyte OST identified ribophorin I, ribophorin II (doublet),
  and a Wbp1 homologue as OST components: [PMID:9642163 "N-terminal sequence analysis identified the"]
  proteins as ribophorin I, ribophorin II (doublet)... — supports OST-complex membership
  and involvement in N-glycosylation (IDA in GOA).
- ER retention: RPN2 (RII) carries independent ER-retention signals in its transmembrane
  and cytoplasmic domains: [PMID:10660554 "ER retention information is independently contained within the transmembrane and"]
  the cytoplasmic domain of RII. (basis of the TAS "protein modification process" annotation).
- Proteomic dissection of mammalian OST subcomplexes (Sec61/TRAP association): PMID:15835887
  (basis for the NAS `contributes_to` GO:0004579 annotation).

## Disease

RPN2 mutation is associated with a congenital disorder of glycosylation (CDG-Ix), per the
Reactome record: [Reactome:R-HSA-446209 "A mutation in RPN2 is associated with CDG-Ix (Vleugels et al. 2009)."]

## Protein-binding (IPI) annotations — over-annotations

Four bare `protein binding` (GO:0005515) IPI annotations come from high-throughput or
unrelated-context interaction studies and do not describe RPN2's molecular function:
- PMID:32707033 — kinase interaction network (interaction with POMK, Q9H5K3).
- PMID:28169274 — ARMC5 knockout / T-cell study (interaction with ARMC5, Q96C12).
- PMID:29290612 — RTF2/replisome study; UniProt records this as "Interacts with DDI2"
  `[file:human/RPN2/RPN2-uniprot.txt "both the Sec61 and TRAP complexes (By similarity). Interacts with DDI2"]` (with Q5TDH0/DDI2).
- PMID:24965446 — pestivirus Npro ribonucleoprotein interactome (viral protease with/from P19712).
These are kept but marked as over-annotated per curation policy (bare protein binding IPI).

## Core function model

- in_complex: oligosaccharyltransferase complex (GO:0008250) — protein-containing complex
- contributes_to_molecular_function: dolichyl-diphosphooligosaccharide-protein glycotransferase
  activity (GO:0004579) — RPN2 is non-catalytic; STT3A/STT3B carry the catalytic site
- directly_involved_in: protein N-linked glycosylation (GO:0006487)
- locations: endoplasmic reticulum membrane (GO:0005789)
