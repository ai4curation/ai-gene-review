# PTHR24119 (ACBD6 and plant Class-II ACBP1/ACBP2): domain-architecture, transmembrane, and pocket-residue survey

Script: `member_survey.py` (this folder); output table: `member_architectures.tsv`.
Run from repository root:

```bash
uv run python interpro/panther/PTHR24119/PTHR24119-bioinformatics/member_survey.py
```

## Question

`PTHR24119-entries.csv` records the 12 reviewed Swiss-Prot members of PANTHER family
`PTHR24119`, whereas PANTHER 19.0 reference-proteome membership (`panther-members-19.0.tsv`)
and InterPro's PANTHER HMM assignments span 27 UniProtKB accessions across five subfamilies
(`SF0`, `SF1`, `SF4`, `SF7`, `SF10`), including unreviewed TrEMBL members in *Drosophila*,
*C. elegans*, *Populus*, *Xenopus*, *Gallus*, and *Dictyostelium*. Because PAINT node
`PTN001191022` (Eukaryota) propagates `GO:0005783` (`endoplasmic reticulum`), `GO:0005886`
(`plasma membrane`), `GO:0000062` (`fatty-acyl-CoA binding`), and `GO:0008047` (`enzyme
activator activity`) across the family, this survey verifies for all 27 members:

1. Presence or absence of the four-helix `IPR000582` (`Acyl-CoA-binding_protein`) domain;
2. Presence or absence of `FT TRANSMEM` helices;
3. BLOSUM62-aligned residues at the human `Q9BR61` (`SV=1`) ACB-pocket and regulatory-loop
   positions (`Tyr69`, `Lys73`, `Lys95`, `Ser106`, `Ser108`, `Tyr114`).

## Summary of Findings (`member_architectures.tsv`)

1. **Soluble eukaryotic ACBD6 orthologs in `PTHR24119:SF0` (15 entries)**:
   - Mammalian (`Q9BR61`, `Q9D061`, `Q5RJK8`, `A2VDR2`, `G3N0L6`), avian (`E1C483`),
     amphibian (`Q4V869`, `Q66JD7`, `Q28E11`, `A0A8J1N1S3`), teleost (`Q4V8X4`), insect
     (`Q9VRG6` / `anox`), nematode (`Q9XVJ0` / `acbp-5`), and amoebozoan (`Q54GC8` /
     *Dictyostelium* `acbd6`) orthologs all carry `IPR000582` + `IPR002110` (`has_ipr000582=True`),
     have **no** `FT TRANSMEM` segment (`ft_transmem=none`), and strictly conserve the
     CoA-headgroup triad (`Tyr69`/`Lys73`/`Lys95` in `Q9BR61`; `Y87/K91/K113` in `Q4V8X4`;
     `Y36/K40/K62` in `Q9VRG6`; `Y55/K59/K82` in `Q9XVJ0`; `Y36/K40/K62` in `Q54GC8`).
   - All reviewed orthologs conserve helix-`alpha4` `Tyr114` (`Y132` in `Q4V8X4`, `Y81` in
     `Q9VRG6` and `Q54GC8`, `Y101` in `Q9XVJ0`). At the mammalian `Ser106`/`Ser108` regulatory
     loop, zebrafish `Q4V8X4` retains `Ser124` (`S124`) and carries glutamate (`E126`) at the
     `Ser108`-equivalent position (`Y87/K91/K113/S124/E126/Y132`).
2. **Land-plant Class-II ACBPs in `PTHR24119:SF4` and `PTHR24119:SF0` (5 entries)**:
   - *Arabidopsis* `ACBP2` (`Q9STP8`, `SF4`, `FT TRANSMEM 11..31`), *Arabidopsis* `ACBP1`
     (`Q9SM23`, `SF0`, `FT TRANSMEM 11..31`), and *Oryza sativa* `ACBP4` (`A3AYR1`, `SF0`,
     `FT TRANSMEM 12..32`) carry an N-terminal transmembrane anchor plus `IPR000582` +
     `IPR002110` and conserve the ACB pocket (`Y136/K140/K162` + `Y181` in `Q9STP8`;
     `Y126/K130/K152` + `Y171` in `Q9SM23`; `Y120/K124/K146` + `Y165` in `A3AYR1`).
   - Full-length *Populus trichocarpa* `B9IDN1` (353 aa, `ACB:106..196`) retains the N-terminal
     extension upstream of the ACB domain, whereas N-terminally truncated *Populus* entry
     `A0A2K1Y7F9` (246 aa, `ACB:1..88`, `ft_transmem=none`) begins directly at the ACB domain.
3. **ACB-less repeat/domain-creep and truncated entries (`has_ipr000582=False`, 7 entries)**:
   - Inside `PTHR24119:SF0`:
     - `UniProtKB:O50999` (*Borreliella burgdorferi* `BB_B28`, reviewed, 414 aa): `interpro_domains=IPR002110;IPR036770`, `ft_transmem=none`, `ANK 1:326..355;ANK 2:359..389`, `no_ACB_domain`.
     - `UniProtKB:A0A1L8GMQ7` (*Xenopus laevis* truncated `acbd6.L`, unreviewed, 169 aa): `interpro_domains=IPR002110;IPR036770`, `ft_transmem=none`, `ANK:65..97;ANK:98..130`, `no_ACB_domain`.
     - `UniProtKB:Q54ZJ0` (*Dictyostelium discoideum* `DDB_G0277559`, unreviewed, 645 aa, UniProt RecName `IPT/TIG domain-containing protein`): `has_ipr000582=False`, `interpro_domains=none`, `ft_transmem=506..531`, `no_ACB_domain`.
     - `UniProtKB:Q86H58` (*Dictyostelium discoideum* `DDB_G0275529`, unreviewed, 1422 aa): `has_ipr000582=False`, `interpro_domains=IPR002110;IPR036770`, `ft_transmem=none`, `ANK:615..647;ANK:648..680`, `no_ACB_domain`.
   - Divergent *Dictyostelium* subfamilies:
     - `PTHR24119:SF1` (`UniProtKB:Q8MP77`, `DDB_G0277427`, unreviewed, 636 aa): `has_ipr000582=False`, `interpro_domains=IPR002110;IPR036770`, `ANK:33..65`, `no_ACB_domain`.
     - `PTHR24119:SF7` (`UniProtKB:Q54VR7`, `DDB_G0280375`, unreviewed, 1608 aa): `has_ipr000582=False`, `interpro_domains=none`, 7 `FT TRANSMEM` helices, `no_ACB_domain`.
     - `PTHR24119:SF10` (`UniProtKB:Q54JS2`, `DDB_G0287823`, 854 aa, `IPR032675;IPR000980;IPR036860`, `SH2:173..248`; and `UniProtKB:Q55BF3`, `DDB_G0271308`, 771 aa, `interpro_domains=none`): `has_ipr000582=False`, `no_ACB_domain`.
