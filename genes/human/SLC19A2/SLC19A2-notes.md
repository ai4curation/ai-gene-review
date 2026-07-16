# SLC19A2 (Thiamine transporter 1 / THTR1) — review notes

UniProt: O60779 (S19A2_HUMAN), 497 aa, gene SLC19A2 (synonyms THT1, TRMA), human (NCBITaxon:9606).

## Summary of function

SLC19A2 encodes **thiamine transporter 1 (THTR-1 / ThTr-1)**, a polytopic plasma-membrane
solute carrier of the SLC19 / reduced-folate-carrier (RFC) family (TCDB 2.A.48.1.2) that
mediates **high-affinity cellular uptake of thiamine (vitamin B1)**. It is the founding
mammalian thiamine transporter, identified by positional cloning of the gene mutated in
thiamine-responsive megaloblastic anemia syndrome (TRMA / Rogers syndrome).

- "the gene SLC19A2 ... encodes the first known mammalian thiamine transporter, which we
  designate thiamine transporter-1 (THTR-1)" [PMID:10391222, abstract].
- "We have isolated a cDNA from human placenta, which, when expressed heterologously in
  mammalian cells, mediates the transport of the water-soluble vitamin thiamine. The cDNA
  codes for a protein of 497 amino acids containing 12 putative transmembrane domains ...
  the cDNA induces the transport of thiamine (K(t) = 2.5 +/- 0.6 microM) in a
  Na(+)-independent manner ... stimulated by an outwardly directed H(+) gradient ...
  the transporter is specific to thiamine" [PMID:10542220, abstract].
- UniProt FUNCTION: "High-affinity transporter for the intake of thiamine ... Mediates
  H(+)-dependent pyridoxine transport" [file:human/SLC19A2/SLC19A2-uniprot.txt].
- UniProt catalytic activity (thiamine): `thiamine(out) + H(+)(in) = thiamine(in) + H(+)(out)`
  (Rhea:71271) — i.e. thiamine/H+ **antiport**, consistent with the outwardly-directed H+
  gradient dependence [file:human/SLC19A2/SLC19A2-uniprot.txt]. NOTE: because the mechanism
  is antiport, GO:0034215 "thiamine:proton symporter activity" (which is defined as symport,
  H+ in with thiamine) does NOT match; the generic GO:0015234 is the correct MF.

## Topology / structure

- 497 aa, 12 transmembrane helices; N- and C-termini cytoplasmic
  [file:human/SLC19A2/SLC19A2-uniprot.txt, FT TRANSMEM x12].
- Cryo-EM structures 8Z7Z / 8Z80 (2024) resolved (PDB DR lines).
- N-glycosylated at Asn63 and Asn314 (predicted); N-acetyl-Met1; phospho-Ser222.
- SIMILARITY: "Belongs to the reduced folate carrier (RFC) transporter (TC 2.A.48) family"
  [file:human/SLC19A2/SLC19A2-uniprot.txt].

## Substrates

- **Thiamine (vitamin B1)** — primary, high-affinity substrate. KM ≈ 2.5 µM (PMID:10542220),
  2.83 µM at pH 7.4 / 3.66 µM at pH 5.5 (PMID:33008889) [file:human/SLC19A2/SLC19A2-uniprot.txt].
- **Pyridoxine (vitamin B6)** — secondary, lower-affinity, H+/pH-dependent substrate.
  "The stable expression of SLC19A2 and SLC19A3 in MDCKII cells ... led to a significant
  induction in pyridoxine uptake at pH 5.5 ... with an apparent Km of 37.8 and 18.5 μm, for
  SLC19A2 and SLC19A3, respectively" [PMID:33008889, abstract]. KM=37.8 µM pyridoxine
  [file:human/SLC19A2/SLC19A2-uniprot.txt].
- Unlike its paralog SLC19A1 (reduced folate carrier), SLC19A2 is **specific to thiamine**
  (not folate): "the cDNA-induced thiamine transport is not inhibited by other organic
  cations ... the transporter is specific to thiamine" [PMID:10542220]. The historic
  "member of the folate transporter family" naming reflects sequence homology to RFC, not
  folate-transport activity. The NAS GO:0008517 folic acid transmembrane transporter
  activity (and the IEA GO:0015884 folic acid transport inferred from it) is therefore a
  family-homology over-annotation, contradicted by the same paper's substrate-specificity
  data.

### Pyridoxine transport in human SLC19A2 is directly assayed (not only in SLC19A3)
- PMID:35724964 (full text available) directly tests hSLC19A2: an hSLC19A2 mutant with 7
  residues swapped to mouse Slc19a3 counterparts loses pyridoxine transport but retains
  thiamine transport — "we prepared an hSLC19A2 mutant in which all seven residues were
  replaced with their mSlc19a3 counterparts (hSLC19A2-ma3-7AA) and examined pyridoxine
  transport by the mutant. As expected, the specific uptake of pyridoxine was reduced to
  an undetectable level" and "The thiamine uptake activity was, on the other hand,
  unchanged in the mutant" [PMID:35724964, full text]. This is the IMP basis for the
  thiamine-transport annotation (thiamine uptake retained across all mutants).
