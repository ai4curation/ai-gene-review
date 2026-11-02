# A0A137NYV2 (CONCODRAFT_9893) notes - Conidiobolus coronatus NRRL 28638

## Entry identity

- A0A137NYV2_CONC2 is an unreviewed TrEMBL entry (PE 3) of 352 aa from the
  reference proteome UP000070444. Its ORF name is CONCODRAFT_9893 (EMBL
  KXN67957.1), and UniProt gives no gene symbol. The folder follows the repository
  convention for symbol-less TrEMBL entries (accession folder, ORF name as
  `gene_symbol`).
- Domain content from the UniProt record: a predicted SignalP signal peptide
  (1-17), a Peptidase S8/S53 domain (Pfam PF00082, 97-335), and PROSITE
  active-site signatures for all three triad residues (D106, H138, S293:
  SUBTILASE_ASP, SUBTILASE_HIS, SUBTILASE_SER). The CDD hit is cd04077
  (Peptidases_S8_PCSK9_ProteinaseK_like; InterPro IPR034193). The PANTHER
  subfamily is PTHR43806:SF66. No I9 propeptide domain is annotated, although
  residues 18-96 between the signal peptide and the catalytic domain are the
  usual propeptide position in proteinase K-like enzymes.
- The sequence contains the S8A motifs that Arnesen et al. used for
  Entomophthoromycotina SLSPs: Asp-Ser-Gly ("YLIDSGIN"), His-Gly-Thr-His
  ("NGHGTH") and Gly-Thr-Ser-Met-Ala-Xaa-Pro ("GTSMATP") [PMID:30111619
  "contained active site residues closely resembling the motifs
  Asp-Thr/Ser-Gly, His-Gly-Thr-His, and Gly-Thr-Ser-Met-Ala-Xaa-Pro
  characteristic of the S8A subfamily"].

## Paralog context

- C. coronatus encodes a large family of subtilisin-like serine proteases
  [PMID:30111619 "C. coronatus (n = 36)"]. A UniProt query (organism 796925 with
  Pfam PF00082; run 2026-10-28) returned 45 entries. A0A137NYV2 is one of
  dozens of paralogs, and nothing in the literature links it to a characterised
  enzyme.

## Characterised C. coronatus proteases (not mapped to sequences)

- C. coronatus "secretes several proteinases into culture broth"
  [PMID:16933280]. A purified 30-32 kDa enzyme was subtilisin-like by substrate
  and inhibitor profile [PMID:16933280 "the purified proteinase from the
  fermentation broth of Conidiobolus coronatus is a subtilisin-like serine
  proteinase"].
- The National Chemical Laboratory (Pune) alkaline protease, the enzyme lineage
  behind the Shankar et al. 2010 silver-recovery work, is an alkaline serine
  protease. It is functionally like subtilisin Carlsberg but differs from it in
  composition, immunology and peptide maps [PMID:9082920 "Our results demonstrate
  that although they are functionally analogous, the Conidiobolus protease is
  structurally distinct from subtilisin Carlsberg."]. These are not sequence
  data. A fungal proteinase K-like S8 enzyme would be expected to differ from a
  bacterial subtilisin in exactly these ways, so the paper does not exclude an
  S8 assignment. Nor does it identify a gene.
- The same group described intracellular forms and autoproteolytic conversion
  of the alkaline protease that they link to conidial discharge [PMID:1572367].

## Annotation calls

- GO:0004252 serine-type endopeptidase activity (IEA, UniRule-backed): ACCEPT.
  The protein has a complete S8 catalytic triad with all three PROSITE active-site
  signatures. This is a homology inference; the protein has not been assayed.
- GO:0006508 proteolysis (IEA): ACCEPT.
- GO:0008236 serine-type peptidase activity (IEA): MODIFY to GO:0004252.
- No NEW extracellular-region row. The only localisation line is the
  computational signal peptide, and proteinase K-like S8 enzymes include both
  secreted and vacuolar members (yeast proteinase B, PRB1, is vacuolar). One
  line of evidence that does not separate secretion from vacuolar targeting is
  not enough for NEW, so the question is recorded in suggested_questions.

## CMMMech claim check (data/records/waste-x-ray-films.yaml)

CMMMech grounds the `fungal_supernatant_emulsion_stripping` mechanism and the
`conidiobolus_alkaline_protease_supernatant` node to A0A137NYV2. Its
functional_role is "Secreted subtilisin-like serine alkaline protease (peptidase
S8 family; locus CONCODRAFT_77703) in Conidiobolus coronatus capable of
hydrolyzing extracellular protein/gelatin substrates."

Problems found:

1. **Wrong locus.** UniProt gives A0A137NYV2 the ORF name CONCODRAFT_9893.
   CONCODRAFT_77703 is UniProtKB:A0A137PCC5, a glycine--tRNA ligase (UniProt
   query run 2026-10-28). The locus string appears three times in CMMMech
   (functional_role, annotation_note and the node description) and should be
   corrected in CMMMech. This is a CMMMech data error, not a UniProt or GOA
   defect.
2. **Arbitrary paralog choice.** The genome encodes about 36-45 S8 proteases.
   No source links the Shankar et al. 2010 crude-supernatant activity, or the
   purified NCL alkaline protease, to this sequence. CMMMech's evidence entry
   already concedes that the isoform was not sequenced or purified. The grounding
   is therefore a representative family member, not "the" alkaline protease, and
   the functional_role sentence reads as more specific than it is.
3. **"Secreted" and "alkaline" are unverified for this protein.** Secretion rests
   on a SignalP prediction only; vacuolar targeting is not excluded. Nobody has
   measured the pH optimum of this gene product. Gelatin hydrolysis is a
   reasonable expectation for an active S8 protease but has not been tested for
   this sequence.
4. **Strain mismatch.** CMMMech's annotation_note already records it: the
   experimental strain is ATCC PTA-4132 (NCBITaxon:34488) and the proteome strain
   is NRRL 28638 (NCBITaxon:796925).
