# SOL4 notes (P53315, YGR248W)

- 6-phosphogluconolactonase, EC 3.1.1.31 [UniProt:P53315 "Reaction=6-phospho-D-glucono-1,5-lactone + H2O = 6-phospho-D-gluconate"]; oxidative PPP step 2/3 [UniProt:P53315].
- Sol family division of labour: Sol3/Sol4 have 6PGL activity, Sol1/Sol2 do not and act in tRNA export [PMID:15454531 "Thus, Sol3p and Sol4p likely function in carbohydrate metabolism, while Sol1p and Sol2p appear to have roles in tRNA function and nuclear export"].
- Activity: [PMID:15454531 "In contrast, cells containing multi-copy plasmids with SOL3 or SOL4 provided activity beyond wild-type levels"]; quadruple deletion [PMID:15454531 "the strain with the entire SOL family deleted (MLW115) containing pRS426 had very low, if any, 6Pgl activity"].
- Localization: GST-Sol4 cytosolic, nuclear-excluded [PMID:15454531 "Thus, as anticipated, Sol4p appears to be a cytosolic protein"]; Huh GFP screen nucleus+cytosol [PMID:15454531 "A recent genome-wide project reported Sol1-GFP, Sol3-GFP, and Sol4-GFP to be located in the nucleus and the cytosol"].
- No tRNA export role [PMID:15454531 "The data show that Sol1p and Sol2p affect tRNA nuclear export whereas Sol4p has no detectable role in this process"].

Decisions: ACCEPT activity, oxidative PPP, cytoplasm/cytosol; KEEP_AS_NON_CORE nucleus (HTP), carbohydrate metabolic process (general).
Module note: YeastCyc should assign the 6PGL step to SOL3 and SOL4 only, not SOL1/SOL2.
