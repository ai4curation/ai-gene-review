# NDUFAF6 (C8orf38) review notes

UniProt: Q330K2 (NDUF6_HUMAN), 333 aa. Gene symbol NDUFAF6; synonym C8orf38.

## Identity / naming
- RecName: "NADH dehydrogenase (ubiquinone) complex I, assembly factor 6"; AltName "Putative phytoene synthase" [file:human/NDUFAF6/NDUFAF6-uniprot.txt "AltName: Full=Putative phytoene synthase"].
- The "phytoene synthase" alt name and the domain architecture reflect membership in the
  squalene/phytoene synthase (SQS_PSY) / isoprenoid-synthase-like structural family: Pfam PF00494 (SQS_PSY),
  InterPro IPR002060 (Squ/phyt_synthse) and IPR008949 (Isoprenoid_synthase_dom_sf), Gene3D 1.10.600.10
  (Farnesyl Diphosphate Synthase fold), SUPFAM SSF48576 (Terpenoid synthases) [file UniProt DR lines].
- This is a "putative"/fold-level assignment only. UniProt does NOT assert any catalytic (monooxygenase,
  synthase, or oxidoreductase) EC activity for NDUFAF6, and no experimental MF annotation exists in GOA.
  It is treated as an assembly factor that has retained an isoprenoid-synthase-like fold, catalytic status
  uncertain. => Do NOT assign a catalytic molecular function.
- SIMILARITY: "Belongs to the NDUFAF6 family." [file UniProt].

## Function (authoritative UniProt FUNCTION line)
- "Involved in the assembly of mitochondrial NADH:ubiquinone oxidoreductase complex (complex I) at early
  stages. May play a role in the biogenesis of complex I subunit MT-ND1."
  {ECO:0000269|PubMed:18614015, ECO:0000269|PubMed:22019594} [file:human/NDUFAF6/NDUFAF6-uniprot.txt].
- It is an ASSEMBLY FACTOR, not a structural subunit of the holoenzyme. Do NOT assign NADH dehydrogenase
  activity (GO:0008137). Core BP = mitochondrial respiratory chain complex I assembly (GO:0032981).

## Experimental evidence
- PMID:22019594 (McKenzie et al 2011, J Mol Biol; abstract-only in cache, full_text_available: false):
  characterization of C8orf38/NDUFAF6. Patient fibroblasts with a C8orf38 mutation show "almost
  undetectable levels of steady-state complex I and defective biogenesis of the mtDNA-encoded subunit ND1";
  complementation with WT C8orf38 "restored the levels of both ND1 and complex I". Concludes C8orf38 is
  "a crucial factor required for the translation and/or integration of ND1 into an early-stage assembly
  intermediate". Basis for the IMP GO:0032981 (assembly) and IDA GO:0005743 (inner membrane) GOA
  annotations. [PMID:22019594 abstract].
- PMID:18614015 (Pagliarini et al 2008, Cell, MitoCarta): identified C8orf38 as a complex I assembly
  factor via mitochondrial protein compendium + a Leigh-syndrome/complex-I-deficiency patient variant
  (Q99R). Cited by UniProt FUNCTION. (Not in existing_annotations directly; supports the biology.)
- PMID:27466185 (Hartmannova et al 2016, HMG): Acadian variant of Fanconi syndrome (FRTS5) caused by a
  non-coding NDUFAF6 mutation; kidney/lung show specific loss of mitochondrial isoform 1; patient cells
  show complex I assembly defects and altered respiration. Supports mitochondrial isoform-1 being the
  functional assembly-factor isoform.

## Subcellular location
- SUBCELLULAR LOCATION [Isoform 1]: "Mitochondrion inner membrane. Note=Peripherally localized on the
  matrix face of the mitochondrial inner membrane." [file UniProt].
- SUBCELLULAR LOCATION [Isoform 2]: "Cytoplasm. Nucleus." => the IEA cytoplasm/nucleus and the
  UniProt DR IDA cytoplasm/nucleus annotations reflect the non-mitochondrial isoform 2, NOT the
  functional mitochondrial assembly-factor isoform 1. These are legitimately isoform-2-specific and
  non-core for complex I assembly.
- N-terminal TRANSIT peptide 1..44 (mitochondrial targeting) on isoform 1 [file UniProt FT TRANSIT].

## Isoforms
- Isoform 1 (Q330K2-1, displayed): mitochondrial, inner-membrane, functional assembly factor.
- Isoform 2 (Q330K2-2, VSP_026230): N-terminus altered (loses mitochondrial transit peptide) => Cytoplasm/Nucleus.
- Isoform 3 (Q330K2-3, VSP_026231+VSP_026232): C-terminally truncated; the only IntAct interactions
  (GUCD1, OTX1) are on isoform 3 and are not clearly functionally relevant to complex I assembly.

## Disease
- MC1DN17 (Mitochondrial complex I deficiency nuclear type 17, MIM 618239): autosomal recessive; many
  missense variants (D69V, S76P, Q99R, I124T, A178P, H269D, R274G). Leigh syndrome, bilateral striatal
  necrosis/dystonia. [file UniProt DISEASE + VARIANT lines; PMIDs 18614015, 22019594, 26741492,
  27623250, 29531337, 30642748].
- FRTS5 (Fanconi renotubular syndrome 5, MIM 618913): non-coding intron-2 variant, isoform-1 loss.
  [PMID:27466185].

## Annotation decisions summary
- GO:0032981 (complex I assembly) IMP PMID:22019594 => ACCEPT (core).
- GO:0032981 (complex I assembly) IBA GO_REF:0000033 => ACCEPT (core; consistent with experimental).
- GO:0005743 (mito inner membrane) IDA PMID:22019594 => ACCEPT (core location; isoform 1).
- GO:0005743 (mito inner membrane) IEA UniProt-SubCell => ACCEPT.
- GO:0005743 (mito inner membrane) 5x Reactome TAS => ACCEPT one representative / KEEP; all point to
  Complex I biogenesis Reactome pathway. Keep as accurate location.
- GO:0005739 (mitochondrion) IBA => ACCEPT (redundant parent of inner membrane but standard).
- GO:0005739 (mitochondrion) HTP PMID:34800366 => ACCEPT (MitoCoP high-confidence mito proteome).
- GO:0005634 (nucleus) IEA => KEEP_AS_NON_CORE (isoform-2-specific; not the complex-I function).
- GO:0005737 (cytoplasm) IEA => KEEP_AS_NON_CORE (isoform-2-specific).

## Molecular function
- No experimental MF. Family is isoprenoid-synthase-like (putative), but no catalytic activity is
  supported by UniProt/GOA. => core_functions centers on the BP (GO:0032981); no catalytic MF assigned.
