# GTT3 (YEL017W / P39996) — curation notes

Journal for the AI GO-annotation review of *Saccharomyces cerevisiae* GTT3, an
understudied ("dark") gene. Provenance is recorded inline as
`[PMID:xxxx "verbatim quote"]` or `[file:... "quote"]`.

## Identity (from UniProt P39996, `GTT3-uniprot.txt`)

- **Standard name** GTT3; **systematic** YEL017W; UniProtKB **P39996** (`GTT3_YEAST`),
  337 aa, 38.2 kDa. RecName "Glutathione transferase 3".
- **PE 1 (evidence at protein level)** — detected in proteomics (phospho-MS,
  PaxDb/PeptideAtlas), so the protein is genuinely expressed
  [`GTT3-uniprot.txt` "PE   1: Evidence at protein level"; "Present with 1300 molecules/cell in log phase SD medium."].

## Domain / topology reasoning (inline, from `GTT3-uniprot.txt`)

- Family/domain signatures are **GTT3-specific and named "putative"**: Pfam
  **PF27945 (GTT3_N)**, PANTHER **PTHR41807** ("GLUTATHIONE TRANSFERASE 3"),
  InterPro **IPR038872** — whose InterPro name is **"Put_GTT3"** = *putative* GTT3
  [`GTT3-uniprot.txt` "InterPro; IPR038872; Put_GTT3." / "Pfam; PF27945; GTT3_N; 1."].
  These are **not** the canonical soluble-GST signatures (no thioredoxin/GST N-
  and C-terminal domain PROSITE/Pfam hits, no PF00043/PF02798). So the "glutathione
  transferase" name is an **annotation-by-name**, not a domain-supported catalytic call.
- **Membrane topology is the strongest structural fact.** UniProt models a large
  N-terminal cytoplasmic region (1-239) then **two transmembrane helices**
  (TRANSMEM 240-260 and 314-336) flanking a short perinuclear-space loop (261-313)
  [`GTT3-uniprot.txt` "TRANSMEM        240..260"; "TRANSMEM        314..336";
  "TOPO_DOM        261..313 /note=Perinuclear space"]. Multi-pass membrane protein.
  Canonical cytosolic GSTs (Gtt1/Gtt2, Gto1-3) are **soluble**, so a tail-anchored /
  multi-pass topology is unusual for a GST and argues against classic soluble-GST
  catalysis.
- The cytoplasmic N-terminus contains two disordered/low-complexity regions
  (66-95, 107-132; polar-residue biased) carrying multiple **Cdk1/phospho sites**
  (Ser-66/72/99/116) [`GTT3-uniprot.txt` "MobiDB-lite" REGIONs; MOD_RES phosphoserines
  from PMID:17330950, PMID:19779198]. Phospho-regulation is consistent with a
  regulated membrane protein but does not by itself assign a molecular function.

## Localization (KNOWN, high-throughput / experimental)

- **Nuclear membrane / multi-pass membrane protein** — UniProt SUBCELLULAR LOCATION,
  from the Huh et al. global GFP screen
  [PMID:14562095 "provide localization information for 70% of previously unlocalized proteins"].
- **Nuclear periphery (HDA)** — SGD annotation GO:0034399 from the SWAp-Tag N'-GFP
  library screen [PMID:26928762; localization category "Nuclear periphery" is one of the
  assigned classes: `GTT3-goa.tsv` row GO:0034399 HDA PMID:26928762].
- **Membrane (IBA)** — GO:0016020, phylogenetic (GO_Central) inference.
- Two orthogonal high-throughput localizations agree on nuclear-envelope / perinuclear
  membrane. `nuclear periphery` (a nuclear-lumen-proximal region) and `nuclear membrane`
  are consistent with a nuclear-envelope multi-pass protein.

## Molecular function (NOT known)

- GOA carries **GO:0003674 molecular_function, ND (no data)** — SGD explicitly records
  no molecular-function data [`GTT3-goa.tsv` GO:0003674 ND GO_REF:0000015].
