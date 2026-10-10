# ARO10 notes

## Identity
- YDR380W; ThDP/Mg-dependent 2-oxo-acid decarboxylase of the PDC family [file:yeast/ARO10/ARO10-uniprot.txt "Note=Binds 1 thiamine pyrophosphate per subunit."]
- Pyruvate is not a substrate [file:yeast/ARO10/ARO10-uniprot.txt "low efficiency substrate and transaminated valine and pyruvate are no"]; [PMID:22904058 "Aro10, which cannot decarboxylate pyruvate, exhibited clear Michaelis-Menten-type saturation kinetics for all other substrates tested"]

## Evidence
- Physiological phenylpyruvate decarboxylase [PMID:12902239 "showing that Aro10p is the physiologically relevant phenylpyruvate decarboxylase in wild-type cells"]
- Redundancy with PDC1/5/6 for Phe/Trp [PMID:12499363 "This decarboxylation can be effected by any of Pdc1p, Pdc5p, Pdc6p, or Ydr380wp"]; minor in leucine in that study [PMID:12499363 "We also report that in leucine catabolism Ydr380wp is the minor decarboxylase."]
- Isoleucine [PMID:10753893 "Apparently, any one of this family of decarboxylases is sufficient to allow the catabolism of isoleucine to active amyl alcohol."]
- Methionine [PMID:16423070 "The decarboxylation is effected specifically by Ydr380wp."]
- Recombinant enzyme: efficient aromatic 2-keto acid decarboxylase [PMID:21501384 "The enzyme is shown to be an efficient aromatic 2-keto acid decarboxylase, consistent with it playing a major in vivo role in phenylalanine, tryptophan and possibly also tyrosine catabolism."], but questions BCAA/Met role [PMID:21501384 "However, its substrate spectrum suggests that it is unlikely to play any significant role in the catabolism of the branched-chain amino acids or of methionine."]
- Counterpoint (in cell extracts, Km): [PMID:22904058 "The high affinity of Aro10 identified it as a key contributor to the production of branched-chain and sulfur-containing fusel alcohols."]
- Post-transcriptional control / possible partner [PMID:15933030 "The results reported here indicate the involvement of posttranscriptional regulation and/or a second protein in the ARO10-dependent, broad-substrate-specificity decarboxylase activity."]

## Curation decisions
- REMOVE pyruvate decarboxylase (IBA from PDC clade; IEA from RHEA:54360 which is actually the 4-methyl-2-oxopentanoate reaction).
- nucleus IBA: over-annotation.
- generic catalytic / carboxy-lyase: MODIFY to specific decarboxylase terms.
- Core: phenylpyruvate decarboxylase (Phe catabolism), indolepyruvate decarboxylase (Trp), branched-chain 2-oxoacid decarboxylase (Leu/Ile).

## Module notes (ehrlich_pathway)
- ARO10 is the committed decarboxylase; PDC1/5/6 contribute redundantly for BCAA/aromatics; THI3 is not an active decarboxylase (regulatory).
- YeastPathways leucine pathway row assigns EC 4.1.1.43 (phenylpyruvate decarboxylase) to the leucine reaction - mapping quirk; EC 4.1.1.72 is the appropriate one.
