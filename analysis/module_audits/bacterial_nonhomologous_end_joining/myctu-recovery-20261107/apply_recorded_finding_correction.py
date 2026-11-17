from pathlib import Path
import yaml

mapping = {
    "Binds linear dsDNA": "Curated primary-linked experiments distinguish binding to linear double-stranded ends from closed circular duplex or single-stranded DNA.",
    "bacterial Ku specifically": "Ku recruits ligase to DNA ends and stimulates ligation; this is an active partner function rather than bare binding alone.",
    "These enzyme activities allow": "Mycobacterial Ku and LigD join incompatible DNA ends in vitro and reconstitute NHEJ in yeast; the latter is a heterologous assay.",
    "all Ku mutants had": "The accession-defined Ku mutant proteins retain homodimeric assembly in SEC-MALS controls.",
    "DNA-binding assays revealed": "Both isolated POL and ligase domains bind DNA, with greater measured affinity for the ligase domain in this study.",
    "The polymerase domain can": "Purified LigD POL supports template-dependent DNA extension.",
    "LigC and LigD, which": "LigD has ATP-specific adenylation and detectable nick joining; weak activity in this assay does not negate its ligase function.",
    "including gap-filling": "The original full-length Mt-Lig characterization reports polymerase, terminal-transferase, primase and exonuclease activities.",
    "crystal structures of the": "Structures capture the target POL domain both alone and with nucleotides, grounding substrate recognition.",
    "Binds 4 Mn": "Curated primary-linked cofactor synthesis assigns manganese sites across the POL, phosphoesterase and ligase functions; this is not a universal physiological-metal preference claim.",
    "annealing the": "The target polymerase study couples annealing of opposing three-prime overhangs to extension in trans.",
}
for g in ["mku", "ligD"]:
    p = Path(f"genes/MYCTU/{g}/{g}-ai-review.yaml")
    d = yaml.safe_load(p.read_text())
    for ref in d["references"]:
        for f in ref.get("findings", []):
            for prefix, statement in mapping.items():
                if f.get("supporting_text", "").startswith(prefix):
                    f["statement"] = statement
    p.write_text(
        "\n".join(
            x.rstrip()
            for x in yaml.safe_dump(
                d, sort_keys=False, allow_unicode=True, width=100
            ).splitlines()
        )
        + "\n"
    )
