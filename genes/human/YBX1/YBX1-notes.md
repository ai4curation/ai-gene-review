# YBX1 notes

Automated deep research could not run in this workspace: Falcon and the
perplexity-lite fallback were unavailable to `deep-research-client`, and the
only installed provider (`claude_code`) reported a missing login. These notes
therefore record the manual literature pass over the GOA PMID rows, UniProt
text, and Reactome event summaries.

YBX1 is a multifunctional cold-shock-domain nucleic-acid-binding protein. The
core CSD binds DNA and RNA, and the long C-terminal basic/aromatic tail supports
RNA-protein granule association. The most specific experimentally supported
activity is m5C-modified RNA reading: PMID:31358969 identifies YBX1 as the
m5C reader whose W65 indole ring recognizes m5C-modified mRNAs and recruits
ELAVL1 to stabilize those targets. PMID:27559612 shows that YBX1 binds miR-223
and is required for sorting selected miRNAs into CD63-positive exosomes in a
cell-free assay and in HEK293T cells. PMID:29073095 broadens this to tRNAs, Y
RNAs, and vault RNAs in purified extracellular vesicles.

The CRD complex rows from PMID:19029303 are well supported and more specific
than generic RNA binding. IGF2BP1-associated HNRNPU, SYNCRIP, YBX1, and DHX9
assemble on the MYC coding-region determinant and are required for CRD-mediated
MYC mRNA stabilization. PMID:18335541 supports cytoplasmic stress granule
localization through MBNL1/YB-1/DDX1 colocalization after stress.

Several DNA-binding and transcription rows are real but are less central than
the RNA-sorting and RNA-stabilization functions. The original cloning papers
identified Y-box or single-stranded DNA binding (PMID:2977358, PMID:3174636,
PMID:8188694); PMID:15229244 shows YBX1 binding and activation at the 5-HTT
VNTR reporter; PMID:18809583 shows acetylated APEX1 strengthening YBX1 binding
to the MDR1 Y-box and activating MDR1. PMID:14718551 supports in vitro strand
separation, endonucleolytic activity, and DNA-repair-protein binding, but no
specific GO DNA-repair activity is in GOA.

The extracellular and extracellular-exosome rows are kept as non-core. Secreted
YBX1 is demonstrated for LPS-stimulated primary human monocytes and vesicle
fractions in PMID:19483673, and that paper also shows extracellular mitogenic
and migratory activity. PMID:27559612 and PMID:29073095 support the exosome
fraction as a specialized RNA-sorting location rather than YBX1's main cellular
site.

The many `GO:0005515 protein binding` IPI rows are removed as bare protein
binding. Where the same paper gives a mechanistic activity or location (e.g.
PMID:19029303 for the CRD RNP complex, PMID:18335541 for stress granules,
PMID:18809583 for APEX1-dependent transcription activation, PMID:31358969 for
ELAVL1 recruitment to m5C-containing mRNAs), that function is kept on a more
informative row.
