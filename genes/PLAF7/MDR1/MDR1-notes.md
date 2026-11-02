# MDR1 (PfMDR1 / Pgh1, PF3D7_0523000, UniProt Q7K6A5) — curation notes

> **Provenance note.** Automated deep research was **not available** in this environment
> (Falcon auth failure, invalid OpenAI key), so **no `*-deep-research-*.md` file was generated**.
> What follows is a **manual literature review** carried out by reading the cached UniProt
> record, the cached publications in `publications/`, and targeted web searching. Every
> assertion below carries inline provenance as `[PMID:NNNN "verbatim quote"]` or a pointer
> to the UniProt flat file.

## Identity

- UniProt accession **Q7K6A5**; the entry carries **no gene symbol**, so the review's
  `gene_symbol` stays as the accession and the folder is the alias `MDR1`.
- Commonly called **PfMDR1** (P. falciparum multidrug resistance protein 1) or, in the
  older literature, **Pgh1** (P-glycoprotein homologue 1); gene id **PF3D7_0523000**.
- Family: UniProt — "Belongs to the ABC transporter superfamily. ABCB family.
  Multidrug resistance exporter (TC 3.A.1.201) subfamily."
  PANTHER: PTHR43394 / PTHR43394:SF27 (ATP-DEPENDENT TRANSLOCASE ABCB1-LIKE).
  Architecture: two ABC_membrane (PF00664) TMDs + nucleotide-binding domains (PF00005),
  i.e. a full-length type-1 ABC exporter (InterPro IPR039421).

## Localization — digestive (food) vacuole membrane

The founding localization paper is unambiguous:

- [PMID:1674943 "localized on the membrane of the digestive vacuole of mature parasites"]
- Same paper establishes the protein size and expression:
  [PMID:1674943 "the P. falciparum homologue of the P-glycoprotein (Pgh1) is a 160,000-D protein that is"]
- and that it is **not** overexpressed in chloroquine-resistant isolates as a rule:
  [PMID:1674943 "approximately equal levels in chloroquine resistant and sensitive isolates"]

Confirmed repeatedly since:

- [PMID:35507548 "PfMDR1 and PfCRT reside in the membrane of the parasite’s digestive vacuole (DV), the lysosomal-type compartment (pH 5.0 to 5.5) in which many antimalarials accumulate, act, and/or are activated."]
- [PMID:37527341 "Plasmodium falciparum multidrug resistance protein 1 (PfMDR1), an adenosine triphosphate (ATP)-binding cassette (ABC) transporter on the digestive vacuole"]

UniProt records `SUBCELLULAR LOCATION: Vacuole membrane {ECO:0000269|PubMed:1674943,
ECO:0000269|PubMed:8097560}; Multi-pass membrane protein`.

**Curation consequence.** The organelle is the apicomplexan **food vacuole** (GO:0020020),
and the protein sits in its **membrane**. GO has `GO:0005774 vacuolar membrane` but (checked
via OLS) **no "food vacuole membrane" term**, so the best available pair is
GO:0020020 + GO:0005774. The ARBA-derived `GO:0005737 cytoplasm` is true only in the
trivial sense that the vacuole is a cytoplasmic organelle; it is uninformative for an
integral DV-membrane protein.

## Nucleotide binding and ATPase activity

- Photoaffinity labelling of purified digestive vacuoles with 8-N3-ATP labels PGH1:
  [PMID:8097560 "This reagent labels a 160-kDa protein in vacuoles from both a chloroquine sensitive and a chloroquine-resistant parasite isolate."]
  and the labelling is nucleotide-specific:
  [PMID:8097560 "Inhibition of photoaffinity labeling of PGH1 could be achieved with ATP, ADP, GTP and GDP but not with AMP or GMP."]
  The authors already read this as a transport function at the DV membrane:
  [PMID:8097560 "involved in a nucleotide-regulated transport function across the membrane of the digestive vacuole"]
- Direct biochemistry on purified protein:
  [PMID:37527341 "To confirm that the PfMDR1 protein purified in a detergent solution is functionally active, we measured the ATP hydrolysis activity at different ATP concentrations."]
  [PMID:37527341 "Compared to the EQ mutant protein in which the key catalytic glutamates were mutated to glutamines, the wild-type PfMDR1 protein showed significant ATPase activity."]
  UniProt lists KM 0.33 mM for ATP and Vmax 198.3 nmol/min/mg (ECO:0000269|PubMed:37527341).
- Cryo-EM confirms a canonical ABC catalytic cycle (inward-facing apo → ATP-bound,
  NBD-dimerized, outward-facing toward the DV lumen) and an unusual N-terminal
  autoinhibitory element:
  [PMID:37527341 "Notably, there is a regulatory domain (R domain) on the N terminus of PfMDR1, significantly different from the well-studied R domain of cystic fibrosis transmembrane conductance regulator (CFTR) (34) and other ABC transporters (35), which is in the internal linker region."]
  [PMID:37527341 "we truncated the first two helices (residue 1 to 37) from the full-length PfMDR1 and found that the truncated protein has 80% higher ATPase activity than the full-length PfMDR1"]

## Transport activity and direction

The decisive functional work is the Xenopus oocyte system of Shafik et al.:

