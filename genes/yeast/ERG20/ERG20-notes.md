# ERG20 notes (P08524, YJL167W)

- FPP synthase, essential single-copy gene [PMID:2681213 "the gene is an essential, single copy number gene in yeast"]; IPP+DMAPP -> GPP (EC 2.5.1.1) and GPP+IPP -> FPP (EC 2.5.1.10) [UniProt:P08524].
- Sole FPP source for non-sterol isoprenoids [PMID:8096487 "no other prenyl transferase is able to synthesize the FPP molecules required for essential non-sterol metabolites"]; erg20-2 (K197E) excretes geraniol [PMID:8096487].
- erg20 mutants ergosterol auxotrophs; FPPS can be rate-limiting [PMID:1779710].
- Cytosol (IBA) and ER association (Kuranda 2009) [PMID:19416104].
- Issues: GO:0004452 IPP isomerase IDA from PMID:7908830 is an Idi1 mutagenesis paper (same ref supports IDI1) -> UNDECIDED, flag to SGD. Vacuole NAS (Hu 2017 review, UniProt function text) lacks primary support -> MARK_AS_OVER_ANNOTATED. Ubiquinone biosynthesis RCA (HEXPPSYN-PWY-2, PWY3O-862) is superpathway inflation of a shared precursor enzyme -> MARK_AS_OVER_ANNOTATED.
- Review: 36 ACCEPT, 1 KEEP_AS_NON_CORE, 2 MODIFY, 3 MARK_AS_OVER_ANNOTATED, 1 UNDECIDED.

## 2026-11-24: vacuole NAS query to UniProt

The is_active_in vacuole NAS row (PMID:28904410, Hu et al. 2017 review) now carries a UniProt WRONG_TERM CHECK source defect (PROBABLE). It is one of the 2022-02-18 batch UniProt made from that review on ERG10, ERG8, MVD1, ERG20 and IDI1; the ERG10 review already queries the batch, and each entry now records it. The cached PMC text of the review does not mention the vacuole, so the claim was not read in context, which is why this is a query and not a deletion request. The UniProt entry is now in references with a WRONG_STATEMENT CHECK on the same claim in its FUNCTION text, as ERG8, MVD1 and IDI1 already had.
