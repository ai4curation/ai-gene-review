# ESR2 (estrogen receptor beta, ER-beta, NR3A2; UniProtKB:Q92731) — review notes

## What the protein is

Human ER-beta was cloned in 1996 as a second estrogen receptor, 96% identical to
ER-alpha across the DNA-binding domain and 58% across the ligand-binding domain, with
the A/B, hinge and F regions not conserved
[PMID:8769313 "A comparison of the amino acid sequence of ER beta with the 'classical' ER (ER alpha) shows a high degree of conservation of the DNA-binding domain (96%), and of the ligand-binding domain (58%)"].
The UniProt record keeps the canonical nuclear-receptor architecture: a modulating
N-terminal region, the two C4 zinc fingers of the DNA-binding domain (residues
149-214) and the C-terminal ligand-binding domain (264-498)
[file:human/ESR2/ESR2-uniprot.txt "DOMAIN: Composed of three domains: a modulating N-terminal domain, a DNA-binding domain and a C-terminal ligand-binding domain."].

## Ligand binding

ER-beta binds 17beta-estradiol with low-nanomolar affinity, measured side by side with
ER-alpha: Kd 0.6 nM for ER-beta against 0.2 nM for ER-alpha
[PMID:9671811 "the average dissociation constants ( K d) of ERalpha and ERbeta for 17beta-estradiol (E2) are 0.2 and 0.6 nM respectively, but ERbetacx has no ligand binding ability"].
Saturation binding on the rat protein gives the same picture (Kd 0.4 nM) together with
a competition series spanning estrone, estriol, phytoestrogens and antiestrogens
[PMID:9048584 "Saturation ligand binding analysis of in vitro synthesized human ER alpha and rat ER beta protein revealed a single binding component for 16 alpha-iodo-17 beta-estradiol with high affinity"].
The crystal structure of the ER-beta ligand-binding domain shows estradiol's partial
agonist genistein buried in the same hydrophobic pocket that the endogenous hormone
occupies, while raloxifene's side chain displaces helix 12
[PMID:10469641 "In contrast, genistein is completely buried within the hydrophobic core of the protein and binds in a manner similar to that observed for ER's endogenous hormone, 17beta-oestradiol"].
So the specific binding claim supported for this gene is estradiol binding, not steroid
binding in general.

## DNA binding, dimerization, and transcriptional output

ER-beta binds estrogen response elements and dimerizes. Gel-shift work compares it
directly with ER-alpha and shows heterodimer formation
[PMID:9325313 "We further report that ERalpha and beta can dimerize with each other, the DNA binding domain of hERalpha being sufficient for dimerization with hERbeta"];
the isoform survey shows DNA-binding homodimers as well
[PMID:9636657 "the isoforms were able to form DNA-binding homodimers and heterodimers with each other and with the ER alpha subtype"],
which is what UniProt records
[file:human/ESR2/ESR2-uniprot.txt "SUBUNIT: Binds DNA as a homodimer. Can form a heterodimer with ESR1."].
BRET in live cells separates ER-beta homodimers from ER-alpha/beta heterodimers and
shows ligands can favour one over the other
[PMID:19022902 "a bioactive component was found to induce ERbeta/beta homodimers, and ERalpha/beta heterodimers but had minimal activity on ERalpha/alpha homodimers"].

Transactivation of an ERE reporter by estradiol was demonstrated in the cloning paper
[PMID:8769313 "Transient transfections of an ER beta expression construct together with an ERE-based reporter construct in CHO cells clearly demonstrated transactivation of ER beta by 17 beta-estradiol"]
and UniProt summarizes the same activity
[file:human/ESR2/ESR2-uniprot.txt "FUNCTION: Nuclear hormone receptor. Binds estrogens with an affinity similar to that of ESR1/ER-alpha, and activates expression of reporter genes containing estrogen response elements (ERE) in an estrogen-dependent manner"].

