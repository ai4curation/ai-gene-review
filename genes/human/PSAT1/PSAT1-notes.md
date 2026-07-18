# PSAT1 review notes

UniProt: Q9Y617 (SERC_HUMAN), gene PSAT1 (HGNC:19129), synonym PSA. 370 aa, chromosome 9.
EC 2.6.1.52. Class-V PLP-dependent aminotransferase family, SerC subfamily.

## Core function (well established)

PSAT1 is **phosphoserine aminotransferase**, the enzyme catalyzing the **second step of the
phosphorylated pathway of de novo L-serine biosynthesis**. It is a **pyridoxal 5'-phosphate
(PLP)-dependent** transaminase that transfers the amino group from L-glutamate onto
3-phosphohydroxypyruvate (3-PHP) to form O-phospho-L-serine (OPS) and 2-oxoglutarate
(alpha-ketoglutarate). Physiologically the reaction runs 3-PHP + L-Glu -> OPS + 2-OG.

- UniProt FUNCTION [file:human/PSAT1/PSAT1-uniprot.txt]: "Involved in L-serine biosynthesis via the phosphorylated
  pathway, a three-step pathway converting the glycolytic intermediate 3-phospho-D-glycerate into L-serine ...
  Catalyzes the second step, that is the pyridoxal 5'-phosphate-dependent transamination of 3-phosphohydroxypyruvate
  and L-glutamate to O-phosphoserine (OPS) and alpha-ketoglutarate."
- UniProt CATALYTIC ACTIVITY: Rhea RHEA:14329, EC 2.6.1.52; O-phospho-L-serine + 2-oxoglutarate =
  3-phosphooxypyruvate + L-glutamate.
- UniProt PATHWAY: "Amino-acid biosynthesis; L-serine biosynthesis; L-serine from 3-phospho-D-glycerate: step 2/3."
- UniProt COFACTOR: pyridoxal 5'-phosphate; "Binds 2 pyridoxal phosphate molecules per dimer, each cofactor is
  bound at the monomer-monomer interface." PLP is covalently bound via Schiff base at Lys-200 (MOD_RES:
  N6-(pyridoxal phosphate)lysine at 200).
- UniProt SUBUNIT: "Homodimer."
- Class-V PLP aminotransferase / SerC subfamily; InterPro IPR022278 (Pser_aminoTfrase), TIGR01364 serC_1,
  PANTHER PTHR43247 PHOSPHOSERINE AMINOTRANSFERASE.

### Primary experimental support
- [PMID:36851825 "Phosphoserine aminotransferase (PSAT) catalyzes the intermediate step, the pyridoxal 5'-phosphate-dependent transamination of 3-phosphohydroxypyruvate and L-glutamate to O-phosphoserine (OPS) and alpha-ketoglutarate"] — full functional + structural characterization of recombinant human PSAT (Protein Sci 2023). Solved apo and OPS-bound X-ray structures (PDB 8A5V/8A5W); kcat/Km ~5.9e6 M-1 s-1; homodimer with cofactor at monomer-monomer interface. UniProt cites this for EC, catalytic activity, cofactor, subunit, activity regulation.
- [PMID:37627284 "phosphoserine aminotransferase (PSAT) and phosphoserine phosphatase"] — functional characterization of PSAT SDD variants (Biomolecules 2023); reconstructed the phosphorylated pathway in vitro; established pathway step and catalytic activity. UniProt cites for FUNCTION, PATHWAY, catalytic activity, subunit.
- [PMID:40281343] — Nat Chem Biol 2025; establishes canonical catalytic activity (mutagenesis K200A abolishes phosphoserine aminotransferase activity) AND a noncanonical, phosphorylation-dependent moonlighting role suppressing ferroptosis.
- [PMID:10637769] — Basurko et al. 1999, IUBMB Life; characterized mammalian (bovine) phosphoserine aminotransferase kinetics; abstract-only cache. Basis of older NAS annotations for MF and L-serine biosynthesis.

## Localization

