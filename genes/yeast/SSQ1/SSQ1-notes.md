# SSQ1 review notes

## 2026-08-12 re-review

- Identity verified as *Saccharomyces cerevisiae* SSQ1/YLR369W, UniProt Q05931,
  the mitochondrial Ssq-type Hsp70 dedicated to iron-sulfur cluster biogenesis.
- The existing Falcon report is correctly scoped to Q05931. An OpenScientist
  run was launched through `just deep-research-openscientist yeast SSQ1`; after
  extended silent polling without a returned artifact it was interrupted. No
  unreturned result was treated as evidence.
- Core mechanism: Jac1 recruits the Isu scaffold and stimulates the Ssq1 ATPase
  cycle; Mge1 promotes nucleotide exchange; Ssq1 recognizes the Isu LPPVK motif
  and drives release/handoff of the newly assembled cluster to Grx5.
- UniProt resolves the GOA IntAct partners directly: Q03020 is the physiological
  Isu1 scaffold client, whereas P15646 is the nucleolar protein Nop1. The Isu1
  rows are biologically relevant but poorly expressed by bare protein binding;
  the Nop1 rows are likely high-throughput background for a matrix protein.
- Generic family terms were narrowed where a more informative child exists:
  GO:0044183 and GO:0051082 are modified to GO:0140662, generic nucleotide and
  hydrolase parents are over-annotated, and mitochondrial matrix is the core
  location rather than its broad organelle/lumen parents.
- GO:0042026 protein refolding is an unsafe general-Hsp70 IBA transfer. Ssq1 is
  specialized for the Isu client and ISC transfer rather than broad stress
  refolding; the propagation audit records this functional divergence.
- The cytoplasm IBA is ontologically true because mitochondria are part of the
  GO cytoplasm, but it is marked over-annotated because matrix is the precise
  functional compartment. Intracellular iron homeostasis is retained as a
  genuine downstream phenotype, not a core direct function.

## 2026-08-28 completion audit

- Reconciled all 29 GOA rows by the exact machine signature (GO term, evidence
  code, reference, and qualifier); `just validate-goa yeast SSQ1` passes and no
  review remains `PENDING`.
- Audited all seven IBA rows against the current GOA `WITH/FROM` field and
  `interpro/panther/PTHR19375/PTHR19375-paint.tsv`. The actual PAINT nodes are
  PTN002321897 for cytoplasm, PTN000452554 for mitochondrion and iron-sulfur
  cluster assembly, and PTN000452648 for ATP hydrolysis, heat-shock-protein
  binding, protein-folding chaperone, and protein refolding. SSQ1 appearing
  among the experimental descendants for conserved ATPase/ISC assertions is
  expected phylogenetic grounding, not circularity.
