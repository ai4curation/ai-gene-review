# PPP2R2A (PP2A B55-alpha, P63151) — curation notes

## Identity and architecture

PPP2R2A encodes the ~55 kDa B-type (B/B55/PR55) regulatory subunit alpha of protein
phosphatase 2A. It was cloned from PR55 peptide sequences obtained by purifying the
trimeric PP2A1 holoenzyme from rabbit skeletal muscle
[PMID:1849734 "Amino acid sequences derived from the 55-kDa regulatory subunit (PR55) were used to clone human and rabbit cDNAs encoding this protein."],
and the gene family comprises alpha and beta paralogues
[PMID:1849734 "The PR55 subunit was found to be encoded by two genes, termed alpha and beta."]
(PR55-beta = PPP2R2B, the neuronal-enriched isoform of that paper).

The holoenzyme is a heterotrimer of a catalytic C subunit (PPP2CA/CB), a HEAT-repeat A
scaffold (PPP2R1A/B) and one variable B subunit
[PMID:30595372 "PP2A holoenzymes comprise catalytic C-, scaffolding A-, and regulatory B-type subunits, which determine substrate specificity and physiological function."].
B55-alpha is a seven-bladed WD40 beta-propeller carrying an acidic substrate-binding
groove on its top face, latched onto the A scaffold by a protruding beta-hairpin arm
[PMID:18922469 "The Balpha subunit comprises a seven-bladed beta propeller, with an acidic, substrate-binding groove located in the center of the propeller."].
UniProt records seven WD repeats (11-446) and notes that the extended WD 2 repeat mediates
the PPP2R1A contact (ECO:0000269|PubMed:38123684).

Critically for grading MF rows: **the catalytic centre is in the C subunit, not in B55-alpha.**
B55-alpha recruits, positions and selects substrates; PP2A-C hydrolyses the phosphoester.
This is why `contributes_to` (not `enables`) is the correct qualifier for phosphatase
activity on this gene product, and why `GO:0019888 protein phosphatase regulator activity`
and `GO:0140767 enzyme-substrate adaptor activity` are the informative MF terms for it
[PMID:20711181 "It is generally accepted that the regulatory B-type subunit confers substrate specificity and thereby regulates diverse functions of PP2A"].

## Core function 1: the CDK1-counteracting phosphatase of mitotic exit

A genome-wide live-cell RNAi screen of human phosphatases identified the PP2A-B55-alpha
trimer as the principal mitotic-exit phosphatase
[PMID:20711181 "We identify a trimeric PP2A-B55alpha complex as a key factor in mitotic spindle breakdown and postmitotic reassembly of the nuclear envelope, Golgi apparatus and decondensed chromatin."],
acting downstream of CDK1 inactivation
[PMID:20711181 "we find that PP2A-B55alpha functions downstream of Cdk1 inactivation"],
i.e. on the CDK1 substrates themselves rather than on the kinase switch. Cryo-EM work frames
the same logic: mitotic exit is driven by phosphatases, especially PP2A:B55
[PMID:38123684 "mitotic exit is achieved by counteracting dephosphorylation, a process driven by phosphatases, especially PP2A:B55"],
and PP2A:B55 has hundreds of substrates
[PMID:38123684 "PP2A:B55 dephosphorylates hundreds of substrates"].

Reactome places B55-alpha-specific reactions in this window: FOXM1 dephosphorylation
(R-HSA-4088141, nucleoplasm) and BANF1/BAF dephosphorylation in anaphase/telophase with
ANKLE2 as the targeting factor (R-HSA-2995388, R-HSA-9667965) — the latter summary states
outright that "The PP2A complex that contains the regulatory subunit PPP2R2A (B55-alpha) is
the only phosphatase essential for mitotic exit".

Repository modules `modules/g2_m_transition.yaml` and
`modules/metaphase_anaphase_transition_and_mitotic_exit.yaml` both use PPP2R2A (P63151) as
the B55 exemplar, typed as the "substrate-targeting regulatory subunit that confers
CDK-substrate preference" in the holoenzyme whose function is
`GO:0004722 protein serine/threonine phosphatase activity`. The `genes/human/MASTL` review
is the mirror image: MASTL phosphorylates ENSA/ARPP19 to inhibit exactly this holoenzyme.

## Core function 2: inhibitor-gated regulator activity (mitotic entry, G2/M checkpoint)

B55-alpha is the subunit the physiological PP2A inhibitors bind. Cryo-EM structures of
PP2A:B55 with thiophosphorylated ARPP19 and with FAM122A/PABIR1 show that both
intrinsically disordered inhibitors dock on B55 itself
[PMID:38123684 "both intrinsically disordered proteins bind PP2A:B55, but do so in highly distinct manners, leveraging multiple distinct binding sites on B55"],
occupying the same B55 platform that substrates such as p107 use
[PMID:38123684 "All p107 residues that had reduced N/HN cross-peaks"] — i.e. inhibition is
competitive with substrate recruitment. FAM122A binds Aalpha and B55-alpha specifically, not
B56-alpha, and inhibits the trimer
[PMID:27588481 "directly interacts with PP2A-Aα and B55α rather than B56α subunits, and inhibits the phosphatase activity of PP2A-Aα/B55α/Cα complex"].
In striatum the ARPP-16 route does the same thing via MAST3
[PMID:28167675 "phosphorylation of ARPP-16 at Ser46 by MAST3 kinase converts the protein into a selective inhibitor of B55α- and B56δ-containing heterotrimeric forms of PP2A"].

