# Dog API testing

The testing was not completed as due to a bug the model for dog profile needed to be updated. The dog_age was set to blank but not Null, which meant that the form validation didn't show that age was required, so if left empty it just didn't save. When this change was migrated something happened that got the error 

```django.db.migrations.exceptions.InconsistentMigrationHistory: Migration posts.0003_alter_post_dog_id is applied before its dependency dog_profile.0003_alter_dogprofile_dog_age on database 'default'.```

This meant that it wouldn't deploy - as this was during testing and the developer couldn't fix it alone, and as a bank holiday student tutors were closed till morning. This put a halt to the testing.

Therefore, userstories testing has not been completed. The list of tests is shown below without results means it has not been completed.

These tests were performed during development and passed.

## Validation

### PEP8 linter

- [PEP8Online.com](https://pep8ci.herokuapp.com/) was used to validate python coding

The results of the testing gave one error that was part of the standard set up of setting which will be left as this is part of the standard boilerplate code.

Here are the [results](/document/PEP8.pptx)

## Automated testing

Some automated testing was performed in posts.testing.py. It was adapted from the walkthrough to take account of the slightly different model. These tests pass when run locally with an appropriate database.

## User stories

These userstories are taken from the ones written on the project board. They don't have a specific explanation of what this enables the website to do. This is because generating/modifying/listing/deleting the data with the appropriate permissions are the aims. What the website decides to do with this doesn't need to be defined at the backend. The actions in themselves are the aim.


### user_profile app [#43](https://github.com/users/RachWalm/projects/4/views/1?pane=issue&itemId=59544320)

- As a user my profile is created when I sign up for an account

pass

- As a user I can create a user profile

pass

- As a user I can read a list of user profiles

pass

- As a user I can read a specific user profile

pass

- As a user I get an error if I put in an invalid user profile ID

pass detail: "Not found"

- As a user I can edit a user profile that I own

- As a user I can't edit a profile I don't own, but can view it

###  posts app [#45](https://github.com/users/RachWalm/projects/4/views/1?pane=issue&itemId=59589351)

- As a user I can create a post

- As a user I can read a list of posts

pass

- As a user I can read a specific post

pass

- As a user I get an error if I put in an invalid post ID

pass

- As a user I can edit a post that I own

- As a user I can't edit a post I don't own, but can view it

- As a user I can delete a post that I own

- As a user I can't delete a post that I don't own

###  comments app [#48](https://github.com/users/RachWalm/projects/4?pane=issue&itemId=59786064)

- As a user I can create a comment attached to a post

- As a user I can read a list of comments

pass

- As a user I can read a specific comment

pass

- As a user I get an error if I put in an invalid comment ID

pass

- As a user I can edit a comment I made

- As a user I can't edit a comment I don't own, but can view it

- As a user I can delete a comment that I own

- As a user I can't delete a comment that I don't own

###  favourite app [#50](https://github.com/users/RachWalm/projects/4/views/1?pane=issue&itemId=60073597)

- As a user I can create a favourite link to a dog

- As a user I can read a list of favourite connections

- As a user I can look at a specific favourite connection

- As a user I get an error if I put in an invalid favourite ID

- As a user I can remove a favourite connection that I own

- As a user I can't delete a favourite connection that I don't own

- As a database I can't store duplicate connections so that if something is deleted there isn't an old copy

###  dog profile app [#55](https://github.com/users/RachWalm/projects/4/views/1?pane=issue&itemId=60338529)

- As a admin I can create a dog profile

- As a user I can read a list of dog profiles

pass

- As a user I can read a specific dog profile

pass

- As a user I get an error if I put in an invalid dog profile ID

pass

- As a admin I can edit a dog profile 

- As a non-admin I can't edit a dog profile

- As an admin I can delete a dog profile

- As a non-admin I can't delete a dog profile

###  dog vaccine app [#56](https://github.com/users/RachWalm/projects/4/views/1?pane=issue&itemId=60338694)

- When a dog profile is created an associated dog vaccine is created

- As a staff/admin I can read a list of dog vaccine

- As a staff/admin I can read a specific dog vaccine

- As a user I get an error if I put in an invalid dog vaccine ID

- As a admin I can edit a dog vaccine 

- As a non-admin I can't edit a dog vaccine

- As an admin I can delete a dog vaccine

- As a non-admin I can't delete a dog vaccine

- As a staff/admin I can get a list of out of vaccination dogs id's

###  request_adopt app [#51](https://github.com/users/RachWalm/projects/4/views/1?pane=issue&itemId=60229234)

- As a user I can fill out the form and create a request to adopt a dog

- As a user it automatically selects the logged in user so that it can't be filled out with another users name

- As a user it won't let me fill out the form if I am not logged in so the user is attached to the form

- As a user I can edit my own requests so that I can make adjustments to the information in the adoption request

- As a user I can only edit my own requests so that I can't adjust someone elses data

- As a user I can delete my adoption request so that I can change my mind

- As a user I cannot delete someone elses users request so that I can't remove their data

- As a user I can see just one adoption request so I can focus on one request

pass as super user

- As a user I can see a list of adoption requests so that I can see all the requests at once

not as annoymous but can as superuser

- As a user I get an error if I put in an id that doesn't exist for an adoption request

pass as super user

### Filtering/Sorting/Search [#56](https://github.com/users/RachWalm/projects/4/views/1?pane=issue&itemId=60338694)

- As a user I can on the comments page order by updated_at and created_at, search the comment_content and filter by user so I can use the data for my own purpose

- As a user I can on the dog profile page count how many people have favourited this dog, order by fav count, updated_at and created_at, search the dog name and breed and filter by dog gender, size and if the home has cats, dogs, animals or children so I can use the data for my own purpose

- As a user I can on the dog vaccine page order by each vaccination next due and filter by overdue so I can use the data for my own purpose

- As a user I can on the favourite page count how many dogs a user has favourited, and how many times a dog has been favourited, order by dog name, user_id person_count and favourited_count as well as created_at, and filter by user or dog so I can use the data for my own purpose

- As a user I can on the posts page order by updated_at and created_at, search the title and content and filter by user or dog so I can use the data for my own purpose

- As a user I can on the request adopt page order by updated_at and created_at and filter by user or dog so I can use the data for my own purpose

- As a user I can on the user profile page count posts, comments, and number of dogs favourited, order by fav_count, updated_at and created_at and filter by how many dogs the user favourited so I can use the data for my own purpose

### Permission classes [#58](https://github.com/users/RachWalm/projects/4/views/1?pane=issue&itemId=61014500)

- As a user that hasn't logged in I can view posts, comments and dogs profiles

- As an authenticated user I can on the comments page create, read, update and delete comments I have made, but only view other users comments

- As an user on the dog profile page I can view the dogs profile but can't create, update or delete a dog profile.

- As a staff or super user  on the dog profile page I can create, view, update and delete a dog profile.

- As a user on the dog vaccine page my access is blocked unless 
1. staff and superusers can read the dog vaccine information
2. superusers can also update 

- Delete is denied as it is created by creation of the dog profile and deleted by cascade of deletion of the dog profile only to avoid extraneous records in the database.

- As an anonymous user on the favourite page I can see favourites, as an authenticated user I can create and delete them. There is no update function as the link exists or doesn't - there are no variables to update.

- All users (annoymous to super user) on the posts page can read posts, staff and above can create, update and delete their own posts but not anyone elses.

- As an annoymous user access is blocked to the request adopt page. As an authenticated user I can view/create/update/delete my own request but not anyone elses. super users can view all posts but not update or delete any that do not belong to them.

- As an authenticated user on the user profile I can read/update my profile but not create or delete as this is done by the auth model when a User is created.

### Superuser [#46](https://github.com/users/RachWalm/projects/4/views/1?pane=issue&itemId=59743374)

- As a super user I can log into the admin panel

pass

- As a super user I can view data stored in the admin panel

pass

- As a super user I can edit data stored in the admin panel

pass

- As a super user I can set roles to admin, staff and general in the admin panel

pass

### Authentication [#44](https://github.com/users/RachWalm/projects/4/views/1?pane=issue&itemId=59554583)

- When logged out can get list of profiles, and view individual profiles

- When logged in can get list of profiles, and view individual profiles, can edit our own profiles

- Can't edit profiles of other users when logged in