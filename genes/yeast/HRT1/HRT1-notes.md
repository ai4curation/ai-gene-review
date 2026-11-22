# HRT1 (Q08273, YOL133W; Rbx1/Roc1) - curation notes

## Identity and family

- Hrt1 is the ~17 kDa RING-H2 subunit identified by mass spectrometry among Cdc53-copurifying proteins [PMID:10385629 "Mass spectrometric analysis of proteins copurifying with Cdc53 identified the RING–H2 finger protein Hrt1 as a subunit of SCF."]. It is the yeast orthologue of human RBX1/ROC1 and the paralogue of Apc11; it is the only cullin-binding RING-box protein in the yeast genome [PMID:17296727 "Roc1 physically and functionally interacts with the three highly related yeast cullins, Cdc53 (Cul1), Cul3, and Cul8, and it interacts also with the distantly related cullin Apc2"].
- The gene is essential (the HRT1 ORF overlaps YOL134C; complementation shows HRT1 is the essential one) [PMID:10385629 "Two lines of evidence indicate that HRT1 is essential, and YOL134c is dispensable."], and human HRT1/RBX1 complements the deletion [PMID:10385629 "The highly conserved human HRT1 complements the lethality of hrt1Δ"].
- UniProt: RING-type zinc finger 55-111, eleven zinc-ligand residues by similarity to RBX1 (three zinc sites); temperature-sensitive rbx1-1 (K72R/C81R) and hrt1-C81Y RING alleles lose ligase activity.

## Molecular function

- Hrt1 binds Cdc53, Cdc4 and Cdc34 directly but not Skp1 [PMID:10385629 "Hrt1 assembles into recombinant SCF complexes and individually binds Cdc4, Cdc53 and Cdc34, but not Skp1."]; the Cdc53/Hrt1 subcomplex is a minimal ligase that activates Cdc34 without a reactive thiol [PMID:10385629 "Cdc53/Hrt1-dependent autoubiquitination of Cdc34 is indifferent to NEM."] - i.e. a RING E3, no E3~Ub thioester.
- GST-Hrt1 stimulates SCF(Cdc4) ubiquitination of phospho-Sic1 >5-fold and is required for SCF(Grr1) activity on Cln2 [PMID:10385629 "GST–Hrt1 potently stimulated ubiquitination of phospho–MBP–Sic1."; "those that contained Hrt1 sustained Cdc34-dependent ubiquitination of Cln2"].
- Skowyra et al. reconstituted SCF(Grr1)-Rbx1 ubiquitination of phospho-Cln1 and showed Rbx1 recruits Cdc34 to Cdc53 [PMID:10213692 "Rbx1 promotes association of Cdc34 with Cdc53 and stimulates Cdc34 auto-ubiquitination in the context of Cdc53 or SCF complexes."].
- RING mutations abolish ligase activity of ROC1 immunocomplexes without disturbing complex assembly [PMID:10230407 "ROC1 mutations completely abolished their ligase activity without noticeable changes in associated proteins."].
- Rub1/NEDD8 pathway: Hrt1 promotes Rub1 conjugation to Cdc53 and Rtt101 (UniProt, from PMID:10579999 - not cached) [file:yeast/HRT1/HRT1-uniprot.txt "Also stimulates CDC34/UBC3 autoubiquitination and promotes the neddylation of CDC53 and RTT101."]; Scott et al. 2010 (not cached; summarised in the deep research) showed the Hrt1 RING activates Ubc12~Rub1 and is required for transfer to Cdc53 K760, with Dcn1 as co-E3. Purified Cdc53/Hrt1 is rubylated in vitro and sequestered by the CAND1-like Lag2 [PMID:19942853 "Although both hCul1/hRbx1 and Cdc53/Hrt1 complexes were efficiently modified by Rub1"; "Lag2/Cand1 tightly binds to the cullin/Hrt1 heterodimer, and thereby prevents the assembly of an active CRL complex."].

## Biological processes

