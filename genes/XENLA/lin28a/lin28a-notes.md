# lin28a (Xenopus laevis, Q8JHC4) — curation notes

Project: `projects/NEURAL_CREST_ORIGINS.md`, Tier 3 (blastula pluripotency programme retained in the crest).
Reviewed 2026-10-07 (claude-code).

## Identity

- Q8JHC4 = Xenbase lin28a.S (UniProt DR line `Xenbase; XB-GENE-866059; lin28a.S`), 195 aa, cold-shock domain
  (CSD) + two CCHC zinc knuckles; PANTHER PTHR46109:SF2 (Protein lin-28 homolog A). Paralog in frog:
  lin28b (Q8AVK2). X. tropicalis ortholog Q5EB47.
- Cloned by Moss & Tang 2003 [PMID:12798299 "These homologues are characterized by the LIN-28 protein's
  unusual pairing of RNA-binding motifs: a cold shock domain (CSD) and a pair of retroviral-type CCHC zinc
  knuckles"]. Frog expression: "Expressed from mid-gastrula to the tadpole stage" (UniProt, ECO:0000269 from
  PMID:12798299).
- All GO annotations on Q8JHC4 are electronic or ISS/IBA; there are no experimental frog annotations.

## Molecular activity (mostly mammalian, by homology)

