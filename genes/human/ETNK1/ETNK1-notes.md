# ETNK1 (Ethanolamine kinase 1) — review notes

UniProt: Q9HBU6 (EKI1_HUMAN). HGNC:24649. EC 2.7.1.82. Gene on chromosome 12.
452 aa, MW ~51 kDa. Choline/ethanolamine kinase family.

## Core biology (grounded in UniProt Q9HBU6)

- **Molecular function — ethanolamine kinase.** Catalyzes the first committed step of
  the CDP-ethanolamine (Kennedy) pathway: phosphorylation of ethanolamine by ATP.
  Reaction from UniProt CATALYTIC ACTIVITY:
  `ethanolamine + ATP = phosphoethanolamine + ADP + H(+)` (Rhea:RHEA:13069, EC 2.7.1.82),
  evidence ECO:0000269|PubMed:11044454 [file:human/ETNK1/ETNK1-uniprot.txt].
- **Substrate specificity.** UniProt FUNCTION: "Highly specific for ethanolamine
  phosphorylation. May be a rate-controlling step in phosphatidylethanolamine biosynthesis"
  [file:human/ETNK1/ETNK1-uniprot.txt]. The primary paper shows EKI1 "has negligible
  choline kinase activity in vitro and does not influence phosphatidylcholine biosynthesis"
  and that "The data demonstrate the existence of separate ethanolamine and choline kinases
  in mammals" [PMID:11044454 "EKI1 has negligible choline kinase activity in vitro and does
  not influence phosphatidylcholine biosynthesis"]. This distinguishes ETNK1 from the
  choline kinases CHKA/CHKB.
- **ATP binding.** Uses ATP as phosphate donor (KW ATP-binding; GO:0005524 ATP binding
  IEA:UniProtKB-KW) [file:human/ETNK1/ETNK1-uniprot.txt].
- **Pathway.** UniProt PATHWAY: "Phospholipid metabolism; phosphatidylethanolamine
  biosynthesis; phosphatidylethanolamine from ethanolamine: step 1/3"
  (UniPathway UPA00558, UER00741) [file:human/ETNK1/ETNK1-uniprot.txt]. Functional
  demonstration: "EKI1 overexpression in COS-7 cells results in a 170-fold increase in
  ethanolamine kinase-specific activity and accelerates the rate of [3H]ethanolamine
  incorporation into PtdEtn" [PMID:11044454].
- **Subcellular location.** UniProt SUBCELLULAR LOCATION: "Cytoplasm
  {ECO:0000305|PubMed:11044454}" [file:human/ETNK1/ETNK1-uniprot.txt]. GOA carries an
  IDA cytoplasm annotation (is_active_in) from PMID:11044454 and a TAS cytosol annotation
  from Reactome. Reactome R-HSA-1483222: "In the cytosol, ethanolamine (ETA) is
  phosphorylated to phosphoethanolamine (PETA) ... by ethanolamine kinase 1/2 (ETNK1/2)"
  [file:reactome/R-HSA-1483222.md].
- **Tissue specificity.** UniProt: "Expressed in kidney, liver, placenta, heart, leukocyte,
  ovary and testis" [file:human/ETNK1/ETNK1-uniprot.txt].

## Disease / physiological context (context only; not a GO supporting_text)

- Recurrent somatic ETNK1 mutations occur in atypical chronic myeloid leukemia (aCML) and
  other myeloid neoplasms (e.g. systemic mastocytosis with associated myeloid neoplasm).
  PubMed returns a well-populated body of literature linking ETNK1 mutations to aCML
  (PubMed MCP search "ETNK1 mutations atypical chronic myeloid leukemia", 16 hits, e.g.
  PMID:40288921, PMID:38644693). Mutations cluster in the kinase domain, reduce
  ethanolamine kinase activity, lower phosphoethanolamine, and increase mitochondrial ROS.
  This is not encoded in the current GOA set and is left for the disease/notes context.

## Annotation-by-annotation reasoning

Thirteen seeded GOA annotations, three GO terms repeated across evidence tiers:

- **GO:0004305 ethanolamine kinase activity** — MF; core. IDA (PMID:11044454) is the gold
  standard and is directly supported by the primary characterization. IBA (GO_REF:0000033,
  PAN-GO) and IEA (GO_REF:0000120, from RHEA:13069|EC:2.7.1.82) redundantly recapitulate
  the same well-supported activity. ACCEPT the IDA as core; ACCEPT the IBA and IEA as
  consistent redundant support.
- **GO:0006646 phosphatidylethanolamine biosynthetic process** — BP; core. IDA
  (PMID:11044454) directly supported by the 170-fold acceleration of the CDP-ethanolamine
  pathway. IBA and IEA (UniPathway UPA00558) redundantly support the same. ACCEPT.
- **GO:0005737 cytoplasm** — CC. IDA (PMID:11044454, is_active_in) is the primary
  subcellular-location evidence and matches UniProt SUBCELLULAR LOCATION. IBA (is_active_in)
  and IEA (GO_REF:0000044, SubCell SL-0086) redundantly support cytoplasm. ACCEPT; the more
  granular cytosol (GO:0005829, Reactome TAS) is the better term but both are compatible.
- **GO:0005829 cytosol** — CC; TAS from Reactome R-HSA-1483222. Consistent with a soluble
  cytosolic enzyme; the CDP-ethanolamine pathway kinase step is cytosolic. ACCEPT.
- **GO:0016020 membrane** — CC; HDA from PMID:19946888 ("Defining the membrane proteome of
  NK cells"). This is a large-scale membrane-proteome pulldown from the NK-like cell line
  YTS; the paper itself notes that a large fraction of identified species were "largely
  involved in cellular processes and molecular functions that could be predicted to be
  transiently associated with membranes" [PMID:19946888]. ETNK1 is a soluble cytosolic
  enzyme with no TM domain (UniProt has no TRANSMEM feature); the CDP-ethanolamine pathway
  operates near the ER but ETNK1 itself is cytosolic. Treat as MARK_AS_OVER_ANNOTATED
  (co-purification with membranes, not a bona fide membrane location).
- **GO:0005515 protein binding** ×2 (IPI, PMID:25416956 and PMID:32296183) — MF but
  uninformative bare "protein binding". Both are high-throughput binary interactome maps
  (Rolland 2014; Luck 2020). The recorded interactors (UBQLN1 Q9UMX0, SGTA O43765, CAMLG
  P49069, SLC51B Q86UW2, SGTB Q96EQ0, UBQLN2 Q9UHD9) all appear in the UniProt INTERACTION
  block [file:human/ETNK1/ETNK1-uniprot.txt], so the interactions are corroborated. Several
  partners (SGTA/SGTB co-chaperones, UBQLN1/UBQLN2 ubiquilins, CAMLG) are
  chaperone/quality-control proteins — consistent with generic handling rather than a
  specific ETNK1 catalytic-complex partner. Per policy do NOT REMOVE an IPI protein-binding
  annotation; MARK_AS_OVER_ANNOTATED (uninformative term). Do not put "protein binding" in
  core_functions.

## Core functions (final)

- MF: ethanolamine kinase activity (GO:0004305)
- MF: ATP binding (GO:0005524) — supporting/contributes
- BP: phosphatidylethanolamine biosynthetic process (GO:0006646)
- CC: cytosol (GO:0005829)
