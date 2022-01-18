## linear regression
simple algebraeic function, uses scikit learn

because we are determining the results of a simple function using ml is overkill for this particular problem
it is here as an illustration of using ML  `f(x,y,z)  = x + 2y + 3z`


* ml.py 
    * training: generates random x,y,z uses them as input dataset, runs function to create corresponding output dataset
* ml-timeit.py  same as above, using timeit to benchmark 
* popy.py 
    * shows the plain old python code to do the same as the trained model
* popy-timeit.py  same as above, using timeit to benchmark 