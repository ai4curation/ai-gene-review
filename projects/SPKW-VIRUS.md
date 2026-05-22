# SPKW Viral Clades Subproject

**Parent project:** [SPKW.md](SPKW.md)

## Overview

This subproject extends the Swiss-Prot Keyword (SPKW) review from single-organism and term-focused analyses to viruses across multiple viral clades. The goal is to separate three different phenomena that are conflated in raw SPKW annotations:

1. **Legitimate viral biology** - terms such as virion component, viral DNA genome replication, viral envelope, host-cell entry, or latency-replication decision can be appropriate for the right viral protein.
2. **Taxon-dependent semantic mismatch** - phage proteins should not be annotated with eukaryotic innate immune response terms when the host is a bacterium.
3. **Specificity loss** - many SPKW-derived annotations are directionally correct but too broad, especially generic enzymatic functions, generic membrane/virion components, and broad host-defense suppression terms.

The bacteriophage T4 subproject, [SPKW-BPT4.md](SPKW-BPT4.md), is the first focused viral case study. This page is the virus-wide equivalent: it summarizes all viral SPKW candidates, folds in additional viral gene reviews, and defines clade-specific follow-up batches.

## Summary Statistics

Database: `~/repos/go-db/db/virus.ddb`  
Queried: 2026-05-21

| Metric | Count |
|--------|------:|
| Total virus GO annotations | 419,561 |
| Proteins with GO annotations | 75,488 |
| Viral taxa represented | 6,679 |
| SPKW annotations (GO_REF:0000043) | 180,680 |
| Proteins with SPKW annotations | 57,961 |
| Viral taxa with SPKW annotations | 6,629 |
| Naive SPKW-unique annotations | 135,117 |
| Proteins with naive SPKW-unique annotations | 54,131 |
| Closure-filtered SPKW-unique annotations | 80,218 |
| Proteins with closure-filtered SPKW-unique annotations | 42,507 |
| Closure filtering reduction | 41% |

### Distribution by Aspect

Naive SPKW-unique annotations:

| Aspect | Annotations | Proteins | Terms |
|--------|------------:|---------:|------:|
| F (Molecular Function) | 79,511 | 39,050 | 73 |
| P (Biological Process) | 34,930 | 20,799 | 192 |
| C (Cellular Component) | 20,676 | 14,876 | 32 |

Closure-filtered SPKW-unique annotations:

| Aspect | Annotations | Proteins | Terms |
|--------|------------:|---------:|------:|
| F (Molecular Function) | 39,239 | 25,050 | 68 |
| P (Biological Process) | 26,809 | 16,873 | 183 |
| C (Cellular Component) | 14,170 | 10,717 | 31 |

### Swiss-Prot vs TrEMBL

| Status | SPKW annotations | Proteins |
|--------|-----------------:|---------:|
| TrEMBL | 156,933 | 52,452 |
| Swiss-Prot | 23,747 | 5,509 |

Only 13.1% of virus SPKW annotations are on Swiss-Prot entries. This differs from human and T4, where the reviewed Swiss-Prot fraction is very high. For viruses as a whole, errors may come from either the KW->GO mapping layer or automatic keyword assignment on TrEMBL entries.

### ViralZone-Primary Keyword Stratification

ViralZone pages are integrated with UniProt keywords, but the safest machine-readable mapping is the page-header `data-about="kw:KW-####"` field, not the visible "Links / Uniprot Keyword" box. A ViralZone sitemap audit on 2026-05-21 found 147 pages with exactly one primary UniProt keyword; none of those primary keywords were reused as the primary keyword on another ViralZone page. The links box disagreed with the primary keyword on 4 pages, so this report uses the primary keyword as the ViralZone-backed mapping.

In `virus.ddb`, the SPKW rows carry the exact keyword in `with_or_from`, such as `UniProtKB-KW:KW-1113`. This lets us split SPKW annotations into **ViralZone-primary KW** annotations versus all other UniProt keyword annotations.

| SPKW set | ViralZone-primary KW annotations | Other KW annotations | ViralZone-primary share | Swiss-Prot share within ViralZone-primary | Swiss-Prot share within other KW |
|----------|---------------------------------:|---------------------:|------------------------:|------------------------------------------:|---------------------------------:|
| All SPKW annotations | 23,016 | 157,664 | 12.7% | 20.1% | 12.1% |
| Naive SPKW-unique annotations | 18,231 | 116,886 | 13.5% | 19.9% | 12.6% |
| Closure-filtered SPKW-unique annotations | 15,435 | 64,783 | 19.2% | 20.8% | 12.7% |

For ViralZone-primary keywords with UniProt GO cross-references, the observed `virus.ddb` SPKW rows matched the UniProt KW->GO mapping exactly: 0 mismatched GO IDs across ViralZone-primary SPKW rows. This supports treating the ViralZone-primary keyword set as a curated vocabulary layer rather than an accidental annotation source.

The important curation consequence is a **different prior**, not automatic acceptance. ViralZone-primary keyword rows are much less dominated by the broad high-risk terms driving the virus-wide SPKW burden. The broad terms most often flagged in this report are all from non-ViralZone-primary keywords:

| High-risk term family | ViralZone-primary rows in naive SPKW-unique set | Interpretation |
|-----------------------|-----------------------------------------------:|----------------|
| GO:0044423 virion component | 0 | Broad component keyword, not a ViralZone-primary process term |
| GO:0016787 hydrolase activity; GO:0016740 transferase activity; GO:0016779 nucleotidyltransferase activity | 0 | Generic enzyme-class keyword layer |
| GO:0000166 nucleotide binding; GO:0046872 metal ion binding; GO:0003677 DNA binding | 0 | Generic binding keyword layer |
| GO:0031640 killing of cells of another organism; GO:0042742 defense response to bacterium | 0 | Non-VZ terms; high-risk phage perspective errors |
| GO:0006260 DNA replication | 0 | Non-VZ generic process; often should be viral genome replication |
| GO:0052170 symbiont-mediated suppression of host innate immune response | 0 | Non-VZ broad parent; ViralZone-primary rows are usually pathway-specific children such as type I interferon signaling suppression |

Top ViralZone-primary naive SPKW-unique terms show the contrast:

| ViralZone page | Keyword | GO term | Naive SPKW-unique annotations | Preliminary interpretation |
|----------------|---------|---------|------------------------------:|----------------------------|
| VZ-895 Helicase | KW-0347 | GO:0004386 helicase activity | 3,792 | Often legitimate but still broad for multi-domain/polyprotein records |
| VZ-956 Viral attachment to host cell | KW-1161 | GO:0019062 virion attachment to host cell | 1,472 | Higher confidence on true attachment proteins; check protein assignment |
| VZ-3958 Viral tail protein | KW-1227 | GO:0098015 virus tail | 1,188 | Good phage structural specificity |
| VZ-3955 Viral tail assembly | KW-1245 | GO:0098003 viral tail assembly | 1,075 | Good phage assembly specificity |
| VZ-897 DNA-directed RNA polymerase | KW-0240 | GO:0000428 DNA-directed RNA polymerase complex | 920 | Usually plausible for polymerase-complex subunits; review subunit granularity |
| VZ-980 Viral genome integration | KW-1179 | GO:0044826 viral genome integration into host DNA; GO:0075713 establishment of integrated proviral latency | 821 each | Integration is often valid, but the latency fanout needs review for bacteriophages and episomal viruses |
| VZ-989 Viral penetration into host nucleus | KW-1163 | GO:0075732 viral penetration into host nucleus | 763 | Higher confidence in nuclear-replicating eukaryotic viruses; check clade biology |
| VZ-883 Inhibition of host interferon signaling pathway by virus | KW-1114 | GO:0039502 type I interferon signaling suppression | 254 | Better than broad innate immune suppression; still requires protein/mechanism review |
| VZ-3966 Restriction-modification system evasion by virus | KW-1258 | GO:0099018 symbiont-mediated evasion of host restriction-modification system | 125 | Good phage-specific replacement target for antirestriction proteins |

**Working rule:** mark ViralZone-primary KW rows as `VZ-primary` in review notes. This should raise the prior that the term is a deliberate viral biology term, especially for entry, tail, genome-ejection, immune-pathway-specific, and restriction-modification terms. It should not override gene-level review: polyprotein granularity, wrong host context, TrEMBL keyword assignment, and multi-GO fanout can still produce over-annotations.

## Top Naive SPKW-Unique Terms

| Term | Label | Annotations | Proteins | Taxa | Initial interpretation |
|------|-------|------------:|---------:|-----:|------------------------|
| GO:0044423 | virion component | 11,664 | 11,664 | 4,137 | Often true but too broad; prefer capsid, envelope, tail, virion membrane, or nucleocapsid when known |
| GO:0016787 | hydrolase activity | 11,084 | 11,084 | 4,632 | Broad MF; usually non-core when a specific hydrolase term exists |
| GO:0016740 | transferase activity | 10,128 | 10,128 | 5,253 | Broad MF; often modify/remove in favor of specific transferase activity |
| GO:0000166 | nucleotide binding | 7,595 | 7,595 | 4,713 | Broad MF; usually keep non-core or modify to ATP/GTP/nucleic-acid-specific terms |
| GO:0046872 | metal ion binding | 7,017 | 7,017 | 3,399 | High-risk generic binding annotation |
| GO:0016779 | nucleotidyltransferase activity | 5,553 | 5,553 | 4,302 | Often too broad for polymerases |
| GO:0004519 | endonuclease activity | 4,256 | 4,256 | 2,395 | Often plausible, but specificity matters |
| GO:0046718 | symbiont entry into host cell | 4,212 | 4,212 | 2,662 | Often legitimate for entry proteins, but needs protein-level mechanism |
| GO:0004386 | helicase activity | 3,792 | 3,792 | 2,484 | Likely legitimate for viral helicases |
| GO:0003677 | DNA binding | 3,192 | 3,192 | 1,742 | Usually too broad for DNA enzymes and transcription regulators |
| GO:0031640 | killing of cells of another organism | 1,845 | 1,845 | 1,357 | High-risk for phage lysis proteins; consider viral release by cytolysis |
| GO:0006260 | DNA replication | 1,788 | 1,788 | 1,003 | Often too broad; use viral DNA genome replication where appropriate |
| GO:0052170 | symbiont-mediated suppression of host innate immune response | 1,553 | 1,553 | 973 | Clade-dependent: often wrong for phage, plausible but broad for eukaryotic viruses |
| GO:0042742 | defense response to bacterium | 1,489 | 1,489 | 1,284 | High-risk semantic inversion for bacteriophage proteins |
| GO:0019062 | virion attachment to host cell | 1,472 | 1,472 | 1,367 | Often legitimate but should be restricted to attachment proteins |

