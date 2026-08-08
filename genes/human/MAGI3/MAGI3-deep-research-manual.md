# Manual deep research: human MAGI3 (Q5TCQ9)

## Scope and provenance

This report is a manual evidence synthesis prepared after both configured automated providers failed on 2026-07-18 (Falcon/Edison HTTP 402; Perplexity Lite HTTP 401 quota exceeded). It uses the local UniProt/GOA records, cached PubMed/PMC publications, and current Gene Ontology definitions. It is deliberately named `-deep-research-manual.md`, not after a provider.

## Biological identity and architecture

MAGI3 (membrane-associated guanylate kinase, WW and PDZ domain-containing protein 3) is a 1,481-residue MAGUK-family scaffold. The reviewed UniProt record contains an N-terminal guanylate-kinase-like domain, two WW domains, and six PDZ domains. Despite the name, the guanylate-kinase-like domain is noncatalytic: the full-text MAGI3 study in breast cancer describes "a catalytically inactive region of homology to the yeast guanylate kinase" [PMID:27205883]. The protein is therefore a multidomain interaction organizer, not a GMP kinase.

UniProt records four alternatively spliced products. The literature also describes a tumor-associated premature-polyadenylation product, MAGI3(pPA), that is truncated after intron 10. That pathological product lacks C-terminal PDZ domains and is not equivalent to a normal curated splice isoform [PMID:27205883].

## Junctional scaffold and enzyme-substrate adaptor

The first direct human characterization found MAGI3 at epithelial tight junctions, mapped PTEN binding to a MAGI3 PDZ domain, and showed that MAGI3 and PTEN cooperate to modulate AKT/PKB. The authors inferred that MAGI3 juxtaposes PTEN with phospholipid signaling pathways [PMID:10748157]. This provides direct support for a junctional molecular-adaptor role and for regulation of PI3K/AKT signaling.

An independent study identified receptor protein tyrosine phosphatase beta (PTPRB/RPTP-beta) as a MAGI3 partner. Immunofluorescence and immunoelectron microscopy placed MAGI3 at selected plasma-membrane sites, in nuclei, at epithelial tight junctions, at E-cadherin contacts, and at focal adhesions. A 130-kDa phosphoprotein was dephosphorylated by RPTP-beta only when the phosphatase retained the C-terminal sequence needed for MAGI3 binding. The paper concludes that MAGI3 links the phosphatase with its substrate at the plasma membrane [PMID:12615970]. This is a particularly close match to GO:0140767 enzyme-substrate adaptor activity.

## Receptor signaling and trafficking

MAGI3 recognizes multiple C-terminal PDZ-binding motifs and can tune signaling selectively rather than simply activating or inhibiting all pathways:

- TGFA: PDZ1 binds the pro-TGF-alpha tail. In polarized MDCK cells, MAGI3 overexpression increased basolateral TGF-alpha release, supporting efficient cell-surface trafficking [PMID:15652357].
- ADRB1: the receptor tail binds PDZ1; MAGI3 expression strongly reduced beta1-adrenergic-receptor ERK1/2 activation without changing cAMP generation or receptor internalization [PMID:16316992].
- ADRB2: the receptor tail binds PDZ5; MAGI3 expression retarded beta2-adrenergic-receptor ERK1/2 activation [PMID:20353789].
- LPAR2: the receptor tail binds PDZ5. MAGI3 depletion strongly reduced LPA-induced ERK activation, while overexpression enhanced RhoA activation in SW480 cells [PMID:16904289].
- FZD4/FZD7 and Ltap/Vangl2: mouse MAGI3 forms a ternary cell-contact complex and, with FZD4 and Ltap, activates JNK in a Rac-dependent manner [PMID:15195140].

These studies support broad regulation of signal transduction and specific ERK/JNK terms. They also show that the direction of MAGI3's effect depends on the assembled receptor complex, so neutral "regulation" is preferable for a general core statement.

## Ubiquitin-ligase substrate recognition

A 2022 full-text study reports a second, more specific adaptor mechanism in colorectal-cancer cells. MAGI3 PDZ5 directly recognizes the c-Myc C-terminal PDZ-binding motif, while PDZ2 binds SKP1. Co-immunoprecipitation detected a c-Myc-MAGI3-SKP1-CUL1 assembly; SKP1 depletion blocked MAGI3-dependent c-Myc ubiquitylation. MAGI3 expression increased K48-linked c-Myc polyubiquitylation, shortened c-Myc half-life, and promoted proteasome-dependent degradation [PMID:35864508].

The authors sometimes call MAGI3 an E3 ubiquitin ligase, but their mechanistic data place it in the substrate-recognition/bridging position rather than the catalytic center. GO:1990756 ubiquitin-like ligase-substrate adaptor activity is therefore more accurate than ubiquitin-protein transferase activity. GO:0043161 proteasome-mediated ubiquitin-dependent protein catabolic process captures the demonstrated downstream process. The normal physiological breadth of this mechanism remains to be established beyond the tested cancer models.

## Hippo/YAP regulation and disease context

Full-length MAGI3 interacts with YAP through its C-terminal PDZ6 domain and restrains YAP-dependent transformation in human mammary epithelial cells. A recurrent tumor-associated premature-polyadenylation product lacks PDZ6, binds full-length MAGI3, blocks the normal MAGI3-YAP interaction, and acts as a dominant-negative oncogenic product [PMID:27205883]. This supports a tumor-suppressive signaling role for full-length MAGI3 and demonstrates strong isoform/context dependence, but it does not establish that any normal UniProt splice isoform is oncogenic.

## Curation implications

1. Retain junctional/plasma-membrane/nuclear localizations and enzyme-substrate adaptor activity.
2. Replace broad catalytic-looking annotations: MAGI3 has no demonstrated GMP kinase activity, and GMP/GDP metabolic annotations derived from that assignment should be removed.
3. Treat generic GO:0005515 protein binding as low-information even when the underlying partner is experimentally real.
4. Represent signaling as regulation by an adaptor, with pathway-specific terms supported by direct experiments.
5. Add the c-Myc ubiquitin-ligase substrate-adaptor mechanism, while distinguishing adaptor activity from E3 catalytic activity.

