MultiFoXS: determination of multi-state models {#multifoxs}
==============================================

[TOC]

# Introduction {#multifoxsintro}

In many cases our data comes from a heterogeneous sample. Heterogeneity
can be both compositional and conformational. Interpretation of data
collected on a heterogeneous sample requires a *multi-state model*.
A multi-state model is a model that specifies two or more co-existing
structural states and values for other parameters, such as the weights
of each state.

%IMP includes a command line tool `multi_foxs` for enumeration and scoring
of multi-state models against SAXS profiles. There is also a
[web interface](https://salilab.org/multifoxs/) available, which functions
similarly.

In this example, we will demonstrate how to use it using PDB structures
of replication protein A and a simulated SAXS profile.

For full help on the `multi_foxs` tool, run from a command line:

\code{.sh}
multi_foxs --help
\endcode

# Setup {#multifoxssetup}

First, download the input files used in this example (if you don't already
have them for the [FoXS demonstration](@ref foxssetup)), either by
[cloning the GitHub repository](https://github.com/salilab/foxs_tutorial/tree/master)
or by [downloading the zip file](https://github.com/salilab/foxs_tutorial/archive/master.zip).

All of the data for this example can be found in the `multi_foxs/rpa`
subdirectory.

# Calculation {#multifoxscalc}

The structure of the RPA in complex with ssDNA is available in the
[Protein Data Bank (PDB)](https://www.rcsb.org/) as code
[1jmc](https://www.rcsb.org/structure/1JMC)
(file `1jmc.pdb`), and the unbound RPA structures as code
[1fgu](https://www.rcsb.org/structure/1FGU)
(file `1fguA.pdb`, `1fguB.pdb`), while the SAXS profile is given in the
`weighted.dat` file. The SAXS profile was simulated from the 3 structures
with the following weights:

\verbatim
1jmc.pdb 0.5
1fguA.pdb 0.25
1fguB.pdb 0.25
\endverbatim

3% Gaussian noise was added to the simulated profile.

The atomic structures can be fit against the SAXS profile by running MultiFoXS:

\code{.sh}
multi_foxs weighted.dat 1fguA.pdb 1fguB.pdb 1jmc.pdb
\endcode

FoXS calculates the theoretical profiles of the input structures,
enumerates multi-state models, and fits them to the input SAXS
profile.  The output is a list of best scoring multi-state models of
size 1, 2, and 3 in files `ensembles_size_1.txt`,
`ensembles_size_2.txt`, and `ensembles_size_3.txt`,
respectively. It also generates `multi_state_model_x_x_x.dat`
files, containing the computed theoretical profile for the multi-state
model and its fit against the experimental profile.

In this example, the best fit is obtained using a 3-state model
(Chi=1.74) `ensembles_size_3.txt`, with weights of 0.53, 0.197, and 0.27,
showing a maximal deviation of 7% compared to the weights that were used to
simulate the profile:

\verbatim
1 |  1.74 | x1 1.74 (1.03, 0.53)
0   | 0.533 (0.533, 1.000) | 1jmc.pdb (0.333)
1   | 0.197 (0.197, 1.000) | 1fguA.pdb (0.333)
2   | 0.270 (0.270, 1.000) | 1fguB.pdb (0.333)
\endverbatim
