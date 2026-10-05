# CD52 (CAMPATH-1 antigen, HE5) - curation notes

UniProt: P31358 (CD52_HUMAN), 61 aa precursor; HGNC:1804.

## Deep research status

- `just deep-research-falcon human CD52` was launched in parallel with publication caching.
  See the end of this file for the outcome. Literature for this review was gathered with the
  PubMed MCP tools and cached via `ai-gene-review fetch-pmid` (PMIDs 29997173, 29244050,
  33658999, 31507595, 8418821, 7688956) in addition to the GOA-cited PMIDs.

## Structure and biogenesis

- Tiny GPI-anchored glycopeptide: 24-aa signal peptide, mature peptide of ~12 residues, C-terminal
  propeptide removed on GPI attachment [PMID:1711975 "It consists of 37 amino acid residues plus a
  24-residue signal peptide"; "It has all the features expected for a GPI-anchored membrane protein"].
- GPI anchor at Ser-36; single N-glycosylation site; mature peptide 12 aa [PMID:7688956 "the antigen is a
  very small glycosylphosphatidylinositol (GPI)-anchored glycoprotein with a mature peptide comprising
  only 12 amino acids"].
- UniProt: "Cell membrane; Lipid-anchor, GPI-anchor" [file:human/CD52/CD52-uniprot.txt].
- The peptide is essentially a scaffold for the GPI anchor and N-glycan [PMID:29997173 "The mature human
  CD52 protein, comprising just 12 amino acids, acts as a scaffold for the posttranslational addition of a
  GPI anchor and an N-glycan"]. Bioactivity resides in the sialylated N-glycan
  [PMID:31507595 "Removal of α-2,3 sialylation abolished bioactivity"].

## Expression

- Leukocytes (B, T, NK, monocytes, macrophages, eosinophils, DCs) and male reproductive tract epithelium
  (epididymis, vas deferens) [PMID:8418821 "showing the gene product to originate from epithelial cells
  of the epididymal and deferent duct"]; epididymal CD52 is released into seminal fluid and taken up by
  sperm [PMID:29997173 "in the male reproductive tract by epithelial cells of the epididymis from which it
  is released into the seminal fluid to be taken up by sperm"]. HPA: tissue enriched (epididymis).

## Function: soluble CD52 as an immunosuppressive Siglec-10 ligand

- Activated CD52-high CD4 T cells release soluble CD52 (phospholipase C cleavage of GPI anchor); soluble
  CD52 binds Siglec-10 and suppresses TCR signaling [PMID:23685786 "Their suppression was mediated by soluble
  CD52 released by phospholipase C. Soluble CD52 bound to the inhibitory receptor Siglec-10 and impaired
  phosphorylation of the T cell receptor-associated kinases Lck and Zap70 and T cell activation"].
- Mechanism: CD52-Fc binds HMGB1 Box B (Kd ~130 nM), which promotes binding of the alpha-2,3-sialylated
  N-glycan to Siglec-10; this induces Siglec-10 tyrosine phosphorylation and SHP1 recruitment
  [PMID:29997173 "CD52-Fc induced tyrosine phosphorylation of Siglec-10 and was recovered from T cells
  complexed with HMGB1 and Siglec-10 in association with SHP1 phosphatase and the T cell receptor (TCR)"].
  This qualifies CD52 as a receptor ligand (GO:0048018) for the inhibitory receptor SIGLEC10.
- Innate cells: soluble CD52 inhibits TLR- and TNFR-driven NF-kB activation; Cd52 KO mice have exaggerated
  LPS responses [PMID:29244050 "soluble CD52 inhibits Toll-like receptor and tumor necrosis factor receptor
  signaling to limit activation of NF-κB"; "genetic deletion of CD52 exacerbates LPS responses"].
- B cells: CD52-deficient JeKo-1 cells hyperresponsive to BCR signalling; CD52-Fc inhibits BCR signaling
  partially via Siglec-10 [PMID:33658999].
- Reproductive tract: soluble CD52 in semen proposed to contribute to immune tolerance of sperm
  [PMID:29997173 "the immune regulatory function of CD52 is likely to extend to the reproductive tract"] -
  hypothesis, not demonstrated.

## Older antibody-crosslinking literature

- Cross-linking anti-CDw52 F(ab')2 on monocytes induces Ca2+ flux and oxidative burst, but the paper's own
  conclusion is that this is a generic property of GPI-anchored proteins [PMID:8223854 "most, if not all,
  GPI-linked surface glycoproteins on myeloid cells are capable of mediating cell activation and suggest that
  the GPI anchor is a structure facilitating signal transduction"]. Not a physiological CD52 function;
  annotations to calcium and respiratory burst treated as over-annotations.

## Annotation decisions (summary)

- protein binding (SIGLEC10, PMID:23685786) -> MODIFY to receptor ligand activity GO:0048018.
- protein binding (SIGLEC10, PMID:35922511 large screen) -> REMOVE (uninformative; interaction itself real).
- plasma membrane / membrane / extracellular region -> ACCEPT.
- Ca2+ (IDA, IBA), respiratory burst (NAS) -> MARK_AS_OVER_ANNOTATED (antibody-crosslinking artefact,
  generic GPI property).
- sperm midpiece (IBA from mouse Cd52) -> KEEP_AS_NON_CORE (CD52 is acquired by sperm from epididymal fluid).
- NEW: negative regulation of T cell activation (GO:0050868), negative regulation of toll-like receptor
  signaling pathway (GO:0034122), external side of plasma membrane (GO:0009897).
