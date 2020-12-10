#!/bin/sh
git add .
git commit -m "Any uncommitted changes."
git fetch --unshallow origin
git pull staff master --allow-unrelated-histories --no-edit
<<<<<<< HEAD
git push origin master
=======
git push origin master
>>>>>>> f9051954353bdf7dafc8727fe3d5a4692c9a9096
