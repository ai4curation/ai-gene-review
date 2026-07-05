# CAF120 (YNL278W / P53836) — curation notes

Journal of research for the AI GO-annotation review of *Saccharomyces cerevisiae* CAF120.
CAF120 is an **understudied ("dark") gene**: it is named as a CCR4-associated factor and
is reported to be associated with the CCR4-NOT complex, but its own molecular function and
biological role are essentially uncharacterized. The primary deliverable of this review is
therefore an honest `knowledge_gaps` section plus conservatively-reasoned `description` /
`core_functions` grounded in domain content, orthology and the sparse literature — never
invented function.

## Identity (verified from UniProt record)

- UniProt: **P53836** (CA120_YEAST); systematic name **YNL278W**; ORF N0610; SGD:S000005222.
- Standard name **CAF120** = "CCR4-Associated Factor 120" / "120 kDa CCR4-associated factor".
- 1060 aa, 118 kDa, non-essential.
- Present with 1380 molecules/cell in log-phase SD medium
  [UniProt MISCELLANEOUS, ECO:0000269|PubMed:14562106].

## Domain / family architecture (read inline from CAF120-uniprot.txt)

- Single recognized folded domain: a **PH (pleckstrin-homology) domain**, residues 75–204
  (PROSITE PS50003; Pfam PF00169 "PH" and PF25381 "PH_26"; SMART SM00233; Gene3D 2.30.29.30;
  SUPFAM SSF50729). InterPro **IPR058155 "Skg3/CAF120-like_PH"** — i.e. CAF120 defines,
  together with its paralog SKG3, a *specialized/divergent* PH-domain subfamily.
- The rest of the protein (≈residues 205–1060) is largely **intrinsically disordered**:
  MobiDB-lite disordered regions 465–589, 801–942, 955–1060, with low-complexity / polar /
  basic-acidic biased composition. No catalytic, nucleic-acid-binding, or other functional
  domain is annotated.
- **No protein kinase domain** is present (no PF00069 / Pkinase; the only Pfam hits are the
  two PH models). This is decisive for judging the IBA "protein kinase activity" annotation
  (see below).
