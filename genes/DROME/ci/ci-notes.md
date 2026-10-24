# cubitus interruptus (ci, Drosophila melanogaster, UniProt P19538) — curation journal

## Why this gene is unusual

Ci is the only Gli-family zinc-finger transcription factor in the fly, and it is the only known
transcriptional output of Smoothened signalling. Cells that lack Ci but have maximal pathway
activation (patched removed) show no Hedgehog output at all
[PMID:11171398, "The analysis of target gene expression and morphogenetic read-outs of Hh in embryonic, larval and adult stages indicates that Ci is absolutely required for all examined aspects of Hh outputs."].
That fact structures the whole review: nearly everything downstream of Hedgehog in the fly is
downstream of Ci, so the hard part of the curation is separating what Ci *does* from what happens
*because of* what Ci does.

The second structural fact is that one gene produces two proteins with opposite outputs. UniProt
records both explicitly, as two CHAIN features on P19538: `PRO_0000046917` (Transcriptional
activator cubitus interruptus, residues 1..1397) and `PRO_0000406217` (Transcriptional repressor
cubitus interruptus, residues 1..?). The repressor chain has an undefined C-terminal boundary —
worth noting, because the processing site has still not been mapped to a residue.

## The two forms

**Ci-75, the repressor (default state).** In the absence of Hedgehog, Ci-155 is phosphorylated on
clustered, successively primed sites by PKA, GSK3 and CK1, all of which are physically recruited by
Costal-2
[PMID:15691767, "We propose that Cos2 recruits multiple kinases to efficiently phosphorylate Ci and that Hh inhibits Ci phosphorylation by specifically interfering with kinase recruitment."].
The phosphorylated sites form an atypical extended binding site for Slimb
[PMID:17925225, "Here we show that multiple successively phosphorylated CK1 sites on Ci create an atypical extended binding site for the SCF substrate recognition component Slimb."],
and Slimb binding is what commits Ci to partial proteolysis
[PMID:16386907, "the sole Drosophila Gli homolog, Cubitus interruptus (Ci), undergoes partial proteolysis to Ci-75, which represses key Hh target genes"].
The truncated product loses the cytoplasmic tethering domain, enters the nucleus and represses
[PMID:9215627, "This form translocates to the nucleus where it represses hh and other target genes."].
Cleavage is not incidental — it is required for limb patterning in vivo
[PMID:10102270, "A repressor form of Ci arises in the absence of Hh signaling by proteolytic cleavage of intact Ci."].

**Ci-155, the activator.** Hedgehog blocks processing, and activation is a *separate* regulatory
step, not just the absence of cleavage
[PMID:10102270, "We provide evidence for the existence of a distinct activator form of Ci, which does not arise by mere prevention of Ci proteolysis, but rather depends on a separate regulatory step subject to Hh control."].
Activation involves Fused-mediated phosphorylation
[PMID:31279575, "we demonstrate that Hh stimulates the phosphorylation of Ci by the Ser/Thr kinase Fused (Fu) and that Fu-mediated phosphorylation of Ci promotes its activation."],
which is graded with ligand dose
[PMID:36271509, "we show that graded Hh induces a progressive increase in Ci phosphorylation at multiple Fused (Fu)/CK1 sites including a cluster located in the C-terminal Sufu-binding domain."],
and, in the most recent mechanistic account, proceeds through Fused condensates that allosterically
expose Ci
[PMID:39792672, "Within the condensates, Fu/Ulk3 undergoes a conformational change to expose Ci/Gli for Fu/Ulk3-mediated phosphorylation and activation, leading to gradual accumulation of nuclear CiA/GliA transcriptional complexes in proportion to ligand dose and exposure time."].
Nuclear entry uses two signals, a bipartite NLS
[PMID:10529426, "We first characterize a bipartite nuclear localization signal (NLS) within Ci."]
and a PY-NLS read by Transportin
[PMID:24413177, "We demonstrate that the PY-NLS functions in parallel with a previously identified bipartite NLS to promote nuclear localization and activity of full-length Ci."].
Activation requires the coactivator dCBP/nejire
[PMID:10669739, "Taken together, our data suggest that dCBP function is necessary for ci-mediated transactivation of wg during Drosophila embryogenesis."].

**Shared DNA binding.** Both forms keep the five C2H2 fingers and read the same GLI consensus
[PMID:9122207, "We show that Ci is a sequence-specific DNA binding protein that drives transcription from the wg promoter in transiently transfected cells."],
[PMID:8769644, "we identify sequences in the promoter region of the ptc gene, a primary target of Hh signaling, that are identical to the consensus-binding sequence of the GLI protein"].
Genome-wide occupancy has been mapped
[PMID:20978080, "We mapped chromatin binding sites for Cubitus interruptus (Ci), the transcription factor that mediates outputs of Hh signal transduction"].

