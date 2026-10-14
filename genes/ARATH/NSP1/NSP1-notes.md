# NSP1 (Q9SDM9, At3g16400) curation notes

## Nomenclature warning
- In Burow et al. 2009 and the Wittstock-lab papers, NSP1 is At3g16400 (this gene).
- Kissen & Bones 2009 call At3g16400 "AtNSP3" and use "AtNSP1" for At5g48180 [PMID:19224919 "Assays with crude bacterial extracts containing AtNSP1 ( At5g48180 ) or AtNSP3 ( At3g16400 ) recombinant proteins also resulted in the production of 2-phenylacetonitrile"].
- In PMID:30395611, "AtNSP3" is At3g16390, a tandem paralog [PMID:30395611 "The expression construct for AtNSP3 (At3g16390)"]. Its iron data therefore do not apply directly to NSP1.
- Kong et al. 2012 (PMID:22954730, cached, abstract-only) uses the Kissen numbering, so its "AtNSP1" is probably At5g48180. It is not used as evidence here.
- Also named JAL28 (jacalin-related lectin 28).

## Function
- The nsp1 T-DNA mutant (SALK_072600) lacks constitutive and herbivore-induced leaf nitrile formation [PMID:18987211 "a line with a T-DNA insertion in the second exon of At3g16400 (SALK_072600) produced no or only trace amounts of simple nitriles of the endogenous glucosinolates in rosette leaf homogenates"].
- Purified NSP1 forms simple nitriles only [PMID:18987211 "AtNSP1 did not promote thiocyanate or epithionitrile formation from any of the tested substrates."].
- In vitro, its activity did not depend on added iron [PMID:18987211 "Thus, simple nitrile formation by AtNSP1 is not dependent on the presence of Fe 2+ or Fe 3+ ion."]. UniProt still lists an Fe(2+) cofactor (by similarity or from other studies), so no iron binding NEW was proposed.
- Organ roles [PMID:27990154 "simple nitrile formation upon tissue disruption depended almost entirely on NSP2 in seeds and mainly on NSP1 in seedlings"].
- Structure: monomer with an N-terminal JAL domain [PMID:30900313 "NSP1 from A. thaliana (AtNSP1) (which is a monomer)"; PMID:30395611 "In addition, AtNSP1 possesses an N-terminal JAL domain"; PMID:28479247 crystal structure].
- Seeds and germination [PMID:31850033 "The time course of total glucosinolate content during ten days of germination depended on functional NSP1."]. The cache is abstract-only, and the phenotype is metabolic, so the seed germination and dormancy rows are UNDECIDED.

## Decisions
- Specifier activity: MODIFY enzyme regulator activity (IBA) to GO:0016846 carbon-sulfur lyase activity, consistent with ESP and TFP. Proposed new term: nitrile-forming thiohydroximate-O-sulfate sulfolyase activity (EC 4.8.1.5).
- Lectin domain: carbohydrate binding (IEA) is KEEP_AS_NON_CORE, because glycan binding is untested [PMID:19224919 "the role of these domains in AtESP and homologous proteins is not yet known"].
- Nucleus (IBA) is MARK_AS_OVER_ANNOTATED. It is seeded only by ESP's WRKY53-dependent nuclear import [PMID:17369373 "ESR is exclusively in the cytoplasm in W53-KO cells"].
- mRNA binding (HDA) is UNDECIDED, because the paper is abstract-only.
- Response to herbivore (IMP) is KEEP_AS_NON_CORE. NSP1 is required for the P. rapae-induced nitrile shift, but no protective effect has been shown.
- No falcon deep-research file was available when this review was written.