- G1/S: hrt1-ts (HRT1myc9) cells fail to enter S phase, keep Sic1, and stabilise Cln2 (t1/2 8 -> 19 min) [PMID:10385629 "Conditional inactivation of hrt1 ts results in stabilization of the SCF Cdc4 substrates Sic1 and Cln2 and cell cycle arrest at G 1 /S."]; reduced ROC1 expression accumulates Sic1 and Cln2 [PMID:10230407 "YeastROC1 encodes an essential gene whose reduced expression resulted in multiple, elongated buds and accumulation of Sic1p and Cln2p."]. SCF(Met30) output (MET25 repression) is also lost in hrt1-ts.
- Non-SCF cullins: Cul8/Rtt101 anaphase function requires Roc1 binding [PMID:12676951 "The anaphase delay phenotype can be complemented by ectopic expression of Cul8 but not by any other yeast or human cullins, nor by a cul8 mutant deficient in binding to RING finger protein Roc1."]; the Elc1-Ela1-Cul3-Roc1 ligase is proposed to K48-polyubiquitylate Rpb1 after DNA damage, with Roc1 participation explicitly presumed [PMID:17296727 "Although we have not examined the effects of ROC1 inactivation upon Pol II polyubiquitylation and degradation, ... we presume that Roc1 also is indispensable for Pol II polyubiquitylation and degradation."]. The Cul8 complex-composition paper never tests Hrt1 [PMID:20139071 "Herein, we report that Cul8 forms at least four different protein complexes: Cul8-Mms1-Mms22-Esc4, Cul8-Mms1-Mms22-Ctf4, Cul8-Mms1-Esc2, and Cul8-Mms1-Orc5."].
- Receptor-defined outputs annotated to the shared RING by NAS transfer: GAL1 derepression via SCF(Das1)/Mig2 [PMID:21323640], mitochondrial fusion via SCF(Mdm30)/Fzo1 [PMID:21502136], HMR/telomeric silencing via SCF(Dia2)/Sir4 [PMID:22844255 "we show that SCF(Dia2) ubiquitylates Sir4 in vitro and in vivo."], checkpoint recovery via SCF(Dia2)/Mrc1 [PMID:23172854], methylmercury resistance via SCF(Hrt3)/SCF(Ylr224w) [PMID:17141224]. None of these papers manipulates HRT1.

## Localisation

- Functional GFP-Hrt1 (GAL-driven) is in nucleus and cytoplasm; Cdc4 is exclusively nuclear and restricts Far1 degradation to the nucleus [PMID:11080155 "The core SCF subunits Cdc53, Hrt1 and Skp1 were distributed in the nucleus and the cytoplasm, whereas the F-box protein Cdc4 was exclusively nuclear."]. UniProt: cytoplasm and nucleus (PMID:10880467, not cached).
- The GO:0000781 (chromosome, telomeric region) IEA is an inter-ontology inference from the GO:0031509 NAS row; no evidence places Hrt1 at telomeres.

## Curation decisions (summary)

- ACCEPT: all ligase/complex/catabolic/localisation rows, all five IBA rows (PAINT node PTN000129805; Hrt1 in its own WITH/FROM is expected), zinc binding, proteasomal catabolism IEA, Cul3/Cul8 complex rows.
- MODIFY: GO:0030674 adaptor activity -> GO:0061630 / GO:0031624 (the RING activates the E2, it does not merely bridge); GO:0007346 -> GO:0000082; GO:0031573 intra-S checkpoint signaling -> GO:1904290 (SCF(Dia2) switches the checkpoint off); GO:0006289 NER -> GO:0006974 DNA damage response (Pol II degradation is an alternative to TCR, not an excision step; Roc1 role presumed); protein-binding rows with cullins from focused studies -> GO:0097602.
- REMOVE: GO:0000781 IEA (over-propagated location); bare GO:0005515 rows from high-throughput screens (Uetz, Ho, Hazbun, Yu, Michaelis), from the SCF en-masse purification with non-cullin partners, and the two rows citing PMID:23267104 (a S. pneumoniae interaction paper whose cached text never mentions yeast proteins).
- KEEP_AS_NON_CORE: G2/M, GAL1 regulation, mitochondrial fusion, HMR/subtelomeric silencing, regulation of DNA replication (Rtt101 ligases).
- MARK_AS_OVER_ANNOTATED: glucose-transport induction, methylmercury response, nucleosome assembly and heterochromatin formation from the Cul8 composition paper.
- NEW: GO:0019788 NEDD8 transferase activity and GO:0045116 protein neddylation, traceable to UniProt (PMID:10579999) and Scott 2010; human RBX1 carries both, so the yeast absence is a gap rather than a convention. Primary papers are not in the local cache, hence TAS on the UniProt record.

## Gaps / caveats

- PMID:10579999 (Kamura 1999, Rub1 modification), PMID:10880467 (Blondel 2000 Genetics, HRT1/Gic2 screen and localisation) and PMID:10213691 (Kamura 1999 Science, Rbx1/VHL) are cited by UniProt but not cached; not fetched because the task forbids writing outside genes/yeast/HRT1/.
- Many cited references are abstract-only (PMID:10213692, 10230407, 14747994, 21323640, 12676951, 12150908, 21502136, 17141224 and the HTP screens); no experimental annotation was removed on that basis.