- Human/mouse LIN28A binds the terminal loop of pre-let-7 (GGAG motif) and recruits TUT4 for
  oligouridylation, which blocks Dicer [PMID:19703396 "Lin28 recruits TUT4 to pre-let-7 by recognizing a
  tetra-nucleotide sequence motif (GGAG) in the terminal loop"]; [PMID:18951094 "The uridylated pre-let-7
  (up-let-7) fails Dicer processing and undergoes degradation"]. Lin28 "selectively blocks the processing of
  pri-let-7 miRNAs in embryonic cells" [PMID:18292307].
- So Lin28 is a *negative regulator* of let-7 biogenesis, not a component of the processing machinery:
  "Lin28 as a negative regulator of miRNA biogenesis" [PMID:18292307].
- Translational enhancer of specific mRNAs via RNA helicase A [PMID:21247876 "Lin28 may stimulate
  translation by actively recruiting RHA to polysomes"].
- Localisation: cytoplasmic, mRNPs, P-bodies, stress granules; nuclear accumulation when RNA binding is lost
  [PMID:17617744 "Lin28 is a conserved cytoplasmic protein"; "When both RNA-binding domains are mutated,
  Lin28 accumulates in the nucleus, suggesting that it normally shuttles from nucleus to cytoplasm bound to
  RNA"].
- **Frog-protein biochemistry (X. tropicalis lin28a, ortholog of Q8JHC4):** recombinant Xenopus lin28a binds
  the let-7g and pre-mir-363 terminal loops with similar affinity, GGAG-dependent [PMID:26447465
  "We demonstrate that lin28a binds to the terminal loop of pre-mir-363 with an affinity similar to that of
  let-7, and that this high affinity interaction requires to conserved a GGAG motif"]. Lin28 knockdown
  *reduces* mir-17~92/mir-106~363 family miRNAs [PMID:26447465 "Our data suggest a novel function for
  amphibian lin28 proteins as positive regulators of mir-17∼92 family miRNAs"]. So in frog the activity is
  pre-miRNA binding with sign-dependent outcome; MF = GO:0070883 pre-miRNA binding (NEW, ISS).

## Developmental roles in Xenopus

1. **Early embryo / germ layers (X. tropicalis, lin28a+lin28b compound morphants).** "Both lin28a and lin28b
   are expressed in pluripotent cells of the Xenopus embryo and are enriched in cells that respond to
   mesoderm-inducing signals"; "The development of axial and paraxial mesoderm is severely abnormal in lin28
   knockdown (morphant) embryos"; "the ability of pluripotent cells from the embryo to respond to the FGF and
   activin/nodal-like mesoderm-inducing pathways is compromised"; and "this early function is probably
   independent of the recognised role of Lin28 proteins in negatively regulating let-7 miRNA biogenesis"
   [PMID:23344711]. lin28 is an FGF target in X. laevis [PMID:19333377]. Interpretation: Lin28 sets the
   *competence/timing* of pluripotent cells' response to inducers, not maintenance of a stem-cell pool.
2. **Metamorphic timing (X. laevis, heat-shock overexpression).** "Lin28 overexpression before activation of
   TH signaling delays metamorphosis and inhibits the expression of TH target genes" [PMID:28359807]; a
   Lin28aΔC (no RHA interaction) still delays metamorphosis, "indicating that the translational regulation
   domain is not required to inhibit the HPT axis" [PMID:31397023]. Gain-of-function only, but it fits the
   conserved heterochronic role.

## Neural crest: what is the evidence?

- **Frog:** none functional. No Xenopus lin28 crest LOF/GOF found (PubMed "lin28 AND neural crest" returned 7
  hits, none Xenopus; "lin28 AND Xenopus" returned 10, none on crest; searched 2026-10-07).
- **PMID:25931449 (Buitrago-Delgado 2015) does not mention Lin28.** `grep -i lin28` on the cached full text
  (main text, PMC4652794) returns nothing; its shared blastula/NC factors are Myc, Id3, Sox5, TF-AP2, Ets1,
  FoxD3, Snail1, with Oct60/Sox3/Vent. The project page's inclusion of Lin28 in the shared programme should
  be sourced to PMID:39060477 and PMID:36182685 instead (supplementary figures of 25931449 were not checked).
- **Lamprey/Xenopus transcriptomes (PMID:39060477):** lin28 is in the list of pluripotency factors whose
  relative expression is conserved, "particularly within lamprey animal pole cells" ["These included homologs
  of id3, tfap2a, foxd3, pax3, zic1, lmo4, hif1a, dlx5, pbx1 (neural crest factors), myc, stat3, foxh1,
  foxi2, soxB1 (sox2/3), sox11, fgfr4, klf2/4/17, ventx/nanog, brd4, wdr5, lin28, znf281, geminin, yy1, sall4
  (pluripotency factors)"]. Expression only; blastula-weighted.
- **Chick (PMID:36182685):** "neural plate border cells have high expression of several canonical
  pluripotency genes like OCT4 (POU5F3 in chick), SOX2, LIN28A, and KLF5, which are lost at later
  developmental stages".
- **Chick functional (PMID:30520734, Bhattacharya 2018, full text):** Wnt/Lef1 directly activate a Lin28a
  enhancer; Lin28a MO or CRISPR reduces FoxD3/Sox10; rescued by WT Lin28a and by a let-7 sponge but not by
  mCCHC Lin28a; Lin28b knockdown has no effect; sustained Lin28a keeps multipotency genes on and delays
  differentiation. ["high levels of Lin28a during early development are necessary for neural crest
  specification, while its subsequent downregulation is required for silencing of progenitor identity";
  "the mCCHC Lin28a mutant protein could not restore FoxD3 or Sox10 expression"; "Lin28a, but not Lin28b, is
  significantly enriched in neural crest cells"]. This is a genuine competence/multipotency role, through
  let-7 suppression of direct let-7 targets ("Direct let-7 targets (Pax7, FoxD3, Myc) have seed sequence
  complementarity").

### Layer decision

Lin28a is, on frog evidence, a **general pluripotency / developmental-timing RNA-binding factor** (early germ
layer competence; metamorphic timing). On chick evidence it is a **neural crest competence/multipotency
factor** acting through the Lin28/let-7 axis — the same layer as Myc/Id3, and mechanistically linked (let-7
targets Myc). It is not a specifier and not a border specifier. Frog crest evidence is absent, so **no NC-branch
term is added to Q8JHC4**. The chick paper is uncurated in GO; chick LIN28A (Q45KJ5) would be the right
place for an IMP `GO:0014029` (competence-factor convention) — raise with curators.

Module: the competence part could hold a Lin28a annoton only with the chick member (Q45KJ5) as the grounded
participant; the frog member is not yet supported. Recommend recording it as a knowledge gap rather than an
annoton grounded on Q8JHC4.

### Comparator check (QuickGO, 2026-10-07)

Query: `annotation/downloadSearch?geneProductId=<all lin28 gene products in taxa 9606,10090,10116,7955,9031,
8355,8364 from geneproduct/search?query=lin28>&goId=GO:0014029,GO:0014032,GO:0014033,GO:0001755,GO:0014034,
GO:0014036,GO:0019827,GO:0048863,GO:0048864&goUsage=descendants&goUsageRelationships=is_a,part_of,occurs_in`.
Gene products included: human LIN28A Q9H9Z2, LIN28B Q6ZN17; mouse Lin28a Q8K3Y3, Lin28b Q45KJ6; rat; zebrafish
lin28a Q803L0, lin28ab, lin28b; chicken LIN28A Q45KJ5, LIN28B Q45KJ4; X. laevis lin28a Q8JHC4, lin28b Q8AVK2 +
TrEMBL; X. tropicalis Q5EB47 + TrEMBL.

Result: **no Lin28 family member in any of these species carries any neural crest branch term**
(GO:0014029/14032/14033/14034/14036/1755 and descendants). GO:0019827 rows: human LIN28A IMP (PMID:19703396);
mouse ISO/IEA from human; ISS from human on chicken Q45KJ5, X. tropicalis Q5EB47, zebrafish Q803L0, X. laevis
Q8JHC4. Mouse Lin28a has GO:0048863 stem cell differentiation IMP (PMID:18292307, PMID:18604195).
Interpretation: the absence of crest terms is not a convention against annotating Lin28 to crest — the one
crest paper (chick, PMID:30520734) is simply uncurated. But the frog gene has no crest data of its own, so the
gap to fill is on chick, not frog.

## GO:0019827 stem cell population maintenance — judged against frog evidence

Source: ISS from human LIN28A IMP (PMID:19703396, "Knockdown of TUT4 and Lin28 reduces the level of stem cell
markers, suggesting that they are required for stem cell maintenance" — cultured cells). Frog evidence: the
Xenopus role is responsiveness of transient pluripotent blastula cells to mesoderm inducers (PMID:23344711),
and metamorphic timing (PMID:28359807). No frog evidence of maintaining a stem cell population. The ISS
transfers an ES-cell culture phenotype to an embryo that has no self-renewing pluripotent population. Action:
MARK_AS_OVER_ANNOTATED (not wrong for mammals; over-reach for frog). It is also not the right home for the
crest competence role: the chick evidence is about holding multipotency within a migrating population over time,
which GO:0019827 would describe only loosely.

## Other decisions

- pre-miRNA processing (IBA/IEA/ISS) → MODIFY to GO:2000632 negative regulation of pre-miRNA processing:
  Lin28 blocks Dicer/Drosha processing of let-7; it does not perform the conversion. (Human carries
  GO:2000632 IDA, PMID:21247876.) Frog positive effect on mir-17~92 abundance (PMID:26447465) is not shown to
  act at the processing step, so it is recorded as a question.
- nucleic acid binding IEA (InterPro, incl. "CSP_DNA-bd") → MODIFY to GO:0003723 RNA binding. The CSD is an
  OB-fold that in Lin28 binds RNA; no DNA-binding activity is supported.
- Nucleus/nucleolus/rough ER/P-body/stress granule: non-core (shuttling; mammalian cell data).
- positive regulation of cytoplasmic translation ISS: non-core; mammalian RHA mechanism; frog Lin28aΔC
  result shows metamorphic delay does not need it.
- NEW GO:0070883 pre-miRNA binding (ISS from X. tropicalis lin28a, PMID:26447465).
- No NEW process terms. Considered and withheld: GO:0014029 (no frog crest data), GO:0040034 heterochronic
  regulation (frog overexpression only), GO:0001707 mesoderm formation (X. tropicalis compound lin28a+b
  morphants; paralog-shared; recorded as a question).

## Evolution / outgroups

- Lin-28 is an ancient bilaterian heterochronic regulator (C. elegans lin-28, Drosophila lin-28)
  [PMID:12798299]. The let-7 axis is pre-vertebrate. Lin28 as a pluripotency/competence factor therefore
  predates the crest; any crest role is co-option of an ancestral timing/potency module.
- Lamprey lin28 expression in animal pole cells is conserved with Xenopus (PMID:39060477, expression only).
- Paralog usage differs: in chick, Lin28a (not Lin28b) is crest-enriched and required; in Xenopus, lin28b is
  maternal and lin28a zygotic [PMID:23344711], and which paralog is in the frog border/crest is unknown.
- Homeologs: Q8JHC4 is lin28a.S; lin28a.L is TrEMBL. Frog morpholinos in PMID:23344711 were X. tropicalis.
