# SLC6A6 (TauT) — review notes

UniProt: **P31641** (SC6A6_HUMAN). HGNC:11052. Taxon: Homo sapiens (9606). 620 aa.

## Identity and family

- RecName: **Sodium- and chloride-dependent taurine transporter**; AltName: Solute carrier family 6 member 6; Taurine transporter (**TauT**) [file:human/SLC6A6/SLC6A6-uniprot.txt "RecName: Full=Sodium- and chloride-dependent taurine transporter"].
- Belongs to the **sodium:neurotransmitter symporter (SNF) (TC 2.A.22) family. SLC6A6 subfamily** [file:human/SLC6A6/SLC6A6-uniprot.txt "Belongs to the sodium:neurotransmitter symporter (SNF)"].
- 12 transmembrane helices confirmed by cryo-EM (TOPO_DOM/TRANSMEM 1..620, N- and C-termini cytoplasmic). Na+, Cl−, and taurine binding sites mapped near TM1/TM6/TM8 residues (G57, F58, N63, Y138, F300, S301, S402, E406, etc.).

## Core molecular function and mechanism

- **Mediates sodium- and chloride-dependent transport of taurine** [file:human/SLC6A6/SLC6A6-uniprot.txt "Mediates sodium- and chloride-dependent transport of taurine,"]. Stoichiometry Na+/Cl−/taurine = 2:1:1 [PMID:8010975 "The Na+/Cl-/taurine stoichiometry for the cloned transporter is 2:1:1."].
- Catalytic reaction (RHEA:71223): taurine(out) + chloride(out) + 2 Na(+)(out) = taurine(in) + chloride(in) + 2 Na(+)(in) [file:human/SLC6A6/SLC6A6-uniprot.txt].
- Also transports, with lower affinity, **beta-alanine, hypotaurine and GABA (4-aminobutanoate)** [file:human/SLC6A6/SLC6A6-uniprot.txt "Can also mediate transport of beta-alanine, hypotaurine and"]. Substrate specificity: taurine and other beta-amino acids incl. beta-alanine; high affinity for taurine (KM ~6 µM) [PMID:8010975 "The transporter is specific for taurine and other beta-amino acids,"]. RPE clone: taurine, beta-alanine and GABA compete for uptake; alpha-alanine and AIB do not [PMID:8654117 "beta-alanine and gamma-amino-n-butyric acid at 100 microM inhibited the uptake"].
- KM for taurine: 5.9 µM (PMID:8010975), 2 µM (PMID:8654117), 3.8 µM (PMID:31903486), 7.62 µM (PMID:41269860). Uniformly high-affinity, low-µM.
- Intestinal TauT: **Na+- and Cl−-dependent, high-affinity, low-capacity transporter of taurine and beta-alanine** [PMID:19074966 "TauT (SLC6A6) is a Na(+)- and \nCl(-)-dependent, high-affinity, low-capacity transporter of taurine and \nbeta-alanine;"].

Note on GO term choice: GOA carries both **GO:0005369 taurine:sodium symporter activity** (the mechanism-specific term, dominant across IDA/IMP/IBA) and **GO:0005368 taurine transmembrane transporter activity** (parent). The symport is Na+- AND Cl−-coupled (2:1:1). GO:0005369 is the closest well-supported MF term in GOA and is used as the primary core MF. The GABA/beta-alanine symporter activities (GO:0005332, GO:0001761, GO:0015185) are genuine lower-affinity/secondary activities documented structurally and functionally.

## Subcellular location

