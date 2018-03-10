set terminal x11 noraise
set xrange [0:20]
set yrange [-2:2]
plot "${PLOTDATA}" using 1:2 with lines
pause 0.05
reread

