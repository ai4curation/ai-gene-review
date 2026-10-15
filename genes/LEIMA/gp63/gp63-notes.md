# gp63 (leishmanolysin, MSP) — Leishmania major — curation notes

**Note on provenance:** automated deep research was NOT available in this environment
(no working provider credentials), so no `-deep-research-*.md` file exists for this gene.
What follows is a **manual literature review** done by reading the UniProt record, the
cached publications under `publications/`, and primary papers located via PubMed
(E-utilities) and cached with `ai-gene-review fetch-pmid`. Every PMID cited below was
verified against PubMed before caching. Quotes are verbatim from the cached records.

## 1. Identity and structure

- UniProt P08148, `GP63_LEIMA`, "Leishmanolysin", EC 3.4.24.36, 602 aa precursor;
  signal peptide 1–39, activation propeptide 40–100, mature chain 101–577, C-terminal
  propeptide 578–602 removed on GPI attachment (UniProt FT lines).
- Zinc metalloendopeptidase of the **peptidase M8 family** (`PANTHER:PTHR10942`,
  Pfam PF01457, MEROPS M08.001). Crystal structure 1LML at 1.86 Å
  [PMID:9739094 "Leishmanolysin is a membrane-bound zinc proteinase, active in situ."];
  the fold places it in the metzincins [PMID:9739094 "a member of the metzincin class of zinc proteinases."].
- Catalytic HEXXH motif; Glu-265 is the general base
  [PMID:8626468 "the following. 1) Glu-265 in the HEXXH motif is indispensable for the catalytic"].
  UniProt COFACTOR: "Binds 1 zinc ion per subunit." (ECO:0000269|PubMed:9739094).
- Membrane attachment is by a **GPI anchor** on Asn-577
  [PMID:2145267 "contains a glycosyl-phosphatidylinositol (GPI) membrane anchor"], and
  mutating that site releases the protein
  [PMID:8626468 "Asn-577 causes release of all mutant products, indicative of its specificity as"].
  So the protein is an anchored component of the **outer (external) face of the parasite
  plasma membrane**, with a released/secreted pool as well.
- Gene family: in L. major the *msp*/gp63 genes are a tandem array on chromosome 10 plus
  copies on chromosomes 28 and 31, with stage-specific expression (genes 1–6 promastigote,
  gene 7 metacyclic/amastigote) [PMID:9489664]. P08148 is one member of this family;
  paralog-level over-annotation is therefore a real risk, but the biochemistry
  (zinc endopeptidase, surface GPI anchor) is shared across the family and is directly
  established for the L. major protein whose structure was solved.

## 2. Localization

Cell surface of the promastigote, GPI-anchored, catalytically active in situ
[PMID:9739094 "Leishmanolysin is the predominant protein surface antigen of"]. A soluble
pool is released, and released enzyme is active
[PMID:12540585 "Leishmania species engineered to express high levels of the surface metalloprotease gp63 have enhanced capacity of migration through extracellular matrix in vitro."].
GP63 is also exported in exosomes
[PMID:22442494 "leishmania use a remarkably adept, exosome-based secretion mechanism to export"],
and reaches the host macrophage cytosol via lipid rafts, where it meets cytoplasmic
substrates [PMID:19797268 "The mechanism underlying PTP modulation"].

Protist-specific check: no kinetoplastid-specific compartment term (glycosome,
kinetoplast, paraflagellar rod, flagellar pocket) is warranted from the primary data for
P08148. The amastigote pool is reported as partly flagellar-pocket associated in the
review literature, but that is secondary and not species/accession-specific enough to
annotate here.

## 3. Catalytic activity and substrates

EC 3.4.24.36, "Preference for hydrophobic residues at P1 and P1' and basic residues at
P2' and P3'" (UniProt CATALYTIC ACTIVITY). Documented substrates span host proteins:

- **Complement C3b → iC3b**: surface GP63 accelerates C3b conversion, limiting assembly
  of the terminal complement complex
  [PMID:7673725 "Organisms expressing wild-type gp63 more rapidly converted C3b"],
  [PMID:7673725 "surface fixed only small amounts of the terminal complement components and were"],
  [PMID:22919663 "Leishmania overexpressing proteolytically active GP63 was able to increase the conversion of C3b into C3bi and to reduce the fixation of terminal complement components to Leishmania"].
  Loss-of-function mutants are complement-sensitive
  [PMID:9489664 "The gp63 genes 1-6-deficient mutants showed increased sensitivity"],
  [PMID:9489664 "clearly involved in conferring resistance to complement-mediated lysis. The L."],
  and the whole-locus (gp63 1–7) deletion is complement-sensitive and delayed in lesion
  formation [PMID:11849703 "sand flies or from culture showed an increase in sensitivity to"].
  Importantly, complement **fixation** itself does not need GP63 proteolysis
  [PMID:7673725 "The proteolytic activity of this molecule was not"] — the proteolysis-dependent
  part is the C3b→iC3b conversion and the escape from lysis. The iC3b coat then engages
  CR3/Mac-1 [PMID:7673725 "avidly with cells expressing Mac-1, the receptor for iC3b. Complement fixation"],
  which is how GP63 contributes to attachment/uptake by macrophages
  [PMID:11849703 "interaction of promastigotes and host macrophage receptors and interaction with"].