The direction of the transcriptional effect is not fixed. On an AP-1 element estradiol
activates through ER-alpha and represses through ER-beta, and antiestrogens do the
reverse
[PMID:9278514 "with ERalpha, 17beta-estradiol activated transcription, whereas with ERbeta, 17beta-estradiol inhibited transcription"].
On the human CRH-BP promoter both receptors bind ERE half-sites in EMSA, yet estradiol
makes ER-alpha an activator and ER-beta a repressor
[PMID:15345745 "Three ERE half-sites in the CRH-BP promoter bound ERalpha and ERbeta in an EMSA"],
[PMID:15345745 "in the presence of estradiol ERalpha induced and ERbeta repressed promoter activity in a dose-dependent manner"].
This is why the undirected "regulation of transcription by RNA polymerase II" claim is
the honest family-level statement, with both the positive and the negative Pol II terms
supported in their own contexts.

## Coregulator recruitment, in chromatin

ER-beta recruits coactivators and corepressors, and the unusual point is that it binds
N-CoR/SMRT in the presence of agonists rather than in their absence, through an
LXXLL-like motif
[PMID:12904255 "we report that estrogen receptor beta (ERbeta) binds N-CoR and SMRT in the presence of agonists, but not antagonists, in vitro and in vivo"],
[PMID:12904255 "ERbeta recognizes a sequence (PLTIRML) in the N-CoR C-terminus that resembles coactivator LXXLL motifs"].
A coactivator case with chromatin-level evidence is CCDC62/ERAP75, which binds the
ER-beta ligand-binding domain, joins the ERE complex and is recruited to the cyclin D1
promoter in prostate cancer cells, where its knockdown suppresses ER-beta-mediated
transactivation
[PMID:19126643 "Both in vitro and in vivo interaction assays using mammalian two-hybrid, glutathione S-transferase pull-down and coimmunoprecipitation methods proved that ERbeta can interact with the C-terminus of CCDC62/ERAP75 via the ligand-binding domain"],
[PMID:19126643 "a chromatin immunoprecipitation assay demonstrated the hormone-dependent recruitment of CCDC62/ERAP75 within the promoter of the estrogen-responsive gene cyclin D1"].
Other partners reported with direct binding to ER-beta and a functional readout on its
transactivation: the TPR phosphatase PP5
[PMID:14764652 "showed that PP5 directly binds to both ERalpha and ERbeta via its tetratricopeptide repeat domain"],
DBC1/CCAR2
[PMID:20074560 "In vitro pull-down assays revealed a direct interaction between DBC1 amino-terminus and activation function-1/2 domain of ERbeta"],
the methyltransferase PRMT2
[PMID:12039952 "PRMT2 also binds to ERbeta, PR, TRbeta, RARalpha, PPARgamma, and RXRalpha in a ligand-independent manner"],
hMMS19
[PMID:11279242 "the human MMS19 also interacts with estrogen receptors in a ligand-independent manner but not with retinoic acid receptor or thyroid hormone receptor"],
the TrxR1 splice variant TrxR1b
[PMID:15199063 "In vitro interaction studies revealed direct interaction of the TrxR1b with the estrogen receptors alpha and beta"],
and the forkhead factor FOXO3a
[PMID:18312651 "We found that FOXO3a interacted with ER-alpha and ER-beta proteins and inhibited 17beta-estradiol (E2)-dependent, ER-regulated transcriptional activities"].
CTGF/CCN2, EGFR, BRCA1 and PLSCR1 are reported as interactors without any molecular
function following for ER-beta itself
[PMID:21629692 "CTGF interacted with ER DNA-binding domain"],
[PMID:21951318 "Coimmunoprecipitation experiments in these and other lung adenocarcinoma cells confirmed that ERbeta and EGFR interact in a gender-dependent manner and in response to E2 or EGF"].

## Where it acts, and the antibody problem

