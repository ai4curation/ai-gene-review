# WHY2 (At1g71260, Q8VYF7) - manual literature synthesis

No deep-research API was available for this review; this synthesis was written by hand from the cached
publications in `publications/` and the UniProt record. Quotes are verbatim from the cached files.

## Identity and family

- WHIRLY2 (AtWHY2) is one of three Arabidopsis Whirly proteins, a small plant-specific family of
  single-stranded DNA (ssDNA) binding proteins with a Whirly fold (Pfam PF08536, InterPro IPR013742).
  The 238-aa precursor carries a predicted 29-residue mitochondrial transit peptide (UniProt FT TRANSIT 1..29).
- The Arabidopsis WHY2 Whirly domain (residues 45-212) was crystallised (PDB 4KOP) and forms a tetramer
  [PMID:24192350 "In the WHY2 structure, the four proteins present in the asymmetric unit form a Whirly tetramer with fourfold symmetry"].
  DNA-contacting residues defined in the potato StWHY2-ssDNA structures are conserved in AtWHY2
  [PMID:24192350 "residues equivalent to Phe64, His139 and Lys153 of potato WHY2"].

## Localisation

- Mitochondrial targeting was shown by in vitro import and GFP fusions [PMID:15967440 "functionality of these sequences was demonstrated by in vitro import assays into"] (abstract only in cache).
- Stable WHIRLY2:GFP lines co-localise with TMRM and show punctate intramitochondrial spots
  [PMID:32490348 "Within the mitochondria, WHIRLY2:GFP fluorescence was not equally distributed but appeared in punctiform spots."].
- mtDNA immunoprecipitation shows AtWhy2 is bound along the whole mitochondrial genome
  [PMID:18423020 "Binding sites seem to occur along the length of the mitochondrial genome since we were unable to detect a region where Whirlies are not bound to mtDNA."].
- WHY2 co-purifies with ODB1 (RAD52-1) in large nucleoprotein complexes in mitochondria [PMID:22762281 "In mitochondria, WHY2 and ODB1 were found in"] (abstract only).
- Together these support a mitochondrial nucleoid location [PMID:32490348 "The data presented in this study confirm the nucleoid localization of WHIRLY2 but also support a structural role in mitochondria nucleoid organization."].
  No experimental evidence places WHY2 in chloroplasts; the paralogue WHY3, not WHY2, was found dual-targeted (PMID:32490348).

## Molecular function

- Recombinant AtWhirly2 binds ssDNA with nanomolar affinity and is tetrameric
  [PMID:30698803 "AtOSB2 and AtWhirly2 bind to a pssDNA-10 substrate with dissociation constants (Kd) of 8 and 22 nM respectively"].
- Mechanism (from the potato orthologue StWHY2): non-sequence-specific binding in which ssDNA is held between
  adjacent subunits and made unavailable for duplex formation [PMID:20551348 "These reveal a nonsequence-specific ssDNA binding mechanism in which DNA is"]. Potato WHY2 tetramers further assemble into 24-mers on long ssDNA, dependent on the KGKAAL motif lysine (PMID:21911368; potato WHY2 and Arabidopsis WHY1 were tested, not AtWHY2).
- RNA: Whirly proteins, including WHY2, were captured in Arabidopsis mRNA interactome studies [PMID:32344669 "ptRIC also assigned RNA-binding activity to all the members of the Alba- and the Whirly (WHY)-domain-containing protein families."]; the physiological relevance for mitochondrial RNA is unknown.

## Biological role

- Genome stability / DSB repair in mitochondria: after ciprofloxacin-induced organellar DSBs, why2-1 mutants
  accumulate microhomology-mediated mtDNA rearrangements [PMID:20551348 "These results indicate that, upon induction of DSBs, why2-1 plants accumulate DNA rearrangements in the mitochondrial genome more readily than do wild-type plants."].
  The effect is organelle-specific (plastid genome unaffected in why2-1).
- In vitro, AtWhirly2 blocks microhomology-mediated end-joining by organellar DNA polymerases PolIA/PolIB,
  consistent with competition for the ssDNA of a resected break [PMID:30698803 "Only AtWhirly2 and AtOSBs, however, completely block MMEJ by AtPolIs."].
- Overexpression lowers mtDNA content and mitochondrial transcripts; knockout has no visible phenotype under
  normal growth (PMID:18423020), but why2-1 mitochondria show disorganised nucleoids, fewer cristae and impaired
  seed germination (PMID:32490348). These are phenotypes and do not by themselves define new process terms.
- Defense response / nuclear transcription: these roles were described for potato StWHY1 and Arabidopsis AtWHY1
  [PMID:15708347 "Arabidopsis and potato Whirly orthologs act as transcription factors that"]; there is no
  WHY2-specific evidence.
