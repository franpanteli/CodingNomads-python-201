'''
Write a program that makes a DELETE request to remove the user your create in a previous example.

Again, make a GET request to confirm that information has been deleted.

'''

import requests

#api endpoint
api_endpoint = "http://demo.codingnomads.co:8080/tasks_api/users"

breakpoint()  # Pause before making the DELETE request

#make post request
response = requests.delete(api_endpoint + "/15567") #make a delete request for the John Does user

breakpoint()  # Pause after DELETE request to inspect the response

#making a get request to confirm that the user has been deleted
contents = requests.get(api_endpoint).content

breakpoint()  # Pause after GET request to inspect returned contents

print(contents) #b'{"data":[{"id":15542,"email":"krobertazzi0@wired.com","first_name":"Kendal","last_name":"Robertazzi","created_at":1758844800000,"updated_at":1758844800000},{"id":15543,"email":"ccallow1@xinhuanet.com","first_name":"Corrinne","last_name":"Callow","created_at":1758844800000,"updated_at":1758844800000},{"id":15544,"email":"nwolland2@over-blog.com","first_name":"Niall","last_name":"Wolland","created_at":1758844800000,"updated_at":1758844800000},{"id":15545,"email":"mdavenhill3@exblog.jp","first_name":"Marlowe","last_name":"Davenhill","created_at":1758844800000,"updated_at":1758844800000},{"id":15546,"email":"spudding4@webmd.com","first_name":"Selia","last_name":"Pudding","created_at":1758844800000,"updated_at":1758844800000},{"id":15547,"email":"eixer5@indiatimes.com","first_name":"Edyth","last_name":"Ixer","created_at":1758844800000,"updated_at":1758844800000},{"id":15548,"email":"crex6@google.ca","first_name":"Catherin","last_name":"Rex","created_at":1758844800000,"updated_at":1758844800000},{"id":15549,"email":"gbrain7@joomla.org","first_name":"Guendolen","last_name":"Brain","created_at":1758844800000,"updated_at":1758844800000},{"id":15550,"email":"echeake8@shop-pro.jp","first_name":"Etta","last_name":"Cheake","created_at":1758844800000,"updated_at":1758844800000},{"id":15551,"email":"mlashmar9@uiuc.edu","first_name":"Marcelia","last_name":"Lashmar","created_at":1758844800000,"updated_at":1758844800000},{"id":15552,"email":"rtrodlera@t.co","first_name":"Rickard","last_name":"Trodler","created_at":1758844800000,"updated_at":1758844800000},{"id":15553,"email":"zroblinb@java.com","first_name":"Zabrina","last_name":"Roblin","created_at":1758844800000,"updated_at":1758844800000},{"id":15554,"email":"djahndelc@vkontakte.ru","first_name":"Dal","last_name":"Jahndel","created_at":1758844800000,"updated_at":1758844800000},{"id":15555,"email":"mdecarolid@cocolog-nifty.com","first_name":"Mirabel","last_name":"De Caroli","created_at":1758844800000,"updated_at":1758844800000},{"id":15556,"email":"bhakeye@businesswire.com","first_name":"Brina","last_name":"Hakey","created_at":1758844800000,"updated_at":1758844800000},{"id":15557,"email":"irubbertf@si.edu","first_name":"Ilyssa","last_name":"Rubbert","created_at":1758844800000,"updated_at":1758844800000},{"id":15558,"email":"bmablyg@opera.com","first_name":"Bari","last_name":"Mably","created_at":1758844800000,"updated_at":1758844800000},{"id":15559,"email":"ucumbersh@cam.ac.uk","first_name":"Ursala","last_name":"Cumbers","created_at":1758844800000,"updated_at":1758844800000},{"id":15560,"email":"glillemani@bandcamp.com","first_name":"Garner","last_name":"Lilleman","created_at":1758844800000,"updated_at":1758844800000},{"id":15561,"email":"acastellanij@theatlantic.com","first_name":"Amos","last_name":"Castellani","created_at":1758844800000,"updated_at":1758844800000}],"error":{"message":"none"},"status":"200 OK"}'

#the user has been deleted from the database
