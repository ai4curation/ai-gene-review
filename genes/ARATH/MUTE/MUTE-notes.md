# MUTE (AT3G06120, Q9M8K6) — Gene Review Notes

## Identity
- *Arabidopsis thaliana* bHLH transcription factor, also known as AtbHLH45 / bHLH045 / EN20.
- 202 aa; single bHLH domain (UniProt FT DOMAIN 1..49; PROSITE PS50888 BHLH).
- Member of the FAMA/SPEECHLESS/MUTE-like subfamily (InterPro IPR044283; PANTHER PTHR46684:SF1 "TRANSCRIPTION FACTOR MUTE").
- TAIR: AT3G06120; expressed at transcript level (UniProt PE 2).

## Core biology (synthesis)
MUTE is the central of three closely related stomatal bHLH transcription factors — SPEECHLESS (SPCH) → MUTE → FAMA — that act sequentially to build stomata. MUTE terminates the amplifying (asymmetric) divisions of the meristemoid and triggers the transition of the meristemoid into a guard mother cell (GMC), which then divides once symmetrically to form the guard cell pair. MUTE functions as a nuclear, DNA-binding transcription factor that heterodimerizes with the broadly expressed ICE1/SCRM and SCRM2 bHLH-leucine-zipper proteins.

## Provenance

### Master-switch function: meristemoid → GMC transition
[PMID:17183267 "the Arabidopsis thaliana basic helix-loop-helix (bHLH) protein MUTE is a key switch for meristemoid fate transition. In the absence of MUTE, meristemoids abort after excessive asymmetric divisions and fail to differentiate stomata. Constitutive overexpression of MUTE directs the entire epidermis to adopt guard cell identity."]
[PMID:17183267 "SPCH, MUTE and FAMA bHLH proteins control stomatal development at three consecutive steps: initiation, meristemoid differentiation and guard cell morphogenesis."]

[PMID:17183265 "We demonstrate that SPCH and two paralogues are successively required for the initiation, proliferation and terminal differentiation of cells in the stomatal lineage. The stomatal bHLHs define a molecular pathway sufficient to create one of the key cell types in plants."]
- Note: PMID:17183265 abstract foregrounds SPCH but the full study (MacAlister, Ohashi-Ito & Bergmann 2007) characterizes the three paralogues; the GOA IMP annotation to GO:0010374 stomatal complex development is curator-attributed from the full text.

### Late-meristemoid expression; SLGC fate and lineage-autonomy
[PMID:23662679 "MUTE is a bHLH transcription factor that is expressed in late meristemoids and drives their transition to GMCs. Loss-of-function mute mutants are stomata-less dwarf plants with arrested lineages, in which stunted putative SLGCs surround a halted meristemoid."]
[PMID:23662679 "These results show that timely MUTE expression is essential to prevent stomatal fate in SLGCs and to promote their differentiation as pavement cells."]
- This is the basis for the GO:0090627 plant epidermal cell differentiation IMP annotation (MUTE timing affects SLGC/pavement-cell fate, not only guard cells).

### Heterodimerization with ICE1/SCRM and SCRM2 (key for MF/dimerization)
[PMID:18641265 "we identify two paralogous proteins, SCREAM (SCRM) and SCRM2, which directly interact with and specify the sequential actions of SPCH, MUTE, and FAMA."]
[PMID:18641265 "three stomatal bHLHs, SPCH, MUTE, and FAMA, that exhibit transient expression within a specific precursor state of the stomatal cell lineage function as heterodimers with broadly expressed ICE1."]
[PMID:18641265 "these nuclear-localized bHLH heterodimers most likely act as DNA binding transcription factors."]
- Full text available (PMC2518248). Establishes physical interaction (Y2H + BiFC in epidermal nuclei) of MUTE with ICE1/SCRM and SCRM2. UniProt SUBUNIT says "Homodimer {ECO:0000305}" but the experimentally supported biologically relevant partner is the SCRM/SCRM2 heterodimer; the dimerization MF annotation (GO:0046983) is therefore well supported, with heterodimerization the functional reality.

