micro_cholmod
#############

This package groups C functions extracted from **SuiteSparse** to collect only C functions without dependancies

- Everything connects to the C source files of SuiteSparse through symbolic links.
- The SuiteSparse has to be installed somewhere from:

  http://faculty.cse.tamu.edu/davis/SuiteSparse/SuiteSparse-4.2.1.tar.gz

- Only the sources of the SuiteSparse package are needed (no need to build it)
- In order to connect to the SuiteSparse sources, one simply need to install one symbolic link at micro_cholmod root:

  SuiteSparse -> [*physical place of the SuiteSparse package*]

- This package is configured as an LSST package (using EUPS & Scons)

                                                                                
The selection of routines is meant to allow the user to perform a simplicial
Cholesky factorization of a sparse matrix, possibly followed by small rank updates of the factorization, solving (factorizes) linear systems,  and nothing else. This is why this is a small subset of **SuiteSparse**. 
