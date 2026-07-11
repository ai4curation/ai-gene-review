# PHKA2 review notes

UniProtKB: P46019 (KPB2_HUMAN). Gene: PHKA2 (synonyms PHKLA, PYK). X chromosome. 1235 aa.

## Verified biology

PHKA2 encodes the **liver isoform of the alpha regulatory subunit** of phosphorylase kinase (PhK).

PhK is a large (alpha-beta-gamma-delta)4 hexadecameric holoenzyme:
- **gamma (PHKG1 muscle / PHKG2 liver)** is the **catalytic** subunit (a Ser/Thr protein kinase).
- **alpha (PHKA1 muscle / PHKA2 liver)** and **beta (PHKB)** are the large **regulatory** subunits.
- **delta = calmodulin** confers Ca2+ sensitivity.

UniProt SUBUNIT [file:human/PHKA2/PHKA2-uniprot.txt]:
"Hexadecamer of 4 heterotetramers, each composed of alpha, beta, gamma, and delta subunits. Alpha (PHKA1 or PHKA2) and beta (PHKB) are regulatory subunits, gamma (PHKG1 or PHKG2) is the catalytic subunit, and delta is calmodulin."

Therefore **PHKA2 is NOT itself a protein kinase.** Its own molecular role is regulatory: the alpha/beta subunits are the targets of cAMP-dependent (PKA) phosphorylation which, together with Ca2+/calmodulin, relieves the inhibition of the catalytic gamma subunit and activates the holoenzyme. UniProt ACTIVITY REGULATION: "By phosphorylation of various serine residues and by calcium." PHKA2 carries multiple experimentally-mapped phosphoserines in its C-terminal multiphosphorylation domain (Ser695, Ser729, Ser735, Ser983, Ser1015, Ser1044).

PhK phosphorylates glycogen phosphorylase (b -> a), triggering glycogenolysis (Reactome R-HSA-71588; R-HSA-70221 Glycogen breakdown). So PHKA2 is a structural/regulatory part of the complex that carries out the holoenzyme activity GO:0004689 phosphorylase kinase activity, but does not itself enable it.

UniProt FUNCTION: "Phosphorylase b kinase catalyzes the phosphorylation of serine in certain substrates, including troponin I. The alpha chain may bind calmodulin." Note this FUNCTION line describes the holoenzyme (PHK); the alpha chain's own contribution is calmodulin binding. Two Calmodulin-binding REGIONs are annotated (807-837, 1059-1099), and the KW list includes Calmodulin-binding.

## Localization

- Reactome/GOA: cytosol (GO:0005829, TAS). The complex acts in the cytosol on cytosolic glycogen phosphorylase.
- UniProt SUBCELLULAR LOCATION: "Cell membrane {ECO:0000305}; Lipid-anchor {ECO:0000305}; Cytoplasmic side" — this is an ECO:0000305 (inferred) subcellular location, based on a possible C-terminal farnesyl-Cys (LIPID at 1232, itself by similarity ECO:0000250|UniProtKB:P18688; and PTM note says the terminal tripeptide is "probably not removed" and C-terminus "not methylated"). The plasma-membrane GO annotation (GO:0005886, IEA UniProtKB-SubCell SL-0039) rests on this weak by-similarity prenylation inference. The dominant, functionally relevant compartment is the cytosol.
- Cytoplasm (GO:0005737, IEA ARBA) is a correct but less-specific parent of cytosol.

## Disease

Deficiency causes **Glycogen storage disease type IXa / GSD9A (X-linked liver phosphorylase kinase deficiency)** — MIM:306000, Orphanet 264580. Most common form of PhK deficiency. Hepatomegaly, growth retardation, usually mild and improving with age (often asymptomatic in adults). Two subtypes: type 1/classic (no PhK activity in liver AND erythrocytes) and type 2/variant (deficient in liver, normal in erythrocytes). Extensive allelic series of GSD9A missense/indel variants in UniProt.

[PMID:7549948 "X-linked liver glycogenosis (XLG) due to liver phosphorylase kinase (PHK)" ... "deficiency is the most frequent liver glycogen storage disease."; "We isolated and determined the structure of human liver alpha subunit of PHK (PHKA2) cDNA."; "a valine substitution for glycine at amino acid 193, in the PHKA2 gene of a family with XLG."]

## GOA annotation assessment summary

- GO:0005964 phosphorylase kinase complex (IBA, IEA-Ensembl, TAS PMID:7549948, part_of): ACCEPT x3. Core — this is the defining, well-supported complex membership.
- GO:0004689 phosphorylase kinase activity (IEA ARBA `enables`; TAS PMID:7549948 `enables`): MARK_AS_OVER_ANNOTATED. This is the HOLOENZYME activity, catalyzed by the gamma subunit. PHKA2 as a regulatory subunit contributes to it but does not itself enable it. Not REMOVE — the essence (participation in the complex activity) is right, but `enables` on the alpha subunit over-attributes catalysis. In core_functions captured via contributes_to_molecular_function.
- GO:0005516 calmodulin binding (IEA InterPro/KW): ACCEPT (core). Supported by two annotated CaM-binding regions and the KW; a genuine molecular function of the alpha subunit.
- GO:0005737 cytoplasm (IEA ARBA): ACCEPT as broad parent of cytosol; less specific.
- GO:0005886 plasma membrane (IEA SubCell SL-0039): MARK_AS_OVER_ANNOTATED. Rests on an ECO:0000305 by-similarity prenylation inference; the functionally relevant compartment is the cytosol. Not clearly wrong but weakly supported / likely over-annotation.
- GO:0005975 carbohydrate metabolic process (IEA InterPro; TAS PMID:7549948): ACCEPT (broad but correct).
- GO:0005977 glycogen metabolic process (IEA UniPathway): ACCEPT (correct, specific-enough; could be refined to glycogen catabolic).
- GO:0005515 protein binding (IPI x9, all high-throughput IntAct datasets, bare term): MARK_AS_OVER_ANNOTATED for all. Uninformative bare term. The biologically meaningful partners (PHKG2 catalytic gamma P15735, PHKB Q93100) are complex partners already captured by the complex annotation; the rest (UROD P06132, SPRED1 Q7Z699) are HT hits without functional interpretation. Per policy: MARK_AS_OVER_ANNOTATED, not REMOVE.
- GO:0005829 cytosol (TAS Reactome): ACCEPT (core location).
- GO:0006091 generation of precursor metabolites and energy (TAS PMID:7549948): KEEP_AS_NON_CORE. Downstream/indirect (glycogenolysis feeds energy metabolism) but not PHKA2's core function.
- GO:0036211 protein modification process (TAS PMID:7549948): MARK_AS_OVER_ANNOTATED. Refers to PhK phosphorylating its substrate — a gamma-subunit (catalytic) property, over-broad and over-attributed to the alpha regulatory subunit.

## Core functions
- MF (own): calmodulin binding GO:0005516.
- contributes_to MF: phosphorylase kinase activity GO:0004689 (holoenzyme).
- directly_involved_in BP: glycogen catabolic process GO:0005980.
- in_complex: phosphorylase kinase complex GO:0005964.
- location: cytosol GO:0005829.
</content>