## The PAINT node question (PTHR45718)

The family review flags node **PTN001836086** as the PAINT assertion of `GO:0007224 smoothened
signaling pathway` for PTHR45718. I checked `interpro/panther/PTHR45718/PTHR45718-paint.tsv`
directly. Two things follow.

1. **No ci annotation descends from PTN001836086.** That node is stamped `taxon:33511`
   (Deuterostomia) and its seeds are the mouse and human GLI paralogs, zebrafish gli genes and
   `UniProtKB:A0A8J1LVR3`. Drosophila is a protostome, so ci is outside the clade the IBD covers,
   and — consistent with that — ci's GOA record contains **no IBA row for GO:0007224 at all**.
   The four IBAs ci does carry (`GO:0000978`, `GO:0000981`, `GO:0005634`, `GO:0006357`) all descend
   from **PTN000456649**, a `taxon:33213` (Bilateria) node, which ci is properly inside. So there
   was nothing here to judge on donor identity: the node placement itself keeps the vertebrate
   pathway assertion away from the fly.

2. **The fly evidence independently, and overwhelmingly, supports the claim the node makes.**
   ci carries 28 direct GO:0007224 rows — 11 IDA, 5 IGI, 10 IMP, 1 IEP, 1 NAS — from the literature
   in which the pathway was discovered. If anything the node is placed conservatively: Ci is the
   founding member of the family and the protein that defined what "Hedgehog effector" means, so a
   bilaterian placement (matching PTN000456649) would be defensible on the biology. I have not
   proposed that change — re-pointing a PAINT node is an evolutionary judgement, and the repo rules
   are explicit that it should not be done mechanically — but I note it here as the one thing a
   PAINT curator might want to look at.

Note also that PTN000456649's seed lists for `GO:0000981`, `GO:0005634` and `GO:0006357` include
`FB:FBgn0004859`, i.e. ci itself. That is expected and correct: ci's own experimental annotations
are among the descendant evidences used to place the IBD, so ci legitimately appears in the
WITH/FROM of the IBAs it later receives. Marked `SUPPORTS_TRANSFER`, not circular.

## Decisions worth recording

**Core vs non-core.** Transcriptional activation, transcriptional repression, sequence-specific
Pol II cis-regulatory DNA binding, the smoothened signaling pathway, nucleus, cytosol and the
Hedgehog signalling complex are ACCEPTed as core. Every organ-level patterning outcome — segment
polarity, wing and genital disc A/P patterning, compound eye and spiracle morphogenesis, labial
disc development, cuticle pattern, heart development, dendrite morphogenesis, hindgut epithelial
differentiation, the cell-cycle terms, mucosal immunity — is KEEP_AS_NON_CORE. These are all real
and well-evidenced; they are simply the consequences of Ci switching target enhancers on and off,
not things Ci does.

**The one MARK_AS_OVER_ANNOTATED.** `GO:0035224 genital disc anterior/posterior pattern formation`
rests on IEP evidence from a descriptive survey that used ci as an anterior-compartment marker
[PMID:8798147, "cubitus interrupts (ci) localized the anterior compartments for each segment"].
The paper shows where ci protein is, not that ci function is required. Involvement is likely given
that Ci is the sole Hedgehog effector, so the term is probably not wrong — hence
MARK_AS_OVER_ANNOTATED rather than REMOVE.

**Protein binding (22 rows).** Per the repo policy, none of these are ACCEPTed or marked
over-annotated. Seventeen are REMOVEd as uninformative (removal is not a claim the interaction is
false — the Cos2, Fu and Su(fu) interactions are among the best-documented in the pathway, and
their functional content is already carried by `GO:0035301`). Five are MODIFIed where the cited
paper supports a specific molecular function:

- Slimb (PMID:16326393) and Roadkill/HIB (PMID:16740475, PMID:19955409 ×2) → `GO:0031625 ubiquitin
  protein ligase binding`. Both partners are substrate-recognition subunits of cullin-RING ligases
  [PMID:16740475, "HIB forms a complex with Cul3, a scaffold for modular ubiquitin ligases, and promotes Ci ubiquitination and degradation through Cul3."].
- dCBP/nejire (PMID:9109493 ×2) → `GO:0001223 transcription coactivator binding`
  [PMID:9109493, "Here we show that Drosophila CBP (dCBP) functions as a coactivator of Ci"].

