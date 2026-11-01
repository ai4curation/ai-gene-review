# Module-context oracle: MODULE:ubiquitin_transfer_relay

Detector: `ubiquitin_transfer_relay.yaml`. Cache (counts of proteome members per
InterPro signature, proteome completeness, CR-0003 matches): `cache/ubiquitin_transfer_relay.yaml`.
Reproduce or extend with:

```bash
just evaluate-module-context rules/curated/context/ubiquitin_transfer_relay.yaml UP000005640 ... --rule rules/curated/CR-0003.yaml
```

Counts come live from UniProt REST (2026-10-30 run) and change with releases; add
`--refresh` to re-fetch cached proteomes.

## Results (2026-10-30)

| Proteome | Organism | BUSCO | UBC E2 (IPR000608) | Ubiquitin-like (IPR000626) | Verdict | CR-0003 |
|---|---|---|---|---|---|---|
| UP000005640 | *Homo sapiens* | 99 | 268 | 398 | satisfiable | annotates 72 |
| UP000002311 | *Saccharomyces cerevisiae* S288c | 99 | 14 | 14 | satisfiable | annotates 7 |
| UP000008243 | *Haloferax volcanii* DS2 | 99 | 0 | 0 | unsatisfiable | blocks 2 |
| UP000000242 | *Metallosphaera sedula* DSM 5348 | 98 | 0 | 0 | unsatisfiable | blocks 1 |
| UP000001584 | *Mycobacterium tuberculosis* H37Rv | 99 | 0 | 0 | unsatisfiable | 0 matches |
| UP000321408 | *Promethearchaeum syntrophicum* (Asgard) | 89 | 1 | 1 | satisfiable | annotates 2 |
| UP001208689 | *Candidatus* Lokiarchaeum ossiferum (Asgard) | 87 | 2 | 2 | satisfiable | annotates 3 |
| UP000050535 | *Halolamina pelagica* | 86 | 1 | 0 | not evaluated (incomplete) | annotates 2 |

"Satisfiable" means every module step (E1, E2, E3) and the detector's extra
ubiquitin-modifier step has at least one matching protein. "Unsatisfiable" is
reported only for a complete proteome (reference proteome, full assembly, BUSCO
at least 95); otherwise the verdict is "not evaluated" and the rule still fires.

## What this shows

- The two haloarchaeal and sulfolobal proteomes have only a ThiF-fold activating
  enzyme (the SAMP/MoaD system) and no UBC E2 or ubiquitin-like protein, so CR-0003
  blocks ubiquitin-dependent catabolism on their proteasome alpha subunits.
- The two Asgard proteomes contain a UBC E2, a ubiquitin-like-domain protein and a
  RING protein, so the rule keeps the term there. A plain Eukaryota condition would
  have blocked them. Whether these Asgard systems are functional ubiquitin systems
  was not assessed here; the detector only shows the components are encoded.
- *Halolamina pelagica* has one UBC-domain protein but no ubiquitin-like protein.
  Its proteome is below the completeness threshold, so the oracle declines to call
  the module absent. The single UBC hit in a haloarchaeon is unusual and was not
  investigated.
- *M. tuberculosis* proteasome subunits do not match IPR000426, so the InterPro
  mapping never reached them; bacterial proteasomes are outside this rule.

## All archaeal proteomes with IPR000426 (2026-10-31)

Run with `just evaluate-module-context rules/curated/context/ubiquitin_transfer_relay.yaml
--rule rules/curated/CR-0003.yaml --taxon 2157`. The bulk mode streams one UniProt query
per signature across Archaea instead of one count per proteome; for the seven
archaeal proteomes resolved individually above it gave identical counts.

888 archaeal UniProtKB entries match IPR000426. 873 of them belong to 610 proteomes,
all of them reference proteomes; 15 belong to no proteome and cannot be evaluated, so
the rule still fires on them.

| Verdict | Proteomes | IPR000426 proteins | CR-0003 |
|---|---|---|---|
| unsatisfiable (complete proteome, relay absent) | 501 | 733 | blocks GO:0006511 |
| satisfiable | 3 | 6 | keeps GO:0006511 |
| not evaluated (BUSCO below 95) | 106 | 134 | keeps GO:0006511 |
| no proteome | - | 15 | keeps GO:0006511 |

