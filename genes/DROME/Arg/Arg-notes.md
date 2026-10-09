# Arg (CG18104, O76895) notes

Module: dmel_arginine_metabolism (with Ass, Argl).

## Literature journal
- Samson 2000 cloned the single fly arginase, nested around elav: [PMID:10878001 "A Drosophila gene encoding a 351-amino acid-long predicted arginase (40% identity with vertebrate arginases) is reported."]
- Insect arginase is not a urea-cycle/ammonia-detox enzyme: [PMID:10878001 "Most organisms, including insects, produce only one type of arginase, whose function is not centered on ammonia detoxification."]
- Expression: [PMID:10878001 "During embryogenesis, the arginase transcripts localize to the fat body."]; mutant is viable with delay [PMID:10878001 "this recessive allele causes a developmental delay but does not affect viability."]
- No urea cycle in insects: [PMID:40081835 "no insect can synthesize arginine via the urea cycle, as ornithine carbamoyltransferase is absent from all genomes analysed"]; arginase retained [PMID:40081835 "all insects (except some Hemiptera) can degrade it to ornithine and urea, as the arginase (ARG) gene is conserved across the orders analysed"]
- Mitochondrial Mn enzymes listed in a fly Mn-depletion study: [PMID:31799578 "three mitochondrial enzymes: superoxide dismutase (Sod2), arginase"] (general statement, not a fly localisation experiment).
- Sequence: N-terminus MWWSRKFASRSLRLHRLKST is Arg/Lys-rich with no acidic residues, resembling a mitochondrial presequence (my inspection of the UniProt sequence; no TargetP run).
- Deep research (falcon) agrees: localisation unproven; DJ-1beta PD model shows Arg/Argl transcript increase (Solana-Manrique 2022, not cached).

## Decisions
- urea cycle (IEA UniPathway): REMOVE (no OTC in insects). Same call on Ass.
- ammonium excretion (ISS from Aedes): MARK_AS_OVER_ANNOTATED.
- mitochondrion ISS: ACCEPT; cytosol IBA: UNDECIDED; cytoplasm IBA: KEEP_AS_NON_CORE.