- **Cell membrane (plasma membrane); multi-pass** [file:human/SLC6A6/SLC6A6-uniprot.txt "SUBCELLULAR LOCATION: Cell membrane"]. IDA plasma membrane from patient-mutation and proteomic studies (PMID:31345061, PMID:31903486, PMID:28112518).
- **Mitochondrion inner membrane** — newly reported: SLC6A6 also localizes to mitochondria and imports taurine for mt-tRNA modification [PMID:41652173 "we show that SLC6A6, \nbut not exogenous taurine, is essential for mitochondrial metabolism and cancer \ncell growth. We discover that SLC6A6 also localizes to mitochondria and imports \ntaurine for mitochondrial transfer RNA modifications."]. PKA phosphorylation at Ser-21/Ser-25 promotes plasma-membrane localization while inhibiting mitochondrial localization; N-terminal MTS (1–41) targets mitochondria.
- Epithelial polarity: in placental syncytiotrophoblast TAUT is **primarily localized in the syncytiotrophoblast microvillous plasma membrane (MVM)** — maternal-facing/apical [PMID:15166008 "TAUT \nwas primarily localized in the syncytiotrophoblast microvillous plasma membrane \n(MVM)."]. In human fetal RPE, TAUT quantified on both apical and basolateral surfaces (PMID:31791063 QTAP of apical vs basolateral membranes).

## Tissue expression

- **Expressed abundantly in placenta and skeletal muscle, at intermediate levels in heart, brain, lung, kidney and pancreas and at low levels in liver** [file:human/SLC6A6/SLC6A6-uniprot.txt]. HPA: tissue enhanced (retina).

## Physiology and disease

- Loss of function causes **Hypotaurinemic retinal degeneration and cardiomyopathy (HTRDC, MIM:145350)**, autosomal recessive: low plasma taurine, childhood-onset progressive retinal degeneration, cardiomyopathy [file:human/SLC6A6/SLC6A6-uniprot.txt "Hypotaurinemic retinal degeneration and cardiomyopathy (HTRDC)"].
- Biallelic SLC6A6 mutation linked to early retinal degeneration; variant A78E severely decreases taurine transport in patient cells [PMID:31345061 title].
- Variant G399V; taurine supplementation treats retinal degeneration and cardiomyopathy in a consanguineous family [PMID:31903486 title].
- Taurine is the most abundant amino acid in human placenta; TauT knockdown compromises trophoblast differentiation and increases apoptosis under inflammatory cytokine [PMID:23519128 "Trophoblast differentiation was compromised in TauT-deficient \ncells, and susceptibility of these cells to an inflammatory cytokine that is \nelevated in FGR was increased, evidenced by elevated levels of apoptosis."].
- Anti-aging/senescence: taurine acts as an anti-aging agent, levels decline with age; TauT structure work framed around alleviating cellular senescence (PMID:40108449) and aging-associated disorders (PMID:40615403). Negative regulation of cellular senescence annotated by ISS/IEA from mouse ortholog O35316.
- Cancer / drug delivery: SLC6A6 (with SLC6A13) mediates uptake of 5-aminolevulinic acid (ALA), enhancing protoporphyrin IX accumulation / photodamage in cancer cells [PMID:24842606 "neurotransmitter transporters including SLC6A6 and SLC6A13 \nmediate the uptake of ALA"]. Note this is a substrate-promiscuity / drug-uptake role, not a canonical physiological function.

## Regulation

- Stimulated by thyrotropin (TSH) via cAMP in thyroid (FRTL-5) cells [PMID:8382624 "The taurine \nuptake in FRTL-5 cells appears to be regulated by thyrotropin through cAMP."].
- Stimulated by hypertonic stress (osmoregulation; by similarity); inhibited by GABA, hypotaurine, beta-alanine and various sulfonate analogs; down-regulated by Ser-322 phosphorylation (by similarity) and by PKC activation / NO in placenta.
- Induction regulated by NFAT5 (tonicity-responsive), which regulates mitochondrial function of SLC6A6 [file:human/SLC6A6/SLC6A6-uniprot.txt "Expression is regulated by NFAT5"].

## Annotation-review reasoning highlights

