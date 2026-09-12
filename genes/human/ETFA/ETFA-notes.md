# ETFA (human) review notes

UniProtKB:P13804 — Electron transfer flavoprotein subunit alpha, mitochondrial (Alpha-ETF).
HGNC:3481. Gene MIM 608053; disease MIM 231680 (Glutaric aciduria 2A). 333 aa precursor;
transit peptide 1..19; mature chain 20..333.

## Verified biology (from -uniprot.txt and cached publications)

- ETF is a soluble mitochondrial-matrix FAD-containing **heterodimer** of ETFA (alpha) +
  ETFB (beta), binding one FAD and one AMP per dimer
  [Reactome R-HSA-169260 "63kDa heterodimer composed of alpha and beta subunits and binds
  one FAD and one AMP per dimer"; PMID:8962055 "Mammalian electron transfer flavoproteins
  (ETF) are heterodimers containing a single equivalent of flavin adenine dinucleotide (FAD)"].
- Most of the FAD binds in the C-terminal (Domain II) portion of the alpha subunit
  [PMID:8962055 "most of the FAD molecule residing in the C-terminal portion of the alpha
  subunit"]. UniProt lists ~16 FAD BINDING residues on ETFA (223..319).
- ETF is the common electron acceptor for at least a dozen mitochondrial matrix FAD-dependent
  acyl-CoA dehydrogenases of fatty-acid beta-oxidation (ACADM/MCAD, ACADVL, etc.) and of
  amino-acid catabolism (IVD, GCDH), plus choline-pathway dehydrogenases (DMGDH, SARDH); it
  passes electrons to ETF-ubiquinone oxidoreductase (ETFDH / ETF-QO), funneling them to the
  respiratory-chain ubiquinone pool
  [PMID:25416781 full text "ETF acts as a mobile electron carrier that shuttles electrons
  between several FAD-containing dehydrogenases present in the mitochondrial matrix and the
  membrane-bound ETF:quinone oxidoreductase ... Altogether, there are 13 human dehydrogenases
  that interact with ETF ... it is the third major provider of electrons to the ubiquinone
  pool of the mitochondrial respiratory chain"].
- UniProt FUNCTION: "Heterodimeric electron transfer flavoprotein that accepts electrons from
  several mitochondrial dehydrogenases, including acyl-CoA dehydrogenases, glutaryl-CoA and
  sarcosine dehydrogenase ... transfers the electrons to the main mitochondrial respiratory
  chain via ETF-ubiquinone oxidoreductase (ETF dehydrogenase) ... Required for normal
  mitochondrial fatty acid oxidation and normal amino acid metabolism."
- SUBCELLULAR LOCATION: Mitochondrion matrix [PMID:3760196]. ETF resides on the matrix face
  of the inner membrane [Reactome].
- Deficiency (ETFA/ETFB/ETFDH) => multiple acyl-CoA dehydrogenase deficiency (MADD) /
  glutaric acidemia type II [MONDO:0009282; dismech MADD KB].

## Annotation decisions summary

Core (ACCEPT): GO:0009055 electron transfer activity (IDA/IBA/IEA); GO:0050660 FAD binding
(IDA/IBA/IEA); GO:0033539 fatty acid beta-oxidation using acyl-CoA dehydrogenase (IDA/IBA);
GO:0009063 amino acid catabolic process (IDA); GO:0022904 respiratory electron transport
chain (IDA); GO:0045251 electron transfer flavoprotein complex (IPI); GO:0005759
mitochondrial matrix (IDA/NAS/TAS). Mitochondrion terms (GO:0005739) KEEP_AS_NON_CORE or
ACCEPT (broader parent of matrix; HPA/HTP/HDA localization support).

protein binding (GO:0005515) IPIs: bare, uninformative. Most are high-throughput
interactome/CFTR proximity screens => MARK_AS_OVER_ANNOTATED (policy: not REMOVE). The
ETFRF1 (PMID:27499296) and MBTPS1 (PMID:35362222) interactions are functionally meaningful
(ETFRF1 promotes FAD dissociation; MBTPS1/S1P stabilizes the ETFA/ETFB heterodimer and
promotes FAD binding) but the GO term itself is still bare "protein binding" =>
MARK_AS_OVER_ANNOTATED with notes pointing to informative partners; better captured by
proposed complex/regulation terms rather than protein binding.

## Deep research
Falcon DR file did NOT arrive within the 8-min poll window (timed out, no file). Review is
grounded in UniProt (P13804), GOA, cached publications (PMID:8962055, 9334218, 10423253,
25416781, 3760196, 8504797, 3170610, 8617498, 27499296, 35362222, 34800366, 20833797),
Reactome R-HSA-169260/169270, and the dismech MADD KB.

## Final result
Validation clean (`just validate human ETFA` => Valid) on first run. 35 existing annotations
reviewed: 20 ACCEPT, 6 KEEP_AS_NON_CORE, 9 MARK_AS_OVER_ANNOTATED (all bare protein-binding
IPIs). 4 core_functions (electron transfer activity x3 contexts: respiratory ETC / fatty-acid
beta-ox / amino-acid catabolism; + FAD binding), all in mitochondrial matrix / ETF complex.
19 reference_review blocks added.
