<<<<<<< HEAD
git commit -a -m "commit before update by staff"
git pull staff master --allow-unrelated-histories --no-edit
git commit -a -m "commit after merge by staff"
=======
#!/bin/sh
git add .
git commit -m "Any uncommitted changes."
git fetch --unshallow origin
git pull staff master --allow-unrelated-histories --no-edit
>>>>>>> 25f08b9c85719775922a55bbfdd05f7e404c7b15
git push origin master
