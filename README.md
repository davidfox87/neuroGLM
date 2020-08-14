# neuroGLM

Fitting and simulation of linear guassian and Poisson generalized linear model (GLM) for single neuron spike trains

**Description:**
-
computes estimates for the parameters of a linear Gaussian GLM spike train model.

The GLM is a regression model used to characterize the relationship between external or internal covariates and a set of
recorded spike trains
 
In systems neuroscience, the label “GLM” often refers to an autoregressive point process model, a model in which 
linear functions of stimulus and spike history are nonlinearly transformed to produce the spike rate

Parameters of GLMs consist of a stimulus temporal filter, which describes how a neuron integrates past stimuli,
a spike-history filter, which captures the influences of previous spiking on the current probability of spiking,
and a scalar that captures the baseline level of spiking. 
The outputs of these filters are summed and passed through a nonlinear function to 
to generate a prediction of spike rate. 

The weights on the temporal filter are found using using ridge regression and cross-validation is used to find
the best ridge penalty. A nonparametric nonlinearity is then fit to the data to scale the filtered stimulus, which is
used to make a prediction of the response to the stimulus (given by spike rate).
Maximum-likelihood and MAP estimation methods can also estimate filter weights assuming an exponential 
nonlinearity and poisson spike rate.  

**Installation:**
-
To install the modules, all you have to do is the following:
   1) download dist/NeuroGLM-1.0.tar.gz
   2) unpack it
   3) from the NeuroGLM-1.0 directory run python setup.py install

**System Requirements**
-
PY

**Usage:**
-
Examine test scripts in sub-directory tests/ to see simple scripts illustrating how to fit stimulus temporal and 
spike history filters to spike train data.

Also to come is a jupyter notebook with embedded code and plots

**Credits:**

**License:**








