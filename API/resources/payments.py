from flask_restful import Resource,reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import jwt_required
from db import query
import datetime

class FinePayments(Resource):
    @jwt_required
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('user_id',type=str,required=True,help="User_id cannot be left blank!")
        parser.add_argument('reg_id',type=str,required=True,help="reg_id cannot be left blank!")
        parser.add_argument('type_of_request',type=str,required=True,help="type_of_request cannot be left blank!")
        data=parser.parse_args()
        try:
            query(f"""INSERT INTO PAYMENTS(user_id,reg_id,type_of_request,fine,payment_status,payment_date)
                                    VALUES('{data['user_id']}',
                                           '{data['reg_id']}',
                                           '{data['type_of_request']}',
                                           '200',
                                           'pending',
                                           '{datetime.date.today()}')""")
        except:
            return {"message": "An error occurred."}, 500
        return query(f"""SELECT MAX(request_id) FROM CBIT_PARKING.PAYMENTS WHERE user_id='{data['user_id']}' AND reg_id='{data['reg_id']}'AND payment_date='{datetime.date.today()}'""",return_json=False)[0]

    @jwt_required
    def put(self):
        parser=reqparse.RequestParser()
        parser.add_argument('request_id',type=int,required=True,help="please give request_id")
        data=parser.parse_args()
        try:
            query(f"""UPDATE CBIT_PARKING.PAYMENTS SET payment_status='paid',payment_date='{datetime.date.today()}' WHERE request_id={data['request_id']}""")
        except:
            return {"message":"there was an error updating the payment_status"},500
        return {"message":"successfully updated"},201

    @jwt_required
    def get(self):
        try:
            return query(f"""SELECT * FROM CBIT_PARKING.PAYMENTS WHERE payment_status='pending'""")
        except:
            return {"message":"there was an error retrieving the data"},500
        
class PaymentStats(Resource):
    @jwt_required
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('payment_date',type=str,required=True,help="please give the date")
        data=parser.parse_args()
        try:
            return query(f"""SELECT * FROM CBIT_PARKING.PAYMENTS WHERE payment_date='{data['payment_date']}'""")
        except:
            return {"message":"There was an error displaying the data"},500 
        