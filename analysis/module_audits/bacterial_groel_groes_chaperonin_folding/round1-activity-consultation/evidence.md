# Activity adjudication for PR6164 review5809803940

## GroEL2 self-association and folding modes

PMID12198306 reports a Cpn60.2 dimer in the asymmetric unit; its accessible abstract was checked at https://pubmed.ncbi.nlm.nih.gov/12198306/ . The publisher endpoint was attempted but unavailable. An asymmetric-unit dimer alone need not establish physiological assembly. Independent PMID15327959 reports lower oligomers in biochemical characterization, and the frozen UniProt SUBUNIT statement records experimentally supported dimeric and other oligomeric forms. Together these support identical-protein association, without fixing its native stoichiometry or equating it with the E. coli tetradecamer. MODIFY to GO0042802 is more informative than deleting the self-binding claim. PMID15327959 also explicitly reports partial refolding without ATP/co-chaperonin; the broader GO0044183 is retained to cover that observed mode alongside ATP-dependent folding.

## E. coli GroES metal-binding inference

PMID12837792 full publisher Methods, Table2 and metal-ion discussion were independently reread: https://journals.asm.org/doi/full/10.1128/jb.185.14.4172-4185.2003 . E. coli GroES shifts from 3.70 to 4.27 nm hydrodynamic radius in a comparison containing 20 mM calcium chloride. This is real solution-response evidence, but does not separate specific coordination from other ion-dependent assembly effects or measure affinity. The Mtb protein has two additional acidic roof-loop residues, making its observed coordination environment different; E. coli Glu53 coordination is proposed. The PAINT source therefore remains sound, while direct transfer of its binding property is less secure than KEEP_AS_NON_CORE implied. MARK_AS_OVER_ANNOTATED records this evidence limit. High concentration alone is not proof of artifact, and absence of physiological regulation is not itself evidence against molecular binding. No quantitative cytosolic-calcium ratio is asserted here. The prior source-analysis note remains an unchanged historical interpretation; this assessment supersedes its endorsement of retention.

## Ontology

Current QuickGO responses are frozen in ontology.json. GO0042802 means identical protein binding; GO0044183 covers folding assistance without imposing ATP hydrolysis; GO0140662 specifies that energetic requirement. GO0046872 is broad metal ion binding, not calcium regulation. All original row payloads/order and inherited proposals remain unchanged.
