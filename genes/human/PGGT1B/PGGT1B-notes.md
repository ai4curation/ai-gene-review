# PGGT1B (P53609) review notes

## Identity and gene product

- Human gene **PGGT1B** (HGNC:8895), UniProt **P53609** (PGTB1_HUMAN), 377 aa, chromosome 5.
- Product: **Geranylgeranyl transferase type-1 subunit beta** (GGTase-I-beta), EC 2.5.1.59
  [file:human/PGGT1B/PGGT1B-uniprot.txt "RecName: Full=Geranylgeranyl transferase type-1 subunit beta"].
- This is the **catalytic beta subunit** of protein geranylgeranyltransferase type I (GGTase-I).
  The functional enzyme is a **heterodimer of FNTA (alpha, shared with farnesyltransferase) and
  PGGT1B (beta)** [file:human/PGGT1B/PGGT1B-uniprot.txt "SUBUNIT: Heterodimer of FNTA and PGGT1B. PGGT1B mediates interaction"].

## Core molecular function

- GGTase-I transfers a **geranylgeranyl (C20 isoprenoid) group from geranylgeranyl diphosphate (GGPP)**
  to the cysteine of a C-terminal **CAAX motif** (X typically Leu/Phe), targeting substrates for membrane
  association [file:human/PGGT1B/PGGT1B-uniprot.txt "Catalyzes the transfer of a geranyl-geranyl moiety from"].
- The modified cysteine is at the fourth position from the C-terminus; consensus is Cys-aliphatic-aliphatic-X
  [file:human/PGGT1B/PGGT1B-uniprot.txt "aliphatic-aliphatic-X. Known substrates include RAC1, RAC2, RAP1A and"].
- Catalytic reaction: geranylgeranyl diphosphate + L-cysteinyl-[protein] = S-geranylgeranyl-L-cysteinyl-[protein]
  + diphosphate; EC 2.5.1.59; RHEA:21240
  [file:human/PGGT1B/PGGT1B-uniprot.txt "geranylgeranyl-L-cysteinyl-[protein] + diphosphate;"].
- **Zinc metalloenzyme**: binds one catalytic Zn2+ per subunit; the Zn2+ coordinating residues (Asp269, Cys271,
  His321) reside on the beta (PGGT1B) subunit
  [file:human/PGGT1B/PGGT1B-uniprot.txt "Binds 1 zinc ion per subunit. {ECO:0000250|UniProtKB:P53610};"].
  Mg2+ is a second cofactor. FT BINDING residues 269/271/321 coordinate Zn(2+) (catalytic); residues 219-221,
  263-266, 272-275 bind GGPP.
- Best original characterization: Zhang et al. 1994 (PMID:8106351) cloned rat and human GGTase-I beta,
  showed it is composed of a 48-kDa alpha subunit and 43-kDa beta subunit, and that the alpha subunit is
  shared with farnesyltransferase [PMID:8106351 "The enzyme is composed of a 48-kilodalton alpha subunit and a 43-kilodalton beta subunit."].
  Yeast counterpart is CDC43 [PMID:8106351 "gene CDC43 is the yeast counterpart of the mammalian GGTase-I beta subunit."].

## Substrates and biological role

- Known direct substrates include the Rho-family / Ras-superfamily small GTPases **RAC1, RAC2, RAP1A, RAP1B**
  (also Rho, Cdc42) — CAAX proteins with X = Leu/Phe
  [file:human/PGGT1B/PGGT1B-uniprot.txt "aliphatic-aliphatic-X. Known substrates include RAC1, RAC2, RAP1A and"].
- Biological process: **protein geranylgeranylation** (GO:0018344), a step in CAAX-box protein maturation
  that governs membrane targeting and signaling of small GTPases.
- Reactome documents GGTase-I (FNTA:PGGT1B) geranylgeranylating the guanylate-binding proteins **GBP2**
  (C588, CNIL box) and **GBP5** (C583, CVLL box) in host defense, enabling their membrane association
  [Reactome:R-HSA-9947999; Reactome:R-HSA-9954195].

## Structure / catalytic mechanism (PMID:16893176)

- Terry, Casey & Beese 2006 (crystallographic + kinetic) analyzed the isoprenoid specificity of GGTase-I
  vs farnesyltransferase (FTase), showing specificity is determined by two beta-subunit residues
  [PMID:16893176 "this specificity is dependent upon two enzyme residues in the beta subunits of"].
  This is the IDA source for GGTase-I activity / complex / geranylgeranylation on P53609. Note the abstract
  foregrounds FTase-to-GGTase conversion, but the full text characterizes GGTase-I beta (T49beta and F324beta)
  and the recombinant enzyme; the curator (UniProt) read the full text.

## Protein interactions (GO:0005515 IPI annotations)

- All five bare "protein binding" IPI annotations (PMID:24981860, 31209342, 32296183, 33961781, 40205054)
  in GOA are IntAct records whose WITH/FROM is **UniProtKB:P49354 = FNTA**, i.e. they all capture the
  PGGT1B–FNTA heterodimer interaction (the biologically meaningful partner). UniProt records this same
  interaction with NbExp=12 [file:human/PGGT1B/PGGT1B-uniprot.txt "P53609; P49354: FNTA; NbExp=12; IntAct=EBI-8456634, EBI-602336;"].
  Several of these papers are large-scale interactome/proteomics screens (Cell Rep 2014 chromatin AP-MS;
  Nat Struct Mol Biol 2019 GGTase3; Nature 2020 HuRI binary interactome; Cell 2021 BioPlex; Nature 2025
  multimodal cell maps) — the FNTA edge is the retained annotation. These are non-core "protein binding":
  the partner is informative (structural heterodimer), but GO:0005515 itself is uninformative and should be
  MARK_AS_OVER_ANNOTATED per policy (never REMOVE an IPI).
- PMID:31209342 (Kuchay et al., GGTase3) is background on the prenylation code; it does NOT report a
  functional PGGT1B assay (it describes a distinct enzyme, GGTase3 = PTAR1:RabGGTB). The FNTA edge is
  IntAct-curated from it.

## Complex / location

- Complex: **CAAX-protein geranylgeranyltransferase complex** (GO:0005953) = the FNTA:PGGT1B GGTase-I
  heterodimer (ComplexPortal CPX-2157) [file:human/PGGT1B/PGGT1B-uniprot.txt "ComplexPortal; CPX-2157; Protein geranylgeranyl transferase type I complex."].
- Location: cytosol (GO:0005829), consistent with soluble GGTase-I acting on cytosolic substrate GTPases
  prior to their membrane targeting (Reactome TAS).

## Curation decisions summary

- Core MF: **GO:0004662 CAAX-protein geranylgeranyltransferase activity** (has-activity as the catalytic
  subunit of the heterodimer). GO:0004661 (parent) and GO:0008318 (protein prenyltransferase activity) and
  GO:0003824 (catalytic activity) are correct-but-general parents.
- Core cofactor MF: **GO:0008270 zinc ion binding** (catalytic Zn2+ on the beta subunit).
- Core BP: **GO:0018344 protein geranylgeranylation**.
- Core complex: **GO:0005953 CAAX-protein geranylgeranyltransferase complex** (in_complex).
- `contributes_to` qualifier on the IBA MF is appropriate — the activity is a property of the heterodimer,
  but PGGT1B carries the catalytic Zn2+ and the isoprenoid/peptide binding sites, so it is more than a
  purely structural contributor; still, the complex-level activity is shared with FNTA, so
  contributes_to_molecular_function is used in core_functions.
</content>
