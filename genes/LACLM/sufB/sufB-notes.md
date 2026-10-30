# sufB (A2RMK5, llmg_1969) notes

## Source of request

Reviewed from the KBase Dark Protein Atlas item
https://gene-annotate-dashboard.kbase.us/review/NZ_LKLC01000161.1_58
(Lactococcus lactis, 470 aa). That protein is 100% identical over its full
length to UniProt A2RMK5 (MG1363 llmg_1969), so the review is filed under
`genes/LACLM/sufB`.

Dashboard call (tier A): "SufB iron–sulfur cluster assembly scaffold protein of
the SUF system", GO:0051536 iron-sulfur cluster binding and GO:0016226
iron-sulfur cluster assembly. Prior annotations: eggNOG "Uncharacterized protein
family (UPF0051)", Pfam PF19295, KEGG K09014.

**Dashboard verdict: supported.** The call agrees with, and refines, the older
UPF0051 label. It does not assign an EC number, rightly, because SufB is a
scaffold, not an enzyme. Rejecting the transporter and cysteine-desulfurase
labels on distant hits is also right: "ABC transporter" names on SufB homologs
come from the SufC ATPase partner, and the desulfurase labels belong to SufS.

## Evidence

- Identity: the dashboard sequence is exactly equal to A2RMK5 (470/470;
  `sufB-bioinformatics/identity_and_family.py`).
- Full-length TIGR01980 (SufB-specific) match: residues 14-461, 95.3% coverage,
  E=1.6e-224 by local hmmsearch (dashboard InterProScan: 15-461, E=1.1e-216);
  SufBD N-terminal (PF19295) and core (PF01458) domains (UniProt A2RMK5).
- E. coli SufB residues conserved: C254→C236 (sulfur acceptor), C405→C380 and
  E434→E409 (cluster site) [PMID:28839209 "Cys254 of SufB (SufBC254) is essential
  for sulfur-transfer from SufE"]; see `sufB-bioinformatics/RESULTS.md`.
- Operon llmg_1974-1969 = sufC, sufD, sufS, (llmg_1971 unknown), sufU, sufB
  (KEGG), the Firmicute arrangement in which SufU replaces SufE
  [PMID:24321018 "the Suf system includes SufB, SufC, and SufD ortholog proteins in
  addition to SufU, a sulfur acceptor substrate of SufS"].
- E. coli SufB is the site of cluster assembly [PMID:17350958 "SufB can act as a
  site for Fe-S cluster assembly in the Suf system"].
- Only L. lactis literature: sufB used as a prophage-integration landmark
  [PMID:24009606]. Close homolog data: E. faecalis EF2390 operon induced by H2O2
  (PMID:24936909) and important for growth in Tn-seq (PMID:33234689).

## Caveats

- No direct experimental work on the lactococcal protein.
- The MF stays at the generic GO:0051536 because the cluster species on the
  donor E. coli SufB is not settled: E. coli SufB has IDA rows for both
  [4Fe-4S] (PMID:17350958) and [2Fe-2S] (PMID:25485887) binding, and the
  anaerobically isolated SufBCD cluster differs spectroscopically from the
  in vitro [4Fe-4S] one [PMID:28839209 "anaerobically isolated SufBCD complex
  from E. coli was demonstrated to possess Fe-S cluster with distinct
  spectroscopic features from that of [4Fe-4S] cluster reconstituted in vitro"].
- The dashboard's fitness homologs (37-39% identity, Enterobacterales) are too
  distant to add anything specific.
