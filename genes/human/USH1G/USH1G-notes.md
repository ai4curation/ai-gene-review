# USH1G / SANS (Q495M9) — curation notes

Scaffold protein containing **AN**kyrin repeats and **S**AM domain. 461 aa, ~51.5 kDa,
17q25.1. Domain architecture (UniProt Q495M9): three N-terminal ANK repeats (31-60,
64-93, 97-126), a central "CENT" region containing two MobiDB-lite disordered segments
(208-243, 332-368), a C-terminal SAM domain (385-447) and a terminal class-I
PDZ-binding motif (…DEL, residues 459-461).

> "The SANS protein contains three ankyrin domains and a sterile alpha motif, and its
> C-terminal tripeptide presents a class I PDZ-binding motif."
> [PMID:12588794]

## 1. Disease gene identity

Biallelic *USH1G* variants cause Usher syndrome type 1G (MIM 606943): congenital
profound sensorineural deafness, vestibular areflexia, prepubertal retinitis
pigmentosa. Weil et al. identified the gene by positional cloning of the mouse
*Jackson shaker* (*js*) orthologue:

> "These results demonstrate that SANS underlies USH1G." [PMID:12588794]

> "In Jackson shaker mice the hair bundles, the mechanoreceptive structures of inner
> ear sensory cells, are disorganized." [PMID:12588794]

A subset of *USH1G* alleles (e.g. p.Met104Val, p.Asp458Val) cause **non-syndromic**
progressive sensorineural hearing loss without ophthalmic or vestibular findings
(UniProt DISEASE note, ECO:0000269|PubMed:25255398), showing that the auditory arm of
the phenotype is the most dose-sensitive.

## 2. Hair cell: upper tip-link density (UTLD) scaffold — the core function

SANS binds harmonin/USH1C and MYO7A and localises with them at the **upper tip-link
density** of mature stereocilia — the tension-bearing anchor of the CDH23 end of the
tip link. This is the mature-bundle USH1 complex, distinct from the transient
ankle-link/USH2 complex of developing bundles.

> "Using immunofluorescence, we now show that MYO7A and sans, a MYO7A-interacting
> protein, cluster at the UTLD." [PMID:21709241]

> "Cotransfection studies in a heterologous system show that MYO7A, sans, and the UTLD
> protein harmonin-b form a tripartite complex and that each protein is capable of
> interacting with one another independently." [PMID:21709241]

> "We propose that MYO7A, sans, and harmonin-b form the core components of the UTLD
> molecular complex." [PMID:21709241]

> "In this complex, MYO7A is likely the motor element that pulls on CDH23 to exert
> tension on the tip-link." [PMID:21709241]

Molecular basis of the harmonin link (crystal structure 3K1R, 2.3 Å, SANS 388-461):

> "We discover that the SAM domain of Sans, specifically, binds to the PDZ domain of
> harmonin, revealing previously unknown interaction modes for both PDZ and SAM
> domains." [PMID:20142502]

> "We further show that the synergistic PDZ1/SAM and PDZ1/carboxyl PDZ binding-motif
> interactions, between harmonin and Sans, lock the two scaffold proteins into a highly
> stable complex." [PMID:20142502]  (K_D ≈ 1 nM for the bipartite interaction)

> "Mutations in harmonin and Sans found in USH1 patients are shown to destabilize the
> complex formation of the two proteins." [PMID:20142502]

The MYO7A link is via the central region binding the MyTH4-FERM cassette of the MYO7A
tail (PDB 3PVL, SANS 295-390; UniProt MUTAGEN F307E, F317E, W374Q all reduce MYO7A
affinity, ECO:0000269|PubMed:21311020).

**Self-association caveat.** SANS SAM-PBM homo-oligomerises in vitro, but harmonin
binding is mutually exclusive with it:

> "We noted that wild-type Sans SAM-PBM tends to form various forms of homo-oligomers
> in solution" [PMID:20142502]

> "The direct interaction between Sans SAM and harmonin PDZ1 prevents the formation of
> the SAM homo-multimer" [PMID:20142502]

So GO:0042802 "identical protein binding" is real but is an in-vitro property of the
free protein, not a property of the physiological UTLD complex — non-core.

## 3. Photoreceptor: ciliary base / periciliary scaffold and IFT-B positioning

> "The USH1G protein SANS is a scaffold of the ciliary/periciliary USH protein network
> of photoreceptor cells." [PMID:31637240]

> "Moreover, SANS is associated with microtubules, the transport routes for protein
> delivery toward the cilium." [PMID:31637240]

> "Our study demonstrated direct binding of IFT complex B proteins IFT52 and IFT57 to
> the N-terminal ankyrin repeats and the central domain of SANS." [PMID:31637240]

> "Quantitative immunofluorescence microscopy revealed the co-localization of SANS with
> IFT20, IFT52, and IFT57 particularly at ciliary base of wild type mouse photoreceptor
> cells." [PMID:31637240]

> "Analysis of photoreceptor cells of SANS knock out mice revealed the decrease of IFTs
> in the ciliary compartment indicating a role of SANS in the proper positioning of
> IFT-B molecules in primary cilia." [PMID:31637240]

The USH1G alleles p.Leu48Pro and p.Met104Val both reduce IFT52/IFT57 binding
(UniProt VARIANT annotations, ECO:0000269|PubMed:31637240), tying the ciliary arm of
the phenotype to this interaction.

## 4. Endocytosis at the periciliary membrane (MAGI2)

> "we identified Magi2 (membrane-associated guanylate kinase inverted-2) as a new
> component of the USH protein interactome, binding to the multifunctional scaffold
> protein SANS (USH1G)" [PMID:24608321]

