# secDF (Bacillus subtilis 168, UniProt O32047) - curation notes

## Deep research status

Automated deep research could not be generated for this gene on 2026-11-13:

- `just deep-research BACSU secDF --provider perplexity` failed: "Provider 'perplexity' not available. Available: falcon, openscientist, claude_code".
- `just deep-research BACSU secDF --provider falcon` failed: "falcon: 403 Failed to authenticate -- the API key is missing, invalid, or lacks access to this endpoint".
- `just deep-research BACSU sipS --provider openai` (run for the sibling sipS review) failed: "Provider 'openai' not available".

These notes are therefore a manual literature summary built from the cached publications
(`publications/PMID_*.md`) and the UniProt record. Literature consulted: PMID:9694879,
PMID:15995216, PMID:11524133 (all abstract-only in the cache), PMID:21562494 and
PMID:29718185 (full text cached).

## Identity and architecture

- B. subtilis SecDF is a single polypeptide in which SecD and SecF are fused
  [PMID:9694879 "the SecD and SecF equivalents of the Gram-positive bacterium Bacillus subtilis are jointly present in one polypeptide, denoted SecDF, that is required to maintain a high capacity for protein secretion"].
- It has 12 predicted transmembrane segments and resembles secondary solute transporters
  [PMID:9694879 "Thus, SecDF does not only show sequence similarity but also structural similarity to secondary solute transporters"].
- UniProt places the SecD region at residues 1-416 and the SecF region at 446-737, with two
  large extracytoplasmic loops (27-254, the P1-equivalent, and 475-569, the P4-equivalent).
- The T. thermophilus homolog is also a single-chain SecDF with 12 TM helices and the RND
  fold [PMID:21562494 "SecDF from Thermus thermophilus HB817 is composed of a single polypeptide chain"].
  This makes T. thermophilus SecDF a closer architectural model for B. subtilis SecDF than the
  two-subunit E. coli SecD/SecF.

## Function

- Required for efficient (high-capacity) secretion; not required for release of mature proteins
  from the membrane, unlike E. coli SecD [PMID:9694879 "SecDF of B. subtilis was not required for the release of a mature secretory protein from the membrane, indicating that SecDF is involved in earlier translocation steps"].
- Loss of SecDF gives cold sensitivity, worsened by hypersecretion
  [PMID:9694879 "Strains lacking intact SecDF showed a cold-sensitive phenotype, which was exacerbated by high level production of secretory proteins"].
- Mechanism (from the T. thermophilus / E. coli work): SecDF is a proton-conducting,
  PMF-powered component of the Sec machinery that acts after SecA/ATP-dependent initiation
  [PMID:21562494 "we have shown that SecDF is a component of the Sec machinery that utilizes the PMF to complete protein translocation after the ATP-dependent SecA function"];
  [PMID:21562494 "SecDF conducts protons in a manner dependent on pH and the presence of an unfolded protein"].
  No B. subtilis-specific proton-conduction measurement is in the cached literature; the
  PMF-coupled transporter activity is transferred by homology (same fused architecture, same
  family, conserved TM Asp/Arg residues).
- SecDF is not an ATPase. The InterPro2GO mapping to GO:0015450 protein-transporting ATPase
  activity is mechanistically wrong for this family (SecA is the ATPase).

## Localization

- Membrane protein uniformly distributed in the cell membrane, including in mother cell and
  forespore during sporulation [PMID:15995216 "three SecYEG translocase-associated membrane proteins (SecDF, SpoIIIJ, and YqjG) are uniformly distributed"].

## Curation decisions (summary)

- Plasma membrane rows: ACCEPT.
- GO:0043952 protein transport by the Sec complex: ACCEPT (core process).
- GO:0065002 intracellular protein transmembrane transport: ACCEPT (accurate transmembrane
  transport process; GO:0043952 is not one of its descendants, so it cannot be refined to it).
- GO:0006886 intracellular protein transport: MODIFY to GO:0065002 (a true descendant).
- GO:0015031 protein transport (IBA): MODIFY to GO:0043952 (a true descendant).
- GO:0006605 protein targeting: MARK_AS_OVER_ANNOTATED. SecDF acts during translocation after
  substrates have been targeted to SecYEG, and GO:0043952 is not a descendant of protein
  targeting, so no valid refinement exists.
- GO:0015450 protein-transporting ATPase activity: REMOVE (wrong energy coupling), and add NEW
  contributes_to GO:0009977 proton motive force dependent protein transmembrane transporter
  activity, matching the E. coli SecD/SecF reviews.
