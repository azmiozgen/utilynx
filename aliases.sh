alias upup="sudo apt -y update && sudo apt -y upgrade && sudo apt -y dist-upgrade && sudo apt -y autoclean && sudo apt -y autoremove"
alias gitlog="git log --decorate --oneline --all --graph"
alias act="source activate"
alias deact="source deactivate"
alias sizeof="du -sh"

alias miletos="sshuttle -v -r tunnel@checkocr.demo.miletos.co 10.10.10.0/24 -e 'ssh -i $HOME/.ssh/azmi -v'"
alias monster="ssh azmi@monster.hq.miletos.co"
alias 1080ti="ssh thales@1080ti.hq.miletos.co"
alias 1050ti="ssh thales@10.10.10.235"

alias titanx="ssh azmi@160.75.26.191"
alias titan2x="ssh azmi@160.75.26.173"
alias titan3x="ssh azmi@160.75.26.246"
