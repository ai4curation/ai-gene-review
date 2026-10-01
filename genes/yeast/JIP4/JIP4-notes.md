# JIP4 (YDR475C) — curation notes

Journal for the AI GO-annotation review of *Saccharomyces cerevisiae* **JIP4** (systematic
name YDR475C; UniProt Q03361; SGD:S000002883). This is an **understudied ("dark") gene**:
UniProt names it "Uncharacterized protein JIP4" (AltName "Jumonji-interacting protein 4"),
and SGD classifies it as a protein of unknown function. The deliverable therefore centres
on an honest `knowledge_gaps` section grounded in domain composition, orthology, and the
(sparse) literature — no invented function.

## Summary of what is machine-known (UniProt Q03361)

- 876 aa protein, MW ~98.7 kDa. Entry version 148 (2026). `PE 1: Evidence at protein level`
  — but the only experimental evidence is **large-scale phosphoproteomics** (see below);
  there is **no functional assay**.
- Highly **intrinsically disordered**: MobiDB-lite predicts 7 disordered regions
  (37–67, 112–155, 226–254, 330–353, 490–513, 661–728, 750–876) covering a large fraction
  of the protein. Multiple **low-complexity / compositionally biased** stretches, including
  runs of basic+acidic residues, polar residues, and notably several **Arg/Ser (RS-type)
  repeats** — e.g. `...RSVSSARRSRSRSRSRSICTRR...` (~aa 350–370) and
  `SKSRSSSKSRIRDKSKPSSP` (~aa 675–695), and a C-terminal `...KSRSPSSFRKEDE...RGGLFGFGRL`.
  These RS/RD-rich low-complexity tracts are the reason PANTHER places it in the
  SR-repetitive-matrix family (below). [file:yeast/JIP4/JIP4-uniprot.txt]
- **No PWI/RRM or catalytic domain** is annotated in UniProt. The 2026-09 UniProt record now
  lists two JIP4-family Pfam/InterPro entries, `JIP4_N` and `JIP4_helical`, in addition to
  disorder + compositional bias, but these domains do not establish a nucleic-acid-binding or
  enzymatic activity. This is important: the human family members that carry the splicing
  function have a folded **PWI** nucleic-acid-binding domain; JIP4 does not have one
  annotated. [file:yeast/JIP4/JIP4-uniprot.txt]