- **Host protein tyrosine phosphatases SHP-1, PTP1B, TCPTP**: cleaved by GP63, which
  *activates* them and thereby shuts down JAK/STAT (IFN-γ) and MAPK signaling
  [PMID:19797268 "involves the proteolytic activity of the Leishmania surface protease GP63."],
  [PMID:19797268 "lipid raft-dependent mechanism, resulting in PTP cleavage and stimulation of"],
  [PMID:22919663 "GP63 is responsible for the activation of protein tyrosine phosphatases (PTPs; SHP-1, PTP1B,"].

- **mTOR**: GP63 cleaves mTOR, inhibiting mTORC1 and activating 4E-BP1, repressing
  cap-dependent translation in the infected macrophage
  [PMID:21501832 "the Leishmania protease GP63 cleaves"],
  [PMID:21501832 "inhibition of mTOR complex 1 (mTORC1) and concomitant activation of 4E-BP1 to"].

- **Synaptotagmin XI (host)**: directly degraded, de-repressing TNF/IL-6 secretion
  [PMID:25063865 "Syt XI is directly degraded by the zinc metalloprotease GP63"],
  [PMID:25063865 "Infected macrophages were found to release TNF and IL-6 in a"],
  [PMID:25063865 "proinflammatory cytokine release and increases infiltration of inflammatory"].
  Note the direction: here GP63 *increases* a proinflammatory output, i.e. it perturbs
  (not simply suppresses) the host inflammatory response.

- **Antimicrobial peptides**: degraded by surface GP63; knockouts are AMP-hypersensitive
  [PMID:17074074 "AMP evasion is due to rapid and"],
  [PMID:17074074 "extensive peptide degradation by wild-type parasites"].

- **Host extracellular matrix** (collagen IV, fibronectin), promoting migration
  [PMID:12540585 "This correlates with gp63 degradation of extracellular matrix components, such as collagen type IV and fibronectin"].

## 4. Curation decisions taken

- `GO:0004222 metalloendopeptidase activity` and `GO:0008237 metallopeptidase activity`:
  both correct; the endopeptidase term is the core MF, the generic metallopeptidase row
  is kept as the same claim at lower resolution (MODIFY → GO:0004222).
- `GO:0005886 plasma membrane`: correct but less specific than the GPI data support →
  MODIFY to `GO:0009897 external side of plasma membrane`. (The anchored-component terms
  that would state the GPI attachment directly, GO:0031362 and GO:0046658, are **obsolete**
  in the ontology version used by validation, so they cannot be used here.)
- `GO:0016020 membrane`: TOO_GENERAL (entailed by the plasma-membrane claim).
- `GO:0007155 cell adhesion`: an InterPro-family electronic transfer of a generic
  (animal-flavoured) adhesion term. The real, documented adhesion claim is
  parasite-to-host-cell attachment → MODIFY to `GO:0044650 adhesion of symbiont to host cell`.
- `GO:0006508 proteolysis` (IEA and IMP rows): accepted, core.
- Host-interaction terms (`GO:0039514`, `GO:0052028`, `GO:0052032`, `GO:0141115` ×2):
  all supported by the cited primary work and used in the right direction
  (suppression of JAK-STAT; activation of host signaling and perturbation — here
  augmentation — of the inflammatory response; inactivation of complement proteins).
- NEW proposed: `GO:0008270 zinc ion binding` (structure/cofactor, PMID:9739094) and
  `GO:0039604 symbiont-mediated suppression of host translation` (GP63 itself cleaves
  mTOR, so it performs the step; PMID:21501832).
  AMP degradation and ECM degradation are real but I did not find a GO term that fits
  without stretching, so they are recorded as questions rather than asserted annotations.

## 5. Revision (review-fix round, PR #5029)

- **Truncated quotations repaired.** Two `supporting_text` values had been cut at the cached
  file's hard line wrap and ended mid-clause ("the Leishmania protease GP63 cleaves"), so they
  no longer stated the claim they were attached to. Both are now full clauses:
  [PMID:21501832 "we show that the Leishmania protease GP63 cleaves the mammalian/mechanistic
  target of rapamycin (mTOR), a serine/threonine kinase that regulates the translational
  repressor 4E-BP1"]. The companion quote in the same row was completed likewise:
  [PMID:21501832 "mTOR cleavage results in the inhibition of mTOR complex 1 (mTORC1) and
  concomitant activation of 4E-BP1 to promote Leishmania proliferation."].
- **GO:0008270 zinc ion binding (NEW) re-anchored.** It had been supported by a metzincin
  *class* statement ("a member of the metzincin class of zinc proteinases"), which is a
  family-level property, not an observation on P08148. It is now anchored to the three
  explicit UniProt `BINDING` features for the catalytic Zn(2+) in P08148 itself -- residues
  264, 268 and 334, each `/ligand="Zn(2+)" /ligand_id="ChEBI:CHEBI:29105"
  /ligand_note="catalytic"` and evidenced to PubMed:9739094 -- cited as
  `file:LEIMA/gp63/gp63-uniprot.txt`, the form other reviews use for UniProt features
  (cf. genes/DANRE/asah2, genes/human/AGTPBP1). Residue identities were read off the
  sequence in the flat file: 264 H, 265 E (catalytic base), 268 H, 334 H, i.e. the
  HEXXH pair plus the third metzincin histidine, not a Met-turn methionine.