Functionally, releasing that inhibition activates B55-alpha toward WEE1 and reinforces the
G2/M checkpoint
[PMID:33108758 "Knockout of FAM122A results in activation of PP2A-B55α, a phosphatase that dephosphorylates the WEE1 protein and rescues WEE1 from ubiquitin-mediated degradation."],
and the B-subunit identity is what matters — knocking down B55-alpha (but not B56-alpha or
B56-gamma) reverses the FAM122A-knockout phenotype
[PMID:33108758 "demonstrating that B55α is the critical subunit of PP2A required for dephosphorylation of WEE1"].
This is the experimental basis of the `GO:0006470` IMP row and of the UniProt FUNCTION
statement about WEE1 and the G2/M checkpoint.

## Core function 3: substrate targeting outside mitosis (Tau and signalling substrates)

The reconstituted Tau assay plus the PP2A-Balpha holoenzyme crystal structure show that
B55-alpha is what makes PP2A a Tau phosphatase
[PMID:18922469 "We show that Balpha specifically and markedly facilitates dephosphorylation of the phosphorylated Tau in our reconstituted assay."],
with the acidic top-face groove as the Tau-binding site
[PMID:18922469 "the central groove on the top face of Bα is the likely binding site for Tau"].
This supports the `GO:0048156 tau protein binding` row despite its IEA/ortholog provenance.

The same adaptor logic recurs for individual signalling substrates, and these are the
`GO:0005515` rows that can be resolved to an informative MF rather than simply dropped:

- HSF1: [PMID:25816751 "The B55 subunits directly bind to HSF1."] and
  [PMID:25816751 "Expression of IER5 and B55 in cells leads to HSF1 dephosphorylation and activation of HSF1 target genes."]
- CRTC3: [PMID:30611118 "CRTC3 interacts with B55 PP2A holoenzymes via a conserved PP2A-binding region (amino acids 380-401)"],
  where S391 phosphorylation
  [PMID:30611118 "enables B55 PP2A holoenzyme recruitment and subsequent dephosphorylation of CRTC3 at 14-3-3 binding sites"]
- DAPK1: [PMID:20220139 "These findings further validate the in vivo specificity of the Bα and Bδ subunits in targeting PP2A to DAPK."]
- p107/RBL1: the NMR competition experiment in [PMID:38123684] places p107 on the B55 platform.

## Chromosome segregation