> "We showed that the SANS-Magi2 complex assembly is regulated by the phosphorylation of
> an internal PDZ-binding motif in the sterile alpha motif domain of SANS by the protein
> kinase CK2." [PMID:24608321]  (Ser422; S422A abolishes MAGI2 binding)

> "We affirmed Magi2's role in receptor-mediated, clathrin-dependent endocytosis and
> showed that phosphorylated SANS tightly regulates Magi2-mediated endocytosis."
> [PMID:24608321]

> "we demonstrated the localization of the SANS-Magi2 complex in the periciliary
> membrane complex facing the ciliary pocket of retinal photoreceptor cells in situ"
> [PMID:24608321]

> "Specific depletions by RNAi revealed that SANS and Magi2-mediated endocytosis
> regulates aspects of ciliogenesis." [PMID:24608321]

UniProt's SUBUNIT text records the direction as inhibitory: "the interaction is
triggered by phosphorylation of USH1G by CK2 and negatively regulates MAGI2-mediated
endocytosis". The abstract itself says only "tightly regulates", so the GOA term
GO:2000369 (unsigned regulation) is the defensible level.

## 5. Nucleus: intranuclear tri-snRNP transfer / pre-mRNA splicing

The 2021 finding that reoriented the UniProt recommended name to "pre-mRNA splicing
regulator USH1G":

> "Previously, SANS was shown to function only in the cytosol and primary cilia."
> [PMID:34023904]

> "We show that SANS is found in Cajal bodies and nuclear speckles, where it interacts
> with components of spliceosomal sub-complexes such as SF3B1 and the large splicing
> cofactor SON but also with PRPFs and snRNAs related to the tri-snRNP complex."
> [PMID:34023904]

> "SANS is required for the transfer of tri-snRNPs between Cajal bodies and nuclear
> speckles for spliceosome assembly and may also participate in snRNP recycling back to
> Cajal bodies." [PMID:34023904]

> "SANS depletion alters the kinetics of spliceosome assembly, leading to accumulation
> of complex A." [PMID:34023904]

> "SANS deficiency and USH1G pathogenic mutations affects splicing of genes related to
> cell proliferation and human Usher syndrome." [PMID:34023904]

**Curation gap identified:** GOA carries the two nuclear CC terms (Cajal body, nuclear
speck, both IDA from PMID:34023904) but **no biological-process term for splicing at
all**, even though this is the function UniProt now uses to name the protein. Proposed
as a NEW annotation: GO:0048024 *regulation of mRNA splicing, via spliceosome* (IMP).

Follow-on work (not in the cached publications set, from the deep-research report):
Fritze et al. 2023 (doi:10.3390/ijms242417608) map PRPF31 to CENTn1 and PRPF6 to
CENTn1/CENTn2; Fritze et al. 2024 (doi:10.3390/cells13221855) map an NLS at 213-224 and
CRM1-dependent NESs at 181-195 and 406-420, showing regulated nucleocytoplasmic
shuttling that distinguishes SANS from its cytoplasmic paralog ANKS4B.

## 6. Other verified partners

- **PDZD7** (Q9H5P4): "Protein-protein interaction assays revealed the integration of
  PDZD7 in the protein network related to the human Usher syndrome." [PMID:19028668]
- **Spectrin βV** (SPTBN5): "We showed that spectrin βV also associates with two USH1
  proteins, sans (USH1G) and harmonin (USH1C)." [PMID:23704327]; spectrin βV in turn
  "binds to several subunits of the microtubule-based motor proteins, kinesin II and
  the dynein complex" — i.e. SANS is coupled to the photoreceptor trafficking route.
- **CDH23 / PCDH15**: by similarity from mouse Q80T11 (UniProt); "these interactions may
  recruit USH1G to the plasma membrane". This is the basis of the ISS/IEA plasma-membrane
  annotations.

## 7. Reference problem found during review

**PMID:11398101** (Ahmed et al. 2001, "Mutations of the protocadherin gene PCDH15 cause
Usher syndrome type 1F") carries three IMP annotations on USH1G in GOA
(GO:0045494 photoreceptor cell maintenance; GO:0007605 sensory perception of sound;
GO:0050953 sensory perception of light stimulus), all assigned by HGNC-UCL in 2007.
The cached record has `full_text_available: true`, and a full-text search returns
**zero occurrences of "SANS" or "USH1G"**. The paper is entirely about *PCDH15*/USH1F
and predates the 2003 identification of SANS as the USH1G gene product by two years —
so it cannot be the source of a USH1G IMP.

Per project policy the underlying biology is not in doubt (USH1G loss causes congenital
deafness and RP; PMID:12588794, UniProt DISEASE), so the annotations were kept rather
than removed, but PMID:11398101 is flagged `correctness: MISCITED` in `references` and
PMID:12588794 added as `additional_reference_ids`. The three rows should ideally be
re-referenced by GOA.

## 8. Summary of curation stance

| Compartment | Role | GO handling |
|---|---|---|
| Stereocilium UTLD (mature bundle) | scaffold linking MYO7A ↔ harmonin ↔ CDH23; tip-link tensioning complex | core; NEW GO:1990435, NEW GO:0030674 |
| Photoreceptor ciliary base / periciliary membrane | positions IFT-B (IFT20/52/57); MAGI2-dependent endocytosis | core (GO:0097546, GO:0032391, GO:0097733, GO:2000369) |
| Nucleus (Cajal bodies, speckles) | intranuclear tri-snRNP transfer, spliceosome assembly | core; CC accepted, NEW BP GO:0048024 |
| Cytosol / cytoskeleton / plasma membrane (generic) | true but uninformative | kept, mostly non-core |
| GO:0005515 protein binding (12 IPI rows) | uninformative | MODIFY for the four characterised partner papers; MARK_AS_OVER_ANNOTATED for the eight high-throughput screens |
