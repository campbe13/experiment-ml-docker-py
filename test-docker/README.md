# Run your script without installing python or scikit learn 

ref https://docs.docker.com/engine/reference/run/
ref https://docs.docker.com/engine/reference/commandline/build/

1.  `script.py` is used in the `Dockerfile`, change the name or ` ln algebra-ml.py script.py`
1.  `docker build -t myapp .`  build the image myapp is the name of the image
1.  `docker images`  look at the images
1.  `docker run -it --rm myapp`  run it interactively at the terminal: keep stdin open  `-i` run on a pseudotty `-t` and clean up volumes when finished`--rm`
