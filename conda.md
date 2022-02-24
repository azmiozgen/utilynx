# Conda commands

## Add kernels to Jupyter
1. `conda install nb_conda_kernels`
2. `python -m ipykernel install --user --name <env_name>`

## Create environment from file
`conda env create --file envname.yml`

## List environments
`conda env list` or `conda info -e`

## List packages in environment
`conda list`

## Export
`conda env export --name <environment_name> > environment.yml`