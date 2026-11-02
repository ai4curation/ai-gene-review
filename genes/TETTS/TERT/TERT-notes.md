# TERT (Tetrahymena thermophila, O77448) — curation notes

> **Automated deep research was unavailable for this gene.** The `deep-research` providers
> configured in this repository could not be used (perplexity is not a registered provider;
> falcon fails authentication; openai returns `invalid_api_key`). What follows is a **manual
> literature review** compiled from the cached publications in `publications/`, the UniProt
> flat file `TERT-uniprot.txt`, and QuickGO term lookups. No file named `*-deep-research-*.md`
> was created.

## 1. Identity and architecture

- UniProt **O77448** (`TERT_TETTS`), 1117 aa, Swiss-Prot reviewed; gene `TERT` /
  `TTHERM_00112560`. EC 2.7.7.49 with experimental evidence from
  PubMed:10944124, 15696174, 16462747, 20713447 (`TERT-uniprot.txt`).
- Domain layout per UniProt features: **TEN** (1–191), **RBD/TRBD** (217–519),
  **RT** (520–887, PROSITE RT_POL 517–881), **CTE**. PANTHER `PTHR12066:SF0`
  (telomerase reverse transcriptase); InterPro IPR003545 (Telomerase_RT),
  IPR021891 (Telomerase_RBD), IPR049915 (TERT_TEN), IPR059777 (CTE_TERT).
- Structural coverage is unusually deep for a protist protein: 2B2A (TEN, 2.22 Å),
  2R4G (RBD, 1.71 Å), 5C9H (RBD–TER, 3.0 Å), and cryo-EM holoenzyme maps
  6D6V, 7LMA, 7LMB, 7UY5, 7UY6, 8GAP.

## 2. Core molecular function: the catalytic subunit of a telomerase RNP

TERT is the protein half of a ribonucleoprotein; the RNA half (TER) supplies the template.
This is explicit in the founding Tetrahymena work:

