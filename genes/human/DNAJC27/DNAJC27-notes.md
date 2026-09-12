# DNAJC27 (RBJ / RABJS) research notes

## Identity
- UniProt Q9NZQ0 (DJC27_HUMAN), 273 aa. HGNC:30290. Synonyms RABJS, RBJ. "Rab and DnaJ domain-containing protein".
- Chimeric protein: N-terminal Ras/Rab-like small-GTPase (P-loop NTPase) domain + C-terminal J domain (residues 217-273). Member of the RJL family (Ras-related + J-domain-like).

## Function
- GTPase that can activate the MEK/ERK pathway and induce cell transformation when overexpressed; may act as a nuclear scaffold for MAPK1/ERK2.
  [UniProt FUNCTION (by similarity to mouse Q8CFP6): "GTPase which can activate the MEK/ERK pathway and induce cell transformation when overexpressed. May act as a nuclear scaffold for MAPK1..."]
- RBJ mediates nuclear entrapment of MEK1/MEK2 and prolongs ERK1/2 activation, promoting gastrointestinal carcinogenesis.
  [PMID:24746703 "Nucleus-localized RBJ interacts with MEK/ERK and prolongs the duration of MEK/ERK activation."]
- Interacts directly with MAPK1 (N-terminal region 1-18 required) and with MAP2K1/MEK1 in GTP-bound form (UniProt SUBUNIT).

## GTPase caveat (important)
- The RJL family lacks the conserved catalytic glutamine that coordinates GTP hydrolysis in canonical Ras-superfamily GTPases.
  [PMID:14980719 "RJLs lack classical membrane targeting signals and the conserved glutamine residue that coordinates GTP hydrolysis in other proteins from the Ras superfamily."]
- UniProt reference [5] is annotated "IDENTIFICATION, AND POSSIBLE LACK OF GTPASE ACTIVITY." So GTP binding is supported but catalytic GTPase activity is doubtful — the IBA/IEA "GTPase activity" annotations are likely over-annotations; "GTP binding" is on firmer ground.

## J domain / Hsc70
- The C-terminal J domain is predicted to recruit Hsc70/HSP70.
  [PMID:14980719 "chordate orthologues are chimeras fused to 'J' domains in their C-terminal, suggesting that these proteins recruit Hsc70 to specific sites in the cell."]
- Original cloning ref (Chen et al. 2002, submitted) titled "a unique Rab GTPase containing a J domain that interacts with Hsc70." However, no detailed experimental characterization of canonical HSP70 co-chaperone (ATPase-stimulating) activity for human DNAJC27 is established.

## Localization
- Nucleus (by similarity to mouse; ISS). IEA also cytoplasmic vesicle (ARBA) and organelle membrane — weakly supported / generic.
- Tissue enhanced in testis (HPA); overexpressed in GI cancers (PMID:24746703).

## Interactome
- TFCP2 (Q12800) is the only curated IPI partner, from two large interactome screens (PMID:25416956 Y2H proteome map; PMID:32296183 HuRI binary interactome). Bare protein binding; not clearly tied to RBJ's MEK/ERK function.

## GO annotation review reasoning
- GTP binding (IEA, InterPro) — ACCEPT (P-loop, GTP-binding motifs present; KW GTP-binding).
- GTPase activity (IBA/IEA) — likely over-annotated given lack of catalytic glutamine; MARK_AS_OVER_ANNOTATED.
- nucleus (ISS/IEA) — ACCEPT (functionally relevant; nuclear MEK/ERK scaffold).
- positive regulation of ERK1 and ERK2 cascade (IEA from mouse ortholog) — ACCEPT/core; this is the best-characterized function.
- cytoplasmic vesicle / organelle membrane (IEA ARBA) — weakly supported, KEEP_AS_NON_CORE or over-annotated.
- protein binding (IPI, TFCP2) — KEEP_AS_NON_CORE (uninformative bare term).
- Core MF: this protein is best described as a J-domain GTP-binding scaffold acting in MEK/ERK signaling. No clean MF GO term beyond GTP binding; for biological process, positive regulation of ERK1/ERK2 cascade is core.
