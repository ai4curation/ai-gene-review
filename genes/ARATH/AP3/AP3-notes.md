# AP3 (APETALA3) — Arabidopsis thaliana — Gene Review Notes

UniProt: P35632 (AP3_ARATH), At3g54340. 232 aa MIKC-type MADS-box transcription factor.

## Identity and domain architecture

- MADS-box domain (residues 3–57), K-box domain (84–174), coiled-coil region (75–164) per UniProt FT lines. MIKC-type architecture (MADS / Intervening / Keratin-like / C-terminal).
- KW: Activator; Coiled coil; Developmental protein; Differentiation; DNA-binding; Flowering; Nucleus; Transcription; Transcription regulation.
- Member of the MADS-box / MEF2 family (InterPro IPR002100, IPR002487 K-box, IPR033896 MEF2-like_N). It is the Arabidopsis ortholog of Antirrhinum DEFICIENS (B-class).

## Core biology (B-class floral homeotic function)

AP3 is a B-class floral homeotic gene of the ABC model. Together with PISTILLATA (PI), it specifies petal (whorl 2) and stamen (whorl 3) identity. AP3 acts as an obligate heterodimer with PI; neither protein is functional alone.

- Homeotic phenotype: [PMID:2535466 "in apetala3-1, petals to sepals and stamens to carpels"]. UniProt MISCELLANEOUS: "Mutations in AP3 cause transformation of petals into sepals and stamina into carpels."
- AP3 acts later than AP2: [PMID:2535466 "the AP2 product acts at the time of primordium initiation; the AP3 product is active later"].
- AP3 + PI sufficient for B function: UniProt cites PubMed:8565821 (Krizek & Meyerowitz 1996) "The Arabidopsis homeotic genes APETALA3 and PISTILLATA are sufficient to provide the B class organ identity function." (title).

## Obligate heterodimerization with PI (central to function)

- UniProt SUBUNIT: "Forms a heterodimer with PISTILLATA, capable of binding to CArG-box sequences. AP3/PI heterodimer binds AP1 or SEP3 to form complexes."
- Dimerization specificity characterized in Riechmann, Krizek & Meyerowitz 1996 (PubMed:8643482) "Dimerization specificity of Arabidopsis MADS domain homeotic proteins APETALA1, APETALA3, PISTILLATA, and AGAMOUS." (title).
- Nuclear import depends on heterodimer: [PMID:8698240 "coexpression of AP3-GUS with PI, or PI-GUS with AP3, resulted in nuclear localization of GUS activity"] and [PMID:8698240 "Transient transformation assays of either the AP3-GUS or PI-GUS fusion protein alone resulted in cytoplasmic localization of GUS activity"]. Thus heterodimerization is upstream of and required for nuclear localization and DNA binding.

This makes protein dimerization activity (GO:0046983) a genuinely core molecular function for AP3, not a peripheral InterPro inference — obligate AP3/PI heterodimer formation is mechanistically required for all downstream activity.

## DNA binding / transcription factor activity

- AP3/PI heterodimer binds CArG-box DNA elements (UniProt SUBUNIT, above). MADS-box proteins are sequence-specific DNA-binding transcription factors that bind CArG boxes [CC(A/T)6GG], in RNA Pol II regulatory regions of target genes.
- TFDB/UniProt GO cross-refs: GO:0003700 DNA-binding TF activity (ISS:TAIR), GO:0000981 DNA-binding TF activity RNA Pol II-specific (IBA:GO_Central), GO:0000978 RNA Pol II cis-regulatory region sequence-specific DNA binding (IBA:GO_Central).
- AP3 is annotated as a transcriptional Activator (UniProt KW Activator), consistent with positive regulation of B-function target genes.

## Direct/downstream targets and regulatory role

