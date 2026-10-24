# Gpdh1 (P13706, FBgn0001128, CG9042) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: Gpdh1 is the closest experimentally characterised paralog of the ProtNLM2 benchmark gene
Gpdh3 (E1JIT1). Both are in PANTHER PTHR11728:SF8 and descend from fly clade node PTN000198082.
This review covers Gpdh1 in its own right; no ProtNLM2 file or prediction-evidence folder was
opened or used.

### Deep research

`just deep-research-falcon DROME Gpdh1 --fallback perplexity-lite` failed: falcon raised
"Failed to authenticate" and the perplexity-lite fallback returned HTTP 401 (quota exceeded).
No deep-research file exists. This review uses the cached GOA publications plus one additional
paper fetched for this review (PMID:9307964, Wojtas et al. 1997).

### Sequence and family (UniProt P13706)

- 360 aa (isoform B displayed), NAD-dependent glycerol-3-phosphate dehydrogenase family;
  Pfam NAD_Gly3P_dh_N (PF01210) and NAD_Gly3P_dh_C (PF07479), NCBIfam TIGR03376, PIRSF000114,
  PROSITE PS00957.
- UniProt curated reaction: sn-glycerol 3-phosphate + NAD(+) = DHAP + NADH + H(+) (RHEA:11092, EC 1.1.1.8).
- Active-site proton acceptor K206 and NAD-binding GxGxxG loop (11..16) annotated by similarity (ECO:0000250).
- Three isoforms differ only at the C-terminus: B (DTSIMPSPKL), C (ends QNL; the flight-muscle
  GPDH-1 isozyme), A (truncated at 350). These correspond to the classical larval/adult isozymes
  that Bewley & Lucchesi showed derive from one structural gene [PMID:405967 "all alpha-GPDH
  isozymes are the product of a single structural gene"].

### Phylogenetic grounding

PAINT (PTHR11728-paint.tsv): Gpdh1 (FB:FBgn0001128) is an experimental donor for IBD nodes
PTN000919759 (GO:0047952, NAD(P)+-dependent G3P dehydrogenase activity) and PTN000198006
(GO:0006072 glycerol-3-phosphate metabolic process; GO:0005829 cytosol). The IBAs on Gpdh1 are
therefore inherited from deep eukaryotic nodes that Gpdh1 itself helped to place; the target
appearing in its own WITH/FROM is expected. PAINT placed the activity at the NAD(P) level for the
family; Gpdh1-specific biochemistry (purified enzyme, kinetics) supports NAD+.
A NOT (IRD) is placed on PTN001712215 (taxon 7227), which is not the Gpdh1 leaf.

### Experimental findings (this species)

- Activity: enzyme purified to homogeneity from flies [PMID:109448]; larval vs adult isozyme
  kinetics [PMID:4204332, abstract not available in cache]; null alleles abolish all isozymes
  [PMID:405967 "\"null\" mutations at the Gpdh locus obliterate all isozymatic species"].
- G3P production: Gpdh1 CRISPR null (A10) larvae have decreased G3P
  [PMID:35536221 "G3P levels were significantly decreased in relative to the control strain"].
  Ldh mutants overproduce G3P, and Ldh; Gpdh1 double mutants show growth defects, synthetic
  lethality and decreased glycolytic flux [PMID:31399469].
- G3P shuttle: classical work (O'Brien & MacIntyre) plus [PMID:405967] on the
  alpha-glycerophosphate cycle; Gpdh1 reduces DHAP in cytosol, mitochondrial GPO1 oxidises G3P.
  Reduced activity lowers wing-beat frequency [PMID:16204217].
- TAG: 33-80% activity reductions give small decreases in triglyceride [PMID:16204217]; G3P is
  the glycerol backbone precursor (Gpdh1 supplies a precursor; it is not an acyltransferase).
- Sarcomeric localization: GPDH at Z-discs and M-lines of flight muscle; only the QNL-ending
  isoform (GPDH-1, UniProt isoform C) localizes and supports flight; GPDH null prevents
  localization of aldolase and GAPDH [PMID:9307964; PMID:12756285]. Y2H: GPDH-GAPDH and
  GPDH-PGLYM interactions [PMID:12756285].
- Oogenesis/embryogenesis/lifespan requirement [PMID:35536221] — phenotypes, not process
  participation; not proposed as NEW.
- Ethanol tolerance increases with GPDH activity [PMID:19033156] (abstract only; tolerance is a
  phenotype, ethanol metabolism itself not measured in the abstract).
- Hyperoxia: P-element (EY01534) line with reduced Gpdh mRNA survives high O2 better
  [PMID:20668515] — an indirect selection/phenotype result.

### Decisions summary

Core: GO:0141152 G3P dehydrogenase (NAD+) activity, in cytosol (and isoform C at Z disc/M band),
supporting G3P biosynthesis and the G3P shuttle. Phenotype-derived process rows (flight behavior,
response to hyperoxia) marked over-annotated; glycolysis (IGI with Ldh) marked over-annotated
because Gpdh1 regenerates NAD+ alongside, but is not a step of, glycolysis. Ethanol metabolic
process left UNDECIDED (full text not readable).

### Transfer guidance for Gpdh3

Experimentally established in D. melanogaster for Gpdh1 only: NAD+-dependent G3P dehydrogenase
activity, cytosolic localization, isoform-C-specific sarcomere targeting via the C-terminal QNL
tripeptide, G3P biosynthesis and the G3P shuttle. The sarcomere targeting depends on an isoform-
specific C-terminus that Gpdh3 does not share and should not be transferred.
