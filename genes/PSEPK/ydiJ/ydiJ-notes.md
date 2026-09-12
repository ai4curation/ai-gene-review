# ydiJ (D-2-hydroxyglutarate dehydrogenase, D2HGDH) — Pseudomonas putida KT2440

UniProt: Q88EH0 (D2HDH_PSEPK); locus PP_4493; 1006 aa.

## FUNCTION
- Catalyzes the oxidation of D-2-hydroxyglutarate (D-2-HG) to 2-oxoglutarate (2-ketoglutarate, 2KG). [UniProt "Catalyzes the oxidation of D-2-hydroxyglutarate (D-2-HGA) to"]
- Final step of the D-lysine catabolic pathway, returning the D-2-HG metabolite to central metabolism. [UniProt "Is involved in a D-lysine catabolic pathway"]
- Experimentally implicated by reverse-genetics: deletion abolishes growth on D-lysine and causes accumulation of D-2-HG. [PMID:31064836 "PP_4493 putatively oxidizes d-2HG to 2KG and connects d-lysine to central metabolism."]
- The D-2-HG isomer (rather than L-2-HG) is the substrate, requiring this dehydrogenase rather than the L-2-HG-specific oxidase LghO. [PMID:31064836 "the dehydrogenase PP_4493 gene rather than the l-2HG-specific oxidase lghO gene"]
- Belongs to the FAD-linked oxidase / glycolate dehydrogenase family of enzymes that oxidize the alcohol group of an alpha-hydroxyacid to the corresponding alpha-ketoacid. [PMID:31064836 "Glycolate dehydrogenases are members of a larger family of enzymes that oxidize the alcohol group of an alpha-hydroxyacid to the corresponding alpha-ketoacid"]

## CATALYTIC ACTIVITY
- Reaction: (R)-2-hydroxyglutarate + A = 2-oxoglutarate + AH2 (EC 1.1.99.39; RHEA:38295); physiological direction left-to-right. [UniProt "Reaction=(R)-2-hydroxyglutarate + A = 2-oxoglutarate + AH2;"]
- "(R)-2-hydroxyglutarate" is D-2-hydroxyglutarate; A is an unspecified electron acceptor (the "99" in EC 1.1.99.39 denotes "with other acceptors").

## COFACTOR
- FAD (flavin). [UniProt "Name=FAD; Xref=ChEBI:CHEBI:57692;"]
- One [4Fe-4S] cluster. [UniProt "Binds 1 [4Fe-4S] cluster."]
- Domain architecture: N-terminal FAD-binding PCMH-type domain (residues 47-279) and a 4Fe-4S ferredoxin-type domain (655-687). [UniProt "DOMAIN          47..279"], [UniProt "4Fe-4S ferredoxin-type"]
- N-terminal section belongs to the FAD-binding oxidoreductase/transferase type 4 family. [UniProt "belongs to the FAD-binding"]

## PATHWAY / PHYSIOLOGY
- Amino-acid degradation; specifically the D-lysine branch of lysine catabolism in P. putida. [UniProt "PATHWAY: Amino-acid degradation."]
- D-2-HG is produced upstream from 2-oxoadipate (2OA) by the DUF1338 metalloenzyme HglS/PP_5260; YdiJ then oxidizes D-2-HG to 2KG to feed central metabolism. [PMID:31064836 "The first route, catalyzed by the DUF1338-containing metalloenzyme PP_5260, involves the direct conversion of 2OA to d-2HG."]
- RB-TnSeq fitness: ydiJ (PP_4493) mutant had fitness defects on both D-lysine and L-lysine (scores -5.4 and -2.7). [PMID:31064836 "PP_4493, did show fitness defects on both d-lysine and l-lysine (fitness scores of −5.4 and −2.7, respectively)"]
- Deletion phenotype: cannot grow on D-lysine as sole carbon source; attenuated growth on L-lysine; accumulates D-2-HG (~500 uM). [UniProt "Deletion mutant cannot grow on D-lysine as a sole"], [PMID:31064836 "the mutant accumulated ∼500 μM 2HG"]
- Induction: up-regulated when grown on L-lysine, D-lysine, or 2-aminoadipate (2AA). [UniProt "Up-regulated when grown on L-lysine, D-lysine or 2-"]
- The gene is dispersed (outside operons), distant from other lysine catabolic genes. [PMID:31064836 "PP_4493 found at locations that were outside operons and relatively distant from other lysine catabolic genes"]

## CURATION NOTES (annotation assessment)
- Core MF: GO:0051990 (R)-2-hydroxyglutarate dehydrogenase activity — directly matches EC 1.1.99.39 and the experimentally supported reaction. ACCEPT (both the EC-based IEA and the ISS to ortholog P77748).
- GO:0003824 catalytic activity is a root-level parent and is over-annotated once the specific dehydrogenase term is present.
- GO:0050660 (flavin adenine dinucleotide binding) and GO:0071949 (FAD binding): correct cofactor (UniProt records FAD), but broad relative to the specific dehydrogenase term; mark as over-annotated (keep cofactor signal but not core). The two are near-duplicate FAD-binding terms.
- GO:0004458 D-lactate dehydrogenase (cytochrome) activity and GO:0008720 D-lactate dehydrogenase (NAD+) activity: TreeGrafter/PANTHER family-based predictions. The protein is a D-2-HG dehydrogenase, not a D-lactate dehydrogenase; these are paralog/family over-annotations and the specific lactate substrate activity is not supported. MODIFY toward the specific D-2-HG dehydrogenase activity (the NAD+ one is additionally wrong on cofactor; this enzyme is FAD-dependent, EC 1.1.99.x uses "other acceptors", not NAD+).
- GO:1903457 lactate catabolic process: TreeGrafter family transfer; the demonstrated process is lysine catabolism / 2-oxoglutarate metabolism, not lactate catabolism. MODIFY to the lysine catabolic / 2-oxoglutarate metabolic process.
- 4Fe-4S / metal-ion: UniProt keyword-based GO terms (GO:0051539, GO:0046872) appear in the UniProt cross-references but are NOT in the GOA TSV, so they are not reviewed as existing_annotations here.
