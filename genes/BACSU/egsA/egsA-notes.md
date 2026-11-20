# egsA (araM, yseB; BSU28760; P94527) notes

## Provenance of this review

- No deep-research provider key was available for this session, so no
  `egsA-deep-research-*.md` file exists.
- `just mod-description-deep-research BACSU egsA` was run and skipped:
  "no MOD provider configured for organism 'BACSU'". There is no MOD
  description file.
- Literature search (PubMed via MCP, 2026-11-02):
  `(heptaprenylglyceryl OR PcrB OR AraM OR "glycerol-1-phosphate dehydrogenase") AND Bacillus`
  returned 11 hits; the relevant ones are PMID:18558723, PMID:9084180,
  PMID:22614947, PMID:23322418, PMID:27226549, PMID:35767906 and
  PMID:40626731. Also read: PMID:10417639 (AraR), PMID:42286214 (Rieche 2026,
  full text), PMID:21761520 (abstract only).
- Full text was not available for PMID:18558723 (Guldan 2008), PMID:21761520
  (Guldan 2011) or PMID:27226549 (Linde 2016, PMC4938202; the PMC and Europe
  PMC full-text services returned no body text). What the araM knockout in
  Guldan 2008 actually showed could therefore not be checked.

## Enzyme activity (well supported)