- [PMID:35507548 "Lumefantrine, mefloquine, and chloroquine are weak bases that enter the DV via 2 main routes: (1) simple diffusion of the neutral species across the membrane and subsequent protonation within the acidic DV lumen; and (2) ATP-driven import via PfMDR1."]
- ATP dependence of the transport itself:
  [PMID:35507548 "The microinjection of ATP into the oocyte greatly stimulated [3H]lumefantrine transport via PfMDR1NFCDY but had a milder effect on PfMDR1NYSND (Fig 1L)."]
- Direction is **cytosol → DV lumen** (import into the organelle), not efflux out of the cell:
  [PMID:35507548 "Likewise, for PfMDR1 the direction of transport is analogous to the PfMDR1-mediated transport of a substrate from the parasite’s cytosol into the DV (S9 Fig)."]
  [PMID:35507548 "By contrast, the overexpression of PfMDR1 (which increases the level of PfMDR1 at the DV membrane [93,94]) will heighten the rate of drug transport into the DV, thereby increasing the sequestration of drugs within this organelle."]

**This matters for GO.** PfMDR1 is *not* a plasma-membrane efflux pump; terms framing it as
cellular drug efflux (e.g. xenobiotic detoxification by transmembrane export across the
plasma membrane) would be wrong. Substrate range per UniProt: "Transports lumefantrine,
mefloquine, chloroquine, quinine, quinidine, amodiaquine, piperaquine, dihydroartemisinin
and quinacrine (PubMed:35507548)", plus human P-gp substrates rhodamine B and vinblastine,
and *not* amantadine.

## Drug resistance — what the IDA reference actually shows

- [PMID:10706290 "mutations in Pgh1 can confer resistance to mefloquine, quinine and halofantrine."]
- [PMID:10706290 "The same mutations influence parasite resistance towards chloroquine in a strain-specific manner and the level of sensitivity to the structurally unrelated compound, artemisinin."]
- Mechanistically, polymorphisms change transport capacity, redistributing drug between DV
  and cytosol:
  [PMID:35507548 "Of note, the PfMDR1 isoforms prevalent in chloroquine-resistant isolates exhibit reduced capacities for chloroquine, lumefantrine, and mefloquine transport."]

The GOA row derived from PMID:10706290 is `GO:0009410 response to xenobiotic stimulus (IDA)`.
The experiment is allelic exchange changing drug susceptibility — i.e. it demonstrates that
the protein *handles* the drugs, not that the gene product executes a cellular
"response to a xenobiotic stimulus" program. The accurate process term for what PfMDR1
itself does is `GO:0006855 xenobiotic transmembrane transport` (verified via OLS: a
descendant of both GO:0042908 xenobiotic transport and GO:0055085 transmembrane transport).

## Protist-specific checks performed

- **No animal/plant-only terms** are present in the GOA. The IBA rows (GO:0016020,
  GO:0042626, GO:0055085) come from a broad ABCB/MDR node (PANTHER:PTN000657189,
  PTN002517083) with plant, fungal, nematode, fly and mammalian donors; the claims they
  make (membrane, ATPase-coupled transport, transmembrane transport) are generic to the
  family and correct for PfMDR1 — they are simply less specific than the direct evidence.
- **Organelle checks**: the DV/food vacuole is a real apicomplexan compartment and is
  correctly used here; nothing is mis-assigned to apicoplast, rhoptry, microneme or the
  parasitophorous vacuole.
- **Host-vs-symbiont**: no host-interaction process terms are asserted, and none are
  warranted — PfMDR1 acts inside the parasite on the parasite's own DV membrane.
- **Paralog over-annotation**: P. falciparum has several ABC transporters (PfMDR2,
  PfMRP1/2, PfABCI3 etc.); none of the annotations reviewed here transfer a paralog-specific
  function onto PfMDR1. The EC 7.6.2.2 mapping (GO:0008559) is directly confirmed by
  UniProt's experimental CATALYTIC ACTIVITY entry for this accession.

## Knowledge gaps

- The **endogenous (non-drug) substrate is unknown**. [PMID:35507548 "Considerably less is
  understood about the function(s) of PfMDR1."] Targeted searching found no published
  natural substrate and no clean knockout; the drug substrates are almost certainly
  adventitious cargo of a transporter whose physiological job is still undefined. PfCRT,
  its DV-membrane neighbour, turned out to export haemoglobin-derived peptides
  [PMID:35507548 "PfCRT normally mediates the H+-dependent transport of hemoglobin-derived peptides from the DV into the parasite’s cytosol [10]"], which is the obvious model to test for PfMDR1.
- Essentiality is asserted but not, in the sources read here, backed by a conditional
  knockout: [PMID:35507548 "In addition to their roles in mediating multidrug resistance, PfMDR1 and PfCRT are essential for parasite survival and are thus themselves potential drug targets [1,5]."]
- Physiological trigger for the N-terminal R domain is unknown; unlike CFTR's R domain it
  lacks phosphorylation sites, so what relieves autoinhibition in vivo is open.

## Ontology gap noted

GO has no `food vacuole membrane` cellular-component term (OLS search returns nothing;
GO:0020020 has no children). A DV-membrane protein can currently only be annotated to the
generic GO:0005774 vacuolar membrane plus GO:0020020 food vacuole. Recorded as a
`proposed_new_terms` entry in the review.
