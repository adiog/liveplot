import sys

resolution = sys.argv[1]
pipe = sys.argv[2]
live = sys.argv[3]

plot = [0.0 for x in range(int(resolution))]

while True:
    print("Opening FIFO...")
    with open(pipe) as fifo:
        print("FIFO opened")
        while True:
            data = fifo.readline()
            if len(data) == 0:
                print("Writer closed")
                break
            plot = plot[1:] + [float(data)]
            with open(live, "w") as liveplot:
                for x,y in enumerate(plot):
                    liveplot.write("{} {}\n".format(x,y))
            print('Read: "{0}"'.format(data))
