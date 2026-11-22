# YML6 (P51998, YML025C) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: YML6 is the experimentally characterised S. cerevisiae relative of
SCHPO/yml6 (O74801). This review was done without consulting any ProtNLM2
output.

### Deep research

`just deep-research-falcon yeast YML6 --fallback perplexity-lite` failed:
falcon returned `403 Forbidden` at Edison auth ("Failed to authenticate"), and
the perplexity-lite fallback returned HTTP 401 "You exceeded your current quota".
No deep-research file was produced. The review relies on the UniProt record and
the cached primary literature listed below.

### Identity and evolutionary placement

- UniProt: "Large ribosomal subunit protein uL4m"; "Belongs to the universal
  ribosomal protein uL4 family." [file:yeast/YML6/YML6-uniprot.txt]
- PANTHER: PTHR10746 (50S RIBOSOMAL PROTEIN L4), subfamily PTHR10746:SF6
  (LARGE RIBOSOMAL SUBUNIT PROTEIN UL4M). The same subfamily holds S. pombe
  yml6 and human MRPL4 (Q9BYD3).
- PAINT: the mtLSU IBA comes from node PTN000078780 (the mitochondrial uL4m
  clade). Its WITH/FROM lists SGD:S000004487 (this gene), Q9BYD3 (human MRPL4)
  and Q385G8 (trypanosome). The structural-constituent and ribosome IBAs come from
  the family root PTN000078778. The regulation-of-translation IBA also sits at
  PTN000078778, and its only experimental donor is E. coli L4 (P60723).
- The N-terminal 26 residues form a mitochondrial transit peptide. Grohmann et al.
  1991 sequenced the mature N-terminus from residue 27 [PMID:2060626; UniProt FT
  TRANSIT 1..26, ECO:0000269|PubMed:2060626].

### Experimental evidence in S. cerevisiae itself

1. Protein chemistry. YmL6 was purified from the mitochondrial large subunit and
   partially sequenced, which assigned it to its gene [PMID:9151978 "We have
   purified 13 large subunit proteins of the mitochondrial ribosome of the yeast
   Saccharomyces cerevisiae and determined their partial amino acid sequences."].
   The UniProt RP line for this paper is "PROTEIN SEQUENCE OF 110-121; 147-156;
   241-249 AND 279-286, AND SUBUNIT". Only the abstract is cached.
2. Structure. In the 3.2 A cryo-EM structure of the yeast 54S subunit, the protein
   is built as uL4m (PDB 3J6B chain D, residues 1-286) [PMID:24675956]. The
   conserved exit-tunnel constriction is "formed by uL22 and uL4"
   [PMID:24675956]. The full mitoribosome structure is described in PMID:28154081.
3. Localisation. Large-scale and organellar proteomics place the protein in
   mitochondria [PMID:16823961; PMID:24769239; UniProt SUBCELLULAR LOCATION
   ECO:0000269|PubMed:14562095, PubMed:14576278]. Mitoribosomes are tethered to
   the inner membrane by rRNA ES 96-ES1 and Mba1 [PMID:25609543]. uL4m itself
   does not form those contacts.

### Inferred, not experimentally shown for YML6

- rRNA binding and its role as an early assembly initiator are known for
  bacterial L4. No YML6-specific experiment on either was found in the cached
  literature, so no NEW MF term is proposed.
- Regulation of translation: E. coli L4 represses the S10 operon autogenously.
  That mechanism depends on bacterial operon organisation. No mitochondrial uL4m
  donor (yeast, human or trypanosome) has a regulatory annotation, so the IBA is
  treated as an over-propagation from the family root.

### Decisions summary

- structural constituent of ribosome (IBA/IDA/IEA): ACCEPT.
- mitochondrial large ribosomal subunit (IBA/IDA/NAS): ACCEPT.
- mitochondrial translation (IC/NAS): ACCEPT.
- mitochondrion (HDA x2, IEA): ACCEPT. Correct, and as specific as the proteomic
  and SubCell evidence allows.
- mitochondrial inner membrane (NAS, ComplexPortal): KEEP_AS_NON_CORE. This is a
  complex-level peripheral association.
- ribosome (IBA, IEA): MODIFY to mitochondrial large ribosomal subunit.
- translation (IEA): MODIFY to mitochondrial translation.
- regulation of translation (IBA, root node, E. coli donor): MARK_AS_OVER_ANNOTATED.

### Transfer guidance for SCHPO/yml6 and human MRPL4

Several things are established experimentally in S. cerevisiae: the protein is a
subunit of the 54S mtLSU (by protein sequencing and cryo-EM), and it is located
in mitochondria. Its position lining the tunnel constriction is structural.
Structural constituent of ribosome and mitochondrial translation follow from
subunit membership; they are not shown by a separate activity assay. These
properties can be transferred within PTHR10746:SF6 / PTN000078780. Regulation of
translation should not be transferred.
