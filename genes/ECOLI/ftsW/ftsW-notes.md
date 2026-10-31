# Manual notes on ftsW

FtsW is the SEDS-family membrane polymerase paired with FtsI/PBP3 for septal peptidoglycan synthesis; it should be curated for glycan polymerization, division-site localization, divisome function, and peptidoglycan biosynthesis, not for D,D-transpeptidase activity.

## UniProt and literature synthesis

- UniProtKB:P0ABG4 lists FtsW as a probable peptidoglycan glycosyltransferase with EC 2.4.99.28 by HAMAP rule, places it in the E. coli inner membrane as a multipass protein, and describes its function with FtsI/PBP3 in cell division.
- Mercer and Weiss showed that FtsW is recruited to the septal site downstream of FtsZ, FtsA, FtsQ, and FtsL, and is needed to recruit FtsI/PBP3 [PMID:11807049].
- Wang and co-workers had already localized FtsW and FtsI to the septum [PMID:9603865], and Pastoret and colleagues mapped the FtsW topology as a 10-transmembrane protein with both termini in the cytoplasm [PMID:12423747].
- The SEDS polymerase papers provide the functional split now used for curation: FtsW and RodA are the glycan polymerases for the divisome and Rod system, respectively, while FtsI/PBP3 and MrdA/PBP2 are their cognate class-B PBP transpeptidases [PMID:27525505, PMID:27643381, PMID:37620344].

## Annotation review decisions

- The many FtsW protein-binding rows report real contacts with FtsI/PBP3, FtsN, FtsQ, MtgA, or PBP1b, but GO:0005515 is too generic to keep as a molecular function.
- The lipid-linked peptidoglycan transporter activity reported for FtsW is retained only as non-core because the 2011 in vitro flippase activity predates the SEDS glycosyltransferase model and the physiological identity of the lipid II flippase is controversial [PMID:21386816].
- The regulation of cell shape rows overstate FtsW biology. FtsW loss causes filamentation through failed septation; RodA/MrdB is the SEDS paralog that maintains rod shape during lateral-wall elongation.
