# GPD (Pichia kudriavzevii / Issatchenkia orientalis, UniProtKB A8W1U0) notes

No deep-research provider was available in this environment. This file is a manual
literature and record review.

## Identity

- UniProtKB A8W1U0 (A8W1U0_PICKU), TrEMBL, 388 aa, PE 3 (inferred from homology).
  Gene name `GPD` from EMBL ABW38024.1; the entry is derived from the single genomic
  clone EU186536, not from a genome assembly, and it carries no `DR Proteomes` line.
- The entry's only literature reference is PMID:18452539, whose title names
  *Candida glycerinogenes*. This is **not** a wrong-organism attribution: NCBI
  Taxonomy lists `'Candida glycerinogenes'` (in quotes, i.e. not validly published)
  as a synonym of *Pichia kudriavzevii* (NCBITaxon:4909), together with
  *Issatchenkia orientalis* and *Candida krusei*, and GenBank EU186536 itself is
  filed under `/organism="Pichia kudriavzevii" /db_xref="taxon:4909"` (NCBI efetch,
  2026-10-28). The deposited CDS ABW38024.1 translation is exactly the A8W1U0
  sequence, and the paper's reported 388 residues match the entry's length
  [PMID:18452539 "Sequence analysis revealed a 1167-bp open reading frame encoding a
  putative peptide of 388 deduced amino acids"]. So PMID:18452539 characterises this
  very protein, and the UniProt taxonomy assignment is sound.
- Family: PANTHER PTHR11728 / PTHR11728:SF8, NCBIfam TIGR03376 (`glycerol3P_DH`),
  PIRSF000114, PROSITE PS00957. Two-domain architecture: Pfam PF01210
  (NAD(+)-binding, residues 36-201) and PF07479 (C-terminal substrate-binding,
  234-379), with a PIRSR-annotated proton-acceptor active site at Lys245 and NAD(+)
  and substrate binding residues.

## Relationship to the reference proteome

A8W1U0 is not in a reference proteome. A UniProtKB REST search for every EC 1.1.1.8
entry of NCBITaxon:4909 returns exactly two records (2026-10-28): A8W1U0 (388 aa, no
proteome) and A0A2U9RB90 (415 aa, `UP000249293: Chromosome 5`, ORF `C5L36_0E02100`).
A8W1U0's own record cross-references `FungiDB:C5L36_0E02100`, i.e. the same locus.
Aligned, A8W1U0 corresponds to residues 28-415 of A0A2U9RB90 with 385/388 identities
(99.2%; R89K, F165S, R228H in A8W1U0 numbering); A0A2U9RB90 carries a 27-residue
N-terminal extension (`MFLISKSLHFTRSFSNTIKTLNRSNIK`) that the A8W1U0 gene model
starts after. These are different strains (an industrial glycerol producer versus the
sequenced reference isolate) and the shorter model is the one with functional data
behind it, since the 388-residue product complements *S. cerevisiae* gpd1Δ. The
relationship is recorded under `alternative_records` as
`REFERENCE_PROTEOME_EQUIVALENT`, with the gene-model difference stated. Which start
codon is used in vivo is unresolved and is raised in `suggested_questions`; the review
does not assert that either model is defective.

## Function

- Direct evidence for this protein: heterologous complementation.
  [PMID:18452539 "Functional analysis revealed that Saccharomyces cerevisiae gpd1Delta
  and gpd1Delta/gpd2Delta osmosensitive mutants transformed with CgGPD were restored
  to the wild-type phenotype when cultured in high osmolarity media, suggesting that
  it is a functional GPD protein."] and
  [PMID:18452539 "Transformants also accumulated glycerol intracellularly and
  GPD-specific activity increased significantly when stressed with NaCl"]. This is a
  phenotypic and enzyme-activity result in a heterologous host, not a purified-enzyme
  kinetic characterisation.
- Direction of the physiological reaction. The EC 1.1.1.8 reaction is written
  G3P + NAD(+) = DHAP + NADH, but in yeast the NAD(+)-dependent enzyme runs the
  reductive direction, making glycerol 3-phosphate from DHAP; glycerol 3-phosphate
  phosphatase then releases glycerol. In *S. cerevisiae*,
  [PMID:8196651 "We have cloned a gene encoding the key enzyme of glycerol synthesis,
  the NADH-dependent cytosolic glycerol-3-phosphate dehydrogenase, and we named it
  GPD1"] and
  [PMID:9171333 "Mutants deleted for both GPD1 and GPD2 do not produce detectable
  glycerol"]. In *P. kudriavzevii* itself, deleting GPD abolished glycerol
  accumulation [PMID:41617712 "Since glycerol-3-phosphate dehydrogenase (GPD) plays a
  key role in the glycerol biosynthesis pathway, we knocked out the GPD gene in strain
  JL01, generating the strain JL02."; "without any detectable glycerol accumulation"].
  The UniRule-derived `GO:0046168 glycerol-3-phosphate catabolic process` therefore
  asserts the wrong direction for this family; it is MODIFYed to
  `GO:0046167 glycerol-3-phosphate biosynthetic process` and recorded as a
  `source_defect` against UniProt (rule UR000080073).
- Localisation. The NAD(+)-dependent enzyme is cytosolic in *S. cerevisiae*
  [PMID:8196651 "the NADH-dependent cytosolic glycerol-3-phosphate dehydrogenase"],
  and PAINT asserts cytosol for the family. The nucleus annotation traces to a
  fungi-scoped IBD node (PTHR11728 PTN000919785, taxon:4751) seeded by a single gene,
  *S. cerevisiae* GPD1, whose nuclear localisation is a stress-conditional
  relocalisation [PMID:20026609 "Exposure of cells to osmotic stress induces changes
  in the subcellular distribution of Gpd1p to the cytosol and nucleus."]. The target
  is inside the clade, so the transfer is not rejected, but the claim is conditional
  and secondary: kept as non-core.
- Oligomeric state. `GO:0042803 protein homodimerization activity` comes from
  InterPro IPR017751 (eukaryotic NAD-dependent G3PDH). Human GPD1 is a homodimer by
  crystallography (PMID:16460752; the abstract does not use the word, the oligomeric
  state is in the structures and in UniProt's curated SUBUNIT line for P21695). No
  oligomeric state has been determined for this protein, so this row is kept as
  non-core on family grounds rather than accepted as core.

## Review decisions (10 IEA rows, no PENDING left)

| Term | Action |
| --- | --- |
| GO:0141152 glycerol-3-phosphate dehydrogenase (NAD+) activity | ACCEPT (core) |
| GO:0047952 G3P dehydrogenase [NAD(P)+] activity | MODIFY → GO:0141152 |
| GO:0016616 oxidoreductase activity, CH-OH donors, NAD(P) acceptor | MODIFY → GO:0141152 |
| GO:0051287 NAD binding | KEEP_AS_NON_CORE |
| GO:0042803 protein homodimerization activity | KEEP_AS_NON_CORE |
| GO:0006072 glycerol-3-phosphate metabolic process | MODIFY → GO:0046167 |
| GO:0046168 glycerol-3-phosphate catabolic process | MODIFY → GO:0046167 (+ source defect) |
| GO:0005975 carbohydrate metabolic process | MODIFY → GO:0006114 |
| GO:0005829 cytosol | ACCEPT |
| GO:0005634 nucleus | KEEP_AS_NON_CORE |

No `NEW` rows were added. Glycerol biosynthesis and glycerol-3-phosphate biosynthesis
both enter the review as MODIFY replacements of terms the gene already carries, which
is the refinement path; neither needed the `NEW` bar. No process term was proposed for
oxalic acid production: GPD is deleted in those strains, and a gene whose removal
improves a pathway is not a participant in it.

## CMMMech cross-check (data/records/allanite-leachate.yaml)

The grounding of the `gpd_glycerol3P_dehydrogenase` node to UniProtKB:A8W1U0 is
correct in species, gene and enzyme, and the InterPro/Pfam/EC fields match the UniProt
record exactly. Three points for the CMMMech curator (not edited here; CMMMech is
read-only for this work):

1. **`functional_role` is self-contradictory on JL04.** It says GPD is "deleted in
   Issatchenkia orientalis (Pichia kudriavzevii) strain JL02 (and retained in JL04)",
   while the accompanying evidence item in the same block says Supplementary Table 1
   documents "the Δgpd knockout genotype in engineered strains JL02, JL03, and JL04".
   The latter is right: JL04 descends from JL02, so GPD is deleted, not retained, in
   JL04. The "(and retained in JL04)" phrasing appears to have been copied from the
   neighbouring PYK1 and PYC entries, where retention in JL04 is the correct claim.
2. **No locus or reference-proteome field is given for this protein example**, unlike
   the PYC entry. A8W1U0 is not in any reference proteome; the reference-proteome
   representation of the same locus is A0A2U9RB90 (`UP000249293`, ORF
   `C5L36_0E02100`). Recording that would make the grounding checkable. (The PYC
   entry's `reference_proteome_id: UP000249646` is wrong and was reported from the
   PYC review; the GPD entry has no such field, so the error does not recur here.)
3. **The 14.72 g/L figure is more precise than the cited text.** The paper's running
   text gives 14.7 g/L for JL02; 14.72 is presumably read from the source data. Minor,
   but the evidence explanation attributes it to the main-text section.

Nothing in CMMMech overstates this protein's function: calling it an "endogenous
NAD-dependent glycerol-3-phosphate dehydrogenase" whose deletion removes glycerol
byproduct is exactly what the paper shows, and the record does not claim any role for
GPD in oxalate formation or REE recovery.
