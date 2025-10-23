#!/usr/bin/env bash
set -euo pipefail
SRC_DIR="b-UnitesEnseignement/Support"
OUT_DIR="${SRC_DIR}/_build/html"
sphinx-build -b html "${SRC_DIR}" "${OUT_DIR}"
echo "[OK] Docs HTML -> ${OUT_DIR}"
