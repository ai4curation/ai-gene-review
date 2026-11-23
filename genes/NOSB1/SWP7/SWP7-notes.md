# SWP7 (Nosema bombycis, UniProt B3STP1) — curation notes

## Provenance of this research

No deep-research API keys are available in this container, so `just deep-research`
could not be run and **no `-deep-research-<provider>.md` file exists or was
written** for this gene. The literature below was assembled by hand from the
cached publications, PubMed (MCP `search_articles` / `get_article_metadata`) and
the UniProt flat file.

**Full text of the key paper is not reachable.** PMID:25605761 is the single
source behind every experimental GOA row. Its cached record is abstract-only
(`full_text_available: false`); the article is in PMC (PMC4363453) but is not
open access, so Europe PMC returns no `fullTextXML` and the PMC HTML page could
not be retrieved in this environment. The GONUTS wiki, which normally records
the CACAO student's own evidence per paper, is offline: a fetch of
`https://gowiki.tamu.edu/wiki/index.php/PMID:25605761` on 2026-10-29 returned
only "This site is temporarily offline while we perform upgrades." This matches
the status already recorded in `projects/CACAO.md`. Every judgment below is
therefore made from abstracts, from the UniProt curator's own
`ECO:0000269|PubMed:25605761` statements, and from a **second, independent paper
by the same group** (PMID:28031263) that re-assays SWP7 localization — not from
the figures of PMID:25605761 itself.

## What the protein is

