wmctrl -r :ACTIVE: -b add,fullscreen
wmctrl -r :ACTIVE: -b add,below
wmctrl -r :ACTIVE: -b add,skip_taskbar
while true; do (( RANDOM % 2 )) && echo -ne "\e[3$(( $RANDOM % 8 ))m╱" || echo -n ╲; sleep 0.005; done