## Top Viral Taxa by Naive SPKW-Unique Burden

Taxon labels and higher-level clades were resolved from NCBI Taxonomy.

| Taxon | Clade | Family | Annotations | Proteins | Terms |
|-------|-------|--------|------------:|---------:|------:|
| Yasminevirus sp. GU-2018 | Varidnaviria / Megaviricetes | Mimiviridae | 821 | 426 | 79 |
| Fadolivirus FV1/VV64 | Varidnaviria / Megaviricetes | Mimiviridae | 710 | 403 | 68 |
| Acanthamoeba polyphaga mimivirus | Varidnaviria / Megaviricetes | Mimiviridae | 556 | 259 | 61 |
| Tupanvirus soda lake | Varidnaviria / Megaviricetes | Mimiviridae | 552 | 282 | 71 |
| Bodo saltans virus | Varidnaviria / Megaviricetes | Mimiviridae | 492 | 241 | 58 |
| Megavirus chiliensis | Varidnaviria / Megaviricetes | Mimiviridae | 393 | 223 | 49 |
| Tequatrovirus T4 | Duplodnaviria / Caudoviricetes | Straboviridae | 353 | 124 | 66 |
| Vaccinia virus WR | Varidnaviria / Pokkesviricetes | Poxviridae | 342 | 125 | 65 |
| Vaccinia virus Copenhagen | Varidnaviria / Pokkesviricetes | Poxviridae | 337 | 120 | 65 |
| Acanthamoeba polyphaga moumouvirus | Varidnaviria / Megaviricetes | Mimiviridae | 336 | 181 | 57 |
| Monkeypox virus | Varidnaviria / Pokkesviricetes | Poxviridae | 325 | 117 | 64 |
| Variola virus human/India/Ind3/1967 | Varidnaviria / Pokkesviricetes | Poxviridae | 322 | 110 | 59 |
| Moumouvirus goulette | Varidnaviria / Megaviricetes | Mimiviridae | 308 | 164 | 52 |
| Cafeteria roenbergensis virus BV-PW1 | Varidnaviria / Megaviricetes | Mimiviridae | 292 | 129 | 53 |
| Fowlpox virus strain NVSL | Varidnaviria / Pokkesviricetes | Poxviridae | 253 | 102 | 53 |
| African swine fever virus BA71V | Varidnaviria / Pokkesviricetes | Asfarviridae | 247 | 94 | 63 |
| Orpheovirus IHUMI-LCC2 | Varidnaviria / Megaviricetes | Orpheoviridae | 237 | 132 | 41 |
| Yersinia phage phiYeO3-12 | Duplodnaviria / Caudoviricetes | Autotranscriptaviridae | 233 | 59 | 28 |
| Camelpox virus CMS | Varidnaviria / Pokkesviricetes | Poxviridae | 230 | 94 | 58 |
| Tetraselmis virus 1 | Varidnaviria / Megaviricetes | Allomimiviridae | 229 | 105 | 50 |

## Clade-Specific Patterns

### Bacteriophages / Caudoviricetes

**Status:** multiple reviews completed, including [SPKW-BPT4.md](SPKW-BPT4.md), Tequatrovirus genes, anti-CRISPR proteins, phage quorum-sensing, and diversity-generating retroelement proteins.

**Main pattern:** GO immune and defense terms often encode a eukaryotic-host frame that does not apply to bacterial hosts. Bacterial hosts have restriction-modification, CRISPR-Cas, abortive infection, and related anti-phage systems, not "innate immune response" in the GO immune-system sense.

**Representative decisions:**

| Gene | Taxon | SPKW term | Action | Finding |
|------|-------|-----------|--------|---------|
| DAM | Enterobacteria phage T4 | symbiont-mediated suppression of host innate immune response | REMOVE | Phage methyltransferase evades restriction-modification, not innate immunity |
| E | Enterobacteria phage T4 | defense response to bacterium | REMOVE | Phage lysozyme lyses host for viral release; not defense |
| AcrF8 | Pectobacterium phage ZF40 | symbiont-mediated suppression of host innate immune response | MODIFY | Anti-CRISPR activity should use CRISPR-Cas-specific suppression |
| darB | Tequatrovirus | methyltransferase activity | MODIFY | Use DNA-methyltransferase activity; biological role is antirestriction |
| g022 | Tequatrovirus | transferase/nucleotidyltransferase activity | REMOVE | Too broad for a DNA polymerase with viral replication role |

**Recommended replacements where supported:**

| Problem term | Better viral/phage term |
|--------------|-------------------------|
| GO:0052170 symbiont-mediated suppression of host innate immune response | GO:0099018 symbiont-mediated evasion of host restriction-modification system, or GO:0098672 symbiont-mediated suppression of host CRISPR-cas system |
| GO:0042742 defense response to bacterium | GO:0044659 viral release from host cell by cytolysis, when reviewing phage lysis proteins |
| GO:0006260 DNA replication | GO:0039693 viral DNA genome replication, if the protein directly participates in viral genome replication |

### Poxviruses / Pokkesviricetes

**Status:** not yet reviewed as full gene-review batches in this project, but high-volume candidates are present.

Poxviruses are a different case from phages. "Suppression of host innate immune response" may be biologically real for many poxviral immunomodulators, but the broad parent term can hide whether the protein blocks interferon signaling, NF-kappaB signaling, apoptosis, chemokines, complement, antigen presentation, or host-cell entry.

**High-priority terms:**

| Term | Virus-wide candidates | Interpretation |
|------|----------------------:|----------------|
| GO:0052170 symbiont-mediated suppression of host innate immune response | 1,553 | Plausible in poxviruses, but should be made pathway-specific when mechanism is known |
| GO:0046718 symbiont entry into host cell | 4,212 | Needs restriction to entry/fusion/attachment proteins |
| GO:0044423 virion component | 11,664 | Usually true but too broad |

**Priority batch:** vaccinia and monkeypox immune evasion proteins. Do not blanket-remove the immune term; review mechanism and replace with specific host-pathway child terms when available.

### Herpesviruses / Herviviricetes

**Status:** not yet reviewed as a focused SPKW batch.

Herpesviruses have real latency, host immune evasion, envelope, entry, and nuclear trafficking biology. The main expected error is not semantic impossibility, but over-generalization and missing specificity.

**Priority patterns:**

| Candidate term | Expected review action |
|----------------|------------------------|
| GO:0052170 symbiont-mediated suppression of host innate immune response | KEEP/MODIFY depending on direct mechanism |
| GO:0075713 establishment of integrated proviral latency | Check carefully; herpesvirus latency is usually episomal, not integrated |
| GO:0044826 viral genome integration into host DNA | High-risk outside integrating viruses |
| GO:0019031 viral envelope | Usually acceptable but may be non-core for non-envelope proteins |

### Giant dsDNA Viruses / Megaviricetes

**Status:** high candidate burden; no focused gene-review batch yet.

Mimiviridae and related giant-virus taxa dominate the top taxa table. Their large genomes produce many broad SPKW-derived enzymatic and structural annotations. Many will be directionally correct, but several are probably too general to retain as core function.

**Expected patterns:**

| Pattern | Example terms | Expected action |
|---------|---------------|-----------------|
| Broad enzyme class instead of specific MF | hydrolase activity, transferase activity, nucleotidyltransferase activity | MODIFY or KEEP_AS_NON_CORE |
| Broad component | virion component | MODIFY to capsid/envelope/virion membrane/tail-like component where supported |
| Generic DNA process | DNA replication, methylation | MODIFY to viral genome replication, DNA methylation, or antirestriction only when directly supported |

**Priority batch:** one Mimiviridae representative with high SPKW burden, preferably Acanthamoeba polyphaga mimivirus or Tupanvirus soda lake.

### RNA Viruses

**Status:** small-proteome viruses are underrepresented in the top virus-wide burden table but have highly specific host-interaction annotations.

The local `ZIKV.ddb` contains 85 annotations on 3 proteins, including 36 SPKW annotations on 1 protein. Naive SPKW-unique terms include viral entry, viral envelope, host JAK-STAT suppression, host type I interferon suppression, host autophagy modulation, and capping/processing terms.

**Key issue:** many RNA virus UniProt records are polyproteins. A single polyprotein entry may carry terms that apply to different mature cleavage products. Reviews should be careful not to treat every SPKW-derived term as a function of every mature protein product.

**Priority batch:** Zika virus polyprotein or mature NS proteins, with special attention to mature-product granularity.

## Reviewed Viral SPKW Annotations

Existing viral gene reviews in this repo include 11 genes and 31 SPKW-derived annotations:

| Action | Count |
|--------|------:|
| ACCEPT | 13 |
| KEEP_AS_NON_CORE | 1 |
| MARK_AS_OVER_ANNOTATED | 1 |
| MODIFY | 6 |
| REMOVE | 10 |

If MODIFY, REMOVE, and MARK_AS_OVER_ANNOTATED are counted as annotations requiring curation changes, the current viral pilot issue rate is **17/31 (55%)**.

### Reviewed Genes

