#/usr/bin/python

# Copyright 2013 by Hartmut Goebel <h.goebel@crazy-compilers.com>
# Licence: GNU Public Licence v3 (GPLv3), but not for military use

import subprocess
import argparse

GRAPH_HEADER = '''
digraph "%s"
{
  nodesep=0; sep=0; ranksep=0
  ratio="compress"
  packmode="node"; pack=1
  pad=0
  splines=true
  rankdir=TB // top-bottom
  concentrate=true;
  //K=0
  edge [arrowsize=0.7,fontsize="6",fontcolor=grey]
  node [fontname="Helvetica",fontsize="10"]
  //node [shape=plaintext,height=0,width=4]
  node [shape=plaintext,height=0]
'''


ignore = set('coreutils python perl ruby bash desktop-file-utils initscripts shadowutils'.split())

MAX_DEPTH = 5 # see option --depth

seen = set(ignore)
nodenames = {}

def nodename(name):
    if name not  in nodenames:
        nodenames[name] = (''.join(c for c in name if c.isalnum())
                          + '_' + str(abs(hash(name))))
    return nodenames[name]


def draw_req(pkg, depth):
    if pkg in seen or depth >= MAX_DEPTH:
        return
    seen.add(pkg)
    pn =  nodename(pkg)

    print ('%s[label="%s"]' % (pn, pkg))
    try:
        req = subprocess.check_output(['rpm', '--query', '--requires', pkg])
    except:
        return
    if not req:
        contine
    for req in req.strip().splitlines():
        req = req.split(None, 1)[0]
        if '/' in req or '(' in req:
            continue
        rn = nodename(req)
        print ('%s[label="%s"]' % (rn, req))
        print ('%s -> %s [color=plum]' % (pn, rn))
        draw_req(req, depth+1)



parser = argparse.ArgumentParser()
parser.add_argument('--depth', type=int, default=MAX_DEPTH,
                    help='walk the tree that deep, default: %(default)s')
parser.add_argument('pkgname', nargs='+')
args = parser.parse_args()
MAX_DEPTH = args.depth

print GRAPH_HEADER % "XXX"
for pkg in args.pkgname:
    draw_req(pkg, 0)
print "}"
