# res1 (Sct1, p72res1) — curation notes

UniProt P33520; PomBase SPBC725.16; S. pombe 972h-. 637 aa; APSES/KilA-N HTH domain 6-112
(H-T-H motif 37-58), ankyrin repeats 236-265 and 357-386, disordered region 114-137;
mutagenesis E56K "renders the cell independent of cdc10 function for the execution of start"
(UniProt, from PMID:7916653). PANTHER PTHR43828:SF16; PAINT node PTN000917496 (APSES family:
Swi4, Mbp1, Swi6, Cdc10, Res1, Res2 and C. albicans / A. nidulans members).

Inputs used: `res1-uniprot.txt`, `res1-goa.tsv` (31 rows), `res1-deep-research-falcon.md`
(Edison synthesis built on Ayte 1995, Ayte 1997, Eshaghi 2011, Ivanova 2013, Knezevic 2018),
and the cached publications. Only PMID:24006488 is a full-text cache; every other cited paper
is abstract-only. The budding yeast MBP1 and SWI4 reviews were used as comparators, and the
cdc10 and res2 reviews are being written in parallel.

## Biology (what the primary literature actually shows)

- Discovery. res1+ was cloned as "a multicopy dual suppressor of the pat1 and cdc10 mutants"
  and is "required for entry into S phase"; the disruptant "grows poorly at 30 degrees C with
  severe heat- and cold-sensitivities, and completely arrests in G1 at 36 degrees C and 23
  degrees C" and "retains a full conjugation ability" [PMID:1464317]. The transcriptional role
  was inferred in 1992 from the Res1/SWI4 and Cdc10/SWI6 parallels: "Res1 might be a putative
  association partner of Cdc10 which appears to be involved at least in the activation of
  promoters containing a MluI cell-cycle box" [PMID:1464317].
- Independently found as sct1: "Loss of sct1 function results in cell cycle arrest at START
  and simultaneously in derepression of the mating pathway"; "p72sct1 is shown to act in
  partnership with p85cdc10 in a cell cycle regulatory transcription complex"; "A single
  dominant mutation within the putative DNA-binding domain of p72sct1 renders the cell
  independent of cdc10 function for the execution of START" [PMID:7916653].
- DSC1/MBF composition and cell-cycle regulation: the pombe DSC-1-like factor "is composed of
  at least the products of the cdc10 and sct1/res1 genes, and binds to the promoters of genes
  whose expression increases prior to S phase"; "p85cdc10 is a nuclear protein"; "the
  reactivation in late G1 is dependent on the G1 form of p34cdc2" [PMID:8223442].
- Domain mapping (the key biochemical paper): "p72res1 can bind specifically to the cdc22
  promoter, when analyzed by gel mobility shift assay, and that the N-terminal 157 amino acids
  of p72res1 are sufficient for this specific binding"; "the C-terminal region of p72res1 is
  necessary and sufficient for binding to p85cdc10"; "Overexpression of the cdc10-binding
  domain of p72res1 leads to a G1 arrest with a cdc phenotype and a decrease on MBF activity";
  "the MBF activity in vivo is dependent on the interaction of p85cdc10 with p72res1"
  [PMID:7739540].
- Res2/Pct1 paralog and division of labour: "two functionally overlapping parallel 'start'
  systems, Res1-Cdc10 and Res2-Cdc10, the former of which plays a major role in mitotic cycle
  whereas the latter in meiotic cycle" [PMID:8168485]; "Pct1+ is related to, but distinct
  from, the res1+/sct1+ gene that also encodes a p85cdc10 partner" [PMID:7926774]; in
  meiosis "cdc10+, res2+, rep1+ and rep2+ are required for correct meiotic transcription,
  while res1+ is not required for this process" [PMID:14648198].
- Target gene evidence: the cyc17 (cig2) "poly(A)+ transcript is significantly reduced in
  res1- cells" [PMID:7909513]; "the cell-cycle-regulated expression of the cyclin cig2 gene is
  dependent on MBF" and "Cig2p can bind to Res2p, promote the phosphorylation of Res1p and
  inhibit MBF-dependent gene transcription" [PMID:11781565].
- Activation vs repression within MBF: "res2p represses transcription in G2 of the cell cycle
  as a part of the DSC1 complex"; the DSC1 bandshift "requires res2p and correlates with
  inactive transcription" [PMID:9303312].
