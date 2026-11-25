# TRAF2 horse evidence notes

Target F7BIV4 is the selected 516-residue horse protein. [Pairwise sequence analysis](TRAF2-bioinformatics/RESULTS.md) covers all 501 residues of human Q12933 with 92.0% paired identity; the RING/zinc-finger and C-terminal TRAF architecture is retained. The insertion after aligned human position 265 does not remove a major domain. Pairwise similarity is not a reciprocal-orthology analysis, and the current sequence has not been verified against the original ProtNLM input.

Primary human/mouse evidence supports all five ProtNLM terms: T-cell cytokine production (PMID:15125833), direct CD40 binding (PMID:9718306), cIAP-associated ligase-complex and TNF-receptor-complex membership (PMID:20447407), and broad immunoglobulin regulation through CD40 (PMID:17360936 with direct human receptor-binding evidence). These are explicitly mammalian transfers, not horse experiments. The last claim does not establish every isotype or species-specific response. COR means the supported term is absent from the frozen horse GOA; training membership is unknown.

The existing electronic E3 and autoubiquitination assertions remain UNDECIDED because human primary studies provide conflicting mechanistic evidence (PMID:19810754 versus PMID:20577214). TRAF2 recruitment of catalytic cIAPs is independently supported and is sufficient for ligase-complex membership. No ARBA assertion or AI-generated review prose is used as biological validation. The unreviewed horse record and absence of identified horse-specific mechanistic literature did not justify a horse Edison job; [human manual research](../../human/TRAF2/TRAF2-deep-research-manual.md) supplies the detailed investigation.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not consulted for this re-review. The `*-protnlm-*` files were not opened, and the paragraph above about ProtNLM terms was not used as evidence.

**Deep research.** `just deep-research-falcon HORSE TRAF2 --fallback perplexity-lite` failed. Edison returned `403 Forbidden` at `/auth/login`, and the perplexity-lite fallback also failed. No provider file was written. The evidence base is the human manual investigation (`genes/human/TRAF2/TRAF2-deep-research-manual.md`) and the cached primary papers, plus two newly cached papers: PMID:26701909 (Etemadi 2015, full text) and PMID:10650002 (Urano 2000, abstract).

**Identity.** F7BIV4 (516 aa, unreviewed TrEMBL, VGNC:24455 TRAF2, Ensembl ENSECAP00000011150) is the full-length TRAF2 gene model. It is not a fragment.
- PANTHER places it in PTHR10131:SF21 (TNF receptor-associated factor 2), the same subfamily as human Q12933 (501 aa).
- Feature mapping ([RESULTS-rereview.md](TRAF2-bioinformatics/RESULTS-rereview.md), new script `compare_features_rereview.py`) aligns every human residue to the horse protein.
- The RING Cys/His ligands (8/8), the cIAP-binding residues I285/V288/E292 (horse I300/V303/E307), the coiled coil (46/50 identical) and the MATH domain (142/146) are all conserved.
- The extra 15 residues are two insertions in the ZF2-to-coiled-coil linker: SSSFLG after human 260, and NPGAEVSKA after human 265. They do not correspond to any human splice variant. Whether they are a real horse exon feature or a gene-model artefact is unverified.
- The `gene_symbol` field was wrongly set to the accession (`F7BIV4`) and has been corrected to `TRAF2`.

**Evolutionary grounding.** Horse is not a PAINT reference genome, so it receives no IBA rows. The PTHR10131 PAINT IBDs that cover SF21 are:
- GO:0035591 signaling adaptor activity at PTN008301857, with IRD negations only on separate subclades;
- GO:0005164 and GO:0033209 at PTN000805720;
- GO:0005737 at PTN008938480;
- GO:0004842, GO:0043123 and GO:1990604 at the vertebrate TRAF2 node PTN002562154.

On this basis I added GO:0035591, GO:0043123 and GO:1990604 as NEW. They are the human IBA set and all are grounded in human or mouse experiments. GO:0004842 is also PAINT-placed, but the human donor evidence is itself contested, so it stays UNDECIDED as in the human review.

**E3 question.** Etemadi et al. 2015 (PMID:26701909) show that keratinocyte or fibroblast Traf2 loss, but not Sphk1 loss, disrupts TNF-induced NF-kappaB and MAPK signaling. Their introduction summarises the field as holding that "the main function of TRAF2 in TNF-induced NF-κB is to recruit cIAPs to the TNFR1-SC". Combined with the absence of an E2 interface (PMID:19810754), this weakens the S1P-cofactor E3 model (PMID:20577214). GO:0004842, GO:0061630 and GO:0051865 remain UNDECIDED, and PMID:20577214 is now flagged DISPUTED.

**Action changes from the previous version:**
- GO:0007165 signal transduction: ACCEPT changed to TOO_GENERAL, because GO:0033209 is accepted and descends from it.
- GO:0046872 metal ion binding: KEEP_AS_NON_CORE changed to TOO_GENERAL, because zinc ion binding is kept.
- GO:0046328 regulation of JNK cascade: ACCEPT changed to MODIFY, replaced by GO:0046330 positive regulation of JNK cascade (TNF and IRE1 evidence).
- Three NEW terms were added, as listed above.
- Core functions now include GO:0005164 receptor binding as a second function, and GO:0043123 and GO:0046330 as processes.
- The description was rewritten to cover NIK and non-canonical NF-kappaB restraint and the IRE1 link.

**Relative.** Human TRAF2 Q12933 is in the same PANTHER subfamily (SF21) and under the same PAINT TRAF2-clade node. It already has a complete review in `genes/human/TRAF2/`.

**Modules.** `modules/tnf_signaling.yaml` (TRAF2 adaptor part) and `modules/nfkb_canonical_signaling.yaml`.
