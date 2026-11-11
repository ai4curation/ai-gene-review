# SRY (human, Q05066) curation notes

Started 2026-10-24. Inputs: UniProt Q05066, GOA (46 rows), the OpenScientist report
(`SRY-deep-research-openscientist.md`, treated as leads), and primary papers cached under
`publications/`.

## Identity and architecture

- 204 aa, Y-linked, single HMG box (UniProt DNA_BIND 60..128). Two NLSs flank the box
  (61..77 and 130..136 in UniProt). Human SRY has no glutamine-rich C-terminal domain;
  the mouse protein does (see `genes/mouse/Sry/Sry-notes.md`).
- Cloned as the candidate TDF: [PMID:1695712 "This gene has been termed SRY (for
  sex-determining region Y) and proposed to be a candidate for the elusive
  testis-determining gene, TDF."]

## Molecular function

- Sequence-specific minor-groove binding with a sharp bend: [PMID:1425584 "when SRY binds
  to linear duplex DNA containing its specific target AACAAAG, it produces a sharp bend"];
  [PMID:8265659 "partial intercalation of a nonpolar side chain in the DNA minor groove"];
  NMR bend 54 +/- 2 degrees, reduced to 41 degrees by M64I [PMID:11563911].
- Li et al. reassessed M64I: in the full-length protein the tail restores bending and the
  defect is nuclear localization [PMID:16762365 "M64I-associated sex reversal is instead
  caused by the impaired function of a flanking non-classical nuclear localization signal
  (NLS)."]. So bend angle versus localization is unresolved for this allele.
- Transactivation of the human SOX9 TES with SF1 in NT2/D1 cells, and patient alleles
  reduce it [PMID:21412441 "SRY and SF1 co-operate to activate the human SOX9 homologous
  TES (hTES)"].
- Repression: SRY bridges via KRAB-O to KAP1 [PMID:19850934 "Transcriptional repression
  by SRY requires binding to KRAB-O, thus bridging to the KAP1 repression machinery."].
  Physiological repressed targets are not established (RSPO1 is proposed only).

## Nuclear import

- Two NLS pathways, CaM (N-terminal) and importin-beta (C-terminal):
  [PMID:12764225 "We conclude that SRY normally requires the two distinct NLS-dependent
  nuclear import pathways to reach sufficient levels in the nucleus for sex
  determination."]; [PMID:15746192 "The SRY N-terminal NLS (n-NLS) binds calmodulin (CaM)
  in vitro"].
- Exportin-4 imports SRY [PMID:19349578]; shuttling variants V60L/I90M reduce SOX9
  activation ~2-fold [PMID:24003159].
- Acetylation K136 by p300 promotes import; HDAC3 deacetylation gives cytoplasmic SRY
  [PMID:15297880].

## Speckles / splicing

- Ohe et al. saw SRY in SC-35 speckles in NT2/D1 [PMID:11818535]; Knower et al. did not
  [PMID:21412441 "Flag-SRY protein does not co-localize with splicing factor SC-35"].
  Nuclear speck is kept as non-core and contested; no splicing GO term proposed.

## Disease (verified against cached abstracts)

- 46,XY complete gonadal dysgenesis (Swyer syndrome): de novo HMG-box mutations
  [PMID:2247149 "the de novo mutation associated with sex reversal provides compelling
  evidence that SRY is required for male sex determination"]; nonsense W->stop and G->R
  [PMID:1339396]; missense plus a frameshift deletion in 3/5 CGD patients [PMID:1415266];
  five of 22 pure gonadal dysgenesis females had HMG-box changes, some de novo, one
  nonsense in sibs implying paternal gonadal mosaicism [PMID:8353496].
- Inherited variants shared with fertile fathers (V60L, I90M) [PMID:24003159, PMID:2247149].
- Partial gonadal dysgenesis: S18N outside the HMG box, familial [PMID:9521592].
- 46,XY ovotesticular presentation from a postzygotic gonadal SRY mutation (L101H)
  [PMID:8447323].
- NLS variants (R62G, R75N, R76P, R133W) partly cytoplasmic [PMID:12764225]; R75M
  cytoplasmic in a 46,XY CGD female with dysgerminoma [PMID:28030592].
- 46,XX testicular DSD: about 80% SRY-positive [PMID:20301589 "Approximately 80% of
  individuals with nonsyndromic 46,XX testicular DSD are SRY positive"], usually Xp;Yp
  translocation [PMID:25169080, PMID:32882067]. 46,XX ovotesticular cases with Yp on Xq
  [PMID:10602113] or gonad-restricted SRY mosaicism [PMID:9652903].

## Annotation judgements (summary)

- Generic DNA binding (IDA, IEA) -> MODIFY to DNA binding, bending plus RNA pol II
  cis-regulatory region sequence-specific DNA binding.
- Protein binding to NHERF2/SIP-1 -> MODIFY to PDZ domain binding (C-terminal 7 aa of SRY
  bind the PDZ domains) [PMID:9054412].
- DNA-binding TF binding (11 IPI rows, PMID:16582099): GST pulldowns of SRY HMG fragments
  with neural/glial TFs; real biochemistry, no SRY physiology -> KEEP_AS_NON_CORE.
- positive regulation of gene expression (NWD1, HEK293T overexpression, PMID:24681825) and
  positive regulation of DNA-templated transcription (PMID:21412441) -> MODIFY to positive
  regulation of transcription by RNA polymerase II.
- cell differentiation IBA -> MODIFY to Sertoli cell differentiation.
- NEW: calmodulin binding (PMID:15746192; mouse Sry also binds CaM, PMID:21558314).

## Open questions

- Direct in vivo target set of human SRY (only SOX9 TES/Enh13 and FGF9 promoter proposed).
- Contribution of DNA bending versus nuclear dose to individual patient alleles.
- Extragonadal (dopaminergic neuron) role: human SRY in TH+ neurons [PMID:22568433].
