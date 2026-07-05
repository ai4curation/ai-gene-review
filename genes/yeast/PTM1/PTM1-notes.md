# PTM1 (YKL039W) — curation notes

Journal of research for the AI GO-annotation review of *Saccharomyces cerevisiae* PTM1
(UniProt P32857, systematic name YKL039W, SGD:S000001522).

## Summary of the curation problem

PTM1 is a **dark / understudied** gene. Its very name PTM1 stands for "**P**utative
**T**rans**M**embrane protein", coined in the 1993 GenBank submission that first noted it
"enhances recovery from transformation of a profilin deletion strain" (Haarer, Petzold &
Brown, submitted to EMBL/GenBank/DDBJ Mar-1993; cited as UniProt reference [1]). No
dedicated functional study of PTM1 itself has been published. Everything known is
(a) sequence/topology, (b) one experimental localization (co-purification with a late-Golgi
compartment), (c) one phosphoproteomic dataset, and (d) inference from the wider
GPR107/GPR108/TMEM87 (GOST/LUSTR) protein family, whose molecular function is itself
largely unresolved.

The primary deliverable is therefore an **honest knowledge_gaps section** plus a carefully
reasoned localization-grounded description and minimal core_functions — no invented function.

## What is KNOWN

### Sequence, topology and domain architecture (UniProt P32857, inline from PTM1-uniprot.txt)
- 523 aa, MW 60 kDa, precursor with an N-terminal **signal peptide (1–26)**.
- **Seven transmembrane helices** predicted (TM1 198–218, TM2 231–251, TM3 266–286,
  TM4 305–325, TM5 334–354, TM6 382–402, TM7 418–438), with a large **lumenal
  N-terminal domain (27–197)** and a **cytoplasmic C-terminal tail (439–523)**. This is the
  canonical GOST/LUSTR "GOLD-domain + 7TM" architecture (N-terminal lumenal β-sandwich
  atop a GPCR-like 7TM bundle).
- Pfam / InterPro domains: **GOST_TM (PF06814 / IPR053937)**, **GPR107/GPR108-like
  (IPR009637)**, **PTM1-like_N (PF21902 / IPR053938)**. UniProt SIMILARITY: "Belongs to the
  LU7TM family" (LU7TM = Lung Seven TransMembrane / LUSTR).
- PANTHER family **PTHR21229 "LUNG SEVEN TRANSMEMBRANE RECEPTOR"**; PTM1 is in
  subfamily **PTHR21229:SF1** together with its yeast paralog **YHL017W (P38745)** and the
  *S. pombe* proteins SPAC26H5.07c / SPBC18A7.02c. The mammalian members GPR107 (SF12),
  GPR108 (SF11), TMEM87A/TMEM87B (SF19/SF16) sit in **distinct subfamilies** — relevant to
  how far specific mammalian phenotypes can be transferred to PTM1 (see below).
- One predicted **N-glycosylation site (Asn132)**; UniProt keyword Glycoprotein; single
  GlyGen/GlyCosmos site → consistent with a lumenal, glycosylated ectodomain of a
  secretory-pathway membrane protein.
- Disordered, acidic C-terminal region (483–523) carrying three mapped phosphosites.
- Paralog **YHL017W** arose from the whole-genome duplication (ohnolog pair) — a second,
  equally uncharacterized yeast GOST protein. Possible functional redundancy is a live
  hypothesis and complicates single-deletion phenotype interpretation.

### Subcellular localization (experimental)
- UniProt SUBCELLULAR LOCATION (ECO:0000269|PubMed:16107716): **Golgi apparatus membrane;
  Multi-pass membrane protein. Early endosome membrane; Multi-pass membrane protein.
  Note=Copurifies with the late Golgi SNARE TLG2.**
