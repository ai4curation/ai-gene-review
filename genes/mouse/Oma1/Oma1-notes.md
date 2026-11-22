# Oma1 (mouse, Q9D8H7) curation notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Context: mouse Oma1 is the experimentally characterised 1:1 ortholog of human OMA1
(Q96E52); both sit in PANTHER subfamily PTHR22726:SF1 (METALLOENDOPEPTIDASE OMA1,
MITOCHONDRIAL), per the UniProt `DR PANTHER` lines of each record, and both descend
from the PAINT nodes PTN000506393 (metalloendopeptidase activity) and PTN000506394
(mitochondrial inner membrane; protein quality control), as shown in the WITH/FROM
of the IBA rows. Yeast Oma1 (P36163, SGD:S000001795) is the founding member
[PMID:12963738 "we describe the identification of a novel conserved metallopeptidase
that exerts activities overlapping with the m-AAA protease and was therefore termed
Oma1"]. No ProtNLM2 output was consulted.

### Deep research

`just deep-research-falcon mouse Oma1 --fallback perplexity-lite` failed: falcon
raised "Failed to authenticate" (Edison auth) and the perplexity fallback returned
HTTP 401 insufficient_quota. No deep-research file exists; the review is built from
the cached primary literature listed below and the curated UniProt record.

### Literature read (publications/ cache)

- PMID:20038678 (Ehses 2009, full text). MEFs. OMA1-GFP localises to mitochondria
  ["OMA1-GFP was exclusively localized to mitochondria and not detected in the ER
  membrane"]. RNAi of Oma1 stabilises L-OPA1 in AFG3L1/2-deficient MEFs and after
  CCCP/oligomycin ["these experiments identify OMA1 as the protease responsible for
  the inducible cleavage of OPA1 at processing site S1"]. OMA1 depletion restores
  tubular mitochondria and lamellar cristae in AFG3L1/2-deficient MEFs, i.e. the
  OMA1 activity is what destroys fusion/cristae when m-AAA is absent (epistasis).
- PMID:22433842 (Quiros 2012, abstract only). Oma1 KO mice: L-OPA1 inactivation
  requires OMA1 in vivo; KO mice are obese, have hepatic steatosis, lower energy
  expenditure and impaired thermogenesis, altered lipid/glucose gene expression.
  These are organismal phenotypes downstream of OPA1 processing.
- PMID:24550258 (Baker 2014, abstract only). OMA1 is constitutively active but is
  strongly activated by stress; N-terminal stress-sensor region present only in
  higher eukaryotes; activation is coupled to autocatalytic degradation from both
  termini.
- PMID:24719224 (Zhang 2014, abstract only). Depolarisation triggers self-cleavage
  to S-OMA1; UniProt places the C-terminal autocleavage at mouse residues 443-452 and
  E324Q (HExxH glutamate) abolishes both protease activity and autocleavage.
- PMID:24616225 (Anand 2014, full text). Oma1-/- and Yme1l-/-Oma1-/- MEFs: S1
  products (forms c, e) absent in Oma1-/- cells; OPA1 processing is dispensable for
  fusion; stress-induced OMA1 cleavage inhibits fusion.
- PMID:26365306 (Bohovych 2015, full text). Oma1-/- MEFs fail to reach maximal
  respiration; yeast oma1 mutant destabilises respiratory supercomplexes, rescued by
  WT but not catalytic-dead Oma1; Oma1 is not a stoichiometric supercomplex
  component. Requirement, not participation in assembly.
- PMID:26783299 (Korwitz 2016, full text). Oma1 ablation delays neurodegeneration
  in prohibitin-deficient neurons; stress-induced OPA1 processing by OMA1 promotes
  neuronal death.
- PMID:33200421 (Murata 2020, abstract only). Drp1-KO cells: membrane-potential
  flickering activates Oma1, which cleaves Opa1 and limits extreme fusion.
- PMID:37816711 (Qiu 2023, full text). FAM210A/YME1L in BAT; recombinant OMA1
  cleaves OPA1 in a cell-free assay; FAM210A promotes YME1L-mediated OMA1
  degradation. Does not show OMA1 participating in inner-membrane fusion.
- PMID:18614015 (Pagliarini 2008): mitochondrial proteomics compendium (HDA).
- PMID:26785494, PMID:29593106, PMID:31819158 (abstract only): heart-failure and
  prohibitin/cardiolipin context; cached for completeness.

### Experimentally established in mouse vs inferred

Established in mouse (or mouse cells): metalloendopeptidase activity (E324Q;
KO MEFs lose S1 cleavage of OPA1; recombinant cleavage), OPA1 S1 processing,
stress-induced inhibition of mitochondrial fusion, self-cleavage/autoprocessing,
mitochondrial/inner-membrane location, organismal KO phenotypes (thermogenesis,
obesity, cardioprotection, delayed neurodegeneration).

Inferred from human by orthology (same SF1 subfamily, 1:1 ortholog; DELE1 ortholog
Q9DCV6 exists in mouse): DELE1 cleavage, HRI-mediated signalling/ISR, BAX/BAK-
triggered cristae remodelling and apoptosis priming. Several ISO rows from human
(mitophagy, positive regulation of mitophagy, translational initiation, protein
localization to mitochondrion) could not be traced to a human source row in a
QuickGO query of Q96E52 on 2026-10-20; judged on biology.

### Decisions

- Downstream metabolic/thermogenic IMP terms: MARK_AS_OVER_ANNOTATED (organismal
  phenotypes; OMA1 performs no step of thermogenesis or lipid/glucose metabolism).
- mitochondrion organization / cristae formation IGI (acts upstream): MODIFY to the
  regulatory terms the gene already carries (negative regulation of mitochondrial
  fusion; regulation of cristae formation).
- mitochondrial inner membrane fusion IDA: MARK_AS_OVER_ANNOTATED, OMA1 cleavage is
  not required for fusion (PMID:24616225) and its stress-induced cleavage inhibits it.
- Respiratory chain complex assembly IMP: MARK_AS_OVER_ANNOTATED (requirement only).
- IBA rows (PTN000506393/4): accepted; mouse is inside the clade and has its own
  experimental grounding.
