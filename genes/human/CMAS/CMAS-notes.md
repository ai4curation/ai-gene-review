# CMAS (human) — review notes

UniProt: Q8NFW8 (NEUA_HUMAN). Gene: CMAS. HGNC:18290. Chromosome 12.
Recommended name: **N-acylneuraminate cytidylyltransferase** (EC 2.7.7.43).
AltName: CMP-N-acetylneuraminic acid synthase (CMP-NeuNAc synthase).

## Core biology

CMAS is the enzyme that **activates free sialic acid** so it can be used for
glycoconjugate biosynthesis. It condenses **N-acetylneuraminate (Neu5Ac)** with
**CTP** to form the sugar-nucleotide donor **CMP-N-acetylneuraminate (CMP-Neu5Ac)**
plus diphosphate. CMP-Neu5Ac is the universal donor substrate used by
sialyltransferases (after CMP-Neu5Ac is transported into the Golgi by SLC35A1).

- FUNCTION (UniProt): "Catalyzes the activation of N-acetylneuraminic acid (NeuNAc) to cytidine 5'-monophosphate N-acetylneuraminic acid (CMP-NeuNAc), a substrate required for the addition of sialic acid. Has some activity toward NeuNAc, N-glycolylneuraminic acid (Neu5Gc) or 2-keto-3-deoxy-D-glycero-D-galacto-nononic acid (KDN)." [file:human/CMAS/CMAS-uniprot.txt]
- CATALYTIC ACTIVITY (UniProt): "an N-acylneuraminate + CTP = a CMP-N-acyl-beta-neuraminate + diphosphate"; Rhea:RHEA:11344; EC=2.7.7.43; Evidence ECO:0000269|PubMed:11602804. [file:human/CMAS/CMAS-uniprot.txt]
- PATHWAY (UniProt): "Amino-sugar metabolism; N-acetylneuraminate metabolism." [file:human/CMAS/CMAS-uniprot.txt] (UniPathway UPA00628)
- Substrate promiscuity: acts on Neu5Ac, Neu5Gc and KDN — hence the recommended name is the general "N-acylneuraminate cytidylyltransferase", not just CMP-Neu5Ac synthase.

## Subcellular location — notably nuclear

Human CMAS is (at least partly) **nuclear**. This is unusual among the sialic-acid
biosynthetic enzymes (the others are cytosolic); CMP-Neu5Ac made in the nucleus is
then exported to the cytosol and imported into the Golgi.

- SUBCELLULAR LOCATION (UniProt): "Nucleus {ECO:0000269|PubMed:11602804}." [file:human/CMAS/CMAS-uniprot.txt] — experimental, from Lawrence et al. 2001.
- DOMAIN (UniProt): "The BC2 (basic cluster 2) motif is necessary and sufficient for the nuclear localization and contains the catalytic active site. The localization in the nucleus is however not required for the enzyme activity (By similarity)." [file:human/CMAS/CMAS-uniprot.txt] — i.e. nuclear localization and catalysis are separable; nuclear import is NOT needed for activity.
- SUBUNIT (UniProt): "Homotetramer; the active enzyme is formed by a dimer of dimers." [file:human/CMAS/CMAS-uniprot.txt]

Reactome R-HSA-4084982 concurs: "CMAS is ubiquitously expressed and localizes to the nucleus in mammalian cells. The active form of the enzyme is a homotetramer (a dimer of dimers) ... CMP-Neu5Ac is the donor substrate for sialyltransferases." [reactome:R-HSA-4084982]

## GO term id verification (OLS, 2026-07)

- GO:0008781 N-acylneuraminate cytidylyltransferase activity — MF; def "Catalysis of the reaction: CTP + N-acylneuraminate = diphosphate + CMP-N-acylneuraminate." Current, not obsolete. Core MF.
- GO:0006055 CMP-N-acetylneuraminate biosynthetic process — BP; current. Core BP (the actual product of the reaction).
- GO:0006054 N-acetylneuraminate metabolic process — BP; current. Parent/broader metabolic process (UniPathway IEA).
- GO:0005634 nucleus — CC; current. Experimental (Lawrence 2001) + HDA.
- GO:0005730 nucleolus — CC; current. HPA IDA (immunofluorescence).
- GO:0005654 nucleoplasm — CC; current. Reactome TAS.

