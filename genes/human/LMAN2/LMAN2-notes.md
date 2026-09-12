# LMAN2 (VIP36) — Gene Review Notes

UniProt: Q12907 (LMAN2_HUMAN). Gene symbol: LMAN2 (HGNC:16986), synonym C5orf8.
Protein name: Vesicular integral-membrane protein VIP36 (also Glycoprotein GP36b, Lectin
mannose-binding 2). 356 aa precursor; signal peptide 1-44; mature chain 45-356; single-pass
type I membrane protein (lumenal 45-322, TM 323-345, cytoplasmic 346-356).

## What VIP36 is

VIP36/LMAN2 is a type I transmembrane **leguminous-type (L-type) lectin** of the early
secretory pathway. Its lumenal L-type lectin-like domain (52-276) binds carbohydrate in a
Ca2+-dependent manner [file:human/LMAN2/LMAN2-uniprot.txt "L-type lectin-like"; UniProt COFACTOR
"Binds 2 calcium ions per subunit"]. UniProt FUNCTION: "Plays a role as an intracellular lectin
in the early secretory pathway. Interacts with N-acetyl-D-galactosamine and high-mannose type
glycans and may also bind to O-linked glycans. Involved in the transport and sorting of
glycoproteins carrying high mannose-type glycans" [file:human/LMAN2/LMAN2-uniprot.txt].

It is a member of the same L-type lectin family as LMAN1/ERGIC-53 (P49257; PANTHER
PTN000259611). It is NOT a glycosidase / mannosidase — it has no catalytic activity; it is a
carbohydrate-binding cargo/sorting receptor. The CDD/InterPro signatures are lectin signatures
(cd06901 lectin_VIP36_VIPL; IPR035664 VIP36_lectin; PF03388 Lectin_leg-like).

## Localization (core CC = ERGIC/Golgi/ER membrane of the early secretory pathway)