- PMID:35512554 (rat/mouse ortholog paper) also reports human SLC19A2 assays: "both rat and
  mouse Slc19a2 can transport pyridoxine ... all SLC19A2/3 orthologs were capable of thiamine
  transport" [PMID:35512554, abstract]; human ortholog included as reference.

## Localization

- Plasma / cell membrane (multi-pass). UniProt SUBCELLULAR LOCATION: "Cell membrane"
  (ECO:0000269|PubMed:21836059) [file:human/SLC19A2/SLC19A2-uniprot.txt]. Reactome
  R-HSA-199626: "SLC19A2 (THTR1) and SLC19A3 (THTR2), associated with the plasma membrane".
- Directly localized to plasma membrane by IDA in PMID:21836059 (GOA row 29).

## Interactions

- **TSPAN1** (tetraspanin-1, O60635): interacts with THTR-1 and stabilizes it (extends
  half-life from 6 h to 12 h). "Tspan-1, interacts with hTHTR-1 ... Coexpression of
  hTspan-1 ... led to a significant decrease in the rate of degradation of hTHTR-1"
  [PMID:21836059, abstract]. UniProt SUBUNIT: "Interacts with TSPAN1; this interaction
  increases the stability of SLC19A2" [file:human/SLC19A2/SLC19A2-uniprot.txt]. This is a
  real, functional interaction, but the GOA term is the uninformative bare "protein binding"
  (GO:0005515). A specific MF (protein stabilization / chaperone-binding partner) would be
  more informative but no established MF term is well-supported; kept as non-core/over-annotated.
- **ENDOD1** (O94919) and **TSPAN1** appear in the UniProt INTERACTION section (IntAct).
  The two large-scale interactome IPI annotations (PMID:33961781 Huttlin BioPlex;
  PMID:40355756 Frommelt SLC interactome) are the source of the ENDOD1 (O94919) bare
  protein-binding calls; neither cached full text names SLC19A2/O60779 in-line (pairs are in
  supplementary networks). High-throughput; uninformative bare protein-binding → over-annotated.

## Disease

- **Thiamine-responsive megaloblastic anemia syndrome (TRMA / Rogers syndrome)**, MIM 249270,
  autosomal recessive: megaloblastic anemia + diabetes mellitus + sensorineural deafness.
  UniProt DISEASE (ECO:0000269|PubMed:10391221, 10391222, 10874303)
  [file:human/SLC19A2/SLC19A2-uniprot.txt]. TRMA variants include D93H, S143F, G172D.

## Tissue expression

- Ubiquitous; most abundant in skeletal and cardiac muscle; medium in placenta, heart,
  liver, kidney [file:human/SLC19A2/SLC19A2-uniprot.txt, TISSUE SPECIFICITY].

## Annotation review reasoning

Core MF/BP/CC (thiamine transmembrane transporter activity GO:0015234; thiamine transport
GO:0015888; thiamine transmembrane transport GO:0071934; plasma membrane GO:0005886) are all
ACCEPT — strongly supported by IDA/IMP + UniProt, correct even where the specific row is IEA/IBA/ISS
(do not over-annotate a gene's own core function just because a redundant electronic copy exists).

- Pyridoxine transport (GO:0031923) — real secondary function, IDA-supported (PMID:33008889),
  human protein directly assayed; ACCEPT (as non-core relative to thiamine). Only MF-level
  gap: no pyridoxine transmembrane transporter activity (GO:0031928) MF annotation exists →
  propose as new term.
- Folic acid transport / folic acid transmembrane transporter activity (GO:0015884 IEA;
  GO:0008517 NAS) — family-homology artifact contradicted by PMID:10542220 substrate
  specificity. GO:0015884 is a clearly-wrong logically-inferred IEA (from the NAS folate MF)
  → REMOVE. GO:0008517 is NAS (author statement, not experiment) but not an experimental
  code → MARK_AS_OVER_ANNOTATED (do not lose provenance; it is the origin of the folate story).
- vitamin transport / vitamin transmembrane transporter activity (GO:0051180, GO:0090482 IEA)
  — correct but very general parents of the specific thiamine terms; KEEP_AS_NON_CORE.
- membrane (GO:0016020 IEA InterPro; GO:0016020 NAS) — correct but generic parent of plasma
  membrane; KEEP_AS_NON_CORE.
- spermatogenesis (GO:0007283 IEA from mouse ortholog Q9EQN9 via Ensembl Compara) —
  phenotype-derived electronic transfer from mouse; not a molecular function of a thiamine
  transporter and no human evidence; MARK_AS_OVER_ANNOTATED (electronic phenotype
  over-propagation; not experimental so does not require ACCEPT).
- thiamine-containing compound metabolic process (GO:0042723 TAS Reactome) — SLC19A2 imports
  thiamine, enabling downstream ThPP metabolism; broad but defensible as the pathway context;
  KEEP_AS_NON_CORE.
- protein binding (GO:0005515) x3 IPI — bare uninformative term; MARK_AS_OVER_ANNOTATED
  (never REMOVE an IPI protein-binding call).

## Proposed new terms
- GO:0031928 pyridoxine transmembrane transporter activity (MF) — currently only the BP
  GO:0031923 pyridoxine transport is annotated; the MF is directly supported by IDA
  (PMID:33008889) and mutagenesis (PMID:35724964).
</content>
</invoke>
