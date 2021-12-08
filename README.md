# Online Auction

Website that allows users to show and sell their products online by allowing other people to bid on the price. So it helps people to get unique products that cannot be found in the usual markets.  

##  MVP Features:
- Custom user login system.
- Form designed for product information.
- A page for displaying the available products.
- A form that allows other users to bid on a certain product.
- A page that has the product’s owner’s information shown after someone wins the bidding and wants to connect with the owner.


## Group Members 
1. Tahany Ali
2. Tasneem Al-Absi
3. Abdullah Nazzal
4. Anas Abusaif

## User Stories

1. As a user I want to have the ability to register and login to the website so that I can start bidding on items.

  - Feature Tasks:

    * provide a login and register Forms for unauthenticated users.
    * User can logout at anytime by clicking the logout button.

  - Acceptance Tests:
    * Scenario(1):

      Given: User isn't authenticated.

      When: The user click the 'Sign Up' button

      Then: A form will appear giving the options to Login or Register
    * Scenario(2):
      Given: The user is authenticated
      When: The user Clicks the Logout button
      Then: The user will be logged out

2. As a user I want to view some items that are featured today so that I can see what items are trending

- Feature Tasks:

    * view some of the items of one or more categories on a section at the home page.

  - Acceptance Tests:

    * Scenario(1):

      Given: User is at the home page.

      When: The user is browsing the home page.

      Then: the items that started today will be displayed in a certain section.
3. As a user I want to search for certain items so that I can see the item I'm looking for

- Feature Tasks:

  * view the items that match the search .

- Acceptance Tests:
 
   * Scenario(1):

      Given: User is at the home page.

      When: The user searches for a certain item in the search bar.

      Then: the items that match the search will be displayed for the user.
      
  * Scenario(2):

      Given: User is at the home page or at the browse page.

      When: The user searches for a certain item in the search bar.

      Then: A message will appear if the item has no matches. 
 
 
 
4. As a user i want to have the ability to browse all of the items displayed for auction so that I can see all of the available items . 

- Feature Tasks:

  * view all of the available items in the browse page.
  * view the items that match the search .

- Acceptance Tests:
 
   * Scenario(1):

      Given: User is at the home page.

      When: The user clicks on the browse link.

      Then: the user will be navigated to the browse page with all of the items displayed.
      
  * Scenario(2):

      Given: User is at the home page.

      When: The user clicks on the browse link.

      Then: the user will be navigated to the browse page with no available items.
 
   * Scenario(3):

      Given: User is at the browse page.

      When: The user searches for a certain item in the search bar.

      Then: the items that match the search will be displayed for the user.
      
5. As a user I want to see the items information so that I would know more details about it.

- Feature Tasks:

  * view all of the item's details in the selected item page.
  

- Acceptance Tests:
 
   * Scenario(1):

      Given: User is viewing the items.

      When: The user clicks on a certain item.

      Then: the user will be navigated to the selected item's page and shown details about the item.
      
6. As a user i want to have the ability to bid on any displayed item so that I will have a chance to win the auction .

- Feature Tasks:

  * user can bid on the item with their own price .
  

- Acceptance Tests:
 
   * Scenario(1):

      Given: User is in the item's page.

      When: The user clicks on bid button.

      Then: the user can bid successfully.
      
7. As a user I want to see the item's owner details when I win the auction so that I can contact them to get the item.

- Feature Tasks:

  * the winning user can see the owner's information.
  

- Acceptance Tests:
 
   * Scenario(1):

      Given: User won the auction.

      When: The user will be notified to contact with the owner.

      Then: the owner's details will be shown to the user.     

   
8. As a user I want to add my own product so that people can bid on it.

- Feature Tasks:

  * users can add their own products.
  

- Acceptance Tests:
 
   * Scenario(1):

      Given: User is at the web site and is authenticated.

      When: The user clicks on the add button.

      Then: A form will be shown to the user with the item's details and submit it so the item will be added successfully.

      
   
