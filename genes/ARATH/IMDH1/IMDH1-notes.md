# IMDH1 (Q9FMT1, At5g14200) review notes

## Identity
- IPMDH1 / AtIMD1 / MAM-D1; chloroplast-stromal NAD+-dependent isopropylmalate dehydrogenase (LeuB family), homodimer by similarity.
- [PMID:19674406 "This work characterized an enzyme in plants that catalyzes the oxidative decarboxylation step in both leucine biosynthesis (primary metabolism) and methionine chain elongation of glucosinolates (specialized metabolism)."]

## Specialization for glucosinolates
- [PMID:21697089 "AtIPMDH1 accepts both substrates with comparable k cat / K m values, but was ∼500-fold more efficient with the glucosinolate substrate than the other two isoforms."]
- Phe-137 determinant: [PMID:21697089 "Site-directed mutagenesis of Phe-137 to a leucine in AtIPMDH1 (AtIPMDH1-F137L) reduced activity toward 3-(2′-methylthio)ethylmalate by 200-fold"]
- Only IMDH1 rescues ipmdh1: [PMID:21697089 "the altered glucosinolate profile of the atipmdh1 mutant could only be rescued by expression of AtIPMDH1"]
- Mutant: [PMID:19674406 "Mutation of AtIPMDH1 leads to a significant reduction in the levels of free leucine and of glucosinolates with side chains of four or more carbons."]
- [PMID:33568694 "IPMDH1 is the major enzyme that participates in Met chain-elongation pathway, whereas IPMDH2 and IPMDH3 are functionally redundant in Leu biosynthesis with IPMDH3 playing a larger role than IPMDH2."]

## Leucine (secondary)
- [PMID:21697089 "all three AtIPMDHs are involved in leucine biosynthesis, with AtIPMDH2 and AtIPMDH3 exhibiting dominant roles"]
- [PMID:20840499 "IPMDH2 and IPMDH3 proteins exhibited significantly higher activity toward 3-IPM than IPMDH1, which is indicative of a pivotal role in leucine biosynthesis."]

## Other
- Redox regulation: [PMID:19674406 "Interestingly, AtIPMDH1 activity is regulated by a thiol-based redox modification."]
- Interaction with IPMI large subunit LeuC [PMID:33568694].
- GO:0103093 methylthioalkylmalate dehydrogenase activity is obsolete, replaced_by GO:0003862 (checked in local go.db), so GO:0003862 is the correct MF for the glucosinolate-pathway activity.

## Curation decisions
- Cytosol HDA (PMID:25293756, crude soluble fraction) -> MARK_AS_OVER_ANNOTATED (plastid carry-over; stroma established).
- Pollen / embryo sac development (IMP, PMID:20840499, abstract only) -> KEEP_AS_NON_CORE (indirect via Leu supply; mainly IPMDH2/3).
- Wounding / JA response (IEP) -> KEEP_AS_NON_CORE.
- Everything else ACCEPT; no NEW annotations.
- Falcon deep research not available at time of review.


## 2026-10-25 independent chain-elongation audit

Re-examined every existing annotation and core against the primary studies and exact GO reactions; preserved all machine-sourced fields and prior rows. Normal fetch-gene and fetch-gene-pmids completed. The default Falcon attempt for this panel (MAM1) failed authentication and perplexity-lite failed insufficient quota; no fabricated provider report was created. Existing provider reports were contextual only; primary sources govern decisions. Plant proteins do not require bacterial fitness fetches.

Correct broad terms now refine to supported descendants. IIL1 and SSU3 catalytic claims refer to heterodimers, with contributes_to in cores; catalytic-site ownership alone does not establish autonomous subunit activity. MAM1 lacks measured IPMS activity, whereas MAM3 retains a weak non-core activity without established native leucine-pathway participation. IMDH1 biochemical comparisons distinguish its specialized methylthioalkylmalate substrate from 3-isopropylmalate; IPMDH2 structural data are not direct IMDH1 structures. BCAT3 terminal transamination is distinct from unelongated methionine transamination and does not establish exclusivity over all chain lengths.

UniProt CC:INDUCTION gives experimental wounding/MeJA induction tied to PMID:19674406; retained IEP using this curated source, not generic coexpression. Publisher full text inspected at https://onlinelibrary.wiley.com/doi/10.1111/j.1365-313X.2009.03990.x; local cache remains abstract-only. Cytosolic proteomics detection remains UNDECIDED rather than assuming contamination. Experimental UniProt CC:FUNCTION supports target developmental phenotypes despite the paper abstract foregrounding IPMDH2/3. QuickGO confirmed GO:0003862 exact 3-IPM chemistry and obsolete GO:0103093; a replacement pointer does not broaden a chemical definition.
