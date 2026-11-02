# Pfs/MtnN manual notes

Automated deep-research providers were unavailable for this host, so this is a compact manual review against the cached UniProt and PMID records.

## Function

- UniProtKB:P0AF12 describes MtnN/Pfs as a cytosolic homodimeric 5'-methylthioadenosine/S-adenosylhomocysteine nucleosidase. The record carries three hydrolase reactions: SAH to S-ribosylhomocysteine plus adenine, MTA to 5-methylthioribose plus adenine, and 5'-deoxyadenosine to 5-deoxy-D-ribose plus adenine.
- Della Ragione et al. purified the E. coli enzyme and characterized cleavage of both S-adenosylhomocysteine and 5'-methylthioadenosine [PMID:3911944].
- Cornell and Riscoe cloned and expressed the complete E. coli pfs gene and confirmed the recombinant protein as MTA/SAH nucleosidase [PMID:9524204].
- Lee et al. identified active-site residues for EcMTAN by structural analysis, site-directed mutagenesis, and steady-state kinetics [PMID:16101288].
- Choi-Rhee and Cronan showed that 5'-deoxyadenosine, the radical-SAM reaction byproduct, is a Pfs substrate in E. coli; pfs mutants accumulate the metabolite and become deficient for BioB and LipA activity [PMID:15911379].

## Annotation decisions

- Accept the exact SAH and MTA nucleosidase molecular-function rows from experiment, PAINT, and UniProt automation.
- Modify root `catalytic activity` to the exact SAH and MTA nucleosidase functions already present in GOA.
- Accept cytosol rows; the enzyme is a soluble MtnN-family enzyme, and EcoCyc has curated direct cytosolic localization from the fractionation proteomics survey.
- Mark generic nucleoside metabolism/process rows as over-annotated rather than false: they capture only a broad consequence of a nucleosidase family.
- Accept `L-methionine cycle`: the SAH reaction generates S-ribosylhomocysteine for LuxS and is a direct bacterial route from SAH to homocysteine.
- Modify `identical protein binding` to `protein homodimerization activity`, then keep homodimerization as non-core structural context.
- Mark `purine deoxyribonucleoside catabolic process` as over-annotated: Pfs does hydrolyze the purine deoxyribonucleoside 5'-deoxyadenosine, but the E. coli role of that reaction is radical-SAM byproduct repair rather than general purine deoxyribonucleoside catabolism.
- Do not add `L-methionine salvage from methylthioadenosine` or `quorum sensing` to the MTA arm of Pfs: the UniProt methionine-salvage pathway is HAMAP-derived and E. coli K-12 lacks an obvious downstream 5-methylthioribose kinase route, and the direct AI-2/quorum-sensing producer step is LuxS cleavage of S-ribosylhomocysteine to DPD.