- Upstream control: "in addition to Cdc2, Sct1/Cdc10 complex formation requires Ran1"
  (through Puc1) [PMID:9201720].
- Chromatin occupancy (full text): Res1-HA ChIP on cdc22 and cdc18 promoters; "both Res1 and
  Res2 are released from chromatin after treatment with MMS"; the MBF core is Cdc10 plus
  "Res1 and Res2, which form a heterodimeric DNA-binding domain" [PMID:24006488].
- Localization: ORFeome YFP survey [PMID:16823372] scores Res1 nuclear (HDA); genome-wide
  ChIP-seq atlas of 89 tagged TFs [PMID:40015273] underlies the HDA cis-regulatory binding
  row. Res1 is not named in either abstract.

## Annotation decisions (31 rows: 24 ACCEPT, 5 MODIFY, 2 REMOVE)

- All MBF complex (GO:0030907), MCB/cis-regulatory binding (GO:0000978), activator MF
  (GO:0001228), positive regulation of Pol II transcription (GO:0045944), G1/S transition
  (GO:0000082), chromatin and nucleus rows: ACCEPT. Abstract-only rows (PMID:9201720
  chromatin IDA; PMID:9303312 EXP/IMP) are accepted with deference to the PomBase curator
  because the claims are clearly right for the gene even though the specific assay is not in
  the cached abstract.
- IBA rows: the target in its own WITH list (GO:0000978, GO:0030907, GO:0045944) is expected
  and treated as experimental grounding, not circularity. The GO:0030907 IBA is accepted for
  Res1 even though the same node wrongly gives MBF to Swi4 (pombe has a single MBF).
- GO:0005737 cytoplasm IBA (is_active_in, single donor Swi6): REMOVE with a
  propagation_review (PROPAGATION_BAD; COMPARTMENT_OR_COMPLEX_MISMATCH,
  WRONG_ORTHOLOG_OR_PARALOG), mirroring the SWI4 and MBP1 reviews. Cytoplasmic residence is a
  Swi6-specific regulated-import property; Res1 is nuclear (HDA) and chromatin-bound (ChIP).
- Protein binding (GO:0005515) rows, per the project policy for generic protein binding:
  - with Cdc10 (PMID:7739540): MODIFY -> GO:0046982 protein heterodimerization activity (the
    paper is titled on heterodimerization and maps the C-terminal Cdc10-binding region).
  - with Res2 (PMID:11781565, PomBase and IntAct duplicates): MODIFY -> GO:0046982, on the
    full-text statement that Res1 and Res2 "form a heterodimeric DNA-binding domain"
    [PMID:24006488].
  - with Cig2 (PMID:11781565, IntAct): REMOVE. The abstract attributes cyclin contact to Res2
    and only phosphorylation to Res1; no informative MF for Res1 follows. GO:0030332 cyclin
    binding would be the alternative if the full text shows direct binding.
- GO:0006357 regulation of transcription by RNA polymerase II IMP (PMID:1464317): MODIFY ->
  GO:0045944, since the direction is established by later work and the row is otherwise a
  less specific duplicate.
- GO:0045893 positive regulation of DNA-templated transcription IMP (PMID:7916653): MODIFY ->
  GO:0045944 (all MBF targets are Pol II genes; the gene's other IMP rows use the Pol II term).
- No NEW terms. UniProt calls Res1 "a negative regulator of sexual differentiation" and sct1
  loss derepresses mating [PMID:7916653], but PomBase has not annotated a conjugation term and
  the effect is plausibly indirect (G1 arrest is permissive for conjugation; the res1
  disruptant "retains a full conjugation ability" [PMID:1464317]). Raised as a question.
- UniProt DR lines list GO:0033309 SBF transcription complex IBA, which is not in the GOA
  seed; not reviewed here, but it would be the same paralog mismatch noted for Swi4/MBF.

## Core functions written

1. GO:0001228 activator MF (contributes_to GO:0000978 MCB binding), involved in GO:0045944 and
   GO:0000082, in chromatin/nucleus, in the MBF complex.
2. GO:0046982 heterodimerization with Cdc10, obligatory for MBF activity in vivo, involved in
   GO:0000082.

## Validation

`just validate SCHPO res1` passes; all supporting_text quotes were checked as verbatim
(whitespace-normalised) substrings of the cached publications or the deep-research file.
