# set up the training data for the rpi

first I will use the prebuilt dataset
then can connect a phone and set up my own

## original project
https://docs.edgeimpulse.com/docs/audio-classification
instructions for building own data set via phone or other devices 

5x1 minute of target sound (ex faucet running)
5x1 minute of noise 

## prebuilt data set 
https://docs.edgeimpulse.com/docs/running-faucet

1. install uploader https://docs.edgeimpulse.com/docs/cli-installation
1. download `wget https://cdn.edgeimpulse.com/datasets/faucet.zip`
2. unzip
3. upload 
   1. `edge-impulse-uploader --clean`
   1. `edge-impulse-uploader --category training faucet/training/*.cbor`
   1. `edge-impulse-uploader --category testing faucet/testing/*.cbor`

## on the Raspberry Pis
for full info see my [engr log for setup](https://docs.google.com/document/d/1p_lMzSajbariFG9m-hjeu7plwu8Sy22_FReBc6XZi-w/edit?usp=sharing)

roughly 

install
1.    curl -sL https://deb.nodesource.com/setup_12.x | sudo bash -   
1.    `sudo apt install -y gcc g++ make build-essential nodejs sox gstreamer1.0-tools gstreamer1.0-plugins-good gstreamer1.0-plugins-base gstreamer1.0-plugins-base-apps`
1.    `sudo npm install edge-impulse-linux -g --unsafe-perm`
connect to the web component (1x it will be cached)
1. `edge-impulse-linux  # (authenticate w uid and password)`
once the data has been used to train the model on the edge website, run it locally
1. `edge-impulse-linux-runner `

