# coding-blog
coding adventures with oran: a central place for all my coding writeups found in repo's readme's    


# install 
```
pip install -r requirements.txt
```
# run 
```
python ./update.py
```
#### writes the resulting updated blog posts to index.html file 

# how to run docker container to build updated version of blog
```
docker build -t wisehackermonkey/blog-updater:latest .
(POWERSHELL)
v1
docker run --rm -it wisehackermonkey/blog-updater:latest
v2
docker run --rm -it -v ${PWD}:/app --name blog wisehackermonkey/blog-updater:latest

```

# Publish
```
docker login
docker push wisehackermonkey/blog-updater:latest
```


# Scratch pad
```
# sudo docker run -v ${{ github.workspace }}:/app  wisehackermonkey/blog-updater:latest

```
# TODO
- ~~docker container
    - ~~pass github username as docker env variable
- ~~build github action
    - ~~trigger github action on commit from other OR change from repo    
