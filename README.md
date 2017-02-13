# WhatsAppLog
Take an output of a WhatsApp conversation where I log exercise and sum all the entries to give a total and average required to meet target

At the start of each year I usually participate in a 'challenge' to exercise [run, row, walk] a number of kms by a peredfined date. Each days total is usually exchanged in a whatsap group. I got sick of manually adding up each entry to give a total to date so wrote a symple python script to do it. As entries are logged in the whatsapp message they must be prefaced with a tag followed by the number of kms/miles so that they can be identified e.g. mykms:10  The output gives the total to date for that particular tag and the daily average that is reqiured from now until the end of the challenge to meet the target.

To use:

1. In whatsap record your kms/miles with a code at the start - like this "dlog:10 run" You'll need to use the same code for every entry or else it wont be counted.

2. In whatsap(on you phone) click on the message/contact at the top.

3. Scroll down to bottom and press export chat > Without Media > mail > send it to yourself.

4. On your laptop open your mail and save the attacment that you sent yourself. It should be downloaded as something like "_chat 2.txt"

5. Copy that file to your desktop. Rename it to chat.txt - it must be exactly that name.

6. Save the file log.py to your desktop

7. On a mac open a terminal. Do this by pressing cmd and spacebar at the same time. A window pops up - type in terminal and hit enter. A terminal window should pop up.

8. Type in python2.7 log.py

9. It will ask you to type in your code - e.g. dlog: then press enter.

10. It should output what you have done so far, how may days left to the end of your target and what you need to average per day to hit your target. 