So CR-0003 removes 733 of the 888 archaeal GO:0006511 annotations the InterPro2GO
mapping produces (83%). The other 155 keep it: 6 because the relay is detected, 149
because the evidence is not good enough to call it absent.

Every not-evaluated proteome failed on BUSCO alone (type and assembly level passed).
The cut-off of 95 is a policy choice: lowering it would block more proteins at more
risk of calling a detection gap an absence.

The three satisfiable proteomes:

| Proteome | Organism | UBC E2 | Ubiquitin-like | RING | Notes |
|---|---|---|---|---|---|
| UP000321408 | *Promethearchaeum syntrophicum* (Asgard) | A0A5B9D7T8 | A0A5B9D6M8 | A0A5B9DAL9, A0A5B9DG89 | BUSCO 89; satisfiable regardless of completeness |
| UP001208689 | *Candidatus* Lokiarchaeum ossiferum (Asgard) | 2 | 2 | 1 | BUSCO 87 |
| UP000030787 | *Candidatus* Methanoplasma termitum | A0A0A7LA35 (161 aa) | A0A0A7LA92 (80 aa) | A0A0A7LF26 (175 aa) | BUSCO 98; a termite-gut Thermoplasmata methanogen, not an Asgard archaeon |

The *Methanoplasma* hit was not expected. It carries one small UBC E2, one
ubiquitin-like protein and one RING protein, which may be a minimal ubiquitin-like
operon or a horizontal acquisition; this was not assessed. Two incomplete haloarchaeal
proteomes, *Halolamina pelagica* (UP000050535) and *Halosegnis longus* (UP000270581), each
carry a single UBC-domain protein but lack a RING or ubiquitin-like protein
respectively, so the relay is not satisfied; being below the completeness threshold,
they are not evaluated and keep the term.

## What the literature says about the unusual cases (2026-10-31)

PubMed searched through NCBI E-utilities; cited papers cached in `publications/`.

**Asgard archaea (*Promethearchaeum syntrophicum*, *Lokiarchaeum ossiferum*).**
Keeping GO:0006511 here is consistent with the literature. Asgard genomes encode a
eukaryote-like ubiquitin system, and parts of it have been shown to work.
- In the cultured *P. syntrophicum* (strain MK-D1), ubiquitin is among the most highly
  expressed eukaryotic signature genes: "Among eukaryotic signature proteins, 23 fall in
  the 500 most highly expressed genes, including hypothetical proteins related to actin,
  gelsolin, ubiquitin" [PMID:31942073].
- Asgard ESCRT proteins are recruited through ubiquitin: "We provide evidence for the
  ESCRT-I and ESCRT-II subcomplexes being involved in ubiquitin-directed recruitment of
  ESCRT-III, as it is in eukaryotes." [PMID:35697693]
- An Asgard cascade modifies a protein in vitro: "A steadiness box in the Vps23 domain
  undergoes ubiquitination through an Asgard E1, E2, and RING E3 cascade."
  [PMID:38358888]
- None of these papers shows that Asgard proteasomes degrade ubiquitinated substrates,
  which is what GO:0006511 asserts. The term is plausible for these organisms, not shown.

**The first functional archaeal ubiquitin system is outside this rule's reach.** The
system reconstructed in vitro came from *Candidatus* Caldiarchaeum subterraneum
(Aigarchaeota, now Caldarchaeales), where the components sit in operons: "Encoded in
operons, these components are likely representative of the progenitor apparatus that
founded the modern eukaryotic ubiquitin modification systems." [PMID:29066714; genome
in PMID:21169198, which found the system "unprecedented in prokaryotes"]. No
Caldarchaeales entry in UniProtKB matches IPR000426, so CR-0003 neither keeps nor
removes anything there.

