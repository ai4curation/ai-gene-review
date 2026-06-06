# NCED3 (AT3G14440, Q9LRR7) — curation notes

## Identity and overview
- 9-cis-epoxycarotenoid dioxygenase NCED3, chloroplastic. EC 1.13.11.51. Also named STO1 (SALT TOLERANT 1) and SIS7.
- Carotenoid oxygenase family (InterPro IPR004294; Pfam PF03055 RPE65). 599 aa precursor with an N-terminal chloroplast transit peptide (1-40).
- Non-heme Fe(2+) dioxygenase; binds 1 Fe(2+) per subunit (His-coordinated residues 297, 346, 411, 585 by similarity to O24592) [UniProt Q9LRR7].

## Molecular function / catalysis
- Catalyzes the oxidative cleavage of 9-cis-epoxycarotenoids at the 11,12 (11',12') double bond, producing xanthoxin (2-cis,4-trans-xanthoxin) + a C25 apo-aldehyde. This is the first committed, rate-limiting step of ABA biosynthesis from carotenoids.
- UniProt curates three Rhea reactions (RHEA:23328 generic; RHEA:16541 9-cis-violaxanthin; RHEA:19677 9'-cis-neoxanthin), all EC 1.13.11.51, with experimental evidence from PubMed:11532178 and PubMed:15466233.
- Catalytic activity demonstrated: [PMID:11532178 "9-cis-epoxycarotenoid dioxygenase (NCED) is thought to be a key enzyme in ABA biosynthesis"] and the gene "controls the level of endogenous ABA under drought-stressed conditions."
- Inhibited by abamine and abamineSG (NCED-specific inhibitors) [UniProt; PMID:15247398, PMID:16682205].

## Biological process — ABA biosynthesis under stress
- AtNCED3 is the major stress-induced NCED in leaves; its expression is induced by drought and salt and controls endogenous ABA levels under stress [PMID:11532178 "the expression of an NCED gene of Arabidopsis, AtNCED3, is induced by drought stress and controls the level of endogenous ABA under drought-stressed conditions"].
- Overexpression increases ABA and improves drought tolerance; antisense/disruption gives a drought-sensitive phenotype [PMID:11532178 "Overexpression of AtNCED3 ... caused an increase in endogenous ABA level ... improvement in drought tolerance. By contrast, antisense suppression and disruption of AtNCED3 gave a drought-sensitive phenotype"].
- sto1/nced3 mutant: ABA-deficient, fails to accumulate ABA after hyperosmotic stress, salt-stress tolerant (enhanced germination on NaCl/sorbitol), hypersensitive to Li+ [PMID:15466233 "Mutant sto1 plants were unable to accumulate ABA following a hyperosmotic stress" / "enhanced germination on both ionic (NaCl) and nonionic (sorbitol) hyperosmotic media"]. Confirmed by complementation with WT NCED3 and ABA rescue.
- sis7/nced3 mutant is sugar-insensitive; NCED3 "is primarily required for ABA biosynthesis under drought conditions" [PMID:18854047 "Mutations in the SIS7/NCED3/STO1 gene, which is primarily required for ABA biosynthesis under drought conditions, confer a sugar-insensitive phenotype"].
- Peanut AhNCED1 driven by the AtNCED3 promoter complements the nced3 mutant, restoring drought-induced ABA accumulation [PMID:16870153 abstract] — i.e., the IMP for GO:0006970 response to osmotic stress reflects NCED3's role in producing ABA needed for osmotic-stress responses.

## Localization
- Plastid / chloroplast stroma, partially bound to the thylakoid membrane [UniProt "Plastid, chloroplast stroma ... Note=Partially bound to the thylakoid"].
- Experimental fractionation: AtNCED3 found in both stroma and thylakoid membrane-bound compartments [PMID:12834401 "AtNCED2, AtNCED3, and AtNCED6 are found in both stroma and thylakoid membrane-bound compartments"]. All AtNCEDs are plastid-targeted.

## Expression / tissue
- Expressed in roots, leaves, stems, silique envelopes, seeds; localized at organ-attachment points and abscission zones [UniProt tissue specificity]. NCED2/NCED3 account for root NCED activity; NCED3 is the major stress-induced leaf NCED [PMID:12834401].

## Curation reasoning summary
- Core MF: GO:0045549 9-cis-epoxycarotenoid dioxygenase activity (IDA, PMID:11532178) — ACCEPT as core.
- GO:0016702 (oxidoreductase, dioxygenase parent) IEA from InterPro is correct but a broad parent of GO:0045549 — KEEP_AS_NON_CORE (accurate but less informative than the specific term).
- GO:0010436 carotenoid dioxygenase activity (IBA, GO_Central) and GO:0016121 carotene catabolic process (IBA) appear in UniProt's GO block but not in the supplied GOA TSV; metal ion binding GO:0046872 (IEA UniProtKB-KW) likewise. Added as NEW where biologically warranted (Fe binding is a documented cofactor requirement).
- Stress-response BP terms (GO:0009414 water deprivation, GO:0006970 osmotic stress, GO:0042538 hyperosmotic salinity) are acts_upstream_of_or_within IMP — these are downstream physiological consequences mediated by ABA, not the direct enzymatic process. Kept but several marked non-core; ABA biosynthesis (GO:0009688) is the direct core process.
