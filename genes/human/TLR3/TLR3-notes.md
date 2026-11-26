# TLR3 (human, O15455) curation notes

Reviewer: annotation-reviewer (INNATE_IMMUNITY batch 1, Toll/TLR axis).
Deep research: `TLR3-deep-research-falcon.md` arrived after the review was drafted
(the earlier run had failed); see the cross-check section at the end.
The review itself rests on the cached publications in `publications/`, the
UniProt record, and OLS/QuickGO term checks. No file named
`-deep-research-<provider>.md` was written by hand.

## Core biology

TLR3 is the endosomal dsRNA-sensing Toll-like receptor. Architecture: N-terminal
LRR ectodomain (horseshoe), single TM helix (705-725), cytoplasmic TIR domain
(754-897) [UniProt O15455 features].

- Direct dsRNA binding to the ectodomain, saturable/specific/reversible, affinity
  rising with acidic pH and ligand length; 40-50 bp dsRNA is the smallest that
  forms a stable complex and activates the receptor
  [PMID:18172197 "dsRNA binds saturably, specifically, and reversibly to a defined ligand-binding site (or sites) on the TLR3 ectodomain"].
- Ligand-induced dimerisation is the minimal signalling unit
  [PMID:18172197 "the minimal signaling unit is one TLR3 dimer"].
- Binding site mapped to H539/N541 on the glycan-free lateral surface
  [PMID:16720699 "only two, H539E and N541A, resulted in the loss of TLR3 activation and ligand binding functions"].
- Specificity: dsRNA yes; ssRNA and dsDNA no
  [PMID:12054664 "TLR3 signaling was not elicited by either single-stranded RNA (ssRNA) or dsDNA"].

## Trafficking / location

- Resting TLR3 in ER; moves to dsRNA-containing endosomes on stimulation
  [PMID:16858407 "TLR3 is localized in the endoplasmic reticulum of unstimulated cells, moves to dsRNA-containing endosomes in response to dsRNA"].
- ER -> Golgi -> endosome, chaperoned by UNC93B1; cathepsin B/H cleavage (aa 252-346)
  yields the signalling-competent, predominant endosomal form
  [PMID:22611194 "newly synthesized endogenous TLR3 is transported through the ER and Golgi apparatus to endosomes, where it is rapidly cleaved"; "TLR3 proteolytic processing is essential for its function"].
- Ligand interaction requires acidic pH
  [PMID:16144834 "TLR3 interacted with its ligand in acidic subcellular compartments"].
- Surface expression is cell-type dependent: endosomal only in myeloid DCs, but both
  surface and endosomal in fibroblasts, macrophages, epithelial cells
  [PMID:21266579 "it localizes to both the cell surface and endosomes of fibroblasts, macrophages, and epithelial cells"].
  This is why I split the plasma-membrane rows: `located_in` (TAS) kept as non-core,
  but `is_active_in` (IBA/IDA/IEA) marked over-annotated because signalling needs
  endosomal acidification.
- Termination: c-Src activates ZNRF1, which K63-ubiquitinates TLR3 at K813 for
  lysosomal degradation [PMID:37158982].

## Signalling

- MyD88-independent; uses TRIF/TICAM1 via the TIR domain
  [PMID:12471095 "Dominant-negative TRIF inhibited TLR3-dependent activation of both the NF-kappaB-dependent and IFN-beta promoters."; "TRIF associated with TLR3 and IFN regulatory factor 3."].
- Outputs: type I/III IFN (IRF3), canonical NF-kappaB, MAPK/JNK2, and (when
  cIAPs/caspase-8 blocked) RIPK3 necroptosis [PMID:21737330].
- Human fibroblasts express only TLR3 and respond to poly(I:C) with IFN-beta,
  IRAK4-independently [PMID:16286015 "Human fibroblasts express a single TLR, TLR-3, respond to only one known TLR agonist, poly(I:C), and secrete IFN-β and IFN-λ (this report)."].

## Disease / physiology

- Inherited TLR3 deficiency -> herpes simplex encephalitis; TLR3 largely redundant
  for most microbes, vital for anti-HSV-1 immunity in CNS
  [PMID:17872438 "Human TLR3 appears to be redundant in host defense to most microbes but is vital for natural immunity to HSV-1 in the CNS"].
- Also sensor of endogenous dsRNA in sterile skin-wound inflammation via JNK2
  [PMID:27830702].

## Project-question findings

- **PRR status (Q from TLR_FAMILY.md):** TLR3 is a bona fide PRR - it binds the
  microbial product (dsRNA) directly, unlike Drosophila Toll (binds Spaetzle
  cytokine). GO:0038187 accepted. It is on the GO:0002224 branch (GO:0034138 TLR3
  pathway), not GO:0008063 (fly Toll pathway).
- **No TLR-specific MF term exists;** GO:0038187 PRR activity + GO:0003725 dsRNA
  binding + GO:0004888 transmembrane signalling receptor activity are the right set.
  No new MF term proposed.

