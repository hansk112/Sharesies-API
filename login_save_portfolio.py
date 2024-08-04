import sharesies
import json
import os

client = sharesies.Client()

email = os.getenv('SHARESIES_EMAIL')
password = os.getenv('SHARESIES_PASSWORD')



if client.login(email, password):
  print('Login succeeded')
else:
  print('Login failed')

profile = client.get_profile()
# print(profile)>>
user_id = profile['user']['id']
# print(user_id)
portfolio = profile['portfolio']
# print(portfolio)



json_file = 'portfolio.json'

# Save the portfolio as a JSON file
with open(json_file, 'w') as file:
    json.dump(portfolio, file, indent=4)

print(f"Portfolio data has been saved to {json_file}")

