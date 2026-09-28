# MPEG1 (perforin-2) review notes

## Why this gene was selected

MPEG1/perforin-2 is a MACPF-superfamily pore former with a single, well-supported molecular
function (`GO:0022829` wide pore channel activity, IDA) that is deployed in two very different
biological settings: killing of bacteria inside phagolysosomes, and rupture of antigen-containing
endocytic compartments so that antigen reaches the cytosol for cross-presentation. A 2026 EMBO J
paper (PMID:42618800) argues that the *form of the protein* that makes the pore differs between the
two settings, which raises the curation question of whether this is one molecular function used
twice, or two mechanistically distinct activities.

## The pore-forming molecular function

The cryo-EM/AFM study that underpins the GOA `GO:0022829` IDA established both the prepore and the
pore, and the acid trigger:

[PMID:31537793 "We use cryo-Electron Microscopy (cryo-EM) to determine the 2.4 A structure of a
hexadecameric assembly of MPEG1 that displays the expected features of a soluble prepore complex."]

[PMID:31537793 "We further discover that MPEG1 prepore-like assemblies can be induced to perforate
membranes through acidification, such as would occur within maturing phagolysosomes."]

The same paper is the origin of the "TM anchor orients the pore away from the host membrane" model
that PMID:42618800 now challenges:

[PMID:31537793 "These data reveal that a multi-vesicular body of 12 kDa (MVB12)-associated
beta-prism (MABP) domain binds membranes such that the pore-forming machinery of MPEG1 is oriented
away from the bound membrane."]

[PMID:31537793 "This unexpected mechanism of membrane interaction suggests that MPEG1 remains bound
to the phagolysosome membrane while simultaneously forming pores in engulfed bacterial targets."]

Independent morphological evidence for pores on the bacterial surface:

[PMID:26402460 "Subsequently, Perforin-2 polymerizes and forms large clusters of 100 A pores in the
bacterial surface with Perforin-2 cleavage products present in bacteria."]

UniProt (Q2M385) records the mechanism as an acid-triggered prepore-to-pore transition in which two
alpha-helical regions refold into transmembrane beta-hairpins (TMH1/TMH2) forming a giant
beta-barrel, citing PubMed:31537793.

## Antibacterial deployment (long-established, not contested)

- Chlamydia: [PMID:23753625 "Knockdown of perforin-2 in macrophages did not alter the invasion of
  host cells but did result in chlamydial growth that closely mirrored that detected in HeLa
  cells."]
- MRSA / Salmonella in vivo: [PMID:26402460 "Perforin-2 knockout mice are unable to control the
  systemic dissemination of methicillin-resistant Staphylococcus aureus (MRSA) or Salmonella
  typhimurium and perish shortly after epicutaneous or orogastric infection respectively."]
- S. aureus in human skin: [PMID:30609079 "P-2 overexpression resulted in a reduction of
  intracellular S. aureus, while infection of human wounds by this pathogen resulted in P-2
  suppression, revealing a novel mechanism by which S. aureus may escape cutaneous immunity to
  cause persistent wound infections."]
- Human loss-of-function: [PMID:33224153 "We showed that haploinsufficiency of perforin-2 reduced
  the bactericidal capacity of human phagocytes."] and [PMID:33224153 "Functional studies revealed
  that the truncation variant resulted in significantly reduced capacity of the patient's phagocytes
  to kill intracellular bacteria."]

The delivery route is vesicular, not secretory:
[PMID:26402460 "Perforin-2 is a transmembrane protein of cytosolic vesicles -derived from multiple
organelles- that translocate to and fuse with bacterium containing vesicles."]

## Cross-presentation deployment

Discovered by genetic screening in cross-presenting DCs:
[PMID:37347855 "We devised an assay suitable for genetic screening and identified a pore-forming
protein, perforin-2 (Mpeg1), as a dedicated effector exclusive to cross-presenting cells."]
[PMID:37347855 "Mpeg1-/- mice failed to efficiently prime CD8+ T cells to cell-associated antigens,
revealing an important role for perforin-2 in cytosolic entry of antigens during
cross-presentation."]

That 2023 paper proposed that maturation releases the pore-forming domain:
[PMID:37347855 "Perforin-2 was recruited to antigen-containing compartments, where it underwent
maturation, releasing its pore-forming domain."]

An independent 2026 study reproduces the cross-presentation requirement, though it attributes it to
different proximal steps (uptake and control of acidification rather than escape per se):
[PMID:41951589 "Here, we show that loss of P2 markedly impairs DC-mediated cross-presentation of
both soluble and particulate antigens, leading to weakened antigen-specific CD8+ T cell
responses."]
[PMID:41951589 "Mechanistically, oligomerization of plasma membrane P2 promotes antigen uptake via
membrane-repair-mediated macropinocytosis. In parallel, P2 limits excessive endosomal
acidification, preserving antigens for efficient loading onto MHC class I molecules."]

## The contested point: anchored full-length protein vs released ectodomain

PMID:42618800 (Laub, Chatterjee & Kozik, EMBO J 2026 - same lab as PMID:37347855) revises the 2023
model of its own group:

[PMID:42618800 "We demonstrate that perforin-2 undergoes extensive proteolytic processing involving
multiple endocytic proteases."]

[PMID:42618800 "Although the transmembrane anchor has been proposed to protect host membranes by
orienting pores towards bacterial targets, we find that endocytic escape is mediated by full-length,
membrane-anchored perforin-2 rather than by the proteolytically released ectodomain."]

[PMID:42618800 "Moreover, we show that perforin-2-mediated antigen translocation does not require
low pH, explaining how perforin-2 can form pores in cross-presenting dendritic cells which do not
acidify their phagosomes."]

[PMID:42618800 "Our findings point to a critical role of the transmembrane anchor in perforin-2
biology and suggest that perforin-2 employs distinct mechanisms of pore formation during
anti-bacterial defence and cross-presentation."]

Status of the evidence: this is abstract-only in the cache (`full_text_available: false`), it is a
single paper, and it has no published rebuttal. It does not dispute that MPEG1 forms pores, nor
that it is required for cross-presentation; both of those are independently replicated. What it
disputes is (a) the topological model in which the TM anchor merely aims the pore at bacteria, and
(b) the assumption - inherited from the acid-activation result of PMID:31537793 - that acidification
is required for pore formation in every setting.

Note that the two claims pull in the same direction and are mutually consistent: if the protein
stays anchored, its pore is necessarily made in the host compartment membrane, and a DC phagosome
that is deliberately kept non-acidic cannot supply the acid trigger, so a different trigger must
exist. UniProt already records the released-ectodomain model as an inference from the mouse ortholog
("cleaved by trypsin in proximity of the helical transmembrane domain releases the ectodomain into
the lysosomal lumen to orient the pore-forming domain toward the endogenous membranes",
ECO:0000250|UniProtKB:A1L314) and as a separate "processed form" chain; PMID:42618800 argues this is
not the species that does the work in cross-presentation.

## Curation position taken

**One core molecular function, not two.** `GO:0022829` covers the act of building an oligomeric
transmembrane pore; that act is the same chemistry (MACPF prepore -> beta-barrel) in both settings.
What PMID:42618800 changes is *which molecular species* oligomerises (full-length anchored vs
released ectodomain), *which membrane* is perforated (host endocytic membrane vs engulfed bacterium)
and *what triggers* it (pH-independent vs acid-triggered). Those are differences in regulation,
topology and target - none of which GO's molecular-function branch distinguishes, and none of which
would be captured by splitting `GO:0022829` into two entries. Splitting on a single, abstract-only
paper would also assert more confidence than the evidence carries. The two deployments are instead
separated in `directly_involved_in` (antibacterial defence terms vs the cross-presentation terms)
and the divergence is recorded in the `reason` fields of `GO:0022829` and `GO:0061474` and in
`suggested_questions`.

**No annotation is removed on the strength of PMID:42618800.** `GO:0061474` phagolysosome membrane
(`is_active_in`, IDA) is if anything *strengthened* by it: a pore made by anchored full-length
protein is unambiguously active in the compartment membrane. `GO:0005576` extracellular region is
kept as non-core - it reflects the secreted, TM-less splice isoform perforin-2b
[PMID:28705375 "In contrast, the short isoform perforin-2b lacking the transmembrane domain failed
to localize to the membrane of vesicles."] and [PMID:28705375 "On the other hand, we detected the
secretion of perforin-2b in response to LPS stimulation."] - not the pore-forming species.

**Ontology observation (not acted on).** `GO:0022829` is defined as "the energy-independent
facilitated diffusion of propanediol through a large pore, un-gated channel. Examples include gap
junctions ... and porins", which is a poor fit for an acid-gated lytic MACPF beta-barrel; `GO:0140911`
pore-forming activity ("a protein is inserted into the membrane of another cell where it forms
transmembrane pores") fits the antibacterial deployment far better. `GO:0022829` is nonetheless the
term GO uses consistently across this protein class (PRF1, GSDMD and MPEG1 all carry it), so it is
accepted here rather than replaced for MPEG1 alone; adding `GO:0140911` - as PRF1 already has via
InterPro - is raised as a recommendation instead. Neither term covers pore formation in the cell's
*own* endomembrane, which is what the cross-presentation deployment does.

## Loose ends

- `GO:0055085` transmembrane transport is an automatic inter-ontology inference from `GO:0022829`
  (GO_REF:0000108). It reads as solute transport, which is not what a lytic pore does; marked as
  over-annotated.
- `GO:0002478` is the parent of `GO:0042590`; both are carried by ISS from the mouse ortholog. Kept,
  but the specific child is the informative one.
