## twist

### The Objective:
I want to write some code that analyses gyro data from an IMU and spots _twisting_ motions.
A _twist_ is rotating the IMU in one direction and then back to where it started, in a relatively short time period.

### The Overcomplication:
I could probably just find an existing algorithm to do this, but I want to use a RNN (Recurrent Neural Network). Why? Because its a flex.


### The plan:

* find out how RNNs work
* find out how to format training data for RNNs
* record training data with my arduino and IMU
* train RNN
* ... profit?
