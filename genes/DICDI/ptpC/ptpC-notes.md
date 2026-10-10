# ptpC (PTP3) notes — Dictyostelium discoideum, UniProt P54637

## Deep research status

- `just deep-research-falcon DICDI ptpC --fallback perplexity-lite` was run on 2026-10-05 and
  FAILED: falcon returned HTTP 402 Payment Required, and the perplexity-lite fallback
  reported "Provider 'perplexity' not available. Available: openai, falcon, openscientist".
  No deep-research file was produced; this review is based on the cached publications below
  and PubMed searches ("PTP3 Dictyostelium" returned 9 PMIDs, all now cached).

## Protein

- 990 aa non-receptor PTP; single PTP catalytic domain (aa 422-715; PF00102, PS00383 active-site
  signature), flanked by long disordered N- and C-terminal regions (UniProt). PANTHER
  PTHR19134:SF549.
- Two genomic copies in JH10/Ax3 background; one could be disrupted (slow growth), the other was
  refractory, suggesting essentiality [PMID:8628311 "There are two copies of the PTP3 gene in this
  haploid organism"; "We were unable to obtain a strain with disruptions in both PTP3 genes"].

## Catalytic activity

- Recombinant PTP3 has vanadate-sensitive phosphatase activity [PMID:8628311 "Recombinant PTP3
  exhibited phosphatase activity that was inhibited by vanadate"]. Intrinsic activity of the
  bacterial enzyme is low and the PTP3 sequence is divergent at otherwise conserved residues
  [PMID:18305004 "the bacterially produced enzyme has a very low intrinsic phosphatase activity"].
- C-to-S substrate-trapping mutant forms a stable complex with tyrosine-phosphorylated p130 (pp130)
  [PMID:10207040 "Mutation of the catalytically essential Cys to a Ser results in inactive PTP3 that
  forms a stable complex with tyrosine-phosphorylated p130 (pp130) in vivo and in vitro"].
- pp130 was later identified as STATc [PMID:18305004 "STATc is the 130 kDa stress-responsive
  tyrosine phosphorylated protein"]. PTP3 directly interacts with and dephosphorylates STATc
  [PMID:18305004 "We show that PTP3 directly interacts with and dephosphorylates STATc"], removing
  phosphate from Tyr922 [PMID:24587195 "PTP3 is constitutively active in its non-phosphorylated form
  and removes the phosphate from Tyr922 of STATc."].

## Biological role: STATc deactivation and its regulation

- PTP3 overexpression makes STATc refractory to activation; a dominant inhibitor (substrate trap)
  causes constitutive Tyr phosphorylation and ectopic nuclear localisation of STATc [PMID:18305004].
- DIF-1 and hyperosmotic stress inhibit PTP3 (transient 20% vs stable 40% activity decrease) and
  induce Ser/Thr phosphorylation of PTP3, an atypical STAT-activation mechanism where the phosphatase
  arm is regulated [PMID:18305004].
- Phosphosites S448 and S747; Ca2+-elevating agents stimulate their phosphorylation and activate
  STATc [PMID:20159963 "stress-induced Ca(2+) signalling represses STATc dephosphorylation through
  its inhibitory effect on PTP3"].
- Actin cytoskeleton disruption (latrunculin A, cytochalasin A) and DIF-1 increase S747
  phosphorylation [PMID:22365144].
- The TKL kinase Phg2 binds PTP3 in vitro and is required for full S747 phosphorylation
  [PMID:24587195 "The pull-down experiments showed for both approaches in vitro binding of Phg2 to
  PTP3."].
- CblA (Cbl homologue) positively regulates STATc by downregulating PTP3 [PMID:18840649].
- Pyk2 (the STATc Tyr922 kinase) co-IPs with PTP3 and they co-localize in stress-induced granules
  [PMID:25143406 "Biochemical coimmunoprecipitation analysis confirms that there is a Pyk2 and PTP3
  interaction"]. STATc kinase is constitutive; the PTP3 phosphatase arm is the regulated arm for
  DIF-1 [PMID:22699506].
- ptpC expression is induced by sorbitol in a STATc- and cGMP-dependent manner (positive feedback)
  [PMID:24587195].

## Localization

- Cytosolic in unstimulated cells; upon stress, translocates to structures that co-localize with
  endosomal vesicles, independently of its activity [PMID:10207040]. Stress granules shared with
  Pyk2 [PMID:25143406].
- Expression enriched in anterior-like and prestalk cells (lacZ reporter) [PMID:8628311].

## Curation decisions summary

- PTP activity (IDA x2, IEA): accept; core.
- protein binding IPI with STATc (Q54BD4): MODIFY to STAT family protein binding (GO:0097677).
  The PMID:12220630 IPI (OSBPa paper) is abstract-only; the abstract does not mention PTP3/STATc,
  but per project rules I do not remove a curator IPI; the STATc interaction itself is
  independently established by PMID:18305004.
- protein binding IPI with Phg2 (Q54QQ1): MODIFY to protein kinase binding (GO:0019901).
- protein localization to nucleus (IMP): direction is wrong — PTP3 opposes STATc nuclear
  accumulation; MODIFY to negative regulation of protein localization to nucleus (GO:1900181).
- Proposed NEW: peptidyl-tyrosine dephosphorylation (GO:0035335) — PTP3 itself performs the
  dephosphorylation step on STATc Tyr922.
