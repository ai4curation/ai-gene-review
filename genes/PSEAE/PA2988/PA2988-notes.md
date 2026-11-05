# PA2988 (Q9HZL6) notes

LolC/LolE-family permease subunit of the P. aeruginosa LolCDE lipoprotein-release ABC
transporter (operon PA2986 permease, PA2987 lolD, PA2988 permease). No deep-research provider
was available; literature search was done by hand (PubMed metadata and abstract for
PMID:17350955; QuickGO for the E. coli LolC/LolE seeds).

## Literature

- Tanaka, Narita & Tokuda 2007 (PMID:17350955; abstract only, JBC full text not reachable):
  the purified P. aeruginosa LolCDE homologue, reconstituted into proteoliposomes, released
  lipoproteins in the presence of ATP and LolA ["When incubated in the presence of ATP and a LolA
  homologue, the reconstituted LolCDE homologue released lipoproteins, leading to the formation of
  a LolA-lipoprotein complex."]; LolB then put them in the outer membrane. Lipoproteins with
  Lys3-Ser4 stayed in proteoliposomes ["As revealed in vivo, lipoproteins with Lys and Ser at
  positions 3 and 4, respectively, remained in proteoliposomes."].
- UniProt Q9HZL6 (unreviewed): four Phobius TM helices, MacB-like periplasmic core domain,
  NCBIfam TIGR02212 lolCE. Which of PA2986/PA2988 is the LolC-like and which the LolE-like
  subunit is not resolved in the sources I read.

## Review decisions

- GO:0044874 IDA and IBA: ACCEPT (core).
- GO:0042953 lipoprotein transport IEA: ACCEPT (same step, transport view; not an ancestor of
  GO:0044874).
- GO:0016020 membrane: MODIFY to GO:0005886.
- GO:0098797 IBA: MODIFY to GO:0043190 ABC transporter complex (is_a descendant; E. coli LolC/E
  carry it by IPI).
- NEW GO:0140306 lipoprotein releasing activity (IDA, PMID:17350955), as for E. coli LolC/LolE.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002524722 | GO:0044874 lipoprotein localization to outer membrane | 4 | 46 (26 taxa) | GO:0044874, IDA, PMID:17350955 (PseudoCAP; also CACAO) | SOUND | Abstract states the purified P. aeruginosa LolCDE complex releases lipoproteins to LolA (ATP-dependent) and LolB inserts them in the outer membrane: direct biochemical evidence for the complex containing PA2988. Node term suits a LolC/LolE clade. | E. coli LolC P0ADC3 and LolE P75958 (both IDA GO:0044874, PMID:17509078; IDA/IMP acts_upstream PMID:10783239, 11844772); PA2986 Q9HZL8 (SOUND, same paper) | Yes, on the E. coli LolC/LolE seeds |

Node-level record for PTN002524722 is kept here (PA2988 has both CACAO and PseudoCAP IDA rows);
PA2986 cross-references it. No PSEUDOCAP or GO_CENTRAL defect.
