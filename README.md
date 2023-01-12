# HCIPaper

> The main goal of the project is to conduct research in the context of the course "Human-Computer Interaction" (KU Leuven, Belgium). We chose this specific topic to try and improve matches for shelter dogs, since we believe this context has a lot of social benefit.

The research is about giving recommendations of dogs to people who are interested in adopting a dog. More specifically, we will be researching the effect of different levels of control on the acceptance of recommendations. This is done by creating 3 different versions of the questionnaire webpage: one with 5 questions, one with 5 questions and a weight for some questions, one with 10 questions and a weight for some questions. The participants each get one questionnaire webpage, randomly assigned. After the questionnaire, the participants will get to see their recommendations. They can then answer the questions ‘Hoe waarschijnlijk is het dat u het asiel zal contacteren voor meer informatie over de hond?’ (How likely are you to contact the shelter for more information about one of the dogs?) and ‘'Hoe goed sluiten de aanbevelingen aan bij uw verwachtingen?' (How well do these recommendations fit your expectations?). They can answer these questions by means of a slider. On the basis of these questions, we will measure the acceptance of the recommendations in relation to the level of control and time spent.

### The App

The site can be found [here](https://hondenzoeker.web.app/).
The backend is hosted on the KU Leuven server using picasso.
The database is hosted by [MongoDB](https://www.mongodb.com/atlas/database).

### The structure

Both the frontend code as well as the backend code is provided in this repo. You will find the respective folders in the root folder.

##### Frontend

The fronted is written in plain HTML5, SCSS and JavaScript. To bundle everything together, Parcel.js is used. This choice was made to avoid all the boilerplate code that comes with React or Angular or other frameworks, but keep access to npmjs packages which wouldn't be accessible if we didn't use Parcel.js as bundler.

##### Backend

The backend, written in Python, consists of a Flask REST API on top of a self-written recommender system based on the dogs of the dog shelter and the questions posed in the frontend. The data that it receives from the frontend is then stored in a [MongoDB](https://www.mongodb.com/atlas/database) cluster.

## The Team

- [Mout Pessemier](https://www.linkedin.com/in/moutpessemier/)
- [Jackie Vanheusden](https://www.linkedin.com/in/jackie-vanheusden-595960254/)
- [Nam Le](https://www.linkedin.com/in/nam-le-036069232/)
- [Charlotte Schneider](https://www.linkedin.com/in/charlotte-schneider-depr%C3%A9-b0a6b9238/)
