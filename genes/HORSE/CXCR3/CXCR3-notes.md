# CXCR3 notes


## 2026-09-08 paired review

Selected accession A0A9L0T1D1; ordinary UniProt record is TrEMBL and cites genome sequencing/submission rather than a gene-specific functional experiment. Human evidence is summarized in [the paired human investigation](../../human/CXCR3/CXCR3-notes.md). [Sequence comparison](CXCR3-bioinformatics/RESULTS.md) records the exact target gaps and transfer limits. Direct horse CXCR3 expression evidence exists (PMID:31256888), motivating a horse-specific Edison request; expression is not a ligand-binding validation.

CXCR3-A and CXCR3-B share the seven-transmembrane receptor core but differ at the N terminus and in signaling behavior. In the directly inspected Lasagni study, CXCR3-A supports cell survival/proliferation, whereas CXCR3-B supports endothelial growth inhibition and apoptosis; CXCL4 preferentially binds the B isoform. The paper explicitly includes a negative competition panel containing CCL3, CCL4 and CCL5/RANTES. That experiment is decisive against treating the named ligand list in the horse model output as established. It does not prove that every conceivable CC ligand fails to interact with every CXCR3 isoform. The C-C receptor/binding IBA annotations require tracing the curated ancestral claim and its actual experimental grounding, not counting donor proteins.

Sources: [PMID:12782716](https://pubmed.ncbi.nlm.nih.gov/12782716/), [PMID:31256888](https://pubmed.ncbi.nlm.nih.gov/31256888/).

## Horse Edison investigation

The horse Falcon/Edison report completed and is preserved as CXCR3-deep-research-falcon.md with its artifact. It distinguishes direct horse expression evidence from mammalian receptor-mechanism transfer and identifies exercise-expression and EHV-1 chemokine studies as further source leads. The EHV-1 migration study does not directly block or disrupt CXCR3, so it is not treated as receptor-specific validation. The independently checked human ligand experiments remain the basis for the ProtNLM ligand-specificity assessment.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

**Identity.** Benchmark accession A0A9L0T1D1 (369 aa, TrEMBL, Ensembl ENSECAP00000082094 / gene ENSECAG00000023587, chromosome X) is a full-length CXCR3 product, the counterpart of human CXCR3-A (P49682, 368 aa; 90.8% identity over 368 paired residues). It is not a fragment. The only other horse UniProt entry for the gene, F6U4S6 (392 aa, transcript ENSECAT00000025236), is identical from residue 8 onward but carries a 23-residue N-terminal extension that does not begin with Met and is only 25% identical to the human CXCR3-B N-terminal exon, so it looks like an incomplete alternative gene model rather than evidence of a horse CXCR3-B. No reviewed horse CXCR3 entry exists. [file:HORSE/CXCR3/CXCR3-bioinformatics/RESULTS-rereview.md]

**Evolutionary grounding.** UniProt places A0A9L0T1D1 in PANTHER PTHR10489:SF671 (C-X-C chemokine receptor type 3), the same subfamily as human P49682, mouse O88410, dog Q5KSK8 and bovine Q5MD61 (85.8-90.8% identity). Paralogous chemokine receptors in other subfamilies (CXCR1 SF916, CXCR2 SF689, CXCR4 SF594, CCR5 SF686, zebrafish cxcr3.2 SF947) are only 37-42% identical. A small NJ tree is consistent (horse sister to dog CXCR3). Human sulfotyrosines Y27/Y29, N-glycosylation sites N22/N32, the C124-C203 disulfide and the DRY motif all map to conserved horse residues. So CXCR3 subfamily-specific functions (CXCL9/10/11 receptor activity) transfer. Horse has no IBA rows. The human IBA rows come from the broad chemokine-receptor node PTN001628461, including C-C chemokine receptor activity and C-C chemokine binding, which the human review left UNDECIDED; I did not propose them for horse. ARBA text on the horse record calls CXCR3 a receptor for CCL21. That is mouse biology: the human record carries a CAUTION that human CCL21 does not bind CXCR3. I did not use it.

**Literature.** Human CXCR3 is selective for IP10/CXCL10 and Mig/CXCL9, mediates Ca2+ mobilization and chemotaxis, and is expressed on IL-2-activated T cells [PMID:9064356 "It mediates Ca2+ mobilization and chemotaxis in"]. Both CXCR3-A and CXCR3-B bind CXCL9/10/11, and CXCR3 drives chemotaxis of activated Th1 cells, NK cells, macrophages and DCs [PMID:12782716 "the interaction of CXCL9, CXCL10, and CXCL11 with CXCR3 also results in the chemotaxis of activated Th1 cells (17, 18)"]. Horse-specific evidence covers expression only: mRNA in wounded skin [PMID:31256888] and, per the falcon report, in blood after exercise. No horse ligand-binding or signalling assay exists.

**Changes to annotations.**
- GO:0016494 C-X-C chemokine receptor activity, GO:0070098 chemokine-mediated signaling pathway, GO:0005886 plasma membrane and GO:0009986 cell surface: ACCEPT.
- GO:0004930 GPCR activity and GO:0004950 chemokine receptor activity: changed from ACCEPT to MODIFY, replaced by GO:0016494. Both are correct but general, and the specific term is already carried.
- GO:0007165 signal transduction (was UNDECIDED) and GO:0007186 GPCR signaling pathway (was ACCEPT): MODIFY, replaced by GO:0070098.
- GO:0006935 chemotaxis: MODIFY, replaced by GO:0010818 T cell chemotaxis.
- GO:0016020 membrane: MODIFY, replaced by plasma membrane (was KEEP_AS_NON_CORE).
- GO:0002685 regulation of leukocyte migration and GO:0006954 inflammatory response: KEEP_AS_NON_CORE (both were ACCEPT).
- I rewrote the description and core function: CXC chemokine receptor at the plasma membrane, involved in chemokine signalling and T-cell chemotaxis. Isoform claims are now stated as unknown for horse.

**Relative.** Human CXCR3 (P49682) is the SF671 ortholog with experimental evidence. Its review, genes/human/CXCR3/CXCR3-ai-review.yaml, is complete. Family review interpro/panther/PTHR10489/PTHR10489-review.yaml places human and horse CXCR3 in SF671, which agrees with this placement. Module: modules/chemokine_signaling.yaml.
