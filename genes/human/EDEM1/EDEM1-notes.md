# EDEM1 (Q92611) review notes

## Identity
- ER degradation-enhancing alpha-mannosidase-like protein 1 (EDEM, KIAA0212). 657 aa.
- Single-pass type II ER membrane protein (TM 5-25, signal-anchor); lumenal mannosidase-homology (GH47) domain.
- Glycosyl hydrolase 47 family member; one of three mammalian Htm1 homologues (EDEM1/2/3).

## Function (synthesis)
- Core role: extracts terminally misfolded glycoproteins (and some nonglycoproteins) from the calnexin folding cycle and accelerates their ER-associated degradation (ERAD), delivering substrates to the SEL1L/HRD1 dislocation/ubiquitination machinery [PMID:12610306 "the alpha-mannosidase I-like protein EDEM was shown to extract misfolded glycoproteins, but not glycoproteins undergoing productive folding, from the calnexin cycle"; PMID:19524542 "EDEM1 binds nonnative proteins and uses its mannosidase-like domain to target aberrant proteins to the ER membrane dislocation and ubiquitination complex containing SEL1L"].
- Substrate recognition is glycan-independent (binds nonnative protein structure), and SEL1L association requires the mannosidase-like domain [PMID:19524542 "EDEM1 specifically binds nonnative proteins in a glycan-independent manner. Inhibition of mannosidase activity with kifunensine or disruption of the EDEM1 mannosidase-like domain by mutation had no effect on EDEM1 substrate binding but diminished its association with the ER membrane adaptor protein SEL1L"].
- Catalytic activity debate: historically proposed to lack alpha-1,2-mannosidase activity (PMID:12610306 era; UniProt has a NOT mannosidase IDA from this paper). Endogenous KO analysis later showed all three EDEMs DO possess mannosidase activity; EDEM1 has the weakest activity and contributes to the second step (M8B->M7) [PMID:25092655 "all endogenous EDEMs possess mannosidase activity. Mannose trimming from Man8GlcNAc2 to Man7GlcNAc2 is performed mainly by EDEM3 and to a lesser extent by EDEM1"]. EDEM1 can also act ERAD-promotingly independent of catalysis (lectin/holdase) when overexpressed [PMID:25092655 "hEDEM1 can function in gpERAD independently of its alpha1,2-mannosidase activity, when overexpressed or up-regulated by the unfolded protein response during ER stress... likely as a lectin for substrate delivery"]. UniProt: "It has low mannosidase activity, catalyzing mannose trimming from Man8GlcNAc2 to Man7GlcNAc2."
- Mannose trimming by ERManI is required to hand off substrate from EDEM1 to the late ERAD lectin XTP3-B; EDEM1 binding itself is trimming-independent [PMID:21062743 "mannose trimming enables delivery of a substrate glycoprotein from EDEM1 to late ERAD steps through association with XTP3-B"].
- Shared pathway for glycosylated and nonglycosylated misfolded substrates; both use calnexin, EDEM1 and HRD1; substrates and ERAD machinery accumulate in the ERQC on proteasome inhibition [PMID:23233672 "makes use of calnexin, EDEM1, and HRD1"; "proteasomal inhibition induced accumulation of the nonglycosylated proteins and ERAD machinery in the endoplasmic reticulum-derived quality control compartment"; "EDEM1 associates through a region outside of its mannosidase-like domain with the nonglycosylated proteins"].
- Promotes retrotranslocation/retrograde transport from ER to cytosol; e.g. ricin A chain (like an ERAD substrate) retrotranslocation is promoted by EDEM1 (and EDEM2) [PMID:24200403 "This transport is promoted by EDEM1"; "EDEM2 is also involved in ricin retrotranslocation out of the ER"].
- Dual chaperone role for rod opsin: promotes degradation of misfolded P23H rod opsin, reduces aggregation, and can promote folding/trafficking; binding is mannose-trimming-independent [PMID:19934218 "EDEM1 binding to rod opsin was independent of mannose trimming and EDEM1 promoted the cell-surface expression of mutant rod opsin"].

