# SkpA (Skp1 ortholog) review notes

Accession: O77430. Module: dmel_scf_slimb_ubiquitin_ligase (SkpA adaptor part).

## Literature journal

- SCF assembly in flies: [PMID:11500045 "We show that putative Drosophila SCF core subunits dSkpA and dRbx1 both interact directly with dCu11 and the F-box protein Slmb."]; neuronal SCF(Slimb) [PMID:24068890 "The SCF E3 ligase consists of four core components Cullin1/Roc1a/SkpA/Slimb"].
- F-box partners: Fsd [PMID:21170036 "Fsd is an F-box protein that directly interacts with both Skp1 and Bcd"]; Rca1 [PMID:17099689 "Rca1/Emi proteins contain a conserved F-box and interact with components of the Skp-Cullin-F-box (SCF) complex."]; Slmb in all three Y2H screens [PMID:16603075 "The map also shows that one interaction (SkpA-Slmb) was detected in all three two-hybrid screens."].
- Null phenotypes: [PMID:12730292 "Lethal skpA null mutants exhibit dramatic centrosome overduplication and additional defects in chromatin condensation, cell cycle progression and endoreduplication."]
- IMD repression [PMID:12401167]; apoptosis/DIAP1 [PMID:23979704 "we show that the loss of skpA function activates the intrinsic pathway of apoptosis and down-regulates the levels of expression of the anti-apoptotic DIAP1 protein"]; synaptic growth/JNK with Highwire [PMID:24948796 "Hence, SkpA is a novel negative regulator of the Wnd-Jnk pathway"]; synaptonemal complex [PMID:33382409].

## Decisions

- Core MF: GO:0160072 ubiquitin ligase complex scaffold activity (own, IPI-supported bridging), contributing to GO:0061630 of the SCF; GO:0019005 complex. Same pattern as Cul1 and the CRL2 adaptors (EloB/EloC).
- Protein binding (16 rows): partners are F-box proteins (Fsn, FBXO3/CG9003, Rca1, Ntc, Slmb) -> MODIFY to GO:1990444 F-box domain binding; Cul1 partner -> GO:0097602 cullin family protein binding; Minus (not an F-box protein) -> REMOVE.
- GO:0051298 centrosome duplication -> MODIFY to GO:0010826 negative regulation of centrosome duplication (null overduplicates).
- Generic parents (GO:0006511, GO:0016567) and positive-regulation-of-catabolism rows kept as non-core per batch convention; pathway outputs (Wnt, Hippo, IMD, JNK, apoptosis) non-core on the shared core subunit.

## Deep research

falcon deep research launched; status recorded in the commit history.

## Revision (batch rule change)

Correct-but-general terms are now MODIFY: GO:0016567 -> GO:0000209 protein polyubiquitination; GO:0006511 -> GO:0031146. Supersedes the generic-parent convention above.
