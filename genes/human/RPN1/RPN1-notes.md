# RPN1 (Ribophorin I) — curation notes

UniProt: P04843 (RPN1_HUMAN). RecName: Dolichyl-diphosphooligosaccharide--protein
glycosyltransferase subunit 1; AltName: Ribophorin I / Ribophorin-1. Human (NCBITaxon:9606).
HGNC:10381. 607 aa precursor.

## Core biology (from UniProt P04843 and primary literature)

RPN1 is a **non-catalytic subunit of the oligosaccharyltransferase (OST) complex**, the
ER-membrane enzyme that carries out the first committed step of protein N-glycosylation.

- FUNCTION (UniProt): "Subunit of the oligosaccharyl transferase (OST) complex that
  catalyzes the initial transfer of a defined glycan (Glc(3)Man(9)GlcNAc(2) in eukaryotes)
  from the lipid carrier dolichol-pyrophosphate to an asparagine residue within an
  Asn-X-Ser/Thr consensus motif in nascent polypeptide chains, the first step in protein
  N-glycosylation" [file:human/RPN1/RPN1-uniprot.txt]. "N-glycosylation occurs
  cotranslationally and the complex associates with the Sec61 complex at the
  channel-forming translocon complex" [file:human/RPN1/RPN1-uniprot.txt]. "All subunits are
  required for a maximal enzyme activity (By similarity)" [file:human/RPN1/RPN1-uniprot.txt].
- PATHWAY (UniProt): "Protein modification; protein glycosylation." [file:human/RPN1/RPN1-uniprot.txt]
- SUBUNIT (UniProt): "Component of the oligosaccharyltransferase (OST) complex ... OST exists
  in two different complex forms which contain common core subunits RPN1, RPN2, OST48, OST4,
  DAD1 and TMEM258, either STT3A or STT3B as catalytic subunits" [file:human/RPN1/RPN1-uniprot.txt].
  RPN1 is thus a **shared core subunit of both OST-A (STT3A) and OST-B (STT3B)** complexes.
  In STT3A assembly, "Subcomplex 1 contains RPN1 and TMEM258" [file:human/RPN1/RPN1-uniprot.txt].
- LOCATION (UniProt): "Endoplasmic reticulum membrane ... Single-pass type I membrane
  protein" [file:human/RPN1/RPN1-uniprot.txt]. Topology: lumenal 24-438, single TM 439-457,
  cytoplasmic 458-607 [file:human/RPN1/RPN1-uniprot.txt]. Historically ribophorin I is a
  **rough-ER-specific** glycoprotein [PMID:3034581 title "highly conserved rough endoplasmic
  reticulum-specific glycoproteins"].
- SIMILARITY (UniProt): "Belongs to the OST1 family." [file:human/RPN1/RPN1-uniprot.txt]
  Yeast ortholog = Ost1p; InterPro IPR007676 Ribophorin_I; Pfam PF04597.

## Substrate-recognition / facilitator role

Ribophorin I is not the catalytic subunit (STT3A/STT3B are). Functional data indicate it acts
as a **substrate-specific facilitator / chaperone** that promotes glycosylation of selected
substrates by presenting the nascent chain to the STT3 catalytic subunit:

- Wilson & High 2007: "ribophorin I dramatically enhances the N-glycosylation of selected
  membrane proteins and provide evidence that it is not essential for N-glycosylation per se
  ... We propose a new model for OST function where ribophorin I acts as a chaperone or escort
  to promote the N-glycosylation of selected substrates by the catalytic STT3 subunits."
  [PMID:17264154] — RNAi knockdown, substrate-specific; supports IMP for protein N-linked
  glycosylation (GO:0006487).
- Cryo-EM (Ramirez, Kowal, Locher 2019): "In OST-A, interactions with TMEM258 and STT3A allow
  ribophorin-I to form a four-helix bundle that can bind to a translating ribosome, whereas the
  equivalent region is disordered in OST-B." [PMID:31831667] — structural basis for RPN1's role
  in cotranslational substrate delivery in the STT3A complex.

## OST complex membership evidence

- Kumar, Heinemann & Ozols 1998: purified human lymphocyte OST; "the enzyme preparation
  contained four predominant proteins. N-terminal sequence analysis identified the proteins as
  ribophorin I, ribophorin II (doublet), and a 50-kDa homologue of Wbp1" [PMID:9642163] —
  IDA membership of OST complex + involvement in N-glycosylation (biochemical purification).
- Shibatani et al. 2005: mammalian OST proteomics; "All known mammalian OST subunits (STT3-A,
  ribophorin I, ribophorin II, OST48, and DAD1) were present in all complexes." [PMID:15835887]
  — TAS support for RPN1 contributing to the OST glycotransferase activity (GO:0004579).
