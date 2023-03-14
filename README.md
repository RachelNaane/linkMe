
# LinkMe

LinkMe is an app for storing links for future use.
In linkMe you can store links easily, and access them quickly without ever losing them. 

LinkMe is a flask app, and it uses mongodb in order to store and retrieve data, and nginx as a web server.
## Deployment

To deploy this project run

```bash
  docker build -t linkme .
  export APP_IMAGE=linkme
  docker-compose up -d
```

Docker compose will bring up 3 containers - the mongodb container, the LinkMe app and the nginx web server. The app will be available at localhost:80.

## Environment Variables

To run this project, you will need to set the following environment variables 

`APP_IMAGE`

The value of the variable need to be the name of the docker image build from the Dockerfile of this project.

You can set the value in 2 ways:
*  Run ```export APP_IMAGE=linkme ``` before running ```docker-compose up -d```
*  Create a .env file, and set the variable and the value - ```APP_IMAGE=linkme```