- Recombinant AraM is a homodimeric, Ni2+-dependent G1P dehydrogenase
  [PMID:18558723 "the purified protein forms a homodimer that reversibly reduces
  dihydroxyacetone phosphate (DHAP) to glycerol-1-phosphate (G1P) in a
  NADH-dependent manner"].
- Kinetics favour the reductive (biosynthetic) direction: UniProt, from
  PMID:18558723, gives KM 8.1 uM for DHAP and 16 uM for NADH, versus 1370 uM
  for G1P [file:BACSU/egsA/egsA-uniprot.txt "KM=1370 uM for G1P"].
- Cofactor: prefers NADH; NADPH also used [UniProt "Prefers NADH over NADPH as
  coenzyme."]. Ni2+ only; no activity with Zn2+, Mg2+, Mn2+ etc. Strictly G1P,
  not G3P, in the reverse direction.
- Soluble, no TM segment; UniProt cytoplasm is a curator inference
  (ECO:0000305).

## In vivo role: what is and is not shown

- Guldan 2008 propose a lipid role from the enzymology plus an araM knockout
  [PMID:18558723 "On the basis of these findings and the analysis of an araM
  knockout mutant, we propose that AraM generates G1P for the synthesis of
  phosphoglycerolipids in Gram-positive bacterial species"]. The knockout data
  are not visible in the cached abstract.
- Guldan 2011 [PMID:21761520] show PcrB makes heptaprenylglyceryl phosphate
  (HepGP) from G1P in Bacillales; Linde 2016 [PMID:27226549] name G1PDH and
  HepGP synthase as "the key enzymes" of bacterial ether lipid synthesis. This
  makes EgsA the only known source of G1P for PcrB in B. subtilis, but I found
  no accessible data showing that an egsA deletion abolishes HepG/Ac-HepG.
- Komazin 2025 [PMID:40626731] screened a transposon library for loss of
  lipoprotein N-acetylation (which needs the PcrB product Ac-HepG). Hits were
  pcrB, yvoF and ypjA (plus lgt/lsp); egsA was not reported among them. The
  screen was in LB and need not be saturating, so this is not evidence against
  EgsA supplying G1P, but it does leave open whether another G1P source exists
  in vivo. My inference, not a claim of that paper.
- Rieche 2026 [PMID:42286214] note that in engineered E. coli "other
  mechanism(s) of G1P biosynthesis must exist in E. coli and possibly other
  bacteria, as archaeal lipids with the correct chiral structure could be
  produced even in the absence of AraM (Caforio et al, 2018)".
- G1P-backbone PG: Palyzová 2022 [PMID:35767906] detected both G1P and G3P
  (about 1:4) in B. subtilis and both enantiomers in the backbone of some PG
  species. Nobody has shown that this G1P comes from EgsA (no egsA mutant
  lipidomics). Knowledge gap, not an annotation.

## Arabinose operon context

- egsA/araM is the 5th gene of the araABDLMNPQ-abfA operon, induced by
  L-arabinose and repressed by glucose and AraR [PMID:9084180;
  PMID:10417639].
- It is not needed for arabinose use [PMID:9084180 "araL, araM, araN, araP,
  araQ and abfA are not essential for L-arabinose utilization"]. There is no
  biochemical link between G1P/DHAP chemistry and arabinose catabolism, and no
  arabinose-related GO term is proposed. Why a lipid-precursor enzyme is
  co-regulated with arabinose catabolism is unknown (knowledge gap).

## Annotation decisions (summary)

- GO:0050492 G1PDH [NAD(P)+] IEA: ACCEPT (core; EC 1.1.1.261 term fits a
  dual-cofactor enzyme).
- GO:0106357 G1PDH (NAD+) IEA: ACCEPT (physiological, preferred cofactor).
- GO:0106358 G1PDH (NADP+) IEA: KEEP_AS_NON_CORE (secondary cofactor).
- GO:0005737 cytoplasm IEA: ACCEPT.
- GO:0006650 glycerophospholipid metabolic process IEA: MODIFY to GO:0046474
  glycerophospholipid biosynthetic process (the enzyme runs in the reductive,
  G1P-forming direction; G1P feeds HepGP, which is itself a glycerophospholipid).
  Not GO:0008611 ether lipid biosynthesis: G1P may also feed ester-linked
  G1P-PG, and the ether bond is made by PcrB.
- Ontology gap: no GO term for sn-glycerol 1-phosphate biosynthesis (there is
  GO:0046167 glycerol-3-phosphate biosynthetic process). Proposed as new term.

## Review pass 2026-11-06: resolving the GO:0006650 question

The earlier plan justified `MODIFY GO:0006650 -> GO:0046474` with "G1P feeds
HepGP, which is itself a glycerophospholipid". That reason is not usable: the
same notes record that no egsA-deletion lipidomics ties this enzyme's output to
HepG/Ac-HepG or to the G1P-backbone PG. The action is retained but re-grounded,
on two things that are demonstrated and one structural observation.

1. **The lipid framing is not what this row decides.** `GO:0046474` is an `is_a`
   descendant of `GO:0006650` (checked: ancestors of GO:0046474 include
   GO:0006650). Both terms assert involvement in glycerophospholipid metabolism;
   the child adds only direction. Keeping the parent would not avoid the
   undemonstrated flux, it would only state it more vaguely. If the flux were the
   problem, the right action would be `MARK_AS_OVER_ANNOTATED` on the lipid
   wording, not a refinement of it.
2. **Direction is demonstrated without reference to any downstream lipid.**
   KM 8.1 uM for DHAP and 16 uM for NADH against 1370 uM for G1P
   [file:BACSU/egsA/egsA-uniprot.txt "KM=8.1 uM for DHAP", "KM=1370 uM for G1P"],
   i.e. about 170-fold against the oxidative side. The enzyme is a reductase that
   forms glycerophosphate.
3. **Comparator check (per CLAUDE.md's `NEW`/convention guidance, applied here to
   a refinement).** E. coli GpsA (P0A6S7), the stereochemical mirror of EgsA and
   likewise a precursor-supplying NAD(P) glycerophosphate dehydrogenase, carries
   `GO:0046474` by IMP from PMID:4591941, PMID:4597451 and PMID:4914567 and by
   IBA, alongside its own precursor term `GO:0046167` (QuickGO annotation query,
   2026-11-06). So treating a glycerophosphate dehydrogenase as `involved_in`
   glycerophospholipid biosynthesis is GO's own convention, not an inference we
   are inventing. GpsA holding *both* terms is also what shows the ontology gap:
   the G1P enzymes can only hold the lipid term.

Option (b), keeping `GO:0006650` until a G1P process term exists, was rejected:
CLAUDE.md forbids `ACCEPT`/`KEEP_AS_NON_CORE` while arguing a term is too
general, the term is not as precise as the evidence allows (direction is known),
and an ontology gap is recorded in `proposed_new_terms`, not by parking a row on
a less specific existing term.

Ontology gap verified: a QuickGO ontology search for "glycerol-1-phosphate"
(2026-11-06) returns only MF terms (GO:0050492, GO:0106357, GO:0106358,
GO:0000121, GO:0120536) and no process term at any level, while GO:0046167
(G3P biosynthesis, under GO:0006072) exists for the other enantiomer. Proposed
`sn-glycerol 1-phosphate biosynthetic process` under `GO:0090407`.

Also verified in this pass: neither `egsA` nor `araM` occurs anywhere in the
Komazin 2025 full text [PMID:40626731], so its screen is silent on EgsA rather
than counter-evidence; the hits are stated as [PMID:40626731 "Only pcrB, yvoF,
and ypjA fully suppressed TLR2 activity, indicating these genes are strictly
required for Ac-LP synthesis."]. The Rieche 2026 second-G1P-route statement is
the authors' reading of Caforio et al. 2018, not new data here
[PMID:42286214 "At present, there is no other mechanism of G1P biosynthesis
known"]. Guldan 2008, Sa-Nogueira 1997, Mota 1999, Guldan 2011, Linde 2016,
Palyzova 2022 and the lipid-divide review remain abstract-only in the cache, so
the araM knockout result is still unverified.


## 2026-11-07 module audit: source scope and complete annotation review

Rechecked all existing annotation rows, references and core functions against the frozen sources. No machine payload, row order or historical NEW assertion was changed; no new annotation was added. The default Falcon attempt failed with HTTP403 and produced no provider report; manual review is documented here instead. Normal PAINT-loss checks returned no IRD/IKR.

The lipid-process claim is now UNDECIDED: kinetic asymmetry does not establish native direction or lipid flux. Broad NAD(P) activity is refined to both existing cofactor-specific children; preferred NAD activity remains core and measured lower-efficiency NADP activity remains non-core. The official author thesis was read separately from the still abstract-only 2008 article; scoped source analysis documents Table10 and the exogenous-G1P bypass in the ΔaraM experiment. The 2026 alternative-G1P statement cites prior engineered E. coli work, not a new B. subtilis pathway.


## 2026-11-07 PR review follow-up

Kinetic differences between reaction directions do not determine the net cellular flux. This evidence limitation is retained in notes and in the native precursor-flux knowledge gap rather than the standalone biological description.
