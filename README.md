# Find out who doesn't follow you back on IG

1. Login to IG and download your data. You can find instructions [here](https://help.instagram.com/181231772500920)

2. Select JSON as the format.

3. Check your email for a message containing a link to download your data.

4. Click the link and download the data to your computer.

5. Locate the downloaded data and open the folder called "followers_and_following". Inside this folder, find the files "followers.json" and "following.json".

> if you want to use terminal, you can skip to the [code block](#terminal)

6. Create a new folder on your computer and copy the "followers.json" and "following.json" files into it.

7. Open the new folder in a code editor such as Visual Studio Code and create a new file called "ig.py".

8. Copy the code from the ig.py file of this repository into the "ig.py" file that you just created.

9. Run the "ig.py" file.

## <a name="terminal"></a>Terminal

```
$ git clone https://github.com/cng008/ig-no-follow-back.git
<!-- drag files toig-no-follow-back folder -->
$ python ig.py
```
