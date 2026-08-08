# NT5C2 (cytosolic purine 5'-nucleotidase / cN-II) — review notes

UniProt: P49902 (5NTC_HUMAN). HGNC:8022. 561 aa. Human (NCBITaxon:9606).

## Identity and core biochemistry

NT5C2 is a **cytosolic purine 5'-nucleotidase** (cN-II; also "High Km 5'-nucleotidase",
"cytosolic IMP/GMP-specific 5'-nucleotidase"). It is a member of the HAD (haloacid
dehalogenase) superfamily [file:human/NT5C2/NT5C2-uniprot.txt "The tetrameric enzyme is
structurally similar to enzymes of the haloacid dehalogenase (HAD) superfamily"; CDD
cd07522 HAD_cN-II; "Belongs to the 5'(3')-deoxyribonucleotidase family"].

Reaction: dephosphorylates **6-hydroxypurine nucleoside 5'-monophosphates**
[file:human/NT5C2/NT5C2-uniprot.txt "Broad specificity cytosolic 5'-nucleotidase that
catalyzes the dephosphorylation of 6-hydroxypurine nucleoside 5'-monophosphates"].
Highest activity for **IMP and GMP, then dIMP, dGMP and XMP**
[file:human/NT5C2/NT5C2-uniprot.txt "Has the highest activities for IMP and GMP followed
by dIMP, dGMP and XMP"]. Products are inosine/guanosine/xanthosine (and deoxy-
counterparts) + phosphate. EC 3.1.3.5 and EC 3.1.3.99 (IMP 5'-nucleotidase).

Also has a **phosphotransferase activity** (EC 2.7.1.77): transfers a phosphate from a
donor NMP to an acceptor nucleoside, preferably inosine, deoxyinosine and guanosine
[file:human/NT5C2/NT5C2-uniprot.txt "possesses a phosphotransferase activity by which it
can transfer a phosphate from a donor nucleoside monophosphate to an acceptor nucleoside,
preferably inosine, deoxyinosine and guanosine"]. This dual hydrolase/transferase
behavior means cN-II is not a pure catabolic enzyme [PMID:1659319 "cytosolic
5'-nucleotidase cannot be considered a pure catabolic enzyme"].

Through these activities it **regulates intracellular purine nucleoside/nucleotide pools**
[file:human/NT5C2/NT5C2-uniprot.txt "regulates the purine nucleoside/nucleotide pools
within the cell"; PMID:17405878 "regulates the IMP and GMP pools within the cell"].

## Cofactor, regulation, structure

- **Mg2+** required; binds 1 Mg2+ per subunit [file:human/NT5C2/NT5C2-uniprot.txt "Binds 1
  Mg(2+) ion per subunit"].
- **Homotetramer** [file:human/NT5C2/NT5C2-uniprot.txt "SUBUNIT: Homotetramer";
  PMID:17405878 "The tetrameric enzyme"].
- **Allosterically activated** by ATP, diadenosine polyphosphates (Ap4A), and
  2,3-bisphosphoglycerate; inhibited by inorganic phosphate
  [file:human/NT5C2/NT5C2-uniprot.txt "Allosterically activated by various compounds
  including ATP, 2,3-BPG/2,3-Bisphosphoglyceric acid and Ap4A"; "Inhibited by inorganic
  phosphate"]. Effector binding is a prerequisite to Mg2+ and substrate binding
  [file:human/NT5C2/NT5C2-uniprot.txt "Binding of an allosteric activator is a
  prerequisiste to magnesium and substrate binding"].
- Crystal structures (many PDB entries, e.g. 2J2C/2JC9/2XCV) define catalytic Asp52
  (nucleophile, ACT_SITE), Asp54 (proton donor), and two allosteric effector sites
  [PMID:21396942 "reveal the structural basis for the allosteric activation of cN-II"].
  D52N mutant loses activity [file:human/NT5C2/NT5C2-uniprot.txt "MUTAGEN 52 ... D->N:
  Loss of 5' nucleotidase activity"].
- C-terminal polyglutamic/aspartic tail (residues ~548-561) required for tetramer assembly
  [file:human/NT5C2/NT5C2-uniprot.txt "REGION 548..561 ... Required for tetramer
  assembly"; PMID:10092873 "removal of the polyglutamic/aspartic acid tail ... caused
  profound kinetic and structural changes"].

## Location

Cytosol / cytoplasm [file:human/NT5C2/NT5C2-uniprot.txt "SUBCELLULAR LOCATION: Cytoplasm,
cytosol"; PMID:9371705]. Widely expressed.

## Physiology / disease

- **Drug (in)activation**: cN-II dephosphorylates the active 5'-monophosphates of purine
  nucleoside-analog prodrugs, reversing kinase activation and reducing efficacy;
  overexpression of cN-II can confer resistance to purine analogs [PMID:12907246
  "overproduction of cN-II could lead to resistance against purine analogs";
  "Activation may be reversed by dephosphorylation if the 5'-phosphates are substrates for
  5'-nucleotidases"]. Reactome captures its role in abacavir/carbovir and ribavirin
  metabolism (R-HSA-2162066, R-HSA-9754916, R-HSA-9755078). Activating NT5C2 mutations
  drive thiopurine resistance / relapse in acute lymphoblastic leukemia (ALL) — widely
  reported clinical relevance (CIViC 18 evidence items; not in cached pubs but well
  established).
- **Hereditary spastic paraplegia SPG45/SPG65**: autosomal-recessive; caused by NT5C2
  variants [file:human/NT5C2/NT5C2-uniprot.txt "DISEASE: Spastic paraplegia 45, autosomal
  recessive (SPG45)"; PMID:24482476 involvement in SPG45; PMID:28884889 SPG45 variant
  Pro-460].
- **Metabolic/AMPK**: siRNA silencing of NT5C2 in human myotubes raises AMP/ATP ratio and
  activates AMPK [PMID:21873433 "Using siRNA to silence NT5C2 expression in cultured human
  myotubes, we observed a 2-fold increase in the AMP/ATP ratio, a 2.4-fold increase in
  AMPK phosphorylation"]. This paper (MGI curated) is the source of several BP annotations
  (IMP catabolic process, allantoin metabolic process, cytosol).

## Notable single-paper / non-canonical claims

PMID:36159777 (glioblastoma/TRIM22 study) reports that **NT5C2 acts as an E3-ubiquitin-
ligase-like factor responsible for K48-linked ubiquitination of RIG-I**, negatively
regulating antiviral RIG-I signaling [PMID:36159777 "NT5C2 is responsible for K48-linked
ubiquitination"; "NT5C2 is responsible for the K48-linked ubiquitination of RIG-I"]. This
is the sole source for the GO:0061630 (ubiquitin protein ligase activity), GO:0070936
(protein K48-linked ubiquitination) and GO:0050689 (neg reg of defense response to virus
by host) annotations. It is mechanistically surprising for a HAD-fold metabolic enzyme
with no recognizable ubiquitin-ligase (RING/HECT/RBR) domain, and the paper itself shows
NT5C2 and RIG-I "interacted indirectly" via TRIM22. These are experimental IDA
annotations, so they are retained but flagged as non-core / likely over-annotation
(moonlighting claim needing independent confirmation), not removed.

## Annotation landscape (GOA, 52 rows)

- Core MF: **5'-nucleotidase activity (GO:0008253)** — supported by IDA (PMID:1659319,
  9371705, 10092873, 21873433), EXP (PMID:12907246, 17405878), plus IBA/ISS/IEA/TAS
  redundancies. This is the single well-supported catalytic function.
- **nucleoside phosphotransferase activity (GO:0050146)** — IDA (PMID:1659319, 9371705),
  IBA, IEA. Second bona-fide catalytic activity.
- **5'-deoxynucleotidase activity (GO:0002953)** — IEA (Rhea), consistent with dIMP/dGMP
  substrates; keep non-core.
- Core BP: IMP metabolic/catabolic (GO:0046040, GO:0006204), GMP metabolic (GO:0046037),
  dGMP metabolic (GO:0046054), purine ribonucleotide catabolic (GO:0009154). Well
  supported.
- allantoin metabolic process (GO:0000255) — IDA from MGI/PMID:21873433; allantoin is a
  downstream purine-degradation product but humans lack urate oxidase, so this is
  peripheral (non-core).
- adenosine metabolic process (GO:0046085) — IBA only; cN-II prefers IMP/GMP over AMP;
  keep non-core.
- CC: cytosol (GO:0005829) / cytoplasm (GO:0005737) — strongly supported (IDA, IBA, IEA,
  TAS). Core location.
- MF binding: ATP binding (GO:0005524, IDA PMID:21396942 — this is the allosteric ATP
  activator site, real), identical protein binding (GO:0042802 — homotetramer, real),
  metal ion binding (GO:0046872 — Mg2+, real IEA-KW).
- protein binding (GO:0005515) — 13 IPI rows from high-throughput interactome screens;
  uninformative, keep as non-core (do not remove IPI per policy).
- Ubiquitin-related (see above): retained, flagged.

## Core function summary

1. Cytosolic purine 5'-nucleotidase: hydrolyzes IMP/GMP/XMP (+ deoxy forms) to the
   nucleoside + Pi (GO:0008253), Mg2+-dependent, allosterically regulated.
2. Nucleoside phosphotransferase activity (GO:0050146): transfers phosphate from NMP to a
   nucleoside acceptor.
3. Regulation of intracellular purine (deoxy)nucleotide pools — IMP/GMP metabolic and
   catabolic processes (GO:0046040, GO:0006204, GO:0046037), in the cytosol.
</content>
