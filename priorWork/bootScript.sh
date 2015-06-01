CWD=$("pwd")

#turn off flashing leds, turn 0 on
cd /home/ubuntu/quad/util/
./all.sh 0
./set.sh 0 1

#execute the spi firmware script
../setup/once_runas_root_spi.sh

#return to starting directory
cd $CWD