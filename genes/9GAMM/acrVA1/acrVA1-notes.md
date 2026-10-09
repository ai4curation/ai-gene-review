# acrVA1 (A0A5H1ZR47, Moraxella bovoculi) — curation notes

## Identity

Unreviewed TrEMBL entry, 174 aa, `SubName: Full=AcrVA1 {ECO:0000313|PDB:6NMD}` — the name
comes from a PDB deposition. `GN ORFNames=AAX09_07405`, a *Moraxella bovoculi* locus tag.
`PE 1: Evidence at protein level`. CDD `cd22787 AcrVA1`. Seeded taxon was wrong
(`NCBITaxon:9`, which is *Buchnera aphidicola*); UniProt gives `OX NCBI_TaxID=386891`
(*Moraxella bovoculi*) and the review is corrected to that. No GOA annotations at all.

`PDB; 6NMD; EM; 3.49 A; B=5-174` is the LbCas12a–crRNA–AcrVA1 complex; RCSB confirms its
primary citation is PMID:31155345 and its structure title is "cryo-EM Structure of the
LbCas12a-crRNA-AcrVA1 complex". So the structural work is on this accession.

For PMID:30936531 (Knott et al.), the methods say only that the AcrVA1 expression plasmid
was "generated from a custom pET-based expression vector as described previously18"
(ref 18 = Marino et al. 2018), with no accession. Both papers work on the *Moraxella
bovoculi* AcrVA1, which is the canonical one, but I cannot verify sequence identity from
the cached text. The structural/binding annotations are therefore grounded on
PMID:31155345 (direct, via 6NMD), and PMID:30936531 is used for the enzymology with that
caveat recorded.

## Mechanism: the module's assignment is right about the outcome and over-asserts the catalyst

The module (annoton `acrva1_crrna_nuclease`) places AcrVA1 in the
`crrna_cleavage_variant` of the enzymatic-subversion part, and asserts
`required_function` and `function` = `GO:0004521 RNA endonuclease activity`, with substrate
"Cas12a-bound crRNA guide". **The mechanism class is correct. The attribution of the
catalytic centre to AcrVA1 is not established, and the module asserts it without
qualification.**

What is established:

- AcrVA1 is a broad-spectrum inhibitor of Cas12a cis-cleavage
  [PMID:30936531 "AcrVA1 blocked dsDNA cleavage by all three Cas12a orthologs"].
- It blocks dsDNA binding
  [PMID:30936531 "revealing that AcrVAs abolished dsDNA binding"].
- Its distinctive mechanism is guide destruction, not occupancy
  [PMID:30936531 "AcrVA1 is a multiple-turnover inhibitor that triggers cleavage of the target-recognition sequence of the Cas12a-bound guide RNA to irreversibly inactivate the Cas12a complex."],
  [PMID:30936531 "we show that AcrVA1 triggers multiple turnover endoribonucleolytic cleavage of a Cas12a-bound crRNA to truncate the spacer sequence and permanently inactivate the complex"].
- The chemistry is endonucleolytic and the cut positions are mapped
  [PMID:30936531 "we mapped the scissile phosphates at positions five to eight within the crRNA spacer"],
  [PMID:30936531 "The activity is that of an endoribonuclease where catalysis generates an intact 3’-fragment of the crRNA that is released by Cas12a after AcrVA1-triggered truncation"].
- Catalysis is sub-stoichiometric, which is what makes it catalytic rather than
  stoichiometric and is the basis of the module's part-3 boundary
  [PMID:30936531 "Thus, AcrVA1 activity is multiple-turnover where cleavage of a crRNA will permanently inactivate Cas12a-crRNA complexes through a mode of inhibition not previously observed for any anti-CRISPR protein."].
- Structurally, AcrVA1 occupies the PAM-binding pocket
  [PMID:31155345 "AcrVA1 is sandwiched between the recognition (REC) and nuclease (NUC) lobes of Cas12a and inserts into the binding pocket for the protospacer-adjacent motif (PAM), a short DNA sequence guiding Cas12a targeting."].

**What is not established — the catalyst.** The activity requires both AcrVA1 and
Cas12a-crRNA together; AcrVA1 alone does nothing to RNA
[PMID:30936531 "AcrVA1 had no effect on the integrity of mature or pre-crRNA in the absence of Cas12a"],
and Knott et al. say explicitly that they could not assign the catalytic centre
[PMID:30936531 "We demonstrated that the nuclease activity is entirely dependent on the presence of a Cas12a-crRNA complex and AcrVA1, but our data do not describe the identity of the component bearing the catalytic center for the observed nuclease activity. It is likely that AcrVA1 is an RNase, however we could not detect any RNase"].
They also report that mutating either known Cas12a nuclease centre (RuvC, and the
pre-crRNA processing nuclease) does not abolish the truncation, so the obvious alternative
candidates are excluded without the AcrVA1 option being confirmed. The independent
structural paper states the active reading without qualification
[PMID:31155345 "AcrVA1 cleaves crRNA in a Cas12a-dependent manner, inactivating Cas12a-crRNA complexes."]
but does not identify catalytic residues either.

**Curation decision.** GO:0004521 RNA endonuclease activity is asserted, because two
independent groups report Cas12a-dependent endoribonucleolytic cleavage with multiple
turnover and the balance of the published interpretation is that AcrVA1 is the nuclease.
But it is asserted with the caveat in `review.reason` and with an explicit BIOLOGY
knowledge gap, because the alternative — that AcrVA1 allosterically licenses a latent
Cas12a ribonuclease activity — has not been excluded, and if it were true the term would
belong on Cas12a and AcrVA1 would instead be an enzyme *activator*. **This is the point at
which the module should be softened:** `required_function: GO:0004521` makes the
unestablished attribution a membership criterion for the family, which is stronger than
the evidence.

`GO:0043021 ribonucleoprotein complex binding` is also asserted, and is on firmer ground
than the catalytic term: the cryo-EM structure is of AcrVA1 bound to the Cas12a-crRNA
ribonucleoprotein, and every activity AcrVA1 has is conditional on that complex existing.

## Note on "DNA mimicry"

AcrVA1 inserts into the PAM-binding pocket, which is superficially the AcrIIA4/AcrIIA2
mechanism. It is **not** annotated as a nucleic acid mimic here, because neither paper
describes an acidic pseudo-DNA surface or competition with the duplex; the PAM-pocket
insertion is reported as the positioning that puts AcrVA1 next to the crRNA spacer it then
cleaves. Assigning mimicry would be reading the AcrIIA4 story onto a different protein.
The module's placement of AcrVA1 in part 3 (enzymatic) rather than part 1 (recognition
blockade) is the right call, even though AcrVA1 does also block dsDNA binding.

## Curation gap

Unreviewed entry, PDB-derived name, zero GOA annotations, for a protein whose mechanism
was called "a mode of inhibition not previously observed for any anti-CRISPR protein".
Same curation gap class as L7P7R7 and A0A2D0TCG3.