UniProt gives one location, the nucleus, with the two human interaction/localization
papers behind it
[file:human/ESR2/ESR2-uniprot.txt "SUBCELLULAR LOCATION: Nucleus"].
The strongest tissue-level statement available comes from the one anti-ER-beta antibody
that survives validation: of thirteen antibodies tested, only PPZ0506 is specific in
IHC, and with it ER-beta protein is nuclear in ovarian granulosa cells, testicular
Leydig cells, adrenal glandular cells and lymphoid cells, with no signal in breast
[PMID:28643774 "We conclude that only one antibody, the rarely used monoclonal PPZ0506, specifically targets ERbeta in immunohistochemistry"],
[PMID:28643774 "IHC revealed nuclear ERbeta expression in glandular cells of adrenal gland, granulosa cells in ovary, Leydig cells of the testis, and lymphocytes in secondary lymphoid organs"],
[PMID:28643774 "We do not find evidence of expression in normal or cancerous human breast."].
That paper is the reason to treat localization claims resting on the commonly used
clones (PPG5/10, 14C8) as unsupported rather than merely unreplicated.

The mitochondrial-ER-beta claim is the live case. It rests on immunocytochemistry with
two antibodies plus MALDI-TOF of a 50-65 kDa band from human heart mitochondria, and
the same paper reports no nuclear translocation on estradiol treatment
[PMID:15024130 "In immunocytochemistry studies, ERbeta was detected with two ERbeta antibodies and found to colocalize almost exclusively with a mitochondrial marker in rat primary neuron, primary cardiomyocyte, and a murine hippocampal cell line"],
[PMID:15024130 "No translocation of ERbeta into the nucleus on 17beta-estradiol treatment was seen by using immunocytochemistry"].
An independent attempt to reproduce the mass-spectrometric identification found that the
peptide masses matching ER-beta do not fragment as ER-beta peptides
[PMID:16563354 "However, fragmentation of these peptides shows that they are not from ERbeta"],
[PMID:16563354 "Our conclusion is that ERbeta cannot be identified by MALDI-TOF from a mixture of mitochondrial proteins resolved on SDS-PAGE"].
The original authors replied that their own heart-mitochondrial spectra are not the ones
reanalysed
[PMID:16707101 "our MALDI-TOF analysis using human heart mitochondrial protein has identified 7 and 8 sequences that could be potentially from ERbeta and ERbeta3, respectively"],
so the dispute is on the record; what is not on the record is any replication of
mitochondrial ER-beta with a validated reagent, and the companion claim of nuclear
exclusion is contradicted by the nuclear evidence above.

## Ovary: the best-supported physiology

Human loss of function. A heterozygous ESR2 mutation in a 16-year-old with absent
breast development, primary amenorrhoea and streak gonads behaves as a dominant negative
and fails to recruit NCOA1
[PMID:30113650 "We identified a loss-of-function heterozygous mutation of a highly conserved residue in ESR2 that disrupts estradiol-dependent signaling and has a dominant negative effect, most likely due to failure to interact with its coactivator, nuclear coactivator 1"],
[PMID:30113650 "suggesting that ESR2 is necessary for human ovarian determination and/or maintenance and that ESR1 is not sufficient to sustain ovarian function in humans"].
Separate ESR2 variants segregate with 46,XY differences of sex development, and the
DNA-binding-domain deletion and a ligand-binding-domain missense change increase
transactivation rather than abolishing it
[PMID:29261182 "Significantly increased transcriptional activation and an impact on protein conformation were shown for the p.(Asn181del) and p.(Leu426Arg) variants"].
Both sets of human variants are read out as changes in ER-beta's transcriptional
activity, which is what makes them evidence for the molecular function.

