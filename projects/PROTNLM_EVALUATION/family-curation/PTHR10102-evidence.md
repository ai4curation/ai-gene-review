# PTHR10102: source excerpts

Raw provenance: [family snapshot](family-sources/PTHR10102.json); [UniProt snapshot](uniprot-records.jsonl.gz), supplemented by [successful retries](uniprot-retries.jsonl.gz).

## Integrated InterPro IPR002092

Generated description flag: False; reviewed generated text flag: False. Generated prose is a source lead, not independent biological validation.

DNA-directed RNA polymerases [ec:2.7.7.6] (also known as  DNA-dependent RNA polymerases) are responsible for the polymerisation of ribonucleotides into a sequence complementary to the template DNA. In eukaryotes, there are three different forms of DNA-directed RNA polymerases transcribing different sets of genes. Most RNA polymerases are multimeric enzymes and are composed of a variable number of subunits. The core RNA polymerase complex consists of five subunits (two alpha, one beta, one beta-prime and one omega) and is sufficient for transcription elongation and termination but is unable to initiate transcription. Transcription initiation from promoter elements requires a sixth, dissociable subunit called a sigma factor, which reversibly associates with the core RNA polymerase complex to form a holoenzyme [[cite:PUB00000061]]. The core RNA polymerase complex forms a "crab claw"-like structure with an internal channel running along the full length [[cite:PUB00033173]]. The key functional sites of the enzyme, as defined by mutational and cross-linking analysis, are located on the inner wall of this channel.

RNA synthesis follows after the attachment of RNA polymerase to a specific site, the promoter, on the template DNA strand.  The RNA synthesis process continues until a termination sequence is reached. The RNA product, which is synthesised in the 5' to 3' direction, is known as the primary transcript.

Eukaryotic nuclei contain three distinct types of RNA polymerases that differ in the RNA they synthesise:


RNA polymerase I: located in the nucleoli, synthesises precursors of most ribosomal RNAs.
RNA polymerase II: occurs in the nucleoplasm, synthesises mRNA precursors.
RNA polymerase III: also occurs in the nucleoplasm, synthesises the precursors of 5S ribosomal RNA, the tRNAs, and a variety of other small nuclear and cytosolic RNAs.


Eukaryotic cells are also known to contain separate mitochondrial and chloroplast RNA polymerases. Eukaryotic RNA polymerases, whose molecular masses vary in size from 500 to 700kDa, contain two non-identical large (>100kDa) subunits and an array of up to 12 different small (less than 50kDa) subunits.
The phage-type enzymes are a family of single chain polymerases found in bacteriophages and mitochondria [[cite:PUB00003849], [cite:PUB00101425]].

## Exact benchmark records

### SCHPO/rpo41 — O13993
UniProt record: https://www.uniprot.org/uniprotkb/O13993/entry
Status: UniProtKB reviewed (Swiss-Prot); length: 1154 aa; sequence version: 2.

**FUNCTION**
DNA-dependent RNA polymerase catalyzes the transcription of DNA into RNA using the four ribonucleoside triphosphates as substrates. Combines in the mitochondrion with mitochondrial transcription factor mtf1 as a holoenzyme to recognize and initiate transcription at the core mitochondrial promoters
Evidence: [{"evidenceCode": "ECO:0000269", "source": "PubMed", "id": "21357609"}]
**CATALYTIC ACTIVITY**
{"name": "RNA(n) + a ribonucleoside 5'-triphosphate = RNA(n+1) + diphosphate", "reactionCrossReferences": [{"database": "Rhea", "id": "RHEA:21248"}, {"database": "Rhea", "id": "RHEA-COMP:14527"}, {"database": "Rhea", "id": "RHEA-COMP:17342"}, {"database": "ChEBI", "id": "CHEBI:33019"}, {"database": "ChEBI", "id": "CHEBI:61557"}, {"database": "ChEBI", "id": "CHEBI:140395"}], "ecNumber": "2.7.7.6", "evidences": [{"evidenceCode": "ECO:0000255", "source": "PROSITE-ProRule", "id": "PRU10031"}, {"evidenceCode": "ECO:0000255", "source": "PROSITE-ProRule", "id": "PRU10032"}]}
**SUBCELLULAR LOCATION**
{"location": {"value": "Mitochondrion", "id": "SL-0173"}}
**SIMILARITY**
Belongs to the phage and mitochondrial RNA polymerase family
Evidence: [{"evidenceCode": "ECO:0000305"}]
InterPro: IPR046950 [{"key": "EntryName", "value": "DNA-dir_Rpol_C_phage-type"}]
InterPro: IPR002092 [{"key": "EntryName", "value": "DNA-dir_Rpol_phage-type"}]
InterPro: IPR043502 [{"key": "EntryName", "value": "DNA/RNA_pol_sf"}]
InterPro: IPR037159 [{"key": "EntryName", "value": "RNA_POL_N_sf"}]
InterPro: IPR029262 [{"key": "EntryName", "value": "RPOL_N"}]
PANTHER: PTHR10102 [{"key": "EntryName", "value": "DNA-DIRECTED RNA POLYMERASE, MITOCHONDRIAL"}, {"key": "MatchStatus", "value": "1"}]
PANTHER: PTHR10102:SF0 [{"key": "EntryName", "value": "DNA-DIRECTED RNA POLYMERASE, MITOCHONDRIAL"}, {"key": "MatchStatus", "value": "1"}]
Pfam: PF00940 [{"key": "EntryName", "value": "RNA_pol"}, {"key": "MatchStatus", "value": "1"}]
Pfam: PF14700 [{"key": "EntryName", "value": "RPOL_N"}, {"key": "MatchStatus", "value": "1"}]

