# AP4M1 (mu4-adaptin) — research notes

UniProt **O00189** (`AP4M1_HUMAN`), 453 aa, sequence version 2, entry version 194
(2026-09-02). Verified against `AP4M1-uniprot.txt`: the accession returns
`RecName: Full=AP-4 complex subunit mu-1`, so this is the intended protein and not a
merged/redirected accession. HGNC:574, chromosome 7q22. PANTHER family
**PTHR10529** "AP COMPLEX SUBUNIT MU" (`DR   PANTHER; PTHR10529; AP COMPLEX SUBUNIT MU`).

Single domain of note: `FT DOMAIN 184..452 /note="MHD"` (mu homology domain,
PROSITE PS51072). N-terminal ~180 residues are the longin-like subdomain that packs
into the AP core; the MHD is the cargo-signal-binding module. Two mutagenesis positions
are recorded, both inside the MHD and both from the APP co-crystal work:
`FT MUTAGEN 255 F->A: Abolishes interaction with APP` and
`FT MUTAGEN 283 R->D: Strongly reduced interaction with APP`
(`ECO:0000269|PubMed:20230749`). No catalytic residues — this is an adaptor, not an
enzyme, and no EC number is claimed anywhere in the record.

## 1. The complex: which subunit is which, and what compartment

AP-4 is a heterotetramer of two large adaptins (epsilon/AP4E1 and beta-4/AP4B1), one
medium adaptin (mu-4/AP4M1) and one small adaptin (sigma-4/AP4S1). Both founding papers
say so independently:

