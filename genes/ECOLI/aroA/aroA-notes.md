# aroA (P0A6D3, b0908) - Escherichia coli K-12 EPSP synthase - notes

## Provenance

Provider deep research (`just deep-research`) was unavailable for this review (no provider
key in the session), so no `aroA-deep-research-*.md` file exists. These notes are built from
the UniProt record (aroA-uniprot.txt), the cached publications under `publications/`, the
PANTHER family review `interpro/panther/PTHR21090/PTHR21090-review.yaml`, and the GO ontology
(term definitions read from the cached GO sqlite via runoak). All cached E. coli AroA papers
listed below are abstract-only (`full_text_available: false`), except the cytosol proteomics
paper PMID:18304323, which is full text.

## Identity and family

- 427-aa monofunctional EPSP synthase (3-phosphoshikimate 1-carboxyvinyltransferase,
  EC 2.5.1.19), gene b0908/JW0891. UniProt: "Belongs to the EPSP synthase family."
  Pfam PF00275 EPSP_synthase, NCBIfam TIGR01356 aroA, HAMAP MF_00210, PANTHER
  PTHR21090:SF5. Class I (glyphosate-sensitive) EPSPS.
- E. coli AroA is the reference protein of the PTHR21090 family review and one of the four
  seeds of PAINT node PTN000472635 (EPSP synthase activity, chorismate biosynthesis,
  cytoplasm). The family review judges that node correct for every member with an EPSP
  synthase domain; its only problem is the quinate-repressor branch SF27, which does not
  affect aroA.

## Reaction and mechanism

- UniProt CC FUNCTION (ECO:0000269 to seven E. coli papers): "Catalyzes the transfer of the
  enolpyruvyl moiety of phosphoenolpyruvate (PEP) to the 5-hydroxyl of shikimate-3-phosphate
  (S3P) to produce enolpyruvyl shikimate-3-phosphate and inorganic phosphate."
- Sixth enzyme of the shikimate pathway: [PMID:13129913 "AroA is the sixth enzyme of the
  shikimate pathway leading to the synthesis of aromatic compounds in numerous
  microorganisms and plants."]
- Enolpyruvyl transfer is an addition-elimination reaction via a tetrahedral intermediate;
  Asp313 is required for the elimination step: [PMID:13129913 "The structures depict the
  tetrahedral reaction intermediate states of the enzymes and prove that, without the
  aspartate side chain, the overall addition-elimination reaction in both enzymes is halted
  after the addition step."] UniProt FT ACT_SITE 313 "Proton acceptor".
- Shares the enolpyruvyl transferase fold with MurA (UDP-GlcNAc enolpyruvyl transferase):
  [PMID:13129913 "UDP-N-acetylglucosamine enolpyruvyl transferase (MurA) and
  5-enolpyruvylshikimate-3-phosphate synthase (AroA) constitute the small enzyme family of
  enolpyruvyl transferases, which catalyze the chemically unusual reaction of enolpyruvyl
  transfer."]
- Two-domain enzyme closing on S3P: [PMID:11171958 "The two-domain enzyme closes on ligand
  binding, thereby forming the active site in the interdomain cleft."]
- Purified as an active monomer from an overproducing strain: [PMID:6229418 "A simple method
  for the purification of homogeneous enzyme in milligram quantities has been devised."]
  Km S3P 3.5 uM, Km PEP 15 uM (UniProt, ECO:0000269|PubMed:6229418).
- Shikimate can substitute (poorly) for S3P: [PMID:16225867 "The natural substrate of EPSP
  synthase is shikimate-3-phosphate. However, this enzyme can also utilize shikimate as
  substrate."] This is a substrate-analogue property, not a separate physiological activity.
- Covalent inactivation by bromopyruvate at conserved Cys408/Lys411: [PMID:1899181
  "bromopyruvate inactivated the enzyme by modifying Cys-408 and Lys-411, which are
  conserved in all enzyme sequences studied to date."]

## Glyphosate

- Glyphosate binds in the PEP site: [PMID:11171958 "Glyphosate appears to occupy the binding
  site of the second substrate of EPSP synthase (phosphoenol pyruvate), mimicking an
  intermediate state of the ternary enzyme.substrates complex."]
- Resistance mutations G96A [PMID:12430021 "The mutant enzyme is insensitive to glyphosate
  with unaltered affinity for its first substrate, shikimate-3-phosphate (S3P), but displays
  a 30-fold lower affinity for its second substrate, phosphoenolpyruvate (PEP)."], P101X
  (PMID:17855366) and T97I/P101S (the GA21 maize mutation) [PMID:19211556 "The T97I/P101S
  enzyme is essentially insensitive to glyphosate (K(i) = 2.4 mm) but maintains high
  affinity for the substrate phosphoenolpyruvate (PEP) (K(m) = 0.1 mm)."]
- Class I vs class II: [PMID:17958399 "The (R)-difluoromethyl and (R)-phosphonate analogues of
  the TI are the most potent inhibitors of EPSPS described to date."]

All of the EXP rows on GO:0003866 come from these steady-state kinetic/structural studies of
wild-type and mutant E. coli enzyme, which assay the S3P + PEP reaction directly.

## Pathway context

- UniProt PATHWAY: chorismate biosynthesis, chorismate from D-erythrose 4-phosphate and
  phosphoenolpyruvate, step 6/7 (UniPathway UPA00053/UER00089). The product EPSP is
  converted to chorismate by chorismate synthase (AroC); chorismate is the branch point for
  Phe, Tyr, Trp, folate, ubiquinone, menaquinone and enterobactin.
- PMID:4289188 (Morell et al. 1967, J Biol Chem 242:82-90, "The enzymic synthesis of
  chorismic and prephenic acids from 3-enolpyruvylshikimic acid 5-phosphate") has no abstract
  in the cached record (PubMed has none for this 1967 paper). The EcoCyc IDA rows from it
  (EPSP synthase activity; chorismate biosynthetic process, acts_upstream_of_or_within)
  cannot be checked against the text here; they are consistent with everything else known.

## Location

- Soluble, no signal peptide or TM segment. Detected in the cytosolic fraction of E. coli
  MC4100 by LC-MS/MS: [PMID:18304323 "we identified 1103 proteins from the cytosolic fraction
  of the Escherichia coli strain MC4100."] aroA is not named in the main text (the protein
  list is supplementary), so the EcoCyc IDA rests on the dataset.

## GO term checks (cached GO via runoak)

- GO:0009423 chorismate biosynthetic process is_a chorismate metabolic process and dicarboxylic
  acid biosynthetic process; it is NOT a descendant of GO:0009073 aromatic amino acid
  biosynthetic process (defined as "The chemical reactions and pathways resulting in the
  formation of an amino acid whose structure includes an aromatic ring."). So the IEA
  GO:0009073 row is a separate, broader pathway claim, not a parent term.
- GO:0003866 is_a GO:0016765 transferase activity, transferring alkyl or aryl (other than
  methyl) groups, is_a transferase activity, is_a catalytic activity.
- GO:0005829 cytosol part_of GO:0005737 cytoplasm.
