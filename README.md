# Quote checker

Project works on Python 3+ and Django 2+.
Simply, run the following command:
```
docker-compose up --build
```

Once the application starts, the **API key** will be generated to be tested by the client side

client must pass the **API key** via the Authorization header. It must be formatted as follows:
 ```
Authorization: Api-Key <API_KEY>
```