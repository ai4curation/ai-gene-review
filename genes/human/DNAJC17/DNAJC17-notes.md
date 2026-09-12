# DNAJC17 research notes

## Identity
- UniProt Q9NVM6, HGNC:25556, 304 aa. DnaJ/HSP40 subfamily C member 17. Poorly characterized
  (Pharos Tbio).
- Architecture: N-terminal J domain (11-76), central disordered acidic/basic region (79-145),
  C-terminal RRM (RNA recognition motif, 178-249; NMR structure PDB:2D9O). [file:human/DNAJC17/DNAJC17-uniprot.txt]
- So it is a J-domain + RRM protein: a putative HSP70 co-chaperone with RNA-binding capacity.
- Predominantly nuclear (also cytoplasmic). Phosphorylated at Ser-112 (many MS studies);
  methylated at Lys-264. Associated with nuclear speckles (CD-CODE 804901D1). [file:human/DNAJC17/DNAJC17-uniprot.txt]

## Inferred functions
- Spliceosome / spliceosomal complex disassembly (IBA, GO_REF:0000033): inferred from orthologs
  PomBase:SPCC10H11.02 and SGD:S000003096 (yeast Cwc23), a J-domain protein that functions with the
  Prp43 helicase in spliceosome disassembly. RRM + nuclear-speckle localization + EFTUD2 interaction
  are consistent. [file:human/DNAJC17/DNAJC17-goa.tsv]
- RNA binding (IEA from InterPro RRM, IPR000504) and nucleic acid binding (IEA, IPR035979): supported
  by the RRM domain and the RIKEN NMR structure of the RNA-binding domain. [file:human/DNAJC17/DNAJC17-uniprot.txt]
- UniProt FUNCTION (by similarity to mouse Q91WT4): "May negatively affect PAX8-induced
  thyroglobulin/TG transcription." Speculative/orthology-based; the gene is also reported essential
  in mouse (lethal knockout). [file:human/DNAJC17/DNAJC17-uniprot.txt]
- GO:0000122 negative regulation of transcription by RNA pol II (IEA Ensembl) - in UniProt DR but not
  in seeded ai-review/goa list; reflects the PAX8/TG inference.

## Interactions (IPI GO:0005515)
- Q15029 = EFTUD2 (SNRP116/U5-116K), a core U5 snRNP/spliceosome GTPase. PMID:35271311 (OpenCell),
  PMID:40205054 (cell maps). Corroborates spliceosome association.
- Q6FHY5 = MEOX2 (homeobox TF). PMID:32296183 (HuRI Y2H). Less clearly relevant.

## Localization
- Nucleus (IEA SubCell + ISS from rat D3ZSC8), cytoplasm (IEA + ISS), predominantly nuclear.
  [file:human/DNAJC17/DNAJC17-uniprot.txt]

## Curation
- Core function uncertain. Best-supported convergent picture: a nuclear J-domain/RRM protein
  associated with the spliceosome (likely human ortholog of yeast Cwc23 acting in spliceosome
  disassembly). RNA binding (RRM) is a genuine inferred MF. Keep spliceosome BP/CC as
  KEEP_AS_NON_CORE / ACCEPT given convergent (IBA + EFTUD2 IPI) but not direct human experimental
  evidence; flag the PAX8/TG transcription inference as orthology-only.
- Use UNDECIDED only where truly unable to assess. Here we can reason from orthology + domain +
  interactome, so avoid UNDECIDED; use ACCEPT/KEEP_AS_NON_CORE for the convergent spliceosome/RNA
  picture and KEEP_AS_NON_CORE for the protein-binding HT terms.
