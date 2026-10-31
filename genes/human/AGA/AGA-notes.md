# AGA notes

Deep research (`just deep-research-falcon human AGA`) timed out after 600 s ("All providers failed"),
so the literature work was done manually with PubMed and the cached `publications/` files.

## Function
- Lysosomal glycosylasparaginase (EC 3.5.1.26), Ntn-hydrolase: [PMID:1281977 "which hydrolyses the asparagine to N-acetylglucosamine linkages of glycoproteins and glycopeptides"].
- Disease mechanism: [PMID:27906067 "AGU is caused by deficient activity of the lysosomal enzyme glycosylasparaginase that cleaves the N-glycosidic bond between the L-asparagine and N-acetylglucosamine moieties of GlcNAc-Asn."]
- Autoproteolytic activation: [PMID:14616088 "the critical nucleophile functions both as the catalytic and autocatalytic residue"]; [PMID:8776587 "suggest that the driving mechanism of AGA precursor cleavage is autocatalytic"]. Activation cleavage occurs in the ER [PMID:8776587 "specifically prevents the proteolytic activation cleavage of AGA in the endoplasmic reticulum (ER)"].
- Finnish founder C163S abolishes activity and processing [PMID:1904874 "Expression studies in COS-1 cells revealed only the Cys163----Ser mutation caused a deficiency of glycosylasparaginase activity."].
- Core fucose must be removed by FUCA1 first (see FUCA1 notes, PMID:27491075).

## Annotation notes
- Protein-binding rows from HuRI / neurodegeneration Y2H interactome removed as uninformative.
- IBA is_active_in cytoplasm (PTN000022481) marked over-annotated; node not inspected in detail.
- NEW: glycoprotein catabolic process (GO:0006516) and protein autoprocessing (GO:0016540).
- Module: `modules/lysosomal_glycoprotein_degradation.yaml`.
