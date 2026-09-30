# PTHR24072: source excerpts

Raw provenance: [family snapshot](family-sources/PTHR24072.json); [UniProt snapshot](uniprot-records.jsonl.gz), supplemented by [successful retries](uniprot-retries.jsonl.gz).

## Integrated InterPro IPR003578

Generated description flag: False; reviewed generated text flag: False. Generated prose is a source lead, not independent biological validation.

This entry represents the Rho subfamily of Ras-like small GTPases. The small GTPase-like protein LIP2 (light insensitive period 2) fromArabidopsis thalianais implicated in control of the plant circadian rhythm [[cite:PUB00083222]].  The crystal structures of a number of the members of this entry have been determined: Rnd3/RhoE [[cite:PUB00027242]], RhoA [[cite:PUB00028136]] and  Cdc42 [[cite:PUB00025351]].
Small GTPases form an independent superfamily within the larger class of regulatory GTP hydrolases. This superfamily contains proteins that control a vast number of important processes and possess a common, structurally preserved GTP-binding domain [[cite:PUB00052600], [cite:PUB00004087]]. Sequence comparisons of small G proteins from various species have revealed that they are conserved in primary structures at the level of 30-55% similarity [[cite:PUB00000348]].

Crystallographic analysis of various small G proteins revealed the presence of a 20kDa catalytic domain that is unique for the whole superfamily [[cite:PUB00004087], [cite:PUB00023196]]. The domain is built of five α helices (A1-A5), six β-strands (B1-B6) and five polypeptide loops (G1-G5). A structural comparison of the GTP- and GDP-bound forms allows one to distinguish two functional loop regions, switch I and switch II that surround the gamma-phosphate group of the nucleotide. The G1 loop (also called the P-loop) that connects the B1 strand and the A1 helix is responsible for the binding of the phosphate groups. The G3 loop provides residues for Mg2 and phosphate binding and is located at the N terminus of the A2 helix. The G1 and G3 loops are sequentially similar to Walker A and Walker B boxes that are found in other nucleotide binding motifs. The G2 loop connects the A1 helix and the B2 strand and contains a conserved Thr residue responsible for Mg2 binding. The guanine base is recognised by the G4 and G5 loops. The consensus sequence NKXD of the G4 loop contains Lys and Asp residues directly interacting with the nucleotide. Part of the G5 loop located between B6 and A5 acts as a recognition site for the guanine base [[cite:PUB00015117]].

The small GTPase superfamily can be divided into at least 8 different families, including:

Arf small GTPases. GTP-binding proteins involved in protein trafficking by modulating vesicle budding and uncoating within the Golgi apparatus.
Ran small GTPases. GTP-binding proteins involved in nucleocytoplasmic transport. Required for the import of proteins into the nucleus and also for RNA export.
Rab small GTPases. GTP-binding proteins involved in vesicular traffic.
Rho small GTPases. GTP-binding proteins that control cytoskeleton reorganisation.
Ras small GTPases. GTP-binding proteins involved in signalling pathways.
Sar1 small GTPases. Small GTPase component of the coat protein complex II (COPII) which promotes the formation of transport vesicles from the endoplasmic reticulum (ER).
Mitochondrial Rho (Miro). Small GTPase domain found in mitochondrial proteins involved in mitochondrial trafficking.
Roc small GTPases domain. The small GTPase domain is always found associated with the COR domain.

## Exact benchmark records

### human/RHOJ — G3V4H1
UniProt record: https://www.uniprot.org/uniprotkb/G3V4H1/entry
Status: UniProtKB unreviewed (TrEMBL); length: 153 aa; sequence version: 1.

**CATALYTIC ACTIVITY**
{"name": "GTP + H2O = GDP + phosphate + H(+)", "reactionCrossReferences": [{"database": "Rhea", "id": "RHEA:19669"}, {"database": "ChEBI", "id": "CHEBI:15377"}, {"database": "ChEBI", "id": "CHEBI:15378"}, {"database": "ChEBI", "id": "CHEBI:37565"}, {"database": "ChEBI", "id": "CHEBI:43474"}, {"database": "ChEBI", "id": "CHEBI:58189"}], "ecNumber": "3.6.5.2", "evidences": [{"evidenceCode": "ECO:0000256", "source": "ARBA", "id": "ARBA00047660"}]}
**SIMILARITY**
Belongs to the small GTPase superfamily. Rab family
Evidence: [{"evidenceCode": "ECO:0000256", "source": "PROSITE-ProRule", "id": "PRU00753"}]
InterPro: IPR027417 [{"key": "EntryName", "value": "P-loop_NTPase"}]
InterPro: IPR005225 [{"key": "EntryName", "value": "Small_GTP-bd"}]
InterPro: IPR001806 [{"key": "EntryName", "value": "Small_GTPase"}]
InterPro: IPR003578 [{"key": "EntryName", "value": "Small_GTPase_Rho"}]
PANTHER: PTHR24072 [{"key": "EntryName", "value": "RHO FAMILY GTPASE"}, {"key": "MatchStatus", "value": "1"}]
Pfam: PF00071 [{"key": "EntryName", "value": "Ras"}, {"key": "MatchStatus", "value": "1"}]

