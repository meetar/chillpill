#chillpill

A twitter bot that checks the most recent tweet and deletes it if it's all caps.

###Requirements

- An always-up server, if you want the bot to run at all times
- A Twitter account
- A command line shell with Python

###Installation

1. Log in to the Twitter account you want to apply the bot to.
2. Create a new app at http://apps.twitter.com (none of the details really matter here)
3. If you haven't already, associate a mobile number with the Twitter account https://twitter.com/settings/add_phone – you'll need to enter a confirmation code texted to your phone (required for app "write" permissions)
4. In the Permissions tab, set Access Level to "Read and Write"
5. In the Keys and Access Tokens tab, "Regenereate Consumer Key and Secret", then "Create my access token"

You now have a Twitter app, with four secret keys.

Then, in your copy of this repository, edit the keys.py file and fill in the values with your new keys, as well as the username for the Twitter account in question.

Upload chillpill.py and keys.py to your server someplace.

Run the bot as a background process, outputting to a file called nohup.out, with this command:

`nohup python chillpill.py &`

If you need to kill the bot, find the process id with

`ps aux | grep '[p]ython'`
and then
`kill [id#]`


###CAUTION!

Please make certain your keys.py file is not in a publicly accessible location.

###DON'T PANIC!

It's good advice.
