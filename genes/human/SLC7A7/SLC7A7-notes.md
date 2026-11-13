# SLC7A7 (y+LAT1) review notes

UniProt: Q9UM01 (YLAT1_HUMAN). HGNC: SLC7A7. Chromosome 14q11.2. 511 aa, 12 TM helices.
Family: amino acid-polyamine-organocation (APC) superfamily, L-type amino acid transporter
(LAT) family, TC 2.A.3.8. PANTHER PTHR11785:SF303.

## Core biology (synthesized)

y+LAT1 is the **catalytic light subunit** of the heteromeric amino acid transporter (HAT)
that constitutes transport **system y+L**. It is **disulfide-linked to the heavy chain
SLC3A2 (4F2hc/CD98hc)**; the heavy chain is required for trafficking the light chain to the
plasma membrane. The light chain carries the substrate-translocation pathway.

System y+L is an **obligatory, electroneutral 1:1 antiporter (exchanger)**: it exports
intracellular **cationic amino acids** (arginine, lysine, ornithine) in a **Na+-independent**
manner, in exchange for extracellular **neutral amino acids** (leucine, glutamine) **plus
Na+**. The Na+-dependence is on the neutral-amino-acid arm only. In polarized epithelia
(kidney proximal tubule, small intestine) the transporter sits at the **basolateral
membrane**, where its physiological net role is **efflux of reabsorbed cationic amino acids
into the blood**. It is also the dominant y+L transporter in monocytes/macrophages (a
non-polarized, plasma-membrane location).

- Catalytic/exchange mechanism (UniProt CC:CATALYTIC ACTIVITY, Rhea):
  `L-leucine(out) + L-arginine(in) + Na(+)(out) = L-leucine(in) + L-arginine(out) + Na(+)(in)`
  (also L-lysine and L-ornithine as the (in) cationic substrate). [UniProtKB:Q9UM01 CC:CATALYTIC ACTIVITY]
- UniProt FUNCTION: "Heterodimer with SLC3A2, that functions as an antiporter which operates
  as an efflux route by exporting cationic amino acids from inside the cells in exchange with
  neutral amino acids plus sodium ions and may participate in nitric oxide synthesis via the
  transport of L-arginine" [UniProtKB:Q9UM01 CC:FUNCTION].
- Subunit: "Disulfide-linked heterodimer with the amino acid transport protein SLC3A2/4F2hc."
  [UniProtKB:Q9UM01 CC:SUBUNIT; ECO:0000269|PubMed:9829974, 9878049, 23940088].
- Location: "Basolateral cell membrane" [UniProtKB:Q9UM01 CC:SUBCELLULAR LOCATION; IDA PMID:15756301].

### Key primary evidence

- PMID:9829974 (Torrents 1998): identified human y+LAT-1 cDNA; induces system y+L transport
  with 4F2hc in oocytes; "y+LAT-1 protein forms a approximately 135-kDa, disulfide
  bond-dependent heterodimer with 4F2hc in oocytes". Candidate LPI gene (14q11.2). Expression
  kidney >> PBL >> lung > placenta. Variant LPI L334R. IDA for L-Leu transport, L-Arg
  transport; TAS for basic AA transport.
- PMID:9878049 (Pfeiffer 1999): y+LAT1/4F2hc heterodimers "form exchangers which mediate the
  cellular efflux of cationic amino acids and the Na+-dependent uptake of large neutral amino
  acids"; identified as y+L-type systems; "the basolateral amino acid exchanger involved in
  transepithelial reabsorption of cationic amino acids". IDA for L-Leu transport; kinetics
  (KM leucine 31.7 uM +NaCl). IPI/complex evidence with SLC3A2 (P08195).
- PMID:15756301 (Sperandeo 2005): basolateral membrane localization (IDA); mutant interferes
  with y+LAT2; "defective cationic amino acid (CAA) transport at the basolateral membrane of
  epithelial cells in the intestine and kidney".
- PMID:31705628 (Rotoli 2020, full text): y+LAT1 is the prevailing y+L transporter in
  monocyte-derived macrophages; "system y+L-mediated arginine transport is mainly accounted
  for by y+LAT1 in monocyte-derived macrophages (MDM)"; in polarized Caco-2 at basolateral
  side "it mediates arginine efflux in exchange with leucine plus sodium". KM(Arg) 0.182 mM.
