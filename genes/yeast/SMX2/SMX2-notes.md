# SMX2 (P40204, YFL017W-A) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: SMX2 is the experimentally characterised SmG in PANTHER subfamily
PTHR10553:SF2 (SMALL NUCLEAR RIBONUCLEOPROTEIN G), which it shares with
S. pombe smg1 (O74966), Trypanosoma brucei Q382A6 and N. crassa NCU09880
(Q7S234). Human SNRPG (P62308) sits in the sister subfamily SF26 ("SMALL NUCLEAR
RIBONUCLEOPROTEIN G-RELATED"), and both subfamilies descend from the SmG PAINT node
PTN000058285 (WITH/FROM of the IBA rows lists SGD:S000002965, PomBase:SPBC4B4.05,
UniProtKB:P62308, UniProtKB:Q382A6, RGD:9286705). Subfamily assignments were checked
in `interpro/panther/PTHR10553/PTHR10553-entries.csv` and against UniProt's PANTHER
xrefs (O74966 and Q382A6 are SF2; the rat RGD:9286705 entry A0A8I5ZRW0 is SF26).
The RNA-binding IBA comes from a deeper node, PTN000058283, whose only listed donor
is yeast LSM7 (SGD:S000005091 = P53905), i.e. the node spanning SmG and Lsm7.
No ProtNLM2 output was consulted.

### Deep research

`just deep-research-falcon yeast SMX2 --fallback perplexity-lite` failed: falcon
returned "Exception: Failed to authenticate" and the perplexity fallback returned
HTTP 401 insufficient_quota. No deep-research file exists; the review is built from the
cached primary literature below.

### What is experimentally established in S. cerevisiae

- Sm ring subunit. Seven essential Sm proteins (B, D1, D2, D3, E, F, G) form the snRNP
  core; one copy of each per snRNP [PMID:11302706 "there is only a single copy of each
  Sm protein in the spliceosomal snRNP core domain"].
- Direct SmE partner. Two-hybrid and GST pulldown [PMID:9528767 "We observed
  interactions between SmB and SmD3, SmE and SmF, and SmE and SmG. For these
  interactions, a direct biochemical assay confirmed the validity of the results
  obtained in vivo."]. This is the F-E-G subassembly.
- Physical presence in snRNPs: U1 and U2 (mass spectrometry of purified snRNPs,
  PMID:9012791: "identified as the yeast homologs of the human Sm proteins D1, D2, D3,
  E, F, and G"; U2 core preparation "identical to the Sm proteins of the yeast U1
  snRNP"), U5 (PMID:11720284, PMID:11720285), U4/U6.U5 tri-snRNP (PMID:10377396,
  PMID:10449419), CWC/Cef1 complex (PMID:11884590), penta-snRNP (PMID:11804584),
  U1-U2 prespliceosome (PMID:16618970). Many yeast cryo-EM spliceosome structures
  include SmG (PDB 5GAN, 5LJ5, 5MQ0, 6J6G, 9DTR, etc.).
- RNA-site genetics [PMID:27417296]: yeast SmG Phe35-Asn37-Arg64 is the Sm-site
  uridine-binding triad (mapped from the human U1 snRNP structure); single Ala
  mutants are viable, F35A-N37A and F35A-N37A-R64A are progressively ts; N37A and
  R64A are synthetically lethal with RNA-site mutations in SmB, SmD3, SmE and SmF;
  many SmG alleles are synthetically lethal with lea1Δ/msl1Δ (U2 snRNP).
  "six intact RNA binding sites in the Sm ring can suffice for in vivo function,
  but five sites may not." SMX2 is essential (smgΔ complemented by plasmid shuffle).

### Inferred, not shown for SMX2 itself

- Direct contact of SmG with the snRNA Sm-site uridine: from human U1 snRNP crystal
  structure (Kondo 2015) and the yeast cryo-EM models, not a yeast biochemical assay.
- Cap hypermethylation (GO:0036261, IMP, ComplexPortal from PMID:9528767): the
  experiment depleted SmE, not SmG; the Tgs1 methyltransferase does the chemistry.
  The Sm core is the platform/substrate RNP. Treated as over-annotation for SMX2.
- Nucleus/cytoplasm: ISS from S. pombe smg1. Cytoplasmic precursor U5 snRNP in
  yeast (PMID:17934474) supports some cytoplasmic presence.

### SMN-Sm protein complex IBA

GO:0034719 is defined as Sm proteins associated with the SMN complex (SMN + Gemins).
S. cerevisiae has no SMN ortholog: a UniProt query (2026-10-21) for "survival motor
neuron"/smn1 in taxon 559292 returns only SMN1/YHR202W, a 5'-nucleotidase unrelated to
SMN; S. pombe has a true smn1 (Q09808). PMID:27417296: budding yeast has "in Brr1, a
putative homolog of the key metazoan Sm assembly factor Gemin2". The IBA donor is
human SNRPG only. The node placement is right for animals and fission yeast, but the
complex cannot form in budding yeast, so I REMOVE it for SMX2 (lineage loss of the
partner, not of SmG function).

### Decisions summary

- Core: Sm-ring subunit of U1/U2/U4/U5 snRNPs (and U4/U6.U5 tri-snRNP), contributes to
  snRNA (Sm site) binding, functions in mRNA splicing via spliceosome.
- protein binding (SmE) x3: REMOVE per protein-binding policy (interaction real).
- spliceosomal tri-snRNP complex IBA: MODIFY to U4/U6 x U5 tri-snRNP complex (yeast has
  only the U2-type spliceosome).
- protein-containing complex (ARBA): TOO_GENERAL.
- ND MF/BP rows: MODIFY to snRNA binding / mRNA splicing, via spliceosome.
- snRNA binding (GO:0017069, contributes_to) is proposed as the MODIFY replacement for
  the ND molecular_function row and used in core_functions, rather than as a separate
  NEW row. Comparator check: human SNRPG, pombe smg1 and other yeast Sm proteins carry
  only RNA binding / mRNA binding in GOA, so this refines an existing claim (RNA
  binding); it is not a new activity.
