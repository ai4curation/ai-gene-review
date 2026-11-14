# E. coli Pfs/LuxS source review

Reviewed 2026-11-07. All existing publication caches remain byte-identical.

## PMID11489131: full publisher text

Source: https://onlinelibrary.wiley.com/doi/full/10.1046/j.1365-2958.2001.02532.x (accessed 2026-11-07 through indexed browser full text; direct HTTP request returned403 and its challenge page is not treated as article text). The local publication cache remains abstract-only.

PMID11489131 used E. coli MG1655 pfs and luxS genes expressed as GST fusions in BL21; purified sequential reactions establish the Pfs-to-LuxS order and homocysteine formation. Table1 used sequential enzyme-removal controls; Ellman's thiol assay and HPLC/electrospray after derivatization corroborated homocysteine. The AI-2 readout used Vibrio harveyi BB170. This establishes an E. coli catalytic step in the methionine cycle, not a native whole-cycle flux measurement or universal quorum signaling.

Exact short source excerpts (Methods and Results):

> used to amplify the E. coli MG1655 genes

> homocysteine was identified as a reaction product

## Other source scopes

PMID11514505 full cache tests K-12 W3110 and its luxS::Tc derivative MDAI2 with conditioned media differing in AI-2 bioactivity. It supports a producer-side quorum role in this strain/condition; conditioned media are not a purified-signal experiment and metabolic mutant effects alone cannot prove quorum sensing. PMID18304323 full cache uses K-12 derivative MC4100 cytosolic proteomics. PMID15911532 abstract describes fractionation; exact target tables were not newly inspected, so the supported localization is retained with the curator's source mapping rather than relabeled as independently reread target data.

PMID22239413 full cache reports native dimeric EcMTAN mass matching the calculated homodimer, while PMID11591349 abstract describes a functional dimeric structure. These support the existing homodimerization interpretation without inventing a distinct signaling or assembly role. PMID15911379 abstract explicitly identifies 5'-deoxyadenosine accumulation and impaired BioB/LipA activity in E. coli pfs mutants. The experiment supports byproduct clearance, not direct participation of Pfs in sulfur insertion.

GO0009116 and GO0009164 are true for hydrolytic breakdown of SAH/MTA nucleosides; GO0006152 purine nucleoside catabolism is a verified descendant of both. The old overannotation verdicts confused broad truth with biological absence. GO0046124 has a substrate-position ambiguity: its text says deoxyribose, while its nucleoside ancestor specifies 2-deoxyribofuranose and the deoxyadenosine child GO0006157 explicitly means 2-deoxyribosyladenine. Pfs's measured radical-SAM byproduct is 5'-deoxyadenosine. Its exact mapping is left UNDECIDED; this does not deny observed 5'-deoxyadenosine hydrolysis.

Both genuine Falcon attempts failed authentication403. Manual curation is not a provider report. No new process annotation is proposed. PAINT-loss commands returned no IRD/IKR; the existing experimentally anchored node judgments are retained, not evaluated from donor counts.
