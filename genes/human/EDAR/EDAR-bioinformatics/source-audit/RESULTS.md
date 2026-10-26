# EDAR source measurements and annotation provenance

The saved-input replay completed successfully against 21 hashed inputs. It reproduces the following source facts; the associated annotation judgments are separate.

## Extracellular binding screen

The actual PMID:32822567 Data S4 contains four EDAR incident records, representing two pairs in both orientations. Each row has three assay and three control readings. The script recomputes each fold-over-background value and its mean from those readings.

| Data S4 Excel row | Prey | Bait | Mean fold over background |
| --- | --- | --- | ---: |
| 99 | EDA | EDAR | 2.9251 |
| 100 | EDAR | EDA | 12.6108 |
| 101 | EDAR | LILRB1 | 7.6461 |
| 252 | LILRB1 | EDAR | 9.8157 |

Data S1 parent sequences exactly match current human Q9UNE0 (448 aa), Q92838 (391 aa) and Q8NHL6 (650 aa). The tested extracellular segments are EDAR 27–187, EDA 63–391 and LILRB1 24–461. Data S5 contains no EDAR SPR record. These results support controlled extracellular binding; they do not establish physiological signaling, native processing or an unmeasured orthogonal assay.

| Partner | Independent class authority | Scope of refinement |
| --- | --- | --- |
| EDA Q92838 | [Official EDA record](https://www.uniprot.org/uniprotkb/Q92838/entry), together with independently reported EDA-A1–EDAR ligand recognition in [PMID:11039935](https://pubmed.ncbi.nlm.nih.gov/11039935/) | Cytokine binding describes the positive pair. The recombinant ECD's natural processing is not inferred. |
| LILRB1 Q8NHL6 | [Official LILRB1 record](https://www.uniprot.org/uniprotkb/Q8NHL6/entry) identifies an inhibitory signaling receptor based on independent ligand/signaling studies | Signaling receptor binding describes the positive pair; it does not claim EDAR is an agonist or that it executes LILRB1's immune functions. |

## Other source joins

The IntAct query has 57 total records; five cite PMID:11035039, including one EDA–EDAR record. Literal tags, regions, species and source identifiers are retained in `results.json`. EDAR and EDA deposited reference ROGIDs match current reference sequences. Original paper constructs and IntAct feature ranges remain distinct rather than silently harmonized.

The PTHR12120 tree and MSA each contain 125 nodes/sequences. EDAR leaf PTN002486226 has a 14-node root-to-leaf path and an exact 448-residue sequence match. Three literal family IBDs occur on the target path: receptor activity and cytokine signaling at PTN004336494, and plasma membrane at PTN000950406. The complete source GAF is included so the family selection and absence of additional family assertions can be reproduced. Self-inclusion among descendant experimental sources is not circular evidence.

Current ARBA condition sets 169, 52 and 11 (zero-based) respectively match the EDAR FunFam in ARBA00027254, ARBA00028236 and ARBA00084990; the latter also specifies Chordata. The script reports the actual conditions and official lineage, without inferring a new empirical experiment from a rule.

Four reaction/component paths reach Q9UNE0 residues 27–448 in plasma membrane from R-HSA-5669012 and R-HSA-5675656. The separate cytosolic EDARADD entity does not change EDAR's compartment. Donor source annotations and InterPro mappings remain explicitly identified in the output.

See [source-manifest.json](source-manifest.json) for the exact input URLs, hashes and byte counts, [results.json](results.json) for full selected measurement/source fields, and [README.md](README.md) for the saved replay command. No paper body is republished here.
