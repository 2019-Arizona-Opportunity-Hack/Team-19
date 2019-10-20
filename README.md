As you can tell this is the README and documentation for the SOL Adoption Candidate Tracker

Purpose: 
The purpose of this project was to optmize the process for reviewing and sotring adoption applicants for SOL. 

Goals:
Database, adoption score, export adopter list, sharing amoung orginzations.
Implention: 
Mongo DB, Flask, Python, Docker

Outcome:
Import CSV/JSON file, loads into Data base, machine learning is used to determine a score to see if an adopter is a good choice. Then the data is sent to a web dashboard where it can be easially viewed and exported into another csv file.  All data is in a database which can be easialy shared with other organization to help to unify the process of applyinf for a cat adoption and to share resources and lists such as a adoption BlackList.  

Docs: 

Setup:

Clone Repo
Build and image from the dockerfile included in the repo
try it out at localhost:5555
go to localhost:5555/adopterData to se demo of system. 
export data from localhost:5555/

