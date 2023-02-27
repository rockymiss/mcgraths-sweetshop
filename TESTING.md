# Testing

## Validation

### Html Validation

Html validation was done with [https://validator.w3.org/](https://validator.w3.org/). All pages were tested by manually inputting the code into the validator.

#### **Errors**

##### Home Page

This error is relation to a dropdown menu using bootstrap 4.  The error could not be avoided and does not affect the functionality of the website. These ID duplicates appeared on each validation page as it was in the navbar.

<details open>
<summary>Home Page</summary>
<p align="center"><img src="https://res.cloudinary.com/rockymiss/image/upload/v1677467234/mcgraths/errors/index_vsvsxk.png"></p>

##### Products

Open and closed p tags appeared as validation errors on any page with products due to the form completion when filling out the add product form.  This does not affect functionality of the website.

<details open>
<summary>Home Page</summary>
<p align="center"><img src="https://res.cloudinary.com/rockymiss/image/upload/v1677467234/mcgraths/errors/index_vsvsxk.png"></p>

#### **#Pages** 

#### **Error Pages**
![403 Error Page](#)
![404 Error Page](#)

### CSS Validation

The stylesheet was validated using [https://jigsaw.w3.org/css-validator/](https://jigsaw.w3.org/css-validator/)

<details open>
<summary>No Errors</summary>
<p align="center"><img src="https://res.cloudinary.com/rockymiss/image/upload/v1677473539/mcgraths/errors/css-no-error_qgl4a4.png"></p>


### Python Validation

Python code was validated using [CI Python Linter](https://pep8ci.herokuapp.com/).  I also used the GitPod workspace to check for errors as I coded.  I found this useful as there were less errors once I ran the code through the validator.

The following files were put through the Python Linter.  Most errors were in relation to white space, blank lines and line too long.  Any errors are noted below.

### Cakes App

1. admin.py
1. apps.py
1. forms.py
1. models.py
1. urls.py
1. views.py

### Cart App

1. apps.py
1. contexts.py
1. forms.py
1. models.py
1. urls.py
1. views.py

### Checkout App

1. apps.py
1. forms.py
1. models.py
1. signals.py
1. urls.py
1. views.py
1. webhook_handler.py (one error see below)
1. webhooks.py

In webhook_handler_py at line 140 there was a line too long error.  I couldn't change it without creating a new temporary variable and I didn't feel it was needed as the error did not affect functionality.

### Contact App

1. apps.py
1. forms.py
1. models.py
1. urls.py
1. views.py

### Home App

1. urls.py
1. views.py

### McGraths Shop

1. settings.py (see below)
1. urls.py
1. wsgi.py

Errors in the settings.py file were in relation to line too long.  Again I didn't feel it necessary to change this as functionality was not affected.

### Products App

1. admin.py
1. apps.py
1. forms.py
1. models.py
1. urls.py
1. views.py
1, widgets.py

### User_Profiles

1. admin.py
1. apps.py
1. forms.py
1. models.py
1. urls.py
1. views.py


### JavaScript Validation

Javascript validation was done with [JShint](https://jshint.com/). All pages were tested by manually inputting the code into the validator.

#### **Errors**

The only error was an unused variable in relation to Stripe.  The variable was not unused, just in another location where JS could be loaded.

<details open>
<summary>Stripe</summary>
<p align="center"><img src="https://res.cloudinary.com/rockymiss/image/upload/v1677472969/mcgraths/errors/js-stripe-elements_ohuzgh.png"></p>

## Lighthouse Testing

All pages were checked on lighthouse.  Results were over 90% for performance and best practice and 100% on Accessability and SEO on both mobile and desktop.  On the first test performance was very poor.  This was fixed by applying height and width to an image.


### **First Test**

![Lighthouse Poor Performance](#)

### **Final Test**

![Final Lighthouse Test](#)


## Manual Testing

To ensure that all elements of the website were working I carried out a detailed manual test and checked off the list as I went.

| Status | **Website Usage - Logged Out**
|:-------:|:--------|
| &check; |:Clicking the McRocks Logo brings you to the homepage
| &check; |:The only menus that can be viewed on the user menu are login or Register, Products, Shop, Offers, Showcase & Contact
| &check; |:On the All Products dropdown when clicked it shows all categories
| &check; |:Within the All Products dropdown all links work
| &check; |:Clicking Shop brings you to a page where you can view all products
| &check; |:Clicking View Offers shows you products currently on offer.
| &check; |:Clicking Click on the Showcase drop down menu and you see two menus, View Cakes or Post a Cake 
| &check; |:Clicking View Cakes brings you to a page where you can view other people's cakes
| &check; |:Clicking Post a Cake brings you to the Sign In/Register Page
| &check; |:Clicking Account Icon opens a dropdown menu showing Log-in and Register
| &check; |:Clicking Log-In opens a the Sign-In page
| &check; |:Clicking Register opens the Sign-Up page
| &check; |:Clicking on any Category in the All Products dropdown will open a page with those products
| &check; |:Clicking in the search menu and typing in a search will show products you searched for if any
| &check; |:If the search is unsuccessful you can see a link to go back to all products
| &check; |:If use the sort menu each option works as it should
| &check; |:When in all products you can see a picture of the product, a button to view item and details about the product
| &check; |:Clicking View Item will bring you to the detail page of that product
| &check; |:The Image of the product is visable
| &check; |:If no product there will be a McRocks' placeholder in it's place
| &check; |:The description of the product is visible
| &check; |:The price of the product is visible
| &check; |:The Shipping alert is visible
| &check; |:The quantity input box is visible
| &check; |:The number of products in the cart is visible
| &check; |:Clicking the plus button will add a product
| &check; |:Clicking the minus button will take away a product
| &check; |:Clicking Keep Shopping will bring you back to Products page
| &check; |:Clicking add to Cart will bring you to the Cart Page
| &check; |:Clicking add to Cart will show a success message of what you have added
| &check; |:A cart icon and amount is visible in the top right hand corner of the nav bar
| &check; |:Clicking on the cart icon in the navigation bar will bring you to cart
| &check; |:The heading shopping cart is visible
| &check; |:Quantity plus and minus function in the cart
| &check; |:Image, quantity and price are all visible in the cart
| &check; |:Clicking in the discount code and entering an incorrect code with reveal an error message
| &check; |:Clicking in the discount code and entering a correct code with reveal an successful message
| &check; |:Clicking the Apply button will apply the discount and reduce the grand total
| &check; |:Grand total is visible with an alert about delivery
| &check; |:The keep shopping and Proceed to pay buttons are visible
| &check; |:Clicking keep shopping will bring you back to products
| &check; |:Clicking proceed to pay will bring you to the checkout
| &check; |:Image, quantity and price are all visible in the checkout
| &check; |:A details form is visible for the user to complete
| &check; |:Completing the form incorrectly will reveal a failure message
| &check; |:Once details are complete there is an option to create an account or login to save the information
| &check; |:Clicking on create account will bring the user to the register page
| &check; |:Clicking on login will login the user
| &check; |:Information will be saved to the users profile page
| &check; |:Entering incorrect card details will show an error
| &check; |:Entering correct card details and clicking proceed with bring you to the success page
| &check; |:Clicking complete order will bring you to the success page and a success message is received
| &check; |:Confirmation of the order will a appear confirming an email is sent
| &check; |:If viewing on a small screen only confirmation that the order was placed is sent with email to follow
| &check; |:Clicking on the Showcase Icon will open cakes others have view
| &check; |:Clicking on View Item will open the Cake post
| &check; |:Unless logged in users cannot comment and will see a message with a login link
| &check; |:Clicking login will bring the user to the login page
| &check; |:Clicking on post a cake will also bring the user to the login page
| &check; |:Clicking on contact will open a page allowing the user to send a message
| &check; |:If information is not correct the user receives an error message
| &check; |:If the information is correct clicking send will send the message 
| &check; |:Click send after a message opens a thank you page to the user for their message
| &check; |:Conctact information is visible on the contact page
| &check; |:On the footer if the user clicks contact us it will link to the contact page
| &check; |:Clicking Privacy Policy on the footer opens a modal on the screen about privacy
| &check; |:Clicking Shipping Policy on the footer opens a modal on the screen about shipping
| &check; |:Clicking Returns & Exchanges on the footer opens a modal on the screen about Returns & Exchanges
| &check; |:Any modal that is open can be closed easily with one click
| &check; |:Clicking on the Facebook icon links to facebook in a new window
| &check; |:Clicking on the Instagram icon links to Instagram in a new window
| &check; |:Clicking on the input and adding the email will redirect the user to a success page confirming signup
| &check; |:On the mailchimp confirmation page there is a link to re-direct back to McRocks

| Status | **Website Usage - Logged In**
|:-------:|:--------|
| &check; |:Clicking the McRocks Logo brings you to the homepage
| &check; |:The only menus that can be viewed on the user menu are logout or profile, Products, Shop, Offers, Showcase & Contact
| &check; |:On the All Products dropdown when clicked it shows all categories
| &check; |:Within the All Products dropdown all links work
| &check; |:Clicking Shop brings you to a page where you can view all products
| &check; |:Clicking View Offers shows you products currently on offer.
| &check; |:Clicking Click on the Showcase drop down menu and you see two menus, View Cakes or Post a Cake 
| &check; |:Clicking View Cakes brings you to a page where you can view other people's cakes
| &check; |:Clicking Post a Cake brings you to Post a Cake form
| &check; |:A correct form entry will give a success message that your message is gone to be approved
| &check; |:An incorrect entry will give a failture message
| &check; |:Clicking Account Icon opens a dropdown menu showing Log-Out and Profile Page
| &check; |:Clicking Log-Out links to the are you sure you want to log out page
| &check; |:Clicking on the profile brings you to the profile page
| &check; |:The users information is visible and can be updated
| &check; |:The users past purchases are visible
| &check; |:Clicking on any Category in the All Products dropdown will open a page with those products
| &check; |:Clicking in the search menu and typing in a search will show products you searched for if any
| &check; |:If the search is unsuccessful you can see a link to go back to all products
| &check; |:If use the sort menu each option works as it should
| &check; |:When in all products you can see a picture of the product, a button to view item and details about the product
| &check; |:Clicking View Item will bring you to the detail page of that product
| &check; |:The Image of the product is visable
| &check; |:If no product there will be a McRocks' placeholder in it's place
| &check; |:The description of the product is visible
| &check; |:The price of the product is visible
| &check; |:The Shipping alert is visible
| &check; |:The quantity input box is visible
| &check; |:The number of products in the cart is visible
| &check; |:Clicking the plus button will add a product
| &check; |:Clicking the minus button will take away a product
| &check; |:Clicking Keep Shopping will bring you back to Products page
| &check; |:Clicking add to Cart will bring you to the Cart Page
| &check; |:Clicking add to Cart will show a success message of what you have added
| &check; |:A cart icon and amount is visible in the top right hand corner of the nav bar
| &check; |:Clicking on the cart icon in the navigation bar will bring you to cart
| &check; |:The heading shopping cart is visible
| &check; |:Quantity plus and minus function in the cart
| &check; |:Image, quantity and price are all visible in the cart
| &check; |:Clicking in the discount code and entering an incorrect code with reveal an error message
| &check; |:Clicking in the discount code and entering a correct code with reveal an successful message
| &check; |:Clicking the Apply button will apply the discount and reduce the grand total
| &check; |:Grand total is visible with an alert about delivery
| &check; |:The keep shopping and Proceed to pay buttons are visible
| &check; |:Clicking keep shopping will bring you back to products
| &check; |:Clicking proceed to pay will bring you to the checkout
| &check; |:Image, quantity and price are all visible in the checkout
| &check; |:A details form is visible which should hold the users information except full name
| &check; |:Entering incorrect card details will show an error
| &check; |:Entering correct card details and clicking proceed with bring you to the success page
| &check; |:Clicking complete order will bring you to the success page and a success message is received
| &check; |:Confirmation of the order will a appear confirming an email is sent
| &check; |:If viewing on a small screen only confirmation that the order was placed is sent with email to follow
| &check; |:Clicking on the Showcase Icon will open cakes others have view
| &check; |:Clicking on View Item will open the Cake post
| &check; |:Logged in user can leave a message
| &check; |:When a comment is sent a success message will appear confirming this
| &check; |:Clicking on contact will open a page allowing the user to send a message
| &check; |:If information is not correct the user receives an error message
| &check; |:If the information is correct clicking send will send the message 
| &check; |:Click send after a message opens a thank you page to the user for their message
| &check; |:Conctact information is visible on the contact page
| &check; |:On the footer if the user clicks contact us it will link to the contact page
| &check; |:Clicking Privacy Policy on the footer opens a modal on the screen about privacy
| &check; |:Clicking Shipping Policy on the footer opens a modal on the screen about shipping
| &check; |:Clicking Returns & Exchanges on the footer opens a modal on the screen about Returns & Exchanges
| &check; |:Any modal that is open can be closed easily with one click
| &check; |:Clicking on the Facebook icon links to facebook in a new window
| &check; |:Clicking on the Instagram icon links to Instagram in a new window
| &check; |:Clicking on the input and adding the email will redirect the user to a success page confirming signup
| &check; |:On the mailchimp confirmation page there is a link to re-direct back to McRocks

| Status | **Website Usage - Logged In SuperUser**
|:-------:|:--------|
| &check; |:Management has access to all of the above mentioned
| &check; |:All menus can be viewed, particularly a new one in the account dropdown called Management
| &check; |:Clicking Management will bring the user to the Management page
| &check; |:Add Products, Showcase, Comments, Messages and Discount lists are visible
| &check; |:Clicking Add Products brings the user to the add product page
| &check; |:Superusers can add a new product here successfully
| &check; |:Clicking add product will redirect the user to the product detail page to see the new product
| &check; |:Clicking Showcase shows the user a list of showcase posts to approve.
| &check; |:Clicking Approve will ask the user if the are sure to approve
| &check; |:Clicking Delete will ask the user if they are sure to delete
| &check; |:Clicking the comments page links the user to a list of comments received on a cake post
| &check; |:A user will see the cake post it relates to, who left the comment and the comment
| &check; |:Clicking the delete button will delete the comment
| &check; |:Clicking approve will approve the comment and add it to the cake post
| &check; |:Clicking messages shows a list of messages sent by users of the website
| &check; |:The Superuser sees the Details of the message, such as name, date, message
| &check; |:Clicking delete will delete the message
| &check; |:Clicking discounts opens the discount page showing discounts already set up and add a discount
| &check; |:Clicking add a discount links the user to the add discount page where a discount can be added
| &check; |:Clicking Delete will delete any discount already created. 
| &check; |:On product details the Super user can see edit and delete buttons.  
| &check; |:The SuperUser is the only one to see these buttons and use them.


## Bugs

### Bugs sub heading

Increase and Decrease Product Value

<details open>
<summary>Increase and Decrease Product Bug</summary>
<p align="center"><img src="https://res.cloudinary.com/rockymiss/image/upload/v1670880846/mcgraths/missing-bracket_wcp7od.png"></p>

Despite updating product_detail and quantity_input_script with the bug fix from Scott of Code Institute my products input value was not increasing or decreasing.  When clicking either the plus or minus icon the page would reload and just one item would add to the cart. The issue of the value increase or decrease remained and this was the result of a missing curly bracket as shown in the image above.  A simple fix yet a deadly needle in a haystack.  Thanks to tutor support for the help with this one.  
</details>

<details open>
<summary>Category List</summary>
<p align="center"><img src="https://res.cloudinary.com/rockymiss/image/upload/v1676152671/mcgraths/category_list_wrong_lkw07u.png"></p>

I wanted to create a for loop so that when new categories were added by admin the dropdown list on the navbar for categories would automatically update. To loop I used the variable "products" from the product_list function in my products view.  Each time I clicked on a category it would display the products from that category, which is what I wanted it to do but when I clicked on the dropdown list again all other categories except the one I just clicked disappeared.  To fix this I created a new variable in the product_list function called product_drop which kept the full list of categories at all times.  Unfortunately on further testing I noticed categories being duplicated.  For now I have created the list based on categories already in.  

I created an issue in github projects and used a development branch called [all-categories-bug](https://github.com/rockymiss/mcrocks-shop/issues/61 )to deal with this issue.  
</details>
