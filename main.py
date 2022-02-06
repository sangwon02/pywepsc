from indeed import extract_indeed_pages
from indeed import extract_indeed_jobs
import requests

last_indeed_pages = extract_indeed_pages()

extract_indeed_jobs(last_indeed_pages)

#노마드코드의 강의가 현재 인디드 페이지와 맞지않아 계속 공부하기에는 어려움이 있을듯
#웹개발과 자바 기초 파이썬 알고지즘 공부를 하는걸로 결정