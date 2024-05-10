# Comper recommandation

This Git contains the recommendation component of the LIRIS' COMPER project. It is mainly based on a python backend accessed through a rest API made with flask.

# Installation

The project is supposed to be hosted on a docker application for remote access. Install the python requirements with
```bash
pip install -r requirements.txt
```

# Usage

Once the application is deployed, you have to send requests to the API to get a recommendation. Here is an example in typescript :

The recommendation can be done through the profile engine with the route 

```typescript
const comperSuggestions = "url-of-the-recommendation-server/api/generate/";
```
Or by giving the profile directly through the request with

```typescript
const comperSuggestions = "url-of-the-recommendation-server/api/generateFromProfile/";
```

then you have to build your array of objectives; with the shape ['id-of-the-objective','intention'] e.g. :
```typescript
const objectives = ["using_for_loop","revision"];
```

if the traces are needed for analysis or explanation, the last objective must be :
```typescript
["sendTraces",""];
```

you then have to build a token with your key :
```typescript
const privateKey = "-----BEGIN RSA PRIVATE KEY-----EXAMPLE_KEY"

const dataBase = {
    user: "asker:" + username,
    username: username,
    role: "learner",
    keyid: "traffic",
    fwid: "83",
    exp: Date.now(),
    plateform: "asker"
  };

const data = {
      ...dataBase,
      "objectives": objectives
};

const token = jwt.encode(data, privateKey, 'RS256');
```

then you build and send your request :
```typescript
axios({
      method: 'POST', 
      url: comperSuggestions, 
      headers: { "Authorization": "Bearer " + token, "Accept": "application/json", "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" },
      data: JSON.stringify(profile) //If you have to include your profile with the request
    }).then(res => {
      setSuggestions(res.data.recommandation); //you get the recommendation results with this variable
      Texpl.getInstance().setRecoTraceText(res.data.traces); //you get the traces with this variable
    })
```

traces are a simple text string
the suggestions are an array of suggested resources that have the following attributes :
```python
reco = 
{
    "title" # name of the suggestion
    "location" # the URL where the suggestion can be found
    "learning_type" # type of resource : exercise or course snippet, as an example
    "learning_platform" # learning platform where the resource is hosted
    "objectiveNode" # objective node that was used to recommend the ressource
    "nobj" # objective number (if multiple objective were in the same request, it will be the number of the objective that led to this recommendation)
    "node"  # Parent node of the resource
    "tag" # tag used to recommend the resource (gives the reason why it was selected)
    "weight" # importance of the resource in the recommendation
}
```

# Project files

Here is a breakdown of the content of the files and folders :

data :
    Contains the local pedagogic strategies in the PS folder, and the traces of the recommendations in the LOG/86/ folder

recommandations :
    Contains the recommendation algorithm. It's divided in multiple folders :

    pedagogicStrategy :
        Components for reading and executing a pedagogic strategy. Those Python files are also used by the COMPER parameters project, this part reads the JSON of the pedagogic strategies to make it usable. If any modification is done on those, it should also be done on the parameters project. If you have the time, it should certainly be a package in itself, used by both projects.

    referential :
        Component for managing and using user's mastery profiles and course referencials.

    algorithm :
        Contains the "true" recommendation system, with the different phases. The entry point is algo.py.

    api :
        The rest API files are here, with the different functions used by the routes of the application.

    routes.py :
        The main entry point of the application, containing the API routes.

resources :
    static resources used by the application :

    grammar :
        The json metaschemas defining the shape of a pedagogic strategy

    rsaKeys :
        Keys for accessing the app, used for testing purpose.

Test : 
    Test files

# Contributing

To contribute, you have to be part of the COMPER project or its following projects.