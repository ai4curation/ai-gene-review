# OAZ1 (Ornithine decarboxylase antizyme 1) — review notes

UniProt: P54368 (OAZ1_HUMAN). Gene: OAZ1 (syn. OAZ). HGNC:8095. 228 aa. Chromosome 19.

## Summary of function

OAZ1 is **ornithine decarboxylase antizyme 1 (AZ1)**, a small non-catalytic regulatory
protein that is the master negative-feedback controller of polyamine (putrescine,
spermidine, spermine) homeostasis. It is NOT an enzyme itself — it works entirely by
binding and regulating ornithine decarboxylase (ODC1), the rate-limiting enzyme of
polyamine biosynthesis.

Key mechanistic facts (all grounded in local files below):

1. **Its own synthesis is a polyamine sensor.** OAZ1 expression requires a programmed +1
   ribosomal frameshift whose efficiency rises with intracellular polyamine concentration,
   closing an autoregulatory circuit.
   - [file:human/OAZ1/OAZ1-uniprot.txt "A ribosomal frameshift occurs between the codons for Ser-68 and Asp-69. An autoregulatory mechanism enables modulation of frameshifting according to the cellular concentration of polyamines."]
   - [PMID:7813017 "A novel autoregulatory mechanism enables modulation of frameshifting according to the cellular concentration of polyamines."]
   - [PMID:7813017 "The frameshift is +1 and occurs at the codon just preceding the terminator of the initiating frame."]
   - [PMID:26443277 "The expression of AZ1 is induced by a unique ribosomal frameshifting mechanism in response to increased levels of intracellular polyamines"]

2. **It binds ODC monomers and inhibits ODC activity.** AZ1 binds one ODC monomer,
   sterically occluding formation of the catalytically active ODC homodimer and disrupting
   the substrate-binding site. This is the "ornithine decarboxylase inhibitor activity"
   molecular function.
   - [file:human/OAZ1/OAZ1-uniprot.txt "Binds to ODC monomers, inhibiting the assembly of the"] (continues: "functional ODC homodimer")
   - [PMID:26443277 "the binding of AZ1 to ODC occludes the binding of a second molecule of ODC to form the active homodimer"]
   - [PMID:26443277 "the binding of AZ1 disrupts the substrate binding site of ODC"]
   - [PMID:17900240 "Measurements of the ODC activity and ODC degradation assay reveal that ODCp inhibits AZ1 function as efficiently as AZI both in vitro and in vivo."] (this paper assays AZ1 function directly via ODC activity/degradation readouts)

3. **It targets ODC for ubiquitin-independent 26S-proteasomal degradation.** AZ1 binding
   induces a conformational change in ODC that exposes its C-terminus for recognition by
   the 26S proteasome; degradation is ubiquitin-independent.
   - [PMID:26443277 "AZ1 is not only essential for the degradation of ODC, it also shortens the half-life of ODC from the basal level of 1.5 hours to approximately 15 minutes"]
   - [PMID:26443277 "ODC is degraded by the 26S proteasome in an ubiquitin-independent manner"]
   - [PMID:26443277 "the binding of AZ1 to ODC causes a global conformational change of ODC and renders its C-terminal region flexible, therefore exposing this region for degradation by the 26S proteasome"]
   - [file:human/OAZ1/OAZ1-uniprot.txt "targets the monomers for ubiquitin-"] (continues: "independent proteolytic destruction by the 26S proteasome")

4. **It inhibits cellular polyamine uptake/transport.** Beyond regulating synthesis, AZ1
   downregulates polyamine import and stimulates excretion.
   - [file:human/OAZ1/OAZ1-uniprot.txt "Also inhibits cellular uptake of polyamines by inactivating the polyamine uptake transporter."]
   - [PMID:26443277 "AZ1 inhibits polyamine uptake into the cells and stimulates excretion of polyamine out of the cell"]

5. **It is itself antagonized by antizyme inhibitors (AZIN1/AZIN2).** Antizyme inhibitors
   bind AZ1, disrupt the AZ1–ODC interaction, and release active ODC. AZIN2 (ODCp) is a
   catalytically dead ODC paralogue that acts as an antizyme inhibitor.
   - [PMID:17900240 "we report that human ODCp is a novel AZI (AZIN2)"]
   - [PMID:17900240 "we show that ODCp binds AZ1-3"]
   - [file:human/OAZ1/OAZ1-uniprot.txt "Interacts with AZIN2; this interaction disrupts the interaction between the antizyme and ODC1"]

## Localization

Cytosol (primary site of action, where ODC and the 26S proteasome operate); also nucleus
per PAN-GO/IBA. Reactome places the ODC-regulation reactions in the cytosol.
- [file:human/OAZ1/OAZ1-uniprot.txt] DR lines: GO:0005829 cytosol (TAS:Reactome), GO:0005634 nucleus (IBA), GO:0005737 cytoplasm (IBA).

## Other interactions (peripheral / non-core)

- **FAM171A1 (astroprincin, C10orf38)**: OAZ1 was recovered as a yeast-two-hybrid partner
  of astroprincin and validated by co-IP. This is the basis of the GO:0005515 IPI from
  PMID:30312582. It reflects a physical interaction, not a distinct catalytic/regulatory
  function of OAZ1.
  - [PMID:30312582 "Yeast two-hybrid screening revealed several interactive partners, of which ornithine decarboxylase antizyme-1, NEEP21 (NSG1), and ADAM10 were validated by coimmunoprecipitation."]
- **AGTR1 (angiotensin II receptor type 1, P30556)**: OAZ1 appears as a prey in a
  systematic GPCR interactome (MaMTH) screen; basis of the IntAct GO:0005515 IPI from
  PMID:28298427. High-throughput physical interaction; the paper does not discuss OAZ1
  function. Over-annotated bare "protein binding".
- **SMAD1/OAZ1/PSMB4 complex** (PMID:12097147, cited in UniProt but not in GOA): links AZ1
  to proteasome-mediated degradation of the SNIP1 repressor and BMP signalling. Not among
  the seeded GOA annotations; noted for completeness.

## Curation reasoning highlights

- Core molecular function = **ornithine decarboxylase inhibitor activity (GO:0008073)**.
  OAZ1's biologically defining "binding" (to ODC1) should be modelled with this specific
  functional term, NOT bare "protein binding".
- OAZ1 has **no catalytic activity** — do not assign decarboxylase/enzyme MF terms.
- Multiple redundant GO:0008073 annotations exist (IDA, EXP, IBA, ISS, TAS, IEA). The IDA
  (PMID:17900240) and EXP (PMID:26443277) are experimental and are the anchors; the rest
  are supporting/redundant and are accepted or kept as non-core.
- BP roles to retain: positive regulation of proteasomal protein catabolic process
  (targeting ODC for degradation), negative regulation of polyamine transmembrane
  transport, intracellular polyamine homeostasis.
- `GO:0006596 polyamine biosynthetic process` (involved_in) is arguably mis-directed for a
  *negative* regulator of polyamine synthesis; it is a legacy TAS/Reactome annotation. AZ1
  is involved in polyamine metabolism/homeostasis but as a down-regulator, so I mark these
  as over-annotated rather than accept them as core "biosynthetic" involvement.
- `GO:0006576 biogenic amine metabolic process` (ARBA IEA) is an over-general parent of
  polyamine metabolism; over-annotated.
- `GO:0090316 positive regulation of intracellular protein transport` and
  `GO:0075523 viral translational frameshifting` are electronic/ISS transfers of limited
  direct relevance to the human protein's core role; kept as non-core / over-annotated.
