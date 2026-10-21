# USP8 (horse, F7BV54) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

**Scope.** F7BV54 (Ensembl ENSECAT00000007330, 1117 aa) is the product of horse USP8 (ENSECAG00000006611, VGNC:24856) that matches human canonical P40818-1 end to end. It was chosen as the transfer reference for the horse USP8 benchmark entry A0A9L0T7K6 (genes/HORSE/USP8), which uses an alternative 3' terminal exon. No ProtNLM2 file or prediction-evidence folder was opened for this review.

**Deep research.** `just deep-research-falcon HORSE USP8__F7BV54 --fallback perplexity-lite` failed: falcon "Exception: Failed to authenticate"; the perplexity-lite fallback returned HTTP 401 (insufficient quota). No deep-research file exists. The review uses the cached publications PMID:9628861, PMID:16520378, PMID:16120644, PMID:17711858, PMID:18388320, PMID:15314180 and PMID:28505279, the human USP8 Swiss-Prot record and review (genes/human/USP8), the local PTHR21646 PAINT file and a new analysis.

**Horse-specific literature.** A web search for equine USP8 (including pituitary pars intermedia dysfunction, the equine Cushing-like disease) found no experimental study of horse USP8. Every function in this review is inferred from human and mouse.

**Analysis.** `USP8__F7BV54-bioinformatics/compare_f7bv54.py` writes `RESULTS.md` and `results.json` (live UniProt and QuickGO, plus the local PAINT file).
- PANTHER: F7BV54, human P40818 and mouse Q80U87 are all PTHR21646:SF27.
- vs human P40818: 92.75% identity over 1117 paired residues, one gap (human 632). vs mouse Q80U87: 83.98%; horse has insertions relative to mouse, including 602-629, a segment that mouse lacks and human has.
- Conserved landmarks: MIT 84/84 aligned (78 identical); rhodanese 119/119; SH3-binding motif PQIDRTKKP identical; 14-3-3 motif LKRSYSSP identical (human S718 = horse S717); USP domain 333/333 aligned (331 identical); catalytic C786/H1067 = horse C785/H1066; the C-terminal YILFY strand segment is intact.
- PAINT: IBD rows seeded by human or mouse USP8 are at PTN002538135 (cysteine-type deubiquitinase activity; regulation of protein stability), PTN002728602 (positive regulation of canonical Wnt signaling), PTN008371010 (cytosol, midbody; postsynaptic density seeded by rat) and PTN008578257 (endosome organization, Ras protein signal transduction; mouse seed only). QuickGO gives human and mouse the same eight IBA rows and gives F7BV54 none. Because human (Euarchontoglires) and mouse both inherit from every one of these nodes, the nodes are ancestral to the boreoeutherian USP8 lineage that includes horse. Note: the benchmark review attributes the deubiquitinase IBD to PTN008371010; the actual DUB node is PTN002538135.

**Decisions (9 IEA rows).**
- GO:0004843 cysteine-type deubiquitinase activity: ACCEPT (core). Inherited at PTN002538135; catalytic dyad conserved.
- GO:0016579 protein deubiquitination: ACCEPT.
- GO:0010008 endosome membrane: ACCEPT (MIT domain and STAM-binding motif intact; PMID:17711858).
- GO:0005829 cytosol: ACCEPT (PAINT IBD at PTN008371010; 14-3-3 motif conserved).
- GO:0005737 cytoplasm: MODIFY to cytosol and endosome membrane (true but general).
- GO:0030496 midbody: KEEP_AS_NON_CORE (PMID:18388320; PAINT IBD).
- GO:0005634 nucleus, GO:0005886 plasma membrane: KEEP_AS_NON_CORE (weak human support; not propagated by PAINT).
- GO:0006511 ubiquitin-dependent protein catabolic process: MARK_AS_OVER_ANNOTATED. USP8 removes ubiquitin and does not perform the degradation steps. Its effect on turnover depends on the substrate: it stabilizes Nrdp1 and STAM, and the two EGFR knockdown studies disagree in direction (PMID:16520378 vs PMID:16120644). PAINT did not place this term.

**No NEW terms.** Endosome organization (PTN008578257) is inheritable by node placement, but its only seed is the mouse knockout, and the human evidence is knockdown morphology (enlarged multivesicular endosomes). That is necessity evidence; whether USP8 does the work of endosome organization, rather than being required for it, is the CLAUDE.md participation question. I have not added it to a horse entry that has no IBA rows. It is raised in suggested_questions together with the other IBA rows horse lacks. K48/K63 linkage-specific activities (human IDA) were not added because PAINT propagated only the generic activity, which is treated as a deliberate decision.
