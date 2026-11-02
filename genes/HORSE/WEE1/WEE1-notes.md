# WEE1: paired human–horse review notes

## Biological evidence

Human WEE1 is a nuclear CDK-inhibitory tyrosine kinase. Direct assays distinguish CDK1 Tyr15 phosphorylation from Thr14 phosphorylation. Mouse egg-activation experiments distinguish WEE2/Wee1B from WEE1/Wee1A: WEE2 depletion blocks pronuclear formation, whereas WEE1 depletion does not in that assay.

- [PMID:8428596: Human Wee1 kinase inhibits cell division by phosphorylating p34cdc2 exclusively on Tyr15.](https://pubmed.ncbi.nlm.nih.gov/8428596/) — abstract cached; full-text availability must be checked separately.
- [PMID:7743995: Regulation of the human WEE1Hu CDK tyrosine 15-kinase during the cell cycle.](https://pubmed.ncbi.nlm.nih.gov/7743995/) — abstract cached; full-text availability must be checked separately.
- [PMID:8348613: Human wee1 maintains mitotic timing by protecting the nucleus from cytoplasmically activated Cdc2 kinase.](https://pubmed.ncbi.nlm.nih.gov/8348613/) — abstract cached; full-text availability must be checked separately.
- [PMID:21454751: Protein tyrosine kinase Wee1B is essential for metaphase II exit in mouse oocytes.](https://pubmed.ncbi.nlm.nih.gov/21454751/) — full text cached.
- [PMID:37527245: Oocyte-specific Wee1-like protein kinase 2 is dispensable for fertility in mice.](https://pubmed.ncbi.nlm.nih.gov/37527245/) — full text cached.

## Exact horse model

The full646-residue horse protein closely matches human WEE1 at95.4% identity. Nuclear phosphorylation is supported. The specific female-pronucleus prediction has a plausible paralog-transfer explanation, but remains UNC: differential necessity does not exclude redundant participation. Broad meiotic claims likewise remain unresolved. Electronic Ser/Thr assignments are refined to the demonstrated tyrosine activity.

The reproducible alignment, source paths and hashes are in [the paired comparison](../../HORSE/WEE1/WEE1-bioinformatics/RESULTS.md). Current UniProt sequences have not been proven identical to the original ProtNLM input sequences. Sequence anomalies are therefore recorded as model/transfer limitations, not as proven wrong-input pipeline errors.

## Evidence gaps

The2023Wee2 knockouts retain substantial fertility and support possible biological redundancy, so do not claim WEE2 is universally essential or WEE1 can never compensate. Check horse oocyte expression/perturbation before scoring broad meiosis. Separate kinase catalysis from regulation of a different phosphorylation reaction.

## Review scope and checks

Every seeded annotation receives a current assessment. UNDECIDED marks unresolved source-specific or biological evidence; these are initial reviews rather than a claim that every original experimental assay has been independently reproduced or verified. The human Edison report is retained as a research synthesis and source-finding aid; decisive YAML excerpts cite primary publications, source records or reproducible analysis. The validator advisory to cite the deep-research file is deliberately not satisfied by citing AI prose as biological proof.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

### Identity of the benchmark accession
- F6TY09 (TrEMBL, Ensembl ENSECAP00000018436, VGNC:25026 WEE1, chr 7) is the canonical full-length horse WEE1: 646 aa, the same length as human WEE1 P30291, 95.4% identity over the whole length (file:HORSE/WEE1/WEE1-bioinformatics/RESULTS.md). Not a fragment, isoform or alternative gene model. Kinase domain 299-569, predicted proton acceptor D426, PIRSR ATP (305-313, K328) and Mg2+ (431, 463) positions all present.
- Phylogenetic placement: PANTHER PTHR11042:SF72 (WEE1-LIKE PROTEIN KINASE), the same subfamily as human P30291, mouse P47810 and rat Q63802 WEE1. WEE2 orthologs sit in SF75, PKMYT1/wee-1.1/wee-1.3 in SF183, S. pombe wee1 in SF196, Drosophila Wee1 in SF185 (interpro/panther/PTHR11042/PTHR11042-entries.csv). So human WEE1 is the experimentally characterised ortholog to transfer from; WEE2 oocyte/meiotic functions must not be transferred.
- PAINT: GO:0004713 IBD at PTN008510964 (seeds FB Wee1, human WEE1, Xenopus wee2-a); GO:0010972 IBD at PTN008510965 (seed human WEE1); nucleus/cytoplasm IBD at the deep node PTN000113601. GO:0004674 (Ser/Thr kinase) was placed by PAINT at PTN008683913, which does not reach the WEE1 clade (no IBA for it on F6TY09) — read as a deliberate decision.
- UniProt caveat: the F6TY09 FUNCTION comment is ARBA-derived (ARBA00059782) and describes the oocyte-specific WEE2 paralog (meiotic arrest, MII exit, pronuclear formation); the Meiosis keyword is likewise ARBA. These are mis-transfers from the paralog and are not used as evidence.

### Deep research
- `just deep-research HORSE WEE1 --provider falcon` failed (Edison "Failed to authenticate"); no deep-research file was created for horse. Relied on the human WEE1 falcon report (genes/human/WEE1/WEE1-deep-research-falcon.md) as a source-finding aid and on cached primary abstracts PMID:8428596, PMID:7743995, PMID:8348613.

### Changes vs previous review
- Description rewritten as a standalone biological summary (removed comparison prose about the horse model).
- GO:0000278 mitotic cell cycle: ACCEPT -> MODIFY to GO:0010972 (correct but general; gene already carries the specific term).
- Ser/Thr kinase rows (GO:0004674, GO:0106310): MODIFY -> GO:0004713 kept, reasoning now grounded in PAINT node placement and Tyr15-only specificity of human WEE1 ("purified human Wee1 phosphorylates p34cdc2 exclusively on Tyr15 in vitro; no Thr14 phosphorylation was detected" [PMID:8428596]).
- Generic kinase/transferase rows: MODIFY -> GO:0004713 (unchanged action, new evolutionary reasoning).
- ATP/nucleotide/Mg binding: ACCEPT, now supported by PIRSR site features and SF72 membership rather than identity alone.
- Nucleolus (Compara copy of human HPA IDA): UNDECIDED, consistent with the human review.
- Cytoplasm: KEEP_AS_NON_CORE. Nucleus, PTK, non-membrane PTK, G2/M negative regulation: ACCEPT.
- No NEW terms: meiotic/oocyte processes belong to WEE2 (SF75); DNA-damage checkpoint roles are not separately annotated for this gene in GOA and were not added.
