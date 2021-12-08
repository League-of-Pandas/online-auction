# Software Requirements

## Vision

An online auction website that offers variety of valuables, collectables, cars, electronics and much more for the users to browse and bit on.

A modern and secure method to bit on your needs without getting mixed in public crowds and to guarantee your safety

## Scope

### In

The website will provide the ability for users to browse and bid on items offered by other users.

If the user wasn't sure and hesitated to bid on a certain item, he/she can use the saving feature to come back again any time and bid on it.

The user can see a detailed information about every item like it's current bid price, bidding increment, bidding history and closing time.

The user can search for items by name and browse specific categories for what items he/she needs.

### Out

The app will never be turned into an IOS or Android app .

## MVP Features

- Custom user login system.
- Form designed for product information.
- A page for displaying the available products.
- A form that allows other users to bid on a certain product.
- A page that has the product’s owner’s information shown after someone wins the bidding and wants to connect with the owner.

## Stretch

users will have the ability to follow and privately message other users.

## Functional Requirements

- The user can login or register.
- The user can see newly added items in the homepage.
- The user can search for a certain item and see the items that match the serach.
- The user can view all of the items in the browse page
- The user can see the item's details when they click on the item .
- The authenticated user can bid on any item successfully.
- The winning user can see the item's owner details .
- The authenticated user can add their own product for people to bid on .

## Data Flow

when the user enters the website, a request will be sent from the back-end to the api to retrieve data and display it on the browse page and home-page.

When the user fill and submit the login form, a request will be sent holding the user information to authenticate the user and give him/her the access to user only features (Adding and bidding on an item).

When a user bids on an item, an update request will be sent to the back-end with the necesery information to complete the process.

When a user clicks on the add button, a form will appear with the product's information for the user to fill, when they fill it, a post request will be sent to the back end so a new object will be added .

When the user wants to logout, they can click on the logout button and the permission for accessing the authenticatd-user-only features will be removed for them .

## Non-Functional Requirements

Security

* every user will have a private data that are only accessable by him/her.

Usability

* all users have the ability to browse but only authenticated users can bid or post items.