## Annotation-by-annotation reasoning

1. GO:0008781 MF, IBA (GO_REF:0000033) — core catalytic function. ACCEPT. Directly supported by UniProt CATALYTIC ACTIVITY + EC 2.7.7.43 + phylogenetic (IBA) consensus across FB/MGI/ZFIN orthologs.
2. GO:0005634 nucleus, IEA (GO_REF:0000044, SubCell) — subcellular-location IEA that mirrors the experimental Nucleus location. ACCEPT (redundant with the HDA nucleus but correct).
3. GO:0008781 MF, IEA (GO_REF:0000120, RHEA/EC) — automated MF from the Rhea/EC mapping; identical to core function. ACCEPT.
4. GO:0006054 N-acetylneuraminate metabolic process, IEA (GO_REF:0000041, UniPathway) — correct but broad parent process. The reaction product is specifically CMP-Neu5Ac (GO:0006055), so this is a less-precise ancestor. KEEP_AS_NON_CORE (correct, but GO:0006055 is the precise core BP).
5. GO:0005730 nucleolus, IDA (GO_REF:0000052, HPA immunofluorescence) — HPA IF sub-nuclear localization. Consistent with the nuclear localization but nucleolar sub-compartment is not functionally established as where catalysis matters. KEEP_AS_NON_CORE.
6. GO:0006055 CMP-N-acetylneuraminate biosynthetic process, IMP (PMID:31121216) — Willems et al. 2019: CMAS KO cells have UNDETECTABLE CMP-sialic acid, directly demonstrating CMAS is required for CMP-Neu5Ac biosynthesis. This is the precise core BP. ACCEPT. (abstract-only cache; abstract explicitly states the CMAS-KO result.)
7. GO:0016020 membrane, HDA (PMID:19946888) — NK-cell membrane-proteome MS dataset. CMAS is a soluble nuclear/cytosolic enzyme with no TM domain; membrane capture is a proteomics artifact (paper itself notes ~60% of hits are not membrane proteins). Non-experimental for a specific function; over-annotation. MARK_AS_OVER_ANNOTATED (HDA, not IDA/IMP — do not REMOVE; flag as over-annotation).
8. GO:0005634 nucleus, HDA (PMID:21630459) — sperm-nucleus proteome MS. Corroborates nuclear localization (consistent with the experimental Lawrence 2001 nucleus). ACCEPT.
9. GO:0005654 nucleoplasm, TAS (Reactome:R-HSA-4084982) — Reactome states CMAS localizes to the nucleus; nucleoplasm is a reasonable sub-nuclear placement. Consistent with nuclear localization. KEEP_AS_NON_CORE.

## Publications reviewed (cache = abstract-only)

- PMID:31121216 (Willems 2019) full_text_available: false. Abstract supports GO:0006055 IMP: "CMP-sialic acid was ... undetectable in CMAS KO." RELEVANT/HIGH.
- PMID:19946888 (Ghosh 2010, NK membrane proteome) full_text_available: false. Large-scale MS; ~40% predicted membrane, remainder transient/artifactual. Supports only "membrane" HDA capture; LOW relevance to CMAS function.
- PMID:21630459 (de Mateo 2011, sperm nucleus proteome) full_text_available: false. Large-scale MS of sperm nuclei; supports nucleus HDA. MEDIUM (corroborative of nuclear localization).
- PMID:11602804 (Lawrence 2001) NOT in publications cache — this is the primary experimental reference for enzyme activity, tissue specificity, and Nucleus location (cited in UniProt with ECO:0000269). Its content is quoted here via the UniProt record (file: reference), not the paper directly.

## Core functions (synthesis)

- MF: GO:0008781 N-acylneuraminate cytidylyltransferase activity.
- BP: GO:0006055 CMP-N-acetylneuraminate biosynthetic process.
- Location: GO:0005634 nucleus (experimental; also detected nucleolus/nucleoplasm sub-compartments).

## 2026-10-09 — weekly compliance pass

Evidence-aware compliance (`just compliance-all`) had CMAS at 47.62 weighted.
All nine annotation actions were left unchanged — the prior review's calls hold —
and the pass added the missing justification and provenance.