- Core MF: GO:0005369 taurine:sodium symporter activity (huge IDA/IMP/IBA support, incl. 6+ structural/functional papers) — ACCEPT.
- Core CC: GO:0005886 plasma membrane (IDA/ISS/IBA/TAS) — ACCEPT. Apical (GO:0016324) + basolateral (GO:0016323) IDA — accept as epithelial context refinements (core plasma-membrane sub-locations).
- Core BP: GO:0015734 taurine transmembrane transport (IDA/IMP/ISS/IBA/TAS) — ACCEPT.
- Mitochondrial inner membrane (GO:0005743) IDA (PMID:41652173) + positive regulation of mitochondrial translation (GO:0070131) IDA — accept as genuine newly-discovered non-canonical/moonlighting localization+role; the IEA SubCell version is redundant but reflects the same finding.
- beta-alanine (GO:0001761/GO:0001762) and GABA (GO:0015185/GO:0005332/GO:0051939) activities: genuine but secondary/lower-affinity substrates — KEEP_AS_NON_CORE (functionally real, not the defining physiological role).
- GO:0022858 alanine transmembrane transporter activity + GO:0032328 alanine transport (IDA PMID:19074966): the paper studies taurine/beta-alanine, and TauT does NOT accept alpha-alanine (PMID:8654117). "alanine" here almost certainly refers to beta-alanine handling in an SLC6A6 context; but the GO term GO:0022858 is for alanine (alpha) transport. Cannot verify alpha-alanine transport; ARUK-UCL experimental IDA — do not REMOVE per policy; MARK_AS_OVER_ANNOTATED (likely a beta-alanine finding over-mapped to the generic alanine term).
- GO:0006836 neurotransmitter transport (IEA InterPro) and GABA-related terms reflect family-level (SNF) inheritance; taurine is not a classical neurotransmitter. KEEP_AS_NON_CORE / non-core, family-derived.
- GO:0150104 transport across blood-brain barrier (NAS, review PMIDs 30280653 & 26590417): both are general BBB reviews that do not specifically establish SLC6A6 BBB transport in their abstracts/text. Author statement (NAS) — KEEP_AS_NON_CORE but flag low relevance; not core.
- GO:0045597 positive regulation of cell differentiation (IMP PMID:23519128): trophoblast differentiation compromised in TauT-deficient cells — genuine but tissue-specific downstream role. KEEP_AS_NON_CORE.
- GO:0089718 amino acid import across plasma membrane / GO:0098739 import across plasma membrane / GO:0006865 amino acid transport / GO:0015171 amino acid transmembrane transporter activity / GO:0005283 amino acid:sodium symporter activity: correct but general parents of the taurine-specific function; ACCEPT the redundant-but-correct ones where experimentally grounded, otherwise KEEP as generalizations. Prefer taurine-specific terms as core.
- GO:0035725 sodium ion transmembrane transport (IBA): mechanistically correct (Na+ is co-transported) but the co-ion role, not the substrate; KEEP_AS_NON_CORE.
- GO:2000773 negative regulation of cellular senescence (IEA/ISS from mouse O35316): plausible (taurine anti-senescence) but by orthology only; KEEP_AS_NON_CORE.
- CC dendrite / neuronal cell body (ISS from rat GAT P31643): transferred from a GABA transporter paralog; SLC6A6 neuronal-compartment localization not established in human — MARK_AS_OVER_ANNOTATED (ISS from a paralog, weak).
- GO:0031528 microvillus membrane (IDA PMID:15166008): placental MVM localization directly shown — ACCEPT (epithelial-context CC).
- GO:0016020 membrane (TAS/IEA): uninformative generic parent — MARK_AS_OVER_ANNOTATED.

## Full-text availability of cited pubs

- full_text_available: true for PMID:19074966, PMID:23519128, PMID:26590417 (and 31903486 pdf_partial).
- Abstract-only (full_text_available: false): 8382624, 8010975, 8654117, 24842606, 41652173, 31345061, 15166008, 28112518, 31791063, 40108449, 40615403, 40789850, 41269860. Quotes taken only from cached text (abstracts) for these.
