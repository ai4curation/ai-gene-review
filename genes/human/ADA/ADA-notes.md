# ADA (human) — curation notes

UniProtKB:P00813 (ADA_HUMAN). 363 aa. EC 3.5.4.4. HGNC:186. Chr 20.

Deep research (falcon) was polled up to the time budget and was NOT present, so this
review is grounded in the UniProt record, the seeded GOA, and the 18 cached
`publications/PMID_*.md` entries (all 18 cited PMIDs are cached; only 3 have full text).

## Core biology
- Zinc metalloenzyme (metallo-dependent hydrolase superfamily; adenosine/AMP deaminase
  family). Catalyzes hydrolytic deamination:
  - adenosine + H2O + H+ -> inosine + NH4+ (RHEA:24408)
  - 2'-deoxyadenosine + H2O + H+ -> 2'-deoxyinosine + NH4+ (RHEA:28190)
  - also deaminates cordycepin (3'-deoxyadenosine) and the drug ribavirin (Reactome:R-HSA-9754964).
  [file:P00813 UniProt "Catalyzes the hydrolytic deamination of adenosine and 2-deoxyadenosine"]
- Binds 1 catalytic Zn2+ per subunit (His15, His17, His214, Asp295; active-site His217 proton donor).
  [file:P00813 UniProt "Binds 1 zinc ion per subunit"]
- Central to purine catabolism / adenosine homeostasis. Loss causes toxic accumulation of
  (deoxy)adenosine and dATP; disease = ADA-SCID (T-B-NK- SCID), OMIM 102700.
  [PMID:9361033 "directly with the accumulation of the toxic metabolites deoxyATP and deoxyadenosine"]

## Localization
- Predominantly cytosolic. Also lysosomal (~10% of activity in fibroblast lysosomes)
  [PMID:8452534 "adenosine deaminase (ADA) activity that accounts for approximately 10% of the total ADA activity"].
- Ecto-ADA: a genuine second localization/role at the cell surface, tethered by CD26/DPP4
  (peripheral membrane, extracellular side). Ecto-ADA/CD26 catabolizes extracellular adenosine
  (endothelium under hypoxia), acts as a T-cell costimulatory molecule, and regulates
  lymphocyte-epithelial adhesion. Keep these as NON-CORE (moonlighting/second site).
  [PMID:16670267], [PMID:8101391], [PMID:7594462], [PMID:11772392].

## Annotation decisions (summary)
- CORE (ACCEPT): GO:0004000 adenosine deaminase activity (IBA/IEA/ISS/IMP/IDA duplicates);
  GO:0046936 2'-deoxyadenosine deaminase activity; GO:0008270 zinc ion binding;
  GO:0006154 adenosine catabolic process; GO:0005829 cytosol; GO:0019239 deaminase activity
  (parent MF — ACCEPT, broader ok).
- NON-CORE (KEEP_AS_NON_CORE): ecto-ADA / CD26 axis and its downstream (T cell activation,
  cell surface, external side of plasma membrane, cell-cell adhesion via integrin, negative
  regulation of adenosine receptor signaling, response to hypoxia), lysosome, sleep regulation,
  ribavirin/xenobiotic metabolism.
- OVER-ANNOTATED: bare protein binding IPIs (POTEF and DPP4 IPIs -> MARK_AS_OVER_ANNOTATED,
  not REMOVE, per policy). High-throughput interactome IPIs (POTEF, A5A3E0) are not informative MF.
- REMOVE candidates (IEA over-propagations): GO:0009168 purine ribonucleoside monophosphate
  biosynthetic process (InterPro2GO; ADA is catabolic, not a monophosphate biosynthesis enzyme);
  GO:0032263 GMP salvage and GO:0044209 AMP salvage / GO:0006196 AMP catabolic /
  GO:0046059 dAMP catabolic (Ensembl-Compara ortholog transfers describing downstream pathway
  steps ADA itself does not carry out); GO:0070161 anchoring junction and GO:0060205 cytoplasmic
  vesicle lumen (SubCell keyword IEAs, weakly supported). These are electronic inferences argued
  against on biological grounds.
- The plasma-membrane / lysosome IEA CC terms are electronic but corroborated by IDA (keep).

## Sleep (GO:0045187)
IBA-only; ADA*2 (D8N) polymorphism modulates deep sleep [UniProt POLYMORPHISM; PMID:16221767,
not cited in GOA]. Real but non-core; KEEP_AS_NON_CORE.
</content>
</invoke>
