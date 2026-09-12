# SUOX (human) — gene review notes

UniProt: P51687 (SUOX_HUMAN). Gene: SUOX (HGNC:11460). Chr 12. 545 aa precursor.
All provenance below is grounded in local files: `SUOX-uniprot.txt`, `SUOX-goa.tsv`,
and cached `publications/PMID_*.md`.

## Identity and core biochemistry

SUOX encodes **sulfite oxidase, mitochondrial** — the terminal enzyme of oxidative
sulfur-amino-acid (cysteine/methionine) catabolism. It oxidises sulfite to sulfate,
passing electrons to cytochrome c.

- EC 1.8.3.1; reaction sulfite + O2 + H2O = sulfate + H2O2
  [file:human/SUOX/SUOX-uniprot.txt: "Reaction=sulfite + O2 + H2O = sulfate + H2O2"].
- Terminal step of sulfur amino acid degradation
  [file:human/SUOX/SUOX-uniprot.txt: "Catalyzes the oxidation of sulfite to sulfate, the terminal"]
  [file:human/SUOX/SUOX-uniprot.txt: "reaction in the oxidative degradation of sulfur-containing amino acids"].
- Confirmed independently in the Kisker 1997 structure paper (chicken orthologue, but
  the paper explicitly frames the human enzyme and human deficiency):
  [PMID:9428520 "sulfite oxidase catalyzes the conversion of sulfite to sulfate, the terminal step in the oxidative degradation of cysteine and methionine"].
- Belaidi & Schwarz 2013 is cited by UniProt for human SUOX CATALYTIC ACTIVITY and
  COFACTOR (Mo-MPT). The cached **abstract is about gephyrin/Moco synthesis** and does
  not mention SUOX; `full_text_available: false`. The SUOX assay is in the full text,
  which was read by the UniProt/GOA curator. Do not overrule (ACCEPT the IDA).

## Cofactors and domains (two-cofactor, homodimeric enzyme)

- Heme b (cytochrome b5-type domain, res 82–161), bound non-covalently, 1 per subunit
  [file:human/SUOX/SUOX-uniprot.txt: "Binds 1 heme b (iron(II)-protoporphyrin IX) group non-covalently"].
  Heme axial residues His118/His143 resolved in the 1.2 Å crystal structure of the human
  cytochrome b5 domain (PDB 1MJ4) [file:human/SUOX/SUOX-uniprot.txt: "X-RAY CRYSTALLOGRAPHY (1.2 ANGSTROMS) OF 79-160 IN COMPLEX WITH HEME"].
- Molybdenum cofactor (Mo-molybdopterin, Mo-MPT), Moco domain (res 175–401), 1 per subunit
  [file:human/SUOX/SUOX-uniprot.txt: "Binds 1 Mo-molybdopterin (Mo-MPT) cofactor per subunit"].
- Homodimer [file:human/SUOX/SUOX-uniprot.txt: "Homodimer."] with a C-terminal
  dimerization region (res 402–538).
- Domain architecture: N-terminal cytochrome b5 heme domain + central Moco/oxidoreductase
  domain + C-terminal dimerization (E-set/Ig) domain (InterPro IPR001199, IPR005066,
  IPR000572; PANTHER PTHR19372:SF7 SULFITE OXIDASE).

## Localization

- **Mitochondrial intermembrane space** (IMS)
  [file:human/SUOX/SUOX-uniprot.txt: "Mitochondrion intermembrane space"], imported via
  an N-terminal mitochondrial transit peptide (res 1–79).
- GOA also carries an ISS `mitochondrial inner membrane` (GO:0005743) transferred from
  the chicken orthologue Q07116, and a Reactome TAS `mitochondrial matrix` (GO:0005759).
  Both conflict with the authoritative UniProt IMS statement; SUOX is a soluble IMS
  enzyme, not matrix or inner-membrane-anchored. Marked as over-annotations / non-core.
- HTP `mitochondrion` (GO:0005739, PMID:34800366) and IBA `mitochondrion` are correct but
  less specific than IMS.

## Secondary / proposed activity: nitrite reductase

- Under hypoxia/ischemia SUOX can run in reverse and reduce nitrite to nitric oxide (NO)
  [file:human/SUOX/SUOX-uniprot.txt: "Can run in reverse direction and reduce nitrite to"].
- Demonstrated electrochemically for human SUOX (HSO):
  [PMID:41337830 "The Mo-dependent enzyme human sulfite oxidase (HSO)"]
  [PMID:41337830 "HSO can act as an effective nitrite reductase with a KM"] (KM 3.5 mM, pH 7;
  a heme-free variant behaves similarly, implicating the Mo centre).
- GOA has an IDA `nitrite reductase activity` (GO:0098809, PMID:41337830). This is a real,
  experimentally supported activity but a secondary/proposed physiological role
  (sulfite is the only established physiological substrate); kept as non-core.

## Disease

- Isolated sulfite oxidase deficiency (ISOD; MIM:272300): autosomal recessive, severe
  neonatal encephalopathy, intractable seizures, ectopia lentis, early death; clinically
  overlaps molybdenum cofactor deficiency
  [file:human/SUOX/SUOX-uniprot.txt: "Sulfite oxidase deficiency, isolated (ISOD)"].
- Many missense variants characterized (R160Q/Arg-217 numbering in precursor, etc.),
  several at the Mo/substrate site (Kisker 1997, PMID:9428520).

## Protein-binding (IPI) annotations

- Two bare `protein binding` (GO:0005515) IPI annotations from high-throughput interactome
  screens: PMID:25910212 (edgotyping of Mendelian-disease alleles) and PMID:32296183
  (HuRI human binary interactome map). Both are large-scale Y2H/systematic maps; the
  ~90 IntAct partners in the UniProt record (transcription factors, keratins, etc.) are
  not biologically coherent for a mitochondrial IMS metabolic enzyme. Uninformative bare
  "protein binding" — marked over-annotated (not removed, per policy for IPI).

## Annotation review summary (aspect / term / decision)

- MF GO:0008482 sulfite oxidase activity — CORE. ACCEPT the IDA (PMID:23163752); IBA/IEA
  redundant copies ACCEPT / MARK_AS_OVER_ANNOTATED as duplicates; TAS (PMID:9428520) ACCEPT.
- MF GO:0043546 molybdopterin cofactor binding — CORE (IDA PMID:23163752; IBA/IEA). ACCEPT.
- MF GO:0020037 heme binding — CORE (IBA + IEA InterPro; structure PMID:12832761). ACCEPT.
- MF GO:0030151 molybdenum ion binding — correct but subsumed by MoCo binding; non-core.
- MF GO:0016491 oxidoreductase activity — correct but too general (parent of sulfite
  oxidase activity); over-annotated.
- MF GO:0098809 nitrite reductase activity — secondary activity; KEEP_AS_NON_CORE.
- MF GO:0005515 protein binding (x2) — uninformative HT interactome; over-annotated.
- BP GO:0006790 sulfur compound metabolic process — correct but general; MODIFY toward
  GO:0000098 sulfur amino acid catabolic process.
- CC GO:0005758 mitochondrial intermembrane space — CORE location. ACCEPT.
- CC GO:0005743 mitochondrial inner membrane — contradicts UniProt IMS; over-annotated.
- CC GO:0005759 mitochondrial matrix (Reactome) — contradicts UniProt IMS; over-annotated.
- CC GO:0005739 mitochondrion (IBA + HTP) — correct but less specific than IMS; non-core.
