# HSPA4 notes


## 2026-09-08 paired review

Selected accession A0A9L0S5Z5; ordinary UniProt record is TrEMBL and cites genome sequencing/submission rather than a gene-specific functional experiment. Human evidence is summarized in [the paired human investigation](../../human/HSPA4/HSPA4-notes.md). [Sequence comparison](HSPA4-bioinformatics/RESULTS.md) records the exact target gaps and transfer limits. The targeted Europe PMC search found no decisive gene-specific horse functional assay warranting a separate horse Edison investigation; general omics/association hits were not counted as mechanistic validation.

Apg2/HSPA4 belongs to the Hsp110 branch of the Hsp70 superfamily. Human biochemical work measures its effect on the Hsc70 ATPase cycle, aggregate binding and refolding. The concentration dependence is important: low Apg2 stimulates the system, while high concentrations can inhibit it. Its acidic and C-terminal regions regulate association and exchange. Those studies do not make HSPA4 the Hsp70L1 subunit of the Mpp11/Hsp70L1 ribosome-associated complex. General chaperone activity is transferable at a broader level than membership of a specific ribosome-bound assembly. A Tom40-import annotation must be checked in the complete original paper, since its abstract emphasizes Hsp90 rather than resolving every chaperone tested.

Sources: [PMID:30521813](https://pubmed.ncbi.nlm.nih.gov/30521813/), [PMID:36167183](https://pubmed.ncbi.nlm.nih.gov/36167183/), [PMID:36604744](https://pubmed.ncbi.nlm.nih.gov/36604744/), [PMID:15644312](https://pubmed.ncbi.nlm.nih.gov/15644312/).

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Deep research: `just deep-research-falcon HORSE HSPA4 --fallback perplexity-lite` was run and failed (falcon "Failed to authenticate"; perplexity-lite HTTP 401 insufficient quota). No deep-research file exists for this folder; this re-review uses the cached primary literature below, PANTHER/PAINT files, and a new sequence analysis.

### Identity of the benchmark accession (alternative gene model)

[RESULTS-rereview.md](HSPA4-bioinformatics/RESULTS-rereview.md) (script `compare_models_rereview.py`, inputs fetched from UniProt and Ensembl REST on 2026-10-20):

- All four horse HSPA4 UniProt entries (F6YZJ4 840 aa, A0A9L0S1K5 821 aa, A0A9L0TEF0 811 aa, A0A9L0S5Z5 800 aa) are products of one Ensembl gene, ENSECAG00000020813, and all are in PANTHER PTHR45639:SF6.
- The Ensembl canonical transcript is ENSECAT00000023133 → F6YZJ4 (840 aa, 19 exons), collinear with human P34932 over all 840 residues (96.9% identity).
- The benchmark A0A9L0S5Z5 is ENSECAT00000106098 (18 exons). It is identical in exon structure to the canonical transcript except that it skips one 120-nt exon (chr14:41857288-41857407), giving an in-frame 40-residue deletion of human residues 679-718 (`KNLGQPIKIRFQESEERPKLFEELGKQIQQYMKIISSFKN`).
- This segment lies in the alpha-helical C-terminal region (UniProt Pfam HYOU1_C domain starts at horse 682). It is 90-95% conserved in mouse, rat and dog HSPA4 and about 50-58% identical in HSPA4L and HSPH1. So it is a conserved Hsp110 feature, not an HSPA4-specific insertion.
- The N-terminal nucleotide-binding domain and the substrate-binding domain (including the acidic subdomain) are fully retained. No catalytic or ATP-binding residue is lost.
- UniProt lists no corresponding human isoform: human P34932-2 is a different, truncating variant (VSP_056885, 109-800 missing). Whether the horse exon-skip transcript is real and abundant is not established.

Conclusion: A0A9L0S5Z5 is an alternative-splice gene model of horse HSPA4, not the canonical product. The canonical product of the same gene is F6YZJ4, which has no review in the repo (folder genes/HORSE/HSPA4 is keyed to A0A9L0S5Z5).

### Evolutionary grounding

- PANTHER PTHR45639:SF6 (HEAT SHOCK 70 KDA PROTEIN 4) contains horse, human (P34932), mouse (Q61316), rat (O88600) and dog (Q2TFN9) HSPA4. HSPA4L is SF5 and HSPH1 is SF2.
- PAINT (interpro/panther/PTHR45639/PTHR45639-paint.tsv): GO:0000774 adenyl-nucleotide exchange factor activity is asserted at PTN002900795, seeded by Sse1/Sse2 (SGD), Msi3 (CGD) and human HSPH1 Q92598. Human HSPA4 inherits it by IBA. Cytosol, nucleus and protein folding come from PTN000452854.
- GO:0016887 ATP hydrolysis activity is asserted only at PTN000452648, seeded by conventional Hsp70s (DnaK, HSPA1A/B, HSPA8, HSPA5, Ssa/Ssb/Kar2). Human HSPA4 has no IBA for it, so it is not propagated to the HSPA4 subfamily, and I treat that as deliberate. A NOT for protein refolding (GO:0042026, IRD at PTN001065099) is also present in the family; I did not propose any refolding process term.

### Literature

- [PMID:16688212 "Here, we show that members of the Hsp70-related Hsp110 family cooperate with Hsp70 in protein folding in the eukaryotic cytosol."] and ["...suggesting that the nucleotide exchange activity of Sse1p requires a functional ATP binding domain."]
- [PMID:22990239 "This Hsp110 effect relies on nucleotide exchange, not on ATPase activity, implying ATP-driven chaperoning is not required."]
- [PMID:30521813 "Apg2 shows a biphasic behavior: at low concentration, it stimulates the ATPase cycle of Hsc70..."]
- [PMID:36167183 "Apg2, one of the three cytosolic Hsp110 chaperones in humans, supports reactivation of unordered and ordered protein aggregates by Hsc70 (HspA8)."] The C-terminal extension's helical first part binds the Hsc70 NBD, and its disordered tail downregulates exchange.

### Changes to the review

- ATP binding: changed KEEP_AS_NON_CORE to ACCEPT. The NBD is fully intact, and ATP binding is mechanistically required for Hsp110 NEF activity.
- cytoplasm: changed ACCEPT to MODIFY, with cytosol (GO:0005829) as the replacement. Cytoplasm is a correct but general term.
- ATP hydrolysis activity: changed UNDECIDED to MARK_AS_OVER_ANNOTATED. This is a family-wide InterPro2GO mapping, PAINT omits the term for the Hsp110/HSPA4 clade, and NEF function is independent of ATPase.
- NEW GO:0000774 adenyl-nucleotide exchange factor activity, by subfamily membership under PTN002900795. The caveat about the missing C-terminal segment is recorded.
- Description rewritten. gene_symbol corrected from the accession to HSPA4. Core function set to NEF activity in the cytosol.
- No ribosome-associated complex, mitochondrial import, or TJP1 interaction (ARBA) claims were transferred.

### Relative and modules

- Relative per the campaign rule: the same-gene canonical product F6YZJ4 (horse HSPA4, 840 aa), which has no review. The closest experimentally characterised ortholog is human HSPA4 P34932 (genes/human/HSPA4, status COMPLETE). Its review is largely templated: many protein-binding rows are UNDECIDED, and ATP hydrolysis is UNDECIDED.
- PANTHER family review interpro/panther/PTHR45639/PTHR45639-review.yaml places A0A9L0S5Z5 and P34932 in SF6, which agrees with UniProt. It lists A0A9L0S5Z5 as an SF6 representative, although the canonical horse model F6YZJ4 would be the better representative.
- Module: modules/heat_shock_response.yaml, part `hsp110_nef` (HSP110-family Hsp70 NEF; PTHR45639, PTN000452854). HSPA4 is not listed as a representative member there.