- [PMID:10066790 "Gel filtration, sedimentation velocity, and immunoprecipitation
  experiments revealed that beta4 is a component of a multisubunit complex (AP-4) that
  also contains the sigma4 polypeptide and two additional adaptor subunit homologs named
  mu4 (mu-ARP2) and epsilon."]
- [PMID:10436028 "We have shown by a combination of coimmunoprecipitation and yeast
  two-hybrid analysis that these four proteins (epsilon, beta4, mu4, and sigma4) are
  components of a novel adaptor-like heterotetrameric complex, which we are calling
  AP-4."]

and UniProt's SUBUNIT block agrees
(`file:human/AP4M1/AP4M1-uniprot.txt` "Adaptor protein complex 4 (AP-4) is a heterotetramer composed").
Loss of any one subunit destroys the complex — [PMID:30262884 "AP-4 consists of four
subunits (β4, ε, μ4 and σ4) forming an obligate complex"] — which is why subunit-level
and complex-level phenotypes are interchangeable in this literature, and why an
experiment on an AP4E1 knockout is evidence about the AP-4 coat rather than about
epsilon alone. That cuts both ways for curation: a complex-level result supports
`part_of`/`contributes_to`-style claims on mu4, but it does not by itself license a
mu4-specific molecular function.

**The coat is not clathrin.** This is the single most consequential fact for reviewing
this gene's GO record, and it is stated directly, by electron microscopy, in the paper
that named the complex: [PMID:10436028 "Immunogold electron microscopy indicates that
AP-4 is associated with nonclathrin-coated vesicles in the region of the trans-Golgi
network."] Fifteen years later the same group still opens with it —
[PMID:26542808 "The heterotetrameric (ϵ-β4-μ4-σ4) complex adaptor protein 4 (AP-4) is a
component of a non-clathrin coat involved in protein sorting at the trans-Golgi network
(TGN)."] — and GO's own definition of GO:0030124 records the caveat ("it is not clear
whether AP-4 forms clathrin coats in vivo"). The ontology backs this structurally as
well: GO:0030131 "clathrin adaptor complex" has exactly two children, GO:0030121
(AP-1) and GO:0030122 (AP-2), and GO:0030124 is **not** among its descendants
(checked via the QuickGO `/children` and `/ancestors` endpoints; AP-4's ancestors run
GO:0030119 → GO:0030117 → GO:0048475/GO:0098796).

Localization: TGN and TGN membrane, as a peripheral membrane protein on the cytosolic
face, plus a cytosolic pool and an early-endosomal pool. UniProt:
`SUBCELLULAR LOCATION: Golgi apparatus, trans-Golgi network membrane ...; Peripheral membrane protein ... Early endosome`.
[PMID:11707398 "This complex consists of four subunits (epsilon, beta4, mu4 and sigma4)
and localizes to the cytoplasmic face of the trans-Golgi network (TGN)."] The
association is ARF-regulated and brefeldin-A-sensitive
[PMID:10436028 "This pattern is disrupted by treating the cells with brefeldin A,
indicating that, like other coat proteins, the association of AP-4 with membranes is
regulated by the small GTPase ARF."].

## 2. mu4 is the cargo-signal recognition subunit, and its signals are its own

The division of labour inside an AP complex puts cargo recognition on the mu subunit.
For AP-4 this was shown at the same time as the complex itself
[PMID:10436028 "The mu4 subunit of the complex specifically interacts with a
tyrosine-based sorting signal, indicating that, like the other three AP complexes, AP-4
is involved in the recognition and sorting of cargo proteins with tyrosine-based
motifs."], and UniProt states it as the subunit-level function:
`Within AP-4, the mu-type subunit AP4M1 is directly involved in the recognition and binding of tyrosine-based sorting signals`.

What makes mu4 distinctive is *which* signals it reads. Aguilar et al. screened a
combinatorial peptide library with mu4 as bait and recovered a preference unlike that of
mu1/mu2/mu3 [PMID:11139587 "Statistical analyses of the results revealed that mu4
prefers aspartic acid at position Y+1, proline or arginine at Y+2, and phenylalanine at
Y-1 and Y+3 (phi)."], with micromolar affinity
[PMID:11139587 "Using surface plasmon resonance measurements, we determined the
apparent dissociation constant for the mu4-YXXphi interaction to be in the micromolar
range."]. A natural signal that fits is the LAMP-2 tail
[PMID:11139587 "These experiments showed that mu4 recognized the tyrosine signal from
the human lysosomal protein LAMP-2, HTGYEQF."]. Not all mu4 ligands are even YXXΦ:
the GluRδ2 tail binds through other motifs
[PMID:14572453 "The interaction between mu4 subunit of AP-4 and the delta2 C-terminal
involved multiple amino acid sequence motifs other than the classical tyrosine-based
signals."].

The structural case is the APP work. The APP tail motif is YKFFE, and the co-crystal
shows both the motif and the site on mu4 are atypical
[PMID:20230749 "Biochemical and X-ray crystallographic analyses reveal that the
properties of the APP sequence and the location of the binding site on mu4 are distinct
from those of other signal-adaptor interactions."], with the functional consequence
that disrupting it pushes APP down the amyloidogenic route
[PMID:20230749 "Disruption of the APP-AP-4 interaction decreases localization of APP to
endosomes and enhances gamma-secretase-catalyzed cleavage of APP to the pathogenic
amyloid-beta peptide."]. PDB 3L81 and 4MDR cover residues 160-453, i.e. the MHD.

Two further mu4 ligands are recorded, both on the cargo side: NAGPA
[PMID:26544806 "We found that the μ4 subunit of AP-4 interacts with NAGPA, an enzyme
involved in the synthesis of the mannose 6-phosphate signal that targets acid hydrolases
to the lysosome"] and ATG9A (below).

### The cargo-binding site tested against the sequence

`AP4M1-bioinformatics/mu_signal_site.py` fetches the sequences live and checks the two
UniProt mutagenesis positions. Results (full table in
`file:human/AP4M1/AP4M1-bioinformatics/RESULTS.md`): O00189 really is 453 aa with F255
and R283, both inside the MHD (184-452); F255 and R283 are present at the same native
positions in mouse (Q9JKC7), rat (Q2PWT8) and dog (E2RED8) mu4, but *Arabidopsis* AP4M
has N at the position aligned to 283.

The negative result matters more than the positive one. **F255 is not mu4-specific**:
every mu subunit tested — mu1A, mu1B, mu2, mu3A, mu3B — has a phenylalanine at the
aligned position. R283 separates mu4 from mu1A/mu1B/mu3A/mu3B (all serine) but *not*
from mu2 (R276). So the sequence alignment cannot be used to argue that mu4 reads a
different signal class; that claim rests on the crystallography and the peptide-library
screen, and this review cites it that way rather than dressing it up as a residue
argument. What the alignment does establish is the precondition for the UniProt ISS
rows: the dog and mouse donors share the cargo-binding surface with the human target.
Pairwise identity to mu1/mu2/mu3 comes out at 24.5-31.8%, reproducing the original
figure [PMID:9013859 "Both predicted proteins share 60% amino acid sequence identity
with each other and 27-31%, identity with mu1-adaptin (ap47) and mu2-adaptin (ap50)."].

## 3. ATG9A export is the function that finally explained AP-4

For nearly twenty years AP-4 had no assigned pathway
[PMID:11802162 "AP-1 and AP-3 mediate sorting events at the level of the TGN and/or
endosomes, whereas AP-2 functions in endocytic clathrin coated vesicle formation; no
function is known so far for AP-4."]. Two 2017-2018 papers settled it, by different
routes and in agreement.

Mattera et al. identified ATG9A as the specific cargo
[PMID:29180427 "Here we report the identification of ATG9A, the only multispanning
membrane component of the core autophagy machinery, as a specific AP-4 cargo."] and
placed the step at TGN export
[PMID:29180427 "AP-4 promotes signal-mediated export of ATG9A from the trans-Golgi
network to the peripheral cytoplasm, contributing to lipidation of the autophagy protein
LC3B and maturation of preautophagosomal structures."]. The IPI row behind UniProt's
`Interacts with tyrosine-based sorting signals ... such as APP, ATG9A, LAMP2 and NAGPA`
is the mu4-ATG9A interaction from this paper.

Davies et al. reached the same cargo from an unbiased proteomic direction
[PMID:30262884 "We identify three transmembrane cargo proteins, ATG9A, SERINC1 and
SERINC3, and two AP-4 accessory proteins, RUSC1 and RUSC2."], including in AP4M1
patient cells [PMID:30262884 "We demonstrate that AP-4 deficiency causes missorting of
ATG9A in diverse cell types, including patient-derived cells, as well as dysregulation
of autophagy."], and argued the AP-4 vesicles are a peripheral reservoir rather than a
direct delivery to the phagophore
[PMID:30262884 "These vesicles cluster in close association with autophagosomes,
suggesting they are the \"ATG9A reservoir\" required for autophagosome biogenesis."].
That distinction is why this review does **not** propose GO:0034497 "protein
localization to phagophore assembly site": the published model is a reservoir near
autophagosomes, not delivery to the PAS.

Crucially for a mu4-specific review, the ATG9A phenotype has been demonstrated in cells
whose lesion is in **AP4M1 itself**, not only in AP4E1/AP4B1 models
[PMID:29698489 "Importantly, we found that ATG9A was more concentrated at the TGN and
depleted from the peripheral cytoplasm in both skin fibroblasts from patients with
mutations in AP-4 μ4 and neurons from AP-4 ε KO mice, as compared to their normal
counterparts."]. Independent mouse work reaches the same conclusion
[PMID:31142229 "We show that ATG9A, critical for autophagosome biogenesis, is an AP-4
cargo, which is retained within the trans-Golgi network (TGN) in vivo and in culture
when AP-4 function is lost."], and the field's review states the consensus
[PMID:33084855 "Defective export of ATG9A from the TGN in AP-4-deficient cells was shown
to reduce ATG9A delivery to pre-autophagosomal structures, impairing autophagosome
formation and/or maturation."].

## 4. Accessory factors: which of them actually touch mu4

This is where the nine bare `GO:0005515` IPI rows have to be sorted out, because
"interacts with AP-4" and "interacts with mu4" are different claims.

- **HOOK1/HOOK2 (FHF complex) — direct mu4 binding.**
  [PMID:32073997 "We found that the AP-4-FHF interaction is mediated by direct binding of
  the AP-4 μ4 subunit to coiled-coil domains in the Hook1 and Hook2 subunits of FHF."]
  Functional consequence: [PMID:32073997 "Knockdown of FHF subunits resulted in dispersal
  of AP-4 and ATG9A from the perinuclear region of the cell"]. This is domain-specific
  binding in the literal sense (a named coiled-coil domain), so GO:0019904 fits.
- **TEPSIN — binds the beta-4 and epsilon EARS, not mu4.**
  [PMID:26542808 "we found that tepsin comprises two phylogenetically conserved peptide
  motifs, [GS]LFXG[ML]X[LV] and S[AV]F[SA]FLN, within its C-terminal unstructured region,
  which interact with the C-terminal ear (or appendage) domains of the β4 and ϵ subunits
  of AP-4, respectively."] Three of the nine `GO:0005515` rows on AP4M1 name TEPSIN
  (Q96N21) and all three come from complex-scale methods — a quantitative interactome
  (PMID:26496610), AP-4 affinity purification-MS (PMID:32073997) and BioPlex
  (PMID:33961781). They record co-membership of the AP-4 coat, which GO:0030124 already
  says, not a mu4 binding surface.
- **RUSC1/RUSC2 — AP-4 accessory, subunit not mapped to mu4** (PMID:30262884, above).
- **ARF1 — direct mu4 binding, and a real gap in the GO record.**
  [PMID:11707398 "In addition, we demonstrate a direct interaction of the epsilon and mu4
  subunits of AP-4 with ARF1."] The two subunits do it differently:
  [PMID:11707398 "epsilon binds only to ARF1-GTP and requires residues in the switch I and
  switch II regions of ARF1. In contrast, mu4 binds equally well to the GTP- and GDP-bound
  forms of ARF1 and is less dependent on switch I and switch II residues."] and the
  interacting region on mu4 is the cargo-binding module itself
  [PMID:11707398 "We map the interacting regions on the AP-4 subunits to the trunk region
  of ε and the signal-binding domain of µ4."] Nothing in the 53-row GOA set covers this.
  Proposed as a NEW row: GO:0031267 small GTPase binding ("Binding to a small monomeric
  GTPase"), IPI, PMID:11707398, partner UniProtKB:P84077 (human ARF1). Note that
  GO:0030742 "GTP-dependent protein binding" would be **wrong** for mu4 — nucleotide
  independence is the explicit finding — although it would be right for epsilon.
- **USP47 (Q96K76, Q96K76-3) and FNTA (P49354)** appear only in binary-interactome
  screens (PMID:25416956 HuRI pilot, PMID:32296183 HuRI) with no follow-up anywhere in
  the AP-4 literature.

## 5. Neuronal cargo, polarity, and disease

The rodent literature adds a somatodendritic-sorting role that human GOA records only
through ISS. AP-4 is neuronal and binds GluRδ2 (PMID:14572453, above); disrupting the
AP-4-TARP link mislocalizes AMPA receptors
[PMID:18341993 "AP-4 indirectly associated with the AMPA receptor via TARPs, and the
specific disruption of the interaction between AP-4 and TARPs caused the mislocalization
of endogenous AMPA receptors in axons of wild-type neurons."], with the interpretation
[PMID:18341993 "These results indicate that AP-4 may regulate proper somatodendritic-specific
distribution of its cargo proteins, including AMPA receptor-TARP complexes and the
autophagic pathway in neurons."]. MGI annotates mouse Ap4m1 GO:0006605 and GO:0008104
IMP from exactly this paper (checked in QuickGO), which is the upstream of the human
GO:0008104 ISS row from Q9JKC7, so the human record already carries this through the
proper evidence code and no human IMP should be invented for it.

Epithelial polarity is the dog result: AP-4 binds basolateral signals and mu4 knockdown
in MDCK cells missorts basolateral proteins apically
[PMID:11802162 "Furthermore, in MDCK cells with depleted mu 4 protein levels, several
basolateral proteins are mis-sorted to the apical surface, showing that AP-4 participates
in basolateral sorting in epithelial cells."]. MDCK is canine, and QuickGO shows dog
AP4M1 (E2RED8) carrying GO:1903361 IMP and GO:0005769/GO:0005802 IDA from precisely this
PMID — so the human ISS rows citing E2RED8 trace back to a real experiment in the right
species, not to a dangling ortholog.

Disease: biallelic loss of function causes SPG50 / AP-4 deficiency syndrome
[PMID:19559397 "In all five patients, a donor splice site pathogenic mutation in intron
14 of the AP4M1 gene (c.1137+1G-->T), was identified."], with the original description
also reporting the glutamate-receptor phenotype
[PMID:19559397 "Aberrant GluRdelta2 glutamate receptor localization and dendritic spine
morphology were observed in the postmortem brain specimen."]. AP4M1 is the
dose-limiting subunit in the therapeutic sense
[PMID:36951961 "We preformed preclinical studies evaluating an adeno-associated virus
(AAV)/AP4M1 gene therapy for SPG50 and describe in vitro studies that demonstrate
transduction of patient-derived fibroblasts with AAV2/AP4M1, resulting in phenotypic
rescue."]. Disease terms are deliberately not proposed as GO annotations here — GO
records the trafficking activity, and the spastic paraplegia is downstream phenotype.

## 6. The five IBAs: PAINT slice, node placement, and one clear leak

Family slice fetched with `just fetch-panther-paint PTHR10529` →
`interpro/panther/PTHR10529/PTHR10529-paint.tsv` (10 nodes, 18 node-level annotations).
The relevant nodes:

| node | assertion | seeds |
|---|---|---|
| PTN000055849 | GO:0005802 TGN (IBD) | AT1G60780, AT4G24550, SGD:S000001011, E2RED8, **O00189** |
| PTN000055849 | GO:0035615 clathrin-cargo adaptor activity (IBD) | FBgn0024833, FBgn0263351, DDB_G0289247, (Q9Y6Q5 in the 2026-08-28 slice) |
| PTN000055849 | GO:0006896 Golgi to vacuole transport (IBD) | SGD:S000000492, SGD:S000001011, SGD:S000006180, **O00189** |
| PTN000242612 | GO:0030124 AP-4 adaptor complex (IBD) | AT4G24550, **O00189** |
| PTN000242612 | GO:0006605 protein targeting (IBD) | MGI:1337063, E2RED8, **O00189** |
| PTN000242612 | GO:0090160 Golgi to lysosome transport (IBD) | **O00189** |
| PTN000242370 | GO:0030122 AP-2 adaptor complex (IBD); GO:0005802 **IRD** (rejected) | AP-2 mu subunits |
| PTN002237676 | GO:0030123 AP-3 adaptor complex (IBD) | SGD:S000000492, DDB_G0277901 |

So PTN000242612 is the AP-4 mu clade and PTN000055849 is the deep pan-mu node ancestral
to the mu subunits of all four AP complexes. The topology is sane — the curator even
placed an **IRD** at the AP-2 node rejecting the inherited TGN localization, which is
exactly right for a plasma-membrane adaptor and shows the node structure is being used
deliberately.

Donors resolved (UniProt `xref:` lookups, `size=5`, reported below with the Swiss-Prot
status):

- `AGI_LocusCode:AT4G24550` → Q9SB50 `AP4M_ARATH`, AP-4 complex subunit mu (reviewed;
  two TrEMBL isoform entries also match). QuickGO shows it carries GO:0030124 **IPI**
  from PMID:26546666 with three Arabidopsis partners — genuine experimental AP-4
  complex evidence in plants.
- `AGI_LocusCode:AT1G60780` → O22715 `AP1M2_ARATH`, AP-1 complex subunit mu-2
  (GO:0005802 IDA, PMID:23733933).
- `SGD:S000001011` → P38700 `APM2_YEAST` (GO:0005802 IDA, PMID:26658609).
- `UniProtKB:E2RED8` → AP4M1_CANLF, dog mu4 (GO:0005802 IDA, PMID:11802162).
- `MGI:MGI:1337063` → Q9JKC7 `AP4M1_MOUSE` (4 hits: 1 Swiss-Prot + 3 TrEMBL; the
  reviewed entry is the donor). GO:0006605 **IMP** from PMID:18341993.
- `FB:FBgn0024833` → O62531 `O62531_DROME`, **AP-1mu** (TrEMBL).
- `FB:FBgn0263351` → O62530 `O62530_DROME`, **AP-2mu** (TrEMBL).
- `dictyBase:DDB_G0289247` → Q54HS9 `AP1M_DICDI`, **AP-1 complex subunit mu** (reviewed).
- `UniProtKB:O00189` → the target itself; expected and not circular, since AP4M1's own
  IDA rows for GO:0005802 and GO:0090160 are among the descendant evidences the PAINT
  curator used to place those IBDs.

**Four of the five IBAs are sound.** GO:0005802, GO:0030124, GO:0006605 and GO:0090160
all sit at nodes whose seeds include AP-4 mu subunits (frequently AP4M1 itself), and the
target has independent experimental support for each.

**GO:0035615 "clathrin-cargo adaptor activity" is the leak.** Its IBD sits on the deep
pan-mu node PTN000055849 and **every one of its seeds is a clathrin-adaptor mu subunit**:
Drosophila AP-1mu and AP-2mu, Dictyostelium AP-1 mu, and (in the newer slice) human
AP1M2. Not one AP-4 subunit seeds it. QuickGO confirms each seed has its own
experimental grounding for the term (AP1M2 IDA PMID:10338135, AP2M1 IDA PMID:23676497,
AP-1mu IMP PMID:22389401, AP-2mu IMP PMID:20226669, apm1 IDA PMID:12802059) while
**AP4M1 has GO:0035615 by IBA only**. Extending that check across the AP-4 clade,
QuickGO returns exactly one GO:0035615 annotation for each of human O00189, mouse
Q9JKC7, rat Q2PWT8, dog E2RED8 and *Arabidopsis* Q9SB50, and in every case it is the
same IBA from GO_REF:0000033 — so no AP-4 mu subunit in any organism has experimental
evidence for this term. The term's definition does not tolerate the transfer: "Bringing together a cargo protein with
clathrin, responsible for the formation of endocytic vesicles" (QuickGO
`/ontology/go/terms/GO:0035615/complete`). AP-4 neither works with clathrin
(PMID:10436028 immunogold, PMID:26542808) nor acts in endocytosis (it is a TGN export
coat). The term was renamed from "clathrin adaptor activity" on 2025-12-24 and its
clathrin/endocytic definition dates from 2019-04-01; it is not obsolete and not merged.

The right correction is a generalisation rather than a deletion: GO:0035615's only
parent is **GO:0140312 "cargo adaptor activity"**, which drops the clathrin and
endocytic commitments while keeping the coat-cargo bridging that mu4 genuinely performs.
GO:0140312 currently has GO:0035615 as its sole child, which is itself the ontology-side
shape of this problem — the non-clathrin AP coats have nowhere more specific to go.

## 7. Other problem annotations in the GOA set

- **GO:0030131 clathrin adaptor complex (IEA, GO_REF:0000002, InterPro:IPR001392 +
  IPR018240).** Checked at the InterPro API: IPR001392 "Clathrin adaptor, mu subunit"
  and IPR018240 "Clathrin adaptor, mu subunit, conserved site" both map to GO:0006886,
  GO:0016192 and GO:0030131. The first two transfer fine. The third is a family-level
  over-call: the signatures match every mu subunit, but only mu1 and mu2 are in clathrin
  adaptor complexes, and GO itself places GO:0030124 outside GO:0030131. Demonstrably
  wrong interpro2go mapping for this protein.
- **GO:0008320 transmembrane protein transporter activity (TAS, Reactome:R-HSA-5229111).**
  Definition: "Enables the transfer of a protein from one side of a membrane to the
  other." AP-4 does vesicular transport, not translocation across a bilayer. The
  Reactome event is named "AP4 transports APP from trans-Golgi network to endosome
  lumen" and its summary (cached in `reactome/R-HSA-5229111.md`) describes signal
  recognition and vesicular transport, with no translocase step. The MF mapping is a
  modelling artefact of Reactome's "transport" reaction class.
- **GO:0071806 protein transmembrane transport (IEA, GO_REF:0000108, with GO:0008320).**
  Inter-ontology logical inference from the bad MF above; it inherits the error.
- **GO:0031904 endosome lumen (TAS, Reactome:R-HSA-5229111).** The lumen is where the
  *cargo* ends up in Reactome's model, not where the adaptor is. AP4M1 is a cytosolic,
  peripheral-membrane coat subunit and is never inside an endosome.
- **GO:0070062 extracellular exosome (HDA, PMID:19056867).** Urinary exosome shotgun
  proteomics; the standard high-throughput CC that says nothing about function.
- **GO:0006622 protein targeting to lysosome / GO:0090160 Golgi to lysosome transport
  (IDA, PMID:11139587).** Both rest on one reporter experiment
  [PMID:11139587 "we constructed a Tac chimera bearing a mu4-specific YXXphi signal. This
  chimera was targeted to the endosomal-lysosomal system without being internalized from
  the plasma membrane."] — a chimera bearing a signal *selected by* mu4, showing what
  such a signal can do, not that an endogenous lysosomal protein is an AP-4 cargo. No
  endogenous lysosomal cargo of AP-4 has been established since; the unbiased survey
  (PMID:30262884) returned ATG9A, SERINC1 and SERINC3. Real but peripheral, so
  KEEP_AS_NON_CORE rather than REMOVE — the curator read the full text and the
  experiment is genuinely an IDA.

## 8. What the affinage record missed

`AP4M1-deep-research-affinage.md` tripped a trust gate: its own head-to-head
self-evaluation scored `self_evaluation_pairwise: tie` against the curated UniProt
reference (recorded in `.affinage.log`), and the narrative bears that out. Its six
citations (PMID:9013859, 19559397, 24486887, 33553621, 34087981, 36951961) are the
cloning paper plus five clinical/genetic/iPSC-line papers. It says in as many words
that "the molecular cargo-recognition mechanism of AP4M1 has not been further
characterized in the available corpus" — which is precisely backwards for this gene.

Missed, and found here by independent PubMed E-utilities searches on the symbol, the
subunit name, each partner and the complex: PMID:11139587 (the mu4 signal-specificity
screen), PMID:10436028 and PMID:10066790 (complex identification and the non-clathrin
EM), PMID:20230749 (APP co-crystal and the F255/R283 site), PMID:29180427 and
PMID:30262884 (ATG9A as cargo), PMID:29698489 and PMID:31142229 (in vivo ATG9A
mislocalization), PMID:11707398 (mu4-ARF1, the source of a NEW annotation),
PMID:26542808 (tepsin binds beta-4/epsilon, not mu4), PMID:32073997 (mu4-HOOK1/2),
PMID:14572453 and PMID:18341993 (neuronal cargo), PMID:33084855 (the field review). All
fourteen are cited in the review, which carries 24 PMID references in total, every one of
them used in at least one `supported_by` (counted from the finished YAML, not asserted). Affinage's `mechanism_profile` grounding
(GO:0060090 molecular adaptor activity; Reactome R-HSA-5653656) was not imported; the
MF was re-grounded from the narrative and the primary papers.

Europe PMC's REST search endpoint returned HTTP 503 throughout this session, so all
literature discovery went through NCBI E-utilities (`esearch`/`esummary`) instead.

## 9. Curation decisions, in brief

Counted from the finished YAML by `AP4M1-bioinformatics/goa_reconciliation.py`, not
asserted: 53 GOA rows map onto 52 seeded entries (the one many-to-one collapse is two
`GO:0005515 IPI PMID:32073997 UniProtKB:Q9UJC3` rows differing only in DATE), plus 2 NEW
rows, for 54 entries in total. Actions: 23 ACCEPT, 14 KEEP_AS_NON_CORE, 7
MARK_AS_OVER_ANNOTATED, 4 MODIFY, 4 REMOVE, 2 NEW. Eighteen rows carry
`propagation_review` (5 IBA, 3 ISS, 10 IEA with `supporting_entities`); all 18 are
present and every `source_id` in them comes from that row's own seeded
`supporting_entities`, which the same script checks.

- Core: mu4 is the cargo-signal-recognition subunit of the non-clathrin AP-4 coat at the
  TGN; the complex-level activity is cargo adaptor activity, which mu4 contributes to
  rather than independently enables. Core BPs: export of ATG9A from the TGN supporting
  autophagosome formation, and export of APP from the TGN to endosomes.
- Non-core: early endosome, Golgi apparatus, cytoplasm, cytosol, the two
  lysosomal-transport terms resting on the Tac chimera, the two near-root
  protein-localization terms, vesicle-mediated transport, and basolateral polarity (ISS
  from dog).
- REMOVE (4): GO:0030131 clathrin adaptor complex (interpro2go over-call, contradicted by
  EM and by GO's own placement of AP-4 outside that branch); GO:0008320 transmembrane
  protein transporter activity and GO:0031904 endosome lumen (both Reactome reaction-class
  artefacts); GO:0071806 protein transmembrane transport (inter-ontology inference whose
  premise is the bad GO:0008320).
- MODIFY (4): GO:0035615 -> GO:0140312 cargo adaptor activity; the ATG9A `GO:0005515` row
  -> GO:0140312; the NAGPA and HOOK1 `GO:0005515` rows -> GO:0019904.
- MARK_AS_OVER_ANNOTATED (7): three TEPSIN rows (tepsin binds the beta-4 and epsilon ears,
  not mu4), USP47 twice, FNTA, and the urinary-exosome HDA.
- NEW (2): GO:0031267 small GTPase binding (mu4-ARF1, PMID:11707398, partner P84077) and
  GO:0030120 vesicle coat (immunogold EM, PMID:10436028).
- Ontology gap proposed: a general "tyrosine-based sorting signal binding" MF. GO's only
  term of that shape, GO:0089710 "endocytic targeting sequence binding", is restricted to
  clathrin-coated-pit internalization and so is unusable for mu1, mu3 or mu4.

The one validation warning left is "No annotations reference available deep research
files". That is deliberate: the affinage record tripped its trust gate, the campaign rule
forbids quoting an affinage sentence as `supporting_text` for a mechanistic claim, and
nothing in this review rests on it. It is carried in `references` with a
`reference_review` of `relevance: LOW`, `correctness: LOW_QUALITY` instead.
