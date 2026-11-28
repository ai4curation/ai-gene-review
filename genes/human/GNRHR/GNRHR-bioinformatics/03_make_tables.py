# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Render results/disease_variant_table.md from results/variant_structure_table.tsv."""
import csv
import pathlib

OUT = pathlib.Path(__file__).parent / "results"
rows = list(csv.DictReader(open(OUT / "variant_structure_table.tsv"), delimiter="\t"))
plp = lambda c: c.lower().startswith(("pathogenic", "likely pathogenic"))
dis = [r for r in rows if r["in_uniprot_HH7"] or r["lit_class"] or plp(r["clinvar"])]
with open(OUT / "disease_variant_table.md", "w") as f:
    f.write("| Variant | Segment (generic no.) | Reported function (PMID) | ClinVar | gnomAD AF (hom) | rSASA 7BR3 "
            "| Å to GnRH / Gαq (9U4W) | Mammal identity | Computed structural class | Rule output |\n" + "|---" * 10 + "|\n")
    for r in dis:
        if r["lit_class"]:
            lit = r["lit_class"] + (" / " + r["lit_mechanism"] if r["lit_mechanism"] else "") + f" (PMID:{r['lit_pmid']}"
            lit += (f", PMID:{r['lit_mechanism_pmid']}" if r["lit_mechanism_pmid"] else "") + ")"
        else:
            lit = "UniProt HH7 variant, no assay in table" if r["in_uniprot_HH7"] else "-"
        f.write(f"| {r['variant']} | {r['gpcrdb_segment']} ({r['generic_number'].split('x')[0] or '-'}) | {lit} "
                f"| {r['clinvar'] or '-'} | {r['gnomad_af'] or 'absent'} ({r['gnomad_hom'] or 0}) "
                f"| {r['rsa_7BR3'] or 'not modelled'} | {r['dist_GnRH_9U4W'] or '-'} / {r['dist_Gq_9U4W'] or '-'} "
                f"| {r['mammal_identical']} | {r['structural_class']} | {r['structural_reasoning']} |\n")
print(f"{len(dis)} disease-associated missense variants written")
