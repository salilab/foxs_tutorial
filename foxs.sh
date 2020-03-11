#!/bin/sh -e

foxs -h

cd foxs/nup133
foxs 3KFO.pdb 23922_merge.dat

foxs -g 3KFO.pdb 3KFO-fill.B99990005.pdb 23922_merge.dat

gnuplot fit.plt
