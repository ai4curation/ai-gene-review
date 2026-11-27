"""Importers: convert a predictor's native output into generic Prediction records.

Each importer is a thin adapter. ``benchmark score`` never reads native
formats; it reads only the predictions these modules write. Add a module here
to evaluate another predictor (an InterProScan or PANNZER TSV, a DeepGO
score file, a curator's spreadsheet).
"""