| Gene | Taxon | File | Main SPKW pattern |
|------|-------|------|-------------------|
| DAM | Enterobacteria phage T4 | `genes/BPT4/DAM/DAM-ai-review.yaml` | Phage antirestriction miscast as host innate immune suppression |
| E | Enterobacteria phage T4 | `genes/BPT4/E/E-ai-review.yaml` | Phage lysis miscast as defense response to bacterium |
| frd | Enterobacteria phage T4 | `genes/BPT4/frd/frd-ai-review.yaml` | Drug target miscast as antibiotic/methotrexate response |
| darB | Tequatrovirus | `genes/9CAUD/darB/darB-ai-review.yaml` | DNA methyltransferase/antirestriction specificity |
| g022 | Tequatrovirus | `genes/9CAUD/g022/g022-ai-review.yaml` | DNA polymerase broad transferase terms removed |
| dfrP | Bacillus phage phiNIT1 | `genes/9CAUD/dfrP/dfrP-ai-review.yaml` | DHFR function mostly accepted; generic oxidoreductase removed |
| AcrF8 | Pectobacterium phage ZF40 | `genes/BPZF4/AcrF8/AcrF8-ai-review.yaml` | Anti-CRISPR should use CRISPR-Cas-specific host defense term |
| ACA2 | Pectobacterium phage ZF40 | `genes/BPZF4/ACA2/ACA2-ai-review.yaml` | RNA binding accepted; generic metal ion binding removed |
| M2 | Influenza A virus | `genes/9INFA/M2/M2-ai-review.yaml` | Ion-channel and virion-component terms modified to specific proton-channel/localization terms |
| brt | Bordetella phage BPP-1 | `genes/BPBPP/brt/brt-ai-review.yaml` | DGR reverse transcriptase function accepted |
| AimP | Bacillus phage phi3T | `genes/BPPHT/AimP/AimP-ai-review.yaml` | Latency-replication decision accepted |

## Manual Spot-Check Round 1

The virus-wide table above is only a prioritization queue. Following the strategy used in the organism-specific SPKW projects, the next step was to inspect row-level examples by term and clade, then classify whether the SPKW-derived term is likely acceptable, too broad, semantically inverted, or dependent on a specific viral host context.

This first manual pass sampled high-volume terms from `virus.ddb` on 2026-05-21:

| Sample | Rows checked | Main examples observed | Preliminary curation call |
|--------|-------------:|------------------------|---------------------------|
| Phage lysis/host-defense terms | 40 rows for GO:0042742 and 40 rows for GO:0031640 | <gene species="BPT4" symbol="E">E/P00720</gene>; gp5 (P16009); t (P06808); rI (P13304); y13J (P39503); y13K (P39504); PHI105_00120 (Q9ZXD7); R (P68920); CPL1 (P15057); gene 16 (Q8W5T9) | Systematic over-annotation or semantic inversion. Use viral release/cytolysis or entry-through-cell-wall-disruption terms, not host defense |
| Generic DNA replication | 50 rows for GO:0006260 | <gene species="9CAUD" symbol="g022">g022</gene>; <gene species="BPT4" symbol="DAM">DAM/P04392</gene>; OPG071 (P20509/P06856); OPG148 (P20995); UL30 (P04293); UL42 (P10226); UL44 (P16790); RIR1 (P08543); RIR2 (P10224); OPG180 (P20492/P16272); gp43 (P04415); gp61 (P04520) | Split by protein role. Direct replication proteins should usually be viral genome replication; nucleotide biosynthesis and methylation enzymes should not be generic DNA replication |
| Host innate immune suppression | 70 rows for GO:0052170 | <gene species="BPT4" symbol="DAM">DAM/P04392</gene>; <gene species="BPZF4" symbol="AcrF8">AcrF8</gene>; <gene species="9CAUD" symbol="darB">darB</gene>; OPG041/K3 (P20639); OPG044/K7 (P68466); A52R (P21070); OPG193 (P21004); OPG204 (P21077); ICP34.5 (P36313); US11 (P04487); TRS1 (P09695); IRS1 (P09715); UL83 (P06725); Ba71V-155 (Q65213) | Clade-specific. Often real for pox/herpes/ASFV but too broad; wrong for phage antirestriction or anti-CRISPR proteins |
| Integration and latency | 60 rows across GO:0044826 and GO:0075713 | int (P08320); 41 (G1BPP5); 69 (G1FGD4); Q9G044; PHI105_00145 (Q9T200); P30 (I7I4C5); gag-pol (P03369) | Integration is often plausible for phage integrases; "integrated proviral latency" needs careful term review for bacteriophage lysogeny |
| Virion component | 70 rows for GO:0044423 | <gene species="9INFA" symbol="M2">M2/F8IZX5</gene>; MCP (P06491/P16729); CVC1 (P10201); OPG083 (P20501); OPG086 (P68459); OPG113 (P20979); OPG102 (P21033); UL44 (P16790); ICP34.5 (P36313); gag-pol (P03369) | Often true but rarely core or sufficiently specific; modify to the structural subcomponent when known, otherwise keep as non-core |
| Broad molecular-function terms | 80 rows plus bucket counts for GO:0016740, GO:0016787, GO:0016779, GO:0000166, GO:0046872, GO:0003677 | <gene species="BPT4" symbol="DAM">DAM/P04392</gene>; <gene species="9CAUD" symbol="darB">darB</gene>; <gene species="9CAUD" symbol="g022">g022</gene>; OPG113 (P20979); OPG102 (P21033); gag-pol (P03369); rep (Q04561); int (P08320); ICP0 (P08393); gp21 (P06807); UL44 (P16790); A085R (Q84406) | Usually MODIFY to a specific MF or KEEP_AS_NON_CORE; broad binding/enzyme-class terms should not be the core function when a precise term is available |

### Sample-Level Findings

| Term pattern | Representative genes/proteins from the spot check | Manual interpretation |
|--------------|------------------------------------------------|-----------------------|
| GO:0042742 defense response to bacterium on phage lysis proteins | <gene species="BPT4" symbol="E">E/P00720</gene>; gp5 (P16009); PHI105_00120 (Q9ZXD7); R (P68920); CPL1 (P15057); e (A0A346FJK3); gene 16 (Q8W5T9); G0YQ82 | REMOVE or MODIFY. The phage is not defending against bacteria; it is lysing or penetrating its bacterial host. Use GO:0044659 viral release from host cell by cytolysis, GO:0001897 symbiont-mediated cytolysis of host cell, GO:0098932 symbiont entry into host cell via disruption of host cell wall peptidoglycan, or GO:0098994 symbiont entry into host cell via disruption of host cell envelope as appropriate |
| GO:0031640 killing of cells of another organism on phage lysis proteins | <gene species="BPT4" symbol="E">E/P00720</gene>; t (P06808); rI (P13304); y13J (P39503); y13K (P39504); gp5 (P16009); Rz (Q9XJJ6); Rz1 (Q9XJJ7); Q9ZXD8; gp25 (O48471) | MARK_AS_OVER_ANNOTATED or MODIFY. Host death is a consequence of the lysis/entry mechanism, not the most informative viral process annotation |
| GO:0006260 DNA replication on viral nucleotide-supply enzymes | RIR1 (P08543); RIR2 (P10224); UL39 (A0A7T1L7L9); UL40 (Q99BK2); gp1 (P04531); nrdJ (A0A0S0N7E1) | MODIFY away from DNA replication. The supported process is GO:0009263 deoxyribonucleotide biosynthetic process, which indirectly supports replication but is not replication machinery |
| GO:0006260 DNA replication on viral polymerases, helicases, primases, and processivity factors | <gene species="9CAUD" symbol="g022">g022</gene>; OPG071 (P20509); OPG148 (P20995); UL30 (P04293); UL42 (P10226); UL44 (P16790); gp43 (P04415); gp41 (P04530); gp45 (P04525); gp61 (P04520) | MODIFY to GO:0039693 viral DNA genome replication when the protein directly acts in genome replication; use GO:0039686 bidirectional double-stranded viral DNA replication where that level of specificity is supported |
| GO:0006260 DNA replication on DNA methyltransferases or some ligases | <gene species="BPT4" symbol="DAM">DAM/P04392</gene>; <gene species="9CAUD" symbol="darB">darB</gene>; OPG180 (P20492); OPG180 (P16272); gp30 (P00970); agt (P04519); bgt (P04547); rnh (P13319) | High-risk. Methyltransferases should be reviewed for DNA methylation/antirestriction rather than replication. Ligases need evidence for replication fork function versus repair/recombination |
| GO:0052170 symbiont-mediated suppression of host innate immune response in pox/herpes/ASFV | OPG041/K3 (P20639); OPG044/K7 (P68466); A52R (P21070); OPG193 (P21004); OPG204 (P21077); ICP34.5 (P36313); US11 (P04487); TRS1 (P09695); IRS1 (P09715); UL83 (P06725); Ba71V-155 (Q65213) | Do not blanket-remove. Often KEEP_AS_NON_CORE or MODIFY to mechanism-specific terms such as type I interferon signaling suppression, NF-kappaB pathway suppression, IRF3/TBK1 inhibition, PKR/eIF2alpha inhibition, or interferon-mediated signaling suppression |
| GO:0052170 on phage antirestriction or anti-CRISPR proteins | <gene species="BPT4" symbol="DAM">DAM/P04392</gene>; <gene species="BPZF4" symbol="AcrF8">AcrF8</gene>; <gene species="9CAUD" symbol="darB">darB</gene>; arn (P39510); stp (P62765); agt (P04519); bgt (P04547); adfA (P39229) | REMOVE or MODIFY. Use GO:0099018 symbiont-mediated evasion of host restriction-modification system or GO:0098672 symbiont-mediated suppression of host CRISPR-cas system |
| GO:0052170 on structural or core replication proteins | UL44 (P16790); UL82 (P06726); UL83 (P06725); Ba71V-060 (Q65152); Ba71V-107 (Q89424); BGLF2 (P0CK53); OPG062 (P68454) | Priority manual review. Treat as likely over-annotation unless the cited evidence directly shows immune pathway suppression by that protein |
| GO:0044826 viral genome integration into host DNA | int (P08320); gp41 (G1BPP5); gp69 (G1FGD4); Q9G044; PHI105_00145 (Q9T200); P30 (I7I4C5); gag-pol (P03369) | Often ACCEPT or KEEP_AS_NON_CORE when the protein is a bona fide integrase |
| GO:0075713 establishment of integrated proviral latency | int (P08320); gp41 (G1BPP5); gp69 (G1FGD4); Q9G044; PHI105_00145 (Q9T200); P30 (I7I4C5); gag-pol (P03369) | MODIFY or UNDECIDED pending ontology review. For bacteriophages, GO:0019042 viral latency or GO:0098689 latency-replication decision may be more appropriate than a "proviral" framing, depending on the evidence |
| GO:0044423 virion component | <gene species="9INFA" symbol="M2">M2/F8IZX5</gene>; MCP (P06491); CVC1 (P10201); MCP (P16729); OPG083 (P20501); OPG086 (P68459); OPG113 (P20979); OPG102 (P21033); UL44 (P16790); ICP34.5 (P36313); gag-pol (P03369) | MODIFY to specific CC terms when known: GO:0019028 viral capsid, GO:0019031 viral envelope, GO:0019033 viral tegument, GO:0055036 virion membrane, or another specific structural component. For packaged enzymes, keep virion-component status non-core and emphasize their enzymatic function |
| Broad MF terms on characterized enzymes | <gene species="BPT4" symbol="DAM">DAM/P04392</gene>; <gene species="9CAUD" symbol="darB">darB</gene>; <gene species="9CAUD" symbol="g022">g022</gene>; OPG113 (P20979); OPG102 (P21033); gag-pol (P03369); rep (Q04561); int (P08320); ICP0 (P08393); gp21 (P06807); UL44 (P16790); A085R (Q84406) | MODIFY to specific MF terms where available. Examples include GO:0003887 DNA-directed DNA polymerase activity, GO:0003899 DNA-directed RNA polymerase activity, GO:0009008 DNA-methyltransferase activity, GO:0009007 site-specific DNA-methyltransferase (adenine-specific) activity, GO:0015667 site-specific DNA-methyltransferase (cytosine-N4-specific) activity, GO:0004672 protein kinase activity, GO:0004674 protein serine/threonine kinase activity, GO:0004386 helicase activity, GO:0008233 peptidase activity, GO:0004518 nuclease activity, GO:0004519 endonuclease activity, or GO:0008907 integrase activity |