- **Phosphoprotein** (KW: Phosphoprotein). Eight phosphoserines mapped by MS:
  - Ser-48, Ser-51, Ser-510, Ser-552, Ser-775 [PMID:19779198 — Cdk1 substrate global analysis]
  - Ser-48, Ser-360, Ser-552 [PMID:18407956 — multidimensional chromatography phosphoproteome]
  - Ser-577 [PMID:15665377 — pheromone-signaling phosphoproteome]
  Several of these sites (from PMID:19779198, "Global analysis of Cdk1 substrate
  phosphorylation sites") indicate JIP4 is among the many proteins phosphorylated in a
  Cdk1-dependent manner; this is a large-scale substrate catalog, not a dedicated study of
  JIP4. [file:yeast/JIP4/JIP4-uniprot.txt]
- Cross-references indicate protein interactions exist in high-throughput datasets:
  BioGRID 87 interactions, IntAct 6, FunCoup 117 — i.e. it appears in interactome data but
  with no curated functional interpretation. [file:yeast/JIP4/JIP4-uniprot.txt]

## Orthology / family (PANTHER PTHR23148)

PANTHER assigns JIP4 to family **PTHR23148** ("Serine/arginine repetitive matrix"),
subfamily **PTHR23148:SF0** = "SERINE/ARGININE REPETITIVE MATRIX PROTEIN 1" (SRRM1 / SRm160).
The reviewed members of SF0 are essentially the metazoan **SRRM1** orthologs plus the two
yeasts [file:yeast/JIP4/interpro/panther/PTHR23148/PTHR23148-entries.csv... i.e.
interpro/panther/PTHR23148/PTHR23148-entries.csv]:

| UniProt | Species | Gene | Length |
|---------|---------|------|--------|
| Q03361  | S. cerevisiae | JIP4 (YDR475C) | 876 |
| Q52KI8  | Mouse | Srrm1 | 946 |
| Q5R5Q2  | Orangutan | SRRM1 | 917 |
| Q5ZMJ9  | Chicken | SRRM1 | 888 |
| Q8IYB3  | Human | SRRM1 | 904 |
| Q9USH5  | S. pombe | SPCC825.05c (PWI domain-containing) | 301 |

The **human/metazoan SRRM1 (SRm160)** is a nuclear-matrix SR-related splicing coactivator:
it promotes constitutive and ESE-dependent splicing by bridging sequence-specific SR
proteins to snRNP components, is a component of the spliceosome / exon junction complex,
binds RNA/DNA with low sequence specificity, and stimulates mRNA 3'-end cleavage.
[PANTHER family description, file:yeast/JIP4/interpro/panther/PTHR23148/PTHR23148-metadata.yaml;
corroborated by SRRM1/SRm160 literature — UniProt Q8IYB3.]

This family assignment is the sole basis for the **IBA** annotations in GOA:
- `part_of spliceosomal complex` (GO:0005681) — with/from MGI:1858303 (mouse Srrm1),
  PANTHER:PTN000567596, UniProtKB:Q8IYB3 (human SRRM1). [file:yeast/JIP4/JIP4-goa.tsv]
- `involved_in regulation of mRNA splicing, via spliceosome` (GO:0048024) — with/from
  FB:FBgn0036340 (Drosophila), PANTHER:PTN000567596. [file:yeast/JIP4/JIP4-goa.tsv]
- Current PAINT also lists an IBA `RNA binding` GO:0003723 from the same `PTN000567596`
  node. The QuickGO TSV row set still omits this 2026-08-28 PAINT assertion, and the
  2026-09 UniProt record no longer exposes it as a GO cross-reference either; validation
  rejects non-GOA rows unless they are proposed NEW annotations, so keep the review DRAFT
  unless and until the GOA cache contains the live row. [file:yeast/JIP4/JIP4-uniprot.txt;
  file:interpro/panther/PTHR23148/PTHR23148-paint.tsv]

### Caveat on the IBA splicing propagation (KEY reasoning)

Whether the metazoan SRRM1 splicing function transfers to yeast JIP4 is **doubtful**, for
biological reasons that are worth stating:

1. **JIP4 lacks the PWI domain.** The defining folded, nucleic-acid-binding module of the
   SRm160/SRRM1 and RED120 (PWI-motif) splicing proteins is the PWI domain. JIP4's UniProt
   record now annotates `JIP4_N` and `JIP4_helical` domains plus disorder and low-complexity
   bias, but still no PWI and no RRM. The S. pombe family member (Q9USH5) is explicitly a
   "PWI domain-containing protein" and is only 301 aa; the PANTHER node still reaches
   budding-yeast Jip4, but the target has diverged from these PWI-containing splicing
   proteins. [file:yeast/JIP4/JIP4-uniprot.txt; PANTHER entries csv]
2. **The budding-yeast splicing machinery is exhaustively characterized.** The S. cerevisiae
   spliceosome has been purified and defined in great biochemical/structural detail. The
   established yeast counterparts of the human SR-related nuclear-matrix splicing proteins are
   **Cwc21** (YDR482C; ortholog of SRm300/SRRM2) and candidate PWI proteins such as **Snu71**
   — *not* JIP4. JIP4 has never been reported as a spliceosome or EJC component in yeast
   spliceosome proteomics. [web: RNA journal / genesdev PWI-motif and Cwc21 characterization —
   background, not gene-specific experimental evidence for JIP4.]
3. The specific ESE-dependent splicing-coactivation role of metazoan SRm160 has not been
   demonstrated for budding-yeast Jip4.

Conclusion: the IBA MF/BP splicing terms are **plausible-by-homology but unverified and
biologically questionable** for yeast. They should be treated as low-confidence
homology-only inferences (mark as non-core / over-annotated candidates), not as established
JIP4 function. The RS/low-complexity composition supports at most a *possible* RNA/nucleic-
acid-associated or nuclear role, but this is not established.

## SGD / literature facts (verified via SGD, BioGRID)

- **Protein of unknown function.** Previously annotated as two separate ORFs (YDR474C and
  YDR475C) that were merged after corrections to the systematic reference sequence.
  [SGD locus JIP4/YDR475C; web:yeastgenome.org]
- **Paralog YOR019W**, arising from the whole-genome duplication; YOR019W is likewise
  uncharacterized. jip4∆ is **viable**; yor019w∆ is viable (double mutant not annotated) —
  consistent with a non-essential, possibly redundant gene. [SGD; web:yeastgenome.org]
- Name "Jumonji-interacting protein 4" (JIP4) is a **legacy/heuristic name** (likely from an
  interaction dataset with a Jumonji/JmjC-family protein); it does not by itself establish a
  molecular function. No dedicated functional paper on yeast JIP4 was found.
- Appears in high-throughput interactome data (BioGRID 87 / IntAct 6) and in
  phosphoproteomics, but with no curated functional role.

## KNOWN vs NOT-KNOWN

**KNOWN (evidence-supported):**
- It is expressed and made as a protein (PE1).
- It is an in vivo phosphoprotein with ≥8 mapped phosphoserines, including Cdk1-dependent
  sites (large-scale MS). [PMID:19779198; PMID:18407956; PMID:15665377]
- It is intrinsically disordered with RS/low-complexity composition (sequence-based).
- It is a member (by low-complexity composition) of the SR-repetitive-matrix PANTHER family
  that in metazoa contains SRRM1/SRm160.
- Non-essential; has a WGD paralog (YOR019W).

**NOT KNOWN (genuine knowledge gaps):**
- Molecular function — no biochemical activity demonstrated; no folded catalytic/binding
  domain identified. RNA binding is only an IBA guess.
- Whether it is truly part of the spliceosome / involved in splicing in yeast (IBA only;
  biologically questionable, see caveat).
- Subcellular localization — not experimentally established (no CC annotation beyond ND).
  RS-rich composition *hints* at nuclear, but unverified.
- Biological process / pathway — unknown (ND at the BP root).
- Loss-of-function phenotype beyond "viable"; role of the phosphorylation; the identity/
  meaning of its interactors; functional relationship to paralog YOR019W.
- What the "Jumonji-interacting" name refers to mechanistically.

## Curation plan

- IBA `spliceosomal complex` (CC) and `regulation of mRNA splicing` (BP): keep but mark as
  **non-core / over-annotated** homology-only inferences — do NOT elevate to core function;
  document the PWI-absence + yeast-splicing-machinery caveat in the review reason. (Per
  guidelines, IBA over-propagations may be argued against on biological grounds.)
- ND molecular_function / cellular_component / biological_process root terms: these are
  "no data" placeholders; keep as-is (they honestly encode "unknown"). Mark KEEP_AS_NON_CORE
  / note that they reflect the dark-gene status.
- `description`: project-independent — disordered RS/low-complexity protein of unknown
  function, SR-repetitive-matrix family by composition, phosphoprotein, non-essential, WGD
  paralog YOR019W. No curation commentary.
- `core_functions`: only the defensible minimum (essentially none can be asserted with
  confidence; possibly a cautious statement that no core molecular function can be assigned).
- `knowledge_gaps`: the primary deliverable (MF, localization, BP, phenotype, splicing
  hypothesis).

## Update after falcon deep research (2026-07-05)

The falcon deep-research report (`JIP4-deep-research-falcon.md`, Edison, 20 citations,
~23 min) is consistent with the assessment above and adds one useful hypothesis about the
gene name:

- The "Jumonji-interacting protein 4" name most plausibly reflects identification of JIP4 as
  a **Gis1-associated factor**. Gis1 is a JmjC (Jumonji-domain) zinc-finger transcription
  factor that acts downstream of the **Rim15/TOR/Sch9** nutrient-signaling and
  calorie-restriction response pathway [file:yeast/JIP4/JIP4-deep-research-falcon.md
  "Gis1 is a Jumonji-domain zinc-finger transcription factor acting downstream of
  **Rim15/TOR/Sch9** nutrient signaling"]. The report explicitly flags that "direct
  mechanistic characterization remains limited", i.e. this is a naming-origin inference, not
  an established function — treated here as a hypothesis in knowledge_gaps / suggested
  questions, not as core function.
- The report reconfirms: merged ORF (YDR474C+YDR475C), non-essential, paralog YOR019W,
  Ser/Arg repetitive matrix (IPR052225) domain class, uncharacterized status, and that the
  splicing/RNA-processing role is a low-to-moderate-confidence domain-based inference only.
- CAVEAT: the report states a "165 aa" size for a "merged gene model/extension" — this is
  inconsistent with the authoritative UniProt length of **876 aa** (Q03361) and is not used;
  it appears to be a confused artifact from the ORF-merge re-annotation history.

## 2026-09-30 IBA re-review

- Rechecked the PTHR23148 IBA rows against the cached PAINT export. `GO:0005681`
  spliceosomal complex, `GO:0048024` regulation of mRNA splicing, via spliceosome, and
  `GO:0003723` RNA binding all trace to the all-eukaryote `PTN000567596` node.
  `GO:0003723` is already present in UniProt's GO_Central rows for JIP4, but QuickGO
  still omits the 2026-08-28 PAINT assertion.
- Retained the two GOA IBA rows as `MARK_AS_OVER_ANNOTATED`, left the live RNA-binding IBA
  as a draft-blocking follow-up, and confirmed that Jip4/Q03361 is in the same cached
  SRRM1 subfamily as human and mouse SRRM1, so the PANTHER family placement itself reaches
  the target. The problem is target-specific functional divergence: S. cerevisiae Jip4 has
  no annotated PWI or RRM domain, no demonstrated RNA binding, and no experimental
  spliceosome or splicing-regulator role.

## 2026-10-01 current GOA refresh

- Forced a fresh GOA/UniProt pull for JIP4. QuickGO still returns exactly five live rows:
  two over-propagated PTHR23148 IBA rows and the three SGD ND root placeholders.
- Copied the explicit IBA `WITH/FROM` values into `supporting_entities`: the spliceosomal
  complex row now records mouse Srrm1, human SRRM1, and `PANTHER:PTN000567596`; the
  mRNA-splicing regulation row records the Drosophila seed and the same PANTHER node.
- Refetched the PTHR23148 PAINT cache and confirmed the same root node still carries three
  node-level assertions: `GO:0005681`, `GO:0048024`, and the 2026-08-28 `GO:0003723` RNA
  binding assertion. The RNA-binding assertion remains absent from QuickGO and has now also
  disappeared from UniProt's GO cross-references, so no non-GOA RNA-binding row was added.
- Updated the domain caveat for UniProt entry version 149: the record now lists Pfam/InterPro
  `JIP4_N` and `JIP4_helical`, but still no PWI/RRM or catalytic domain. These new
  JIP4-family domains do not rescue the SRRM1 splicing-function transfer.
- Searched again for recent direct JIP4/YDR475C literature. No newer paper assigning a
  target-specific yeast molecular function, RNA-binding activity, localization, or
  spliceosome role was found.
