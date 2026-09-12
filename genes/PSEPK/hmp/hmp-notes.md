# hmp (Flavohemoprotein / Flavohemoglobin) — Pseudomonas putida KT2440

UniProt: Q88PP0 (HMP_PSEPK), gene `hmp` (synonym `hmpA`; locus PP_0808), 392 aa.
EC 1.14.12.17. Inferred from homology (PE 3). Annotated by HAMAP-Rule MF_01252.

## Core function

Hmp is a two-domain flavohemoglobin (flavohemoprotein). Its core, defining
catalytic function is **nitric oxide dioxygenase (NOD)** activity: using O2 and
NAD(P)H it converts nitric oxide (NO) to nitrate, detoxifying NO and protecting
the cell against nitrosative stress.

- [UniProt "Is involved in NO detoxification in an aerobic process, termed nitric oxide dioxygenase (NOD) reaction that utilizes O(2) and NAD(P)H to convert NO to nitrate, which protects the bacterium from various noxious nitrogen compounds. Therefore, plays a central role in the inducible response to nitrosative stress."]

## Catalytic activity

- [UniProt "Reaction=2 nitric oxide + NADPH + 2 O2 = 2 nitrate + NADP(+) + H(+);"]
- [UniProt "Reaction=2 nitric oxide + NADH + 2 O2 = 2 nitrate + NAD(+) + H(+);"]
- EC: [UniProt "EC=1.14.12.17"]

## Cofactors / domains

Two distinct domains: an N-terminal heme (oxygen-binding) globin domain and a
C-terminal FAD/NAD(P)H reductase domain.

- Heme b: [UniProt "Binds 1 heme b (iron(II)-protoporphyrin IX) group per subunit."]
- FAD: [UniProt "Binds 1 FAD per subunit."]
- [UniProt "Consists of two distinct domains; an N-terminal heme-containing oxygen-binding domain and a C-terminal reductase domain with binding sites for FAD and NAD(P)H."]
- [UniProt "Belongs to the globin family. Two-domain flavohemoproteins subfamily."]

## Notes on annotation quality

The specific, informative terms for this protein are:
- MF: nitric oxide dioxygenase [NAD(P)H] activity (GO:0008941) — core catalytic function.
- BP: nitric oxide catabolic process (GO:0046210); response to nitrosative stress
  (GO:0051409) / cellular response to nitrosative stress (GO:0071500) — core biological roles.

Broad/supporting terms present in GOA:
- heme binding (GO:0020037) and FAD binding (GO:0071949): true cofactor-binding
  facts (heme b and FAD are bound per the COFACTOR lines) but generic relative to
  the NOD activity; the catalytic term already implies use of these cofactors.
- oxidoreductase activity (GO:0016491): correct but a high-level parent of the
  specific NOD activity (EC 1.14.12.17); over-annotation.
- oxygen binding (GO:0019825): a property of the globin heme domain; supporting
  but generic.

Likely mis-leading / mis-transferred terms (from globin homology, not the actual
biology of a bacterial flavohemoglobin):
- oxygen carrier activity (GO:0005344) and oxygen transport (GO:0015671): these
  are UniRule terms inherited from the globin family. Bacterial flavohemoglobins
  function in NO detoxification, not in physiological O2 transport/carriage; O2 is
  a co-substrate of the NOD reaction, not cargo being transported. These are
  over-annotations / arguably incorrect for this protein's biological role.

There is no organism-specific experimental publication for P. putida hmp in the
cached set; the only cached reference (PMID:12534463) is the KT2440 genome paper
and contains no functional characterization of hmp. All GOA annotations are IEA.
The functional assignment rests on strong homology (HAMAP MF_01252, the
flavohemoglobin/Hmp family) and EC 1.14.12.17.
