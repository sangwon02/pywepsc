import requests

indeed_resul = requests.get("https://search.indeed.jobs/main/jobs?keywords=python&sortBy=relevance&page=1")

print(indeed_resul)