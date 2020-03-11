#!/bin/sh -e

multi_foxs --help

cd multi_foxs/rpa
multi_foxs weighted.dat 1fguA.pdb 1fguB.pdb 1jmc.pdb
