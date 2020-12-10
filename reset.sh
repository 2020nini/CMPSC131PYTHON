#!/bin/sh
echo "Initializing reset of cmpsc131python repository..."

echo "Creating backup..."
git add .
git commit -m "All your old stuff"
<<<<<<< HEAD
<<<<<<< HEAD
git checkout -b backup
git push origin backup
=======
branch=backup.$(date +"%s")
git checkout -b $branch
git push origin $branch
>>>>>>> f9051954353bdf7dafc8727fe3d5a4692c9a9096
echo "...done"

echo "Rolling back commits..."
git branch -D master
<<<<<<< HEAD
git checkout -b master
=======
branch=backup.$(date +"%s")
git checkout -b $branch
git push origin $branch
echo "...done"

echo "Rolling back commits..."
git branch -D master
git checkout -b master 4741ebdd0e1b7a55b2f28261a3ff62f45da9b18a 
>>>>>>> 25f08b9c85719775922a55bbfdd05f7e404c7b15
=======
git checkout -b master 4741ebdd0e1b7a55b2f28261a3ff62f45da9b18a 
>>>>>>> f9051954353bdf7dafc8727fe3d5a4692c9a9096
echo "...done"

echo "Running setup..."
git remote add staff https://github.com/psu-cmpsc131-fa20/CMPSC131PYTHON.git
<<<<<<< HEAD
<<<<<<< HEAD
git pull staff master --allow-unrelated-histories
=======
git pull staff master --allow-unrelated-histories --no-edit
>>>>>>> 25f08b9c85719775922a55bbfdd05f7e404c7b15
=======
git pull staff master --allow-unrelated-histories --no-edit
>>>>>>> f9051954353bdf7dafc8727fe3d5a4692c9a9096
git push -u origin -f master
echo "...done"
