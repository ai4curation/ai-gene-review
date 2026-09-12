# cct-1 (C. elegans) research notes

UniProt: P41988 (TCPA_CAEEL). Gene: cct-1 (synonym tcp-1; ORF T05C12.7);
WormBase WBGene00000377. Chromosome II. 549 aa, ~58.8 kDa.

## Identity / summary

cct-1 encodes the **alpha (TCP-1-alpha / CCT-alpha) subunit** of the eukaryotic
cytosolic chaperonin CCT (chaperonin-containing TCP-1), also called TRiC. CCT/TRiC
is an ATP-dependent, hetero-oligomeric double-ring chaperonin; each ring is built
from eight distinct but paralogous subunits (CCT1-CCT8 / alpha-theta). cct-1 is the
alpha paralog. The assembled complex — not any single subunit — is the folding
machine; it folds actin, tubulin, and a subset of other cytosolic proteins.

- UniProt FUNCTION: "Molecular chaperone; assists the folding of proteins upon ATP
  hydrolysis. Known to play a role, in vitro, in the folding of actin and tubulin."
- UniProt SUBUNIT: "Heterooligomeric complex of about 850 to 900 kDa that forms two
  stacked rings, 12 to 16 nm in diameter."
- UniProt SUBCELLULAR LOCATION: Cytoplasm.
- UniProt family: TCP-1 chaperonin family. PANTHER PTHR11353 (CHAPERONIN);
  InterPro IPR012715 (Chap_CCT_alpha, alpha-subunit-specific).
- Note: UniProt cross-references also list GO:0051082 unfolded protein binding
  (IBA), which is NOT in the QuickGO GOA export used to seed the review; not added
  as an existing annotation.

## KNOWN (well supported)