The mouse ortholog (Q6P1F6) carries IDA rows for `GO:0051983` and `GO:0140767` from
PMID:39003739 ("PP2A-B55 phosphatase counteracts Ki-67-dependent chromosome
individualization during mitosis"), which is also the source of UniProt's MKI67
by-similarity statement. Human-side support is independent and convergent: PP2A acts
non-catalytically to recruit condensin II and KIF4a to chromosomes
[PMID:19915589 "we found that the chromokinesin KIF4a is also targeted to chromosomes via the noncatalytic activity of PP2A"],
and B55-alpha depletion delays spindle breakdown and chromatin decondensation
[PMID:20711181 "We identify a trimeric PP2A-B55alpha complex as a key factor in mitotic spindle breakdown and postmitotic reassembly of the nuclear envelope, Golgi apparatus and decondensed chromatin."].
So the ISS/IEA `GO:0051983` rows are accepted rather than discounted as ortholog transfer.

## Grading decisions and their reasons

1. **`GO:0004721` IDA `contributes_to` (PMID:30595372) → MODIFY to `GO:0004722`.** The
   qualifier is already the weaker, correct claim; the essence is right but PP2A is
   specifically a Ser/Thr phosphatase, which is the term both repository modules use for
   this holoenzyme. Not a demotion of the annotation, a sharpening of it.
2. **43 bare `GO:0005515` IPI rows.** Repository policy: resolve to an informative MF where
   the cited paper supports one, otherwise REMOVE as uninformative without asserting the
   interaction is false. Four rows are resolved to `GO:0140767 enzyme-substrate adaptor
   activity` (HSF1, CRTC3, DAPK1, p107/RBL1 — each a paper that shows B55 binding *and*
   B55-directed dephosphorylation of that partner). The remaining rows are REMOVEd: the
   PPP2R1A/PPP2R1B/PPP2CA rows are holoenzyme assembly already captured by the `GO:0000159`
   part_of rows, and the rest are high-throughput interactome or inhibitor/regulator
   co-precipitations that carry no functional information about B55-alpha itself.
3. **`GO:0044877` protein-containing complex binding (IEA from rat P36876, PMID:11032905).**
   REMOVE — uninformative and redundant: the same rat experiment already yields the specific
   `GO:0048156 tau protein binding` row, which is what the assay actually measured.
4. **`GO:0051721` protein phosphatase 2A binding (IEA from rat).** MARK_AS_OVER_ANNOTATED.
   Binding the PP2A core dimer is real (the A-subunit mutagenesis of PMID:9847399 maps it),
   but B55-alpha *is* a PP2A subunit; annotating a constituent subunit as "binds PP2A"
   conflates complex membership (already asserted five times over via `GO:0000159`) with
   binding an external complex. Not false, so not REMOVE.
5. **Synapse / glutamatergic synapse (IEA from mouse Q6P1F6).** The mouse source is
   PMID:24413018, a fluorescence-sorted glutamatergic synaptosome proteomics screen. Presence
   in a synaptosome preparation is decent evidence of a synaptic pool, poor evidence of
   `is_active_in`. KEEP_AS_NON_CORE rather than REMOVE — B55-alpha is a ubiquitous subunit
   with real neuronal substrates (Tau, DARPP-32 via ARPP-16), but the synapse is not where
   its core function is defined.
6. **Reactome `TAS` cytosol rows.** All ACCEPTed on location grounds. Two (BANF1, ANKLE2)
   are explicitly B55-alpha-specific reactions; the NMD/UPF1 and YAP1 rows use "PP2A"
   generically, so the cytosolic location is right even though the reaction attribution to
   B55-alpha specifically is Reactome's inference rather than a B55-alpha experiment. The
   annotated term is the compartment, not the reaction, so this does not warrant a downgrade.
7. **PMID:17245430 rows.** The paper's headline is B56-gamma
   [PMID:17245430 "the specific B regulatory subunits of PP2A B56gamma1 and B56gamma3 mediate dephosphorylation of p53 at Thr55"],
   and B55-alpha appears in it as the comparator B subunit. Per repository rules this is NOT
   grounds to call the experimental rows mis-attributed: the curator read the full text, and
   B55-alpha's membership in a PP2A holoenzyme (the `GO:0000159` IDA) is independently
   established many times over. The TP53 `GO:0005515` row is REMOVEd on the generic-binding
   policy, not because the interaction is doubted.
8. **No `NEW` terms proposed, and no cell-cycle-transition term in `core_functions` either.** The obvious candidate would be a mitotic-exit process term
   (e.g. `GO:0010458 exit from mitosis`), and B55-alpha would pass the participation test
   — it is the subunit that performs substrate selection for the dephosphorylations that
   *constitute* mitotic exit, not merely a substrate of the process. But the comparator check
   argues against adding it here: the human catalytic and scaffold subunits (PPP2CA,
   PPP2R1A) do not carry `GO:0010458` either, and GOA's chosen representation for this
   holoenzyme's mitotic role is `GO:0051983 regulation of chromosome segregation` plus
   `GO:0006470`, both of which PPP2R2A already has. The mitotic-exit role is captured in
   `core_functions` and in the two repository modules rather than asserted as a new
   annotation.

   The comparator query is worth recording, because it also settled how `core_functions`
   should be phrased. QuickGO returns **zero** annotations to any of `GO:0010389 regulation of
   G2/M transition`, `GO:0000086 G2/M transition`, `GO:0010458 exit from mitosis` or
   `GO:0007096 regulation of exit from mitosis` for the catalytic subunit PPP2CA (P67775), the
   scaffold PPP2R1A (P30153) or PPP2R2A itself (P63151) — while MASTL (Q96GX5), the *kinase*
   that gates this holoenzyme, carries `GO:0000086` twice by IMP. So GO's convention is that
   the cell-cycle-transition terms go to the kinase/regulatory switch, and the phosphatase
   holoenzyme's contribution is represented by `GO:0006470 protein dephosphorylation` plus
   `GO:0051983 regulation of chromosome segregation`. That is a convention across all three
   subunits of the same complex, not an oversight on one gene, so `core_functions` follows it:
   the WEE1/G2/M-checkpoint role is stated in prose and in `review.reason` on the
   `GO:0006470` IMP row, not as a `directly_involved_in` term the holoenzyme's other subunits
   are all missing.

## Open questions carried into the review

- Which mitotic-exit substrates are B55-alpha-specific versus shared with B55-delta
  (PPP2R2D)? B55-delta depletion did *not* delay mitotic exit in HeLa cells even though it is
  the Xenopus-extract isoform, which the authors attribute to expression-level or technical
  differences [PMID:20711181].
- Is the `GO:0019888` "regulator activity" framing or the `GO:0140767` "adaptor" framing the
  better primary MF for a B subunit? They describe the same physical fact from two directions
  and GOA asserts both; the review accepts both and uses `GO:0140767` as the primary MF in
  `core_functions` because substrate selection is the mechanistically specific claim.