### Term-Level Working Rules

These are not final global edits; they are rules for the next gene-level review batches.

| SPKW-derived term | Current manual assessment | Review rule |
|-------------------|---------------------------|-------------|
| GO:0042742 defense response to bacterium | High-confidence systematic problem in phage lysis/entry proteins | Remove or replace unless there is direct evidence that the viral protein mediates defense against bacteria rather than host lysis or entry |
| GO:0031640 killing of cells of another organism | Usually over-broad for normal phage lysis-cycle proteins | Prefer viral release by cytolysis or entry/cell-wall-disruption terms; reserve killing for true toxin-like biology |
| GO:0052170 symbiont-mediated suppression of host innate immune response | Correctness depends on host and mechanism | Remove from phage antirestriction/anti-CRISPR cases; make pathway-specific in pox, herpes, ASFV, flavivirus, and influenza cases where evidence supports immune suppression |
| GO:0006260 DNA replication | Too generic for many viral proteins | Use viral genome replication for direct replication machinery; do not use for nucleotide biosynthesis, DNA methylation, or generic DNA-binding proteins |
| GO:0044423 virion component | Frequently true but too broad and often non-core | Keep as non-core or replace with a specific virion subcomponent term |
| GO:0044826 viral genome integration into host DNA | Often valid for integrases | Accept only when protein is an integrase/recombinase with host-genome integration evidence |
| GO:0075713 establishment of integrated proviral latency | Potentially misframed for bacteriophage lysogeny and wrong for episomal herpes latency | Review per clade; prefer viral latency or latency-replication decision when those terms match the biology better |
| Broad MF terms such as hydrolase activity, transferase activity, nucleotide binding, metal ion binding, DNA binding | High-volume specificity loss | Do not make core unless no better term exists; usually modify to the specific enzymatic or binding activity |

## Manual Spot-Check Round 2

The second manual pass expanded coverage beyond the highest-risk terms. It used raw SPKW counts, per-term row samples, and clade-specific profiles for poxviruses, ASFV, herpesviruses, giant dsDNA viruses, RNA viruses, retroviruses, phages, adenoviruses, papillomaviruses, and cyanophage/algal-virus auxiliary metabolism.

### Expanded Coverage

| Review slice | Terms checked by label | Representative SPKW rows reviewed | Preliminary curation call |
|--------------|------------------------|---------------------------------|---------------------------|
| Structural and entry terms | viral capsid; virion attachment; virus membrane fusion; endocytosis involved in entry; pilus attachment; procapsid maturation; phage tail assembly/fiber/baseplate; genome ejection | HSV-1 `MCP/P06491`, `CVC1/P10201`, `gB/P10211`, `gC/P10228`; HCMV `MCP/P16729`; pox `OPG099/M1LBP0`, `OPG108/A0A7H0DN80`, `OPG086/P68459`, `OPG105/P20508`; coronavirus `S/P11223`; influenza `HA/F8IZX3`; phage `III/P03663`, `A/P07394`, T4 `10/P10928`, `35/P03742`, `18/P13332`, `21/P06807` | Mostly legitimate SPKW contributions. Main risk is granularity: keep structural/process terms on the actual structural or assembly proteins, and avoid treating broad virion component as core |
| RNA-virus and retrovirus replication terms | RNA-directed RNA polymerase; RNA-directed DNA polymerase; 7-methylguanosine mRNA capping; proteolysis/peptidase; translational frameshifting; ion transport; viral budding | HIV-1 `gag-pol/P03369`; pox `OPG102/P21033`, `OPG113/P20979`, `OPG124/P20980`, `OPG083/P20501`; influenza <gene species="9INFA" symbol="M2">M2/F8IZX5</gene>; PBCV-1 `A250R/Q84568`; Megavirus `mchi_633/G5CQF3`; vesicular stomatitis `M/P08671`; arenavirus `Z/P18541`; arterivirus `rep/Q04561` | Often correct, but polyprotein granularity is a major issue. The function may belong to one mature product or domain rather than the whole precursor |
| Host-process modulation | type I interferon suppression; NF-kappaB suppression; IRF3 inhibition; JAK-STAT/STAT1 inhibition; PKR/eIF2alpha suppression; antigen presentation suppression; translation initiation suppression; host cell-cycle/apoptosis/autophagy/ubiquitin-like modification | Pox `OPG029/P17362`, `OPG041/P20639`, `OPG044/P68466`, `A52R/P21070`; HSV-1 `ICP34.5/P36313`, `US11/P04487`, `ICP0/P08393`, `US12/P03170`; HCMV `US6/P14334`, `UL44/P16790`; EBV `BNLF2a/P0C739`; ASFV `Ba71V-060/Q65152`; HPV `E7/Q30BJ2`, `E6/Q30BJ3`; arterivirus `rep/Q04561` | Many are biologically plausible in eukaryotic viruses, but they should be reviewed for direct mechanism and mature-product assignment. Structural or core replication proteins with immune terms need priority review |
| Auxiliary metabolism and photosynthesis | photosynthesis; chlorophyll binding; one-carbon metabolism; pyridine nucleotide biosynthesis; aminoacyl-tRNA ligase activity; lipid metabolism; dioxygenase activity | Cyanophage/algal-virus `psbA/A0A345AWS2`, `psbD/H6WG48`, `psaA/A0A0K0KVP2`, `psaB/A0A0K0KW31`; T4 <gene species="BPT4" symbol="frd">frd/P04382</gene>; phage `116/G1FGI1`; Megavirus `mchi_350/G5CSM6`, `mchi_737/G5CRA4`, `mchi_435/G5CT84`; T6-like `vs/A0A346FJK0`; PBCV-1 `A085R/Q84406` | Not automatically wrong for viruses. Photosystem proteins look mostly legitimate; DHFR/NAMPT/lipid/dioxygenase terms are often broad and should be replaced with specific MF or pathway terms where possible |
| Integration and latency | viral genome integration into host DNA; DNA integration; RNA-directed DNA polymerase; establishment of integrated proviral latency | HIV-1 `gag-pol/P03369`; phage lambda `int/P08320`; additional sampled phage integrase rows included `41/G1BPP5`, `69/G1FGD4`, `Q9G044`, `PHI105_00145/Q9T200`, and `P30/I7I4C5` | Viral genome integration is often correct. "Integrated proviral latency" should be accepted for retroviruses but reviewed carefully for bacteriophage integrases |

### Representative Rows Reviewed in Round 2

These rows are examples from the SPKW records inspected for this round. They are not proposed final gene reviews; they show the evidence trail behind the term-level calls.