## Curation decisions of note

- Many generic `GO:0005515 protein binding` IPI rows (PIK3R1, TICAM1, WDFY1, UNC93B1):
  REMOVE as uninformative (per project policy); interactions not disputed. The TIR->TRIF
  interaction is captured by GO:0004888.
- `GO:0042802 identical protein binding` (homodimer): MODIFY -> GO:0042803 protein
  homodimerization activity, since ligand-driven homodimerisation is functional. The two
  isolated-TMD self-association papers (PMID:23155421, PMID:25217833) kept as non-core
  (in vitro peptide behaviour, not full-length receptor).
- `GO:0007250 activation of NIK activity` (NAS): MODIFY -> GO:0043123 canonical NF-kappaB;
  TLR3 does not activate the non-canonical NIK pathway.
- `GO:0006972 hyperosmotic response` (NAS, PMID:12054664): REMOVE - cited abstract has
  nothing on osmotic stress; likely an error.
- `GO:0042742 defense response to bacterium` (TAS, PMID:10426995): REMOVE - cited paper
  is about TLR2/lipoproteins; TLR3 redundant for antibacterial defence.
- `GO:0071260 cellular response to mechanical stimulus` (IEP, PMID:19593445): UNDECIDED -
  the cited full text is about BAD/prostate cancer and does not mention TLR3 at all.
  Flagged in references (relevance NONE) and as a suggested question. Not removed per the
  "do not overrule experimental annotation from incomplete evidence" rule (though IEP is
  weak; a curator should recheck the identifier).
- `GO:0032729 positive regulation of type II IFN production` (IDA, PMID:16286015):
  MARK_AS_OVER_ANNOTATED - IFN-gamma appears only in the paper's intro citing IRAK4
  literature; the paper's poly(I:C) experiments measure type I/III IFN. IFN-gamma is an
  indirect, cell-extrinsic effect.
- Transcription-regulation IEA rows (GO:0045944): MARK_AS_OVER_ANNOTATED - TLR3 acts far
  upstream of transcription factors.
- `GO:0045766 positive regulation of angiogenesis` (IEA): UNDECIDED - could not trace the
  mouse source or find supporting cached evidence.

## Deep-research cross-check (2026-09-30)

Compared the completed review against `TLR3-deep-research-falcon.md`.
**No annotation action, term, description or core function was changed;** two
`suggested_questions` were added for claims the report makes that could not be verified
against a primary paper.

Agreement:
- Endosomal/lysosomal dsRNA sensing with binding favoured at acidic pH (<=6.5), UNC93B1
  chaperoning from the ER, and cell-type-dependent surface expression on fibroblasts and
  epithelial cells. This is exactly the basis for splitting the plasma-membrane rows into
  `located_in` (non-core) and `is_active_in` (over-annotated).
- Structure-based, sequence-independent recognition of the ribose-phosphate backbone by the
  23-LRR ectodomain with sites at both ends of the horseshoe; ~40-50 bp minimum for a
  stable dimer. Matches the accepted dsRNA-binding rows and the H539/N541 mapping.
- TRIF/TICAM1 recruitment to the TIR domain with TBK1-IKKepsilon-IRF3 for type I interferon
  and TRAF6/RIPK1-TAK1-IKK for NF-kappaB and AP-1; RIPK3/MLKL necroptosis when caspase-8 is
  blocked. Matches the accepted interferon-beta and NF-kappaB rows and the non-core
  necroptotic row.
- Endogenous/damage-associated RNA as a ligand, consistent with keeping
  `inflammatory response to wounding` as non-core rather than core.

Additions not acted on (the report cites only secondary reviews; no primary paper was
available to quote, so nothing was asserted):
- Lateral multimerisation of TLR3 dimers along long dsRNA (reported 2023 cryo-EM), with
  >=90 bp needed for robust signalling. Recorded as a suggested question; the review still
  follows PMID:18172197 in treating one dimer as the minimal signalling unit.
- A reported TRIF-dependent MyD88 contribution to TLR3-driven NF-kappaB in mouse
  macrophages (2025). Recorded as a suggested question; the MyD88-independent model
  (PMID:12471095, PMID:16286015) is retained, and the description was not altered.
- TRIM56 as a scaffolding positive regulator of TRIF, and ligand-induced Tyr759/Tyr858
  phosphorylation. Both concern partners or modifications of TLR3, not new TLR3 functions.
- Disease associations (autoimmunity, allergy, calcific aortic valve disease) and
  poly(I:C)/poly-ICLC therapeutics. Indirect and pleiotropic; no NEW process terms.

Conflicts: the report describes TLR3 surface expression on fibroblasts and epithelial cells
as functional for detecting extracellular dsRNA, which sits against this review marking the
`is_active_in plasma membrane` rows as over-annotated. The report supports this only from
secondary reviews, so the decision stands and the existing suggested question on
cell-surface TLR3 signalling covers it.