- Source: Inadome, Noda, Adachi & Yoda 2005 [PMID:16107716]. This paper immunoisolated
  yeast Golgi subcompartments using the SNAREs **Sed5 (early Golgi)** and **Tlg2 (late
  Golgi/endosome)** and catalogued the membrane proteins of each. PTM1/YKL039W was detected
  among the proteins co-purifying with the **Tlg2 (late-Golgi/endosome) compartment**; that
  detection is the experimental basis for UniProt's Golgi-membrane / early-endosome-membrane
  localization. NOTE: the cached full text of PMID:16107716 is abstract + Discussion only
  (the Results/Tables where YKL039W would be individually listed were not captured in the
  HTML extraction), so I cannot quote "PTM1"/"YKL039W" verbatim from the cache. The paper's
  scope is directly on-point:
  [PMID:16107716 "we immunoisolated vesicles carrying either of the SNAREs Sed5 or Tlg2, the
  markers of the early and late Golgi compartments, respectively, and analyzed the membrane
  proteins"]. The localization annotation itself is a curator-made experimental (SGD/UniProt)
  call from full text; I defer to it.

### Post-translational modification (experimental, large-scale)
- Phosphorylated at **Ser480, Thr483, Thr498** in the cytoplasmic acidic tail
  (ECO:0007744|PubMed:18407956, Albuquerque et al. 2008 phosphoproteome). Cached entry for
  PMID:18407956 is abstract-only (large-scale MS survey); establishes that PTM1 is a
  phosphoprotein but says nothing about biological role.

### Gene history / naming
- Original functional hint: overexpression "enhances recovery from transformation of a
  profilin (PFY1) deletion strain" (UniProt ref [1], Haarer/Petzold/Brown 1993 GenBank
  submission). This is a suppressor-of-transformation-stress observation, NOT a defined
  molecular function, and has not been followed up mechanistically.
- Sequence had two historical frameshift errors (CAA49300.1, CAA81874.1), corrected in the
  reference genome; PE=1 (evidence at protein level).

## What is NOT known (the gaps)
- **Molecular function**: unknown. No enzymatic activity; no demonstrated ligand, transporter
  substrate, or channel activity for PTM1 or, in most cases, for the whole GOST family.
- **Transported / handled molecule**: unknown. The family is *hypothesized* (by structural
  analogy to Wntless, which chaperones lipidated Wnt) to bind hydrophobic cargo/lipid in the
  7TM cavity, but no cargo is established for PTM1.
- **Biological process**: unknown beyond a presumed role in secretory-pathway / Golgi
  membrane-protein trafficking, inferred from localization and family (IBA).
- **Loss-of-function phenotype**: no clear phenotype reported for the *ptm1Δ* single mutant;
  the WGD paralog YHL017W may buffer it. BioGRID lists genetic/physical interactions but no
  defining functional phenotype.
- **GPCR-like signaling**: explicitly NOT supported for the family — see family evidence.

## Family / orthology evidence (for IBA appropriateness and gap framing)

PTM1 is the fungal representative of the GOST (GOLD-domain seven-transmembrane) / LUSTR /
LU7TM family. Two recent structural papers characterize the family (used here for the
gene-review references; they concern human paralogs, not PTM1 directly, so relevance to PTM1
is MEDIUM and localization/mechanism claims are transferred cautiously):

