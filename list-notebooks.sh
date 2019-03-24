#!/usr/local/bin/zsh

for f in multigrid/*.ipynb;
    echo '- ['$f:t']''( https://colab.research.google.com/github/copper-multigrid-conference/2019-tutorials/blob/master/'$f')'

for f in algebraic-multigrid/*.ipynb;
    echo '- ['$f:t']''( https://colab.research.google.com/github/copper-multigrid-conference/2019-tutorials/blob/master/'$f')'