**GO:0008140 is a term-scoping problem, not a wrong interaction.** The existing IPI row annotates
the Ci–nejire interaction to `cAMP response element binding protein binding`, whose definition
(checked against OLS) is *binding to a CREB protein*. Nejire is CREB-**binding** protein, a
coactivator, not CREB. MODIFY to `GO:0001223`, consistent with the two dCBP protein-binding rows
above. The interaction itself is solid
[PMID:25941387, "We also find that binding of Sufu to SIC and the middle region of Ci can impede recruitment of the transcriptional coactivator CBP by masking its binding site in the C-terminal region of Ci."].

**Generalisation MODIFYs.** `GO:0003677 DNA binding` (NAS) and `GO:0043565 sequence-specific DNA
binding` (IDA) → `GO:0000978`; `GO:0006355 regulation of DNA-templated transcription` (NAS) →
`GO:0006357`; `GO:0032991 protein-containing complex` (IPI) → `GO:0035301`, since the complex being
described is precisely the Hedgehog signalling complex
[PMID:9601642, "we show that Su(fu), Ci and Fu can interact directly to form a trimolecular complex, with Su(fu) binding to both its partners simultaneously."].

**The one REMOVE outside protein binding.** `GO:0140297 DNA-binding transcription factor binding`
(IEA, ARBA). Going through the characterised partner list — Cos2 (kinesin-related), Fu (kinase),
Su(fu), Slimb and Rdx (E3 substrate receptors), nejire and Taiman (coactivators), Hyrax (PAF1
subunit), Rbfox1 (RNA-binding) — none is a DNA-binding transcription factor. The only such partner
of Ci is Ci, and that is already stated precisely by `GO:0042803 protein homodimerization activity`
[PMID:19955409, "We provide evidence that both HIB and Ci form dimers/oligomers and engage in multivalent interactions"].

**Two rows I could not inspect but did not overrule.** PMID:20403347 supports both a `GO:0000977`
IDA and a `GO:0001228` IMP for ci, but the cached record is abstract-only and centres on Opa, a
Zic-family paralogue in the same PANTHER family. Per the repo rule, a title/abstract about a
paralogue is not grounds to overrule an experimental annotation whose full text the FlyBase curator
read; dpp is a canonical Ci target and both terms are independently established for ci
(PMID:9122207, PMID:10669739). ACCEPTed, with the limitation stated in the review reason. Similarly
PMID:8660881 (heart development) is an abstract about the wingless pathway in which hedgehog is
shown to act upstream; kept, but as non-core.

**Moonlighting.** Ci binds Hippo directly and competes with Warts for it in ovarian escort cells
[PMID:26403189, "Mechanistically, we found that Ci competitively interacts with Hpo and impairs the Hpo-Wts signaling complex formation, thereby promoting Yki nuclear localization."].
`GO:0019901 protein kinase binding` and `GO:0035331 negative regulation of hippo signaling` are
both kept as non-core: specific and well-evidenced, but a tissue-restricted side branch that does
not run through DNA binding.

## The one NEW annotation: GO:0001227

GOA records Ci's repressor output only as a biological process (`GO:0000122`, five rows) and as the
*unsigned* parent molecular function (`GO:0000981`), while the signed activator function
`GO:0001228` is present. The signed repressor function is simply absent.

- *Participation.* Ci itself does the repressing. The cleaved form goes to the nucleus and represses
  hedgehog and other targets [PMID:9215627]. No other gene product performs that step.
- *Comparator check.* I queried QuickGO: mouse Gli3 (`UniProtKB:Q61602`) carries `GO:0001227` (ISO,
  WITH `UniProtKB:P10071`), i.e. the term *is* applied to the repressor-forming Ci/GLI paralogue,
  and `GO:0001227` has 82 Drosophila gene products annotated to it. The absence on ci is a gap, not
  a convention. Human GLI3 does not currently carry it, which is itself worth a curator's attention.
- *Redundancy.* `GO:0001227` is a child of `GO:0000981`, which ci already has. But GOA already pairs
  `GO:0000981` with the sibling `GO:0001228` on this same protein, so adding the repressor leg
  completes the activator/repressor pair rather than merely refining an existing assertion. This is
  also exactly how `modules/hedgehog_signaling.yaml` models it — ci is a representative member of
  both the repressor annoton (`GO:0001227`) and the activator annoton (`GO:0001228`).

Proposed with IDA evidence anchored on PMID:9215627.

## Loose ends for an expert

Recorded in `suggested_questions`: the unmapped processing site (and hence the undefined C-terminus
of UniProt's `PRO_0000406217`); whether Ci-75 needs a dedicated corepressor or represses by
occupancy alone; which form carries the Hippo-antagonising activity; and the genome-wide split
between targets controlled by loss of repressor versus gain of activator.