- **TMEM87A cryo-EM structure**, Hoel et al. 2022 eLife [PMID:36373655]:
  - Family = GOLD domain + GPCR-like 7TM; proposed common trafficking role:
    [PMID:36373655 "structurally homologous GOST proteins could serve a common role in trafficking"].
  - Not a channel: [PMID:36373655 "We conclude that under these conditions, TMEM87A does not
    form a mechanosensitive ion channel"].
  - Probably not a GPCR: [PMID:36373655 "these differences suggest that TMEM87A may not
    couple to G proteins or arrestins like canonical GPCRs"].
- **GPR180 / GOST review+structure**, 2024 Commun Biol [PMID:39609618]:
  - [PMID:39609618 "Little is known about ligands and the exact function of GOST proteins"].
  - [PMID:39609618 "it was speculated that GOST proteins might function as trafficking
    chaperones for membrane-associated cargo"].
  - [PMID:39609618 "The functional role of GOST proteins is still enigmatic"].

Mammalian family members have specific reported roles (GPR107: retrograde toxin transport,
receptor recycling; GPR108: AAV transduction; WLS: Wnt secretion chaperone) but these map to
**different PANTHER subfamilies** than PTM1 (SF1). The conserved thread across the whole
family — including the fungal SF1 branch — is **Golgi/endosome localization and a presumed
role in membrane-trafficking of hydrophobic/membrane-associated cargo**, with molecular
mechanism unresolved. Transferring a specific mammalian phenotype (e.g. AAV transduction,
Wnt secretion) to yeast PTM1 would be over-annotation; transferring the general
Golgi-localization + trafficking-context is defensible but should stay non-core / general.

## Annotation-by-annotation reasoning (10 GOA annotations, all IBA/IEA/ND)

1. **GO:0005794 Golgi apparatus** (IBA, GO_REF:0000033) — ACCEPT. Consistent with the
   experimental co-purification with the Tlg2 late-Golgi compartment (PMID:16107716) and
   family-wide Golgi localization. Core localization.
2. **GO:0016020 membrane** (IBA, GO_REF:0000033) — MODIFY→ generalize is not needed but the
   bare "membrane" is uninformative given we know it is a Golgi/endosome multi-pass membrane
   protein. Keep as non-core (it is a true but shallow parent of the specific CC terms).
3. **GO:0042147 retrograde transport, endosome to Golgi** (IBA, GO_REF:0000033) — this is the
   only BP annotation with any specific content. It is IBA-transferred from mammalian
   orthologs (with/from includes UniProtKB:Q8NBN3 GPR108, Q96K49 TMEM87B). There is no
   *direct* yeast evidence that PTM1 mediates endosome-to-Golgi retrograde transport;
   however the localization (late-Golgi/endosome) is compatible and the family is
   trafficking-associated. Given no yeast experimental support and subfamily divergence,
   KEEP_AS_NON_CORE (plausible process context, not an established core function). Do NOT
   REMOVE — it is a reasonable phylogenetic inference and the process is compatible with
   localization.
4. **GO:0000139 Golgi membrane** (IEA, GO_REF:0000044, from UniProt SubCell) — ACCEPT. This
   is the specific, experimentally-grounded localization; core.
5. **GO:0005829 cytosol** (IEA, GO_REF:0000108) — over-annotation. Derived by logical
   inference from the retrograde-transport BP term (with/from GO:0042147), not from any
   evidence PTM1 is a soluble cytosolic protein. PTM1 is a multi-pass integral membrane
   protein; the cytosolic C-tail does not make the protein "cytosol"-localized in the CC
   sense. MARK_AS_OVER_ANNOTATED.
6. **GO:0016020 membrane** (IEA, GO_REF:0000002, InterPro IPR009637) — ACCEPT (true,
   uninformative parent; keep as non-core). Redundant with the IBA membrane term but
   correctly reflects integral-membrane status.
7. **GO:0031901 early endosome membrane** (IEA, GO_REF:0000044, UniProt SubCell) — ACCEPT.
   Experimentally grounded (PMID:16107716 endosome/late-Golgi copurification). Non-core
   secondary localization.
8. **GO:0003674 molecular_function** (ND, GO_REF:0000015) — ACCEPT (root ND). Honestly
   reflects that no molecular function is known — appropriate for a dark gene. Keep.
9. **GO:0005575 cellular_component** (ND, GO_REF:0000015) — this ND root CC is now
   superseded by the specific Golgi/endosome CC annotations above. MARK_AS_OVER_ANNOTATED /
   effectively obsolete-by-newer-evidence; recommend it not be treated as core. (Per
   guidance, GOA ND roots are usually left; flag as non-core.)
10. **GO:0008150 biological_process** (ND, GO_REF:0000015) — root ND BP; superseded by the
    IBA retrograde-transport BP. Keep as-is / non-core; honest reflection of limited BP
    knowledge.

## Decisions on core_functions
- Core function statements must stay minimal and localization-grounded. The only defensible
  "core" is: **integral Golgi/endosome membrane protein of the GOST/LUSTR family, presumed
  to act in secretory-pathway membrane-protein trafficking; molecular function unknown.**
- Use CC terms for locations (Golgi membrane / early endosome membrane). Do NOT assert a
  specific MF (no ligand/channel/enzyme evidence). If a MF is required by schema, the honest
  choice is not to fabricate one; core_functions can describe the trafficking-context role
  with molecular_function left unstated or as the general integral-membrane framing.

## Deep research status
Falcon deep-research (`just deep-research-falcon yeast PTM1 --fallback perplexity-lite`) was
attempted twice and hung both times (~24 min with zero output on the first run; SIGTERM at the
500 s bound on the retry). No `-deep-research-falcon.md` file was produced, and none was
fabricated (per repo policy, self-written content must NOT be named `-deep-research-*`). This
review is therefore grounded directly in the UniProt record (P32857), the QuickGO GOA export,
the PANTHER PTHR21229 family data, and four cached primary/structural publications
(PMID:16107716, 18407956, 36373655, 39609618), all with verbatim-verified supporting text.

## Provenance of cached publications
- publications/PMID_16107716.md — Inadome 2005 (full text = abstract+Discussion only in cache).
- publications/PMID_18407956.md — Albuquerque 2008 phosphoproteome (abstract only).
- publications/PMID_36373655.md — Hoel 2022 TMEM87A structure (full text).
- publications/PMID_39609618.md — 2024 GPR180/GOST (full text).
- interpro/panther/PTHR21229/ — family metadata + reviewed members (subfamily assignments).
