# ELP3 (human, Q9H9T3) curation notes

Context: RADICAL_SAM project (projects/RADICAL_SAM.md), Phase 1 human. Review created 2026-10-18.

## Sources

- Deep research: the falcon provider failed (auth 403). `ELP3-deep-research-asta.md` is an Asta
  retrieval-only run, and all 20 papers it returned are irrelevant (generic annotation databases,
  network pharmacology, etc.); none concerns ELP3. It was not used as evidence. Literature was
  gathered directly via PubMed and cached with `just fetch-pmid`.
- UniProt record `ELP3-uniprot.txt` (Swiss-Prot, entry version 200).

## Identity and domains

- 547 aa; radical SAM core domain 82-372 and GNAT N-acetyltransferase domain 396-547
  [file:human/ELP3/ELP3-uniprot.txt "Radical SAM core"; "N-acetyltransferase"].
- Cofactor: [file:human/ELP3/ELP3-uniprot.txt "Binds 1 [4Fe-4S] cluster. The cluster is coordinated
  with 3 cysteines and an exchangeable S-adenosyl-L-methionine."] (by similarity to yeast Q02908).
- Family: NCBIfam TIGR01211 ELP3; PANTHER PTHR11135:SF0; SFLD ELP3-like.

## Catalytic function (core)

- Reaction (EC 2.3.1.311, RHEA:61020): uridine(34) in tRNA + acetyl-CoA + SAM + H2O ->
  cm5U34 + 5'-dA + Met + CoA [file:human/ELP3/ELP3-uniprot.txt "acts as a tRNA uridine(34)
  acetyltransferase by mediating formation of carboxymethyluridine in the wobble base at position
  34 in tRNAs"]. Human activity is by similarity to Methanocaldococcus infernus Elp3 (D5VRB9).
- Archaeal Elp3 alone performs the reaction in vitro [PMID:25151136 "a single archaeal protein, the
  homolog of the third subunit of the eukaryotic Elongator complex (Elp3), is able to catalyze the
  same reaction"]; mechanism: radical abstraction from acetyl-CoA [PMID:25151136 "abstracts a
  hydrogen atom from acetyl-CoA, rather than from tRNA as we initially envisioned"].
  Note: Selvadurai 2014 used the archaeal (M. infernus) enzyme; the D. mccartyi structure is
  Glatt et al. 2016 [PMID:27455459 "form a composite active site and tRNA-binding pocket, with an
  iron-sulfur cluster located in the dimerization interface of two DmcElp3 molecules"].
- Lin et al. 2019 [PMID:30733442 "establish the clinically relevant Elongator subunit as a
  non-canonical acetyltransferase and genuine tRNA modification enzyme"].
- In yeast, Elongator (all six subunits) is required for an early step of mcm5/ncm5 U34 formation
  and Elp3 co-precipitates substrate tRNA [PMID:15769872 "the Elp1 and Elp3 proteins specifically
  coprecipitate a tRNA susceptible to formation of an mcm5 side chain"].
- Human: ELP3 depletion lowers mcm5s2U [PMID:29415125 "Depletion of ELP3 in vitro reduced the
  modified tRNA wobble uridine mcm5s2U"].
- cm5U is the first step; the downstream mcm5U/mcm5s2U/ncm5U are made by other enzymes
  (ALKBH8/TRM112 methylation, CTU1/CTU2 thiolation), so ELP3 participates in GO:0002098 and in the
  first step of GO:0002926.

## Complex

- Elongator holoenzyme (ELP1-6), ELP1-ELP2-ELP3 core plus ELP4-5-6 ring
  [file:human/ELP3/ELP3-uniprot.txt "Component of the elongator complex which consists of ELP1,
  ELP2, ELP3, ELP4, ELP5 and ELP6."]; ELP5 bridges ELP3 to ELP4 [PMID:22854966 "DERP6/ELP5 is
  required for the integrity of Elongator and directly connects ELP3 to ELP4"].
- Purified human holo-Elongator [PMID:11714725 "a six-subunit complex, holo-Elongator, which has
  histone acetyltransferase activity directed against histone H3 and H4"].

## Historic / contested functions

- Histone acetyltransferase / Pol II transcription elongation: purified holo-Elongator acetylates
  H3/H4 and stimulates chromatin transcription in vitro [PMID:11818576 "human Elongator facilitates
  transcription by RNA polymerase II"]. In yeast these phenotypes are bypassed by overexpressing
  two tRNAs [PMID:17018299 "Our results indicate that the physiologically relevant function of the
  evolutionary-conserved Elongator complex is in formation of modified nucleosides in tRNAs"].
  UniProt CAUTION: [file:human/ELP3/ELP3-uniprot.txt "it is no longer thought to play a direct role
  in this process and its primary function is thought to be in tRNA modification"].
- Alpha-tubulin acetylation and cortical neuron migration: [PMID:19185337 "silencing of its
  scaffold (Elp1) or catalytic subunit (Elp3) cell-autonomously delays the migration and impairs
  the branching of projection neurons"]; later work in C. elegans indicates indirect regulation
  [PMID:27847465 "Elongator is not a direct tubulin acetytransferase, but it rather regulates the
  expression of α-tubulin acetyltransferase at translational level"]. UniProt: "Not a major
  acetyltransferase of tubulin".
- Other protein-acetylation substrates (Drosophila Bruchpilot [PMID:22153374], mouse Cx43
  [PMID:28507509]) rest on reduced acetylation upon Elp3 loss; direct KAT activity on proteins is
  unproven in vivo.
- No GOA row for histone acetyltransferase activity exists for human ELP3 at present; the
  acetyltransferase IDA (PMID:11714725) is to the general GO:0016407.

## Localization

- Mainly cytoplasmic/cytosolic (HPA IDA cytosol; several IDA cytoplasm). A minor nuclear pool
  reported [PMID:22002106 "In the case of ELP3, the larger (A) isoform has a turnover value of ∼5 h
  and is detected specifically in the nucleus"]; yeast: [PMID:15769872 "implying that a small
  fraction of Elongator localizes to the nucleus"].

## Disease / development (pleiotropic, downstream of tRNA modification)

- ALS modifier: [PMID:18996918 "allelic variants of ELP3 were associated with ALS in three human
  populations"]; [PMID:29415125 "ELP3 attenuated the axonopathy of a mutant SOD1"].
- Cortical neurogenesis/migration (mouse knockdown/cKO). Melanoma cell migration decreased after
  ELP3 depletion [PMID:22854966]. These are treated as non-core or over-annotated process terms.

## Decisions (summary)

- Generic rows per RADICAL_SAM treatment rule: GO:0003824 -> MODIFY GO:0106261; GO:0051536 ->
  MODIFY GO:0051539. No GO:0051539, GO:0046872 or GO:1904047 row in GOA; GO:1904047 added as NEW
  (radical SAM cosubstrate; cluster coordinated by exchangeable SAM).
- GO:0016407 / GO:0016747 -> MODIFY to GO:0106261.
- Cytoplasm rows -> MODIFY to cytosol (GO:0005829, HPA IDA).
- Protein binding (ELP1 IPI) -> REMOVE (uninformative; captured by elongator holoenzyme complex).