## Interactions
- SEL1L (binds; requires mannosidase-like domain) [PMID:19524542].
- DERL2 and DERL3 (Derlin-2/-3); EDEM links to p97 via Derlins [PMID:16449189 "Derlin-2 and -3 are associated with EDEM and p97"].
- Rod opsin (P08100) client [PMID:19934218].

## Localization
- ER membrane (single-pass type II) [UniProt]. Concentrates in the ER-derived quality control compartment (ERQC) with ERAD machinery [PMID:23233672].

## Annotation review decisions (high level)
- ERAD pathway (GO:0036503), ER mannose trimming (GO:1904380), mannose trimming in glycoprotein ERAD (GO:1904382), ubiquitin-dependent catabolism (GO:0006511): core / accept; strongly supported.
- mannosyl-oligosaccharide 1,2-alpha-mannosidase activity (GO:0004571): the IMP enables annotation (PMID:25092655) is now supported (weak but real). ACCEPT but note weak.
- NOT mannosyl-oligosaccharide 1,2-alpha-mannosidase activity (GO:0004571, IDA, PMID:12610306): a negated experimental annotation reflecting the historical "no activity" view; the later endogenous-KO study contradicts it. Conflicting experimental annotations; keep as historical (do not REMOVE an experimental annotation on weak grounds; mark KEEP_AS_NON_CORE with note that it is superseded).
- misfolded protein binding (GO:0051787): core MF-like; EDEM1 recognizes nonnative proteins; ACCEPT.
- protein binding (GO:0005515) IPI: KEEP_AS_NON_CORE (uninformative; partners SEL1L, DERL2/3, rod opsin captured elsewhere).
- positive regulation of retrograde protein transport ER->cytosol (GO:1904154): supported by ricin study; ACCEPT/non-core.
- protein targeting to ER (GO:0045047, IMP PMID:23233672): the paper concerns ER-retained substrate targeting to ERAD, not protein import to ER. Likely a mislabel toward ERAD targeting; MARK_AS_OVER_ANNOTATED / generalize. Use UNDECIDED-style caution — keep as non-core given experimental basis but note the term is a poor fit.
- calcium ion binding (GO:0005509, IEA): GH47 fold cofactor; KEEP_AS_NON_CORE.
- carbohydrate metabolic process / membrane (generic IEA): MARK_AS_OVER_ANNOTATED in favor of ER N-glycan trimming / ER membrane.
- ER, ER membrane, ERQC localizations: accept.

## Falcon deep-research findings (incorporated 2026-06)
- The EDEM1 review already incorporated the main recent Falcon-cited papers: Chiritoiu 2020 (PMID:32423001), Katsuki 2024 turnover (PMID:38682256), Fasana 2024 ERLAD (PMID:38773321), and Christianson 2023 review (PMID:37528230). No action needed for these.
- NEW reference added: Shenkman et al. 2018 (Commun Biol, PMID:30374462) - this provides the first direct in vitro mannosidase assays for EDEM1, showing bona fide alpha-mannosidase activity that is folding-state dependent: modest on free glycans/native glycoproteins but significantly higher on a denatured glycoprotein, explaining selectivity for misfolded substrates [PMID:30374462 "activity of the EDEMs is modest on free oligosaccharides and on glycoproteins. However, mannosidase activity of ERManI and the EDEMs is significantly higher on a denatured glycoprotein"]. The EDEMs associate with oxidoreductases (PDI, TXNDC11). This complements the endogenous-KO mannosidase evidence (PMID:25092655) and was the main EDEM1-relevant primary paper missing from the review.
- Falcon's other EDEM1 content (E488Q catalytic residue, OS-9 association ~80% reduction on EDEM1 knockdown, ~3h half-life, both soluble and type II TM forms, FAM134B-dependent ERLAD rerouting) is sourced from papers already cited in the review (Shenkman 2018, Katsuki 2024, Fasana 2024); no further citation changes needed.
- PMID:30374462 added (id only, uncached) to the EDEM1 mannosidase core_function supported_by.