| Slice | Taxon/clade | Gene / UniProt | Protein name | SPKW term labels checked | Manual note |
|-------|-------------|----------------|--------------|--------------------------|-------------|
| Structural | HSV-1 | `MCP/P06491` | Major capsid protein | viral capsid; T=16 icosahedral viral capsid; virion component | ACCEPT capsid; demote broad virion component if a specific capsid term is retained |
| Structural | HSV-1 | `CVC1/P10201` | Capsid vertex component 1 | viral capsid; virion component | ACCEPT/MODIFY to specific capsid vertex component if available |
| Entry | HSV-1 | `gB/P10211` | Envelope glycoprotein B | viral envelope; virion attachment; symbiont entry | Plausible entry protein; prefer fusion/entry mechanism terms when supported |
| Entry | HSV-1 | `gC/P10228` | Envelope glycoprotein C | virion attachment; adhesion receptor-mediated attachment; complement suppression | Attachment term looks strong; host complement term needs mechanism-specific evidence |
| Structural | HCMV | `MCP/P16729` | Major capsid protein | viral capsid; T=16 icosahedral viral capsid; virion component | ACCEPT capsid; broad virion component is non-core |
| Entry | Monkeypox | `OPG099/M1LBP0` | Entry-fusion complex associated protein | viral envelope; virion attachment; symbiont entry | Plausible, but entry/fusion role should be protein-specific |
| Entry | Monkeypox | `OPG108/A0A7H0DN80` | Envelope protein OPG108 | viral envelope; virion attachment; symbiont entry | Plausible attachment/envelope row |
| Entry | Vaccinia Copenhagen | `OPG086/P68459` | Entry-fusion complex protein | fusion of virus membrane with host plasma membrane; membrane fusion involved in viral entry | Stronger than generic entry; likely ACCEPT |
| Entry | Vaccinia Copenhagen | `OPG105/P20508` | Cell surface-binding protein | viral envelope; virion attachment; symbiont entry | Good candidate for attachment-specific annotation |
| Entry | Coronavirus | `S/P11223` | Spike glycoprotein | virion attachment; endocytosis involved in entry; virus-endosome membrane fusion | Plausible, but exact entry route is virus/strain dependent |
| Entry | Influenza | `HA/F8IZX3` | Hemagglutinin | virion attachment; endocytosis involved in entry; virus-endosome membrane fusion | Strong entry/fusion example; broad virion component is non-core |
| Phage entry | Filamentous phage | `III/P03663` | Attachment protein G3P | pilus attachment; receptor-mediated attachment; virion component | ACCEPT pilus attachment; this is a good SPKW contribution |
| Phage entry | RNA phage | `A/P07394` | Maturation protein A | pilus attachment; virion attachment; viral genome circularization | Pilus attachment is plausible; genome circularization needs separate evidence |
| Phage structure | T4 | `10/P10928` | Baseplate wedge protein gp10 | viral tail assembly; virus tail; tail baseplate; virion component | ACCEPT tail/baseplate terms; avoid generic virion component as core |
| Phage structure | T4 | `35/P03742` | Long-tail fiber protein gp35 | tail fiber; adhesion receptor-mediated attachment; carbohydrate binding | ACCEPT tail fiber/attachment; broad entry can be less informative |
| Phage entry | T4 | `18/P13332` | Tail sheath protein | tail sheath; genome ejection through host envelope; symbiont entry | Good phage-specific genome-ejection term |
| Phage assembly | T4 | `21/P06807` | Prohead core protein protease | viral procapsid maturation; proteolysis; peptidase activity | ACCEPT procapsid maturation; replace broad proteolysis with specific protease terms where possible |
| Retrovirus | HIV-1 | `gag-pol/P03369` | Gag-Pol polyprotein | RNA-directed DNA polymerase; DNA integration; integrated proviral latency; proteolysis; frameshifting | Retroviral integration/latency terms are expected; polyprotein/domain granularity still matters |
| Capping | Vaccinia Copenhagen | `OPG102/P21033` | Cap-specific mRNA methyltransferase | 7-methylguanosine mRNA capping; methyltransferase; methylation | Capping is plausible; broad methylation/transferase should be more specific |
| Capping | Vaccinia Copenhagen | `OPG113/P20979` | mRNA-capping enzyme catalytic subunit | mRNA capping; GTP binding; methyltransferase; nucleotidyltransferase | Strong capping enzyme; broad MF terms should be modified to specific activities |
| Capping | Vaccinia Copenhagen | `OPG124/P20980` | mRNA-capping enzyme regulatory subunit | mRNA capping; mRNA processing; transcription termination | Capping role plausible; regulatory subunit should not inherit every catalytic MF |
| Protease | Vaccinia Copenhagen | `OPG083/P20501` | Core protease | proteolysis; peptidase; cysteine-type peptidase; virion component | Specific peptidase term is better than generic proteolysis |
| Ion channel | Influenza | <gene species="9INFA" symbol="M2">M2/F8IZX5</gene> | Matrix protein 2 | ion transport; channel activity; proton transmembrane transport; virion component | MODIFY generic ion transport to proton-channel/proton-transport terms |
| Ion channel | PBCV-1 | `A250R/Q84568` | Potassium channel protein Kcv | ion transport; channel activity; ion transmembrane transport | ACCEPT channel biology; prefer potassium-specific terms |
| Ion transport | Megavirus | `mchi_633/G5CQF3` | BTB domain-containing potassium-channel-like protein | ion transport; ion transmembrane transport | Plausible only with channel evidence; generic ion transport is non-core |
| Budding | Vesicular stomatitis virus | `M/P08671` | Matrix protein | viral budding; ESCRT-mediated budding; structural constituent of virion | Budding plausible; keep as life-cycle role, not MF |
| Budding | Arenavirus | `Z/P18541` | RING finger protein Z | viral budding; ESCRT-mediated budding; zinc/metal ion binding | Budding plausible; broad metal binding is not core |
| Immune evasion | Vaccinia WR | `OPG029/P17362` | IFN signaling evasion protein | type I interferon suppression; TLR/TBK1 pathway suppression; innate immune suppression | Specific pathway terms are better than broad innate immune suppression |
| Immune evasion | Vaccinia Copenhagen | `OPG041/P20639` | Protein K3 | type I interferon suppression; PKR/eIF2alpha suppression; innate immune suppression | Strong immune-evasion example; keep specific PKR/interferon terms |
| Immune evasion | Vaccinia WR | `OPG044/P68466` | Protein K7 | NF-kappaB suppression; innate immune suppression | Plausible; prefer NF-kappaB-specific term |
| Immune evasion | Vaccinia Copenhagen | `A52R/P21070` | Protein A52 | TRAF/NF-kappaB suppression; innate immune suppression | Plausible pathway-specific immune modulator |
| Immune evasion | HSV-1 | `ICP34.5/P36313` | Neurovirulence factor ICP34.5 | type I interferon suppression; IRF3 inhibition; translation initiation suppression; autophagy suppression | Multiple host-process terms plausible but require mechanism-specific evidence |
| Immune evasion | HSV-1 | `US11/P04487` | Accessory factor US11 | type I interferon suppression; RIG-I/MDA5/TBK1 suppression; PKR/eIF2alpha suppression | Stronger than broad innate immune suppression; track exact pathway |
| Host ubiquitin/cell cycle | HSV-1 | `ICP0/P08393` | E3 ubiquitin-protein ligase ICP0 | ubiquitin-like modification; cell-cycle perturbation; viral latency; IRF3 inhibition | Plausible but broad; review per pathway and avoid treating every host consequence as core |
| Antigen presentation | HSV-1 | `US12/P03170` | ICP47 protein | adaptive immune suppression; antigen processing/presentation suppression | Low-volume, strong mechanism-specific SPKW row |
| Antigen presentation | HCMV | `US6/P14334` | Unique short US6 glycoprotein | antigen processing/presentation suppression | Low-volume, strong mechanism-specific SPKW row |
| Antigen presentation | EBV | `BNLF2a/P0C739` | Protein BNLF2a | antigen processing/presentation suppression | Low-volume, strong mechanism-specific SPKW row |
| Priority review | HCMV | `UL44/P16790` | DNA polymerase processivity factor | viral DNA genome replication; IRF3 inhibition; NF-kappaB suppression; innate immune suppression; virion component | Replication term is strong; immune terms need direct support and may be overannotations |
| Priority review | ASFV | `Ba71V-060/Q65152` | Minor capsid protein M1249L | IRF3 inhibition; innate immune suppression; virion component | Structural protein with immune terms: high-priority manual review |
| Cell cycle | HPV | `E7/Q30BJ2` | E7 protein | G1/S checkpoint perturbation; host cell-cycle progression; type I interferon suppression | Cell-cycle term plausible; immune term needs separate mechanism |
| Apoptosis | HPV | `E6/Q30BJ3` | Protein E6 | host apoptosis perturbation; innate immune suppression | Apoptosis term plausible; broad immune term needs review |
| Polyprotein risk | Arterivirus | `rep/Q04561` | Replicase polyprotein 1ab | RdRP; helicase; proteolysis; autophagy activation; JAK-STAT, PKR, NF-kappaB suppression; frameshifting | Good example of polyprotein overloading; assign to mature domains/products |
| Photosynthesis | Cyanophage/algal virus | `psbA/A0A345AWS2` | Photosystem II D1 protein | photosynthesis; chlorophyll binding; metal ion binding | Photosynthesis/chlorophyll terms look legitimate; broad binding is non-core |
| Photosynthesis | Cyanophage/algal virus | `psbD/H6WG48` | Photosystem II D2 protein | photosynthesis; chlorophyll binding; metal ion binding | Legitimate photosystem row |
| Photosynthesis | Algal virus | `psaA/A0A0K0KVP2` | Photosystem I P700 apoprotein A1 | photosynthesis; chlorophyll binding; iron-sulfur binding | Legitimate photosystem row; broad oxidoreductase should be reviewed |
| Photosynthesis | Algal virus | `psaB/A0A0K0KW31` | Photosystem I protein | photosynthesis; chlorophyll binding; iron-sulfur binding | Legitimate photosystem row; broad oxidoreductase should be reviewed |
| Auxiliary metabolism | T4 | <gene species="BPT4" symbol="frd">frd/P04382</gene> | Dihydrofolate reductase | one-carbon metabolism; oxidoreductase; methotrexate response; antibiotic response | DHFR activity is real; drug-response terms are wrong for the viral enzyme |
| Auxiliary metabolism | Phage | `116/G1FGI1` | Nicotinamide phosphoribosyltransferase | pyridine nucleotide biosynthesis; glycosyltransferase/transferase | Pathway plausible; MF should be more specific than broad transferase |
| Auxiliary metabolism | Megavirus | `mchi_350/G5CSM6` | Isoleucine--tRNA ligase | aminoacyl-tRNA ligase; ATP/nucleotide binding | Likely true aaRS; broad binding/ligase terms are non-core |
| Auxiliary metabolism | Megavirus | `mchi_737/G5CRA4` | Asparagine--tRNA ligase | aminoacyl-tRNA ligase; ATP/nucleotide binding | Likely true aaRS; broad binding/ligase terms are non-core |
| Modifier risk | T6-like phage | `vs/A0A346FJK0` | Valyl-tRNA synthetase modifier | aminoacyl-tRNA ligase activity | Likely overannotation: a synthetase modifier is not automatically a ligase |
| Lipid metabolism | Megavirus | `mchi_435/G5CT84` | PNPLA domain-containing protein | lipid metabolism; lipid catabolism; hydrolase activity | Plausible lipid enzyme, but broad lipid metabolism/hydrolase should be made specific |
| Dioxygenase | PBCV-1 | `A085R/Q84406` | Fe2OG dioxygenase domain-containing protein | dioxygenase; oxidoreductase; metal ion binding | MF plausible but broad; needs specific dioxygenase activity if known |
| Phage cell wall | Bacillus phage phi105 | `PHI105_00120/Q9ZXD7` | N-acetylmuramoyl-L-alanine amidase | cell wall organization; killing cells; defense response to bacterium; hydrolase | MODIFY to peptidoglycan catabolism or amidase activity; defense term is wrong perspective |
| Phage cell wall | Streptococcus phage | `SmphiM12_144/S5M6U0` | Murein endopeptidase K | cell wall organization; proteolysis; metallopeptidase | MODIFY to specific peptidoglycan/murein cleavage activity |
| Integration | Phage lambda | `int/P08320` | Integrase | DNA integration; viral genome integration into host DNA; integrated proviral latency | Integration likely ACCEPT; "proviral latency" is the questionable bacteriophage framing |

