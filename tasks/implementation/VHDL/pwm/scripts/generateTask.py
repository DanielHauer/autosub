#!/usr/bin/env python3

########################################################################
# generateTask.py for VHDL task pwm
# Generates random tasks, generates TaskParameters, fill
# entity and description templates
#
# Copyright (C) 2015 Martin  Mosbeck   <martin.mosbeck@gmx.at>
# License GPL V2 or later (see http://www.gnu.org/licenses/gpl2.txt)
########################################################################

import random
import math
import string
import sys

from jinja2 import FileSystemLoader, Environment
#################################################################

userId=sys.argv[1]
taskNr=sys.argv[2]
submissionEmail=sys.argv[3]
language=sys.argv[4]

paramsDesc={}

#find a good period, multiples of the 50MHz period and integer PWM frequency 
#smaller than 150 us (because of EdaPlayground Waveviewer plot limitation)
digit_possibles={0:1,1:2,2:5,3:10,4:20,5:25,6:50}
digit=digit_possibles[random.randrange(0,7)]
periodClks= digit*10**2


#duty between 10 and 90%
duty=random.randrange(10,91)
dutyClks=int(periodClks *duty/100)

#resulting values
period=periodClks*20 #in ns
frequency=10**9/period #in Hz

##############################
## PARAMETER SPECIFYING TASK##
##############################
#combine the clock counts
# period_duty#
# period is max 25000 ->ceil(ld(25000))=18 bit -->use 36 Bit
taskParameters= (periodClks<<18)+ dutyClks


############### ONLY FOR TESTING #######################
filename ="tmp/solution_{0}_Task{1}.txt".format(userId,taskNr)
with open (filename, "w") as solution:
    solution.write("For TaskParameters: " + str(taskParameters) + "\n")
    solution.write("Period clocks: " +str(periodClks) + "\n")
    solution.write("Duty clocks: " +str(dutyClks) + "\n")
#########################################################

################################################
# GENERATE PARAMETERS FOR DESCRIPTION TEMPLATE #
################################################
unitPeriod={0:" ns",1:" $\\mu$s",2:" ms"}
unitFrequency={0:" Hz",1:" kHz",2:" MHz"}
expPeriod=0;
expFrequency=0;
pwmFrequency=0;
pwmPeriod=0;
pwmDuty=0;

#find highes unit prefixes
for i in range(0,4):
   if int(period/(10**(3*i)))<10**3:
       expPeriod=i;
       period=period/(10**(3*(i)))
       break;
for i in range(0,4):
   if int(frequency/(10**(3*i)))<10**3:
       expFrequency=i;
       frequency=frequency/(10**(3*(i)))
       break;

#add the prefixes, convert to string
pwmFrequency=str(frequency)+unitFrequency[expFrequency]
pwmPeriod=str(period)+unitPeriod[expPeriod]
pwmDuty=str(duty)+" \\%"

###########################################
# SET PARAMETERS FOR DESCRIPTION TEMPLATE #
###########################################
# FRQ  Frequency
# DUTY Duty Cycle
paramsDesc.update({"FRQ":str(pwmFrequency),"PERIOD":str(pwmPeriod),"DUTY":str(pwmDuty)})
paramsDesc.update({"TASKNR":str(taskNr),"SUBMISSIONEMAIL":submissionEmail})

#############################
# FILL DESCRIPTION TEMPLATE #
#############################
env = Environment()
env.loader = FileSystemLoader('templates/')
filename ="task_description/task_description_template_{0}.tex".format(language)
template = env.get_template(filename)
template = template.render(paramsDesc)

filename ="tmp/desc_{0}_Task{1}.tex".format(userId,taskNr)
with open (filename, "w") as output_file:
    output_file.write(template)

###########################
### PRINT TASKPARAMETERS ##
###########################
print(taskParameters)
