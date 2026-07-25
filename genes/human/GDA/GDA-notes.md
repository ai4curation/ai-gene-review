# GDA (guanine deaminase / guanase / cypin / p51-nedasin) — review notes

UniProt: Q9Y2T3 (GUAD_HUMAN), 454 aa, gene GDA (HGNC:4212), chromosome 9.
EC 3.5.4.3.

## Core enzymatic function (conserved, primary)

GDA is a cytosolic, Zn2+-dependent amidohydrolase that catalyzes the hydrolytic
deamination of guanine to xanthine + ammonia — the committed step of purine base
catabolism upstream of xanthine oxidation to urate.

- Reaction / catalytic activity, from UniProt:
  [file:human/GDA/GDA-uniprot.txt "Catalyzes the hydrolytic deamination of guanine, producing"] (continues "xanthine and ammonia").
  [file:human/GDA/GDA-uniprot.txt "Reaction=guanine + H2O + H(+) = xanthine + NH4(+)"], EC=3.5.4.3, Rhea:RHEA:14665.
- Pathway (UniProt): [file:human/GDA/GDA-uniprot.txt "Purine metabolism; guanine degradation; xanthine from guanine:"] (step 1/1), UniPathway UPA00603/UER00660.
- Independent literature confirmation of the reaction and its quantitative importance:
  [PMID:22662200 "GDA catalyzes the irreversible deamination of guanine to xanthine"] and
  [PMID:22662200 "About 80% of xanthine produced in mammals occurs via guanine deamination."].
- Reactome reaction R-HSA-74255: [Reactome:R-HSA-74255 "Cytosolic guanine deaminase (GDA) catalyzes the reaction of guanine and water to form xanthine and ammonia"]; the active enzyme is a homodimer.

### Biochemical characterization (primary)
- Human enzyme cloned, expressed, purified; guanine deaminase activity with KM ~9.5 µM for guanine; ~1 zinc atom per 51-kDa monomer; dimeric native enzyme [PMID:10075721 abstract, "characterized as having guanine deaminase activity with a Km for guanine of 9.5"; "approximately 1 atom of zinc per 51-kDa monomer"]. Abstract-only cache; the curator's TAS annotations (PINC) are from the full paper.
- Structural: X-ray structures in complex with Zn and xanthine (PDB 2UZ9) and with substrate-analog valaciclovir (PDB 4AQL); homodimer [UniProt SUBUNIT: Homodimer]. Zn2+ cofactor binding residues His82, His84, Asp/…240, …330 (UniProt BINDING features). Metallo-dependent hydrolase superfamily, ATZ/TRZ family; CDD GDEase; PANTHER PTHR11271 GUANINE DEAMINASE; TIGR guan_deamin; InterPro IPR014311 Guanine_deaminase.

## Zinc cofactor
- Zn2+ is a catalytic cofactor: [file:human/GDA/GDA-uniprot.txt "Name=Zn(2+); Xref=ChEBI:CHEBI:29105"], note "Binds 1 zinc ion per subunit."
- The GO "zinc ion binding" (GO:0008270) annotations (IBA, IEA-InterPro, TAS) capture this cofactor requirement. Treated as a supporting/cofactor MF (contributes_to catalysis), not the standalone core MF (which is the deaminase activity itself).

## Moonlighting / non-core neuronal role ("cypin", "p51-nedasin", "nedasin")
- Isoform / splice variant identified as p51-nedasin, a NE-dlg/SAP102 (SAP102 = DLG3)-associated protein of the amidohydrolase superfamily; the neuronal S form binds NE-dlg/SAP102 and interferes with the NE-dlg/SAP102–NMDA receptor 2B association; expression rises with synaptogenesis [PMID:10542258 abstract, "shows identical sequences to a recently identified protein that has guanine aminohydrolase activity"; "nedasin interferes with the association between NE-dlg/SAP102 and NMDA receptor 2B in vitro"]. This underlies the TAS GO:0007399 nervous system development annotation (PINC).
- GDA is the same protein as "cypin", the major cytosolic PSD-95 (DLG4)-binding protein that regulates dendrite branching / microtubule dynamics in neurons (Akum et al. 2004; not in local cache). Independent corroboration that GDA regulates dendrite development: [PMID:22662200 "GDA is also involved in the regulation of dendrite development as a positive regulator by modulating guanine concentrations"].
- The IntAct/IPI protein-binding annotations (GO:0005515, PMID:36115835 quantitative fragmentomics) are PDZ-domain interactome mappings: GDA has a C-terminal PDZ-binding motif that binds many PDZ proteins (DLG1/DLG3/DLG4, MAGI1/2, GRIP1/2, PDZK1, SCRIB, TJP1, etc.; see UniProt INTERACTION block). These are real experimental interactions but are the moonlighting scaffold role, not the catabolic core.

Curation stance: keep the enzymatic MF/BP/CC as core (ACCEPT the well-supported ones);
keep zinc-binding as supporting cofactor MF; keep cypin/nedasin neuronal and PDZ-binding
annotations as NON-CORE (KEEP_AS_NON_CORE), never remove experimental annotations.
The PMID:36115835 abstract does not verbatim name GDA, so no verbatim quote is used for
that IPI; it is anchored to the UniProt INTERACTION data and kept as non-core.

## Annotation-by-annotation summary
- GO:0008892 guanine deaminase activity — core MF. Support: EXP PMID:22662200, TAS PMID:10075721, IBA, IEA. ACCEPT (EXP/TAS/IBA), ACCEPT redundant IEA (own correct core MF).
- GO:0006147 guanine catabolic process — core BP. IBA + IEA(UniPathway). ACCEPT.
- GO:0005829 cytosol — core CC location. IBA + TAS(Reactome). ACCEPT.
- GO:0008270 zinc ion binding — supporting cofactor MF (catalytic Zn). IBA, IEA(InterPro), TAS. ACCEPT (correct, but supporting rather than the headline MF).
- GO:0016787 hydrolase activity / GO:0016810 hydrolase acting on C-N bonds — correct but general parents of GO:0008892. MARK_AS_OVER_ANNOTATED (IEA-InterPro; superseded by the specific deaminase MF).
- GO:0005515 protein binding (IPI, PMID:36115835) — bare, uninformative; experimental. MARK_AS_OVER_ANNOTATED (do not remove); reflects the cypin/PDZ scaffold moonlighting role.
- GO:0006139 nucleobase-containing compound metabolic process (TAS PMID:10075721) — correct but very general parent of the specific guanine catabolic process. MARK_AS_OVER_ANNOTATED / MODIFY toward GO:0006147.
- GO:0007399 nervous system development (TAS PMID:10542258) — real moonlighting neuronal (nedasin/cypin) role. KEEP_AS_NON_CORE.