## Manual Spot-Check Round 3: ViralZone-Primary Keywords

This pass focused on the ViralZone-primary subset. The goal was to test whether `VZ-primary` status behaves like a useful confidence flag and to identify failure modes that remain even when the keyword is ViralZone-backed.

| VZ / KW | GO term from KW mapping | Rows in `virus.ddb` | Representative rows reviewed | What the samples showed | Preliminary curation call |
|---------|-------------------------|--------------------:|------------------------------|-------------------------|---------------------------|
| VZ-3952 / KW-1243 Viral long flexible tail ejection system | GO:0099001 symbiont genome ejection through host cell envelope, long flexible tail mechanism | 36 annotations on 36 proteins; all Swiss-Prot | `O21883`; `O21879/O21879`; `O21884/O21884`; `V/P03733`; `H/P03736`; `J/P03749` | `O21883` is a Lactococcus phage SK1 distal tail protein. UniProt states it forms the distal tail, self-associates as rings, and has a central channel allowing DNA ejection. The sampled rows are portal, tail tube, tape-measure, tail-tip, or baseplate proteins from long-tailed phages | ACCEPT the specific ejection term on tail/ejection apparatus proteins. KEEP_AS_NON_CORE or MODIFY broad `symbiont entry into host cell` and `virion component` if more specific terms are present |
| VZ-3950 / KW-1242 Viral contractile tail ejection system | GO:0099000 symbiont genome ejection through host cell envelope, contractile tail mechanism | 363 annotations on 363 proteins | `18/P13332`; `18/P13332` with virus tail sheath; related contractile-tail rows in T4-like phages | `18/P13332` is T4 tail sheath protein gp18. UniProt describes the contractile sheath and says contraction drives the central tube through the host outer membrane, creating a channel for DNA ejection | ACCEPT the contractile-tail ejection term on sheath/tube/baseplate proteins. This is a good example where VZ-primary is more precise than generic entry |
| VZ-3943 / KW-1233 Viral attachment to host adhesion receptor | GO:0098671 adhesion receptor-mediated virion attachment to host cell | 228 annotations on 228 proteins | `III/P03663` plus related filamentous/RNA phage attachment proteins | `III/P03663` is attachment protein G3P. UniProt says it mediates adsorption to the host F-pilus and subsequent entry-receptor interaction; the SPKW row also carries pilus attachment and entry-receptor attachment terms | ACCEPT specific attachment terms where receptor biology is known. Avoid making generic `symbiont entry into host cell` the main curation outcome when pilus/receptor attachment is available |
| VZ-3966 / KW-1258 Restriction-modification system evasion by virus | GO:0099018 symbiont-mediated evasion of host restriction-modification system | 128 annotations on 128 proteins | <gene species="BPT4" symbol="DAM">DAM/P04392</gene>; many TrEMBL cytosine or adenine methyltransferases | <gene species="BPT4" symbol="DAM">DAM/P04392</gene> is a T4 DNA adenine methylase. UniProt says it methylates the `GATC` motif and may prevent degradation of viral DNA by host restriction-modification antiviral defense. The VZ-primary term captures the phage-specific mechanism better than the broad innate-immune parent | ACCEPT/MODIFY to restriction-modification evasion for bona fide viral DNA methyltransferases. REMOVE the coexisting non-VZ `GO:0052170 symbiont-mediated suppression of host innate immune response` on phage proteins |
| VZ-883 / KW-1114 Inhibition of host interferon signaling pathway by virus | GO:0039502 symbiont-mediated suppression of host type I interferon-mediated signaling pathway | 492 annotations on 492 proteins | `US11/P04487` and related herpes/pox/flavivirus immune modulators | `US11/P04487` is a HSV-1 accessory factor with UniProt function text supporting PKR inhibition, RIG-I/MDA5 interaction, TBK1 destabilization, and inhibition of host immune response. However, the same entry carries many pathway-specific VZ-primary KWs plus broad DNA/RNA-binding and innate-immune terms | Usually ACCEPT pathway-specific VZ-primary immune terms when direct mechanism is present, but review term stacking. The broad non-VZ innate immune parent should not be treated as more informative than RIG-I/MDA5/PKR/TBK1/interferon-specific terms |

### VZ-Primary Working Assessment

This round supports the stratification rule above. The VZ-primary rows sampled here were mostly stronger than generic SPKW rows because they encode a viral mechanism: long-tail ejection, contractile-tail ejection, receptor attachment, restriction-modification evasion, or interferon-pathway inhibition. The remaining risks are narrower:

| Risk | Example from this round | Review response |
|------|-------------------------|-----------------|
| Broad parent co-annotation still present | `O21883` has specific GO:0099001 plus generic entry/virion terms | Keep the specific term as core; demote or replace broad parent terms |
| Non-VZ broad keyword can coexist with good VZ keyword | <gene species="BPT4" symbol="DAM">DAM/P04392</gene> has good GO:0099018 plus bad GO:0052170 | Use VZ-primary term as replacement target; remove phage innate-immune parent |
| Multiple VZ-primary immune terms can stack on one protein | `US11/P04487` carries RIG-I, MDA5, PKR, TBK1, TLR, interferon, and autophagy suppression rows | Do not blanket-accept all children; check which mechanisms are directly supported |
| VZ keyword category may not match GO aspect | KW-1243 is a UniProt "Molecular function" keyword but maps to a GO biological-process ejection term | Judge the GO term, not the UniProt keyword category label |

## Manual Spot-Check Round 4: More Granular ViralZone Terms

This pass deliberately sampled lower-level VZ-primary terms where the term name already describes a specific mechanism, substrate, host pathway component, or entry route. Counts are raw SPKW IEA rows in `virus.ddb`.

