---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ADA
affinage_run_date: 2026-06-09T22:02:40
uniprot_accession: P00813
self_evaluation_pairwise: loss
faith_pct: 100.0
n_discoveries: 30
citation_count: 30
gates_passed: False
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for ADA (human)

> ⚠️ **CAUTION — trust gate(s) tripped; review before using:**
>
> - Affinage's own head-to-head self-evaluation scored this record `pairwise = loss` (not `win`) vs the curated UniProt reference — treat the narrative with extra scepticism.
>
> - Possible symbol collision: the narrative's opening names a non-human context ("e. coli") despite a human record — verify the narrative describes human ADA and not a same-symbol protein (cf. the ADA case).

## Current model (mechanistic narrative)

The ADA symbol in this corpus resolves into three biologically distinct proteins, and the timeline is dominated by the bacterial Ada DNA-alkylation-repair regulator rather than the human adenosine deaminase. The E. coli Ada protein is a bifunctional suicide methyltransferase that, in its repair role, irreversibly transfers methyl groups from O6-methylguanine in alkylated DNA to its own cysteine residues [PMID:2987251], with the active-site cysteine buried in the 19-kDa C-terminal domain whose structure has been solved [PMID:8156986]. A second methyltransferase activity in the N-terminal domain accepts methyl from methylphosphotriesters at Cys-69, and this specific modification—not the C-terminal Cys-321 methylation—converts Ada into a sequence-specific transcriptional activator of the adaptive response to alkylating agents [PMID:2843522, PMID:2648001]. Methylated Ada binds the ada/alkA regulatory sequence (AAAGCGCA) upstream of the promoter and recruits RNA polymerase through direct contact with the C-terminal domain of the alpha subunit and with the C-terminal region of sigma70 (notably Glu575), defining Ada as a class I activator [PMID:3139888, PMID:8468304, PMID:9582376]. The repair-to-activator switch is electrostatic rather than ligand-exchange-based: structural and spectroscopic analyses show S-methyl-Cys69 remains zinc-coordinated, and neutralization of negative charge at the zinc-thiolate center remodels a surface patch to convert phosphate repulsion into attraction for promoter DNA [PMID:9383376, PMID:11284682, PMID:16209950]. The response is self-limiting: unmethylated Ada antagonizes its own activation [PMID:7937881], and an endogenous protease cleaves Ada into a 20-kDa N-terminal fragment that activates alkA but represses ada, terminating the adaptive response [PMID:3058696, PMID:2254928]. A separate set of findings describes the eukaryotic ADA/Ada2/Ada3 transcriptional co-activator subunits, which scaffold the GCN5 histone acetyltransferase within the ADA and SAGA complexes to acetylate nucleosomal histone H3K14, antagonize chromatin-mediated repression together with SWI/SNF, and mediate activation by nuclear receptors, with complex-specific ADA2 isoforms (ATAC ADA2a vs SAGA ADA2b) differentially stimulating GCN5 [PMID:9224714, PMID:9343382, PMID:26468280]. A third set addresses human ADA enzymatic activity, whose deficiency causes toxic purine accumulation impairing TCR signaling [PMID:18218852], Treg suppressive function via the CD39/CD73/adenosine axis [PMID:22184407], bone homeostasis via RANKL/OPG imbalance [PMID:19633200], and brain adenosine receptor signaling [PMID:28074903]. These three groups describe unrelated proteins sharing the ADA/Ada symbol.

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0140097 catalytic activity, acting on DNA, GO:0016740 transferase activity, GO:0003677 DNA binding, GO:0140110 transcription regulator activity, GO:0140096 catalytic activity, acting on a protein
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-73894 DNA Repair, R-HSA-74160 Gene expression (Transcription), R-HSA-4839726 Chromatin organization
- **partners:** GCN5, ADA2, ADA3, TRA1, SPT7
- **complexes:** SAGA, ADA complex, ATAC

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1985 | High | The E. coli Ada protein (38–39 kDa) transfers methyl groups from O6-methylguanine residues in alkylated DNA to its own cysteine residues, functioning as a suicidal methyltransferase; the protein comprises 354 amino acids and the promoter was mapped by S1 nuclease. | PMID:2987251 | The Journal of biological chemistry |
| 1985 | High | Ada protein acts as a positive autogenous regulator: cloned ada gene product induces expression of O6-methylguanine-DNA methyltransferase and 3-methyladenine-DNA glycosylase II even without alkylating agent treatment, and induction is strongly enhanced by methylating agents, demonstrating that the methylated Ada protein promotes transcription of its own gene. | PMID:3929077 | Mutation research |
| 1982 | Medium | The ada mutation is in a regulatory locus controlling O6-methylguanine-DNA methyltransferase induction; ada mutants contain basal methyltransferase but cannot upregulate it upon alkylation treatment, showing Ada is required for the adaptive transcriptional response. | PMID:6749819 | Journal of bacteriology |
| 1988 | High | Methylation of Ada protein at Cys-69 (by methyl phosphotriester transfer) converts Ada into a transcriptional activator; direct methylation of purified Ada protein by chemical methylating agents (methyl methanesulfonate, methyl iodide) also activates its ability to promote ada gene transcription in a reconstituted in vitro system. | PMID:2843522 | The Journal of biological chemistry |
| 1988 | High | Ada protein expression is controlled by an ada regulatory sequence (AAAGCGCA) located upstream of the -35 box; both -10 and -35 promoter elements and this regulatory sequence are required for controlled ada expression. Methylated Ada protein is required for in vitro ada-specific transcription. | PMID:3139888 | Journal of molecular biology |
| 1988 | High | Ada protein is cleaved by an endogenous E. coli thiol protease into a 20-kDa N-terminal fragment (which retains methylphosphotriester methyltransferase activity and can promote alkA but not ada transcription when methylated) and a 19-kDa C-terminal fragment (which retains O6-methylguanine methyltransferase activity); neither fragment alone promotes ada transcription. | PMID:3058696 | The Journal of biological chemistry |
| 1989 | High | Methylated Ada protein binds the ada promoter (positions -63 to -31) including the AAAGCGCA regulatory sequence; non-methylated Ada does not bind stably. Methylation of Cys-69 (not Cys-321) is specifically required for Ada binding to the ada promoter and for facilitating subsequent RNA polymerase binding. The methylated Ada protein also allows RNA polymerase to bind properly, initiating transcription. | PMID:2648001 | Journal of molecular biology |
| 1990 | High | The methylated 20-kDa N-terminal Ada fragment binds the alkA regulatory sequence and facilitates RNA polymerase binding to the alkA promoter, activating alkA transcription in vitro. The same methylated 20-kDa protein binds the ada promoter but does not support RNA polymerase binding there, thus acting as a repressor of ada transcription. Proteolytic cleavage of Ada terminates the adaptive response by removing the activator and generating a repressor. | PMID:2254928 | Journal of molecular biology |
| 1990 | Medium | Ada protein binds DNA non-cooperatively; approximately 7 bp are covered per Ada monomer; binding is ionic in nature (equilibrium association constant decreases with increasing NaCl), as measured by fluorescence anisotropy. | PMID:2354146 | Biochemistry |
| 1993 | High | Methylated Ada protein is a class I transcription factor: it requires the C-terminal domain of the RNA polymerase alpha subunit for transcriptional activation, as demonstrated by loss of Ada-dependent activation with C-terminal-deleted alpha subunit mutant RNA polymerases. | PMID:8468304 | Journal of bacteriology |
| 1994 | High | Crystal structure of the 19-kDa C-terminal domain of E. coli Ada (Ada-C), the O6-methylguanine-DNA methyltransferase domain, shows the active-site cysteine is buried; a conformational change is proposed to allow DNA binding and methyl transfer. | PMID:8156986 | The EMBO journal |
| 1994 | High | Unmethylated Ada at physiologically relevant concentrations specifically inhibits methylated Ada activation of ada transcription (but not alkA transcription) both in vitro and in vivo; this requires the C-terminal 67 amino acids of Ada. This establishes Ada as both a positive and negative modulator of its own expression. | PMID:7937881 | Proceedings of the National Academy of Sciences of the United States of America |
| 1994 | High | In the methylated Ada protein–DNA complex, S-methylcysteine-69 (S-Me-Cys69) remains coordinated to the zinc ion; ligand exchange at the zinc center is not the mechanism for switching Ada from repair to transcriptional activator mode. | PMID:9383376 | Chemistry & biology |
| 1997 | High | Ada protein-dependent transcriptional activation at the ada and aidB promoters requires direct interaction between methylated Ada and the C-terminal domain of the RNA polymerase sigma70 subunit (amino acids 574–613); several negatively charged residues in sigma70 (notably Glu575) are critical. The alpha subunit C-terminal domain allows initial RNA polymerase binding, while sigma70 interaction drives activation. | PMID:9582376 | The Journal of biological chemistry |
| 1997 | High | E. coli Ada-C protein can repair O6-benzylguanine in DNA, but very slowly compared to human alkyltransferase and E. coli Ogt; two active-site mutations (A316P and W336A) that enlarge the substrate-binding pocket of Ada-C greatly increase its reactivity with O6-benzylguanine, and DNA binding activates Ada-C for this reaction. | PMID:9079656 | The Journal of biological chemistry |
| 2001 | High | NMR solution structure of the N-terminal 10-kDa Ada domain (N-Ada10) reveals the zinc-thiolate center; EXAFS/XANES data confirm that S-Me-Cys69 remains coordinated to zinc upon methylation. The transferred methyl group makes contacts within N-Ada but not with DNA, implying that methylation induces a conformational change that remodels the protein surface to enhance promoter DNA binding without direct methyl-DNA contact. | PMID:11284682 | Biochemistry |
| 2005 | High | X-ray and solution structures of the methylated N-terminal Ada chemosensor domain bound to DNA reveal that methyl phosphotriester repair and methylation-dependent transcriptional activation both operate through a zinc- and methylation-dependent electrostatic switch: methylation of Cys69 neutralizes a negative charge at the zinc center, converting a repulsive to an attractive interaction with DNA phosphates, thereby switching Ada from a repair protein to a transcriptional activator. | PMID:16209950 | Molecular cell |
| 1997 | High | In yeast, Gcn5 (which contains Ada protein homologs as subunits) functions as the catalytic histone acetyltransferase subunit in two distinct native complexes: the 0.8-MDa ADA complex and the 1.8-MDa SAGA complex. Both complexes contain Ada2 and can acetylate nucleosomal histones, unlike recombinant Gcn5 alone. The SAGA complex additionally contains Spt proteins linked to TBP function. | PMID:9224714 | Genes & development |
| 1997 | High | Mutations in yeast ADA2, ADA3, and GCN5 (subunits of the Ada/histone acetyltransferase complex) cause phenotypes similar to swi/snf mutants and are required for expression of SWI/SNF-dependent genes; ada and swi1 double mutants are inviable; SIN1 mutations (chromatin component) or histone H3/H4 mutations partially suppress ada/swi defects, establishing that ADA/GCN5 and SWI/SNF complexes cooperate to antagonize chromatin-mediated repression. | PMID:9343382 | Molecular and cellular biology |
| 1998 | High | Tra1p is a component of yeast Ada/Spt transcriptional regulatory complexes; its association with Ada.Spt complexes was established by tandem mass spectrometry of Ngg1p/Ada3p co-purified proteins and confirmed by reciprocal co-immunoprecipitation of Ada2p and Tra1p. Tra1p co-fractionates with Ngg1p and Spt7p; binding of Tra1p to DNA-cellulose requires Ada components. | PMID:9756893 | The Journal of biological chemistry |
| 1999 | High | The yeast ADA complex (0.8 MDa) is a distinct histone acetyltransferase complex separate from SAGA, containing Ada2, Ada3, Gcn5, and a novel unique subunit Ahc1 (product of YOR023C); deletion of AHC1 disrupts ADA complex integrity without affecting SAGA, demonstrating that ADA is not merely a SAGA subcomplex. | PMID:10490601 | Molecular and cellular biology |
| 1997 | Medium | The yeast Ada adaptor complex is important for glucocorticoid receptor (GR)-mediated gene activation; Ada2 directly binds the GR tau1c transactivation domain in vitro using purified proteins and GST-pulldown, and this interaction is reduced by a mutation that reduces tau1c transactivation. | PMID:9154805 | Molecular and cellular biology |
| 2000 | Medium | In yeast, GCN5, ADA2, ADA1, and ADA3 are required for T3/GRIP1 or SRC-1 coactivator-dependent transcriptional activation by human thyroid hormone receptor beta1 (hTRbeta1); hTRbeta1 binds directly to yeast or human GCN5 and to hADA2 in vitro; T3-dependent binding of hTRbeta1 to hGCN5 is enhanced by GRIP1 or SRC-1. The HAT domain and bromodomain of GCN5 must be intact for maximal activation. | PMID:10809234 | Molecular endocrinology (Baltimore, Md.) |
| 2000 | Medium | In human macrophages, ACAT1 localizes to the tubular rough ER under normal conditions; upon cholesterol loading, ~30–40% of total ACAT1 immunoreactivity shifts into small ER-derived vesicles that are also enriched in the ER marker GRP78, suggesting cholesterol overload activates an ER vesiculation process. (Note: appears in the Ada corpus but describes ACAT1; symbol collision artefact.) | PMID:10623671 | The American journal of pathology |
| 2015 | High | In metazoans, GCN5 is incorporated into two distinct HAT complexes: ATAC (containing ADA2a) and SAGA (containing ADA2b). The subunit environment determines GCN5 catalytic activity: all tested GCN5-containing complexes acetylate mainly histone H3K14, but ADA2b has a stronger stimulatory influence on GCN5 activity than ADA2a. Incorporation into holo-complexes further increases GCN5 activity beyond the HAT module alone. | PMID:26468280 | The Journal of biological chemistry |
| 2015 | High | The SAGA complex adopts three major conformations; the acetyltransferase module is localized in the most mobile region. Cross-linking mass spectrometry mapped comprehensive subunit interconnectivity, showing that Spt and Taf subunits form the structural core, and chromatin-binding domains cluster on one flexible face. | PMID:25713136 | The Journal of biological chemistry |
| 2011 | Medium | In ADA-deficient mice, Tregs show alterations in plasma membrane CD39/CD73 ectonucleotidase machinery and have limited suppressive activity via extracellular adenosine; ADA deficiency causes loss of Treg function contributing to autoimmunity. PEG-ADA-treated mice develop autoantibodies and hypothyroidism and have Tregs lacking suppressive activity, whereas bone marrow transplantation or gene therapy corrects Treg function. | PMID:22184407 | Blood |
| 2009 | Medium | ADA deficiency in mice causes a bone phenotype resulting from RANKL/OPG axis imbalance (decreased osteoclastogenesis) and intrinsic osteoblast dysfunction (reduced bone formation); ADA-deficient osteoblasts in vitro show altered transcriptional profile and growth reduction. Treatment with ERT, BMT, or gene therapy fully rescues the bone phenotype. | PMID:19633200 | Blood |
| 2008 | Medium | In ADA-SCID patients, ADA substrate accumulation causes impaired TCR/CD28-driven T-cell proliferation and cytokine production associated with reduced ZAP-70 phosphorylation, Ca2+ flux, and ERK1/2 signaling, and defective CREB and NF-κB transcriptional activity. Exposure to 2'-deoxyadenosine further inhibits T-cell activation via A2A adenosine receptor/PKA hyperactivation. Gene therapy restores normal TCR signaling in patient T cells. | PMID:18218852 | Blood |
| 2017 | Medium | In ADA-deficient mice, metabolic alterations in the brain include aberrant adenosine receptor signaling; PEG-ADA corrects metabolic adenosine-based alterations but not cellular and signaling defects, indicating an intrinsic neurological component to ADA deficiency separate from circulating adenosine levels. | PMID:28074903 | Scientific reports |
| 1990 | Medium | The B. subtilis ada operon encodes two separate DNA alkyltransferases: AdaA (methylphosphotriester-DNA methyltransferase) functioning as a transcriptional activator of the ada operon, and AdaB (O6-methylguanine-DNA methyltransferase) functioning specifically in repair of mutagenic O6-methylguanine; the two genes overlap by 11 bp and are co-induced by MNNG. | PMID:2120677 | Nucleic acids research |

## Citations

- PMID:10490601
- PMID:10809234
- PMID:11284682
- PMID:16209950
- PMID:18218852
- PMID:19633200
- PMID:2120677
- PMID:22184407
- PMID:2254928
- PMID:2354146
- PMID:25713136
- PMID:26468280
- PMID:2648001
- PMID:28074903
- PMID:2843522
- PMID:2987251
- PMID:3058696
- PMID:3139888
- PMID:3929077
- PMID:6749819
- PMID:7937881
- PMID:8156986
- PMID:8468304
- PMID:9079656
- PMID:9154805
- PMID:9224714
- PMID:9343382
- PMID:9383376
- PMID:9582376
- PMID:9756893
