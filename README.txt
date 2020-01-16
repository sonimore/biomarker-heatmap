1/26/2020

Instructions for running heatmap code (for mac only):

1. Go to launchpad and in the search window on top type "terminal". Launch that application.

2. Next, we need to access the directory that the heatmap code is in using the terminal window that you just opened. The path to my directory is: 

/Users/smoreno/Dropbox" (Partners HealthCare)"/bms025/heatmap

Yours will likely be somthing similar:

/Users/{your_username_on_computer}/Dropbox" (Partners HealthCare)"/bms025/heatmap

You can double check by going into your finder window, navigating to the directory there, right clicking on the folder "heatmap", holding down the "option" key on your keyboard, and clicking on the option "Copy heatmap as pathname".

In the terminal window you opened, type in

cd {your_pathname}

In my case, I type 

cd /Users/smoreno/Dropbox" (Partners HealthCare)"/bms025/heatmap

Now you've navigated into the directory where the heatmap is, you're halfway there yay!

3. If you have Python3 installed already, then skip this step (you can check by typing "python --version" in your terminal window (without the quotes). Otherwise, download it by using a tutorial online :) 

I recommend option one from this one: https://www.saintlad.com/install-python-3-on-mac/


4. In your terminal window, type:

python3 -m http.server 1010

5. Open up a web browser (Firefox works best for me when running this, Chrome should work fine too) and type in the url: 

http://0.0.0.0:1010/

6. A few different links should appear. Click on any of the links ending with '.html' to navigate to the respective heatmaps.

Everything should be up and running now, hoorah! Let me know if you run into any issues.