***Candidatus* Methanoplasma termitum.** No paper describes a ubiquitin system in this
organism; its genome paper [PMID:25501486] is about energy metabolism and does not
mention one. Its genome has a compact gene cluster, Mpt1_c00340 to Mpt1_c00370:
UbaA-type E1 (A0A0A7LC91), ubiquitin-like protein (A0A0A7LA92), UBC E2 (A0A0A7LA35) and
a JAB/MPN (Mov34) protein (A0A0A7L9W5); the RING protein (A0A0A7LF26, Mpt1_c10590) is
elsewhere. Two kinds of described system share that make-up:
- the eukaryote-like operons of Caldiarchaeum and Asgard archaea (above);
- prokaryotic conjugation systems that are not linked to proteasomal degradation. A
  bacterial anti-phage defence system comprises "a ubiquitin-like protein,
  ubiquitin-conjugating enzymes E1 and E2, and a deubiquitinase" and attaches the
  ubiquitin-like protein to a phage tail protein [PMID:39020165]. Comparative genomics
  finds prokaryotic Ub-like systems "ranging from those catalyzing cofactor and amino
  acid biosynthesis, with only adenylating E1-like enzymes and ubiquitin-like proteins
  (Ubls), to those that are closer to eukaryotic systems by virtue of possessing E2
  enzymes" [PMID:21547297], including in methanogenic euryarchaea and in
  *Aciduliprofundum*, a Thermoplasmata relative of *Methanoplasma*.

Which kind the *Methanoplasma* cluster is was not determined (that needs a phylogeny
of the E1 and E2). In either case nothing links it to the proteasome, so CR-0003
keeping GO:0006511 on the one *Methanoplasma* alpha subunit is not supported. This is a
weakness of the detector: it finds a conjugation relay, not one coupled to proteasomal
degradation.

**Can a sequence feature separate *Methanoplasma* from the Asgard E2s? No.**
`ubc_features/ubc_features.py` aligns every archaeal UBC-domain protein (IPR000608) and
two eukaryotic controls to human UBE2D1 (P51668) and reads the residues at UBE2D1's HPN
oxyanion-hole motif (H75-P76-N77, the eukaryote-type E2 feature noted in PMID:21547297)
and active-site Cys85. Output (2026-10-31): `ubc_features/ubc_features.tsv`.

| E2 | Organism | Identity to UBE2D1 | HPN | Cys85 |
|---|---|---|---|---|
| P15731 | yeast UBC4 (control) | 0.79 | HPN | C |
| A0A5B9D7T8 | *Promethearchaeum syntrophicum* | 0.34 | HPN | C |
| A0ABY6HW80, A0ABY6HXC4 | *Lokiarchaeum ossiferum* | 0.31, 0.35 | HPN | C |
| A0A0A7LA35 | *Methanoplasma termitum* | 0.26 | HPN | C |
| A0A133VR40 | MSBL1 archaeon | 0.37 | NPN | C |
| A0AAJ4UUM9 | *Halosegnis longus* | 0.27 | NPN | C |
| A0A0P7GUT2 | *Halolamina pelagica* | 0.17 | SDD | P |

The *Methanoplasma* E2 has the eukaryote-type HPN motif and the catalytic cysteine, like
the Asgard E2s, and its identity to UBE2D1 is only slightly lower. The features do flag
the *Halolamina* protein as non-catalytic (no cysteine at the active site), but that
proteome is already not evaluated. Adding the check to the detector would therefore
change no verdict, so the detector is unchanged. Separating the two kinds of system would
need a phylogeny of the E1 and E2 against eukaryotic and bacterial defence-system
homologues; the *Methanoplasma* case affects one protein.

**Haloarchaea with a lone UBC protein.** Nothing published was found. Both are
compact: *Halosegnis longus* has a UBC protein next to a ubiquitin-like protein
(Nmn1133_13640/13645) and *Halolamina pelagica* has a UBC protein four loci from a
large ThiF-family E1 (SY89_03484/03488). Their SAMP-system E1 (MoeB) and JAB protease
sit elsewhere. They look like the same kind of small prokaryotic cluster. Neither
proteome satisfies the relay, and both are below the completeness threshold, so the rule
keeps the term; that is an artefact of incompleteness, not evidence for ubiquitin.

## Limits

- Detection is by InterPro signature presence only; a matching domain is not proof
  of a working enzyme.
- A detected relay is not a proteasome-coupled one. Compact prokaryotic E1-E2-Ubl
  systems can serve other purposes (for example phage defence, PMID:39020165), so a
  satisfiable verdict can keep GO:0006511 where it does not belong (*Methanoplasma*).
- Bacterial and other non-eukaryotic, non-archaeal IPR000426 entries (74) were not
  resolved; run the bulk mode with `--taxon 2` to add bacteria.