Mouse loss of function localizes the defect to the preovulatory follicle. Esr2-null
females are fertile but have fewer and smaller litters from reduced ovarian efficiency
[PMID:9861029 "Our results indicate that ERbeta is essential for normal ovulation efficiency but is not essential for female or male sexual differentiation, fertility, or lactation"].
Granulosa cells of those follicles respond incompletely to FSH, with less aromatase
activity and insufficient LH receptor, so an ovulatory gonadotropin bolus produces fewer
ruptures
[PMID:15831568 "Granulosa cells of ERbeta knockout (ERKO) preovulatory follicles exhibited an attenuated response to FSH-induced differentiation, as evident by reduced aromatase activity and estradiol synthesis, and insufficient expression of LH receptor"],
[PMID:15831568 "These studies demonstrate that ERbeta-mediated estradiol actions are vital to FSH-induced granulosa cell differentiation"].
Follicles cultured out of the ovary show the same block, and it is ER-beta-specific
rather than shared with ER-alpha
[PMID:15731357 "betaERKO follicles showed a significant lack of progression from early antral to large antral stage, decreased estradiol production, and reduced ovulation"],
[PMID:15731357 "these data indicate that ERbeta, but not ERalpha, plays a direct role in folliculogenesis"].
Downstream of that, ER-beta-null granulosa cells make about half as much cAMP
[PMID:19324971 "We observed a 50% reduction in cAMP levels in cultured ERbeta(-/-) granulosa cells exposed to LH compared with ERbeta(+/+) controls"].
Taken together with the one validated-antibody localization (nuclear ER-beta in human
granulosa cells), the granulosa cell is where the receptor's own transduction step
contributes to follicle maturation, which is why ovarian follicle development is
proposed here as a new annotation while granulosa cell differentiation, supported only
in mouse, is not.

## Growth restraint

The claim that ER-beta restrains estrogen-driven proliferation has a direct human
cell-line experiment behind it: induced ER-beta in T47D lowers estradiol-stimulated
proliferation with p27 up and cyclin E, Cdc25A and Skp2 down
[PMID:14745018 "induced expression of ERbeta in the breast cancer cell line T47D reduces 17beta-estradiol-stimulated proliferation when expression of ERbeta mRNA equals that of ERalpha"].
That is negative regulation of cell population proliferation, not of cell growth in the
GO sense of size increase, which is how the legacy NAS annotation is phrased.

## Isoform 2 (ER-beta-cx / ER-beta-2)

Isoform 2 is not a weaker receptor; it is a different activity. It has no ligand
binding, gives no ERE shift, does not transactivate, and preferentially heterodimerizes
with ER-alpha, inhibiting ER-alpha's DNA binding
[PMID:9671811 "ERalpha and ERbeta proteins bind to the estrogen response element, whereas ERbetacx does not form any shifted complex in gel shift assays"],
[PMID:9671811 "ERbetacx preferentially forms a heterodimer with ERalpha rather than that with ERbeta, inhibiting DNA binding by ERalpha"],
[PMID:9671811 "it shows a significant dominant negative activity only against ERalpha transactivation"],
and UniProt carries it as an isoform-scoped function
[file:human/ESR2/ESR2-uniprot.txt "Lacks ligand binding ability and has no or only very low ERE binding activity resulting in the loss of ligand-dependent transactivation ability."].
The five full-length isoforms all diverge inside predicted helix 10 of the
ligand-binding domain
[PMID:9636657 "All five isoforms diverge at a common position within the predicted helix 10 of the ligand binding domain of hER beta"],
which is why C-terminal variation changes ligand competence rather than DNA binding.
The GOA row annotating "receptor antagonist activity" from this paper describes isoform
2, and the mechanism is inhibition of another transcription regulator through
heterodimerization, not interference with agonist binding to a receptor.

## Retracted interaction

UniProt flags that the reported PELP1 interaction comes from a retracted paper
[file:human/ESR2/ESR2-uniprot.txt "CAUTION: Had previously been shown to interact with PELP1. However this paper was retracted as cell-based data was viewed as unreliable."].
No row in the current GOA set depends on it.