| VZ / KW | GO term from KW mapping | Rows in `virus.ddb` | Representative rows reviewed | What the samples showed | Preliminary curation call |
|---------|-------------------------|--------------------:|------------------------------|-------------------------|---------------------------|
| VZ-817 / KW-1107 Inhibition of host TAP by virus | GO:0039588 symbiont-mediated suppression of host antigen processing and presentation | 7 annotations on 7 proteins; all Swiss-Prot | `US12/P03170`; `BNLF2a/P0C739`; `US6/P14334` | `US12/P03170` binds host TAP and blocks peptide binding/translocation; `BNLF2a/P0C739` prevents TAP-mediated peptide transport; `US6/P14334` blocks TAP ATP binding and peptide translocation. These are direct host-factor inhibition proteins, not generic immune modulators | ACCEPT the TAP-specific term. The broad coannotation `GO:0039504 symbiont-mediated suppression of host adaptive immune response` is less informative and should usually be KEEP_AS_NON_CORE or replaced by antigen-processing terms |
| VZ-957 / KW-1165, VZ-976 / KW-1166, VZ-978 / KW-1167 entry-route endocytosis terms | GO:0075512 clathrin-mediated; GO:0075513 caveolin-mediated; GO:0019065 clathrin/caveolin-independent receptor-mediated endocytosis | 89, 10, and 21 annotations | `HA/P03452`; `S/P17400`; `Cap/O56129` | `HA/P03452` explicitly describes clathrin-dependent and clathrin/caveolin-independent internalization; `S/P17400` says caveolin-mediated internalization; `Cap/O56129` says clathrin-, caveolae-, and dynamin-independent entry. These rows are stronger than generic endocytosis when the route is named in the protein record | ACCEPT route-specific terms on entry proteins when the route is explicit for that virus/protein. Keep broad `endocytosis involved in viral entry` and `symbiont entry into host cell` as non-core or redundant. Do not transfer route-specific terms to structural bystanders without entry evidence |
| VZ-979 / KW-1172 Pore-mediated penetration of viral genome into host cell | GO:0044694 symbiont genome entry into host cell via pore formation in plasma membrane | 11 annotations on 11 proteins | `26/P35837`; `9/P04331`; `V/P31340`; `D18-19/Q6QGE7` | `26/P35837` is a P22 tail needle/plug protein; UniProt says host membrane perforation allows viral DNA ejection and that the needle penetrates the host outer membrane. The sampled set is tail needle, tail knob, spike, tape-measure, and selected polyprotein rows | ACCEPT on the actual pore/needle/plug apparatus. Review polyprotein rows carefully: the term may be correct for a mature product but too specific for an uncleaved polyprotein record unless product-level evidence is clear |
| VZ-3940 / KW-1236, VZ-3939 / KW-1237, VZ-3896 / KW-1238 host-envelope substrate degradation during entry | GO:0098932 peptidoglycan disruption; GO:0098995 lipopolysaccharide disruption; GO:0098996 glycocalyx disruption | 97, 8, and 133 annotations | `5/P16009`; `9/P12528`; `GP90/P49714`; `37/D1L2X0` | `5/P16009` is T4 baseplate spike gp5 with lysozyme activity for local peptidoglycan hydrolysis; `9/P12528` is P22 tail spike with O-antigen LPS endorhamnosidase activity; `GP90/P49714` is a K1 capsule depolymerase/endosialidase. The VZ terms preserve the substrate distinction that generic entry and generic hydrolase terms lose | ACCEPT the substrate-specific entry-disruption terms on enzymatic tail/spike/depolymerase proteins. MODIFY broad MF terms to specific lysozyme, endorhamnosidase, or endosialidase activities when available. REMOVE broad `killing of cells` and `defense response to bacterium` rows on these phage entry proteins |
| VZ-3964 / KW-1252 Latency-replication decision | GO:0098689 latency-replication decision | 6 annotations on 6 proteins | `aimR/O64094`; `aimP/O64095`; `cI/P03034`; `cro/P03040` | `aimR/O64094` and `aimP/O64095` are the arbitrium switch regulator/peptide pair; `cI/P03034` maintains lambda latency; `cro/P03040` promotes the lytic transition. The rows are specific switch components rather than generic latency-associated proteins | ACCEPT on switch regulators, anti-repressors, and arbitrium peptides with direct switch biology. Do not use VZ-primary status to annotate all latency proteins with the decision term |
| VZ-3963 / KW-1256 DNA end degradation evasion by virus | GO:0099016 symbiont-mediated evasion of DNA end degradation by host | 6 annotations on 6 proteins; all Swiss-Prot | `gam/P03702`; `2/P15076`; `N/P08557`; `206/Q853W0` | `gam/P03702` inhibits host RecBCD and protects viral DNA; `2/P15076` binds T4 DNA ends and protects against RecBCD degradation. These are mechanistically sharper than the broad phage innate-immune row that coexists on both examples | ACCEPT DNA-end evasion on nuclease inhibitors and DNA-end protection proteins. REMOVE or MODIFY the broad non-VZ `GO:0052170 symbiont-mediated suppression of host innate immune response` on these phage proteins |
| VZ-3962 / KW-1257 CRISPR-cas system evasion by virus | GO:0098672 symbiont-mediated suppression of host CRISPR-cas system | 3 annotations on 3 proteins; all Swiss-Prot | `orf30/Q6TM72`; `orf31/Q6TM71`; `agt/P04519` | `orf30/Q6TM72` and `orf31/Q6TM71` are named anti-CRISPR proteins; `agt/P04519` modifies T4 DNA and UniProt states the modification protects against host CRISPR-Cas9 as well as restriction systems. This is a good example where a VZ-primary term can coexist with a second precise VZ-primary antirestriction term | ACCEPT for bona fide anti-CRISPR proteins and supported DNA-modification evasion proteins. Prefer the specific CRISPR and restriction-modification evasion terms over broad adaptive/innate immune parents |
| VZ-1536 / KW-1187 Viral budding via the host ESCRT complexes | GO:0039702 viral budding via host ESCRT complex | 101 annotations on 101 proteins | `M/P08325`; `M/P03519`; `M/P16629`; `M/P08671` | `M/P08325` is a VSV matrix protein; UniProt says it recruits cellular ESCRT partners for release of budding particles. The sampled rows are mainly matrix proteins from negative-strand RNA viruses and overlap with generic viral budding and virion-component rows | ACCEPT ESCRT budding on matrix/late-domain proteins with ESCRT recruitment. Keep generic `viral budding` as a parent/non-core term when the ESCRT child is present; do not treat `virion component` as functional evidence |

### Round 4 Granularity Takeaways

| Pattern | Examples | Curation response |
|---------|----------|------------------|
| Very low-count VZ terms are often high signal | `US12/P03170`, `gam/P03702`, `orf30/Q6TM72` | Good candidates for confident ACCEPT when the UniProt function text names the host factor or defense pathway |
| Granular entry-route terms are useful but clade-sensitive | `HA/P03452`, `S/P17400`, `Cap/O56129` | Accept only when the route is explicit for that virus/protein; otherwise keep generic entry/endocytosis terms conservative |
| Substrate-specific phage entry terms fix broad-term noise | `5/P16009`, `9/P12528`, `GP90/P49714` | Prefer peptidoglycan/LPS/glycocalyx disruption plus precise MF terms over generic hydrolase, killing, or defense-response terms |
| Precise VZ terms can coexist legitimately on one protein | `agt/P04519` has CRISPR-cas evasion and restriction-modification evasion | Keep both when the mechanisms are separately supported, but demote broad adaptive/innate immune parents |

### Additional Term-Level Findings

| Term pattern | Count in raw virus SPKW | Manual interpretation |
|--------------|------------------------:|-----------------------|
| GO:0019028 viral capsid | 5,401 | Mostly ACCEPT for named capsid, coat, hexon, triplex, and capsid vertex proteins. MODIFY only when a more specific capsid subcomponent is available or when a polyprotein record obscures the mature product |
| GO:0019062 virion attachment to host cell | 1,980 | Usually legitimate for pox cell-surface binding proteins, herpes glycoproteins, phage tail fibers, and coronavirus/influenza entry proteins. Prefer specific attachment/fusion/endocytosis terms when known |
| GO:0039663 membrane fusion involved in viral entry into host cell | 583 | Stronger than the generic entry term for pox entry-fusion complex proteins and enveloped-virus fusion proteins; generally ACCEPT/MODIFY from generic entry |
| GO:0039666 virion attachment to host cell pilus | 478 | Mostly ACCEPT for filamentous/RNA phage maturation or attachment proteins such as G3P and maturation protein A |
| GO:0098003 viral tail assembly, GO:0098024 virus tail fiber, GO:0098025 virus tail baseplate | 1,190 / 173 / 163 | Good phage-specific terms for T4-like and other tailed phage structural proteins. Do not collapse these to generic virion component |
| GO:0099000 and GO:0099002 genome ejection through host envelope | 363 / 533 | Mostly plausible for tail sheath, portal, internal virion, tail needle, and peptidoglycan-disrupting proteins. Prefer these over generic host-cell entry where mechanism is known |
| GO:0046797 viral procapsid maturation | 299 | Mostly ACCEPT for prohead proteases and maturation factors; keep distinct from generic proteolysis |
| GO:0003968 RNA-directed RNA polymerase activity | 2,526 | Mostly ACCEPT for RdRP/replicase proteins. 251 rows are on polyprotein records, so mature-product granularity must be tracked |
| GO:0003964 RNA-directed DNA polymerase activity | 188 | ACCEPT for retroviral/retroelement reverse transcriptase domains; do not confuse with RNA-directed RNA polymerase |
| GO:0006370 7-methylguanosine mRNA capping | 641 | Often ACCEPT for pox capping enzyme subunits and RNA-virus replicase/capping domains; review subunit/domain specificity |
| GO:0006508 proteolysis and GO:0008233 peptidase activity | 2,639 each | Often legitimate for viral proteases, but too broad when a specific peptidase class exists. Polyprotein records need mature protease assignment |
| GO:0006811 monoatomic ion transport and GO:0034220 monoatomic ion transmembrane transport | 176 / 167 | Split by protein. Influenza M2 and Kcv-like channels should use specific ion-channel terms; polyproteins, VP2, and agnoproteins need review before accepting generic ion transport |
| GO:0046755 viral budding | 101 | Often plausible for matrix/Z proteins and some pox envelope proteins, but should be non-core for proteins whose main role is structural or enzymatic |
| GO:0044071 host cell-cycle progression and GO:0039645 G1/S checkpoint perturbation | 445 / 316 | Often plausible for HPV E7 and some herpes immediate-early proteins. High-risk on mRNA export factors, tegument proteins, or DNA processivity factors unless direct cell-cycle evidence exists |
| GO:0052150 host apoptosis perturbation | 437 | Plausible for pox apoptosis regulators and viral oncogenes. Prefer mechanism-specific regulation terms where evidence supports them |
| GO:0039657 suppression of host gene expression | 295 | Strong for virion host-shutoff proteins and known transcription/translation antagonists. 80 rows are polyprotein records, which should be reviewed at mature-product level |
| GO:0039520 activation of host autophagy | 91 | High polyprotein burden: 77/91 rows are polyprotein or replicase-like records. Treat as a priority RNA-virus granularity issue |
| GO:0039648 perturbation of host ubiquitin-like protein modification | 251 | ACCEPT/MODIFY for viral E3 ligases and tegument deneddylases; review broad assignment to polyproteins or proteins with only domain-level evidence |
| GO:0039588 suppression of host antigen processing and presentation | 7 | Low volume and mostly strong examples: herpes ICP47, HCMV US6, and EBV BNLF2a-like proteins |
| GO:0015979 photosynthesis and GO:0016168 chlorophyll binding | 123 / 117 | Mostly legitimate for viral photosystem I/II proteins such as PsbA, PsbD, and Psa subunits. Watch rare non-photosystem enzyme cases |
| GO:0006730 one-carbon metabolic process | 141 | Mostly viral DHFRs. MODIFY from broad one-carbon metabolism to GO:0004146 dihydrofolate reductase activity and GO:0046654 tetrahydrofolate biosynthetic process where supported |
| GO:0019363 pyridine nucleotide biosynthetic process | 128 | Mostly nicotinamide phosphoribosyltransferases. Likely plausible, but should be replaced with a more specific NAD salvage/biosynthesis term if available |
| GO:0004812 aminoacyl-tRNA ligase activity | 134 | Split case. True giant-virus aminoacyl-tRNA synthetases can be accepted; "valyl-tRNA synthetase modifier" proteins are not automatically aminoacyl-tRNA ligases and need review |
| GO:0071555 cell wall organization | 173 | Mostly phage amidases/autolysins. Usually MODIFY to GO:0009253 peptidoglycan catabolic process or specific activities such as GO:0008745 N-acetylmuramoyl-L-alanine amidase activity, GO:0003796 lysozyme activity, GO:0008932 lytic endotransglycosylase activity, or GO:0008933 peptidoglycan lytic transglycosylase activity |

