# GoDemocracy (Concept for an 8h hackathon at Google Munich)

Did you ever pass by an election poster wondering what that party or candidate even stands for? With GoDemocray, you will get the answer!

![Testing the app](photos/paul3.JPG)

Scan an election poster with your phone's camera and instantly get information about the party and candidate. The result includes the following:
- Political views and values fetched from Wikipedia and the BR Mediathek.
- Positions regarding recent news topics from BR24.
- General information about elections and our political system from BR Alpha.

## Technology
We use Google's AutoML to detect the political party corresponding to the respective poster and achieve an accuracy of 95% with only less than 600 images training data.

After identifying the party, the app queries Wikipedia for general information and BR's BR24 web API for recent news involving the relevant party and persons. The iOS app then shows the results and adds information about the German voting and political system from BR's education channels.
