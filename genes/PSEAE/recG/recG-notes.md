# recG (PA5345, Q9HTL3) review notes

## Literature

- recG is co-transcribed with oxyR from a single promoter; a recG::Gm mutant (not an in-frame oxyR deletion) is hypersensitive to UV [PMID:10913087 "The recG ::Gm mutant was hypersensitive to UV and was killed by more than 5 log units within 20 s of irradiation."], partially complemented in trans [PMID:10913087 "Expression of the recG gene in trans partially restored UV tolerance in the recG ::Gm mutant."]. The recG mutant was also less resistant to H2O2 and cumene hydroperoxide [PMID:10913087 "Still, recG appeared to be essential for optimal resistance to H 2 O 2 and CHP, and the recG mutant could be complemented by the recG gene in trans ."].
- Transposon mutants in ruvB and recG are chromate-hypersensitive, complemented by the wild-type genes, and also sensitive to tellurite, selenite and mitomycin C [PMID:16105671 "both mutant strains showed an increased susceptibility to the toxic oxyanions tellurite and selenite as well as to mitomycin C, but not to arsenite, paraquat and hydrogen peroxide."].
- Yeom et al. report that purified RecG binds palindromic promoters of OxyR-controlled genes and, with ATP and SSB, generates linear DNA that OxyR then binds [PMID:22621928 "The OxyR tetramer preferentially binds to promoters after RecG has generated linear DNA in the presence of ATP"]. The abstract covers P. aeruginosa, P. putida and E. coli and does not say which organism's RecG was purified; full text not retrievable (PMC record returned no body text).
- UniRule (RU363016): RecG catalyses Holliday-junction branch migration and fork regression, with 3'-5' helicase polarity. Domain content: RecG wedge, DEAD/DEAH helicase and helicase C-terminal domains (IPR004609).

Search: PubMed metadata for all GOA-cited PMIDs; PMID:10913087 full text cached and read for recG passages; PMID:16105671 and PMID:22621928 abstract only. NCBI E-utilities and Europe PMC search were unavailable (HTTP 500/503) during this session.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002773745 | GO:0003678 DNA helicase activity | 4 | 79 (70 taxa) | GO:0003678 and GO:0009378, IDA, PMID:22621928 | UNVERIFIABLE | The abstract describes purified RecG unwinding palindromic promoter DNA in an ATP-dependent way, which fits helicase activity, but does not state whether the purified protein was the P. aeruginosa or P. putida enzyme. The term is certainly right for RecG; no defect filed. | E. coli RecG (P24230; IDA PMID:8428576, EXP 3'-5' helicase), M. tuberculosis RecG (P9WMQ7), B. subtilis RecG (O34942) | Yes |
| PTN002773745 | GO:0006281 DNA repair | 2 | 79 (70 taxa) | GO:0006281, IMP, PMID:10913087 and PMID:16105671 | SOUND | Full text (PMID:10913087) shows UV hypersensitivity of a recG::Gm mutant with trans-complementation; PMID:16105671 abstract shows chromate and mitomycin C sensitivity with cosmid complementation. RecG is itself a DNA repair helicase, so this is participation, not an indirect phenotype. | Arabidopsis RECG1 (AT2G01440/F4INA9; TAIR IMP DNA repair, PMID:26462909) | Yes |

Both IBDs suit a RecG-orthologue clade (bacterial RecG plus plant organellar RECG1). No GO_CENTRAL defect.

Non-seed PseudoCAP rows: cellular response to UV, oxidative stress, chromate and selenite (IMP) are mutant sensitivities that follow from the DNA repair role; kept as non-core.