- Cytosolic enzyme. GOA IDA GO:0005829 cytosol (HPA immunofluorescence, GO_REF:0000052) and Reactome TAS
  cytosol (R-HSA-977333). IBA cytoplasm (GO:0005737) consistent.
- extracellular exosome (GO:0070062, HDA) from two high-throughput exosome proteomics datasets
  (PMID:19056867 urinary exosomes; PMID:20458337 B-cell exosomes). This is a common HTP-proteomics
  "passenger" localization for abundant cytosolic metabolic enzymes; not part of the core catalytic
  function but a valid HDA observation. Keep as non-core.

## Noncanonical / moonlighting: ferroptosis suppression (PMID:40281343)

[PMID:40281343 "interferon-gamma (IFNgamma)-activated calcium/calmodulin-dependent protein kinase II
phosphorylates phosphoserine aminotransferase 1 (PSAT1) at serine 337 (S337), allowing it to interact with
glutathione peroxidase 4 (GPX4) and stabilize the protein, counteracting ferroptosis"]. PSAT1 provides
alpha-ketoglutarate to PHD3/EGLN3, promoting GPX4 Pro-159 hydroxylation, blocking HSC70 binding and
autophagic degradation of GPX4. This underlies GO:0110076 negative regulation of ferroptosis (IDA,
acts_upstream_of). It is a genuine but context-dependent, non-core regulatory role — keep as non-core
(this is not the housekeeping serine-biosynthesis function that defines the gene). UniProt PTM: Ser-337
phosphorylated by CAMK2A. Note MUTAGEN S337A abolishes GPX4 hydroxylation; K200A abolishes transaminase
activity — separating the two functions.

## Disease

- Phosphoserine aminotransferase deficiency (PSATD, MIM:610992): low plasma/CSF serine and glycine,
  intractable seizures, acquired microcephaly, hypertonia, psychomotor retardation [PMID:17436247, PMID:37627284].
- Neu-Laxova syndrome 2 (NLS2, MIM:616038): lethal AR multiple malformation syndrome [PMID:25152457,
  PMID:31903955, PMID:32579715, PMID:37627284]. Both diseases reflect loss of PSAT catalytic activity in the
  serine-biosynthesis pathway; consistent with core function.

## GO_REF / IEA / NAS notes

- GO:0004648 appears from many sources: EXP (PMID:36851825), IDA (PMID:40281343, PMID:37627284), IBA
  (GO_REF:0000033), IEA (GO_REF:0000120 ARBA/EC/RHEA), NAS (PMID:10637769). All converge on the same
  correct catalytic MF -> ACCEPT the experimental ones as core; others KEEP_AS_NON_CORE / ACCEPT-as-redundant.
- GO:0008615 pyridoxine biosynthetic process (NAS PMID:10637769): PSAT1 USES PLP as a cofactor; it does not
  synthesize pyridoxine/vitamin B6. In some bacteria a serC-family activity feeds the DXP-independent PLP
  pathway, but human PSAT1 has no role in pyridoxine biosynthesis. This is a spurious over-annotation
  (NAS, author statement, not experimental) -> MARK_AS_OVER_ANNOTATED.
- protein binding (GO:0005515, IPI, PMID:32814053) — high-throughput interactome (CALR, CDH1, DLST, NEK7);
  uninformative bare "protein binding"; MARK_AS_OVER_ANNOTATED (do not REMOVE per policy).
- identical protein binding (GO:0042802, IPI, PMID:32296183) — HuRI binary interactome self-interaction;
  consistent with the well-established homodimer, so ACCEPT (KEEP_AS_NON_CORE): supports biological homodimer
  though the term itself is not a core catalytic function.

## Core function term ids (for core_functions block)
- MF catalytic: GO:0004648 O-phospho-L-serine:2-oxoglutarate transaminase activity (go.db current label)
- MF cofactor: GO:0030170 pyridoxal phosphate binding
- BP: GO:0006564 L-serine biosynthetic process
- location: GO:0005829 cytosol
