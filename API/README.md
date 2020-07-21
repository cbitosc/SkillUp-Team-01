# cosc-api : API for Vehicle Registration App
-------------------------------------------
The Rest API has been deployed to HEROKU.

Link : https://cosc-vehicle.herokuapp.com/

Everybody can use the below endpoints to access the tables in the database.

* _/login_             : takes a JSON object with 'user_id','password' and 'usertype' gives back JWT if exists in Users table. The JWT shall be used to access all the end points. 
                         For all the endpoints an Authorization Header should be included with value 'Bearer <JWT>'.
* _/register_ (POST)   : To post into Users table.
* _/vechreg_ (POST)    : To add a vehicle and it's details in the Registration table.The reg_status is by default pending.
* _/vechreg_ (GET)     : To get the details of any vehicle based on Registration ID (reg_id) provided.
* _/pending_ (GET)     : fetches details of all the registrations whose Registration Status (reg_status) is pending.
* _/pending_ (PUT)     : upadates the reg_status as **_approved_** based on the Registration ID (reg_id) provided. 
* _/dismiss_ (PUT)     : To update the reg_status as **_dismissed_** for the particular Registration ID (reg_id) provided.
                         A vehicle will be dismissed in case of Misbehavior.
* _/dismiss_ (GET)     : To fetch List of vehicles that have been dismissed.
* _/delete_ (PUT)      : For Updating the Registration Status as **_deleted_**.
* _/regstats_ (GET)    : To get data of registration table for the date provided by the user.
* _/fine_ (POST)       : To post a fine request and get back request_id.
* _/fine_ (PUT)        : To update the Payment Status as **_paid_** after receiving the Payment manually.
* _/fine_ (GET)        : To get the details of users whose payment_status is **_pending_**.
* _/paymentstats_(GET) : To get the details of fine payments made on a paticular date. The date will be provided by the user.
* _/regsuser_ (GET)    : To get the details of the vehicles registered based on the user_id provided.
