# OPTN (Optineurin) — review notes

UniProt: Q96CV9 (OPTN_HUMAN), 577 aa, human (NCBITaxon:9606). HGNC:17142.

## Architecture / domains (from UniProt feature table)
- Coiled-coil protein: COILED 38-170 and 239-508. Highly homologous (~53% identity) to NEMO/IKBKG ("NEMO-related protein", NRP).
- **LIR motif (LC3-interacting region): residues 176-181** (MOTIF). Mediates interaction with ATG8/LC3/GABARAP family. Phe178 critical [PMID:21617041 "Single point mutations at either OPTN Phe178->Ala178 (F178A) or I181A ... were sufficient to abrogate the interaction with LC3/GABARAP proteins"].
- **UBAN motif (ubiquitin binding in ABIN and NEMO): residues 474-479** (MOTIF). Binds linear (M1) and K63 polyubiquitin; D474/F475 essential. D474N abolishes Ub binding.
- **CCHC NOA-type zinc finger: residues 547-577**; coordinates Zn2+ via residues 555/558/571/575. KW: Zinc, Zinc-finger, Metal-binding. (GO:0008270 zinc ion binding IEA-keyword in DR lines; not in GOA TSV.)
- Phosphoserine S177 by TBK1 (adjacent to LIR; enhances LC3 binding). Also S198, S342, S526 phospho (proteomic).
- Rab8 interaction region 58-209; MYO6 interaction 412-520; HD (huntingtin) interaction 411-577.

## Core function: selective autophagy receptor
OPTN simultaneously binds ubiquitinated cargo (via UBAN) and ATG8/LC3/GABARAP (via LIR), bridging cargo to autophagosomal membranes. TBK1 binds and phosphorylates OPTN at S177, increasing LC3 affinity.

- Salmonella xenophagy [PMID:21617041 "phosphorylation of an autophagy receptor, optineurin, promoted selective autophagy of ubiquitin-coated cytosolic Salmonella enterica. The protein kinase TANK binding kinase 1 (TBK1) phosphorylated optineurin on serine-177, enhancing LC3 binding affinity and autophagic clearance of cytosolic Salmonella"]. UBAN-deficient (E478G / DF474-475NA) and LIR (F178A) mutants fail to restrict bacteria. OPTN/NDP52/p62 act along same pathway. Kd of LIR-LC3B falls from 67 µM (P0) to 13 µM (pS177) to 5 µM (penta-phospho).
- Mitophagy (PINK1/Parkin) [PMID:25294927 "optineurin as an autophagy receptor in parkin-mediated mitophagy"]. Parkin ubiquitinates outer mitochondrial membrane proteins; OPTN stably associates via UBAN, then recruits LC3 via LIR to induce autophagosome formation around damaged mitochondria. ALS-linked UBAN mutant E478G cannot stably associate -> defective mitophagy. This is GO:0061734 "type 2 mitophagy" (Parkin/depolarization-initiated) — verified valid GO term.
- TBK1 binding/activation: extensive (NbExp=17 IntAct). OPTN recruits and activates TBK1 at Golgi for innate immune signaling [PMID:27538435 Golgi platform for TBK1 activation after viral RNA sensing].

## Ubiquitin binding (MF)
- GO:0070530 K63-linked polyubiquitin modification-dependent protein binding (IBA + IEA) — core; UBAN binds K63 and linear chains.
- GO:0031593 polyubiquitin modification-dependent protein binding (IDA, PMID:21617041) — core; OPTN bound to ubiquitin chains but not mono-ubiquitin ["OPTN bound to ubiquitin chains and autophagy modifiers ... but not to mono-ubiquitin"].
- GO:0030674 protein-macromolecule adaptor activity (IPI, PMID:25803835, TBK1) — captures adaptor/bridging function; core MF for receptor role.

## Golgi / membrane trafficking (secondary, real)
[PMID:15837803 "optineurin links myosin VI to the Golgi complex and plays a central role in Golgi ribbon formation and exocytosis"]. OPTN depletion -> myosin VI lost from Golgi, Golgi fragmented, VSV-G exocytosis reduced. Binds GTP-Rab8 and huntingtin. Terms: GO:0090161 Golgi ribbon formation (IDA), GO:0007030 Golgi organization (IMP), GO:0043001 Golgi to plasma membrane protein transport (IMP), GO:0034067 protein localization to Golgi apparatus (IMP). These are genuine but secondary/pleiotropic relative to the autophagy-receptor core.

## Trafficking via TBC1D17/Rab8 (secondary)
[PMID:22854040 "Optineurin mediates a negative regulation of Rab8 by the GTPase-activating protein TBC1D17"]. OPTN bridges Rab8 to GAP TBC1D17; regulates transferrin receptor (TFRC) endocytic recycling. GO:0001920 negative regulation of receptor recycling (IMP). Glaucoma E50K disrupts this. UBAN binds ubiquitinated TFRC [PMID:20085643].

## NF-kB / innate immune signaling (secondary regulatory)
- NEMO-related; negatively regulates NF-kB by competing with NEMO/IKBKG for polyubiquitin. GO:0043122 regulation of canonical NF-kappaB signal transduction (IBA).
- Negatively regulates IFN-beta induction during RNA virus infection [PMID:20174559 "Over-expression of optineurin inhibited Sendai-virus ... triggered induction of IFNbeta, whereas depletion ... promoted virus-induced IFNbeta production"]. Forms complex with TBK1 and TRAF3; UBAN/ubiquitin binding required.
- Reactome models OPTN binding polyUb-RIPK1, CASP8, recruiting CYLD to TNFR1 complex, TBK1 in TLR3/TLR4 complexes.

## Disease
- POAG (GLC1E): E50K (in N-term coiled-coil/Rab8 region), R545Q, H486R, etc. E50K disrupts Rab8 interaction and enhances TBK1 interaction -> insolubility [PMID:23669351].
- Normal-pressure glaucoma (NPG): H26D.
- ALS12 (+/- FTD): E478G (UBAN, abolishes Ub binding -> defective mitophagy/xenophagy), V295F (Golgi fragmentation, ER stress, PMID:27534431), Q398X truncation (literature).

## Annotation-review judgments
- ACCEPT as core: autophagy-receptor MFs (GO:0070530, GO:0031593, GO:0030674 adaptor), positive regulation of autophagy (GO:0010508 IDA), positive regulation of xenophagy (GO:1904417 IMP), defense response to Gram-negative bacterium (GO:0050829 IMP), type 2 mitophagy (GO:0061734 IMP), autophagosome localization (GO:0005776), TBK1-related and well-supported direct localizations.
- KEEP_AS_NON_CORE: Golgi maintenance/trafficking processes & locations, NF-kB regulation, receptor recycling, signal transduction, cell death, secondary localizations (nucleus, recycling endosome, TGN, perinuclear), all generic Reactome cytosol/nucleoplasm terms.
- protein binding (GO:0005515) and identical protein binding (GO:0042802, self-association/oligomerization): KEEP_AS_NON_CORE (uninformative bare terms; note real interactors TBK1, MYO6, RAB8, TBC1D17, SQSTM1, HTT, TNIP1, etc.). Self-association is real (NbExp=16 OPTN-OPTN) but uninformative as MF.
- GO:0034620 cellular response to unfolded protein (IMP, PMID:27534431): based on V295F ALS mutant causing ER stress; this is a mutant-phenotype/disease readout rather than a normal OPTN function -> KEEP_AS_NON_CORE (defer to curator; experimental, do not remove).

No deep-research provider file present; notes assembled from UniProt + cached full-text/abstracts (PMIDs above).
