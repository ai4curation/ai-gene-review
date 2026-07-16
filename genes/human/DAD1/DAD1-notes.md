# DAD1 (defender against cell death 1) — review notes

UniProt: **P61803** (DAD1_HUMAN), HGNC:2664, 113 aa, chromosome 14.
RecName (UniProt): **Dolichyl-diphosphooligosaccharide--protein glycosyltransferase subunit DAD1**;
AltName: **Defender against cell death 1 (DAD-1)** [file:human/DAD1/DAD1-uniprot.txt].

## Core biology

DAD1 is a small, hydrophobic, **multi-pass ER membrane protein** that is a **non-catalytic subunit
of the oligosaccharyltransferase (OST) complex**. The OST complex catalyzes the first committed step
of protein N-linked glycosylation: en-bloc transfer of the pre-assembled Glc3Man9GlcNAc2 glycan from
the dolichol-pyrophosphate lipid carrier onto asparagine residues in Asn-X-Ser/Thr sequons of nascent
polypeptides in the ER.

- UniProt FUNCTION: "Subunit of the oligosaccharyl transferase (OST) complex that catalyzes the
  initial transfer of a defined glycan (Glc(3)Man(9)GlcNAc(2) in eukaryotes) from the lipid carrier
  dolichol-pyrophosphate to an asparagine residue within an Asn-X-Ser/Thr consensus motif in nascent
  polypeptide chains, the first step in protein N-glycosylation" [file:human/DAD1/DAD1-uniprot.txt].
- "All subunits are required for a maximal enzyme activity" and DAD1 is "Required for the assembly of
  both SST3A- and SS3B-containing OST complexes. Loss of the DAD1 protein triggers apoptosis"
  [file:human/DAD1/DAD1-uniprot.txt].
- Topology: three transmembrane helices; TOPO_DOM cytoplasmic 2–30, TM 31–51, TM 53–73, TM 93–113
  [file:human/DAD1/DAD1-uniprot.txt]. SUBCELLULAR LOCATION: "Endoplasmic reticulum membrane;
  Multi-pass membrane protein" [file:human/DAD1/DAD1-uniprot.txt].
- SIMILARITY: "Belongs to the DAD/OST2 family" [file:human/DAD1/DAD1-uniprot.txt].

## OST complex composition and the two forms (OST-A vs OST-B)

Mammalian OST exists in two forms sharing common core subunits, distinguished by catalytic subunit
and accessory subunits:

- UniProt SUBUNIT: "OST exists in two different complex forms which contain common core subunits
  RPN1, RPN2, OST48, OST4, DAD1 and TMEM258, either STT3A or STT3B as catalytic subunits, and
  form-specific accessory subunits" [file:human/DAD1/DAD1-uniprot.txt].
- OST-A (co-translational, STT3A) vs OST-B (post-translocational, STT3B): "Mammals express two
  distinct OST complexes that act in a cotranslational (OST-A) or posttranslocational (OST-B) manner"
  [PMID:31831667 abstract]. Cryo-EM structures of both were solved with DAD1 modeled (PDB 6S7O/6S7T,
  DAD1 = chain D, residues 1–113) [file:human/DAD1/DAD1-uniprot.txt].
- DAD1 is a **shared core subunit present in BOTH OST-A and OST-B**, hence the two ComplexPortal /
  GO annotations to GO:0160226 (OST-A) and GO:0160227 (OST-B).

## Functional evidence

- **PMID:22467853** (Roboti & High 2012, abstract only): siRNA knockdown of DAD1 (and OST48)
  destabilizes both STT3A- and STT3B-containing OST complexes and causes hypoglycosylation. Abstract:
  "OST48 and DAD1 are required for the assembly of both STT3A- and STT3B-containing OST complexes.
  The structural perturbations of these complexes we observe in OST48- and DAD1-depleted cells
  underlie their pronounced hypoglycosylation phenotypes. Thus, OST48 and DAD1 are global modulators
  of OST stability and hence N-glycosylation." This is the basis for the IMP annotations to
  N-linked glycosylation (GO:0006487), regulation of protein stability (GO:0031647, referring to OST
  complex stability), enzyme activator activity (GO:0008047), and the IDA to OST complex (GO:0008250).
