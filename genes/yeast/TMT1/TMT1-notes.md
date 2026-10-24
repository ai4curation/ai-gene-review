# TMT1 (YER175C, P32643) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: TMT1 is being reviewed in its own right as the experimentally characterised
PTHR44942:SF4 relative of fission-yeast SPAC25B8.09 (Q9UTA9). No ProtNLM2 output was
consulted.

### Deep research

`just deep-research-falcon yeast TMT1 --fallback perplexity-lite` failed on 2026-10-21:
falcon returned `403 Forbidden` at `https://api.platform.edisonscientific.com/auth/login`
("Failed to authenticate"), and the perplexity-lite fallback also exited non-zero. No
deep-research file exists. The review is based on the three primary Clarke-lab papers
(all cached abstract-only), the curated UniProt record, and the SF4 pairwise analysis in
`genes/SCHPO/SPAC25B8.09/SPAC25B8.09-bioinformatics/RESULTS-rereview.md`. A web search
found no newer primary characterisation of Tmt1.

### Experimentally established in S. cerevisiae

- Gene identity and activity: deletion of YER175c abolishes extract methyltransferase
  activity toward trans-aconitate, cis-aconitate, isocitrate and citrate; plasmid
  reintroduction overexpresses it [PMID:11695919 "Extracts of a yeast strain with a
  disrupted YER175c gene demonstrate a complete loss of activity toward the methyl-accepting
  substrates trans-aconitate, cis-aconitate, DL-isocitrate, and citrate."].
- Substrate preference: trans-aconitate is the best of the tricarboxylates tested (Km 0.66
  mM); others are very poor [PMID:11695919 "We found that trans-aconitate was the best
  substrate with a Km of 0.66 mM."].
- Localization: activity is cytosolic and rises at the diauxic shift [PMID:11695919 "the
  activity of the yeast trans-aconitate methyltransferase is localized in the cytosol and
  increases markedly as cells undergo the metabolic transition at the diauxic shift"].
  The genome-wide GFP screen also calls it cytoplasmic (UniProt, PubMed:14562095).
- Major endogenous substrate: (2R,3S)-3-isopropylmalate (leucine pathway intermediate),
  with kinetics similar to trans-aconitate [PMID:15147181 "The Tmt1 methyltransferase
  recognizes (2R,3S)-3-isopropylmalate with similar kinetics as it does trans-aconitate"].
  Note: all measurements are in Tmt1-overexpressing extracts, not purified enzyme.
- Product and signalling: methylation yields 3-isopropylmalate-1-methyl ester, which is
  secreted and enhances haploid invasive growth; TMT1 is induced by amino-acid (especially
  leucine) starvation under Gcn4 control [PMID:18092814].
- Structure: PDB 3G5T (1.12 A, structural-genomics deposit with SAH and the trans-aconitate
  methyl ester product bound) confirms a class I Rossmann-fold SAM-MTase with product in the
  active site. No associated paper was found, so this is used only as background.

### Inferred / not established

- Detoxification of trans-aconitate (aconitase inhibitor) is the authors' proposal, not a
  demonstrated in vivo phenotype. Not annotated as a process.
- The physiological role of 3-isopropylmalate methylation (a branch from leucine
  biosynthesis to a secreted signal) is the authors' model; Tmt1 "functions independently of
  the biosynthetic pathway" [PMID:18092814]. No leucine-biosynthesis process annotation is
  warranted.
- No GO term exists for 3-isopropylmalate O-methyltransferase activity; proposed as a new
  term under GO:0010340 carboxyl-O-methyltransferase activity.

### Evolutionary context

- UniProt: PANTHER PTHR44942:SF4; "Tam family" of the methyltransferase superfamily; Pfam
  Methyltransf_31. GOA carries no IBA for TMT1; TMT1 is not a donor at PTN008676703.
- SF4 has two members in each yeast: TMT1 and CRG1 (P38892) in S. cerevisiae (36% identity),
  and the tandem pair SPAC25B8.09/SPAC25B8.10 in S. pombe. Each pombe gene is 25-29% identical
  to both TMT1 and CRG1, so 1:1 orthology to TMT1 is not resolved by pairwise data
  (RESULTS-rereview.md in the SPAC25B8.09 bioinformatics folder). SF4 also contains fungal
  natural-product O-methyltransferases, so SF4 membership does not imply a trans-aconitate /
  3-isopropylmalate acceptor.
- CRG1, the budding-yeast paralog, is reported to methylate the drug cantharidin
  (Lissina et al. 2011 PLoS Genet, doi:10.1371/journal.pgen.1002332; not cached, not cited
  in the review), which illustrates acceptor divergence within SF4.
- For transfer to relatives: the safely transferable claim is the SAM-dependent
  methyltransferase fold/activity (GO:0008757). Trans-aconitate and 3-isopropylmalate
  specificity are experimentally established only for S. cerevisiae Tmt1.

### Annotation decisions

- GO:0046547 trans-aconitate 3-methyltransferase activity (IDA, IEA): ACCEPT, core.
- GO:0005829 cytosol (IDA x2): ACCEPT.
- GO:0005737 cytoplasm (IEA, SubCell): MODIFY to cytosol.
- GO:0034198 cellular response to amino acid starvation (IDA): KEEP_AS_NON_CORE; the
  abstract supports Gcn4-dependent induction plus production of a secreted signal under
  starvation; induction alone is weak support for participation, but the curator read the
  full text.
