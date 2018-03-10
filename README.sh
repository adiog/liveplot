mktemp -p /dev/shm > PLOTDATA
mktemp -u -p /dev/shm > PLOTFIFO
mkfifo `cat PLOTFIFO`
python sampler.py > `cat PLOTFIFO` &
python plotter.py 20 `cat PLOTFIFO` `cat PLOTDATA` &
cat liveplot.plt | PLOTDATA=`cat PLOTDATA` envsubst > PLOTDESC
gnuplot PLOTDESC

