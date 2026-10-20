# SRK2I / SnRK2.3 (At5g66880, UniProt Q39193) - curation notes

## Deep research status

`just deep-research ARATH SRK2I --provider falcon` failed on 2026-10-20 ("Exception: Failed to
authenticate"); perplexity was unavailable and openai had an invalid API key (tested with the
SRK2D run). No deep-research file was generated. These notes were written from my own reading of
cached publications and the UniProt record. See also `genes/ARATH/SRK2D/SRK2D-notes.md` for the
shared SnRK2.2/2.3 literature.

## Identity and naming

- UniProt Q39193 (SRK2I_ARATH), primary gene name SRK2I; synonyms SNRK2.3, OSKL2, 41K; At5g66880.
  Folder uses the UniProt primary name. Mostly called SnRK2.3 in the literature.

## Function summary with provenance

- Redundant with SnRK2.2 in seed germination, dormancy and root growth [PMID:17307925 "SnRK2.2 and
  SnRK2.3 are redundant but key protein kinases that mediate a major part of ABA signaling in
  Arabidopsis"].
- Phosphorylates AREB1 in gel [PMID:16446457 "we showed that ABA-activated SRK2C, SRK2D, SRK2E,
  SRK2F, and SRK2I ( 24 ) can phosphorylate the AREB1 polypeptide by using in-gel kinase activity
  assay"] and AKS1 in vitro [PMID:28438792 "Three ABA-responsive SnRK2s (SnRK2.2/SRK2D,
  SnRK2.3/SRK2I, and SnRK2.6/SRK2E/OST1) phosphorylated AKS1 in vitro"].
- Structure and autoactivation: crystal structure of full-length SnRK2.3 [PMID:22160701 "we report
  the crystal structures of full-length Arabidopsis thaliana SnRK2.3 and SnRK2.6 at 1.9- and 2.3-Å
  resolution, respectively"]; [PMID:22160701 "This stabilization enables SnRK2s to gain full
  activity by activation loop autophosphorylation. Autophosphorylation is more efficient in
  SnRK2.6, which has higher stability than SnRK2.3"]. UniProt: "Activated by autophosphorylation
  of its activation loop."
- HDX of SnRK2.3 and HAB1 [PMID:23290725 "the ABA receptor PYL2, HAB1 phosphatase, and two kinases,
  SnRK2.3 and 2.6"].
- PYR1 co-immunoprecipitates with SnRK2.3 [PMID:19874541 "PYR1 and SnRK2.3 co-immunoprecipitated
  equally well in the presence and absence of ABA"].
- Seed development/dormancy and drought (with SRK2D, SRK2E): PMID:19541597, PMID:19880399,
  PMID:19420218 (see SRK2D notes).

## Annotation-specific observations

- `NOT|located_in cytosol` (RCA, PMID:21166475, TAIR 2011) is in GOA but was not seeded into the
  stub by `just fetch-gene`; I added it as a negated row by hand. It conflicts with the IDA
  cytoplasm annotation (PMID:19880399) and with the HDA cytosol row on the paralog SRK2D; the same
  NOT row was REMOVEd in the OST1 review. REMOVE for consistency.
- `located_in plastid` (HDA, PMID:28887381) is a proteomic co-fractionation call from a
  membrane-protein profiling study; no other evidence puts SnRK2.3 in plastids.
  MARK_AS_OVER_ANNOTATED (not REMOVE, because it is experimental and I cannot see the
  supplementary data).
- TAS rows from PMID:10634783 (Li et al. 2000, Vicia faba AAPK) date from 2006. The abstract is
  about the Vicia faba guard-cell kinase AAPK, not Arabidopsis SnRK2.3; a TAS from this paper
  can only rest on a statement about Arabidopsis homologues in the full text (not cached). The
  claims are true for SnRK2.3 on other evidence, so they are kept (MODIFY protein kinase activity
  to the Ser/Thr child; ACCEPT ABA signaling), with a note.
- IPI with HAB1 from PMID:23290725 (HDX-MS of HAB1-SnRK2.3 complexes) and with ABI1/ABI2/HAB1/AHG1
  from PMID:19805022, PMID:19924127, PMID:19874541: MODIFY to protein phosphatase binding.
- IPI with AKS1 (bHLH122, Q9C690) from PMID:28438792: REMOVE (substrate relationship, bare
  protein binding).

## Differences from OST1

As for SRK2D: seed/root role rather than guard-cell role. SnRK2.3 has lower autophosphorylation
efficiency and stability than SnRK2.6 in vitro (PMID:22160701).