- Heavily phosphorylated: MOD_RES phosphoserines at S491, S510, S518, S538, S556, S871, S885;
  S556 and others are **Cdk1 (Cdc28) substrate sites** [ECO:0007744|PubMed:19779198 "Global
  analysis of Cdk1 substrate phosphorylation sites"]. So CAF120 is a substrate of cell-cycle
  kinases, not itself a kinase.
- **Paralog SKG3 (YHR133C)** arose from the whole-genome duplication (SGD homology; shared
  IPR058155 PH family). SKG3 is likewise poorly characterized.

## CCR4-NOT association — nuanced, do not overstate

- UniProt FUNCTION/SUBUNIT (ECO:0000269|PubMed:11733989): describes CAF120 as a "component of
  the CCR4-NOT core complex … Subunit of the 1.0 MDa CCR4-NOT core complex that contains CCR4,
  CAF1, CAF120, NOT1, NOT2, NOT3, NOT4, NOT5, CAF40 and CAF130. In the complex interacts with
  NOT1." The generic CCR4-NOT FUNCTION text on the UniProt entry is the standard boilerplate
  for the complex (nuclear general transcription factor / cytoplasmic mRNA deadenylase), NOT a
  gene-specific experimental result for CAF120.
- BUT: the **cached PMID:11733989 abstract** ("Purification and characterization of the 1.0 MDa
  CCR4-NOT complex identifies two novel components") lists the identified 1.0 MDa components as
  "CCR4, CAF1, NOT1-5 and two new proteins, **CAF40 and CAF130**" — the abstract does **not**
  name CAF120 [PMID:11733989 "The 1.0 MDa complex was found to contain CCR4, CAF1, NOT1-5 and
  two new proteins, CAF40 and CAF130."]. The full text is not in our cache (full_text_available:
  false), so I cannot confirm what the paper says about CAF120 specifically.
- Critically, the **GO ontology's own definition of GO:0030015 "CCR4-NOT core complex"**
  enumerates the Saccharomyces core subunits as "Ccr4p, Caf1p, Caf40p, Caf130p, Not1p, Not2p,
  Not3p, Not4p, and Not5p" — **CAF120 is not listed** [GO:0030015 definition, verified via OLS].
- Consistent with this, **GOA has NO CCR4-NOT complex annotation for CAF120** (no GO:0030014/
  GO:0030015 in the goa.tsv), and SGD lists CAF120's molecular function and biological process
  as **unknown (ND)** [SGD locus S000005222; ND annotations GO:0003674 / GO:0008150,
  GO_REF:0000015].
- Interpretation: CAF120 is a *CCR4-associated factor* (hence the name) that co-purifies with
  or associates with CCR4-NOT, but its status as a stable/canonical core subunit is not
  established in GO/SGD and cannot be verified from the cached abstract. I therefore do NOT
  assert a CCR4-NOT core-complex membership as a confident core_function; I record it as a
  key knowledge gap and (at most) a KEEP_AS_NON_CORE / candidate association, not fabricated
  MF.

## Localization

- **Bud neck**: IDA, GO:0005935 [PMID:25028499]. Also captured in UniProt SUBCELLULAR LOCATION
  (Bud neck; ECO:0000269|PubMed:14562095, the Huh 2003 GFP localization atlas). Well supported.
- **Cytoplasm** and **Nucleus**: UniProt SUBCELLULAR LOCATION (ECO:0000269|PubMed:14562095);
  GOA has these as IEA GO_REF:0000044 (UniProtKB-SubCell mapping SL-0086 cytoplasm, SL-0191
  nucleus). Reasonable, evidence-backed subcellular locations.
- PMID:25028499 (Lee et al. 2014, "Proteome-wide remodeling of protein location and function by
  stress"; abstract-only in cache) reports that under **DNA-damaging conditions** Caf120 (among
  Tsr1, Dip5, Skg6, Lte1, Nnf2) **changes subcellular location** [PMID:25028499 "under
  DNA-damaging conditions, Tsr1, Caf120, Dip5, Skg6, Lte1, and Nnf2 change subcellular
  location"]. This is a condition-dependent relocalization observation, consistent with the
  multi-compartment (cytoplasm/nucleus/bud neck) steady-state localization.

## Phenotypes (SGD, background context — not directly annotatable here)

caf120Δ null: decreased competitive fitness in minimal medium; altered free amino-acid profile;
elevated cell-surface metal reductase activity; decreased vegetative & anaerobic growth;
abnormal vacuolar morphology; increased stress sensitivity [SGD locus S000005222, phenotype
summary]. These are diffuse, mostly high-throughput phenotypes and do not pin down a specific
molecular function — consistent with the "dark gene" status.

## Annotation-by-annotation reasoning (GOA)

1. **GO:0004672 protein kinase activity — IBA (GO_REF:0000033)** — from PANTHER family
   PTN001969686, with reference members = Arabidopsis MAP3K loci **AT1G05100, AT3G50310,
   AT4G26890** (WITH/FROM). CAF120 has **no protein kinase domain** (only the PH domain). This
   is a family over-propagation: a shared accessory PH module pulled a non-kinase yeast protein
   into a plant-MAP3K-dominated PANTHER cluster, inheriting the kinase MF from the kinase-domain
   members. Biologically indefensible → **REMOVE**.
2. **GO:0007165 signal transduction — IBA (GO_REF:0000033)** — same PANTHER family
   (PTN001969686), same Arabidopsis MAP3K reference set. "Signal transduction" is the generic
   BP the plant MAP3Ks carry. No evidence CAF120 acts in a signaling cascade; inherited via the
   same over-propagation. → **REMOVE** (over-annotation; no gene-specific support).
3. **GO:0005634 nucleus — IEA (GO_REF:0000044, SL-0191)** — UniProtKB-SubCell mapping backed by
   PubMed:14562095 (GFP atlas). Reasonable subcellular location. → **KEEP_AS_NON_CORE**.
4. **GO:0005737 cytoplasm — IEA (GO_REF:0000044, SL-0086)** — same GFP-atlas backing. Broad but
   correct location. → **KEEP_AS_NON_CORE**.
5. **GO:0005935 cellular bud neck — IEA (GO_REF:0000044, SL-0029)** — redundant with the IDA
   below but derived from the SubCell mapping. → **KEEP_AS_NON_CORE** (subsumed by the IDA).
6. **GO:0003674 molecular_function — ND (GO_REF:0000015)** — root "unknown MF" placeholder.
   Honest reflection of the dark-gene state; the ND is appropriate given no defensible MF. →
   **ACCEPT** (it correctly records that MF is unknown).
7. **GO:0008150 biological_process — ND (GO_REF:0000015)** — root "unknown BP" placeholder.
   Same rationale. → **ACCEPT**.
8. **GO:0005935 cellular bud neck — IDA (PMID:25028499)** — direct-assay localization to the
   bud neck. Well supported (and consistent with the Huh GFP atlas). → **ACCEPT** (best-supported
   experimental annotation).

## What is KNOWN vs NOT known

KNOWN:
- Subcellular localization: cytoplasm, nucleus, and bud neck (GFP atlas + IDA); relocalizes
  under DNA-damage stress.
- Has a divergent PH domain (Skg3/CAF120-like PH family, IPR058155); is a Cdk1 phosphosubstrate.
- Co-purifies with / is associated with the CCR4-NOT machinery (named "CCR4-associated factor";
  UniProt SUBUNIT), though not enumerated as a GO/SGD core subunit.
- Has a WGD paralog SKG3 (YHR133C), also uncharacterized.

NOT known (knowledge gaps):
- Molecular function: no demonstrated catalytic, binding, adapter, or scaffold activity. The PH
  domain's ligand (phosphoinositide? protein? — divergent family) is unknown.
- Biological role: whether it functionally contributes to CCR4-NOT mRNA deadenylation/turnover
  or transcriptional regulation, or acts independently at the bud neck, is unresolved.
- Whether it is a bona fide stable CCR4-NOT core subunit vs a transient/substoichiometric
  associated factor.
- Physiological meaning of bud-neck localization (cytokinesis/budding role?) and of the
  DNA-damage-induced relocalization.
- Functional relationship to / redundancy with paralog SKG3.

## Provenance summary of key references
- PMID:11733989 — CCR4-NOT 1.0 MDa complex purification (abstract-only in cache; names CAF40/
  CAF130 as new components; UniProt attributes CAF120 subunit status to it).
- PMID:14562095 — Huh 2003 GFP localization atlas (source of cytoplasm/nucleus/bud-neck SubCell).
- PMID:14562106 — Ghaemmaghami 2003 protein abundance (1380 molecules/cell).
- PMID:19779198 — Holt 2009 Cdk1 substrate phosphosites (CAF120 is a Cdk1 substrate).
- PMID:17287358 — Chi 2007 phosphoproteome (additional phosphosites).
- PMID:25028499 — Lee 2014 stress-induced relocalization; source of the bud-neck IDA
  (abstract-only in cache).
