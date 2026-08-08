# THTPA (Thiamine-triphosphatase, ThTPase) — review notes

UniProt: Q9BU02 (THTPA_HUMAN); HGNC:18987; GeneID 79178; chromosome 14. EC=3.6.1.28.
230 aa; single CYTH domain (residues 5–201). Evidence at protein level (PE 1).

## Core biology (grounded in UniProt file)

- **Function**: "Hydrolase highly specific for thiamine triphosphate (ThTP)."
  [file:human/THTPA/THTPA-uniprot.txt] (FUNCTION line, ECO:0000269|PubMed:11827967, PubMed:23707715).
- **Catalytic activity**: "thiamine triphosphate + H2O = thiamine diphosphate + phosphate + H(+)";
  Rhea:RHEA:11744; EC=3.6.1.28 [file:human/THTPA/THTPA-uniprot.txt]. So the enzyme converts ThTP → ThDP (thiamine diphosphate / TDP) + Pi.
- **Cofactor**: "Name=Mg(2+)"; "Binds 1 Mg(2+) ion per subunit." [file:human/THTPA/THTPA-uniprot.txt]
  (ECO:0000269|PubMed:23707715). Multiple Mg2+-binding residues annotated (BINDING 7, 9, 145, 157, 159).
- **Kinetics**: "KM=8 uM for thiamine triphosphate"; "Vmax=59 umol/min/mg enzyme" [file:human/THTPA/THTPA-uniprot.txt]
  — high affinity, consistent with a physiological role keeping cellular ThTP low.
- **Subunit**: "Monomer." [file:human/THTPA/THTPA-uniprot.txt] (PubMed:23707715).
- **Subcellular location**: "Cytoplasm" [file:human/THTPA/THTPA-uniprot.txt] (ECO:0000269|PubMed:11827967).
- **Tissue specificity**: "Widely expressed but at a low level." [file:human/THTPA/THTPA-uniprot.txt]
- **Family**: "Belongs to the ThTPase family." [file:human/THTPA/THTPA-uniprot.txt]; CYTH / triphosphate-tunnel
  metalloenzyme (TTM) superfamily (CDD cd07758 ThTPase; Pfam PF01928 CYTH; PROSITE PS51707 CYTH).
- **Structure**: X-ray structures 3BHD (1.50 Å) and 3TVL (2.30 Å, complex with triphosphate). CYTH tunnel fold.

## Key references

- **PMID:11827967** (Lakaye et al. 2002, J Biol Chem) — cached abstract only (`full_text_available: false`).
  First molecular characterization of a specific mammalian ThTPase. Purified soluble ThTPase from calf brain,
  a "24-kDa monomer, hydrolyzing ThTP with virtually absolute specificity." Identified the human ortholog
  (MGC2652 / this 230-aa protein), expressed recombinant human enzyme in E. coli (ThTPase activity, ThTP-specific),
  and showed the mRNA is "expressed in most human tissues but at relatively low levels."
  Supports FUNCTION, IDA thiamine-triphosphatase activity, cytoplasmic location, tissue specificity.
  Abstract quote: "hydrolyzing ThTP with virtually absolute specificity"; "The mRNA was expressed in most human
  tissues but at relatively low levels."
- **PMID:23707715** (Delvaux et al. 2013, BBA) — NOT cached locally. Per the UniProt record, this is the X-ray
  crystallography (2.30 Å) paper establishing CATALYTIC ACTIVITY, FUNCTION, COFACTOR (Mg2+), kinetics (KM, Vmax),
  monomeric SUBUNIT, and extensive active-site mutagenesis (K11, D37, Y39, W53, K65, Y79, E81, D147, K193).
  Underpins the ECO:0000269 experimental FUNCTION/COFACTOR/kinetic statements above. Not cited in GOA rows,
  so used only as UniProt-sourced provenance, not quoted as a publication.
- **PMID:32296183** (Luck et al. 2020, "A reference map of the human binary protein interactome", HuRI) —
  cached full text. Systematic Y2H interactome; source of the IntAct interaction Q9BU02 (THTPA) – O43711 (TLX3).
  Bare "protein binding" (GO:0005515) IPI; high-throughput binary interaction, no functional context for THTPA.
- **Reactome R-HSA-965067** "THTPA:Mg2+ hydrolyzes ThTP to TDP" — the ThTPase reaction in the human
  Vitamin B1 (thiamin) metabolism pathway (R-HSA-196819). Source of the TAS cytosol location.

## GO review reasoning

- **Core MF** = GO:0050333 thiamine triphosphate phosphatase activity (IDA from PMID:11827967; also IBA, IEA).
  This is the defining, experimentally established activity (recombinant human enzyme; crystal structure + kinetics).
- **Mg2+ binding** GO:0000287 — supported by COFACTOR (Mg2+, 1 per subunit) and BINDING residues in UniProt;
  contributes to catalysis. IBA/ISS/IEA — accept as a genuine molecular function feature (non-core relative to the
  triphosphatase activity, but real).
- **Core BP**: the enzyme's direct product is thiamine diphosphate (ThDP), so GO:0042357 (thiamine diphosphate
  metabolic process) is the most precise BP; GO:0042723 (thiamine-containing compound metabolic process) and
  GO:0006772 (thiamine metabolic process) are broader parents. GO:0006772 is a child of GO:0042723 (verified in
  go.db entailed_edge). All three describe the same underlying vitamin-B1 phosphate homeostasis role.
- **GO:0016311 dephosphorylation** (IDA, PMID:11827967) — accurate high-level BP for a phosphatase; kept as
  non-core (the specific triphosphatase activity + thiamine BP terms are more informative).
- **GO:0016787 hydrolase activity** (TAS) — correct but a parent of GO:0050333; over-general, MODIFY to GO:0050333.
- **GO:0006091 generation of precursor metabolites and energy** (NAS, PMID:11827967) — weak/dubious. ThTP's role
  as a phosphate donor and possible energy-related signaling was speculative in 2002; ThTPase hydrolyzes ThTP
  (removes it) rather than generating energy metabolites. NAS + broad term = over-annotation.
- **Cytosol/cytoplasm** GO:0005829 / GO:0005737 — supported (UniProt Cytoplasm; Reactome cytosol). Correct CC.
- **GO:0005515 protein binding** (IPI, PMID:32296183) — single HuRI Y2H interaction with TLX3; uninformative;
  MARK_AS_OVER_ANNOTATED per policy (never REMOVE an IPI protein-binding).

No disease association established for THTPA (MIM:611612 gene only). No knockout phenotype in the literature we can
access. Physiological role inferred: regulator of cellular ThTP steady-state levels (thiamine phosphate homeostasis).
