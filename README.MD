# Geocoding

This small backend app returns the coordenates given a place name or address or return a place name given the coordenates.
Also calculates the distance between two places given their respective coordenates.

### Running With Docker

You can simply running with the command `docker build -t <your-prefered-tag> . && docker run -p 5000:5000 --env-file <path-to-your-env-file> <your-prefered-name>`


### Environment Variables

In order to run the project you will need to set up a file with the following variables
`OPEN_CAGE_API_KEY=<your-open-cage-api-key>  # you cand get it in https://opencagedata.com/api`

### Running Locally

- Create a virtual env
- Install the requirements `pip install -r requirements.txt`
- Run with `python -m app`
