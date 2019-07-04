#!/usr/bin/env python3

import argparse
import sys
import math
from functools import reduce

#------------------------------------------------------------------------------
# command line arguments handling
parser = argparse.ArgumentParser()
parser.add_argument("command", 
                    choices =["equation", "eqnarray", "displaymath", "align",
			      "subequations", "itemize", "enumerate", "figure",
                              "multifigure", "eqref", "center", "columns", 
                              "tabular", "minipage", "block", "frame", 
                              "graphics"],
                    help="command to put")
args = parser.parse_args()

block=""

#------------------------------------------------------------------------------
# -- equation
if (args.command == "equation"):
  block ="""\\begin{equation}
  %\\label{eq:}
\\end{equation}""" 
# -- eqnarray
elif (args.command== "eqnarray"):
  block ="""\\begin{eqnarray}
  %\\label{eq:}
\\end{eqnarray}""" 
# -- displaymath
elif (args.command== "displaymath"):
  block ="""\\begin{displaymath}
\\end{displaymath}""" 
# -- subequations
elif (args.command== "subequations"):
  block ="""\\begin{subequations}
  %\\label{eq:}
  \\begin{align}
  \\end{align}
\\end{subequations}""" 
# -- itemize
elif (args.command== "itemize"):
  block ="""\\begin{itemize}
  %\setlength\itemsep{1.2em}
  \item
\\end{itemize}""" 
# -- enumerate
elif (args.command== "enumerate"):
  block ="""\\begin{enumerate}
  \item
\\end{enumerate}""" 
# -- tabular
elif (args.command== "tabular"):
  block ="""{\\renewcommand{\\arraystretch}{0.0}% for the vertical padding
  \\begin{tabular}{cc}
  \\end{tabular}
}""" 
# -- frame
elif (args.command== "frame"):
  block ="""%------------------------------------------------------------------- SLIDE -----
\\begin{frame}{}
\\end{frame}
""" 
# -- figure
elif (args.command== "figure"):
  block ="""\\begin{figure}[t]
  \\begin{center}
    \\includegraphics[width=0.99\\textwidth]{}
  \\end{center}
  \\caption{
  }
  %\\label{fig:}
\\end{figure}""" 
# -- graphics
elif (args.command== "graphics"):
  block ="""\\begin{center}
  \\includegraphics[width=0.99\\textwidth]{}
\\end{center}""" 
# -- multi-figure
elif (args.command== "multifigure"):
  block ="""\\begin{figure}[t]
  \\begin{center}
    \\begin{minipage}[t]{0.48\\textwidth}
    \\centering
    \\includegraphics[width=0.99\\textwidth]{}
    \\caption{
    }
    %\\label{fig:}
    \\end{minipage}
    \\hfill
    \\begin{minipage}[t]{0.48\\textwidth}
    \\centering
    \\includegraphics[width=0.99\\textwidth]{}
    \\caption{
    }
    %\\label{fig:}
   \\end{minipage}
  \\end{center}
\\end{figure}""" 
# -- reference to equation
elif (args.command == "eqref"):
  block ="Eq.~(\\ref{})"
# -- columns
elif (args.command == "columns"):
  block ="""\\begin{columns}[T]
  \\begin{column}{0.5\\textwidth}
  \\end{column}
  \\begin{column}{0.5\\textwidth}
  \\end{column}
\\end{columns}""" 
# -- minipage
elif (args.command == "minipage"):
  block ="""\\begin{minipage}{1.0\\textwidth}
\\end{minipage}""" 
# -- align
elif (args.command == "align"):
  block ="""\\begin{align}
\\end{align}""" 
# -- block
elif (args.command == "block"):
  block ="""\\begin{block}{}
\\end{block}""" 
# -- itemize
elif (args.command== "center"):
  block ="""\\begin{center}
\\end{center}""" 

#------------------------------------------------------------------------------
print(block)
