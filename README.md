# What is this


 This is an example of using google spreadsheetsi / smartsheet to hold ssh authz keys for a group of users.

currently it is done in this order but this can be easily changed

Owner,user,hostname,key


# How to implement



## possible installs required

See https://github.com/burnash/gspread for a better guide 

```
apt-get install python-oauth2client pip
pip install gspread
```

set up the credetial in sshtest.py currently setup for readonly to https://docs.google.com/spreadsheets/d/1II0DzsxRgtsNBlkt-BXL16gmxbxwBirWng119ZHBPmk/edit#gid=0

now install the code

```
cp sshtest.py /usr/bin
chown root:root /usr/bin/sshtest.py
chmod 766 /usr/bin/sshtest.py
```

Edit sshd_config
```
vi /etc/ssh/sshd_config
```

Add these lines 
```
AuthorizedKeysCommand /usr/bin/sshtest.py
AuthorizedKeysCommandUser nobody
```

systemctl restart sshd

And now you can login