### Subcellular localization
[PMID:17183267] reported nuclear localization (UniProt SUBCELLULAR LOCATION: Nucleus, ECO:0000269|PubMed:17183267). GOA carries an IDA nucleus annotation (GO:0005634) to PMID:17183267. Heterodimers also localized to nuclei in BiFC [PMID:18641265 "showed strong heterodimerization with MUTE and FAMA in the nuclei"].

### DNA / cis-regulatory binding
- GOA IPI GO:0000976 transcription cis-regulatory region binding from PMID:30356219 (Gaudinier et al. 2018, nitrogen TF regulatory network), with/from AGI_LocusCode:AT5G07440 (= NLP7, a nitrogen-response TF). This derives from an enhanced yeast-one-hybrid promoter-TF interaction network. The abstract does not mention MUTE specifically; the network screen captured MUTE binding a promoter. Plausible (MUTE is a DNA-binding bHLH) but the in-vivo relevance to stomatal biology is not established here — treat as a real but peripheral binding observation. Keep, non-core.

### Gene-family / structural (ISS, IEA basis)
[PMID:12679534 "there are 133 bHLH genes in Arabidopsis thaliana ... Their mechanism for controlling gene transcription often involves homodimerization or heterodimerization."] — basis for ISS DNA-binding TF activity (family-level inference).
[PMID:11118137 "Arabidopsis dedicates over 5% of its genome to code for more than 1500 transcription factors"] — genome-wide TF census; only weak/background support for MUTE specifically (TF family membership). Low relevance to MUTE function.

## GO term definitions verified (QuickGO services API)
- GO:0000976 transcription cis-regulatory region binding: "the capacity to bind to a particular DNA sequence that comprises a regulatory region controlling transcription."
- GO:0010374 stomatal complex development: "The process whose specific outcome is the progression of the stomatal complex over time from its formation to the mature structure."
- GO:0010052 guard cell differentiation: "The process in which a guard mother cell acquires the specialized features of a guard cell."
- GO:0046983 protein dimerization activity: "The formation of a protein dimer, a macromolecular structure consists of two noncovalently associated identical or nonidentical subunits."

## Annotation review decisions (summary)
- GO:0003700 DNA-binding TF activity (IEA, ISS x2): ACCEPT (core MF). Sequence-specific bHLH TF.
- GO:0005634 nucleus (IEA x1, ISM, IDA): ACCEPT the IDA (PMID:17183267) as core; the IEA/ISM duplicates ACCEPT as redundant electronic support.
- GO:0006355 regulation of DNA-templated transcription (IEA): KEEP_AS_NON_CORE — correct but general; more specific BP is stomatal lineage progression. (Acceptable as-is; not the most informative.)
- GO:0010052 guard cell differentiation (IEA, InterPro): ACCEPT — directly matches MUTE's role driving meristemoid→GMC→guard cell.
- GO:0046983 protein dimerization activity (IEA): MODIFY → GO:0046982 protein heterodimerization activity (experimentally MUTE acts as heterodimer with SCRM/SCRM2 per PMID:18641265). Keep as core MF.
- GO:0090627 plant epidermal cell differentiation (IMP, PMID:23662679): ACCEPT — experimentally supported (SLGC/pavement cell fate + stomatal lineage).
- GO:0000976 transcription cis-regulatory region binding (IPI, PMID:30356219): KEEP_AS_NON_CORE — real binding observation from a large network screen, peripheral to stomatal function.
- GO:0010374 stomatal complex development (IMP, PMID:17183265): ACCEPT — core developmental process.

## GO:0046982 check
GO:0046982 = "protein heterodimerization activity" (child of GO:0046983 protein dimerization activity). Appropriate replacement given MUTE's obligate heterodimerization with ICE1/SCRM and SCRM2 (PMID:18641265).
