import random as rd
import smtplib
from email.message import EmailMessage

def if_alp_or_num():
    return rd.randint(0, 1)

def gen_number():
    return str(rd.randint(0,9))

def gen_alpha():
    return rd.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')


def make_otp(length):

    otp = ""

    for i in range(length):
        flag = if_alp_or_num()

        if flag:
            element = gen_number()
        else:
            element = gen_alpha()

        otp+=element

    return otp


def send_otp_email(receiver_email,password ,otp_code):
    pass