- Cherepanova et al. 2014 [PMID:25135935] and Dumax-Vorzet et al. 2013 [PMID:23606741]:
  identification of RPN1 in the OST complex (cited in UniProt SUBUNIT).
- Cryo-EM OST-A/OST-B 2019 [PMID:31831667]: RPN1 assigned in both OST-A and OST-B structures →
  supports oligosaccharyltransferase complex A (GO:0160226) and B (GO:0160227) membership.
- Lampson et al. 2024 [PMID:38670073]: CRISPR/cryo-EM study of OST-A (STT3A) druggable pocket;
  RPN1 modeled as OST-A subunit → additional IDA for GO:0160226.

## Interactions (IPI, GO:0005515 protein binding)

These are consistent with OST membership and its accessory/quality-control roles, but "protein
binding" is uninformative as a molecular function on its own:
- STT3A (P46977) / STT3B (Q8TCJ2): the two catalytic OST subunits [PMID:19167329, PMID:30021884,
  PMID:35271311] — RPN1 is in the same complex.
- MLEC / malectin (Q14165): "malectin formed a stable complex with an endoplasmic
  reticulum-resident transmembrane protein, ribophorin I ... ribophorin I may function as a
  chaperone that recognizes misfolded proteins" [PMID:22988243]; also detected in interactome/
  proteomic screens [PMID:30021884, PMID:31831667, PMID:35271311]. Suggests RPN1 links OST to a
  glycoprotein-folding QC pathway (malectin recognizes G2M9 N-glycans on misfolded glycoproteins).
- TMEM258 (P61165): OST core subunit; "TMEM258 is a required component of the
  oligosaccharyltransferase complex and is essential for N-linked protein glycosylation"
  [PMID:27974209]; RPN1+TMEM258 = STT3A "Subcomplex 1" [file:human/RPN1/RPN1-uniprot.txt].
- SGTA (O43765), UBQLN1 (Q9UMX0), CAMLG (P49069), KRTAP1-3 (Q8IUG1), POMK (Q9H5K3): high-
  throughput binary/AP-MS interactome or QC-associated interactors [PMID:25416956, PMID:31515488,
  PMID:32296183, PMID:32707033]. Retain as background; not core functions.

## Post-translational modifications / regulation (context, not GO-reviewed here)

- N-glycosylated at Asn-299 [PMID:19159218]; acetyl-Lys187 [PMID:19608861]; SUMO2 at Lys538
  [PMID:25114211].
- Ubiquitinated by ECS(ASB11) [PMID:24337577] and by RNF128, driving degradation and thereby
  regulating N-glycosylation [PMID:39567208, file:human/RPN1/RPN1-uniprot.txt].
- Ufmylated by UFL1 during ER stress, promoting reticulophagy [PMID:32160526].

## Localization annotations to scrutinize

- ER / ER membrane / rough ER: correct, core (UniProt, Reactome, ISS, HPA).
- **cytosol** (GO:0005829, HPA IDA, GO_REF:0000052): RPN1 is a type-I ER membrane protein with a
  short cytoplasmic tail (458-607); a bulk "cytosol" localization is not its functional
  compartment. Keep as non-core / over-annotation (likely diffuse IF signal or the cytoplasmic
  tail). Do not remove (experimental IDA) — MARK_AS_OVER_ANNOTATED.
- **melanosome** (GO:0042470): from melanosome-fraction proteomics [PMID:12643545, PMID:17081065];
  ER contaminant of melanosome preps rather than a genuine RPN1 functional site → non-core.
- **membrane** (GO:0016020): true but generic parent of ER membrane → non-core / over-annotated.

## Molecular function annotations to scrutinize

- **RNA binding** (GO:0003723, HDA, PMID:22658674): from a global mRNA-interactome capture
  screen (HeLa). RPN1 is an ER-membrane glycosylation subunit with no known sequence-specific
  RNA function; the four-helix cytoplasmic bundle contacts the *translating ribosome*
  [PMID:31831667], which plausibly explains crosslinking to mRNA in interactome capture. Not a
  bona fide molecular function → MARK_AS_OVER_ANNOTATED (do not remove; HDA/experimental).
- **protein binding** (GO:0005515, many IPI): uninformative; keep as non-core, do not remove.
- **dolichyl-diphosphooligosaccharide-protein glycotransferase activity** (GO:0004579,
  contributes_to, TAS PMID:15835887): correct modeling — RPN1 contributes to the complex's
  catalytic activity without being catalytic itself. ACCEPT (contributes_to qualifier is exactly
  right for a non-catalytic subunit).

## Core function model

- in_complex: oligosaccharyltransferase complex (GO:0008250)
- contributes_to_molecular_function: dolichyl-diphosphooligosaccharide-protein glycotransferase
  activity (GO:0004579)
- involved_in (biological process): protein N-linked glycosylation (GO:0006487)
- located_in: endoplasmic reticulum membrane (GO:0005789)
</content>
</invoke>
