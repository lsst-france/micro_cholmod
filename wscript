# -*- mode: python; -*- 
# 

import os
import os.path as op
import sys
import Options
import Configure
import commands

import frogsutils


APPNAME = 'micro-cholmod'
VERSION = '4.3'
top  = '.'
out  = frogsutils.get_out_name()
description = "This is micro-cholmod."
requirements = []
#    ('poloka-core', '0.1.0', True), 
#    ('poloka-psf', '0.1.0', True),  
#    ('suitesparse', '', True),
#    ('poloka-simphot', '0.1.0', True), 
#    ('eigen3','',True) ]
# debug = True
# beware : with Eigen, the optimization level matters a *lot* (factors of ~ 10)
optimize = 3


def options(opt):
    opt.load('frogs')

def configure(conf):
    conf.load('frogs')
#    conf.env['CFLAGS'].append('-fexceptions -DNSUPERNODAL -DNPARTITION')
#    conf.load('frogs')
    conf.check_packages(requirements)
#    conf.find_program('doxygen', VAR='DOXYGEN', 
#                      mandatory=False)

def build(bld):
    bld.add_subdirs( ["src"] )
    gen_pkgconfig(bld)

# Not found a way to get it to work directly, and not even to test if
# doxygen was found at configuration. The problem is that the context
# (ctx) passed to doc() is only a small subset of what is passed to
# build(), and we have not found how to use the poor one. So the trick
# is to hack the behavior of build() if one wants to make the doc. As
# a consequence, you won't get the doc if you don't want it.
def doc(ctx) :
    global makingdoc
    makingdoc = True
    print "to make the doc, just type \"./waf doc build install\""
