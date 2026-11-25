# azoR (P41407) review notes

E. coli K-12 AzoR (acpD), FMN-dependent NADH:quinone oxidoreductase / NADH-azoreductase.
~23 kDa, flavodoxin-like fold, obligate homodimer with two shared active sites. HAMAP MF_01216.
EC 1.6.5.- (quinone reductase) and EC 1.7.1.17 (NADH-azoreductase).

## Literature search (2026-11-24)

No deep-research file; searched PubMed directly.

- `azoreductase AzoR Escherichia coli` -> PMID:16684776 (crystal structure), PMID:16511052
  (crystallization), PMID:19666717 (physiological quinone-reductase role), PMID:18337254
  (substrate specificity/mutagenesis), PMID:23795903 (aerobic nitro/azo reductase comparison),
  plus unrelated dye-sensing/probe papers.
- `acpD azoreductase` / UniProt citations -> PMID:11583992 (Nakanishi 2001, the paper that
  identified acpD as the azoreductase; GOA IDA source for most AzoR rows).
- Proteomics GOA cytosol rows: PMID:17309111, PMID:18304323.

## Key findings

- AzoR (acpD gene product) is an FMN-dependent NADH-azoreductase; it reduces methyl red by a
  ping-pong mechanism requiring 2 NADH per azo bond [PMID:11583992 "The reaction followed a
  ping-pong mechanism requiring 2 mol of NADH to reduce 1 mol of methyl red"]. It is NADH-, not
  NADPH-dependent.
- Physiological role: a quinone reductase that provides resistance to thiol-specific stress from
  electrophilic quinones; quinones are better substrates than the model azo dye methyl red
  [PMID:19666717 "AzoR was capable of reducing several benzo-, naphtho-, and anthraquinone
  compounds, which were better substrates for AzoR than the model azo substrate methyl red"];
  azoR deletion is more sensitive to electrophilic quinones, and azoR transcription is induced by
  electrophiles [PMID:19666717].
- Structure: FMN-dependent, acts as a homodimer forming two identical catalytic sites to which
  both monomers contribute; flavodoxin-like fold [PMID:16684776 "AzoR acts in a homodimeric state
  forming the two identical catalytic sites to which both monomers contribute"].
- Substrate specificity governed by Arg59; cannot reduce sulfonated azo dyes; also a
  nitroreductase (PMID:18337254, PMID:23795903).

## RHEA backing (staged RHEA:55872)

- RHEA:55872 is the azoreductase (methyl-red-type) reaction, written with NAD+ (EC 1.7.1.17,
  NADH-dependent). The staged mapping (projects/RHEA/rhea2go.sssom.yaml) has:
  - exactMatch -> sssom:NoTermFound, comment: GO:0050446 is NADP+-specific (EC 1.7.1.6) so does
    not fit; propose "azobenzene reductase (NADH) activity".
  - broadMatch -> GO:0046857 (oxidoreductase, acting on other nitrogenous compounds as donors,
    with NAD or NADP as acceptor).
- This review AGREES the staged finding is right: the existing GOA IDA row to GO:0050446
  azobenzene reductase (NADP+) activity (EC 1.7.1.6) is the WRONG term for AzoR, which is
  NADH-dependent (EC 1.7.1.17). PMID:11583992, the IDA source, explicitly shows NADH. So I MODIFY
  GO:0050446 to a proposed NTR "azobenzene reductase (NADH) activity" (parent GO:0046857), and
  record a source_defects WRONG_TERM against EcoCyc (NADP+ term used for a NADH enzyme). The
  staged broadMatch GO:0046857 and the NoTermFound new-term flag are thereby BACKED; the staged
  GO:0050446 exactMatch is confirmed wrong (already marked NoTermFound in the file).

## Curation decisions

- Core function is the FMN-dependent NADH:quinone oxidoreductase activity GO:0016655
  (NAD(P)H, quinone or similar compound as acceptor): ACCEPT the IBA, IDA (PMID:19666717) and
  InterPro IEA. This is the physiological activity (PMID:19666717). GO:0016655 is already carried;
  no RHEA mapping task here, but it is the primary MF.
- Azobenzene reductase (NADH) activity: the EC 1.7.1.17 azo-reductase activity that named the
  enzyme is a genuine, directly assayed activity -> represented by MODIFY of the mis-cofactored
  GO:0050446 to the NADH NTR; kept non-core (quinones are the better/physiological substrates).
- GO:0016652 (acting on NAD(P)H as acceptor) IEA: its definition is NADH as donor reducing
  NAD+/NADP (a transhydrogenase-like class), not AzoR's quinone/azo reduction. MODIFY (lateral) to
  the correct sibling GO:0016655, which is already present by IDA.
- GO:0009055 electron transfer activity IEA: MARK_AS_OVER_ANNOTATED. AzoR is a terminal FMN
  reductase, not an electron-transport-chain carrier; its function is captured by GO:0016655.
- FMN binding (IDA, IEA): KEEP_AS_NON_CORE (essential cofactor of the core redox activity).
- homodimerization activity IDA: KEEP_AS_NON_CORE (quaternary structure required to build the
  shared active sites).
- cytosol (two IDA proteomics rows): ACCEPT (soluble cytoplasmic flavoenzyme).
- response to oxidative stress (IBA, IMP): KEEP_AS_NON_CORE (downstream role of the quinone
  reductase activity in resisting electrophilic/thiol stress).
