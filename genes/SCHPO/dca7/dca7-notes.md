# dca7 (SPBC17D11.08 / O74763) — curation notes

Journal for the AI GO-annotation review of the *S. pombe* gene **dca7**
(systematic name SPBC17D11.08; UniProt O74763; PomBase standard name `dca7`).

## Identity (verified)

- UniProt: **O74763** (`YBE8_SCHPO`), 435 aa, "Uncharacterized WD repeat-containing
  protein C17D11.08" [dca7-uniprot.txt].
- PomBase standard name **dca7**, systematic name **SPBC17D11.08**; product line:
  "WD repeat protein, DDB1 and CUL4-associated factor Dca7, implicated in gene
  expression" (PomBase API, `dataset/latest/data/gene/SPBC17D11.08`).
- PomBase characterisation status: **"conserved unknown"** — i.e. a *dark* gene.
- Deletion viability: **viable** (PomBase).
- Taxonomic distribution: "eukaryotes only, fungi and metazoa"; PomBase species-distribution
  terms: conserved in eukaryotes / fungi / metazoa / vertebrates; "predominantly single copy
  (one to one)" (PomBase).

## Domain architecture (verified from UniProt)

- InterPro: **IPR045159 DCAF7-like**; IPR015943 WD40/YVTN repeat-like domain superfamily;
  IPR019775 WD40 repeat CS; IPR036322 WD40 repeat domain superfamily; IPR001680 WD40 repeat.
- Pfam PF00400 (WD40, x2); SMART SM00320 (WD40, x4); SUPFAM SSF50978 (WD40 repeat-like);
  PROSITE WD_REPEATS.
- UniProt FT: 4 WD repeats annotated (105–149, 164–204, 207–247, 313–353); disordered/low-complexity
  region ~352–371.
- PANTHER **PTHR19919** (WD REPEAT CONTAINING PROTEIN).
- No catalytic domain, no transmembrane region, no signal peptide. Consistent with a
  β-propeller scaffold/adaptor architecture rather than an enzyme.

## Orthology (verified)

- Human ortholog: **HGNC:30915 = DCAF7 / WDR68 / HAN11** (UniProt P61962) — the accession used
  in the S. pombe ISS annotation `GO:0080008` (PomBase ortholog_annotations, UniProt DR line).
- *S. cerevisiae*: **YPL247C**; *S. japonicus*: SJAG_04087 (PomBase ortholog_annotations).
- Reactome mapping: R-SPO-8951664 "Neddylation" (UniProt DR).

## What is KNOWN about the DCAF7/WDR68 family (from orthologs; NOT S. pombe-direct)

Grounded in the falcon deep-research report (dca7-deep-research-falcon.md), which cites
peer-reviewed DOI sources. The human/animal ortholog DCAF7/WDR68/HAN11 is a WD40 seven-blade
β-propeller with **no intrinsic catalytic activity**, acting as a scaffold/adaptor. Two recurrent
family roles are described in the literature:

1. **Scaffold/adaptor for DYRK-family kinases** (DYRK1A, DYRK1B) and HIPK2. This DYRK–WD40
   partnership is described as ancestral and conserved down to fungi — *S. cerevisiae* YPL247C
   interacts with Yak1, and *C. albicans* Orf19.384 forms a conserved complex with Yak1
   [Ananthapadmanabhan 2023, DOI:10.3389/fcell.2023.1277537; Glenewinkel 2016,
   DOI:10.1038/srep28241; Pinsky 2024, DOI:10.3390/jof10010083]. In humans the DYRK1A–DCAF7
   complex phosphorylates RNA Pol II CTD to promote myogenic transcription [Yu 2019,
   DOI:10.1093/nar/gkz162] — a plausible basis for PomBase's "implicated in gene expression"
   product tag.
2. **Substrate receptor for the CUL4–DDB1 (CRL4) E3 ubiquitin ligase** — this is the basis of
   the "DCAF" name; reported substrates include DNA ligase I, menin, ERCC1-XPF, and influenza PA
   [Peng 2016 DOI:10.1074/jbc.m116.746198; Kawara 2019 DOI:10.1016/j.bbrc.2019.08.147; Higa 2007
   DOI:10.1186/1747-1028-2-5; Lee & Zhou 2007 DOI:10.1016/j.molcel.2007.06.001]. NOTE: whether
   DCAF7 truly acts as a bona fide CRL4 substrate receptor versus primarily a kinase scaffold is
   *debated* in the literature (the DYRK-scaffold role is the more firmly established one).

## What is NOT known (the dark part)

- **No primary literature characterizes S. pombe dca7 / SPBC17D11.08 directly.** The falcon
  report states explicitly: "No primary literature was identified that directly characterizes
  SPBC17D11.08/dca7 in *S. pombe*." All functional inference is by orthology + domain.
