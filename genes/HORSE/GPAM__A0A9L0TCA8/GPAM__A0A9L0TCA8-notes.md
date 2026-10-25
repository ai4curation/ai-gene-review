# GPAM (horse, A0A9L0TCA8) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

### Scope and identity
- A0A9L0TCA8 (828 aa) is the UniProt reference-proteome gene-centric canonical product of horse GPAM
  (Ensembl gene ENSECAG00000014742; protein ENSECAP00000084732). The ProtNLM2 benchmark accession
  A0A9L0TTC1 (790 aa, reviewed separately in `genes/HORSE/GPAM/`) is an alternative isoform of this gene.
  Folder named `GPAM__A0A9L0TCA8` per the shared-symbol convention.
- No ProtNLM2 files or prediction-evidence folders were opened for this review.

### Deep research
- `just deep-research-falcon HORSE GPAM__A0A9L0TCA8 --fallback perplexity-lite` failed: falcon
  "Failed to authenticate"; perplexity fallback HTTP 401 insufficient_quota. No deep-research file
  exists; the review relies on cached primary literature, the human Swiss-Prot record and the
  bioinformatics below.
- A web search found no experimental study of GPAM protein in horse; only genome/annotation
  resources (NCBI Gene 100068677). So **no function is experimentally established in horse**; every
  function below is inferred by phylogenetic transfer.

### Evolutionary grounding (GPAM__A0A9L0TCA8-bioinformatics/RESULTS.md)
- PANTHER PTHR12563:SF16 (GPAT1, mitochondrial), same subfamily as human GPAM Q9HCL2 and mouse Gpam.
- Descendant of PAINT node PTN000970957 (Eumetazoa) carrying IBD for GO:0004366, GO:0005739,
  GO:0006650, GO:0019432 (seeds human GPAM, mouse Gpam, mouse Gpat2, rat).
- Gap-free alignment to human over all 828 residues, 94.4% identity; HXXXXD motif (HRSHID, human
  230-235), six CoA-binding residues and the N-terminal mitochondrial-targeting region (39/41) conserved.
- Unlike A0A9L0TTC1, this product retains the catalytic-domain segment corresponding to human 370-407.
- PAINT placed no plasma-membrane term anywhere in PTHR12563; the DHAPAT (GNPAT) node PTN002488810
  carries peroxisomal/ether-lipid terms that are not transferred to the GPAT1 node — deliberate scoping.

### Donor evidence (experimental, other mammals)
- Human GPAT1: cryo-EM + functional studies; mitochondrial outer membrane, peripheral, membrane-associated
  via amphipathic patch and N-terminal loop-helix with mitochondrial targeting signal
  [PMID:36522428 "GPAT1 has no transmembrane regions as previously proposed"].
- Mouse Gpam knockout: liver mtGPAT activity lost, hepatic TAG reduced 37%
  [PMID:12417724 "These data confirm the important role of mtGPAT in the synthesis of triacylglycerol"].
- Mouse Gpat1-/- hepatocytes cannot incorporate de novo fatty acid into TAG
  [PMID:23908354 "demonstrate that GPAT1, but not GPAT4, is required to incorporate de novo"].
- Palmitoyl-CoA preference [PMID:12417724 "mtGPAT has a marked preference for palmitoyl-CoA (16:0)"].

### Decisions
- Activity GO:0004366 ACCEPT (IBA, IEA); generic acyltransferase rows MODIFY to GO:0004366.
- Location: mitochondrial outer membrane ACCEPT; mitochondrion (IBA) and mitochondrial membrane MODIFY to
  outer membrane; plasma membrane (IPR028354 GPAT_PlsB InterPro2GO, bacterial-derived) REMOVE.
- Process: triglyceride biosynthetic process ACCEPT; glycerophospholipid metabolic process, phospholipid
  biosynthetic process and lipid metabolic process MODIFY to phosphatidic acid biosynthetic process
  (GO:0006654; plus TAG for lipid metabolic process), matching the human GPAM review. CDP-diacylglycerol
  biosynthesis KEEP_AS_NON_CORE (first step of a route GPAT1 output feeds, but TAG is the dominant fate).
- The horse UniProt entry also carries an ARBA-only lysophosphatidylglycerol acyltransferase reaction
  (RHEA:33203); not in GOA and not proposed — its physiological relevance is unresolved even in human.
