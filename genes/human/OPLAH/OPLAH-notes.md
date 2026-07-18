# OPLAH (5-oxoprolinase) — review notes

UniProt: O14841 (OPLA_HUMAN). Gene: OPLAH, HGNC:8149. Chromosome 8.

## Identity and reaction

OPLAH is **5-oxoprolinase**, EC 3.5.2.9 (aliases: 5-oxo-L-prolinase, 5-OPase, pyroglutamase).

- Catalytic reaction (UniProt, from ortholog Q75WB5 bovine):
  `5-oxo-L-proline + ATP + 2 H2O = L-glutamate + ADP + phosphate + H(+)`
  [file:human/OPLAH/OPLAH-uniprot.txt "Reaction=5-oxo-L-proline + ATP + 2 H2O = L-glutamate + ADP + phosphate"]
- FUNCTION: [file:human/OPLAH/OPLAH-uniprot.txt "Catalyzes the cleavage of 5-oxo-L-proline to form L-glutamate coupled to the hydrolysis of ATP to ADP and inorganic phosphate."]
- Rhea:RHEA:10348; EC=3.5.2.9 [file:human/OPLAH/OPLAH-uniprot.txt "Xref=Rhea:RHEA:10348"].

This is the ATP-dependent ring-opening step that closes the **γ-glutamyl cycle** of glutathione
turnover: it converts 5-oxo-L-proline (pyroglutamate), produced by γ-glutamylcyclotransferase
(GGCT) and CHAC enzymes, back to L-glutamate, regenerating glutamate for glutathione (GSH)
resynthesis.

## Domain architecture / family

- SIMILARITY: [file:human/OPLAH/OPLAH-uniprot.txt "Belongs to the oxoprolinase family."]
- 1288 aa, MW ~137 kDa. Multi-domain hydantoinase-A/B architecture (Pfam Hydantoinase_A/B,
  Hydant_A_N/C) — InterPro IPR002821 Hydantoinase_A, IPR003692 Hydantoinase_B, IPR045079
  Oxoprolinase-like, IPR008040 Hydant_A_N, IPR049517 ACX-like_C
  [file:human/OPLAH/OPLAH-uniprot.txt "InterPro; IPR045079; Oxoprolinase-like."].
- PANTHER PTHR11365:SF2 "5-OXOPROLINASE"
  [file:human/OPLAH/OPLAH-uniprot.txt "PANTHER; PTHR11365:SF2; 5-OXOPROLINASE; 1."].

## Subcellular location

- Cytoplasm, cytosol [file:human/OPLAH/OPLAH-uniprot.txt "SUBCELLULAR LOCATION: Cytoplasm, cytosol"].
- Identified by MS in central proteome (PMID:21269460) and liver (PMID:24275569). Tissue enhanced
  in testis; broadly expressed (Bgee: apex of heart + 140 other tissues)
  [file:human/OPLAH/OPLAH-uniprot.txt "HPA; ENSG00000178814; Tissue enhanced (testis)."].

## Quaternary structure / interactions

- SUBUNIT: Homodimer [file:human/OPLAH/OPLAH-uniprot.txt "SUBUNIT: Homodimer."].
- HuRI binary interactome (Y2H) reports OPLAH self-interaction plus POU6F2 and TPK1
  [file:human/OPLAH/OPLAH-uniprot.txt "O14841; O14841: OPLAH; NbExp=3"].
  Source: PMID:32296183 (A reference map of the human binary protein interactome, "HuRI").
  This is a high-throughput binary-interactome screen; the self-interaction is consistent with the
  documented homodimer, but POU6F2 (a POU-domain transcription factor) and TPK1 (thiamine
  pyrophosphokinase) have no established biological relationship to OPLAH's cytosolic 5-oxoprolinase
  function and are treated as non-core.

## Disease

- **5-oxoprolinase deficiency (OPLAHD)**, MIM:260005: calcium oxalate/carbonate urolithiasis and
  excessive urinary 5-oxo-L-proline; recurrent vomiting, diarrhea, abdominal pain
  [file:human/OPLAH/OPLAH-uniprot.txt "5-oxoprolinase deficiency (OPLAHD) [MIM:260005]"].
  First human OPLAH mutation reported by Almaghlouth et al. (PMID:21651516). Missense variants
  (S323R, V1089I) in Calpena et al. (PMID:23430506, JIMD Rep). Notably this OPLAH-deficiency form of
  5-oxoprolinuria is generally a **benign biochemical phenotype**, distinct from the severe
  glutathione-synthetase (GSS) deficiency form of pyroglutamic aciduria.

## Cardiac / oxidative-stress role (context, not GO-annotated here)

- Verheij / de Boer group: 5-oxoproline accumulation is a mediator of cardiac oxidative stress;
  OPLAH detoxifies it and is cardioprotective (PMID:29118264, Sci Transl Med 2017,
  "Accumulation of 5-oxoproline in myocardial dysfunction and the protective effects of OPLAH").
  Oplah-knockout mice show cardiac/renal fibrosis and elevated LV filling pressures resembling
  heart failure with preserved ejection fraction (HFpEF) (Cardiovasc Res 2018).
  These findings frame OPLAH's antioxidant relevance but are not present as GO annotations in the GOA
  file; they are recorded here as biological context only.

## GO term id checks (via OLS)

- GO:0017168 5-oxoprolinase (ATP-hydrolyzing) activity — MF, current, not obsolete.
- GO:0006749 glutathione metabolic process — BP, current.
- GO:0006751 glutathione catabolic process — BP, current.
- GO:0005524 ATP binding — MF, current (UniProt DR: GO:0005524 F:ATP binding IEA:UniProtKB-KW).
- GO:0005829 cytosol — CC, current.
- No dedicated GO "gamma-glutamyl cycle" or "5-oxoproline catabolic process" BP term exists;
  glutathione (catabolic) metabolic process are the appropriate BP terms.

## Annotation assessment summary

- Core MF: GO:0017168 (multiple independent lines: IBA, ISS from bovine Q75WB5, Reactome TAS, IEA
  from Rhea/EC). ATP binding (GO:0005524, KW-derived) is a supported accessory MF (not in GOA TSV as
  a separate row, but in UniProt DR; only added to core_functions, not existing_annotations).
- Core BP: glutathione metabolic/catabolic process (γ-glutamyl cycle; regenerates glutamate).
- Core CC: cytosol.
- Generic IEA MF parents (GO:0003824 catalytic activity, GO:0016787 hydrolase activity) are correct
  but uninformative → MARK_AS_OVER_ANNOTATED (root/near-root, superseded by GO:0017168).
- protein binding (GO:0005515) IPI and identical protein binding (GO:0042802) IPI from HuRI:
  GO:0042802 is consistent with the homodimer (KEEP_AS_NON_CORE); the two bare protein-binding
  (GO:0005515) rows to POU6F2/TPK1 are uninformative high-throughput hits → MARK_AS_OVER_ANNOTATED
  (never REMOVE an IPI per policy).
