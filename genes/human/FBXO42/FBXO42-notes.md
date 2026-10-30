# FBXO42 (human, Q6P3S6) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: FBXO42 is reviewed here because it is the closest experimentally characterised relative
of fly Fbxo42 (Q9W281). No ProtNLM2 file or prediction-evidence folder was opened or used.

### Deep research
`just deep-research-falcon human FBXO42 --fallback perplexity-lite` failed. Falcon returned
"Failed to authenticate" (Edison auth error), and the perplexity-lite fallback returned HTTP 401
(insufficient quota). No deep-research file exists. The review is built from the primary papers
cached in `publications/` and the curated UniProt entry.

### Evolutionary grounding
- UniProt DR lines: PANTHER PTHR46432, subfamily PTHR46432:SF1 (F-BOX ONLY PROTEIN 42).
  `interpro/panther/PTHR46432/PTHR46432-entries.csv` places human Q6P3S6, mouse Q6PDJ6 and fly
  Q9W281 in SF1, which makes them 1:1 orthologs within the subfamily.
- The two IBA rows (GO:0019005 SCF complex; GO:1990756 substrate adaptor) come from PAINT node
  PTN002924600, which covers this clade. Both are also independently established by human
  experiments, so for the human protein the IBA adds only the claim that the function is
  inherited.
- Not transferred: fly-specific substrates (Ataxin-2, Widerborst/PP2A-B56) and processes
  (synaptonemal complex, unfolded protein response). PAINT propagated only the SCF/adaptor
  terms from the fly donor, and the omission of the fly process terms is treated as deliberate.
  The mouse ACAA2/beta-oxidation function (UniProt "by similarity" from Q6PDJ6) is not
  annotated here; it is raised as a question.

### Experimentally established in human (this species)
- SCF membership and substrate-adaptor activity: the F-box is needed for SKP1-CUL1 assembly and
  for substrate ubiquitination; the Kelch domain binds substrates [PMID:21127074 "JFK
  destabilizes p53 through the assembly of a Skp1-Cul1-F-box complex"; PMID:36129980 "The FBXO42
  F-box domain, which links FBXO42 to other components in the SCF complex, was required for RBPJ
  polyubiquitination"].
- p53: recognised after CSN-associated kinase phosphorylation, then ubiquitinated and degraded.
  JFK/FBXO42 is itself a p53 target gene, which forms a feedback loop (PMID:19509332,
  PMID:21127074). PMID:19509332 has a 2025 erratum that I could not read.
- PP2Ac: degraded by SCF(FBXO42) when CCDC6 presents it. Shown by cryo-EM, in vitro
  ubiquitination with purified components, and a half-life that rises from about 36 h to about
  60 h on depletion [PMID:41986709 "Under normal conditions in HOP-62 cells, the PP2Ac half-life
  is approximately 36 h; FBXO42 depletion extends the PP2Ac half-life to nearly 60 h"]. The
  methylated C-terminal tail of PP2Ac binds in the pore of the Kelch domain; W192 and G284 make
  contact with it.
- RBPJ: K63-linked, non-degradative ubiquitination at K175, which promotes chromatin binding and
  Notch target activation [PMID:36129980 "K175 ubiquitination did not affect the turnover rate
  of RBPJ, indicating that it does not mediate RBPJ proteolytic degradation"].
- PP4: FBXO42 ubiquitinates PP4C, PP4R2, PP4R3A and PP4R3B. The chains are mostly
  non-degradative and prefer K33 linkage, and they restrain PP4 activity [PMID:41484364
  "However, the finding supports the idea that FBXO42 catalyses non-degradative ubiquitin
  chains."]. **Discrepancy:** the UniProt FUNCTION text says FBXO42 mediates "'Lys-48'-linked
  polyubiquitination and proteasomal degradation of components of the PP4 phosphatase complex"
  and cites this paper, but the paper reports unchanged half-lives and non-degradative
  ubiquitination. Consider reporting this to UniProt.
- Nuclear localisation (IF in PMID:39134694; co-localisation with PP4R2/R3 in PMID:41484364).
- Phenotypes only, not annotated as processes: hypersensitivity to antimitotics and ATR
  inhibitors and aberrant mitoses (PMID:33539788, PMID:41484364); TP53-dependent proliferation of
  neuroblastoma cells (PMID:39134694).

### Decisions
- All 9 GO:0005515 IPI rows: REMOVE (protein-binding policy). RBPJ functional content is
  captured by the GO:1990756 IDA.
- GO:0031146 IDA (PMID:36129980): ACCEPT. The paper's main modification is non-degradative,
  but the claim is true for FBXO42 on the strength of the p53 and PP2Ac data, and the
  curator had the full text.
- NEW: GO:0070534 protein K63-linked ubiquitination (IDA) and GO:0045747 positive regulation of
  Notch signaling pathway (IMP), both from PMID:36129980. FBXO42 does part of the work (it
  recognises the substrate for the ubiquitination step) and acts directly on the pathway
  transcription factor.
