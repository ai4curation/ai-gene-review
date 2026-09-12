# HMGCL (human) review notes

UniProtKB:P35914 — Hydroxymethylglutaryl-CoA lyase, mitochondrial (HL; HMG-CoA lyase). EC 4.1.3.4.

Deep research: `HMGCL-deep-research-falcon.md` did NOT appear within the 8-min poll budget.
Review grounded in `HMGCL-uniprot.txt`, seeded GOA, cached `publications/PMID_*.md`, cached
`reactome/*.md`, and `~/repos/dismech/kb/disorders/3-Hydroxy-3-Methylglutaric_Aciduria.yaml`.

## Core biology
- Terminal (shared) step of **ketogenesis** and **leucine catabolism**: cleaves
  (S)-3-hydroxy-3-methylglutaryl-CoA → acetoacetate + acetyl-CoA (RHEA:24404; EC 4.1.3.4).
  [file:UNIPROT FUNCTION/CATALYTIC ACTIVITY]
- Requires a **divalent metal cation** (Mg2+/Mn2+) for activity; His233/His235/Asp42/Asn275
  coordinate the cation (crystal structure, PMID:16330550; cation binding, PMID:9200711).
- **(βα)8 TIM-barrel fold**; physiologically a **homodimer** (disulfide-linked via Cys323),
  can form homotetramers (PMID:16330550, PMID:12464283).
- **Localization:** mitochondrial matrix (mature form) + peroxisome (unprocessed precursor
  retaining the N-terminal mitochondrial leader, plus a C-terminal Cys-Lys-Leu PTS1-like
  motif). Dual targeting shown by PMID:8670134, PMID:9869651, PMID:7527399.
- Highest expression in liver (ketogenic tissue).

## Disease
- **HMG-CoA lyase deficiency / 3-hydroxy-3-methylglutaric aciduria (HMGCLD; MIM 246450)** —
  autosomal recessive; hypoketotic hypoglycemia + metabolic acidosis (± hyperammonemia),
  because both ketone-body synthesis and leucine degradation are blocked. Many characterized
  missense variants map to the active site / cation ligands (R41Q, D42H/G/E, H233R, etc.).
  [dismech 3-Hydroxy-3-Methylglutaric_Aciduria.yaml; UNIPROT DISEASE]

## Annotation-attribution nuance (IMPORTANT for the two 2012 IDA papers)
- **PMID:22847177** (full text available) and **PMID:22865860** (abstract only) are primarily
  about **HMGCLL1 / "er-cHL"**, a *close homolog encoded by a different gene* that localizes to
  ER + cytosol (NOT mitochondria/peroxisomes). GOA nonetheless has IDA annotations of
  P35914 (HMGCL) → GO:0004419 and GO:0046951 citing these two papers.
- These are experimental annotations I have not fully verified as being about P35914 itself.
  Per curation policy I do NOT REMOVE them. The *function asserted* (HMG-CoA lyase activity;
  ketone-body biosynthesis) is unambiguously correct for HMGCL and is independently supported
  by many other IDA/IBA/structural refs, so I ACCEPT (MF) / KEEP_AS_NON_CORE where duplicative.
  The full text of 22847177 uses mitochondrial HMGCL ("mHL") as the reference/comparison enzyme
  and its intro cleanly states HMGCL function, so quoting it for HMGCL is defensible.
  Note added in review.reason flagging the primary subject is HMGCLL1.

## GOA action plan (41 annotations)
- **MF GO:0004419** (lyase activity): core. IBA + all IDAs ACCEPT (core). IEA GO_REF:0000120 ACCEPT.
- **GO:0003824 catalytic activity** (IEA InterPro) — correct but far too general → MARK_AS_OVER_ANNOTATED.
- **GO:0016833 oxo-acid-lyase activity** (IEA InterPro) — correct parent, less specific than 0004419 → MARK_AS_OVER_ANNOTATED.
- **GO:0005198 structural molecule activity** (IDA PMID:12464283) — this paper is about oligomeric
  status (dimer/tetramer), NOT a structural (e.g. cytoskeletal) MF role; wrong MF branch. HMGCL is
  a catalytic enzyme, not a structural molecule → REMOVE is tempting but this is an experimental IDA;
  policy says do not REMOVE unverified experimental annotations. However GO:0005198 is a clearly
  mischosen MF (self-assembly of a homodimeric enzyme ≠ "structural molecule activity"). Use
  MARK_AS_OVER_ANNOTATED (not core; misapplied term) — do not assert paralog/wrong-gene.
- **Metal binding**: GO:0000287 magnesium ion binding (IDA 9200711) ACCEPT-core-support;
  GO:0030145 manganese ion binding (IDA 9200711) ACCEPT (both cations documented);
  GO:0046872 metal ion binding (IDA 16330550) MARK_AS_OVER_ANNOTATED (generic parent of the two specific).
- **BP GO:0046951** ketone body biosynthetic process — core (IBA, IEA, 2 IDA). ACCEPT.
- **BP GO:0006552** L-leucine catabolic process — core (IBA, IEA, NAS, TAS). ACCEPT.
- **BP GO:0006629 lipid metabolic process** (IDA 8027038) — over-broad; ketone bodies are lipid
  precursors but 0046951 is the precise term → MARK_AS_OVER_ANNOTATED.
- **CC mitochondrial matrix** GO:0005759 (IEA/ISS/TAS/NAS) ACCEPT-core.
- **CC mitochondrion** GO:0005739 (IBA is_active_in, IEA, HTP, IDA) ACCEPT.
- **CC peroxisome** GO:0005777 / **peroxisomal matrix** GO:0005782 — real (dual targeting), but
  non-core secondary localization; peroxisomal HL function "unknown" (9869651). KEEP_AS_NON_CORE.
- **CC cytosol** GO:0005829 (TAS Reactome R-HSA-9033235/9033236) — these Reactome events are the
  generic PEX5 peroxisomal-import machinery (cargo transiting cytosol before import), not evidence
  of a cytosolic catalytic pool of HMGCL. Transient/import-intermediate; KEEP_AS_NON_CORE.
- **CC protein-containing complex** GO:0032991 (IDA 12464283) — HMGCL is a homodimer; generic
  complex term. KEEP_AS_NON_CORE (homodimer is real but the term is uninformative).
