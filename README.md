How to split coins
============

You are given any amount of money in the format `2.34`. 
This script is able to split this amount in the minimal amount of Euro coins, which represents the given number.
The expected format would be: [ 2, 0.2, 0.02, 0.1, 0.02 ]

The Euro coins are:

2€, 1€, 50¢, 20¢, 10¢, 5¢, 2¢, 1¢

Please implement this function.

Code-Golf:
----------------

Reduced the code to the minimal amount of characters. 

Duplicated Entries
===================

In a former project we had a contact form.
In our production database we have found multiple entries of the same user.

Please describe shortly your approach in debugging this situation and name 2-3 
different possible reasons for this kind of "bug".
For each option describe how we could fix this behaviour.

-----------------------------------

If it is a contact form, actually it sends email, 
it doesn't save anything in the database, so there aren't entries anywhere.
**FIX**: To prevent attacks there are some solutions like adding recaptcha, 
adding a honeypot, using session cookies, ask a test question.

If, anyway, the contact form also saves the data of the form somewhere, 
yes, there is no error on contacting more than once, 
and so using the same, with the same parameters (name, email. ...)
more than once.

**FIX**:In this case, again, it is possible to send more information than the 
one filled thought out the form by the user.
It is possible to manage sessions, or send sessions tokens even for
no-authenticated user can help on discriminate the information sent, 
as well as the timestamp, so in general hidden fields of the form, 
also the IP of the sender, the user-agent (the browser) and so on.
 

Could be a connection error
It is possible that the user performed POST action twice,
because of an error in the Javascript or because there were problems
in the Internet connection, and in general it can happen that the packets
that control that the information is correctly sent are missed themself, 
so the sender didn't receive the ACK (acknowledge).

**FIX**: there is no fix since you can't reproduce the bug.

If there is information duplicated it means that the database allows this, 
and so it depends on how the data management system was designed.
If the only key is the auto-increment index of the id, and there are no UNIQUE constraints 
(if we talk about a relational database), than we can't do so much, 
except for example giving more meaning to the more updated entries, 
and exclude the oldest ones.

**FIX**: rethink the DB, migrate data, clean data with scripts, and rethink 
tables or keys.

In general, to debug I will run the tests in the backend part, unit tests 
and functional tests, simulating the contact form, and I will add tests if there is the need.

Also I will debug by using the contact form as a real user, 
and logging some information in the backend, and then taking 
a look to error or warning messages.
Then I will write tests (TDD), and the I will implement the bug-fix, if any, 
or add new checks to the form or the backend part that checks that data.

File Parsing
============
By seeing the input.json was clear that was possible to repeat a 
Beacon, but with different timestamps, so I decided that eventually, a key, 
could be represented by BeaconId + its timestamp.

Then taking into account that a list of antenna_ids is provided, 
(for example [201,202,203,204,205,206]) it was possible to take advantage of
this data, because for example I know that for every beacon + timestamp
there are at least **len(antenna_ids)** data (where "len" returns the size of the array)

So I initialize the array with the default values [-135]
because I don't want to substitute the missing value after, 
but it's easier if I start with an array initialized with the missing values.

Then to keep the order of the antenna ids, I decided to use a function
in Python that returns the position of the item:
`antenna_ids.index(beacon["ant_id"])
`
so here  I get the position of ant_id in the list of antennas_ids, 
ando so I replace the value that I found, in that position.

Where I don't replace, the value -135 remains.

