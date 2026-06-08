# PPIB (cyclophilin B / CypB / CYPB) research notes

UniProt P23284. ER-lumenal peptidyl-prolyl cis-trans isomerase (PPIase), EC 5.2.1.8. Cyclophilin-type.

## Core MF
- PPIase: catalyzes cis-trans isomerization of proline imidic peptide bonds.
  - [file:human/PPIB/PPIB-uniprot.txt "PPIase that catalyzes the cis-trans isomerization of proline imidic peptide bonds in oligopeptides and may therefore assist protein folding."]
  - [PMID:20676357 structural/biochem characterization of human cyclophilin family PPIases; IDA PPIase activity; inhibited by CsA]
- Cyclosporin A binding (GO:0016018) - cyclophilins bind CsA. Crystal structure with CsA (1CYN).

## Localization
- ER lumen; retained via C-terminal retention motif (213-216).
  - [file "SUBCELLULAR LOCATION: Endoplasmic reticulum lumen."]
- Also secreted (S-cyclophilin/SCYLP), melanosome, exosomes, cell surface. Originally described as secreted cyclophilin.

## Biology
- Collagen folding / prolyl isomerization: part of P3H1/CRTAP/PPIB prolyl 3-hydroxylation complex.
  - [PMID:39245686 "The structural basis for the collagen processing by human P3H1/CRTAP/PPIB ternary complex"]
- Osteogenesis imperfecta type IX (OI9): autosomal recessive, caused by PPIB mutations.
  - [file "Osteogenesis imperfecta 9 (OI9)"]
- Interesting: PPIB-null OI has NORMAL collagen folding (unlike P3H1/CRTAP), i.e. PPIB loss does not delay overall collagen folding rate -> the NOT|protein folding IMP (PMID:20089953).
  - [PMID:20089953 "Lack of cyclophilin B in osteogenesis imperfecta with normal collagen folding."]
- ERp72(PDIA4)-cyclophilin B complex enhances IgG folding rate.
  - [PMID:22665516 "novel ERp72-cyclophilin B complex that enhances the rate of folding of immunoglobulin G"]
- Part of large ER chaperone complex (PMID:12475965).
- CD147/EMMPRIN signaling receptor -> neutrophil chemotaxis (secreted CypB). [PMID:11688976 "CD147 is a signaling receptor for cyclophilin B."]
- Host factor for HCV RNA polymerase (NS5B), measles virus. [PMID:15989969 "Cyclophilin B is a functional regulator of hepatitis C virus RNA polymerase."]

## Action plan
- PPIase activity (GO:0003755) IDA/IEA/ISS/NAS - ACCEPT (CORE MF).
- cyclosporin A binding (GO:0016018) IBA - ACCEPT (cyclophilin signature; non-core but real).
- ER / ER lumen / ER chaperone complex - ACCEPT.
- melanosome / cytosol / exosome / focal adhesion / nucleus / membrane / perinuclear / smooth ER - KEEP_AS_NON_CORE (secondary/HT proteomics).
- protein binding (many IPI HT) - KEEP_AS_NON_CORE; DYM, PDIA4 functionally meaningful but generic term.
- collagen binding (GO:0005518) ISS contributes_to - ACCEPT/KEEP_AS_NON_CORE (collagen substrate; core-related, contributes_to). Keep as supporting core.
- protein folding (GO:0006457) IBA/IDA (PMID:22665516) - KEEP_AS_NON_CORE (assists folding; downstream).
- NOT|protein folding IMP (PMID:20089953) - ACCEPT (PPIB-null has normal collagen folding -> PPIB not required for general collagen folding rate; nuanced but valid negation).
- NOT|regulation of post-translational protein modification (GO:1901873) IMP - ACCEPT (PPIB-null doesn't reduce collagen 3-hydroxylation per that paper; valid negation).
- bone development (GO:0060348) IMP - ACCEPT (OI9; core BP).
- protein stabilization (GO:0050821) IMP - KEEP_AS_NON_CORE.
- pos reg organism growth (GO:0040018) IMP - KEEP_AS_NON_CORE.
- neutrophil chemotaxis (GO:0030593) IDA - KEEP_AS_NON_CORE (secreted CypB/CD147 role).
- host-mediated viral process/genome replication (GO:0044794/0044829) IMP - KEEP_AS_NON_CORE (HCV host factor).
- RNA polymerase binding (GO:0070063) / RNA binding (GO:0003723) HDA/IPI - KEEP_AS_NON_CORE (HCV NS5B / HT RNA-interactome; RNA binding likely non-specific).
- protein-containing complex (GO:0032991) ISS - KEEP_AS_NON_CORE (generic).
- Core MF: peptidyl-prolyl cis-trans isomerase activity (GO:0003755); core BP collagen folding/bone development.
