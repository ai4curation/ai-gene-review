# NPL (N-acetylneuraminate pyruvate lyase) — review notes

UniProt: Q9BXD5 (NPL_HUMAN), 320 aa. Gene C1orf13 (synonym), HGNC:16781, chr 1q25.
All UniProt quotes below are from `file:human/NPL/NPL-uniprot.txt`.

## Identity and enzyme classification
- RecName: N-acetylneuraminate lyase (NALase); AltNames include N-acetylneuraminate
  pyruvate-lyase, N-acetylneuraminic acid aldolase, sialate lyase, sialate-pyruvate
  lyase, sialic acid aldolase, sialic acid lyase [file:human/NPL/NPL-uniprot.txt
  "RecName: Full=N-acetylneuraminate lyase"].
- EC=4.1.3.3, evidence from PubMed:33895133 [file:human/NPL/NPL-uniprot.txt
  "EC=4.1.3.3 {ECO:0000269|PubMed:33895133}"].
- Class I (Schiff-base) aldolase / lyase. Active sites: proton donor at residue 143;
  Schiff-base intermediate lysine at residue 173 [file:human/NPL/NPL-uniprot.txt
  "Schiff-base intermediate with substrate"]. Belongs to the DapA family, NanA
  subfamily [file:human/NPL/NPL-uniprot.txt "Belongs to the DapA family. NanA
  subfamily"]. TIM-barrel (aldolase class I) fold; CDD cd00954 NAL; Pfam PF00701 DHDPS.
- KW: Lyase; Schiff base; Carbohydrate metabolism; Cytoplasm.

## Catalytic reaction / function
- Reversibly cleaves free N-acetylneuraminic acid (sialic acid, Neu5Ac) to pyruvate
  and N-acetylmannosamine (ManNAc) via a Schiff base intermediate
  [file:human/NPL/NPL-uniprot.txt "Catalyzes the cleavage of N-acetylneuraminic acid (sialic"].
- CATALYTIC ACTIVITY (Rhea:RHEA:23296): aceneuramate = aldehydo-N-acetyl-D-mannosamine
  + pyruvate; EC 4.1.3.3; evidence PubMed:33895133 [file:human/NPL/NPL-uniprot.txt
  "Reaction=aceneuramate = aldehydo-N-acetyl-D-mannosamine + pyruvate"].
- Function is to prevent sialic acids from being recycled to the cell surface — i.e.
  it controls the intracellular free-sialic-acid pool and commits sialic acid to
  catabolism [file:human/NPL/NPL-uniprot.txt
  "It prevents sialic acids from being recycled and returning to the cell surface"].
- Also degrades N-glycolylneuraminic acid (Neu5Gc): "Involved in the
  N-glycolylneuraminic acid (Neu5Gc) degradation pathway" — humans lack functional
  CMAHP so cannot synthesize Neu5Gc, but dietary Neu5Gc must be degraded
  [file:human/NPL/NPL-uniprot.txt "Involved" / "in the"; "Although human is not able to";
  Reactome R-HSA-4085217].

## Pathway and localization
- PATHWAY: Amino-sugar metabolism; N-acetylneuraminate degradation (UniPathway
  UPA00629) [file:human/NPL/NPL-uniprot.txt "Amino-sugar metabolism; N-acetylneuraminate degradation"].
  Downstream: ManNAc is phosphorylated to ManNAc-6-P and processed by an epimerase
  (mammalian pathway parallels E. coli) [PMID:33895133 "N-acetylneuraminate is
  metabolized by a similar pathway in mammalian cells"].
- SUBCELLULAR LOCATION: Cytoplasm (by similarity, ECO:0000250)
  [file:human/NPL/NPL-uniprot.txt "SUBCELLULAR LOCATION: Cytoplasm"]. Reactome places
  the reaction in the cytosol [Reactome:R-HSA-4085217 "N-acetylneuraminate lyase (NPL)
  is a cytosolic, tetrameric enzyme"].

## Quaternary structure
- Homotetramer [file:human/NPL/NPL-uniprot.txt "SUBUNIT: Homotetramer"], based on the
  1.60 Å crystal structure PDB 6ARH (Pearce, Bundela, Keown, submitted 2017). Reactome
  also describes it as tetrameric.

## Key primary evidence
- **PMID:33895133** (Kentache et al., 2021, J Biol Chem; full text cached). Primarily
  about E. coli NanA and the anomerase YhcH, but explicitly assays human NPL: the true
  substrate of Neu5Ac aldolase is the open (linear) form of Neu5Ac; both NanM and YhcH
  stimulate human NPL activity on Neu5Ac [PMID:33895133 "both NanM and YhcH stimulated
  the activity of human NPL on Neu5Ac"; "human homolog of NanA (NPL), which only shares
  about 30% sequence identity with the E. coli NanA"]. This is the source of the IDA
  MF/BP annotations and the EC=4.1.3.3 catalytic-activity assignment in UniProt.
- **PMID:22692205** (Bergfeld et al., 2012, J Biol Chem; ABSTRACT ONLY in cache,
  full_text_available: false). Establishes the intracellular Neu5Gc degradation pathway
  in vertebrate cells (Neu5Gc → N-glycolylmannosamine → ... → glycolate + GlcN-6-P).
  Basis for the TAS N-acetylneuraminate catabolic process annotation and UniProt's
  PATHWAY / Neu5Gc-degradation statements. Does not name NPL in the abstract; do not
  quote NPL from it.
- **Reactome R-HSA-4085217** "NPL cleaves Neu5Ac,Neu5Gc to ManNAc,ManNGc and pyruvate":
  cytosolic tetrameric NPL cleaving both Neu5Ac and Neu5Gc (cites Wu et al. 2005,
  Bergfeld et al. 2012). Source of the TAS cytosol CC.

## Disease / physiological context (notes only; not in publications/ cache)
- Deleterious NPL variants cause skeletal myopathy and cardiac edema in humans and
  zebrafish; NPL loss raises free sialic acid, reduces muscle force/regeneration, and
  causes aberrant sialylation of dystroglycan. Oral N-acetylmannosamine (ManNAc)
  rescues the myopathy in mouse models — a candidate therapy. Based on articles
  retrieved from PubMed: Da Silva et al., Sci Adv 2023, PMID:37390204,
  [DOI](https://doi.org/10.1126/sciadv.ade6308). (Abstract only; used for context, not
  as annotation supporting_text.)

## Interactions (IPI annotations)
- GOA carries GO:0005515 protein binding (IPI, PMID:25416956; with NTAQ1/Q96HA8) and
  two GO:0042802 identical protein binding (IPI, PMID:25416956 and PMID:32296183;
  self/self). These are large-scale binary interactome maps (HuRI / Rolland et al.,
  Luck et al.); NPL is not named in the cached article text (interactions are in
  supplementary data). UniProt records the same: IntAct self-interaction (NbExp=4) and
  NPL–NTAQ1 (NbExp=3) [file:human/NPL/NPL-uniprot.txt "Q9BXD5; Q9BXD5: NPL" and
  "Q9BXD5; Q96HA8: NTAQ1"]. The self-interaction is consistent with the homotetramer;
  the NTAQ1 heterodimer has no established functional meaning for NPL's core catabolic
  role.

## GO term id/label verification (OLS, current)
- GO:0008747 N-acetylneuraminate lyase activity — MF (def: Neu5Ac = ManNAc + pyruvate). VERIFIED.
- GO:0019262 N-acetylneuraminate catabolic process — BP. VERIFIED.
- GO:0005829 cytosol — CC. VERIFIED.
- GO:0005737 cytoplasm — CC (parent of cytosol). VERIFIED.
- GO:0016829 lyase activity — MF (general parent). VERIFIED.
- GO:0005975 carbohydrate metabolic process — BP (general parent). VERIFIED.
- GO:0042802 identical protein binding — MF. VERIFIED.

## Review decisions (summary)
- Core MF: GO:0008747 (IDA PMID:33895133 = strongest, ACCEPT; IBA/ISS/IEA duplicates
  ACCEPT or KEEP as supporting).
- Core BP: GO:0019262 (IDA PMID:33895133 ACCEPT; IBA/TAS/IEA duplicates ACCEPT).
- Core CC: cytosol (GO:0005829, TAS Reactome ACCEPT); GO:0005737 cytoplasm IEA is
  correct but less specific (KEEP_AS_NON_CORE).
- GO:0016829 lyase activity (IEA) and GO:0005975 carbohydrate metabolic process (IEA):
  correct but uninformatively general parents → MARK_AS_OVER_ANNOTATED (redundant with
  the specific NanA/catabolic terms).
- protein binding / identical protein binding IPIs: bare/uninformative; identical
  protein binding is consistent with the homotetramer but not a "core function" →
  KEEP_AS_NON_CORE (self) / MARK_AS_OVER_ANNOTATED (bare protein binding). Do not REMOVE
  (experimental IPI, per policy).