- **PMID:31831667** (Ramírez, Kowal & Locher 2019, Science, abstract only): cryo-EM structures of
  human OST-A and OST-B; identification of DAD1 in the OST complex; establishes the N-glycosylation
  pathway. Basis for the ComplexPortal IDA/IPI/NAS annotations and the UniProt IDA to OST-A/OST-B.
- **PMID:36697828** (Gemmer et al. 2023, Nature, full text cached): cryo-ET of the ribosome–translocon
  showing OST-A (OSTA) as a component of the SEC61–OSTA–TRAP translocon at the ER membrane; the paper
  does not name DAD1 individually but resolves the OST-A complex (PDB 8B6L includes DAD1 chain M per
  UniProt). "OSTA, which is responsible for co-translational N-glycosylation of substrates, is
  observed in at least 50% of translocon particles in mammalian cells" [PMID:36697828]. Basis for the
  UniProt IDA to OST-A.
- **PMID:38670073** (Lampson et al. 2024, Cell, abstract only): CRISPR screens + cryo-EM of the
  STT3A-containing OST (OST-A); TLR4 N-glycosylation depends on OST-A; DAD1 modeled in PDB 8PN9
  (chain D) per UniProt. "the LPS receptor Toll-like receptor 4 (TLR4) is specifically dependent on
  the oligosaccharyltransferase complex OST-A for N-glycosylation and cell-surface localization"
  [PMID:38670073]. Basis for the UniProt IDA to OST-A.

## Apoptosis / historical name

DAD1 = "defender against cell death 1". Originally cloned as the gene that complements the tsBN7
temperature-sensitive apoptotic hamster BHK21 mutant; loss of DAD1 protein triggers apoptosis.
- PMID:8413235 (Nakashima et al. 1993, abstract only): "The DAD1 protein disappeared in tsBN7 cells
  following a shift to the nonpermissive temperature, suggesting that loss of the DAD1 protein
  triggers apoptosis." This is the origin of the anti-apoptotic (GO:0043066) TAS annotation and the
  UniProt-KW apoptosis keyword.
- **Interpretation for curation**: the anti-apoptotic phenotype is a **downstream consequence** of
  DAD1's essential OST role — abolishing N-glycosylation and destabilizing OST triggers apoptosis.
  It is not a distinct molecular function of DAD1. The apoptosis-related BP annotations are therefore
  retained as **non-core** (KEEP_AS_NON_CORE), while the core is the OST / N-glycosylation role.

## Membrane proteome (NK cells)

- PMID:19946888 (Ghosh et al. 2010, abstract only): large-scale membrane proteome of NK-like YTS cells;
  DAD1 was one of 1843 MS-identified proteins. Supports generic `membrane` (GO:0016020) HDA. Non-core,
  low-information localization; the ER-membrane term is the specific, correct one.

## Curation summary (core functions)

- `in_complex`: **GO:0008250 oligosaccharyltransferase complex** (protein-complex CC term).
- `contributes_to_molecular_function`: **GO:0004579 dolichyl-diphosphooligosaccharide-protein
  glycotransferase activity** (the OST catalytic activity; DAD1 is non-catalytic but contributes to
  the holo-enzyme activity by being required for complex assembly/stability).
- `involved_in` (BP): **GO:0006487 protein N-linked glycosylation**.
- `locations`: **GO:0005789 endoplasmic reticulum membrane**.

Avoid bare "protein binding" as a core function (there is no GO:0005515 IPI in the GOA anyway). The
non-catalytic subunit role is modeled via `in_complex` + `contributes_to_molecular_function`.

## Term id/label verification (local go.db, oaklib)

Verified labels and branches:
- GO:0008250 oligosaccharyltransferase complex → subClassOf GO:0032991 (protein-containing complex) ✓ CC
- GO:0004579 dolichyl-diphosphooligosaccharide-protein glycotransferase activity → GO:0003674 ✓ MF
- GO:0006487 protein N-linked glycosylation → GO:0008150 ✓ BP
- GO:0005789 endoplasmic reticulum membrane → GO:0005575 ✓ CC
