# CYP71A13 (At2g30770, O49342) notes

## Identity and activity
- ER-anchored CYP71 P450; N-terminal TM 2-20; heme axial Cys439 (UniProt).
- Commits IAOx to camalexin: "CYP71A13 expressed in Escherichia coli converted IAOx to indole-3-acetonitrile (IAN)." and "Exogenously supplied IAN restored camalexin production in cyp71A13 mutant plants." [PMID:17573535, abstract only]
- Yeast-expressed CYP71A13 + ATR1 also makes a thiol-reactive electrophile: "These data establish that CYP71A13 catalyzes the conversion of IAOx to an electrophile capable of accepting the thiol group of L-cysteine or glutathione" [PMID:24151049]; NADPH-dependent, 18O2 incorporated into IAL ("With 97% 18O2, both CYP71A13 and CYP71A12 catalyze incorporation of the isotopic label into IAL") -> alpha-hydroxy-IAN intermediate. Reaction with IAN as substrate is ~10^3 slower, so electrophile forms mainly from IAOx directly.
- CYP79B2 + CYP71A13 + CYP71B15 reconstitute camalexin in vitro [PMID:24151049].
- No GO term for the cyanohydrin-forming oxidation; GO:0047720 (EC 4.8.1.3, RHEA:23156) is the only specific MF. Raised as a suggested question.

## Paralog
- CYP71A12 does the same chemistry but favours IAL/ICA; "CYP71A12, but not CYP71A13, is the major enzyme responsible for the accumulation of ICA" [PMID:31411742]; 4-OH-ICN made by CYP71A12, not CYP71A13 [PMID:26352477].

## Location / complex
- Metabolon: co-IP and FRET-FLIM with CYP71B15, CYP79B2; "the interaction of CYP71A13 and Arabidopsis P450 Reductase1 was observed"; GSTU4 recruited but "not directly involved in camalexin biosynthesis" [PMID:31511315, abstract only].
- GOA ER lumen IDA cites PMID:33831160, a deleted PubMed duplicate of PMID:31511315. Handled as in CYP71B15: is_invalid + replacement DUPLICATE_RECORD; row UNDECIDED (lumen conflicts with type-I P450 topology and ATR1 binding; full text unreadable). ER membrane proposed via MODIFY of membrane rows.
- Mitochondrion ISM (AtSubP) removed: likely signal-anchor artefact; ER colocalization [deep research].

## Phenotypes
- Fungal: susceptible to A. brassicicola [PMID:17573535]; no UV-C-induced resistance to B. cinerea [PMID:19154205]; post-invasive resistance to P. cucumerina / C. tropicale [PMID:31411742].
- Bacterial: cyp71A13 more susceptible to Pst [PMID:26352477]; required for Pf.SS101-induced (SA-dependent) resistance [PMID:23073694]. Kept non-core.

## Decisions
- protein binding x3 REMOVE (policy; consistent with CYP71B15).
- Iron ion binding over-annotated (heme iron).
- Curation-question 3 (necessity vs participation): CYP71A13 catalyses a pathway step, so camalexin biosynthesis is participation; defense response to fungus accepted as the physiological role of an enzyme making the antifungal compound, consistent with PAD3.
