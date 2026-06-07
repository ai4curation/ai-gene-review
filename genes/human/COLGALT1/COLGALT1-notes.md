# COLGALT1 (Q8NBJ5) review notes

## Identity
- HGNC symbol: COLGALT1 (synonym GLT25D1); ORFNames PSEC0241.
- UniProt Q8NBJ5, "Procollagen galactosyltransferase 1" / "Collagen beta(1-O)galactosyltransferase 1" (ColGalT 1) / "Glycosyltransferase 25 family member 1" / "Hydroxylysine galactosyltransferase 1".
- EC 2.4.1.50 [ECO:0000269|PubMed:19075007].
- CAZy GT25; glycosyltransferase 25 family.
- 622 aa precursor; signal peptide 1-29, chain 30-622; C-terminal RDEL (619-622) ER retention motif.

## Core function
- Beta(1-O)galactosyltransferase that transfers galactose from UDP-alpha-D-galactose onto (5R)-5-hydroxy-L-lysine (hydroxylysine, Hyl) residues of collagen, forming Gal-O-Hyl. This is the FIRST step of collagen O-linked glycosylation; the resulting galactose is the acceptor for subsequent alpha1,2-glucosylation, yielding the conserved Glc(alpha1-2)Gal disaccharide [PMID:19075007; PMID:27402836 "Nascent procollagen chains are modified ... and glycosylation of selected hydroxylysine (Hyl) residues"].
- Reaction: (5R)-5-hydroxy-L-lysyl-[collagen] + UDP-alpha-D-galactose = (5R)-5-O-(beta-D-galactosyl)-5-hydroxy-L-lysyl-[collagen] + UDP + H+ (RHEA:12637) [file:human/COLGALT1/COLGALT1-uniprot.txt CATALYTIC ACTIVITY].
- Schegg et al. identified GLT25D1/GLT25D2 as the two beta(1-O)galactosyltransferases that initiate core glycosylation of collagen and also act on the collagenous domain of MBL [PMID:19075007 (UniProt FUNCTION/CATALYTIC ACTIVITY)].
- KM for UDP-galactose ~18.7 uM (PubMed:19075007) / 29.9 uM (PubMed:22216269).
- Catalytic Asp residues identified by mutagenesis: D166/D168 and D461/D463 essential for galactosyltransferase activity (loss when mutated to Ala); D-X-D-like motifs typical of metal(Mn2+)-dependent GT-A glycosyltransferases [file:human/COLGALT1/COLGALT1-uniprot.txt MUTAGEN; PubMed:22216269].

## Subcellular localization
- Soluble protein of the ENDOPLASMIC RETICULUM LUMEN. Has N-terminal cleaved signal sequence and C-terminal RDEL ER-retention/retrieval signal; membrane floatation shows it is NOT an integral membrane protein [PMID:20470363 "GLT25D1 is directed to the ER lumen as a soluble protein and retained there"; "RDEL retrieves GLT25D1 to the ER"; "The bulk of GLT25D1 is observed in the bottom fractions ... indicating the protein is not an integral membrane protein"].
- Co-localizes with PLOD3/LH3 (lysyl hydroxylase 3, upstream enzyme) and with the substrate MBL in the early secretory pathway [PMID:20470363 "overlapping localization patterns of GLT25D1, MBL and LH3"].
- The HDA "membrane" annotation (GO:0016020, PMID:19946888) comes from a large-scale NK-cell (YTS) membrane-proteome mass-spec study. That paper notes ~60% of identified proteins were NOT plausible integral membrane proteins but transiently membrane-associated; this is consistent with a soluble ER-lumen protein being co-isolated with membranes. Not a reliable localization claim for COLGALT1 [PMID:19946888 abstract].

## Glycosyltransferase substrate / biological role
- Loss of GLT25D1 (CRISPR/Cas9) in SaOS-2 osteosarcoma cells: decreased collagen glycosylation by up to 60%, increased collagen type I expression and intracellular (ER) accumulation, with compensatory induction of GLT25D2. GLT25D1 is the main isoform; GLT25D2 loss alone had no effect on collagen secretion. Simultaneous loss of both could not be recovered, suggesting collagen glycosylation is essential for osteosarcoma viability [PMID:27402836 abstract & Discussion]. Notably, loss of GLT25D1 "did not alter collagen folding and thermal stability" in this cell model [PMID:27402836].
- The GO IMP annotation GO:1904028 "positive regulation of collagen fibril organization" (PMID:27402836) is an over-interpretation: the paper measured intracellular collagen accumulation/expression and glycosylation, not fibril organization per se. The UniProt FUNCTION states glycosylation "facilitates the formation of collagen triple helix (PubMed:27402836)" but the paper actually reported no change in folding/thermal stability; the fibril-organization phenotype is at best indirect.

## Disease
- Biallelic COLGALT1 variants cause Brain small vessel disease 3 (BSVD3, MIM:618360), an autosomal recessive cerebral small vessel disease (porencephaly, intracranial hemorrhage, developmental delay). Variants L151R, A154P, G377R; L151R shown to cause loss of galactosyltransferase activity. Also implicated in collagen type IV biosynthesis [PMID:30412317 (UniProt FUNCTION/DISEASE)].

## Structure
- Multiple recent experimental structures (cryo-EM 8ZGC/8ZGE/8ZGG/8ZGH; X-ray 9EVJ/9EVK/9EVL), residues 30-622.
- Tandem GT-A-like domains (HHpred hits to GT-2/pp-GalNAc-T10 and GT-31/Manic Fringe) [PMID:20470363].

## Annotation review summary
- ACCEPT (core MF): GO:0050211 procollagen galactosyltransferase activity (IBA, IMP, TAS, IEA all converge; well supported experimentally).
- ACCEPT (core CC): GO:0005788 endoplasmic reticulum lumen (IDA PMID:20470363; multiple TAS/IEA).
- ACCEPT / KEEP (BP): GO:0180062 protein O-linked glycosylation via galactose (IMP) — accurate description of the process the enzyme performs.
- KEEP_AS_NON_CORE: GO:0030199 collagen fibril organization (TAS Reactome) — downstream/indirect.
- MARK_AS_OVER_ANNOTATED: GO:1904028 positive regulation of collagen fibril organization (IMP PMID:27402836) — over-interpretation of the loss-of-function data.
- MARK_AS_OVER_ANNOTATED: GO:0016020 membrane (HDA PMID:19946888) — soluble ER-lumen protein co-isolated in a membrane proteome screen; contradicted by IDA soluble-ER evidence.

## Proposed additions (not in current GOA)
- GO:0030145 manganese ion binding — UniProt/EC and GT-A-fold D-X-D catalytic Asp residues (D461/D463 essential by mutagenesis) indicate Mn2+-dependence typical of GT-A glycosyltransferases; no direct experimental metal-binding annotation exists in GOA. Proposed as a new term on family/structural grounds.