- The core ATPase and ISC-transfer calls have direct target evidence. Jac1 and
  Isu1 stimulate Ssq1 ATPase [PMID:12756240, "Jac1 and Isu1 cooperatively
  stimulate the ATPase activity of Ssq1."], and a ferredoxin maturation assay
  established a mitochondrial Fe-S assembly requirement [PMID:11273703,
  "Ssq1 was demonstrated to be required for the FeS cluster assembly in
  mitochondria."].
- GO:0051082 is retained only as the imported legacy row and changed to
  `MODIFY` because the term is obsolete, not because the experiment is weak:
  Ssq1 directly showed ATP-regulated binding to unfolded substrates
  [PMID:11601843, "Ssq1 showed typical chaperone properties by binding to
  unfolded substrate proteins in an ATP-regulated manner."]. GO:0140662 is the
  proposed replacement already used in the core-function synthesis.
- Live-ontology recheck on 2026-08-28 confirmed this obsoletion in the official
  EBI OLS GO record (`is_obsolete: true`, label `obsolete unfolded protein
  binding`, with `consider` GO:0044183 and GO:0140309). The repository cache row
  that still says `False` is timestamped 2026-03-21, and the SSQ1 GOA/UniProt
  snapshots are dated 2026-01; all predate closure of the official GO obsoletion
  request on 2026-05-29 (geneontology/go-ontology#30962). They are stale evidence
  for current term status, not a contradiction of the live ontology.
- GO:0042026 remains marked as an over-propagated general-Hsp70 process rather
  than removed. The available literature establishes specialized ISC client
  handling but does not provide a target-specific refolding assay; this avoids
  claiming loss of all refolding capacity from incomplete evidence.
- The five protein-binding IPI rows were retained as over-annotated rather than
  removed. Isu1 is the physiological client, while the Nop1 rows are
  compartmentally discordant high-throughput observations; bare protein binding
  is uninformative in either case.
- Final curation state: 9 `ACCEPT`, 8 `KEEP_AS_NON_CORE`, 10
  `MARK_AS_OVER_ANNOTATED`, 2 `MODIFY`, 0 `PENDING`; status set to `COMPLETE`.

## 2026-09-21 full-source re-review

All 29 original assertions were read and preserved in their original order, including term/evidence/reference/qualifier fields; no NEW rows were added. Source comparison and actual PAINT lineage are saved in the IBA re-review subfolder. Correct parent annotations for cytoplasm, mitochondrion, intracellular organelle lumen, ATP/nucleotide binding and hydrolase activity are core: precision of the matrix/ATPase children is not a biological reason to reject their parents.

The actual PTHR19375 treeinfo root-to-Q05931 path terminates at PTN000452606. It passes through PTN000452648 (ATPase, chaperone binding, folding and refolding), PTN002321897 (cytoplasm) and PTN000452554 (mitochondrion and ISC). Literal cached IBD assertions were inspected; there is no NOT/IRD on this path. The presence of SGD:S000004361 among descendant evidence is target experimental grounding, not circularity. Partner specificity makes the folding question substantive but does not by itself demonstrate ancestral-function loss.

Primary biochemical distinctions:

- [PMID:12756240](https://pubmed.ncbi.nlm.nih.gov/12756240/), full [author PDF](https://craiglab.biochem.wisc.edu/wp-content/uploads/sites/1625/2021/05/2003_Dutkiewicz_JBC.pdf): purified yeast Ssq1, ATP/ADP single-turnover and steady-state assays; Isu client engagement by SPR and glycerol gradients; Mge1 nucleotide release. Figure 8 states “Mdj1 cannot replace Jac1 in stimulation of steady-state ATPase of Ssq1.” This is a partner-specific negative, not a universal refolding assay. Figure 3 shows Jac1 does not remain in the stable Ssq1–Isu1 complex. Mature Yfh1/Nfu1 lack stimulation, but precursor or partially folded Yfh1 is explicitly left possible.
- [PMID:16431909](https://pubmed.ncbi.nlm.nih.gov/16431909/), full [author PDF](https://craiglab.biochem.wisc.edu/wp-content/uploads/sites/1625/2021/05/2006_Dutkiewicz_JBC.pdf): Figure 4C measures bovine rhodanese aggregation after guanidine denaturation and dilution, by light scattering at 500 nm over 15 min. Ssq1 suppresses aggregation, more efficiently without nucleotide or with ADP than with ATP. This establishes a biochemical capacity beyond native Isu recognition, but not rhodanese enzyme reactivation. Figure 4A/B's ATP/Jac1-independent increase in purified Nfs1 desulfurase activity is interpreted as protection against unfolding; Figure 4D shows unchanged Nfs1 activity in Ssq1-depleted mitochondrial lysates, limiting the physiological Nfs1 claim specifically. Figures 5/6 separate Isu cluster formation from subsequent transfer.
- [PMID:11601843](https://pubmed.ncbi.nlm.nih.gov/11601843/): abstract “binding to unfolded substrate proteins in an ATP-regulated manner.” Full text remained unavailable after publisher/author searches. This positive binding finding must not be discarded, but does not alone identify a current folding/holdase replacement for obsolete GO:0051082.
- [PMID:23615440](https://pubmed.ncbi.nlm.nih.gov/23615440/): full relevant Methods/Results and transfer model read. Grx5–Ssq1 interaction occurs at a site distinct from Isu's LPPVK site. Figure 3D also observes recombinant Cia1 binding displaced by LPPVK. Calling that interaction folding in the discussion does not measure folding outcome. The Figure 6 handoff sequence is a supported working model, not a direct observation of every step or a measured obligatory 1:1:1 Jac1-containing assembly. The paper's bacterial “orthologue” wording describes a functional analogy: Ssq1 arose from mitochondrial-Hsp70 duplication.
- [PMID:20224575](https://pubmed.ncbi.nlm.nih.gov/20224575/): full coevolution study supports changes in Jac1 partnership using complementation and ATPase assays. Its introductory claim of lost folding is inferred from partner specificity. This is stronger context than donor counting, but not direct negative refolding on all substrates.
- [PMID:10779357](https://pubmed.ncbi.nlm.nih.gov/10779357/): full Results/Discussion show Yfh1 processing delay but about 75% mature Yfh1 retained. The authors report “no differences were observed” in aggregation/protease-sensitivity comparisons of Yfh1 in mutant versus wild-type mitochondria, and no rescue by simply increasing mature Yfh1. They propose, rather than show, cleavage-site exposure by Ssq1. Twofold Ssc1 overexpression yields partial rescue; the approximately 2000-fold comparison is relative to baseline Ssq1 abundance. Falcon's suggestion of full rescue requiring 1000–2000-fold Ssc1 overexpression conflates those quantities and is marked DISPUTED.

The core synthesis now uses directly measured ATP hydrolysis with Fe-S assembly and matrix location. Folding, refolding and the obsolete unfolded-binding replacement remain UNDECIDED pending focused assessment. The clear antiaggregation capacity is retained in the standalone biological description and evidence; no folding loss or artificial new folding annotation is manufactured. Initial Fe-S chemistry is performed by other ISC proteins, while Ssq1 performs engagement/remodeling/handoff work, so the process annotation is appropriate.

Nop1 and Isu source review:

[PMID:19536198](https://pubmed.ncbi.nlm.nih.gov/19536198/) full methods use whole-cell TAP-MS and spoke assignment. Exact original `msb200926-s8.xls` was obtained via EuropePMC supplementaryFiles; SHA256 and extracted cells are saved in `SSQ1-Nop1-supplement-check.json`. TableS1 row39 maps Ssq1 to YLR369W. TableS2 AI7 is Ssq1, AI44 is `Nop1,b`, and row6 defines `b: bait; p: prey`: Ssq1 was associated with a Nop1 bait. The column lists97 nonchaperone and5 chaperone partners. Thus the pair is verified source evidence, though binary interaction, native colocalization and client-folding function are unresolved. The paper shares a data/methods lineage with PMID:16554755; two citations are not proven independent experiments. Both Nop1 rows are UNDECIDED rather than alleged background from compartment mismatch. No nuclear annotation is proposed.

The three generic protein-binding rows for Isu are removed as uninformative labels under the annotation-reviewer policy, without rejecting the interactions. Full PMID:12756240 establishes native client binding; indexed full PMID:12947415 Results explicitly include Ssq1 in Isu1-GST purification and competition despite the frataxin-focused title. The PMID:37968396 full methods establish GFP pull-down/MS association; its exact Isu/Ssq1 score was not separately recovered. The mechanistic interactions remain in references, notes, description and core prose. A specific folding replacement is deferred rather than inferred from binding alone.

Other source-specific limits were kept explicit:11171977 abstract actually tests ssq1 as well as jac1 with iron normalization;11273703 verifies apo-to-holoferredoxin conversion;8707841 uses the historical SSH1 name for this Hsp70;9813017 explicitly includesSSQ1 despite its SOD1-centered title. The PMID:16823961/24769239 proteomics abstracts and standing curated annotations agree with independently demonstrated target matrix residence; their exact target peptide entries were not rechecked. No experimental annotation was rejected merely because its full text was inaccessible.

Exact OpenScientist query-cache check across935 records returned no SSQ1/Q05931/YLR369W/Ssc2p match. The local Falcon body, table and prior notes were read; the older aborted whole-gene OS attempt produced no local report. One neutral focused question, `folding-refolding-and-secondary-client-interactions`, was registered and runner session11110 launched. It was waiting for the global submission slot at initial inspection; no report was available or adopted. Current GO definitions/obsolescence were obtained from live QuickGO and saved. Report incorporation remains required.


## Recovery PR follow-up (2026-09-22)

Restored readable GO/PMID/PTN identifiers in curation prose. For DCV1, core
localization cites the recorded UniProt topology and SGD-attributed observation;
the unrelated Rim101 report sentence no longer supports plasma-membrane location.
For YAR1, unanswered report questions are not positive evidence. For SSQ1, the
located Nop1 association remains recorded while its generic binding label is removed.
The annotation changes apply only to the relevant gene; no inherited location is
rejected solely from its best-characterized compartment.