- [PMID:10944124 "The ribonucleoprotein enzyme telomerase extends chromosome ends by copying a
  specific template sequence within its integral RNA component."]
- [PMID:10944124 "Only two telomerase components are known to be essential for properly
  templated telomerase activity assayed on oligonucleotide substrates: the telomerase RNA and
  the telomerase reverse transcriptase (TERT) protein."]
- [PMID:10944124 "An active recombinant telomerase RNP is minimally composed of this RNA and
  the telomerase reverse transcriptase (TERT) protein"]

So the activity is a property of the TERT+TER pair. TERT, however, is the subunit that carries
the RT active site and that determines template use — the discriminating result of
PMID:10944124 is that single substitutions *in TERT* change template boundaries, processivity
and nucleotide selectivity:

- [PMID:10944124 "several residues in reverse transcriptase motifs 1, 2, A and D are critical
  for specific aspects of internal template use"]
- [PMID:10944124 "Our results indicate that TERT contributes directly to RNA template
  definition and the characteristics of template use."]
- The Y623A (motif A) substitution destroys deoxy/ribo discrimination:
  [PMID:10944124 "We conclude that the major qualitative change in activity of the Class 5
  enzyme derives from a loss of dNTP/rNTP selectivity."]

Catalytically this is an RNA-templated DNA polymerase (EC 2.7.7.49; Rhea:RHEA:22508 per
`TERT-uniprot.txt`), but one whose template is internal — which is exactly the distinction GO
captures with `GO:0003720 telomerase activity` (def.: "...using an internal RNA template that
encodes the telomeric repeat sequence", QuickGO). `GO:0003964` and `GO:0034061` are its
ancestors (QuickGO ancestor query), i.e. true but entailed.

## 3. Nucleic-acid binding by TERT

**Telomerase RNA (TER).** The TRBD is the high-affinity TER-binding module, and the TEN domain
adds non-sequence-specific RNA contact:

- [PMID:23552895 "Two TER regions, loop 4 (L4) next to the p65 "] xRRM2 interaction site and
  the TERT high-affinity binding element (TBE) 5′ to the template bind the TERT TRBD (the
  sentence continues past the quotable ASCII run).
- [PMID:16462747 "The positively charged C terminus, which becomes ordered upon interaction
  with other macromolecules, is involved in binding RNA in a non-sequence-specific manner."]
- [PMID:26472759 "This study reveals the paths of TER in the TERT-TER-p65 catalytic core and
  single-stranded DNA exit"]

**Telomeric DNA.** Importantly, what TERT binds is the *single-stranded* 3′ telomeric primer,
not duplex telomeric repeat DNA. The TEN crystal structure paper is explicit:

- [PMID:16462747 "These residues are crucial for telomerase catalytic activity, and several of
  them are required for sequence-specific binding of a single-stranded telomeric DNA primer."]

This is the basis for proposing `GO:0043047 single-stranded telomeric DNA binding`
(a child of `GO:0042162 telomeric repeat DNA binding`, QuickGO) in place of the parent term.

## 4. The Tetrahymena holoenzyme — which parts are TERT's

The composition is *Tetrahymena*-specific and must not be read off human telomerase. From the
cached primary literature:

- Catalytic core = TERT + TER + **p65/TAP65** (a La-family protein):
  [PMID:23552895 "Three of these subunits are required for in vivo assembly of a catalytically
  active RNP: TERT, TER, and the La-family protein p65"]
- Seven (later nine) reciprocally co-purifying subunits, each needed for telomere maintenance:
  [PMID:19941821 "Each of seven telomerase proteins is required for telomere maintenance and
  copurifies active RNP."]
  [PMID:19941821 "The catalytic core (p65-TER-TERT) is assembled with a three-protein
  subcomplex (p75-p45-p19) and two peripheral subunits (p82 and p50)."]
- p75-p45-p19 was later identified as a **CST** (CTC1-STN1-TEN1) paralog, and Teb1 as part of
  an RPA paralog **TEB**:
  [PMID:26472759 "The p75-p45-p19 subcomplex is identified as another RPA-related complex, CST
  (CTC1-STN1-TEN1)."]
  [PMID:26472759 "we identify two additional proteins that form a complex (TEB) with
  single-stranded telomere DNA-binding protein Teb1, paralogous to heterotrimeric replication
  protein A (RPA)"]
- Architecture: TERT sits at the centre; p50 is the hub to 7-1-4 and Teb1:
  [PMID:23552895 "Fitting with high-resolution structures reveals the organization of TERT,
  TER and p65 in the ribonucleoprotein (RNP) catalytic core."]
  [PMID:23552895 "The TERT TRBD, RT domain, and C-terminal extension (CTE) form a ring that
  encircles an active site cavity"]
  [PMID:26472759 "extensive subunit interactions of the TERT essential N-terminal domain, p50,
  and TEB"]

**Division of labour that matters for annotation.** High repeat-addition processivity and the
tether to the chromosome end are supplied by Teb1/p82 and p50, *not* by TERT:
[PMID:19941821 "DNA-interacting subunits other than telomerase reverse transcriptase (TERT)
and telomerase RNA (TER) have been hypothesized to account for high repeat addition
processivity of telomerase holoenzyme compared to the minimal catalytic RNP."] and
[PMID:23552895 "reveals the organization of holoenzyme subunits that confer processivity and
bridge telomerase to telomeres"]. So processivity-specific or telomere-recruitment-specific
terms belong to those subunits, not to TERT.

## 5. p65/TAP65 relationship (reviewed in parallel; do not duplicate here)

p65 is an assembly/architectural factor acting on TER, upstream of and within the RNP:

- [PMID:15696174 "The telomerase reverse transcriptase (TERT) and telomerase RNA (TER) alone
  can assemble into active enzyme in a heterologous cell extract"] — i.e. p65 is dispensable
  *in vitro* in rabbit reticulocyte lysate but required *in vivo*.
- [PMID:15696174 "These findings demonstrate that in the presence of TER, p65 and TERT
  associate to form a ternary complex."] — the p65–TERT association is **TER-bridged**, not a
  direct protein–protein interaction.
- [PMID:15696174 "Coassembly of p65 did not affect the primer-extension activity of
  T. thermophila TERT reconstituted with TER in RRL"] — p65 does not add catalytic activity.
- [PMID:20713447 "the binding of p65 to stems I and IV of telomerase RNA (TER) causes a
  conformational change that facilitates the subsequent binding of telomerase reverse
  transcriptase (TERT) to TER"]
- [PMID:20713447 "p65 acts as a molecular buttress within the assembled RNP, mutually
  stabilizing TER and TERT in catalytically active conformations"]
- [PMID:20713447 "Several TER mutants exhibited telomerase activity only in the presence of
  p65"]

Annotation consequence: both TERT and p65 are legitimately `part_of GO:0000333 telomerase
catalytic core complex` and `part_of GO:0005697 telomerase holoenzyme complex`. The
*catalytic* MF (`GO:0003720`) is TERT's, not p65's.

## 6. What is NOT supported in Tetrahymena (guard against human-telomerase import)

The following are well known for human TERT but have **no** support in the cached Tetrahymena
literature and must not be annotated here:

- Shelterin (TRF1/TRF2/TIN2/TPP1/POT1/RAP1) components and TPP1/POT1-mediated recruitment.
  Tetrahymena uses p50 + the TEB (RPA-paralog) and CST-paralog modules instead
  ([PMID:26472759], [PMID:23552895]).
- Cajal body / nuclear body localisation and TCAB1-dependent trafficking — no Tetrahymena data
  in the cached set.
- Dyskerin/H-ACA RNP biogenesis — Tetrahymena TER biogenesis uses p65, explicitly contrasted
  with dyskerin in [PMID:15696174].
- Senescence, cancer, ALT, extra-telomeric/mitochondrial TERT functions, and transcriptional
  regulation of TERT — none assayed in Tetrahymena in these papers.

## 7. Localisation

UniProt records `Nucleus {ECO:0000255|RuleBase:RU365061}` and `Chromosome, telomere
{ECO:0000255|RuleBase:RU365061, ECO:0000269|PubMed:16462747}` (`TERT-uniprot.txt`). Both are
biologically sound — telomerase acts on nuclear chromosome ends — but the Tetrahymena-specific
support is indirect (telomeric primer binding and *in vivo* telomere maintenance requirement
rather than a microscopy or ChIP experiment in the cached set). Note that *Tetrahymena* has two
nuclei; GO has `GO:0031039 macronucleus` and `GO:0031040 micronucleus`, and the cached papers
do not distinguish which compartment was assayed, so the generic `GO:0005634 nucleus` is as
precise as the available evidence allows. This is raised as a suggested question rather than
acted on.

## 8. Review decisions (summary)

| GO term | Action | Why |
|---|---|---|
| GO:0003720 telomerase activity (4 IDA + 1 IEA) | ACCEPT | The defining function; EC 2.7.7.49 with four experimental references |
| GO:0005697 telomerase holoenzyme complex (5 IDA) | ACCEPT | Directly demonstrated by purification, EM and cryo-EM |
| GO:0000333 telomerase catalytic core complex (IEA) | ACCEPT | TERT+TER+p65 core is the structurally defined unit |
| GO:0007004 telomere maintenance via telomerase (IDA + IEA) | ACCEPT | The process TERT executes |
| GO:0070034 telomerase RNA binding (IDA + IEA) | ACCEPT | TRBD/TEN–TER contacts, structurally resolved |
| GO:0000781 chromosome, telomeric region (IEA) | ACCEPT | Site of action; holoenzyme is bridged to telomeres |
| GO:0005634 nucleus (IEA) | ACCEPT | Correct and as precise as the evidence allows |
| GO:0042162 telomeric repeat DNA binding (IDA + IEA) | MODIFY → GO:0043047 | TERT binds the *single-stranded* 3′ primer |
| GO:0034061 DNA polymerase activity (4 EXP + 1 IEA) | TOO_GENERAL | Strict ancestor of the accepted GO:0003720 |
| GO:0003964 RNA-directed DNA polymerase activity (IEA) | TOO_GENERAL | Strict ancestor of GO:0003720 |
| GO:0003677 DNA binding (IEA) | TOO_GENERAL | Strict ancestor of the telomeric DNA-binding term |
| GO:0000723 telomere maintenance (IEA) | TOO_GENERAL | Strict ancestor of the accepted GO:0007004 |

No `NEW` rows were proposed. The obvious candidates were tested and rejected:

- *"telomerase holoenzyme complex assembly" (GO:1905323)* — TERT is the thing being assembled;
  the assembly work is done by p65 ([PMID:20713447 "p65 acts as a molecular buttress within the
  assembled RNP, mutually stabilizing TER and TERT in catalytically active conformations"]).
  Being required for and consumed by an assembly process is not participation in it.
- *processivity / telomere-recruitment terms* — the cached literature assigns these to Teb1,
  p82 and p50, explicitly in contrast to TERT ([PMID:19941821], [PMID:23552895]).
- *`GO:0000287 magnesium ion binding`* — UniProt carries the `Magnesium`/`Metal-binding`
  keywords but the metal-binding residues in the flat file are not backed by a Tetrahymena
  experimental reference, so no id is asserted.

No new GO term is needed: `GO:0003720` already encodes the internal-template distinction that
makes telomerase special, so `proposed_new_terms` is empty.
