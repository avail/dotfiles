[[ -f ~/.bashrc ]] && . ~/.bashrc

eval $(ssh-agent)
ssh-add ~/.ssh/id_rsa