- **`review.reason` added to all 9 annotations.** Two are worth recording here
  because the reasoning is more than "over-general / fine":

  - **GO:0006054 `KEEP_AS_NON_CORE` (not MODIFY).** These are not simply parent
    and child of one claim. GO:0006054 is about metabolism of
    **N-acetylneuraminate**, CMAS's *substrate*; GO:0006055 is about biosynthesis
    of **CMP-N-acetylneuraminate**, its *product*. CMAS genuinely participates in
    both — it consumes the one and makes the other — so the UniPathway row
    (UPA00628) is accurate at its own level of description, not a granularity
    error. Non-core only because the product term is the sharper statement and
    carries the IMP.
  - **GO:0016020 `MARK_AS_OVER_ANNOTATED` is the right action here**, in contrast
    to the GO:0005515 rows elsewhere in this batch: the defect *is* a claim
    exceeding the evidence. The measurement (CMAS peptides in a membrane fraction)
    stands; the inference to a membrane location does not. The authors' own stated
    limitation makes the call checkable rather than merely plausible:
    [PMID:19946888 "The remaining species were largely involved in cellular processes and molecular functions that could be predicted to be transiently associated with membranes."]
    — only ~40% of their 1843 IDs were predicted plausible membrane proteins.

- **Why the two nucleus-adjacent HDA rows get opposite treatment.** GO:0016020
  (PMID:19946888) is flagged; GO:0005634 (PMID:21630459) is accepted. The
  difference is convergence plus preparation quality — sperm nuclei were
  [PMID:21630459 "sperm nuclei were obtained through CTAB treatment and isolated to over 99.9% purity without any tail fragments, acrosome or mitochondria"]
  and the compartment is already established by low-throughput experiment
  (UniProt Nucleus, ECO:0000269|PubMed:11602804). Cell-type caveat now recorded:
  that observation is in mature spermatozoa, while the primary nuclear work is
  somatic.

- **`findings` added to all 9 bare references**, four of them on the UniProt
  entry. Verbatim quotes everywhere a source is cached; the five GO_REF findings
  are statement-only (documents not cached → quotes unverifiable). A second
  finding was added to PMID:31121216 recording the *within-panel contrast* that
  does the real work: CMP-sialic acid is only "dramatically reduced" in GNE and
  NANS KO but **undetectable** in CMAS KO, which is what places CMAS at the single
  committed step rather than merely in the pathway.

- **`alternative_products` descriptions.** Isoform 2 (VSP_012764) lacks residues
  264–434, the entire C-terminal half. Since the active enzyme is a dimer of
  dimers, whether this truncation can tetramerize is an open question, now raised
  explicitly rather than left implicit.

- **4 `suggested_questions` and 3 `suggested_experiments`** where there were none.
  The sharpest gap is the one UniProt itself sets up: the BC2 motif is "necessary
  and sufficient for the nuclear localization and contains the catalytic active
  site", yet [file:human/CMAS/CMAS-uniprot.txt "The localization in the nucleus is however not required for the enzyme
      activity"]. So nuclear residence may be a consequence of the active site
  overlapping an import signal and of no functional consequence — which is exactly
  why `nucleus` is annotated as a location with **no** corresponding nuclear
  process term. The proposed localization-restricted rescue would settle it.
  Second real question: CMAS accepts Neu5Gc, which humans cannot synthesize
  (CMAH inactivated), so its kinetic discrimination between Neu5Ac and Neu5Gc may
  set how much dietary Neu5Gc enters human glycoconjugates.

Result: 47.62 → **91.43** weighted, `just validate` clean (it was already clean
before). Remaining gaps are deliberate: five GO_REF `findings[].supporting_text`
slots, and `literature_support` on two rows that carry **no PMID at all** —
GO:0005730 nucleolus (reference is the HPA curation `GO_REF:0000052`) and
GO:0005654 nucleoplasm (reference is `Reactome:R-HSA-4084982`). Note also that
PMID:11602804 (Lawrence et al. 2001), the primary experimental source for the
activity, tissue specificity and nuclear location, is **not** in the publications
cache; everything from it is quoted through the UniProt record.
