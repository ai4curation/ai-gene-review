# GM2A (Ganglioside GM2 activator protein) — review notes

UniProtKB: P17900 (SAP3_HUMAN). HGNC: GM2A. Chr 5. 193 aa precursor; signal 1-23, propeptide
24-31, mature chain 32-193. Non-enzymatic. Deep research (falcon) not available (provider out of
credits, HTTP 402); review grounded in UniProt record, seeded GOA, and cached publications.

## Core biology

GM2A is a small **lysosomal lipid-binding / lipid-transfer (sphingolipid activator) protein**, a
member of the ML (MD-2-related lipid recognition) / GM2-AP family with a novel beta-cup fold
(PDB 1G13, 1PU5, 1PUB, 1TJJ, 2AF9, 2AG2, 2AG4, 2AG9; PMID:11090283). It is **not an enzyme**.

Function (UniProt FUNCTION, ECO:0000269|PubMed:30988135, PubMed:8900233, PubMed:17552909):
"Lipid-binding and transfer protein essential for lysosomal degradation of ganglioside GM2.
Extracts single GM2 molecules from intralysosomal luminal vesicle (ILV) membranes and presents
them in soluble form to beta-hexosaminidase A (HEXA) for cleavage of N-acetyl-D-galactosamine and
conversion to GM3." Forms a stoichiometric GM2-GM2A complex that is the actual substrate for HEXA.
Also stimulates HEXA breakdown of glycolipid GA2 (by similarity). Large binding pocket can hold
several single-chain phospholipids and fatty acids; some Ca-independent phospholipase activity
(by similarity); participates in cholesterol transfer (PMID:17552909).

Activity regulation (PMID:30988135): inhibited by cholesterol, sphingomyelin, sphingosine,
sphinganine; stimulated by ceramide, diacylglycerol, fatty acids, lysophosphatidylcholine, and
anionic lipids such as BMP (bis(monoacylglycero)phosphate).

Subcellular location: Lysosome (ECO:0000305|PubMed:8900233). Acts at the intralysosomal luminal
vesicle / ILV membrane surface (curator IC to GO:0160317 endolysosomal intralumenal vesicle
membrane). Also detected in extracellular exosomes (proteomics: PMID:23533145, PMID:19056867) and
mapped by Reactome to extracellular region / azurophil granule lumen via neutrophil degranulation
(R-HSA-6798751) — secretory/exosomal presence, not the primary functional site.

Disease: GM2-gangliosidosis AB variant (GM2GAB, MIM:272750), autosomal recessive lysosomal storage
disease; GM2 accumulation in neurons despite normal HexA and HexB. Variants: Arg-138 (PMID:1915858),
Pro-169 (PMID:8244332), Lys-88 del (PMID:8900233).

## MF term choice for core_functions

GOA MF terms present:
- GO:0005319 lipid carrier activity (IBA + IEA) — current label confirmed via OLS (UniProt DR line
  says "lipid transporter activity" which is an older synonym; GOA/current ontology = lipid carrier
  activity).
- GO:7770043 lipid chaperone activity (IDA, PMID:11707436, PMID:30988135) — "Binding to a lipid and
  delivering it to an acceptor protein... The lipid may be presented while bound to the chaperone for
  enzymatic modification." This is the most precise, experimentally-supported MF for GM2A's
  extract-and-present mechanism. USED as the core MF.
- GO:0030290 sphingolipid activator protein activity (TAS, Reactome) — family-level activator term,
  accurate but less mechanistically precise than lipid chaperone activity.
- GO:0008047 enzyme activator activity (IEA/ARBA) — correct in spirit (activates HexA) but generic;
  keep as non-core.
- GO:0032428 beta-N-acetylgalactosaminidase activity (IEA/Ensembl, contributes_to) — this is HEXA's
  catalytic activity, NOT GM2A's. GM2A is non-catalytic; it presents substrate. Over-annotation from
  ortholog transfer. MARK_AS_OVER_ANNOTATED.
- GO:0016004 phospholipase activator activity (IEA/Ensembl) — weak "by similarity" phospholipase note;
  no evidence GM2A activates a phospholipase. Over-annotation from rodent ortholog transfer.

propagation_review for the REMOVE (GO:0009898): root_cause PROPAGATION_BAD, failure_mode
COMPARTMENT_OR_COMPLEX_MISMATCH (localization does not transfer to a signal-peptide-directed
lysosomal/secreted protein).

Core MF used: **GO:7770043 lipid chaperone activity**.
Core BP: **GO:0006689 ganglioside catabolic process** (IDA-supported, PMID:11707436, PMID:30988135).
Core CC: **GO:0043202 lysosomal lumen** (and lysosome GO:0005764).

## Annotation dispositions (summary)

- Lipid carrier activity (IBA, IEA): ACCEPT — correct MF, GM2A binds/delivers GM2.
- Lipid chaperone activity (IDA x2): ACCEPT — most precise MF, core.
- Sphingolipid activator protein activity (TAS Reactome): ACCEPT — family activator role.
- Enzyme activator activity (IEA): KEEP_AS_NON_CORE — generic parent of the activator role.
- ganglioside catabolic process (IBA, IEA x1, IDA x2): ACCEPT — core BP.
- glycosphingolipid catabolic process (IEA, TAS): ACCEPT — GM2A also assists GA2/GA1 breakdown.
- ganglioside metabolic process (IEA/Ensembl): KEEP_AS_NON_CORE — broader parent of catabolic.
- lipid transport (IBA, IEA): KEEP_AS_NON_CORE — mobilization/transfer is real but the biological
  role is substrate presentation in catabolism, not bulk transport.
- lysosome (IEA), lysosomal lumen (TAS x6): ACCEPT — primary site.
- endolysosomal intralumenal vesicle membrane (IC x2): ACCEPT — where it acts on ILVs.
- cytoplasmic side of plasma membrane (IBA, IEA): REMOVE — GM2A is a lumenal/secreted glycoprotein
  with a signal peptide; it has no cytosolic phase. Wrong-compartment IBA/ortholog transfer.
- basolateral / apical plasma membrane (IEA/Ensembl): KEEP_AS_NON_CORE — rodent ortholog transfer;
  possible surface/secretory pool but not the functional site.
- beta-N-acetylgalactosaminidase activity (IEA, contributes_to): MARK_AS_OVER_ANNOTATED — HEXA's
  catalytic activity, not GM2A's.
- phospholipase activator activity (IEA): MARK_AS_OVER_ANNOTATED — no evidence GM2A activates a
  phospholipase.
- protein binding (IPI x2, PMID:28514442, PMID:33961781; partner ACTA2/P62736): MARK_AS_OVER_ANNOTATED
  — high-throughput BioPlex AP-MS; uninformative "protein binding"; not GM2A's functional partner
  (HEXA). Per policy, do not REMOVE bare protein-binding IPIs.
- extracellular region (TAS Reactome): KEEP_AS_NON_CORE — via neutrophil degranulation; secretory.
- azurophil granule lumen (TAS Reactome): KEEP_AS_NON_CORE — neutrophil degranulation mapping.
- extracellular exosome (HDA x2, PMID:23533145, PMID:19056867): KEEP_AS_NON_CORE — proteomic
  detection in exosomes; not functional site.
