# -*- coding: utf-8 -*-
from urllib2 import urlopen
import json
import requests
import urllib
from requests.exceptions import HTTPError
import xmltodict
from json import load, dumps
from twilio.rest import TwilioRestClient

api_key = "4dfq6ew5qq436anav5cr8ush"
cid = "55505"

six_south = 366304
hanover_inn = 365940
arrivalDate = "1/13/2014"
departureDate = "1/15/2014"

request_url = "http://api.ean.com/ean-services/rs/hotel/v3/avail"
url = "{request_url}?cid={cid}&minorRev=20&apiKey={apiKey}&locale=en_US&currencyCode=USD&hotelID={hotelID}&includeDetails=false&arrivalDate={arrivalDate}&departureDate={departureDate}&_type=json".format(
        request_url = request_url,
        apiKey = api_key,
        cid = cid,
        hotelID = hanover_inn,
        arrivalDate = arrivalDate,
        departureDate = departureDate
        )

availability = requests.get(url)
response = availability.json

account_sid = "ACb5c211f8b01ef21dca390641e6eb8c01"
auth_token = "2f77342f1df064879437cb815325fb98"
client = TwilioRestClient(account_sid, auth_token)


if response["HotelRoomAvailabilityResponse"]["@size"] > 0:
	message = client.messages.create(body="Rooms Available at Hanover Inn for Reunion", 
	to="781-223-3310", 
	from_="+17814714207")