import requests
import email_sender

url = 'https://newsapi.org/v2/everything?q=tesla&from=2023-01-19&sortBy=publishedAt&apiKey=' \
      ''

request = requests.get(url=url)
contents = request.json()
content = ''
for article in contents['articles'][0:20]:
    if article['title'] or article['description'] is not None:
        content = content + "Title: " + (article['title']) + "\n" \
                  + "Description: "+(article['description']) + "\n" \
                  + "URL: " + article['url'] + 2 * "\n"
content = "Subject: Today's News" + 2 * '\n' + content + (2 * '\n') + 'Kind Regards \nNews Today!!'
content = content.encode('utf-8')

email_sender.email_sender(content)