- Deep research: *no direct enzymatic assay, substrate specificity, catalytic mechanism,
  or localization study* for Gtt3p was found
  [file:yeast/GTT3/GTT3-deep-research-falcon.md "no direct enzymatic assay, substrate
  specificity, or catalytic mechanism for the specific YEL017W protein was retrieved"].
- The GST-family literature (Gtt1/Gtt2/Gto1-3) is about the **paralogs**, not GTT3;
  Gtt1/Gtt2 are soluble ER/mitochondrial CDNB-active GSTs induced by oxidative stress
  [file:...falcon.md "Gtt1 and Gtt2 ... catalyze the enzymatic conjugation of glutathione
  (GSH) with a multitude of ... toxic compounds"]. GTT3 has the distinct Put_GTT3/GTT3_N
  domains and does **not** share these signatures.

## Biological process (NOT known)

- GOA carries **GO:0008150 biological_process, ND** [`GTT3-goa.tsv`].
- GTT3 is **not** co-regulated with the oxidative-stress GSTs: in a frataxin-deficient
  Friedreich's-ataxia yeast model its transcription is essentially unchanged
  [file:...falcon.md "GTT3 transcription was not detectably altered in the
  frataxin-deficient oxidative-stress model, unlike some other glutathione-related genes"],
  whereas Gtt1/Gtt2 are induced by H2O2 / cumene hydroperoxide. This weakens the
  assumption that GTT3 belongs to the same oxidative-stress detox pathway.
- The only deletion phenotype found is indirect: a SCRaMbLE synthetic-chromosome-V study
  where a YEL017W-containing deletion set increased prodeoxyviolacein output, mechanism
  unresolved and confounded by co-deletions [file:...falcon.md "the exact mechanism by
  which YEL017W deletion increases PDV productivity was not elucidated ... difficult to
  attribute the phenotype solely to loss of GTT3"]. Not curatable as a specific GTT3 role.

## Caveats about the falcon report

- The falcon report states "285 amino acids" — this is **wrong** (UniProt P39996 is
  **337 aa**). I do not propagate the length claim.
- Falcon could not retrieve the Huh et al. full text; I rely on the cached UniProt
  SUBCELLULAR LOCATION + GOA HDA rows for localization, which are independent of falcon.

## Curation decisions (summary)

- **GO:0016020 membrane (IBA)** — ACCEPT (broad but correct; multi-pass TM helices).
- **GO:0031965 nuclear membrane (IEA, SubCell)** — ACCEPT (Huh GFP + SubCell mapping;
  agrees with nuclear-periphery HDA). Core location.
- **GO:0034399 nuclear periphery (HDA, PMID:26928762)** — ACCEPT (experimental HT
  localization; do not overrule a curator's HDA call).
- **GO:0003674 molecular_function ND** — ACCEPT. No demonstrated activity; explicitly
  do NOT infer "glutathione transferase activity" (GO:0004364) — the name is
  annotation-by-analogy, domains are Put_GTT3-specific, no substrate demonstrated.
- **GO:0008150 biological_process ND** — ACCEPT. No specific process demonstrated;
  do NOT infer oxidative-stress/glutathione-metabolism from the paralogs.

## Knowledge gap (primary deliverable)

Gtt3 is **MF-dark and BP-dark with a solid CC**: its subcellular home (nuclear-envelope /
perinuclear multi-pass membrane) is established by two orthogonal screens, but its
**molecular activity, substrate, and biological role are entirely unknown**. The
"glutathione transferase" name rests on a family/name assignment (PTHR41807 / Put_GTT3),
not on any demonstrated GSH-conjugation activity; the GTT3-specific domains and the
multi-pass membrane topology distinguish it from the soluble Gtt1/Gtt2/Gto GSTs, and it
is not co-regulated with them under oxidative stress. Whether Gtt3 is even a bona fide
glutathione transferase is unresolved.
