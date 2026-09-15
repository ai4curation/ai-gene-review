# LNX2 review notes

## Research and source provenance

- The Falcon deep-research provider failed with HTTP 402, so no provider-named
  deep-research file was created. This review instead uses the fetched UniProt
  record, the complete QuickGO export, cached primary literature, and manual
  synthesis.
- Live QuickGO supplied 446 canonical Q8N448 rows. They normalize to 15 review
  objects because interaction-screen rows sharing term/evidence/reference/qualifier
  were collapsed while preserving every ordered WITH/FROM accession. The largest
  group contains 388 PMID:36115835 fragment/PBM interaction candidates.
- No NOT annotations, target isoforms, or annotation extensions were present in
  the source. UniProt Q8N448 has no curated alternative products.

## Protein architecture and core biochemistry

Human LNX2 is a 690-aa RING/PDZ protein. UniProt records an N-terminal RING-type
zinc finger (50-88), an NPXY motif (208-211), and four PDZ domains (233-318,
339-422, 468-554, and 600-688). The most decisive study used full-length human
LNX2 and a crystallized 20-147 Zn-RING-Zn module. Full-length LNX2 underwent
UbcH5-dependent autoubiquitination, and human NUMB was directly
polyubiquitinated [PMID:26451611, "We observed that human Numb acts as a substrate
for FL-LNX2 and undergoes polyubiquitination (Figure 2A and 2B)."]. Mutation of
the N-terminal zinc-binding motif abolished activity, establishing that the
flanking zinc finger is integral to the catalytic module rather than an
incidental metal-binding feature [PMID:26451611, "Collectively, these findings
suggest that the N-terminal Zn finger motif is indispensable for the
ubiquitination function of FL-LNX2."].

The isolated Zn-RING-Zn module and full-length LNX2 behave as dimers, but the
dimer-disrupting Lys109Ala module retained autoubiquitination activity. Therefore
self-association is a mechanistic property, not an obligate catalytic complex.

## Scaffold and partner biology

Lnx2 binds Numb/Numblike through NPXY motifs and oligomerizes through PDZ/PBM and
RING interactions [PMID:11922143, "Lnx2 and the related Lnx1 are multimodular
proteins that bind to Numb via their NPXY motifs."]. The source paper concludes
that Lnx proteins may act as molecular scaffolds, but its cached abstract does
not expose the construct species sufficiently to treat this as direct human
experimental evidence.

Additional studies support context-specific partner trafficking rather than one
universal pathway: LNX2 promotes human CD8α ubiquitylation/endocytosis
(PMID:22045731), regulates GlyT2 in neuronal models (PMID:31628376), and binds
Cx36 at rodent neuronal gap junctions (PMID:30295974). These are substrate- and
model-specific outputs of the PDZ/E3 architecture, not separate universal core
functions.

## Existing annotation decisions

- GO:0004842 is biologically sound but too broad and is modified to GO:0061630
  ubiquitin protein ligase activity using direct human biochemistry.
- The nine normalized GO:0005515 rows are marked over-annotated. Their 428 raw
  partner edges are legitimate interaction-dataset provenance, but generic
  protein binding does not describe LNX2 function. PMID:36115835 chiefly maps
  PDZ-domain/short-peptide affinity space rather than hundreds of established
  full-length cellular partners.
- Identical protein binding and plasma-membrane localization are retained as
  non-core properties. Self-association is not required for module
  autoubiquitination, and membrane association is partner/cell-context dependent.
- GO:0030165 PDZ domain binding is retained from mouse orthology. It describes
  LNX2's C-terminal PDZ-binding motif engaging PDZ domains; it must not be
  misread as the reciprocal activity of LNX2's own PDZ domains binding ligands.

## Boundaries and gaps

- Direct human NUMB polyubiquitination is established in vitro, but the
  physiological substrate hierarchy, ubiquitin linkage outcomes, and tissue
  contexts remain incompletely resolved. Lnx1/Lnx2 double-knockout mice showed
  apparently unperturbed NUMB function (PMID:27889896), cautioning against making
  NUMB/NOTCH regulation a universal in-vivo role.
- Osteoclast, pancreatic, cancer, immune, and neuronal phenotypes are contextual
  or model-organism evidence and remain outside the core molecular function.
- No stable named LNX2 complex is established.

## Priority experiments

1. Endogenously tag LNX2 in human cell types and pair acute depletion with
   ubiquitin-remnant, linkage, and stability proteomics to identify direct
   physiological substrates.
2. Separate the Zn-RING-Zn catalytic module, NPXY motif, individual PDZ domains,
   and terminal PBM by endogenous structure-function alleles.
3. Test whether self-association changes substrate selection or localization even
   though it is dispensable for isolated-module autoubiquitination.
