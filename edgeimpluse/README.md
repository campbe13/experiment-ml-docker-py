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

