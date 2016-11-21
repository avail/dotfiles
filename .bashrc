[[ $- != *i* ]] && return

colors() {
	local fgc bgc vals seq0

	printf "Color escapes are %s\n" '\e[${value};...;${value}m'
	printf "Values 30..37 are \e[33mforeground colors\e[m\n"
	printf "Values 40..47 are \e[43mbackground colors\e[m\n"
	printf "Value  1 gives a  \e[1mbold-faced look\e[m\n\n"

	# foreground colors
	for fgc in {30..37}; do
		# background colors
		for bgc in {40..47}; do
			fgc=${fgc#37} # white
			bgc=${bgc#40} # black

			vals="${fgc:+$fgc;}${bgc}"
			vals=${vals%%;}

			seq0="${vals:+\e[${vals}m}"
			printf "  %-9s" "${seq0:-(default)}"
			printf " ${seq0}TEXT\e[m"
			printf " \e[${vals:+${vals+$vals;}}1mBOLD\e[m"
		done
		echo; echo
	done
}

[ -r ~/.bash_aliases ] && . ~/.bash_aliases

[ -r /usr/share/bash-completion/bash_completion ] && . /usr/share/bash-completion/bash_completion

[[ $- != *i* ]] && return

alias ls='ls -l --color=auto'
alias ff='exec firefox & exit'
alias wireshark='tshark'

dot_progress() {
    local i='0'
    local line=''z

    while read line; do
        i="$((i+1))"
        if [ "${i}" = '25' ]; then
            printf '.'
            i='0'
        fi
    done
    printf '\n'
}

function extract()
{
    if [ -f $1 ] ; then
        case $1 in
            *.tar.bz2)   tar xvjf $1 | dot_progress     ;;
            *.tar.gz)    tar xvzf $1 | dot_progress     ;;
            *.bz2)       bunzip2 $1 | dot_progress      ;;
            *.rar)       unrar x $1 | dot_progress      ;;
            *.gz)        gunzip $1 | dot_progress       ;;
            *.tar)       tar xvf $1 | dot_progress      ;;
            *.tbz2)      tar xvjf $1 | dot_progress    ;;
            *.tgz)       tar xvzf $1 | dot_progress     ;;
            *.zip)       unzip $1 | dot_progress        ;;
            *.Z)         uncompress $1 | dot_progress   ;;
            *.7z)        7z x $1 | dot_progress         ;;
            *)           echo "'$1' cannot be extracted via >extract<" ;;
        esac
    else
        echo "'$1' is not a valid file!"
    fi
}

function parse_git_branch() {
	BRANCH=`git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/\1/'`
	if [ ! "${BRANCH}" == "" ]
	then
		STAT=`parse_git_dirty`
		echo "(${BRANCH}${STAT})"
	else
		echo ""
	fi
}

function parse_git_dirty {
	status=`git status 2>&1 | tee`
	dirty=`echo -n "${status}" 2> /dev/null | grep "modified:" &> /dev/null; echo "$?"`
	untracked=`echo -n "${status}" 2> /dev/null | grep "Untracked files" &> /dev/null; echo "$?"`
	ahead=`echo -n "${status}" 2> /dev/null | grep "Your branch is ahead of" &> /dev/null; echo "$?"`
	newfile=`echo -n "${status}" 2> /dev/null | grep "new file:" &> /dev/null; echo "$?"`
	renamed=`echo -n "${status}" 2> /dev/null | grep "renamed:" &> /dev/null; echo "$?"`
	deleted=`echo -n "${status}" 2> /dev/null | grep "deleted:" &> /dev/null; echo "$?"`
	bits=''
	if [ "${renamed}" == "0" ]; then
		bits=">${bits}"
	fi
	if [ "${ahead}" == "0" ]; then
		bits="*${bits}"
	fi
	if [ "${newfile}" == "0" ]; then
		bits="+${bits}"
	fi
	if [ "${untracked}" == "0" ]; then
		bits="?${bits}"
	fi
	if [ "${deleted}" == "0" ]; then
		bits="x${bits}"
	fi
	if [ "${dirty}" == "0" ]; then
		bits="!${bits}"
	fi
	if [ ! "${bits}" == "" ]; then
		echo " ${bits}"
	else
		echo ""
	fi
}

export PS1="\[\e[31m\]\u\[\e[m\]@\[\e[31m\]\h\[\e[m\] \w \`parse_git_branch\`\[\e[34m\]\\$\[\e[m\] "
