#Lecture 23 : Python Project Youtube manager with mongoDB
#Supporting Lecture 23.1 : Watch this before installing any database | link → https://www.youtube.com/watch?v=j4YeLqxgj1k


#----------------------------------Requirement for local database (optional → not required in this project)-----------------------------------
#VS Code Extension Required : 1. mongoDB 2. Docker
#New Application Required (just like python): 1.Docker installed
#Setup : git clone https://github.com/hiteshchoudhary/docker-databases
# Python 3rd party library → pymongo → pip/pip3 install pymongo → https://pypi.org/project/pymongo/
#---------------------------------------------------Local Requirement end -------------------------------------------------------------------

#----------------------------------------------Current Requirement (We currently use)--------------------------------------------------------
# MongoDB Atlas → make a new account → work on online DB 
# Atlas steps 1:  Login → Create/Select a project → Create/Select a cluster 
# Atlas steps 2:  In project (say youtube) → In sidebar → Database & Network Access → Network Aceess → IP Access List → Add IP Address → (0.0.0.0/0) (for testing purpose only, in real world we will add only our IP address)
# Atlas steps 3:  In project (say youtube) → In sidebar → Database & Network Access → Database Access → Database Users
# Atlas steps 4:  In Project → Cluster0 → click 'connect' → select 'compass' → (I don't have MongoDB Compass installed, Windows 64-Bit) → copy link → Done
# Python 3rd party library → pymongo → pip/pip3 install pymongo → https://pypi.org/project/pymongo/
#-----------------------------------------------------------Requirement End-----------------------------------------------------------------

#-------------------------------------------Credential of Atlas---------------------------
#atlas account → login with google → hda@g.c | DB_Name → youtube | username → thearyandev, password → thearyandev

#------------------------------------------Documentation---------------------------------------
# https://pypi.org/project/pymongo/ → go to this to read basic syntax of pymongo.

#-------------------------------------------NOTE-----------------------------------------
# we need to send data like (id) → in BSON format → conversion from string to bson : ObjectId(your_data) → just like you do int('10') or str(10) → BUT to use ObjectId() you need to first import JSON → or from bson import ObjectId
# Where will you find/view data in Atlas? → mongoDB_Atlas_Dashboard → Sidebar → Database → Data explorer → Clusters (connect it) → your_db_name_appers_here (eg. youtube_manager_db)
# to check how many total packages are installed on your python/device? → pip3 list