287 aa precursor with a 19-residue signal peptide and a mature chain 20-287
[file:NOSB1/SWP7/SWP7-uniprot.txt "FT   SIGNAL          1..19"], consistent with
secretion into the developing spore wall. It is the founding member of its own
family (Pfam PF29448 / InterPro IPR062164, "SWP7") with no catalytic domain and
no recognizable enzyme signature, and UniProt places it in the SWP7 family only
by similarity [file:NOSB1/SWP7/SWP7-uniprot.txt "CC   -!- SIMILARITY: Belongs to
the SWP7 family. {ECO:0000305}."]. Protein-level evidence (`PE 1`). The entry
also flags a frameshift in the original EMBL submission ABV48895.1, which is why
the sequence is at version 2.

Nosema bombycis is the microsporidian agent of pebrine in the silkworm. The
mature spore is wrapped in a two-layered wall — "a thick spore wall composed of a
glycoprotein-rich outer layer or exospore and a chitin-rich inner layer or
endospore" [PMID:18563739 "protected by a thick spore wall composed of a
glycoprotein-rich outer layer or exospore and a chitin-rich inner layer or
endospore"] — plus the polar tube, the extrusion apparatus the parasite fires
through the host plasma membrane. "Spore wall and polar tube are the major
apparatuses for mature spores adhering and infecting to the host cells"
[PMID:29522765 "Spore wall and polar tube are the major apparatuses for mature
spores adhering and infecting to the host cells"].

SWP7 was first picked up as "HSWP7", one of the 14 hypothetical spore wall
proteins recovered from the N. bombycis spore-wall proteome by MALDI-TOF MS and
LC-MS/MS [PMID:18563739 "14 hypothetical spore wall proteins (HSWPs) or peptides
were obtained in total"]; UniProt records that reference for
"IDENTIFICATION BY MASS SPECTROMETRY, AND SUBCELLULAR LOCATION".

## Localization

PMID:25605761 is the characterization paper. Its abstract states that "SWP7 and
SWP9 are mainly localized to the exospore and endospore of mature spores and the
cytoplasm of sporonts, respectively", and that "Both SWP7 and SWP9 are
specifically colocalized to the spore wall in mature spores"
[PMID:25605761 "Both SWP7 and SWP9 are specifically colocalized to the spore
wall in mature spores"]. Read literally, the "respectively" in the first
sentence assigns exospore+endospore to SWP7 and sporont cytoplasm to SWP9. The
UniProt curator, who read the full text, nevertheless records cytoplasm for SWP7
too, with a developmental note: "Localized to the cytoplasm of sporonts and
sporoblasts and to the spore wall and polar tube of mature spores"
[file:NOSB1/SWP7/SWP7-uniprot.txt "Note=Localized to the cytoplasm of sporonts
and sporoblasts and to the spore wall and polar tube of mature spores."].

The follow-up paper settles it independently by immunoelectron microscopy:
"NbSWP9 was localized mainly in the developing polar tube of sporoblasts, while
NbSWP7 was found randomly in the cytoplasm. However, both NbSWP9 and NbSWP7 were
located in the polar tube and spore wall of N. bombycis mature spores"
[PMID:28031263 "NbSWP7 was found randomly in the cytoplasm"],
[PMID:28031263 "both NbSWP9 and NbSWP7 were located in the polar tube and spore
wall of N. bombycis mature spores"]. So all three cellular-component claims in
GOA — cytoplasm, spore wall, polar tube — are corroborated by a second paper,
with cytoplasm being the pre-sporal staging compartment and the wall/polar tube
the mature destinations.

GO has no term for the microsporidian exospore or endospore: the children of
`GO:0031160` spore wall are only `GO:0005619` ascospore wall, `GO:0043591`
endospore external encapsulating structure (bacterial), `GO:0097514` sexual spore
wall and `GO:0097515` asexual spore wall (checked via OLS, 2026-10-29). So
`GO:0031160` is as deep as the ontology currently goes for this protein, and the
sub-layer resolution the papers report cannot be captured. Filed as
`proposed_new_terms`.

## Interaction with SWP9, and what SWP7 does *not* do

Four orthogonal assays establish the SWP7-SWP9 interaction:
"immunoprecipitation, far-Western blotting, unreduced SDS-PAGE, and yeast
two-hybrid data demonstrated that SWP7 interacted with SWP9"
[PMID:25605761 "immunoprecipitation, far-Western blotting, unreduced SDS-PAGE,
and yeast two-hybrid data demonstrated that SWP7 interacted with SWP9"]. SWP9 is
R0MLT0, the WITH/FROM entity on the IPI row.

Two negative results bound what SWP7 itself can be credited with:

1. **SWP7 is not an autonomous chitin binder.** In the total spore-protein
   context both proteins pull down on chitin coats, but the recombinant protein
   does not: "binding of the recombinant protein rSWP7-His to the DCSCs is
   dependent on the combination of rSWP9-glutathione S-transferase (GST) with the
   DCSCs" [PMID:25605761 "binding of the recombinant protein rSWP7-His to the
   DCSCs is dependent on the combination of rSWP9-glutathione S-transferase (GST)
   with the DCSCs"]. So `GO:0008061 chitin binding` would be wrong for SWP7: its
   association with the chitin endospore is piggybacked on SWP9.
2. **SWP7 does not bind the polar tube proteins.** "Coimmunoprecipitation, liquid
   chromatography-tandem mass spectrometry (LC-MS/MS), and yeast two-hybrid data
   demonstrated that NbSWP9, but not NbSWP7, interacts with NbPTP1 and NbPTP2"
   [PMID:28031263 "demonstrated that NbSWP9, but not NbSWP7, interacts with
   NbPTP1 and NbPTP2"]. The authors explicitly read SWP7's polar-tube residence
   as a consequence of being carried there by SWP9: "The reason why NbSWP7 was
   localized to the polar tube may be due to the interaction between NbSWP9 and
   NbSWP7" [PMID:28031263 "The reason why NbSWP7 was localized to the polar tube
   may be due to the interaction between NbSWP9 and NbSWP7"]. And on germination
   it is SWP9, "but not NbSWP7", that accumulates at the anchoring disk; only
   anti-SWP9 reduced germination.

The upshot: SWP9 is the scaffold, SWP7 is the client. "A possible major function
of SWP9 is as a scaffolding protein that supports other proteins (such as SWP7)
that form the integrated spore wall of N. bombycis" [PMID:25605761 "A possible
major function of SWP9 is as a scaffolding protein that supports other proteins
(such as SWP7) that form the integrated spore wall of N. bombycis"]. The one
structural statement the authors make about SWP7 itself is hedged: "SWP7 and SWP9
may have important structural capacities" [PMID:25605761 "SWP7 and SWP9 may have
important structural capacities"].

## Adhesion to the host cell

The functional result for SWP7 is antibody blocking: "rSWP9-GST, anti-SWP9, and
anti-SWP7 antibodies decreased spore adhesion and infection of the host cell"
[PMID:25605761 "anti-SWP9, and anti-SWP7 antibodies decreased spore adhesion and
infection of the host cell"], and the authors' own conclusion is that the two
proteins "play significant roles in modulating host cell adherence and infection
in vitro" [PMID:25605761 "play significant roles in modulating host cell
adherence and infection in vitro"]. UniProt curates this as
"Involved in adherence of spores to the host cell surface and in infection
efficiency" with `ECO:0000269|PubMed:25605761`
[file:NOSB1/SWP7/SWP7-uniprot.txt "CC   -!- FUNCTION: Involved in adherence of
spores to the host cell surface and" ], and the entry carries KW-0130 Cell
adhesion.

This is the right shape of evidence for `GO:0075004 adhesion of symbiont spore to
host`, whose OLS comment restricts it to symbiont gene products, which is what
SWP7 is. Masking a surface-exposed exospore protein with its own antibody and
losing adhesion says the protein is part of the adhesive surface, i.e. it does
some of the work of the adhesion — not merely that it is required somewhere
upstream. Note that microsporidia have no transfection or knockout system, so
antibody/recombinant-protein competition is the only functional handle available;
there is no mutant anywhere in this literature.

## CACAO-specific observations

GOA carries four rows with `ASSIGNED BY = CACAO` (2015-02-10 and 2015-03-03), all
citing PMID:25605761:

| term | evidence | note |
|---|---|---|
| GO:0031160 spore wall | IDA | duplicates the UniProt IDA row; correct and at the deepest term GO offers |
| GO:0044099 polar tube | IDA | duplicates the UniProt IDA row; location is real but secondary (SWP9-dependent) |
| GO:0075004 adhesion of symbiont spore to host | IDA | the antibody-blocking experiment; right term, right branch |
| GO:0075004 adhesion of symbiont spore to host | IMP | **same experiment, second evidence code** |

The only defect found is the fourth row. There is no mutant, knockdown, RNAi or
allele of SWP7 in PMID:25605761 or anywhere in the N. bombycis literature; the
only perturbation is antibody and recombinant-protein competition, already
captured by the companion IDA row on the same date-adjacent submission. `IMP`
therefore misrepresents the assay, and the two rows are one experiment counted
twice. Recorded as a `source_defects` entry (`WRONG_EVIDENCE_CODE`) rather than a
`REMOVE`, because the *claim* is correct — removing a row to deduplicate is
explicitly not allowed, and the curator-deference rule applies with extra force
here since the full text is unreadable.

Nothing in this gene matches the harder CACAO failure shapes catalogued in
`projects/CACAO.md`: the paper is about this gene, the terms are on the right
branch, there is no phenotype-read-as-process (the student chose *adhesion*, the
direct readout, and did not also annotate "infection"), no sign inversion, and no
single-assay localization (every CC row is corroborated by the second paper).
The redundant-evidence-code pattern — one assay submitted under two codes — is a
new shape for the taxonomy, distinct from "parent-level restatement", because
here the *term* is identical and it is the evidence code that differs.

## Open questions

- Which host-cell surface molecule does the spore wall engage? The adhesion assay
  is a loss-of-adhesion-on-masking result; no receptor or ligand is identified.
- Is SWP7 itself adhesive, or is it masked-by-proxy because anti-SWP7 coats a wall
  whose adhesin is another protein? A purified rSWP7 adhesion/competition assay
  would separate these.
- Does SWP7 contribute structural integrity to the wall, or is it only cargo
  deposited by SWP9? The structural claim is hedged in the source, and there is no
  wall-integrity (e.g. mechanical or alkaline-resistance) measurement on an
  SWP7-depleted spore.