UniProt SUBCELLULAR LOCATION (from PubMed:10444376, Fullekrug et al. "VIP36 localisation to the
early secretory pathway"): "Endoplasmic reticulum-Golgi intermediate compartment membrane ...
Golgi apparatus membrane ... Endoplasmic reticulum membrane" [file:human/LMAN2/LMAN2-uniprot.txt].
It cycles early in the secretory pathway between ER/ERGIC and Golgi.

- ERGIC IDA: [PMID:20477988 "The VIP36/alpha1-AT complex localized to Golgi and endoplasmic
  reticulum (ER)"] and the localization of VIP36 to Golgi/ER cycling.
- ERGIC IDA: [PMID:15308636] ERGIC membrane proteomics from BFA-treated HepG2 cells —
  "purification of ERGIC membranes ... enriched 110-fold over the homogenate for ERGIC-53";
  VIP36 was among the cycling/cargo-receptor proteins in this ERGIC-enriched fraction.
- Golgi apparatus IDA: HPA immunofluorescence (GO_REF:0000052) and [PMID:20477988
  "VIP36 localizes to the Golgi apparatus and cycles early in the secretory pathway"].

## Carbohydrate / D-mannose binding (core MF)

- In vitro VIP36 binds high-mannose glycans with a pH optimum ~6.5: [PMID:20477988 "In vitro,
  VIP36 binds high-mannose glycans with a pH optimum of 6.5, a value similar to the luminal pH
  of the Golgi apparatus"].
- In the living cell VIP36 bound exclusively the high-mannose form of its cargo: [PMID:20477988
  "In the living cell, VIP36 bound exclusively to the high-mannose form of alpha1-AT. The binding
  was increased when complex glycosylation was prevented by kifunensine and abolished when the
  glycosylation sites of alpha1-AT were inactivated by mutagenesis"]. This is the basis for the
  D-mannose binding IMP.
- Quantitative lectin-glycan binding (carbohydrate binding IDA): [PMID:23701871 "Estimated Ka
  values of malectin and VIP36 were in good agreement indeed with those evaluated by conventional
  methods such as isothermal titration calorimetry (ITC) or frontal affinity chromatography
  (FAC)"] using "fluorescently labeled high-mannose-type glycans and recombinant intracellular
  lectins."

## Transport / sorting / quality control (core BP)

VIP36 functions in post-ER quality control and ER<->Golgi cycling of high-mannose glycoproteins:
- Silencing VIP36 accelerated cargo transport, arguing against a pure anterograde role and
  consistent with a quality-control / retrograde recycling role: [PMID:20477988 "Silencing VIP36
  accelerated alpha1-AT transport, arguing against a role of VIP36 in anterograde traffic"].
- Retrograde Golgi-to-ER recycling (basis for GO:0006890 IMP): [PMID:20477988 "The complex
  formed by VIP36 and alpha1-AT in the Golgi recycled back to the ER. The combined data are most
  consistent with a function of VIP36 in post-ER quality control of alpha1-AT"].
- VIP36 is "postulated as a cargo receptor for Golgi-to-endoplasmic reticulum transport"
  [PMID:22016386].
- Reactome: COPII-mediated vesicle transport (R-HSA-204005); Cargo concentration in the ER
  (R-HSA-5694530); consistent with COPII vesicle (GO:0030134) and ER-to-Golgi transport
  (GO:0006888) IBA annotations.

## Interactions

- alpha1-antitrypsin (SERPINA1, P01009) is a glycoprotein cargo identified by YFP-fragment
  complementation: source of the protein binding IPI (WITH P01009). [PMID:20477988 "we identified
  the glycoprotein alpha1-antitrypsin (alpha1-AT) as a cargo of VIP36"]. This is a lectin-cargo
  (sugar-dependent) interaction; the bare "protein binding" GO term is uninformative and the real
  informative MF is the mannose/carbohydrate binding.
- heat shock protein binding IPI (GO:0031072), WITH UniProtKB:P11021 (BiP / HSPA5 / GRP78):
  recorded by UniProt from PMID:20477988. P11021 is the ER chaperone BiP. This is a specific,
  more-informative interaction than bare protein binding but is not the defining sorting
  mechanism; kept non-core. (The cached PMID:20477988 entry is abstract-only — full_text_available:
  false — so the BiP interaction detail is in the full text seen by the curator, not the abstract.)

## Secondary / cell-surface role (ectodomain shedding, macrophages)

A minor pool of Endo-H-resistant (late-Golgi / cell-surface) VIP36 reaches the plasma membrane
and is shed; the shed/cell-surface VIP36 regulates phagocytosis in macrophages:
- [PMID:22016386 "the shedding of VIP36 occurs mainly on the cell surface"]
- [PMID:22016386 "VIP36 significantly accumulates on the cell surface upon inhibition of shedding"]
- [PMID:22016386 "the amount of VIP36 precisely regulates phagocytosis in macrophages and that
  the shedding of VIP36 is required for this regulation"]
This is the basis for the extracellular region / plasma membrane / cell surface IDA and the
positive regulation of phagocytosis IMP/IEA. These are genuine but secondary to the core
ER-Golgi lectin/sorting function, which dominates the protein's biology. Notably the lectin
activity is dispensable for phagocytosis enhancement [PMID:22016386 "the lectin activity is
dispensable for the enhancement of phagocytosis"], underscoring that this is a separate moonlighting
role rather than the core function.

## Proteomics-only localizations (non-core / over-annotation)

- extracellular exosome (GO:0070062) HDA from urinary/prostatic exosome shotgun proteomics
  [PMID:23533145; PMID:19056867] — large-scale proteomic catalogs (~900-1132 proteins), no
  VIP36-specific functional claim; reflects presence in secreted vesicles, not core residence.
- membrane (GO:0016020) IEA (InterPro IPR005052) — bare "membrane" is uninformative; the protein
  is specifically an ER/ERGIC/Golgi single-pass membrane protein.

## Cofactor / metal

Lectin domain binds 2 Ca2+ per subunit as a structural cofactor required for carbohydrate
binding [file:human/LMAN2/LMAN2-uniprot.txt COFACTOR "Binds 2 calcium ions per subunit"]; multiple
Ca2+-binding residues (162, 164, 166, 193). UniProt keyword "Metal-binding" / GO:0046872 metal ion
binding (IEA) is a structural attribute, not the core function. (No metal/calcium binding row is
present in the GOA TSV stub, so no annotation is reviewed for it.)

## Summary of review decisions

- Core MF: D-mannose binding (GO:0005537), carbohydrate binding (GO:0030246) — ACCEPT.
- Core CC: ERGIC (GO:0005793), ERGIC membrane (GO:0033116), Golgi membrane (GO:0000139),
  Golgi apparatus (GO:0005794), ER membrane (GO:0005789), COPII vesicle (GO:0030134) — ACCEPT.
- Core BP: ER-to-Golgi vesicle-mediated transport (GO:0006888), retrograde Golgi-to-ER transport
  (GO:0006890) — ACCEPT.
- heat shock protein binding (GO:0031072), protein binding (GO:0005515) — KEEP_AS_NON_CORE.
- positive regulation of phagocytosis (GO:0050766, IMP + IEA) — KEEP_AS_NON_CORE (secondary
  macrophage role); IEA ortholog one MARK_AS_OVER_ANNOTATED.
- extracellular region/plasma membrane/cell surface (22016386 IDA) — KEEP_AS_NON_CORE (shedding).
- extracellular exosome (HDA), membrane (IEA) — MARK_AS_OVER_ANNOTATED.

## Falcon deep-research findings (incorporated 2026-06)

- Specific ectodomain-shedding cleavage site (mechanism for the existing cell-surface/shedding role):
  quantitative protein terminomics maps VIP36/LMAN2 as a metalloprotease-regulated shedding substrate
  cleaved at **F298 down-arrow L299 (SVNF/LKSP)**, reproducible across multiple cell lines and
  suppressed by the broad-spectrum metalloprotease inhibitor BB-94 [PMID:33796845 (Tsumagari et al.,
  iScience 2021) "Exploring the landscape of ectodomain shedding by quantitative protein terminomics";
  DOI 10.1016/j.isci.2021.102476]. This refines the mechanistic basis of the previously curated
  cell-surface/plasma-membrane/extracellular-region IDA and the shedding-dependent phagocytosis role
  (PMID:22016386). Added as MEDIUM-relevance reference; no annotation change (shedding already
  KEEP_AS_NON_CORE).
- Glycan-binding specificity detail (Falcon synthesis of prior reviews; consistent with existing
  D-mannose/carbohydrate binding annotations): VIP36 prefers high-mannose Man7-9GlcNAc2 with strongest
  recognition of the D1/A-arm Man-alpha-1,2-Man-alpha-1,2-Man motif; binding is pH-sensitive (optimum
  ~pH 6.0-6.5, matching early-Golgi/ERGIC lumen) and structurally Ca2+-assisted (residues Asp131,
  Asn166, His190 contact ligand). Reinforces the existing core MF; reviews (Gupta 2012, Yamamoto 2014,
  Reiterer 2010 thesis) are not PubMed-cached primary sources — notes-only, not added to YAML.
- Disease/association context (Falcon; non-causal, not gene function): 2024 plasma-proteome PWAS
  (Xiong et al., Heliyon) associates LMAN2 with CKD-related traits (BUN/eGFR), but colocalization
  PP4 < 0.01 does NOT support a shared causal cis-variant, so LMAN2 is at best an associated marker;
  2023 granulosa-cell proteomics (Eubler et al.) reports LMAN2 as differentially abundant under
  cannabidiol. Both are association/proteomics only and do not inform VIP36 molecular function;
  notes-only, not added to YAML.
</content>
</invoke>
