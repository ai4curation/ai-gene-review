# IDI1 notes (P15496, YPL117C)

- Type I IPP isomerase, IPP <-> DMAPP (EC 5.3.3.2) [PMID:7908830 "antarafacial [1.3] allylic rearrangement of isopentenyl diphosphate (IPP) to its electrophilic allylic isomer dimethylallyl diphosphate (DMAPP)"].
- Purified from yeast, gene cloned [PMID:2681212]; active-site nucleophile Cys139 [PMID:2223785 "The primary site of attachment was Cys-139."]; E207 essential [PMID:7908830].
- Used with avian FPPS to make labelled FPP in vitro [PMID:7858969].
- Cytoplasm/nucleus GFP [PMID:14562095]; cytosol SWAT-GFP [PMID:26928762].
- Issues: vacuole NAS from Hu 2017 review -> MARK_AS_OVER_ANNOTATED; IPP biosynthesis IBA (plant-seeded) misrepresents yeast flux direction -> MARK_AS_OVER_ANNOTATED.
- Review: 21 ACCEPT, 3 KEEP_AS_NON_CORE, 2 MARK_AS_OVER_ANNOTATED, 1 MODIFY.

## 2026-11-24: vacuole NAS query to UniProt

The is_active_in vacuole NAS row (PMID:28904410, Hu et al. 2017 review) now carries a UniProt WRONG_TERM CHECK source defect (PROBABLE). It is one of the 2022-02-18 batch UniProt made from that review on ERG10, ERG8, MVD1, ERG20 and IDI1; the ERG10 review already queries the batch, and each entry now records it. The cached PMC text of the review does not mention the vacuole, so the claim was not read in context, which is why this is a query and not a deletion request.
