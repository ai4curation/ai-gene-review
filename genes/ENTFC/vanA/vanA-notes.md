# vanA (Enterococcus faecium, P25051) — curation notes

## Literature search record

No deep-research provider key exists in this environment and there is no model
organism database description for Enterococcus, so this is a hand search.
`just fetch-fitness ENTFC vanA` was not attempted: no fitness-browser data set
exists for this organism.

Sources checked:

- `genes/ENTFC/vanA/vanA-uniprot.txt` (Swiss-Prot P25051): FUNCTION, CATALYTIC
  ACTIVITY, COFACTOR, BIOPHYSICOCHEMICAL PROPERTIES (five K_m values),
  SUBCELLULAR LOCATION, INDUCTION, the ATP-grasp domain and the ATP/Mg2+/substrate
  BINDING features.
- The three GOA-cited publications: PMID:2266943, PMID:1931965, PMID:1503450
  (all abstract-only in the cache).
- Additional papers fetched for the operon context: PMID:1556077 (VanS-VanR
  control of the operon), PMID:8852545 (review of the mechanism), PMID:7873524
  (VanX).
- Context read but not edited: a glycopeptide-resistance pathway module and a
  review of the vanA-operon GO-CAM, both proposed in
  ai4curation/ai-gene-review#5904 and not part of this branch; nothing in this
  review rests on them.
- GO relations checked against the local GO build, 2026-11-04: `GO:0016881
  acid-amino acid ligase activity` is an `is_a` ancestor of `GO:0008716
  D-alanine-D-alanine ligase activity` but **not** of `GO:0160220
  D-alanine-(R)-lactate ligase activity`; `GO:0005829 cytosol` is a `part_of`
  descendant of `GO:0005737 cytoplasm`.

## What VanA does

VanA is the ligase that re-terminates the peptidoglycan precursor. It is a
D-Ala-D-Ala ligase homolog (36% identity to the Salmonella Ddl, 28% to the E.
coli enzyme) whose specificity has shifted from amide to ester bond formation:

[PMID:1931965 "VanA is a D-alanine:D-alanine ligase of altered substrate specificity"]
[PMID:1931965 "VanA was found to catalyze ester bond formation between D-alanine and the D-hydroxy acid products of VanH, the best substrate being D-2-hydroxybutyrate (Km = 0.60 mM)."]

The product is incorporated into the normal precursor pathway:
[PMID:1931965 "The VanA product D-alanyl-D-2-hydroxybutyrate could then be incorporated into the UDPMurNAc-pentapeptide peptidoglycan precursor by D-Ala-D-Ala adding enzyme from Escherichia coli or by crude extract from E. faecium BM4147."]

In vivo the physiological acyl acceptor is D-lactate, supplied by VanH:
[PMID:1503450 "D-Lactate added to the culture medium restored the vancomycin resistance of a strain that does not produce the VanH dehydrogenase and therefore appears to be a substrate of VanA in vivo."]
[PMID:8852545 "Tn1546 encodes the VanH dehydrogenase which reduces pyruvate to D-lactate (D-Lac) and the VanA ligase which catalyses synthesis of the depsipeptide D-alanyl-D-lactate (D-Ala-D-Lac)."]

and the point of the substitution is the loss of a hydrogen bond to the drug:
[PMID:8852545 "The depsipeptide replaces the dipeptide D-Ala-D-Ala leading to production of peptidoglycan precursors which bind glycopeptides with reduced affinity."]

## The residual D-Ala-D-Ala ligase activity is real, but secondary

VanA is annotated both to `GO:0160220` (the depsipeptide ligase reaction) and to
`GO:0008716` (the dipeptide ligase reaction). The latter is not an artefact:
[PMID:2266943 "The vanA gene was able to transcomplement an E. coli mutant with thermosensitive D-ala-D-ala ligase activity."]
So VanA can make D-Ala-D-Ala well enough to substitute for Ddl in vivo. But it is
the ester-forming activity that the enzyme exists for and that UniProt's
RecName, EC number and reaction statement record, and the measured K_m values
are for D-hydroxy acids. Following the enzyme-specificity tiers, the dipeptide
ligase activity is treated as a genuine secondary activity
(`KEEP_AS_NON_CORE`), not as an over-annotation and not as the core function.

## Location: peripheral, on the cytoplasmic face

The paper that first identified VanA found it in membrane fractions
[PMID:2266943 "Vancomycin induced the synthesis of a ca. 40 kDa membrane-associated protein designated VANA."]
but concluded that the protein belongs with the soluble precursor-synthesising
enzymes
[PMID:2266943 "Thus, the inducible resistance protein VANA was structurally and functionally related to cytoplasmic enzymes that synthesize the target of glycopeptide antibiotics."].
UniProt reconciles the two as a peripheral membrane protein on the cytoplasmic
side, and the substrates (free D-alanine, D-lactate, ATP) and the downstream
MurF step are cytoplasmic. The review therefore accepts the cytoplasm/cytosol
rows as the site of catalysis and keeps the plasma-membrane rows as a real but
non-core observation; neither is removed.

## Process annotations

`GO:0009252 peptidoglycan biosynthetic process` is right and VanA does the work
of a step in it: it supplies the side chain terminus that MurF adds to the
precursor. What is missing from GOA is any antibiotic-response term, even though
the whole point of the gene is inducible glycopeptide resistance and UniProt
records `INDUCTION: By vancomycin, mediated by VanS/VanR`. `GO:0046677 response
to antibiotic` is added as a `NEW` row: it is the most specific available term,
since GO has no glycopeptide-resistance-specific child, and functionally
equivalent resistance enzymes already carry it in this repository.
