# tolC (P02930, *Escherichia coli* K-12) — curation notes

Working journal for the GO annotation review. Append-only; earliest sections first.

No `-deep-research-*.md` file was supplied for this gene and `just deep-research`
was not run, so the literature synthesis below is assembled directly from the 41
cached publications cited by GOA (all were present in `publications/`; none needed
fetching), the UniProt record, and targeted QuickGO/OLS queries. Every assertion
carries its provenance inline.

---

## 1. Identity, architecture and the one fact that organises everything else

TolC is a 493-residue precursor (signal peptide cleaved after residue 22) that
assembles into a **homotrimer** in the outer membrane. The trimer is not an
ordinary beta-barrel porin: it is a two-part conduit.

- Each monomer contributes four beta-strands to a shared 12-stranded
  outer-membrane barrel, and the barrel continues into the periplasm as a long
  alpha-helical tunnel: [PMID:10879525 "Three TolC protomers assemble to form a
  continuous, solvent-accessible conduit--a 'channel-tunnel' over 140 A long that
  spans both the outer membrane and periplasmic space."]
- The periplasmic end is **closed** in the resting state:
  [PMID:10879525 "The periplasmic or proximal end of the tunnel is sealed by sets
  of coiled helices."] and in more detail
  [PMID:21245342 "The TolC periplasmic entrance is closed by densely packed
  α-helical coiled coils, inner H7/H8, and outer H3/H4, constrained by a hydrogen
  bond network."]
- Independently described from 2-D crystals before the X-ray structure:
  [PMID:9044294 "The combined data suggest that TolC is a trimeric outer membrane
  protein with each monomer comprising a membrane domain, predicted to be
  beta-barrel, and a C-terminal periplasmic domain."]
- The trimer, not the monomer, is the functional unit:
  [PMID:7688606 "The oligomeric but not the monomeric form of the protein was able
  to increase the specific conductance of artificial lipid bilayer membranes."]
- Described as a uniquely TolC-like architecture among OMPs:
  [PMID:25218435 "E. coli TolC differs uniquely in having a trimeric antiparallel
  β-barrel channel domain embedded in the OM, which is connected to a
  trans-periplasmic trimeric α-helical tunnel domain"]

**The organising fact.** TolC is a *gated exit duct that is closed until a partner
opens it*, and it is shared. It has no energising component, no substrate-binding
pocket that selects cargo, and no catalytic chemistry. Specificity and energy both
live in the inner-membrane partner. Nearly every annotation decision below follows
from this: substrate-general terms describe TolC correctly, substrate-specific terms
describe its *partners*, and anything implying passive open-pore permeability
describes neither.

## 2. Subcellular location — outer membrane, settled since 1983

- First identification and localisation: [PMID:6337123 "The protein seen in cell
  envelopes of whole cells (TolC protein) was found to exist in an aggregated state
  in the outer membrane"]
- Purified from the OM as a trimer: [PMID:9044294 "the protein was purified from
  the Escherichia coli outer membrane, as a trimer, and crystallized in
  two-dimensional lattices by reconstitution in phospholipid bilayers"]
- UniProt: `SUBCELLULAR LOCATION: Cell outer membrane ... Multi-pass membrane
  protein` with ECO:0000269 from PubMed:15228545, 16079137, 21778229, 6337123,
  9044294.
- Independently recovered in four unbiased envelope/OM proteomics surveys
  (PMID:10806384, PMID:15911532, PMID:17309111, PMID:22534293). These are
  inventory papers; they place TolC in the envelope but carry no functional claim.

**Important consequence for the review:** TolC is in the **outer** membrane. It is
*not* in the plasma (inner) membrane. Two annotation groups get this wrong and are
handled accordingly (§10): the six NAS rows of `GO:0098567 periplasmic side of
plasma membrane`, and the single `GO:1990961` row (xenobiotic export across the
*plasma* membrane).

Note also that TolC's own extent is larger than the OM: its alpha-helical barrel
projects ~100 Å across the periplasm. That makes `GO:0030313 cell envelope` a
defensible — arguably more accurate — `is_active_in` location for TolC itself, not
merely a vague parent.

## 3. The shared-duct architecture: partners and assembly

TolC is recruited by periplasmic **membrane-fusion proteins (MFPs)**, which bridge
it to an inner-membrane transporter. It binds the MFP, not (stably) the transporter.

- The canonical tripartite assembly: [PMID:15228545 "the antiporter AcrB and the
  adaptor AcrA, which form a translocase in the inner membrane, interact with the
  outer membrane TolC exit duct to form a contiguous proteinaceous complex spanning
  the bacterial cell envelope"]
- TolC binds AcrA directly and energetically favourably:
  [PMID:15228545 "calorimetry demonstrated energetically favourable interactions of
  AcrA with both AcrB and TolC proteins"]; confirmed independently
  [PMID:15576805 "This paper provides the biochemical evidence for physical
  interactions between the outer membrane component, TolC, and the membrane fusion
  protein component, AcrA, of the major antibiotic efflux pump of Escherichia coli."]
- AcrB–TolC contact is detectable but transient/not load-bearing:
  [PMID:16101295 "The AcrB-TolC complex formed through disulfide cross-linking was
  detected when a specific pair of mutants was coexpressed in E. coli."] and the
  nanodisc reconstitution concluded the opposite of a direct docking:
  [PMID:26867482 "Projection structures of all three complexes emphasize the role of
  the periplasmic adaptor protein as part of the exit duct with no physical
  interaction between the inner and outer membrane components."]
- **The same duct serves three different transporter superfamilies.** This is the
  key promiscuity result: [PMID:19805313 "we reconstituted interactions and compared
  binding kinetics of the E. coli TolC with AcrA, MacA, and EmrA, the periplasmic
  MFPs that function in multidrug efflux with transporters from the RND, ABC, and MF
  superfamilies, respectively"], with
  [PMID:19805313 "The affinity of TolC to MFPs decreases in the order MacA > EmrA >
  AcrA."]
- Assembled complex is stable and substrate-stabilised:
  [PMID:15155734 "once assembled, the intermembrane AcrAB-TolC complex is stable
  during the separation of the inner and outer membranes and subsequent
  purification"]; [PMID:15155734 "We show that antibiotics, the substrates of
  AcrAB-TolC, stabilize interactions within the complex."]
- Assembly is constitutive for the drug pump, and this is explicitly contrasted with
  the protein-export machine: [PMID:15228545 "Assembly of the pump appeared to be
  constitutive, occurring in the presence and absence of drug efflux substrate."]
- Structures: AcrAB-TolC at near-atomic resolution
  [PMID:28355133 "we report the near-atomic resolution cryoEM structures of the
  Escherichia coli AcrAB-TolC multidrug efflux pump in resting and drug transport
  states, revealing a quaternary structural switch that allosterically couples and
  synchronizes initial ligand binding with channel opening"];
  MacAB-TolC [PMID:28504659 "A hexamer of the periplasmic protein MacA bridges
  between a TolC trimer in the outer membrane and a MacB dimer in the inner
  membrane, generating a quaternary structure with a central channel for substrate
  translocation."]; EmrAB-TolC
  [PMID:33065135 "Comparison of projection structures of EmrAB-TolC and AcrAB-TolC
  indicates that the outer membrane protein TolC linked to the periplasmic adaptor
  EmrA protein form an extended periplasmic canal."]
- Stoichiometry and cellular excess of TolC:
  [PMID:40083904 "the ATP-binding cassette (ABC)-family transporter MacB, the adaptor
  protein MacA, and the outer membrane protein TolC form the MacA6:MacB2:TolC3
  assembly to extrude antibiotics and virulence factors"]
- In-situ cryo-ET of the assembled and partial pumps:
  [PMID:40461577 "we resolve the in situ structures of the MacAB-TolC efflux pump in
  Escherichia coli by electron cryo-tomography and subtomogram averaging"], with a
  standing MacA–TolC intermediate: [PMID:40461577 "MacA-TolC subcomplex can exist as
  a stable entity in cells."]
- Mechanism of propulsion is the partner's, not TolC's:
  [PMID:29109272 "We propose that the assembled tripartite pump acts as a molecular
  bellows to propel substrates through the TolC exit duct, driven by MacB
  mechanotransmission."]

## 4. Small-molecule efflux — the dominant use

- TolC is required for AcrAB function and for the Mar multidrug-resistance phenotype,
  and the requirement is not transcriptional: [PMID:8824631 "functional TolC is
  required for the operation of the AcrAB efflux system and for the expression of the
  Mar phenotype"]; [PMID:8824631 "That the effect of TolC on the AcrAB pump is not
  regulatory in nature is shown by studies measuring the influence of a tolC::Tn10
  insertion mutation on the expression of an acrA::lacZ reporter fusion."]
- Substrate breadth of the main pump: [PMID:17210767 "AcrAB-TolC is the major,
  constitutively expressed tripartite multidrug efflux system in Escherichia coli
  that recognizes various structurally unrelated molecules, including many
  antibiotics, dyes, and steroids."]
- MacAB (ABC-type, macrolides) is strictly TolC-dependent:
  [PMID:11544226 "MacAB required TolC for its function in a way similar to that of
  most of the MFP-dependent transporters in E. coli"], shown genetically
  [PMID:11544226 "TolC-deficient E. coli ZK796 was transformed with pUCmacAB. The
  resulting transformed cells showed no increase in resistance (Table 2 ),
  indicating that the MacAB system depends on TolC."]
- EmrAB (MFS-type) is also a TolC partner: [PMID:19171121 "Previous work has
  indicated that EmrAB-TolC from Escherichia coli is such a tripartite system,
  comprised of EmrB an MFS transporter, EmrA, a membrane fusion protein and TolC, an
  outer membrane channel."]
- Where the substrate is picked up matters, and it is *periplasmic* for the RND
  pumps: [PMID:12923103 "this cooperative effect can be accounted for only if
  substrate capture by the multicomponent efflux transporter occurs in the periplasm
  but not the cytosol"]; directly demonstrated for AcrD
  [PMID:15743938 "This result suggested that AcrD can also capture aminoglycosides
  from the periplasm to extrude them into the medium in intact cells, acting as a
  \"periplasmic vacuum cleaner.\""]. ABC/MFS partners (MacAB, EmrAB) instead deliver
  from the cytoplasm. Either way TolC performs the same single step: conduction
  across the outer membrane.
- UniProt FUNCTION summarises the set: "Outer membrane channel, which is required for
  the function of several efflux systems such as AcrAB-TolC, AcrEF-TolC, EmrAB-TolC
  and MacAB-TolC."

## 5. Endogenous substrates — this is not only a drug-resistance protein

Two endogenous substrates are solidly established, and both matter for deciding
whether substrate-general or substrate-specific terms are right.

**Enterobactin (siderophore export).** Unusually for TolC, here the genetics are
*specific and exclusive*:
[PMID:16166532 "the outer membrane channel tunnel protein TolC but none of the
respective seven resistance nodulation cell division (RND) proteins CusA, AcrB, AcrD,
AcrF, MdtF (YhiV), or the twin RND MdtBC (YegNO) was essential for enterobactin
export across the outer membrane"];
[PMID:16166532 "Strains with deletion of tolC or entS , but not with deletion of
genes encoding RND transporters, excreted very little enterobactin into the growth
medium."]; and the authors' conclusion
[PMID:16166532 "it seems that TolC forms the only pathway for enterobactin to leave
the periplasm to the outside"]. Note that the inner-membrane partner for this route
is *unidentified* — the RND transporters were all excluded. So for enterobactin, TolC
is the only named protein in the outer-membrane step. Also relevant to the IGI
annotation with *fur*: tolC itself is not iron-regulated
[PMID:16166532 "Quantitative reverse transcription-PCR analysis of gene-specific
transcripts showed no significant changes in tolC expression upon iron depletion."] —
the *fur* interaction is a genetic background used to deregulate enterobactin
synthesis, not evidence that Fur controls tolC.

**Protoporphyrin IX (heme-precursor overflow).**
[PMID:25257218 "we demonstrate that this compound is expelled by the MacAB-TolC
pump, an efflux pump involved in E. coli and Salmonella for macrolide efflux"];
[PMID:25257218 "The E. coli macAB and tolC mutants accumulate PPIX and are sensitive
to photo-inactivation."];
[PMID:25257218 "We propose that PPIX is an endogenous substrate of the MacAB-TolC
pump in E. coli and S. typhimurium"]. UniProt records the quantitative phenotype:
tolC mutants accumulate 9× more PPIX than the complemented strain.

Other TolC-dependent exports in the cited set: indole via AcrEF
[PMID:10518736 "Defined inactivation of the acrEF gene, the product of which is known
as an energy-dependent multiple drug efflux pump, decreased indole excretion while
reintroduction of the acrEF gene restored it."] and the enterotoxin STII via MacAB
[PMID:29109272 "MacB is an ABC transporter that collaborates with the MacA adaptor
protein and TolC exit duct to drive efflux of antibiotics and enterotoxin STII out of
the bacterial cell."].

## 6. Type I protein secretion — the second, genuinely distinct use

This is the use the review must not let the efflux annotations swallow.

- The founding result: [PMID:2112747 "an E. coli outer membrane protein, the TolC
  protein, encoded by a gene not located in the hly cluster, is specifically required
  for hemolysin secretion"]
- And the mechanism, with TolC shown to be part of one contiguous channel:
  [PMID:9822594 "Both engaged HlyA, inducing the IM complex to contact TolC,
  concomitant with conformational change in all three exporter components."];
  [PMID:9822594 "Export thus occurs via a contiguous channel which is formed, without
  traffic ATPase ATP hydrolysis, by substrate-induced, reversible bridging of the IM
  translocase to the OM export pore."]
- TolC was already understood in these terms before the structure:
  [PMID:9044294 "TolC is an outer membrane protein required for the export of
  virulence proteins and toxic compounds without a periplasmic intermediate."]
- Note the mechanistic contrast with the drug pumps, which the curators of
  PMID:15228545 drew themselves: the drug pump is constitutively assembled, whereas
  the protein exporter bridges only on substrate engagement and then reverts.
- MacAB-TolC also carries polypeptide cargo:
  [PMID:28504659 "The MacA-MacB-TolC assembly of Escherichia coli is a transmembrane
  machine that spans the cell envelope and actively extrudes substrates, including
  macrolide antibiotics and polypeptide virulence factors."]

Caveat to keep in view: the *hly* locus is plasmid/pathogen-strain-borne and is not
present in K-12. Both PMID:2112747 and PMID:9822594 reconstitute export by supplying
HlyB/HlyD (and substrate) to a K-12-background host. So K-12 TolC's protein-secretion
competence is demonstrated, but it is a capability of the protein rather than a
pathway running in wild-type K-12.

`modules/bacterial_type_i_secretion.yaml` grounds its `outer_membrane_exit_duct` part
on P02930, assigns it `GO:0008320 transmembrane protein transporter activity` and
`GO:0009279 cell outer membrane`, and carries the explicit note that "The same protein
serves resistance-nodulation-division and major-facilitator efflux pumps. Membership
in this family is therefore not evidence that a given organism performs type I protein
secretion." My review agrees with the module on every point of substance (gated trimeric
duct; conducts protein cargo; OM location; family membership is not evidence of
secretion). Where we differ is only in which MF *id* is asserted, and §9 explains why I
did not propagate the module's `GO:0008320` into GOA.

## 7. Colicin E1 import — the duct runs backwards

- Genetics have long required tolC for colicin E1 killing; the bilayer work localised
  the interaction: [PMID:15465872 "OmpF and TolC channels in planar bilayers were
  occluded by colicins E3 and E1, respectively, from the trans- side of the
  membrane."]; [PMID:15465872 "Occlusion was dependent upon a cis- negative
  transmembrane potential."]
- The colicin's recognition element is its translocation domain:
  [PMID:15465872 "The OmpF recognition sites of colicins E3 and N, and the TolC
  recognition site of colicin E1, were found to reside in the N-terminal translocation
  domains."]; mapped further to
  [PMID:15465872 "This implies that the N-terminal segment, residues 1 – 180,
  containing the T-domain, mediates the interaction of colicin E1 with TolC."]
- Interpretation offered: [PMID:15465872 "A similar translocon could be formed by BtuB,
  TolC, and colicin E1"]
- Specificity is real: colicins E3 and N did not occlude TolC at any potential, and
  colicin E1 did not affect OmpF.
- UniProt FUNCTION: "TolC is also involved in import of colicin E1 into the cells
  (PubMed:23176499, PubMed:35199644)."

**Comparator used for the MF decision.** OmpF (P02931), the equivalent
outer-membrane translocator for colicins E3/N, carries `GO:0042912 colicin
transmembrane transporter activity` (IMP, PMID:1706457). So GO does give the OM
translocator a colicin transporter MF. TolC currently carries none — its colicin role
is recorded only as `GO:0005515 protein binding` with colicin E1 (P02978). Replacing
that uninformative row with `GO:0042912` matches the OmpF precedent and the UniProt
FUNCTION statement. Caveat recorded in the review: the newer structural work
(PubMed:35199644, "Colicin E1 opens its hinge to plug TolC") frames the interaction as
plugging, so whether colicin E1 actually *threads* TolC remains open; this is raised as
a suggested question rather than hidden.

## 8. Biogenesis — TolC is the *substrate* of TAM, not a participant in assembly

The `GO:0005515` row from PMID:35061668 pairs TolC with P0ADE4 = **TamA**
(translocation and assembly module subunit A):
[PMID:35061668 "Using TolC as a model protein, we demonstrate that assembly of conduit
subunits into the outer membrane uses the chaperone TAM to physically organise the
membrane-embedded staves of the conduit subunit of the efflux pump."]

Applying the participation test from CLAUDE.md: the entity that performs the assembly
step is TAM; TolC is the thing acted on. Being a chaperone substrate is not
participation in the chaperone's process. **No `NEW` biogenesis term is proposed.** The
interaction is real and worth recording in prose, but it supports no GO assertion on
TolC beyond what is already there. (This is the same relationship the `flu` review
records between Antigen 43 and TAM, from the other side.)

## 9. Three comparator checks that changed my mind

I ran these before writing any action, and two of them stopped me from proposing
annotations I had drafted.

### 9a. `GO:0030253 protein secretion by the type I secretion system` — rejected as NEW

I drafted this as an obvious gap: TolC is *the* outer-membrane factor of the paradigm
type I system, with direct in-vivo evidence (§6), and GOA carries no type I secretion
BP for it at all. The comparator check refutes the gap reading:

| protein | role | GO:0030253 | GO:0030256 |
|---|---|---|---|
| HlyB (P08716) | ABC transporter | IEA | IEA |
| PrtD (P23596) | ABC transporter | IEA | IEA |
| AprD (Q03024) | ABC transporter | IEA | IEA |
| HlyD (P06739) | MFP adaptor | — | — |
| PrtE (P23597) | MFP adaptor | — | — |
| **PrtF (P23598)** | **OMF (TolC ortholog)** | **—** | **—** |
| **AprF (Q03027)** | **OMF (TolC ortholog)** | **—** | **—** |
| **TolC (P02930)** | **OMF** | **—** | **—** |

The two direct TolC counterparts in the Prt and Apr type I secretion systems carry
only `GO:0015562`, exactly as TolC does. More decisive still: in all of GO there are
only **two** experimental `GO:0030253` annotations, and both are from one paper
(PMID:7703231) — hlyA (P09983, the *cargo*) and hlyD (P09986, the MFP). Curators
annotating the hemolysin system itself chose HlyA and HlyD and did not annotate TolC.
That is a decision to argue with explicitly, not an absence to fill. A second,
independent reason points the same way: *hly* is not in K-12 (§6).

→ **No NEW `GO:0030253`.** The protein-secretion use is represented in
`core_functions` prose and `knowledge_gaps`, and raised in `suggested_questions`.

### 9b. `GO:0015562` on the two protein-export references — not modified to `GO:0008320`

My second draft kept `GO:0015562` for the small-molecule rows but modified the two
protein-export rows (PMID:2112747, PMID:9822594) to `GO:0008320 transmembrane protein
transporter activity`, to agree with the module. The same table kills it: `GO:0015562`
is the term GO uses for *every* OMF including PrtF (IEA) and AprF (IEA + IBA), and no
OMF anywhere carries `GO:0008320`. Rewriting TolC alone would break it away from its
own family's convention on my preference, and the term's definition ("transfer of a
specific substance or related group of substances from the inside of the cell to the
outside") does cover a protein substrate. → **ACCEPT**, with the cargo-class point made
in `reason` and escalated as a suggested question.

### 9c. `GO:0015288 porin activity` — flagged, not removed

My instinct was that this is wrong: TolC is a gated duct, closed in the resting state
(§1), and the very reference annotated for it reports
[PMID:7688606 "The channels of 80 pS in 1 M KCl had a much smaller single-channel
conductance than the general diffusion pores of E. coli outer membrane (1500 pS)."] —
i.e. ~19-fold below a real diffusion pore. The paper's own conclusion is narrower than
"porin": [PMID:7688606 "The results are consistent with the assumption that TolC acts
as an outer membrane channel for peptides."]

But the comparator check shows `GO:0015288` is applied family-wide, and the TolC row is
a PAINT IBA on node PTN002011530: PrtF (IEA, GO_REF:0000118), AprF (IBA), *Salmonella*
TolC (IBA), E. coli TolC (IBA + IDA). Challenging an IBA means arguing with the node
placement, and TolC is the node's own exemplar — so the IBA survives that test. The
term is also not flatly false: the OM domain is a beta-strand barrel that conducts
solutes. → **MARK_AS_OVER_ANNOTATED** for both rows, not REMOVE: the term misleads by
implying a passive general-diffusion pore contributing to OM permeability, which is the
opposite of TolC's biology (UniProt records that *tolC* disruption *increases* outer
membrane permeability, PubMed:38628966), but it is a family-wide convention I am
flagging rather than a TolC-specific error I can overturn.

## 10. Positions taken on the problem groups

- **`GO:0098567 periplasmic side of plasma membrane` ×6 (all NAS).** TolC is not in the
  plasma membrane at any point in its life; it is an integral outer-membrane protein
  (§2), and the correct location is already annotated seven times with direct evidence.
  NAS is the weakest code and these rows come from papers about the *inner-membrane*
  components of the pumps (AcrD, MdtBC, EmrKY, periplasmic-capture modelling), where
  the location is right for the partner and wrong for TolC. `GO:0031241 periplasmic side
  of cell outer membrane` exists but does not fit either, since TolC spans the membrane
  rather than occupying one leaflet. → **REMOVE** ×6. This is not second-guessing an
  experimental annotation whose full text I have not read; it is a mislocation to the
  wrong membrane, contradicted by abundant direct evidence.
- **`GO:1990961` (export across the *plasma* membrane, IDA, PMID:11544226).** Same
  error in BP form, and the correctly-membraned sibling `GO:0140330` is already
  annotated seven times. → **MODIFY** → `GO:0140330`.
- **`GO:0005515 protein binding` ×10.** Per repo policy this term's defect is
  uninformativeness, not over-claiming. Nine rows (AcrA ×5, AcrB, MacA ×3, TamA, plus
  two unpartnered IDA rows) record interactions whose functional content is *already*
  captured by `GO:1990281 efflux pump complex` / `GO:1990196 MacAB-TolC complex` /
  `GO:0015562`, annotated from the very same references — so they add nothing and are
  **REMOVE**d (the interactions are real; removal is not a claim otherwise). The one
  exception is the colicin E1 row, which supports a genuinely more informative MF
  (§7) → **MODIFY** → `GO:0042912`.
- **`GO:0042802 identical protein binding` ×4.** Obligate homotrimerisation is a real,
  core structural fact for this protein, and `GO:0042802` is not the uninformative
  `GO:0005515` — it names the activity (self-association) rather than a partner. →
  **ACCEPT** ×4. One provenance caveat: PMID:25218435 studies the *cyanobacterial*
  homolog Slr1270 and mentions TolC's trimeric architecture only as cited background
  (I read the full text to confirm this). The claim it makes about TolC is nonetheless
  true and better evidenced by the other three rows, so I accept the row and record the
  citation concern in `reference_review` as `MISCITED` rather than deleting it.
- **Bile acid/salt terms (`GO:0015125` MF, `GO:0015721` BP, both IMP PMID:8824631).**
  TolC genuinely participates in bile-salt export as the AcrAB-TolC duct, so neither is
  false. But both impute a substrate-specific transporter identity to a duct whose
  specificity is AcrB's (§1), from a reference whose abstract reports no bile-acid assay
  (full text unavailable). The substrate-general terms already annotated
  (`GO:0140317`, `GO:0046618`, `GO:0015562`) state TolC's actual contribution without
  that implication. → **MARK_AS_OVER_ANNOTATED** ×2, deliberately not REMOVE.
- **Enterobactin terms (`GO:0042931` MF, `GO:0042930` BP).** Contrast with bile acid:
  here the genetics are specific, exclusive and TolC-directed, and no partner RND was
  identifiable (§5). → **ACCEPT** both.
- **`response to …` terms (`GO:0009410`, `GO:0009636`, `GO:0046677`).** Each is true but
  states the phenotype where the mechanism is known and already annotated. `GO:0009636`
  is additionally a literal ancestor of `GO:0140330` (verified: `GO:0140330`'s ancestors
  include `GO:0009636`, `GO:0140317`, `GO:0055085`, `GO:0042908`), so that row is
  formally redundant. → **MODIFY** ×3 → `GO:0140330`. (Contrast with
  `projects/ANTIMICROBIAL_RESISTANCE.md`, which notes `GO:0046677` is usually the *only*
  BP available for drug-*modifying* enzymes. For a transporter it is not.)
- **Ion channel terms (`GO:0005216` MF, `GO:0034220` BP, both IDA PMID:15465872).** The
  conductance is genuinely directly observed, but in a planar bilayer, and it is the
  assay readout for colicin occlusion rather than a physiological role — TolC has no
  part in ion homeostasis and is closed in the resting state. → **MARK_AS_OVER_ANNOTATED**
  ×2. (OmpF carries `GO:0005216` from the same paper, so this is a consistent
  curation habit rather than a TolC-specific slip; I flag it on TolC where the gated
  duct makes it most misleading.)
- **`GO:0016020 membrane` ×2 (IDA) and `GO:0019867 outer membrane` ×2.** Redundant
  ancestors of the seven-times-annotated `GO:0009279`. The two IDA `membrane` rows come
  from papers that themselves localise TolC to the OM → **MODIFY** → `GO:0009279`. The
  `GO:0019867` IDA row likewise. The `GO:0019867` IEA row is left **ACCEPT**ed, since
  CLAUDE.md allows IEA mappings to be broader than the curated picture.
- **`GO:0030313 cell envelope` ×3 (IDA, `is_active_in`).** Accepted on the positive
  argument in §2, not merely tolerated.

## 11. Core functions settled on

Three, deliberately: one for the shared duct itself, one for the protein-secretion use
(so it is not collapsed into efflux, per the task), and one for colicin import, which
is the only case where cargo moves *inward*. Endogenous-substrate export (enterobactin,
PPIX) is folded into the first rather than split out, since it is the same molecular
step with different partners.

Knowledge gaps recorded: (i) no GO MF distinguishes an outer-membrane-factor exit duct
from a passive porin, which is why `GO:0015288` keeps attaching to this family;
(ii) no OMF carries the type I secretion process term, so the protein-export use has no
machine-readable home on TolC; (iii) the inner-membrane partner for enterobactin export
is unidentified; (iv) whether colicin E1 threads TolC or merely plugs it is unresolved.

## 12. Validation

`just validate ECOLI tolC` run repeatedly during drafting; all 68 `supporting_text`
snippets were pre-checked against the cache with the repo's own
`build_supporting_text_validator` before being written into the YAML, so every quote is
a verbatim (whitespace-normalised) substring of the cached publication.
