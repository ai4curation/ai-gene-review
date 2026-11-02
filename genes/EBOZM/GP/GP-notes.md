# GP (Zaire ebolavirus, Mayinga-76) — curation notes

UniProt: Q05320 (VGP_EBOZM), 676 aa, taxon NCBITaxon:128952.
Reviewed for the [CACAO project](../../../projects/CACAO.md): 5 of the 31 GOA rows
are `assigned_by: CACAO`.

**Deep research was unavailable for this review.** No deep-research API keys are
configured in this container, so `just deep-research` was not run and there is no
`GP-deep-research-*.md` file. The literature below was read directly: the cached
`publications/PMID_*.md` entries, the PubMed MCP full-text service (used to recover
the Results/Methods of PMID:20202662, which the cached copy omits), and the UniProt
flat file. The GONUTS wiki (`gowiki.tamu.edu`), which the CACAO project page
recommends for recovering a student's stated evidence, was **offline** at the time of
review ("temporarily offline for upgrades"), so the CACAO rows were judged from the
papers themselves.

## Gene / product architecture

The single GP gene of EBOV yields three products by RNA editing at a run of seven
uridines (position 295 of the mRNA): unedited RNA → sGP (P60170), +1A → full-length
GP (this entry, Q05320), +2A → ssGP (Q9YMG2)
[file:EBOZM/GP/GP-uniprot.txt "The sequence displayed here is the full-length transmembrane
glycoprotein GP, derived from the +1A edited RNA. The unedited RNA
gives rise to the small secreted glycoprotein sGP (AC P60170), the +2A
edited RNA gives rise to the super small secreted glycoprotein ssGP (AC
Q9YMG2)."].
sGP and ssGP are **separate UniProt entries**, so they are out of scope for this
review (per the CLAUDE.md alternative-ORF/separate-accession rule); only products
that share Q05320 are modelled here.

Within Q05320 the chains are (FT CHAIN): Envelope glycoprotein 33-676
(PRO_0000037485), Shed GP 33-637 (PRO_0000445686), GP1 33-501 (PRO_0000037486),
GP2 502-676 (PRO_0000037487). Signal peptide 1-32; extracellular 33-650;
TM helix 651-671; cytoplasmic tail 672-676 (five residues). Receptor-binding
region 54-201; mucin-like region 305-485 (largely MobiDB-lite disordered);
fusion peptide 524-539; coiled coils 554-595 and 615-634.

These are cleavage products of one accession, so they are recorded as
`functional_isoforms` of type `CLEAVAGE_PRODUCT` mapped to the `PRO_` chains, not as
separate gene folders.

## Entry: attachment, internalisation, fusion

GP1,2 trimers are the only spike on the virion; GP1 binds, GP2 fuses
[file:EBOZM/GP/GP-uniprot.txt "Trimeric GP1,2 complexes form the
virion surface spikes and mediate the viral entry processes, with GP1
acting as the receptor-binding subunit and GP2 as the membrane fusion
subunit."]. The trimer is disulfide-linked and chalice-shaped
[PMID:26917592 "The EBOV glycoprotein (GP) is a class I fusion protein comprising
disulfide-linked subunits, GP1 and GP2, which associate to form a chalice-shaped"].

Attachment cofactors are lectins (CD209/DC-SIGN, CLEC4M/DC-SIGNR, CLEC10A) and
integrin alpha-V; the **entry receptor proper is NPC1**, which GP1 can only engage
after cathepsin B/L remove the glycan cap in the endosome
[file:EBOZM/GP/GP-uniprot.txt "After internalization of the virus
into the endosomes of the host cell, proteolysis of GP1 by two cysteine
proteases, CTSB/cathepsin B and CTSL/cathepsin L removes the glycan cap
and allows GP1 binding to the host entry receptor NPC1"]. NPC1 binding plus Ca2+ and
low pH then trigger the GP2 conformational change that unmasks the fusion peptide
[file:EBOZM/GP/GP-uniprot.txt "NPC1-binding, Ca(2+) and acidic pH
induce a conformational change of GP2, which unmasks its fusion peptide
and permit membranes fusion"].

Internalisation is clathrin-dependent. PMID:20202662 shows that EbGP-pseudotyped
HIV infection is blocked by four independent perturbations of the clathrin pathway
(chlorpromazine, 0.45 M sucrose, dominant-negative Eps15 DIII, clathrin heavy-chain
siRNA) while wild-type HIV and VSVg-pseudotyped HIV are unaffected, and that
chlorpromazine and bafilomycin A1 block replication-competent ZEBOV-GFP
[PMID:20202662 "Sensitivity of EbGP pseudotyped HIV as well as infectious EBOV
to inhibitors of clathrin suggests that EBOV uses clathrin-mediated endocytosis
as an entry pathway."]. Entry is pH-dependent (Baf A1 sensitive), consistent with
fusion from an endosome rather than the plasma membrane.

The GP2 fusion peptide EBO16 (GAAIGLAWIPYFGPAA, residues ~524-539) adopts a
3(10)-helix in membrane-mimetic environments and interacts with
detergent-resistant (raft) membranes, with Trp8/Phe12 required for the structure
[PMID:17545161 "Our results also reveal that EBO(16) can interact with detergent-resistant
membrane fractions and strongly suggest that Trp-8 and Phe-12 are important for
structure maintenance within the membrane bilayer."]. This is the evidence behind
the three DisProt `lipid binding` rows; note the assay used SDS micelles and DRM
fractions, i.e. no physiological lipid class is identified.

## Localisation: rafts, plasma membrane, virion membrane

PMID:11877482 (the source of two CACAO rows) is a focused raft study:
- Transfected Ebola GP partitions into sucrose-gradient raft fractions, and a
  palmitoylation-site mutant does not
  [PMID:11877482 "As shown in Fig. 1 A and B, a
significant fraction of Ebola and Marburg GPs were found to reside in rafts. In contrast, an Ebola GP, mutated at cysteine residues 670 and 672
(Ebo-GPC670/672A), the putative palmitoylation sites, failed to localize to the rafts (Fig. 1 B)."].
- Raft association is cholesterol-dependent (MβCD strips GP from the raft fraction)
  and the raft-excluded control TrfR stays soluble
  [PMID:11877482 "The association of GPs with detergent insoluble fraction was dependent on cholesterol since pretreatment with methyl-β-cyclodextrin (MβCD), a
drug that depletes the membrane of cholesterol (33), resulted in almost complete removal of Ebola GP from rafts (Fig. 1 C, top panel)."].
- On intact cells GP colocalises with the raft marker GM1 in plasma-membrane patches
  (Fig. 2A, confocal)
  [PMID:11877482 "As shown in Fig. 2 A, a substantial portion of both of the GPs were found to colocalize with GM1 in
large patches on the plasma membrane, confirming the raft association of both GPs on intact cells."].

So the raft row rests on two independent assay types plus a mutant control — unusually
strong for a CC row, and *not* the "single-assay localization" CACAO failure mode.

The same paper is also the evidence for GP's contribution to budding: GP alone releases
GM1-containing particulate material, GP+VP40 shifts both proteins into the supernatant,
and the released particles are filamentous, spiked, GM1-positive and TrfR-negative
[PMID:11877482 "Interestingly, coexpression of GPwt and VP40, directed the
majority of both proteins into the supernatant (Fig. 5 A, panels 2 and 4, lane 5)."],
[PMID:11877482 "Immunogold
staining of the VLPs with anti-Ebola GP antibodies demonstrated the identity of the spikes on the surface of the particles as Ebola GP (Fig. 6 B)."],
with EM showing release through small plasma-membrane platforms
[PMID:11877482 "C shows a typical site of VLP release, where a large number of particles that stain for GP exit through a small region of the plasma membrane (indicated by
arrows)."]. UniProt reads the same data the same way
[file:EBOZM/GP/GP-uniprot.txt "In the cell,
localizes to the plasma membrane lipid rafts, which probably represent the assembly
and budding site."]. VP40 is the budding driver; GP is incorporated and raises release
efficiency, so budding is a real but secondary role.

PMID:21223600 (third CACAO paper) reports that transiently expressed full-length GP
accumulates in the ER next to the nuclear membrane, and that GPΔmucin does not
[PMID:21223600 "Co-expression of Ebola GP with
DsRed2-ER showed that GP had localized within the ER (Figure 1B)."],
[PMID:21223600 "Strikingly, while GPΔmucin was expressed at comparable levels to full-length GP, it did not accumulate in the ER (Figure 2A)."].
Caveats worth recording: this is 10 µg plasmid in HEK293T at 24 h, i.e. gross
overexpression of a protein that is itself cytotoxic; the paper found **no** Golgi
signal, which sits badly with the established furin cleavage of GP in the trans-Golgi
[file:EBOZM/GP/GP-uniprot.txt "The precursor is processed into GP1 and GP2 by host cell furin in the trans
Golgi"]; and the authors themselves note other studies place GP at the plasma membrane
[PMID:21223600 "However, separate studies show that Ebola GP localizes in
the plasma membrane of either tissues from experimentally infected non-human primates [10] or HeLa cells 48 hours post-transfection [24]."].
ER residence is nonetheless expected for a signal-peptide-bearing, N-glycosylated type I
membrane protein, so the term is kept as a non-core biosynthetic location.

## Shedding and the soluble products

ADAM17/TACE cleaves at D637, removing the TM anchor and releasing GP1,2-delta
("shed GP") from the cell surface; shed GP is abundant in the blood of infected
animals and soaks up neutralising antibody
[PMID:15103332 "Proteolytic cleavage taking place at
amino-acid position D637 removes the transmembrane anchor and liberates
complexes consisting of GP1 and truncated GP2 (GP(2delta)) subunits from the
cell surface."],
[PMID:15103332 "we provide evidence
that shed GP is present in significant amounts in the blood of virus-infected
animals and that it may play an important role in the pathogenesis of infection
by efficiently blocking the activity of virus-neutralizing antibodies."].

Shed GP is not inert: it binds and activates uninfected DCs and macrophages, raising
pro- and anti-inflammatory cytokines and costimulatory molecules, and increases
vascular permeability; sGP does not do this
[PMID:25412102 "In effect it binds
and activates non-infected dendritic cells and macrophages inducing the
secretion of pro- and anti-inflammatory cytokines (TNFα, IL1β, IL6, IL8,
IL12p40, and IL1-RA, IL10)."]. The receptor is TLR4
[PMID:30085081 "We demonstrate that treatment of monocytic cells
with Ebola virus shed glycoprotein (GP) promotes their differentiation resulting
in increased infection and cell death. The effects were inhibited by blocking
Toll-like receptor 4 pathway."].

## Cytotoxicity / host-cell killing

Two mechanisms are documented, and they are different:
- **Cell-autonomous anoikis.** Adenovirus-delivered GP in primary human cardiac
  microvascular endothelial cells causes loss of adhesion then death; conditioned
  medium does not transfer the effect, so GP must be expressed intracellularly
  [PMID:15051379 "Transfer of conditioned medium from
EGP-transduced HCMEC into naive cells did not induce loss of adhesion or cell
death, suggesting that EGP needs to be expressed intracellularly to exert its
cytotoxic effect."]. Mechanistically this is downstream of GP-mediated
  down-modulation of integrins and MHC-I
  [file:EBOZM/GP/GP-uniprot.txt "Down-modulates
several integrins including ITGA1, ITGA2, ITGA3, ITGA4, ITGA5, ITGA6,
ITGAV and ITGB1 (PubMed:11112476)."] — UniProt flags the vascular consequence as
  `Probable`.
- **Bystander killing of T cells via TLR4.** GP binds CD4+ T cells through TLR4 and
  kills them without infecting them; the TLR4 inhibitor CLI-095 rescues
  [PMID:28542576 "we demonstrate that EBOV directly
binds to CD4+ T cells through interaction of GP with TLR4."],
  [PMID:28542576 "The addition of the TLR4
inhibitor CLI-095 significantly reduced CD4+ T cell death induced by GP."].

## Immune evasion

Besides the shed-GP antibody decoy, GP antagonises BST2/tetherin to allow virion
release, and down-regulates surface molecules needed for immune surveillance
[file:EBOZM/GP/GP-uniprot.txt "Counteracts the antiviral effect of host BST2/tetherin that restricts
release of progeny virions from infected cells (PubMed:26516900,
PubMed:27707924, PubMed:29669839)."]. These are the claims behind the
tetherin/innate-immune-suppression keyword IEAs.

## CACAO row-by-row verdict

| Term | Code | PMID | Action | Note |
|---|---|---|---|---|
| GO:0045121 membrane raft | IDA | 11877482 | ACCEPT | Two assay types + palmitoylation mutant + cholesterol control; exactly what the paper is about |
| GO:0046761 viral budding from plasma membrane | IDA | 11877482 | KEEP_AS_NON_CORE | Figs 5-6 support it; VP40 drives budding, GP contributes |
| GO:0044165 host cell ER | IMP | 21223600 | KEEP_AS_NON_CORE | Paper's own claim; overexpression caveat, no Golgi signal; code is really IDA (marker colocalisation) |
| GO:0030430 host cell cytoplasm | IDA | 20202662 | TOO_GENERAL | Paper has **no** GP-localisation assay (all imaging is of host clathrin/transferrin/Eps15); term is also entailed by the ER row |
| GO:0046718 symbiont entry into host cell | IMP | 20202662 | ACCEPT | Exactly the paper's result, and GP's core function |

New CACAO pattern worth adding to the taxonomy: **mechanism paper read as a
localisation** — an entry-pathway inhibitor study, whose only microscopy is of *host*
trafficking machinery, yielding an IDA cellular-component row on the *viral* protein.
It is the mirror image of "phenotype as process": here a process paper is converted
into a component annotation.

## Open questions

- Which lipid species does the GP2 fusion loop actually engage? The DisProt rows rest
  on SDS micelles and bulk DRM fractions (WITH/FROM is `ChEBI:8984`, sodium dodecyl
  sulfate — a detergent, not a lipid).
- Does GP2 palmitoylation at C670/C672, which is required for raft partitioning
  (PMID:11877482 Fig. 1B), matter for infectivity? UniProt records that palmitoylation
  is dispensable for function (PubMed:11152533), which is in tension with the raft
  requirement.
- Is the ER accumulation of PMID:21223600 a feature of infection or of plasmid
  overexpression?

## Final disposition (all 31 GOA rows + 2 proposals)

ACCEPT 22, KEEP_AS_NON_CORE 4 (GO:0039587 tetherin suppression, GO:0042802 identical
protein binding, GO:0044165 host cell ER, GO:0046761 budding), TOO_GENERAL 5
(GO:0019062, GO:0030430, GO:0039663, GO:0052031, GO:0075509 — each a strict ancestor of
a term kept in this review), plus 2 `NEW` molecular functions: `GO:0046789 host cell
surface receptor binding` and `GO:0035662 Toll-like receptor 4 binding`. GOA gives GP no
molecular function at all apart from `lipid binding` and `identical protein binding`,
which is a real gap for the protein whose entire job is binding host receptors.

Three source defects are recorded: the `ChEBI:8984` (SDS) WITH/FROM on the DisProt
lipid-binding IPI row; `IMP` where the assay is `IDA` on the CACAO host-cell-ER row; and
`WRONG_REFERENCE` (confidence CONFIRMED) on the CACAO host-cell-cytoplasm row, whose
cited paper contains no GP-localisation experiment.

Note for the schema: `core_functions.locations` cannot take `GO:0055036` virion membrane
or `GO:0019031` viral envelope, because `GOCellularLocationEnum` is reachable only from
`GO:0110165` cellular anatomical structure and virion components sit outside it. For a
virion surface protein that is where the core activity happens, so the virion membrane is
stated in the core-function descriptions instead.
