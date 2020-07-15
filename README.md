## twist

### The Objective:
I want to write some code that analyses gyro data from an IMU and spots _twisting_ motions.
A _twist_ is rotating the IMU in one direction and then back to where it started, in a relatively short time period.

### The Overcomplication:
I could probably just find an existing algorithm to do this, but I want to use a ~~R~~NN (~~Recurrent~~ Neural Network). Why? Because its a flex.


### The plan:

* ~~find out how RNNs work~~
* ~~find out how to format training data for RNNs~~
* record training data with my arduino and IMU
* train ~~R~~NN
* ???...profit?


### Training:
#### Collect:
* run sketch on arduino to record and transmit single gyro data packet (1 second @ 100hz of 3d gyro data)
* use `collect_train_data.py`  to collect the packet and enter t/n for twist/not twist
* `collect_train_data.py` will save this data upon exiting into `/data`
#### Process:
* collect data from `/data` and combine into numpy array suitable for training
#### Train:
* train simple neural network on numpy array of training data
### Running:
#### Collect:
* run `broadcast_data` sketch on arduino to broadcast constant steam of gyro data
#### Process:
* package data from `broadcast_data` sketch into 1 second packets
#### Classify:
* run packets through trained neural net and print twist when detected
