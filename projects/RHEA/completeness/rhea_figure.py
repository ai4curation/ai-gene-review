# /// script
# requires-python = ">=3.10"
# dependencies = ["rdkit"]
# ///
"""Render RHEA reactions as SVG from RHEA's own reaction SMILES (rhea-reaction-smiles.tsv).

usage: rhea_figure.py SMILES_TSV OUTDIR RHEA_MASTER_ID [...]
The left-to-right directional id (master + 1) is drawn, since the file keys directional ids.
"""
import sys
from pathlib import Path
from rdkit.Chem import rdChemReactions
from rdkit.Chem.Draw import rdMolDraw2D

tsv, outdir, ids = sys.argv[1], Path(sys.argv[2]), sys.argv[3:]
smiles = {}
for line in open(tsv):
    k, v = line.rstrip("\n").split("\t", 1)
    smiles[k] = v
outdir.mkdir(parents=True, exist_ok=True)
for master in ids:
    lr = str(int(master) + 1)
    rxn = rdChemReactions.ReactionFromSmarts(smiles[lr], useSmiles=True)
    n = rxn.GetNumReactantTemplates() + rxn.GetNumProductTemplates()
    d = rdMolDraw2D.MolDraw2DSVG(min(2400, 340 * n), 360)
    opts = d.drawOptions()
    opts.padding = 0.05
    opts.bondLineWidth = 1.5
    d.DrawReaction(rxn)
    d.FinishDrawing()
    (outdir / f"RHEA_{master}.svg").write_text(d.GetDrawingText())
    print(f"RHEA:{master} -> {outdir}/RHEA_{master}.svg ({n} participants)")
