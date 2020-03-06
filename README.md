# GoDemocracy

Did you ever pass by an election poster and ask yourself what that party or candidate even stand for? With **GoDemocracy**, that won't ever happen again!

![Testing the app](photos/paul3.JPG)


Simply scan an election poster with you phone's camera and instantly get information about the party and candidate on the poster: Their political views and values (from Wikipedia and BR Mediathek), their positions regarding recent news topics (from BR24) and general information about elections and our political system (from BR Alpha).

![Detailed party information](photos/paul2.JPG)



This app was built for and presented on the Bayerischer Rundfunk (BR) track at StudySmarter Hackathon in April 2019.

## Technology
We use Google's AutoML machine learning cloud to recognize an election poster's party. Using less than 600 images of training data for two parties (CSU and Grüne), it was possible to achieve an accuracy of 95%!

After it knows which party the poster belongs to, the app queries Wikipedia for general information about the party (and, possibly, the candidate) and BR's BR24 web API for recent news involving the relevant party and persons. This is combined with information about the general German voting and political system from BR's education channels and then shown beautifully on the iOS app.