- GOA records **MF = GO:0003674 (ND)** and **BP = GO:0008150 (ND)** for this gene: PomBase has
  formally declared molecular function and biological process **unknown**.
- No S. pombe DYRK partner has been demonstrated for dca7. (S. pombe encodes candidate
  DYRK/Yak-family kinases, but no dca7–kinase complex is reported.)
- Whether dca7 acts in a CUL4/DDB1 complex in fission yeast is **not experimentally shown**; the
  known S. pombe DCAFs are Cdt2 (canonical CRL4) and Raf1/Dos1 (CLRC heterochromatin) — dca7 is a
  *distinct* DCAF7-like protein, so the `GO:0080008` complex membership is an ISS inference from
  human P61962, not local evidence.

## Existing annotations (from dca7-goa.tsv) — review plan

1. `GO:0005634 nucleus` — **IBA** (GO_REF:0000033, PANTHER PTN000460287). Ortholog DCAF7 is
   nucleocytoplasmic; nuclear localization is plausible and phylogenetically supported. PomBase
   also carries this CC. KEEP as non-core (localization, not core function; no direct S. pombe
   localization datum for the nucleus — the direct large-scale localization study reported
   cytoplasm + Golgi).
2. `GO:0005737 cytoplasm` — **IEA** (GO_REF:0000044, UniProtKB-SubCell SL-0086). Backed by the
   S. pombe ORFeome-GFP localization study PMID:16823372 (UniProt SUBCELLULAR LOCATION: Cytoplasm
   {ECO:0000269|PubMed:16823372}). KEEP as non-core.
3. `GO:0005794 Golgi apparatus` — **IEA** (GO_REF:0000044, UniProtKB-SubCell SL-0132). Same
   PMID:16823372 source (UniProt: Golgi apparatus {ECO:0000269|PubMed:16823372}). This is a
   single high-throughput GFP localization; a WD40 scaffold is not an obvious Golgi resident and
   this may be a minor/secondary pool. KEEP as non-core but flag as weakly supported /
   over-interpretable.
4. `GO:0003674 molecular_function` — **ND** (GO_REF:0000015). This is the ND root placeholder =
   "MF unknown". Not something to ACCEPT/REMOVE as a real term; represents the knowledge gap.
   Mark accordingly (KEEP_AS_NON_CORE is inappropriate for a root; use the ND convention — action
   reflects that this is the honest "unknown" placeholder).
5. `GO:0008150 biological_process` — **ND** (GO_REF:0000015). Same: "BP unknown" placeholder.
6. `GO:0080008 Cul4-RING E3 ubiquitin ligase complex` — **ISS** from human DCAF7 P61962
   (GO_REF:0000024). Defensible orthology-based complex inference, but note the CRL4-receptor role
   of DCAF7 is itself debated, and there is no S. pombe evidence. KEEP_AS_NON_CORE (inferred,
   not core; do not upgrade to core without local evidence). Do NOT REMOVE — it is a
   curator ISS transfer from a legitimate ortholog, and the complex is real in the family.

## Localization datum detail

UniProt SUBCELLULAR LOCATION: "Cytoplasm {ECO:0000269|PubMed:16823372}. Golgi apparatus
{ECO:0000269|PubMed:16823372}." — both from the Matsuyama 2006 ORFeome-GFP global localization
screen (abstract-only in cache; individual-gene call is in supplementary data, curated by
UniProt/PomBase). PMID:18257517 (Wilson-Grady 2008 phosphoproteome) supports Ser266/Ser388
phosphorylation (UniProt MOD_RES).

## Interactions (PomBase, high-throughput; context only)

- fft3 (SPAC25A8.01c, Fun30-family chromatin remodeler) — Affinity Capture-MS [PMID:28218250].
- ppk15 (SPAC823.03, protein kinase) — Two-hybrid [PMID:26771498]. (Of note: ppk15 is a kinase,
  loosely consistent with the family kinase-scaffold theme, but this single Y2H hit is not
  sufficient to assert a DYRK-scaffold function in S. pombe.)
None of these full texts mention dca7/SPBC17D11.08 in prose (screen data only); they are not used
as supporting_text.

## Curation decisions summary

- Dark gene: MF and BP officially ND. `core_functions` kept **empty** — there is no direct
  evidence of any S. pombe molecular function, and the strongest signal (WD40 scaffold/adaptor)
  is an orthology hypothesis, not established fission-yeast function. The scaffold/DCAF hypothesis
  is captured in `knowledge_gaps` and `suggested_experiments` instead.
- `description`: project-independent, states it is an uncharacterized DCAF7-family WD40 protein,
  its domain architecture, its verified localization, and its conservation — without asserting a
  proven function.
- `knowledge_gaps` (REQUIRED): the MF is genuinely unknown (BIOLOGY gap, WHOLLY_DARK / MF_DARK).
