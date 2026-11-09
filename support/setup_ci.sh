#!/bin/bash -e

# Set up an environment to run CI tests, e.g. with GitHub Actions or Travis

if [ $# -ne 1 ]; then
  echo "Usage: $0 imp_branch"
  exit 1
fi

imp_branch=$1

if [ ${imp_branch} = "develop" ]; then
  IMP_CONDA="imp-nightly"
else
  IMP_CONDA="imp"
fi

conda install -n test --yes -q modeller pip ${IMP_CONDA}

pip install pytest-cov coverage
