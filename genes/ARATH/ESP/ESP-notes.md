# ESP (Q8RY71, At1g54040) curation notes

## Identity
- Epithiospecifier protein (AtESP), also called ESR (EPITHIOSPECIFYING SENESCENCE REGULATOR). It is a Kelch-repeat six-bladed beta-propeller with no jacalin lectin domain (UniProt MISCELLANEOUS).
- UniProt EC 4.8.1.6 (epithionitrile-forming) and EC 4.8.1.5 (nitrile-forming). Cofactor Fe(2+).

## Biochemistry
- Recombinant ESP plus myrosinase converts glucosinolates to epithionitriles and simple nitriles [PMID:11752388 "The heterologously expressed Arabidopsis ESP was able to convert glucosinolates both to epithionitriles and to simple nitriles in the presence of myrosinase"].
- It has no activity without myrosinase [PMID:11752388 "No conversion was observed in boiled control extracts, in extracts of nontransformed E. coli , or in the absence of myrosinase."].
- Fe2+ stimulates activity but is not strictly required in the 2001 assays [PMID:11752388 "Thus, the activity of the Arabidopsis ESP protein appears not to depend on added Fe 2+ , although supplemental Fe 2+ can increase nitrile formation"].
- Iron is bound in purified AtESP, and mutating the iron-binding residues E260/D264 reduces activity [PMID:30395611 "Substitution of the corresponding iron binding residues of AtESP, E260 and D264, by Gln and Asn, respectively, resulted in strongly diminished activity"].
- Specifier proteins are reclassified as catalysts [PMID:30900313 "Based on these insights, we propose that specifier proteins are catalysts that might be classified as Fe2+ -dependent lyases."]. The review therefore MODIFYs enzyme regulator activity to GO:0016846 carbon-sulfur lyase activity, consistent with genes/THLAR/TFP.
- The crystal structure shows a dimer [PMID:27498030 "AtESP shows a dimerization pattern different from TaTFP"; PMID:30900313 "TaTFP and ESP from Arabidopsis thaliana (AtESP) (which are homodimers)"].
- ESPs evolved from NSPs [PMID:30900313 "a monophyletic origin of epithiospecifier proteins (ESPs) from NSPs has been demonstrated"].

## Accessions and expression
- Col-0 is a natural leaf ESP knockout [PMID:27990154 "Due to an insertion upstream of the ESP coding sequence, Col-0 is a natural knockout of ESP and ESP activity is not detectable in leaf extracts"].
- In Ler, ESP is found in epidermis and S-cells [PMID:17390109 "In the ecotype Landsberg erecta, ESP was found to be consistently present in the epidermal cells of all aerial parts except the anthers and in S-cells of the stem below the inflorescence."].

## Defence role (ambiguous)
- [PMID:11752388 "The role of ESP in plant defense is uncertain, because the generalist herbivore Trichoplusia ni (the cabbage looper) was found to feed more readily on nitrile-producing than on isothiocyanate-producing Arabidopsis."] GOA has no insect-response annotation for ESP. The IMP "defense response to bacterium" (PMID:17369373) was kept as non-core.

## WRKY53 / senescence (Miao & Zentgraf 2007)
- [PMID:17369373 "ESR inhibits WRKY53 DNA binding in vitro, and their interaction is localized to the nucleus in vivo; however, ESR is exclusively in the cytoplasm in W53-KO cells, indicating that ESR is brought to the nucleus by the interaction."]
- The work was done in Col(-0) with SALK lines. That conflicts with the natural-knockout description above, so the reference is flagged DISPUTED and the senescence, JA and bacterium terms are kept as non-core. Protein binding was MODIFYed to GO:0140416 transcription regulator inhibitor activity, based on the EMSA data.
- The TAS "response to jasmonic acid" row cites PMID:11752388, whose full text never mentions jasmonate. It is REMOVEd, and the JA IMP row is kept.

## Decisions
- NEW: GO:0005506 iron ion binding (IDA, PMID:30395611).
- REMOVE: chloroplast (ISM) and the TAS JA row.
- Proposed new term: epithionitrile-forming sulfolyase activity (EC 4.8.1.6), under GO:0016846.
- No falcon deep-research file was available when this review was written.