### Clade Calls After Round 2

| Clade | Representative taxa checked | Main call |
|-------|-----------------------------|-----------|
| Poxviridae and Asfarviridae | Monkeypox, vaccinia Copenhagen/WR, variola, camelpox, ASFV BA71V | Immune-evasion terms are often real, especially type I interferon, NF-kappaB, PKR/eIF2alpha, apoptosis, and ubiquitin-like modification. Structural/capsid proteins with immune-suppression terms remain high-priority manual review |
| Herpesviruses | HSV-1/2, HCMV AD169/Merlin, EBV B95-8/AG876, HHV8, herpesvirus saimiri | Capsid/envelope terms are generally good. Host shutoff, antigen presentation, PKR, IRF3, and cell-cycle terms should be accepted only with protein-specific mechanism; latency terms should not be conflated with integration |
| Giant dsDNA viruses | Mimivirus, Megavirus, Moumouvirus, Tupanvirus, Fadolivirus, Yasminevirus, Bodo saltans virus, PBCV-1 | Main issue is specificity loss: broad hydrolase, transferase, kinase, ligase, lipid metabolism, dioxygenase, and virion component terms dominate. True auxiliary metabolic enzymes should be curated with precise MF/process terms |
| RNA viruses | Alphaviruses, coronaviruses, arteriviruses, influenza-like examples | RdRP, capping, spike/HA entry, budding, and M2-like ion-channel terms can be correct. Polyprotein records are the major risk because one UniProt entry can carry capsid, entry, protease, polymerase, channel, autophagy, and host-shutoff terms that belong to different mature products |
| Retroviruses and pararetroviruses | HIV-1/HIV-2 and related retroviral Pol/Gag-Pol samples | Reverse transcriptase, DNA integration, and integrated proviral latency are expected on Pol/Gag-Pol, but the same "proviral latency" term should not be automatically transferred to temperate phage integrases |
| Caudoviricetes and filamentous/RNA phage | T4-like phages, lambda-like integrases, filamentous pilus-attachment proteins | Phage-specific structural terms, tail assembly, genome ejection, pilus attachment, and restriction-modification evasion are good SPKW contributions. The recurring failures remain eukaryotic immune terms, defense-response inversion, and broad cell-wall/cell-killing processes |
| Cyanophages and algal viruses | Viral PsbA/PsbD/Psa proteins and PBCV-like algal-virus enzymes | Photosynthesis and chlorophyll binding are not automatically overannotations for viral genes. They look largely valid for photosystem proteins, but non-photosystem metabolic enzymes still need specificity review |

## High-Priority Virus-Wide Term Batches

| Priority | Term | Candidates | Rationale |
|----------|------|-----------:|-----------|
| 1 | GO:0052170 symbiont-mediated suppression of host innate immune response | 1,553 | Critical clade split: wrong for many phages, plausible but broad for eukaryotic viruses |
| 2 | GO:0042742 defense response to bacterium | 1,489 | Likely systematic semantic inversion for phage proteins |
| 3 | GO:0031640 killing of cells of another organism | 1,845 | Distinguish true toxins/cytolysins from viral release and normal lysis-cycle proteins |
| 4 | GO:0006260 DNA replication | 1,788 | Often too broad; compare with GO:0039693 viral DNA genome replication |
| 5 | GO:0044423 virion component | 11,664 | High-volume broad CC term; prioritize well-studied viruses where specific components are known |
| 6 | GO:0044826 viral genome integration into host DNA / GO:0075713 establishment of integrated proviral latency | 821 each | Correct for integrating viruses; high-risk for episomal latency viruses |
| 7 | GO:0046677 response to antibiotic / GO:0031427 response to methotrexate | 5 / 1 | Low-volume but clear drug-target-vs-response error in phage DHFR |
| 8 | GO:0044071 / GO:0039645 host cell-cycle perturbation terms | 442 / 119 | Valid for some viral oncogenes and immediate-early proteins; risky on structural, mRNA-export, and replication accessory proteins |
| 9 | GO:0039520 symbiont-mediated activation of host autophagy | 89 | Small but high-risk: 77/91 raw rows are polyprotein or replicase-like records |
| 10 | GO:0071555 cell wall organization | 173 | Mostly phage cell-wall hydrolases; replace with peptidoglycan catabolism or specific enzymatic activity |
| 11 | GO:0004812 aminoacyl-tRNA ligase activity | 39 | Split true viral aminoacyl-tRNA synthetases from synthetase modifier proteins |
| 12 | GO:0006811 / GO:0034220 ion transport terms | 151 / 166 | Correct for M2/Kcv-like channels, questionable on polyproteins and non-channel structural proteins |

## Query Used

```sql
-- Database: ~/repos/go-db/db/virus.ddb
-- Naive SPKW-unique viral annotations: no non-SPKW evidence for the same gene-term pair.

WITH spkw AS (
    SELECT db_object_id, db_object_symbol, db_object_taxon, ontology_class_ref, aspect
    FROM gaf_association
    WHERE supporting_references = 'GO_REF:0000043'
),
other AS (
    SELECT DISTINCT db_object_id, ontology_class_ref
    FROM gaf_association
    WHERE supporting_references != 'GO_REF:0000043'
),
naive AS (
    SELECT s.*
    FROM spkw s
    WHERE NOT EXISTS (
        SELECT 1
        FROM other o
        WHERE o.db_object_id = s.db_object_id
          AND o.ontology_class_ref = s.ontology_class_ref
    )
)
SELECT
    n.ontology_class_ref,
    tl.label,
    n.aspect,
    COUNT(*) AS annotations,
    COUNT(DISTINCT n.db_object_id) AS proteins,
    COUNT(DISTINCT n.db_object_taxon) AS taxa
FROM naive n
LEFT JOIN term_label tl ON n.ontology_class_ref = tl.id
GROUP BY n.ontology_class_ref, tl.label, n.aspect
ORDER BY annotations DESC;
```

Closure-filtered SPKW-unique annotations were also computed using `isa_partof_closure`, matching the method in [SPKW-METHODOLOGY.md](SPKW-METHODOLOGY.md). For viruses, both views are useful:

- **Naive** gives the practical review queue, especially for poorly curated viral taxa.
- **Closure-filtered** reduces redundant broad annotations and is better for prioritizing well-studied viruses with substantial non-SPKW evidence.

## Curation Recommendations for Viral SPKW

1. **Always check host biology.** Phage-bacterium interactions should not inherit eukaryotic immune terms. Use restriction-modification or CRISPR-Cas terms when that is the actual mechanism.

2. **Do not blanket-remove immune evasion terms from eukaryotic viruses.** Poxviruses, herpesviruses, flaviviruses, and influenza viruses genuinely suppress host innate immune pathways. The right action is often MODIFY to a more specific host-pathway term.

3. **Treat broad enzymatic SPKW terms as non-core unless they are the best available term.** Viral polymerases, methyltransferases, proteases, and nucleases should usually get specific MF terms.

4. **Separate viral life-cycle terms from generic cellular terms.** Prefer viral DNA genome replication over generic DNA replication when reviewing viral DNA polymerases and replication proteins.

5. **Review component terms at the correct structural level.** "Virion component" is often true but rarely sufficient. Use capsid, envelope, virion membrane, tail, nucleocapsid, or other specific CC terms where supported.

6. **Handle polyproteins explicitly.** For RNA virus polyproteins, record which mature product supports each function and avoid treating all terms as functions of the uncleaved precursor.

7. **Use ViralZone-primary keyword status as a confidence flag, not evidence by itself.** A `VZ-primary` SPKW row is less likely to be one of the generic keyword artifacts, but it still needs protein-level review. Non-VZ broad parent terms should be prioritized for cleanup.

## Next Review Batches

| Batch | Scope | Reason |
|-------|-------|--------|
| Phage immune/defense cleanup | GO:0052170, GO:0042742, GO:0031640 in Caudoviricetes | Existing reviews show systematic semantic mismatch |
| Poxvirus immune-evasion specificity | Vaccinia, monkeypox, variola candidates | High volume; likely legitimate but too broad |
| Herpesvirus latency/integration audit | GO:0044826 and GO:0075713 | Check integration vs episomal latency |
| Giant-virus specificity pilot | Mimiviridae/Tupanvirus broad MF and CC terms | Largest candidate burden in virus.ddb |
| RNA-virus polyprotein pilot | ZIKV and influenza | Tests mature-product granularity and host-defense specificity |

## Relationship to Existing SPKW Projects

| Existing project | Viral lesson carried forward |
|------------------|------------------------------|
| [SPKW-BPT4.md](SPKW-BPT4.md) | Phage host-defense terms need bacterial-host-specific replacements |
| [SPKW-PSEPK.md](SPKW-PSEPK.md) | Reverse transcriptase/defense keywords require system-level context |
| [SPKW-ECO57.md](SPKW-ECO57.md) | Distinguish true toxins from effectors and normal host manipulation |
| [SPKW-ARATH.md](SPKW-ARATH.md) | Family/clade divergence can invalidate keyword-level annotations |
| [SPKW-METHODOLOGY.md](SPKW-METHODOLOGY.md) | Use both naive and closure-filtered SPKW-unique queries depending on curation depth |
