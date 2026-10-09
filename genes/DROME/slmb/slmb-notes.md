# slmb (Supernumerary limbs; beta-TrCP ortholog) review notes

Accession: A0A0B4KHK1 (Supernumerary limbs, isoform B; the FlyBase canonical entry carrying GOA rows).
Module: dmel_scf_slimb_ubiquitin_ligase (substrate-receptor part).

## Literature journal

- SCF assembly: Slimb binds the fly SCF core in vitro [PMID:11500045 "We show that putative Drosophila SCF core subunits dSkpA and dRbx1 both interact directly with dCu11 and the F-box protein Slmb."]; SCF(Slimb) in neurons is "Cullin1/Roc1a/SkpA/Slimb" [PMID:24068890 "The SCF E3 ligase consists of four core components Cullin1/Roc1a/SkpA/Slimb"].
- Phosphodegron recognition: [PMID:16326393 "CKI phosphorylation of Ci confers binding to the F-box protein Slimb/beta-TRCP, the substrate recognition component of the SCF(Slimb/beta-TRCP) ubiquitin ligase required for Ci processing."]; [PMID:16386907 "we conclude that Slimb binds directly to phosphorylated Ci-155 to initiate processing to Ci-75"].
- Hh and Wg: [PMID:9461217 "Loss of function of slimb results in a cell-autonomous accumulation of high levels of both Ci and Arm, and the ectopic expression of both Hh- and Wg- responsive genes."]. K11 chains on Ci: [PMID:23747190 "We demonstrate that Cul1-Slimb-based E3 ligase, but not Cul3-Rdx-based E3 ligase, modifies Ci by efficient addition of K11-linked ubiquitin chains."].
- Arm destruction in S2 cells: [PMID:22359584 "in these cells the only F-box protein playing a detectable role is Slimb"].
- Centrioles: [PMID:19171756 "the SCF E3 ubiquitin ligase in complex with the F-box protein Slimb mediates proteolytic degradation of the centrosomal regulatory kinase Plk4"] -> negative regulation of centriole reduplication (MODIFY GO:0046599 -> GO:0046600).
- Other substrates/outputs: Cactus/Toll [PMID:24086459 "the fly βTrCP protein Slimb is required in cultured cells to mediate Cactus degradation"]; Per/Tim clock [PMID:12432393]; Expanded [PMID:24778256, PMID:25522691, PMID:31567070]; Kibra [PMID:33555257]; aPKC/Par-6 polarity [PMID:25053431, PMID:25053432]; Cap-H2 [PMID:23530065]; Gcm [PMID:19346490]; Akt in dendrite pruning [PMID:24068890]; oogenesis [PMID:15857915]; synaptonemal complex [PMID:33382409].

## Decisions

- Core MF: GO:1990756 ubiquitin-like ligase-substrate adaptor activity (own activity), contributing to the SCF's GO:0061630 ubiquitin protein ligase activity. Complex GO:0019005.
- Batch convention (shared with SkpA, Cul1, Roc1a, and the CRL2 genes): GO:0016567 protein ubiquitination and GO:0006508 proteolysis are KEEP_AS_NON_CORE as generic parents; positive regulation of proteasomal catabolism terms are KEEP_AS_NON_CORE (the ligase executes rather than regulates degradation; direct term GO:0031146).
- For slmb only, negative regulation of Hh and canonical Wnt signaling are ACCEPTed as its defining physiological roles; the same terms are non-core on the shared core subunits.
- GO:0045849 negative regulation of nurse cell apoptotic process: UNDECIDED (abstract silent; full text not cached).

## Deep research

falcon deep research was launched; see commit history for whether a file was added.

## Revision (batch rule change)

Correct-but-general terms are now MODIFY to the more specific term rather than KEEP_AS_NON_CORE: GO:0016567 -> GO:0000209 protein polyubiquitination; GO:0006508 proteolysis -> GO:0031146. This supersedes the generic-parent convention noted above.

## Deep research (falcon, added after the initial review)

The falcon deep-research run finished after the initial commit and is now in `slmb-deep-research-falcon.md`. Its synthesis is consistent with the annotation decisions above; no review actions were changed.
