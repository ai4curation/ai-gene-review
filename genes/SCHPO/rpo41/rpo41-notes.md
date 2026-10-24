# rpo41: functional evidence

Rpo41 is the mitochondrial DNA-directed RNA polymerase of Schizosaccharomyces pombe. It binds mitochondrial promoters and synthesizes RNA from DNA templates; association with the transcription factor Mtf1 greatly enhances promoter-directed initiation. Its transcriptional activity sustains mitochondrial gene expression.

- [PMID:21357609] "We show biochemically, that purified Mtf1 and Rpo41 together can bind to the S. pombe mitochondrial promoters and can support transcription from the S. pombe mitochondrial promoters in vitro."

Evidence interpretation: sequence/domain records are used for family placement; AI descriptions and ARBA labels are not independent validation. Family transfer is limited to conserved properties and is identified as inference. Genome-scale localization annotations are retained where consistent with the biology; an abstract does not expose every individual observation. All original annotation rows are preserved.

ProtNLM provenance: pre-release `post-processed-2026_02_28k.xml`, exact entry and all evidence keys preserved in the source XML/JSON. These current Swiss-Prot entries are absent from the public TrEMBL pilot. Known-function overlap does not establish model training membership. See the function sidecar for atom-by-atom paragraph assessments.

Research provenance: the gene-focused Falcon report was generated concurrently with publication caching. The report was inspected for source leads; the biological decisions above rely on the cited primary records and specified family evidence.

The completed Falcon search has retrieval gaps: its inability to locate target-level localization is not used to override PomBase’s HDA records. Curated genomic-screen observations and the directly inspected papers take precedence over an empty literature-search result.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Identity: O13993 is the reviewed Swiss-Prot canonical rpo41 product (SPAC26H5.12), 1154 aa, with an N-terminal
transit peptide (1-30), RPOL_N (PF14700) and phage-type RNA polymerase (PF00940) domains, both PROSITE phage RNA
polymerase signatures, and annotated active-site residues 821, 890, 1061. Not a fragment, isoform or alternative
gene model; length is in range for the subfamily (S. cerevisiae RPO41 1351 aa, human POLRMT 1230 aa).

Evolutionary grounding: PANTHER PTHR10102:SF0, the same subfamily as S. cerevisiae RPO41 (P13433) and human POLRMT
(O00411). The polymerase activity, mitochondrial transcription and complex IBAs come from PAINT node PTN000010146
(donors include SGD RPO41, human POLRMT, Dictyostelium, Drosophila, Trypanosoma). Mitochondrial promoter binding
(GO:0001018) was placed at a shallower node PTN000010147 with rpo41 itself as the only donor; read as a deliberate
choice not to push promoter binding to the whole clade. The family review interpro/panther/PTHR10102 agrees with
the SF0 placement; no disagreement.

Literature (PMID:21357609, full text): rpo41 deletion is lethal (petite-negative) and reduces mitochondrial
transcripts with a nuclear control unchanged ["Transcription of the mitochondrial genes was also reduced in the
rpo41Δ cells compared to wild-type cells"]; overexpression raises them. Purified Rpo41 gives a weak promoter
band shift alone and a strong super-shift with Mtf1; core-element mutations reduce binding ["Mtf1 and Rpo41 bind
to the promoters specifically"]. Rpo41 alone or with Mtf1 initiates at the in-vivo start sites ["Rpo41/Mtf1 or
Rpo41 alone can initiate transcription in vitro"], unlike S. cerevisiae Rpo41. Viability/morphology/membrane
potential phenotypes are downstream consequences and not annotated as process participation.
PMID:21727087 (abstract only) is the source of the IDA mitochondrion row; abstract groups the mitochondrial RNA
polymerase with the PPR proteins localized to mitochondria. An earlier ORFeome screen called Rpo41 "cytoplasmic
dots" (cited in PMID:21357609), compatible with mitochondrial puncta.

Changes vs previous review: GO:0034062 5'-3' RNA polymerase activity changed ACCEPT -> MODIFY to GO:0003899 (the
old reason itself called it "broader"). Every row now cites the specific experiment supporting it rather than
one shared abstract sentence; the UniProt DR GO line is no longer used as support for mitochondrion. Description
expanded (transit peptide, holoenzyme, partial Mtf1 independence); added a second core function for promoter
binding; added suggested questions/experiment. Other actions unchanged (DNA binding and DNA-templated transcription
MODIFY to their specific descendants; all others ACCEPT).

Relative to review next: S. cerevisiae RPO41 (P13433, SGD:S000001858), same PANTHER subfamily SF0 and IBA donor
for PTN000010146; no review in repo (genes/yeast/RPO41 absent). Human POLRMT (O00411) also unreviewed.
Modules: none specific; modules/phage_t7_replisome_transcription.yaml mentions POLRMT only in passing.