1. **cct-1 is the alpha subunit of a large ATP-binding chaperonin complex in
   C. elegans (experimental, worm-specific).**
   [PMID:7758963 "Ce TCP-1 is a 57-kDa protein subunit of a high-molecular-mass
   complex capable of binding ATP"] — direct biochemical evidence (sucrose gradient
   + ATP-agarose) that the C. elegans TCP-1/CCT-1 protein is a subunit of a large
   ATP-binding complex. Also: single-copy gene on chromosome II, transcript
   constant through development [PMID:7758963 "the overall level of the tcp-1
   transcript is approximately constant throughout the development of the
   nematode"], and unlike Hsp60 it is not heat-inducible ("tcp-1 is not upregulated
   at elevated temperatures, but instead appears to be down-regulated").

2. **The C. elegans CCT complex contains CCT-1 as a subunit (experimental IDA).**
   [PMID:9434769 "The chaperonin containing TCP-1 (CCT) from the free-living
   nematode Caenorhabditis elegans was purified and shown to contain at least seven
   subunit species ranging from 52-65 kDa"] with Western blots using anti-CCT-1 and
   anti-CCT-5 antibodies; the worm CCT subunit composition closely matches bovine
   CCT. This paper is the basis for the WormBase IDA annotations
   (GO:0005832 chaperonin-containing T-complex; GO:0005634 nucleus).

3. **CCT/TRiC is an ATP-dependent foldase for actin and tubulin (conserved
   mechanism).**
   [PMID:16762366 "The eukaryotic cytosolic chaperonin CCT is an essential
   ATP-dependent protein folding machine whose action is required for folding the
   cytoskeletal proteins actin and tubulin, and a small number of other substrates,
   including members of the WD40-propellor repeat-containing protein family"];
   purified yeast CCT catalyses actin folding [PMID:16762366 "Yeast CCT catalyses
   the folding of yeast ACT1p and human beta-actin with nearly identical rate
   constants and yields"].

4. **The eight subunits are non-equivalent and form a stoichiometric ring.**
   [PMID:15704212 "Eukaryotic chaperonins, the Cct complexes, are assembled into
   two rings, each of which is composed of a stoichiometric array of eight different
   subunits, which are denoted Cct1p-Cct8p"] and "These results provide evidence for
   functional differences among Cct subunits and for physiological properties of
   unassembled subunits."

5. **In C. elegans the CCT subunits (cct-1..cct-8) are ubiquitously expressed,
   essential for embryogenesis, and required in vivo for actin/tubulin biogenesis.**
   [PMID:25143409 "The C. elegans genome contains eight genes encoding the
   individual CCT subunits (cct-1 to cct-8)...These genes are ubiquitously expressed
   during all developmental stages and are essential for embryogenesis"];
   [PMID:25143409 "In C. elegans, CCT is important for tubulin folding and
   microtubule growth in the early embryo"]; loss of CCT causes actin/tubulin
   biogenesis failure and [PMID:25143409 "essential for proper formation of
   microvilli in intestinal cells"]. IFB-2 intermediate filament is unaffected —
   substrate specificity for actin/tubulin.

6. **Subcellular localization: predominantly cytoplasmic.**
   [PMID:25143409 "Immunostaining using an anti-CCT-5 antibody showed that CCT
   existed diffusely in the cytoplasm but less in the nucleus"]. Consistent with
   UniProt SUBCELLULAR LOCATION: Cytoplasm.

7. **cct-1 promoter drives expression in neuronal and muscle tissues** (transcriptional
   reporter), consistent with actin/tubulin-rich tissues [PMID:9434769 "Expression
   of a reporter gene under the control of the C. elegans cct-1 promoter is found to
   be mainly restricted to neuronal and muscle tissues, an observation which is
   consistent with the participation of CCT in actin and tubulin folding"].

## NOT known / uncertain

- **Nucleus localization (GO:0005634, IDA, PMID:9434769):** The 1997 paper's
  abstract (full text not accessible; `full_text_available: false`) describes only a
  *transcriptional* promoter-reporter for expression (tissue level: neuron/muscle),
  not protein subcellular immunolocalization. C. elegans transcriptional reporters
  commonly carry an NLS, giving nuclear signal by design. Independent immunostaining
  of the assembled worm CCT complex shows it is predominantly cytoplasmic ("less in
  the nucleus", PMID:25143409). I cannot verify from the cached abstract what
  evidence underlies a nucleus located_in call for CCT-1. Per repo guidance
  (cannot access the relevant publication's full text), this annotation is marked
  UNDECIDED rather than removed; it is at most a minor / non-core localization.

- **Subunit-specific (alpha) native client repertoire** in C. elegans is undefined;
  there is no GO molecular-function term expressing "substrate-binding CCT subunit",
  so the alpha subunit's own MF can only be annotated as the complex-level foldase
  (GO:0140662) or generic ATP binding/hydrolysis (ontology-level gap; shared across
  the CCT family, cf. cct-8 review).

## Annotation plan (9 GOA annotations)

1. GO:0006457 protein folding (IBA) — ACCEPT (core BP)
2. GO:0005832 chaperonin-containing T-complex (IBA, part_of) — ACCEPT (core CC)
3. GO:0005524 ATP binding (IEA InterPro) — ACCEPT (worm-specific support PMID:7758963)
4. GO:0005737 cytoplasm (IEA SubCell) — ACCEPT (cytosol GO:0005829 would be more precise)
5. GO:0006457 protein folding (IEA InterPro) — ACCEPT (duplicate electronic of core BP)
6. GO:0016887 ATP hydrolysis activity (IEA InterPro) — ACCEPT (alpha is a genuine ATPase subunit)
7. GO:0140662 ATP-dependent protein folding chaperone (IEA InterPro) — ACCEPT (best MF term; complex-level)
8. GO:0005634 nucleus (IDA PMID:9434769, located_in) — UNDECIDED (see above)
9. GO:0005832 chaperonin-containing T-complex (IDA PMID:9434769, part_of) — ACCEPT (worm IDA)

## Deep research provenance

Automated deep research was unavailable for this gene: the falcon provider
(`just deep-research-falcon worm cct-1 --fallback perplexity-lite`) hung/timed out on
repeated attempts and produced no output, so there is intentionally no
`cct-1-deep-research-falcon.md` file (a fabricated one must never be created). This
review is instead grounded in the UniProt record (P41988 / TCPA_CAEEL), the QuickGO GOA
export, and the cached primary literature listed above (PMID:7758963, PMID:9434769,
PMID:7576182 — C. elegans-specific; PMID:16762366, PMID:15704212 — yeast mechanism;
PMID:25143409 — C. elegans in vivo). Every `supporting_text` in the review is a verbatim
substring of one of these cached publications.

## Modeling (subunit vs complex)

Following the cct-8 review pattern: core_functions models the subunit as
molecular_function = ATP binding (GO:0005524, the concrete per-subunit MF),
contributes_to_molecular_function = ATP-dependent protein folding chaperone
(GO:0140662, the complex-level activity), directly_involved_in = protein folding
(GO:0006457), in_complex = chaperonin-containing T-complex (GO:0005832),
locations = cytoplasm (GO:0005737). Unlike theta (a low-ATPase subunit), alpha
retains a canonical nucleotide-binding/ATPase site.