- PMID:40355756 (SLC superfamily interactome): IntAct IPI with SLC3A2 (P08195) — the known
  heterodimer partner; supports the complex, not an independent informative MF.

### Disease (LPI) and the participation test

Loss-of-function mutations cause **lysinuric protein intolerance (LPI; MIM 222700)**: renal
CAA wasting, reduced intestinal CAA absorption, orotic aciduria, hyperammonaemia, failure to
thrive, hepatosplenomegaly, osteoporosis, pulmonary alveolar proteinosis, immune/haematologic
complications. Mechanistically these are **downstream of the transport defect** (low plasma
Arg/Lys → secondary urea-cycle dysfunction; impaired macrophage Arg supply → immune/pulmonary
phenotypes). y+LAT1 **performs transport**; it does not catalyse urea-cycle, nitric-oxide-
synthesis, or immune-effector steps. Per the participation test, **no NEW disease-process or
NO-synthesis process term is warranted** — the entity that performs those steps is a different
gene product (NOS, OTC/ASS1, etc.). The "may participate in NO synthesis via transport of
L-arginine" role (UniProt) is substrate-provision, not participation.

## Annotation decisions (summary)

MF:
- GO:0015174 basic amino acid transmembrane transporter activity (IBA, IEA): MODIFY ->
  GO:0180009 (broad specificity neutral L-amino acid:basic L-amino acid antiporter activity),
  an is_a descendant that captures the obligate y+L exchange mechanism. Confirmed via OLS that
  GO:0180009 is_a GO:0015174 (and is_a GO:0015175 neutral L-AA transporter, is_a GO:0015297
  antiporter).
- GO:0015179 L-amino acid transmembrane transporter activity (IBA): ACCEPT (correct genus;
  neutral + cationic L-amino acids; not an is_a ancestor of GO:0180009 so not redundant).
- GO:0061459 L-arginine transmembrane transporter activity (ISS from SLC7A6/Q92536): ACCEPT
  (arginine is the principal cationic substrate; measured KM in MDM).
- GO:0022857 transmembrane transporter activity (IEA InterPro): TOO_GENERAL (root MF entailed
  by the specific activities asserted here).
- GO:0005515 protein binding x2 (IPI, partner P08195=SLC3A2): REMOVE (bare protein binding,
  uninformative; the functional heterodimer is captured by GO:1902495 and core_functions
  in_complex) — protein-binding policy sanctioned REMOVE.

CC:
- GO:0005886 plasma membrane (IBA is_active_in; TAS x4): ACCEPT (catalytic location; plasma
  membrane in non-polarized cells such as monocytes).
- GO:0016323 basolateral plasma membrane (IDA PMID:15756301; IEA SubCell): ACCEPT (core
  epithelial location).
- GO:0016020 membrane (IEA InterPro): MODIFY -> GO:0005886 plasma membrane (descendant;
  localization is established).
- GO:1902495 transmembrane transporter complex (IPI ComplexPortal, part_of; CPX-8187): ACCEPT
  (the y+LAT1-4F2 heteromeric complex with SLC3A2).

BP:
- GO:0003333 amino acid transmembrane transport (IBA): ACCEPT (overall process, well-placed).
- GO:1990822 basic amino acid transmembrane transport (TAS): ACCEPT (core).
- GO:1903826 L-arginine transmembrane transport (IDA, IEA): ACCEPT (core, measured).
- GO:0015820 L-leucine transport (IDA x2, IEA): ACCEPT (the exchanged neutral substrate, measured).
- GO:0089718 amino acid import across plasma membrane (IDA ComplexPortal, IEA): ACCEPT (the
  neutral-AA/Na influx arm of the obligate exchange; net physiological role is cationic efflux).
- GO:0055085 transmembrane transport (IEA InterPro): TOO_GENERAL (root process).

IBA phylogenetic reading: the IBA MF/CC/BP rows sit on PANTHER PTHR11785 nodes
(PTN000208507, PTN002623481) that gather the LAT-family light chains; y+LAT1 is squarely
within the clade (own experimental grounding present, so its appearance in WITH/FROM is
expected, not circular). No lineage-specific loss. No cross-subfamily over-propagation found
that would require REMOVE.
</content>
