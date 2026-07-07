# HLCS (holocarboxylase synthetase) — review notes

UniProtKB: P50747 (BPL1_HUMAN). HGNC:4976. Chromosome 21q22.13. 726 aa.
RecName: Biotin--protein ligase; AltName: Biotin apo-protein ligase; Holocarboxylase synthetase (HCS).

## Core biology (verified)

HLCS is the human **biotin--protein ligase (holocarboxylase synthetase)**: it covalently
attaches biotin to the biotin-dependent carboxylases, activating the apo-enzymes. It
catalyses a two-step reaction — biotin + ATP -> biotinyl-5'-AMP, then transfer of biotin
to a specific lysine on the biotin carboxyl carrier domain of each apocarboxylase.

Substrate carboxylases activated (UniProt CATALYTIC ACTIVITY, EC 6.3.4.9/.10/.11/.15;
[PMID:7753853], [PMID:10590022]):
- Pyruvate carboxylase (PC) — gluconeogenesis/anaplerosis (mitochondrial)
- Propionyl-CoA carboxylase (PCC; PCCA/PCCB) — odd-chain FA / propionate (mitochondrial)
- 3-Methylcrotonyl-CoA carboxylase (MCC; MCCC1/MCCC2) — leucine catabolism (mitochondrial)
- Acetyl-CoA carboxylases ACC1/ACC2 (ACACA cytosolic; ACACB mitochondrial outer membrane)

A **single HLCS** biotinylates carboxylases in **both cytosol and mitochondria**
([PMID:7753853] "a single HCS is targeted to the mitochondria and cytoplasm"). GOA carries
both cytoplasm (IBA) and mitochondrion (IEA-SubCell) plus cytosol (many IDA/TAS). All are
consistent with the dual-compartment biology.

Kinetics: KM = 224 nM for biotin ([PMID:10590022], via UniProt). Monomer ([PMID:7842009]).

## Disease

**Holocarboxylase synthetase deficiency** (HLCS deficiency; MIM 253270): neonatal/early-onset
**multiple carboxylase deficiency**, autosomal recessive. Loss of HLCS -> all 4/5 carboxylases
remain in inactive apo form -> ketoacidosis, lactic acidosis, hyperammonemia, organic aciduria,
dermatitis/alopecia, seizures. **Biotin-responsive** (10-20 mg/day). Extensive allelic series
of missense variants clustering in the biotin-binding region; some KM mutants, some non-KM
(e.g. R508W very common, biotin-responsive; L216R reduces protein half-life, [PMID:18429047]).
(Confirmed against ~/repos/dismech/kb/disorders/Holocarboxylase_Synthetase_Deficiency.yaml.)

## Moonlighting / non-core (histone biotinylation, chromatin)

A body of work (Zempleni, Gravel labs) reports HLCS in the nucleus, associated with chromatin
/ nuclear lamina / nuclear matrix, biotinylating histones (esp. K12-biotinyl H4) and thereby
implicated in gene silencing and biotin-uptake homeostasis at the SMVT locus ([PMID:14613969],
[PMID:17904341]). The physiological significance and even the existence of appreciable histone
biotinylation in vivo has been **disputed** in the broader literature (stoichiometry very low;
some argue it is a chemical/acetyl-CoA-carboxylase artifact). Treat chromatin/nuclear-lamina/
nuclear-matrix localizations and the "response to biotin" / histone-remodeling roles as
**non-core** (KEEP_AS_NON_CORE) — real experimental observations from a specific lab, but not
the established, disease-defining core function, and their in vivo relevance is contested.

## Annotation decisions summary

- GO:0004077 biotin--[biotin carboxyl-carrier protein] ligase activity — CORE MF. Many
  redundant lines (IBA, IEA, EXP, IDA x3, IMP, TAS x9). ACCEPT the well-supported experimental
  ones; ACCEPT IBA/IEA/TAS as consistent duplicates.
- ATP binding — not separately in GOA F list but implied (KW); reaction uses ATP. Add as
  supporting MF in core_functions (GO:0005524) — NOT adding a NEW existing_annotation since the
  KW-based F:ATP binding is a UniProt DR entry, not a GOA line.
- GO:0009374 biotin binding (IDA, PMID:14613969) — ACCEPT as supporting MF (substrate binding).
- GO:0006768 biotin metabolic process (IEA ARBA; TAS Reactome) — ACCEPT (broad but correct).
- GO:0043687 post-translational protein modification (IDA, PMID:14613969) — ACCEPT; this IS the
  biotinylation-as-PTM process. Best available BP (protein-biotinylation-specific terms
  GO:0009305/GO:0018054 are OBSOLETE).
- GO:0005737 cytoplasm (IBA, IEA), GO:0005829 cytosol (many IDA/TAS/HDA), GO:0005739
  mitochondrion (IEA) — ACCEPT (dual compartment, well supported).
- GO:0000785 chromatin, GO:0005652 nuclear lamina, GO:0016363 nuclear matrix (IDA, PMID:14613969),
  GO:0070781 response to biotin (IDA PMID:17904341; IEA) — KEEP_AS_NON_CORE (moonlighting; contested).
- GO:0005515 protein binding (IPI x several, high-throughput interactome screens PMID:21044950,
  28514442, 32296183, 33961781, plus 20085763) — MARK_AS_OVER_ANNOTATED (bare protein binding,
  uninformative; per curation policy do not REMOVE experimental IPIs).
- GO:0042802 identical protein binding (IEA Ensembl from rat ortholog) — but UniProt says HLCS is
  a MONOMER; homodimerization not supported for human. MARK_AS_OVER_ANNOTATED (IEA orthology transfer,
  contradicts monomer subunit).
- GO:0019899 enzyme binding (IPI, PMID:19157941, with PCCA/P05165) — this is substrate (apo-PCC)
  recognition, i.e. captures HLCS–substrate binding, more meaningful than bare protein binding but
  still generic; ACCEPT-adjacent -> KEEP as informative but replace-worthy. Mark MODIFY toward
  substrate-binding? enzyme binding is defensible (PCC is an enzyme). Keep as ACCEPT/non-core.

## Verified verbatim quotes (grep-confirmed against cached publications)

- PMID:7753853: "Holocarboxylase synthetase (HCS) catalyzes the biotinylation of the four biotin-dependent carboxylases in human cells."; "a single HCS is targeted to the mitochondria and cytoplasm"
- PMID:7842009: "Holocarboxylase synthetase (HCS) plays an essential role in biotin utilization in eukaryotic cells"
- PMID:9630604: "we have identified, in human placenta, three cytosolic HCS proteins, of 86, 82 and 76 kDa."
- PMID:14613969: "Nuclear HCS retains its biotinylating activity and was shown to biotinylate purified histones in vitro."; "fibroblasts from patients with HCS deficiency are severely deficient in histone biotinylation"
- PMID:17904341: "HCS acts as a biotin-histone ligase"
- PMID:18429047: "the turn-over rate for the mutant protein was double that of wildtype HLCS"
- PMID:19157941: "essential for biotinylation of carboxylases by HCS"; "N- and C-termini play roles in substrate recognition"; "catalyzes the binding of the vitamin biotin to"
- PMID:16780588: "the HLCS gene codes for a biotin-protein ligase and was found to localize throughout the cytosol"