- Activates NAP (NAC-domain) as an immediate target: UniProt FUNCTION "AP3/PI heterodimer activates the expression of NAP"; from Sablowski & Meyerowitz 1998 (PubMed:9489703) "A homolog of NO APICAL MERISTEM is an immediate target of the floral homeotic genes APETALA3/PISTILLATA" (title).
- Represses GATA factors: UniProt FUNCTION "AP3/PI prevents GATA22/GNL and GATA21/GNC expression (PubMed:18417639)" (Mara & Irish 2008). So AP3/PI both activates and represses targets — overall "regulation of transcription," with documented positive regulation of at least NAP.
- Autoregulation: UniProt FUNCTION "Forms a heterodimer with PISTILLATA that is required for autoregulation of both AP3 and PI genes." AP3 expression is initiated by AP1/LEAFY+UFO and maintained by AP3/PI autoregulatory loop.
- Higher-order (floral quartet) complexes: UniProt FUNCTION "AP3/PI heterodimer interacts with APETALA1 or SEPALLATA3 to form a ternary complex"; Honma & Goto 2001 (PubMed:11206550) "Complexes of MADS-box proteins are sufficient to convert leaves into floral organs."

## Localization

- Nucleus. IDA from PMID:8698240 (nuclear localization upon AP3+PI coexpression). UniProt SUBCELLULAR LOCATION: Nucleus. This is a real experimentally supported location, but it is conditional on heterodimerization.

## Expression / regulation (context, not core MF)

- Expressed in petals and stamens (UniProt TISSUE SPECIFICITY; original Jack et al. 1992 Cell, PubMed:1346756 title "expressed in petals and stamens").
- Positively regulated by AP1 and LEAFY with UFO (UniProt INDUCTION; PubMed:11283333). Repressed by PcG complex containing EMF1/EMF2 (PubMed:19783648).

## Assessment of existing GOA annotations

| Term | Evid | Assessment |
|------|------|-----------|
| GO:0010093 specification of floral organ identity | IMP (PMID:2535466) | ACCEPT — core; ap3 mutant homeotic transformations directly show this. |
| GO:0046983 protein dimerization activity | IEA | ACCEPT — obligate AP3/PI heterodimer is mechanistically central. |
| GO:0000978 RNA Pol II cis-regulatory region SSDNA binding | IBA | ACCEPT — CArG-box binding by AP3/PI; well-supported MF. |
| GO:0003700 DNA-binding TF activity | ISS (x2), IEA | ACCEPT (one), MARK_AS_OVER_ANNOTATED is not warranted; keep but note generic; the RNA Pol II-specific child is more precise. Keep ISS as ACCEPT/core; treat duplicate ISS and IEA reasonably. |
| GO:0006357 regulation of transcription by RNA Pol II | IBA | ACCEPT — core BP (regulatory role on Pol II targets). |
| GO:0045944 positive regulation of transcription by RNA Pol II | IEA | KEEP_AS_NON_CORE — AP3/PI activates NAP (PMID:9489703) so positive regulation is real, but AP3 also represses targets; the broad "regulation" term is the better core descriptor. |
| GO:0006355 regulation of DNA-templated transcription | IEA | KEEP_AS_NON_CORE — generic parent; Pol II-specific term preferred as core. |
| GO:0000977 RNA Pol II transcription regulatory region SSDNA binding | IEA | KEEP_AS_NON_CORE — redundant with the more specific cis-regulatory IBA term. |
| GO:0003677 DNA binding | IEA | KEEP_AS_NON_CORE — generic parent of the specific DNA-binding TF / cis-reg terms. |
| GO:0048437 floral organ development | IEA (ARBA) | KEEP_AS_NON_CORE — true but less specific than specification of floral organ identity. |
| GO:0005634 nucleus | IDA (PMID:8698240), ISM, IEA | ACCEPT (IDA) as core location; others ACCEPT/non-core duplicates. |

No annotations warrant REMOVE: all are biologically defensible. None require UNDECIDED — the experimental IMP and IDA are corroborated by UniProt-curated text, and the electronic terms are all consistent with established AP3 biology.

## Key references for reference_review

- PMID:2535466 (Bowman et al. 1989) — HIGH relevance, VERIFIED (cached abstract confirms ap3 petal->sepal, stamen->carpel transformations; basis of IMP for specification of floral organ identity).
- PMID:8698240 (McGonigle et al. 1996) — HIGH relevance, VERIFIED (cached abstract confirms AP3/PI co-expression-dependent nuclear localization; basis of IDA nucleus).
- PMID:12837945 (Parenicová et al. 2003) — MEDIUM/LOW; family-wide MADS phylogenetic survey, basis of ISS TF-activity by homology; correct citation but generic.
- PMID:11118137 (Riechmann et al. 2000) — LOW; genome-wide TF census, basis of ISS TF-activity by family membership; generic.
