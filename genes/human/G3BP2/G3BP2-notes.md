# G3BP2 (Q9UN86) — curation notes

Human Ras GTPase-activating protein-binding protein 2, the paralog of G3BP1 and, with
it, the nucleator of cytoplasmic stress granules. Reviewed for the stress-granule
project (issue #3953). No automated deep-research provider was available in this run
(no provider API key), so these notes are my own reading of the cached publications and
the UniProt record; they are **not** a `-deep-research-<provider>.md` file.

## Architecture

482 aa, two isoforms (A = Q9UN86-1 displayed, B = Q9UN86-2, VSP_003605). Domain layout
is the canonical G3BP one: N-terminal NTF2-like domain (residues 11–133), an acidic
disordered region (142–220), a PxxP/disordered central segment, an RRM (331–409) and a
C-terminal RG-rich region (404–476)
[file:genes/human/G3BP2/G3BP2-uniprot.txt FT:DOMAIN/FT:REGION]. InterPro assigns
IPR002075 (NTF2_dom), IPR000504 (RRM_dom) and the paralog-specific IPR034376
(G3BP2_RRM); PANTHER places it in PTHR10693 subfamily SF10.

UniProt's own summary of the mechanism is explicit about which parts do what:
"Can mediate both protein-protein and protein-RNA interactions via the NTF2 domain and
RNA-binding domain RRM" and "The NTF2 domain mediates interaction with CAPRIN1 and
USP10 regulators, thereby regulating assembly of stress granules"
[file:genes/human/G3BP2/G3BP2-uniprot.txt CC:DOMAIN].

## Core function: RNA-driven condensate scaffold for stress granules

- Knockdown of G3BP1 or G3BP2 alone only partially suppresses arsenite-induced stress
  granules, but losing both does not [PMID:23279204 "Although single knockdown of either
  G3BP1 or G3BP2 in 293T cells partially reduced the number of SG-positive cells induced
  by arsenite, the knockdowns of both genes significantly reduced the number."].
  Overexpression of G3BP2 alone is sufficient to nucleate granules without stress
  [PMID:23279204 "Moreover, like G3BP1, the overexpression of G3BP2 induced SGs even
  without stress stimuli."], and G3BP2 self-associates and heterodimerizes
  [PMID:23279204 "G3BP2 formed a homo-multimer and a hetero-multimer with G3BP1."].
- The CRISPR double knockout is the decisive genetic result [PMID:27022092 "We now show
  that cells lacking both G3BP1 and G3BP2 cannot form SGs in response to eukaryotic
  initiation factor 2α phosphorylation or eIF4A inhibition, but are still SG-competent
  when challenged with severe heat or osmotic stress."], and re-expressing G3BP2 alone
  rescues it [PMID:27022092 "SG competence is completely rescued by G3BP2, G3BP1-WT"].
  The 2020 reconstitution papers repeat the rescue with 17 markers [PMID:32302571
  "Expression of GFP-G3BP1 or GFP-G3BP2 were each sufficient to restore SG assembly in
  response to arsenite in G3BP1/2 dKO cells based on 17 markers, indicating that these
  two proteins are redundant with respect to supporting SG assembly"].
- Purified G3BP2 is itself a phase-separating scaffold, not merely a granule resident
  [PMID:32302572 "Indeed, the phase-separated fraction was higher for G3BP2 compared
  with G3BP1 in protein-only systems"; "Although G3BP2 formed oligomers at pH 7, it
  still required RNA to phase-separate at low PEG concentrations"]. The paralogs differ
  quantitatively: G3BP2's RG-rich region carries more arginines and oligomerizes more
  readily [PMID:32302572 "We conclude that the higher valence of arginine residues
  within the RG-rich region renders G3BP2 more prone to oligomerize and, consequently,
  more efficient to form condensates together with RNA."].

So the molecular function is `GO:0140693` molecular condensate scaffold activity and the
process is `GO:0034063` cytoplasmic stress granule assembly, in `GO:0010494`. This is
one of the few genes where the GOA already has the condensate-scaffold MF by IDA from
three independent 2020 papers.

## The NTF2 pocket is a two-way switch, and the agents are the partners

CAPRIN1 and USP10 bind the *same* hydrophobic pocket of the NTF2-like domain, mutually
exclusively, with opposite consequences [PMID:36279435 "The crystal structures of the
nuclear transport factor 2-like (NTF2L) domain of G3BP1 in complex with the
G3BP1-interacting motif (GIM) of Caprin-1 and USP10 show that both GIMs bind to the same
hydrophobic pocket of G3BP1."; "In contrast, USP10 lacks an RBD and acts as a cap,
preventing additional RNA binding to G3BPs and suppressing SG formation"]. ComplexPortal
models this as two complexes containing G3BP2 — CPX-18979 (CAPRIN1-G3BP2, promoting) and
CPX-26723 (G3BP2-USP10, inhibiting) — which is where the `GO:0062029` and `GO:0062030`
NAS rows come from. Both are kept non-core here: they are true statements about the
partner-bound forms, and G3BP2 contributes the pocket that makes the switch possible,
but the gene's own informative claim is the direct scaffold/assembly pair.

## 40S subunits are a real G3BP target, not just an SG co-resident

G3BP2 co-immunoprecipitates specifically with *dissociated* 40S subunits [PMID:27022092
"The results confirm that G3BP1 (lane 4) and G3BP2 (lane 2) interact only with
dissociated 40S subunits"; figure title "G3BP1 and G3BP2 selectively associate with
dissociated 40S ribosomal subunits."]. G3BP1 already carries `GO:0043024` ribosomal
small subunit binding by IDA from this very paper (QuickGO, UniProtKB:Q13283), while
G3BP2 does not — a straightforward curation gap, proposed here as a `NEW` row.

The same association has a biochemical consequence: G3BP-family–USP10 complexes are
required to strip ubiquitin from small-subunit proteins after ribosome collisions
[PMID:31981475 "We show that G3BP1-family-USP10 complexes are required for
deubiquitination of RPS2, RPS3, and RPS10 to rescue modified 40S subunits from
programmed degradation."], with the authors arguing that 40S subunits are the family's
main target [PMID:31981475 "our results identified 40S subunits and associated mRNAs as
their predominant targets"]. The catalysis is USP10's, so the `GO:0016579` NAS row is
kept as non-core rather than accepted as a core function; the same row exists on G3BP1
by IDA from PMID:34469731 (QuickGO), so this is curator practice, not an outlier.

## A second, separable function: cytoplasmic anchoring of signalling proteins

Independently of stress granules, G3BP2 holds partners in the cytoplasm. It was
identified as the IκBα cytoplasmic-retention receptor [PMID:10969074 "The N-terminal
domain of IkappaBalpha contains a sequence responsible for the cytoplasmic retention of
IkappaBalpha that is specifically recognized by G3BP2"; "Overexpression of G3BP2
directly promotes retention of IkappaBalpha in the cytoplasm"], and the same activity
explains its role in mechanotransduction, where matrix stiffness releases TWIST1
[PMID:25893917 "High matrix stiffness promotes nuclear translocation of TWIST1 by
releasing TWIST1 from its cytoplasmic binding partner G3BP2."; "Loss of G3BP2 leads to
constitutive TWIST1 nuclear localization and synergizes with increasing matrix stiffness
to induce EMT and promote tumour invasion and metastasis."].

`GO:0051220` cytoplasmic sequestering of protein was obsoleted precisely because it
"represents a molecular function, not a biological process" (OLS), and the MF that
replaced it, `GO:0140311` protein sequestering activity, is what the two TWIST1 IPI rows
should say. No separate BP term is proposed.

## Viral targeting: G3BP2 is the target, not the actor

Much of the GOA's protein-binding bulk is SARS-CoV-2 nucleocapsid (P0DTC9) interaction
data. The virus sequesters G3BP2 [PMID:34901782 "N localizes to stress granules and
sequesters G3BPs away from their typical interaction partners, thus attenuating stress
granule formation."], and aphthovirus leader proteases cleave it [PMID:30404792 "we show
that Lpro cleaves the known SG scaffold proteins G3BP1 and G3BP2 but not TIA-1"]. Both
are evidence that G3BP2 is an antiviral chokepoint, but neither licenses an
antiviral-process annotation on G3BP2 itself: the work in those experiments is done by
the viral protein. Recorded here for context only.

## RNA binding

GOA has `GO:0003723` RNA binding twice by HDA from the 2012 mRNA-interactome capture
papers. Both assays purify proteins crosslinked to polyadenylated RNA — "interactome
capture" on HeLa poly(A) RNA [PMID:22658674] and "a photoreactive nucleotide-enhanced UV
crosslinking and oligo(dT) purification approach to identify the mRNA-bound proteome"
[PMID:22681889] — so the evidence on those two rows is really for `GO:0003729` mRNA
binding, which is also the PAN-GO/IBA call for the family and is annotated and accepted
on its own row. Because the gene already carries the specific term, and because all rows
on one term must read the same way, the three `GO:0003723` rows are accepted rather than
modified; the InterPro RRM-based IEA row stops at RNA binding, which is as far as a
signature can go.

## Disease context (not annotated)

De novo variants in G3BP2 are enriched in neurodevelopmental disorders [PMID:35977029
"On the basis of data from 40,853 individuals with NDDs, we report a nominally
significant excess of de novo variants within 29 genes that are not implicated in NDDs,
including 3 essential genes (G3BP1, G3BP2, and UBAP2L) in the core SG interaction
network."]. This is disease association rather than a new GO claim, so it informs the
description only.

## Open questions

- Is there any process for which G3BP2 is not interchangeable with G3BP1? The rescue
  experiments show redundancy for granule assembly, but the paralogs are not identical
  in RG-rich arginine content and phase behaviour, and only G3BP2 has a characterised
  IκBα/TWIST1 anchoring role.
- Which G3BP2 isoform (A or B) carries the cytoplasmic-anchoring activity? The IntAct
  rows for NUFIP2 and ZNF618 are isoform-B-specific, but no functional experiment
  separates the isoforms.
