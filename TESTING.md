# Dog API testing

## Validation

### PEP8 linter

- [PEP8Online.com](https://pep8ci.herokuapp.com/) was used to validate python coding

### user_profile app [#43](https://github.com/users/RachWalm/projects/4/views/1?pane=issue&itemId=59544320)

As a user I can create a user profile

As a user I can read a list of user profiles

As a user I can read a specific user profile

As a user I get an error if I put in an invalid user profile ID

As a user I can edit a user profile that I own

As a user I can't edit a profile I don't own, but can view it

###  posts app [#45](https://github.com/users/RachWalm/projects/4/views/1?pane=issue&itemId=59589351)

As a user I can create a post

As a user I can read a list of posts

As a user I can read a specific post

As a user I get an error if I put in an invalid post ID

As a user I can edit a post that I own

As a user I can't edit a post I don't own, but can view it

As a user I can delete a post that I own

As a user I can't delete a post that I don't own

###  comments app [#48](https://github.com/users/RachWalm/projects/4?pane=issue&itemId=59786064)

As a user I can create a comment attached to a post

As a user I can read a list of comments

As a user I can read a specific comment

As a user I get an error if I put in an invalid comment ID

As a user I can edit a comment I made

As a user I can't edit a comment I don't own, but can view it

As a user I can delete a comment that I own

As a user I can't delete a comment that I don't own

###  favourite app [#50](https://github.com/users/RachWalm/projects/4/views/1?pane=issue&itemId=60073597)

As a user I can create a favourite link to a dog

As a user I can read a list of favourite connections

As a user I can look at a specific favourite connection

As a user I get an error if I put in an invalid favourite ID

As a user I can remove a favourite connection that I own

As a user I can't delete a favourite connection that I don't own

As a database I can't store duplicate connections so that if something is deleted there isn't an old copy

###  request_adopt app [#51](https://github.com/users/RachWalm/projects/4/views/1?pane=issue&itemId=60229234)

As a user I can fill out the form and create a request to adopt a dog

As a user it automatically selects the logged in user so that it can't be filled out with another users name

As a user it won't let me fill out the form if I am not logged in so the user is attached to the form

As a user I can edit my own requests so that I can make adjustments to the information in the adoption request

As a user I can only edit my own requests so that I can't adjust someone elses data

As a user I can delete my adoption request so that I can change my mind

As a user I cannot delete someone elses users request so that I can't remove their data

As a user I can see just one adoption request so I can focus on one request

As a user I can see a list of adoption requests so that I can see all the requests at once

As a user I get an error if I put in an id that doesn't exist for an adoption request

### Superuser [#46](https://github.com/users/RachWalm/projects/4/views/1?pane=issue&itemId=59743374)

As a super user I can log into the admin panel

As a super user I can view data stored in the admin panel

As a super user I can edit data stored in the admin panel

As a super user I can set roles to admin, staff and general in the admin panel

### Authentication [#44](https://github.com/users/RachWalm/projects/4/views/1?pane=issue&itemId=59554583)

When logged out can get list of profiles, and view individual profiles

When logged in can get list of profiles, and view individual profiles, can edit our own profiles

Can't edit profiles of other users when logged in