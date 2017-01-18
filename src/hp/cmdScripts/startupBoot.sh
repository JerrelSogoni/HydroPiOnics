#!/bin/sh
# startupBoot.sh

cd /
cd home/pi/HydroPiOnics/src/hp/cmdScripts
sh motorBootup.sh &
sh humidiferBoot.sh &
sh airFilterBoot.sh &
sh airHeaterBoot.sh &
sh ledBoot.sh


