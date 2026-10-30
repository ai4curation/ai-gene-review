# USP8: paired evidence notes

Human reference: https://www.uniprot.org/uniprotkb/P40818/entry

Primary source: [PMID:9628861 UBPY: a growth-regulated human ubiquitin isopeptidase.](https://pubmed.ncbi.nlm.nih.gov/9628861/).

> We have identified and 
> characterized a novel human ubiquitin isopeptidase, UBPY, which both as a 
> recombinant protein and upon immunoprecipitation from cell extracts is able to 
> cleave linear or isopeptide-linked ubiquitin chains.

The horse sequence comparison is in [USP8-bioinformatics/RESULTS.md](USP8-bioinformatics/RESULTS.md). Transfer is assessed for this exact accession; human biochemical evidence is not equine experimental validation.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

**Deep research.** `just deep-research HORSE USP8 --provider falcon` failed ("Exception: Failed to authenticate"; "All providers failed"). No deep-research file was written. The review uses the cached publications (PMID:9628861, PMID:16520378, PMID:17711858, PMID:18388320, PMID:15314180, PMID:28505279), the human USP8 UniProt record and review, the PTHR21646 PAINT data, and new gene-model analysis.

**Identity of A0A9L0T7K6 (alternative gene model, alternative 3' terminal exon).** New analysis `USP8-bioinformatics/compare_horse_models_rereview.py` writes `RESULTS-rereview.md` and `results-rereview.json` (live UniProt fetch). The original RESULTS.md was left untouched.
- Horse USP8 is Ensembl ENSECAG00000006611 (chr1, minus strand). It has eight protein-coding transcripts. Four are in UniProt (all unreviewed, PE 3, all in reference proteome UP000002281, all in PANTHER PTHR21646:SF27). A0A9L0T7K6 has no gene name in UniProt, so a `gene:USP8` search does not return it. Its Ensembl gene is nonetheless USP8.
- Benchmark A0A9L0T7K6 = ENSECAT00000088864, 1112 aa (human P40818-1 is 1118 aa). It is the only transcript that leaves the shared last exon at 140806039 and splices to two exons about 20 kb further 3' (140802872-912, 140786509-595). The protein matches human through ...KSSAA (human ~1101). It then ends with SFSLHFREISQS instead of YILFYTSLGPRVTDVAT. The C-terminal YILFY strand segment of the USP domain is replaced. The USP domain has 328/333 human positions aligned.
- Retained: full MIT domain (84/84), rhodanese domain (119/119), SH3-binding motif, the 601-629 segment absent from human isoform 2, the 14-3-3 site (human S718 = horse S717), and the catalytic Cys785/His1066 (human C786/H1067). Identity is 91.8% over 1112 paired residues.
- Other models: F7BV54 (ENSECAT00000007330, 1117 aa) matches human isoform 1 end to end except for a 1-residue gap at human 632. It is the structural equivalent of the human canonical product. A0A3Q2HXC7 (ENSECAT00000030247, 1139 aa) carries the Ensembl canonical flag but has a 22-residue insertion at horse 84-105 inside the MIT domain. A0A5F5PIL5 (1011 aa) is the human-isoform-2-like product, lacking human 35-111 (MIT) and 602-631. F7BV54, A0A3Q2HXC7 and A0A5F5PIL5 all keep the human C-terminus.
- Conclusion: A0A9L0T7K6 is an alternative splice-form product of horse USP8, not the canonical product. Whether it is catalytically active is unknown. The YILFY segment is part of the conserved C-terminal box of USP domains.

**Evolutionary grounding.** All horse USP8 models are in PTHR21646:SF27 (UBIQUITIN CARBOXYL-TERMINAL HYDROLASE 8), with human P40818 and mouse Usp8 (MGI:1934029). Human USP8 IBAs come from PAINT node PTN008371010 (cysteine-type deubiquitinase activity, cytosol, midbody, postsynaptic density) and PTN008578257 (endosome organization, Ras protein signal transduction; seed MGI:1934029). Horse has no IBA rows. This accession is not a PANTHER tree leaf, and PTHR21646-entries.csv has no horse entries. The USP8-subfamily placement still makes the human/mouse experimental functions an inheritance within the subfamily. PAINT did not propagate nucleus, plasma membrane or GO:0006511 from these nodes.

**Decisions.**
- GO:0004843 cysteine-type deubiquitinase activity: ACCEPT (core; gene-level claim; splice-form activity caveat recorded).
- GO:0016579 protein deubiquitination: ACCEPT.
- GO:0010008 endosome membrane: ACCEPT (MIT domain intact; PMID:17711858).
- GO:0005829 cytosol: ACCEPT (PAINT IBD; Ser717 14-3-3 site conserved).
- GO:0005737 cytoplasm: changed from ACCEPT to MODIFY, with cytosol and endosome membrane as replacements (true but general; both descendants are already rows).
- GO:0030496 midbody: KEEP_AS_NON_CORE (PMID:18388320; PAINT IBD).
- GO:0005634 nucleus and GO:0005886 plasma membrane: KEEP_AS_NON_CORE.
- GO:0006511 ubiquitin-dependent protein catabolic process: changed from ACCEPT to MARK_AS_OVER_ANNOTATED. It is a generic UniRule DUB transfer. USP8 stabilizes some substrates (Nrdp1, STAM, BACE1) and promotes degradation of others (EGFR, Met). Human curation uses regulatory terms instead. USP8 does not carry out the catabolic steps.
- No NEW terms. Endosome organization (human IBA) was not added, because whether this altered-C-terminus splice form takes part is untested. It is raised as a suggested question for the canonical-structure entries instead.

**Relative to review next.** By the campaign rule, the benchmark is an alternative gene model, so the relative is the canonical product of the same gene. No horse USP8 entry is reviewed in UniProt. F7BV54 is the product structurally equivalent to human P40818-1, so I chose it over the Ensembl-canonical A0A3Q2HXC7, which carries a MIT insertion. It has no review in the repo; the folder would be genes/HORSE/USP8__F7BV54. Human USP8 (genes/human/USP8, P40818) already has a full review (no PENDING rows; status field still IN_PROGRESS).

**Family review (interpro/panther/PTHR21646).** The SF27 entry lists A0A9L0T7K6 and P40818 as representative members. There is no subfamily placement disagreement: all horse models are SF27. Two issues: (1) the SF27 `description` repeats the family-level coherence prose instead of describing USP8; (2) an alternative-C-terminus splice form is a poor horse representative, and F7BV54 would be better. I did not edit the family file.

**Modules.** No module in modules/ references USP8 or P40818. The one grep hit, in tca_cycle.yaml, is the unrelated accession Q9USP8.
