# Testing

## Validation

### Html Validation

Html validation was done with [https://validator.w3.org/](https://validator.w3.org/). All pages were tested by manually inputting the code into the validator.

#### **Errors**

![Home Page](https://res.cloudinary.com/rockymiss/image/upload/v1677467234/mcgraths/errors/index_vsvsxk.png)

This error is relation to a dropdown menu using bootstrap 4.  The error could not be avoided and does not affect the functionality of the website. 

#### **About Page**

![About Page](#)

#### **#Pages**

![Page](#)

#### **Error Pages**
![403 Error Page](#)
![404 Error Page](#)

### CSS Validation

The stylesheet was validated using [https://jigsaw.w3.org/css-validator/](https://jigsaw.w3.org/css-validator/)

![Stylesheet validation](#)


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

#### Gitpod Workspace

![Workspace](#)


## Lighthouse Testing

All pages were checked on lighthouse.  Results were over 90% for performance and best practice and 100% on Accessability and SEO on both mobile and desktop.  On the first test performance was very poor.  This was fixed by applying height and width to an image.


### **First Test**

![Lighthouse Poor Performance](#)

### **Final Test**

![Final Lighthouse Test](#)


## Manual Testing

To ensure that all elements of the website were working I carried out a detailed manual test and checked off the list as I went.

| Status | **Page Logged Out? Logged In?**
|:-------:|:--------|
| &check; |:
| &check; |:
| &check; |:
| &check; |:
| &check; |:
| &check; |:
| &check; |:
| &check; |:
| &check; |:
| &check; |:
| &check; |:
| &check; |:
| &check; |:
| &check; |:


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

I wanted to create a for loop so that when new categories were added by admin the dropdown list on the navbar for categories would automatically update. To loop I used the variable "products" from the product_list function in my products view.  Each time I clicked on a category it would display the products from that category, which is what I wanted it to do but when I clicked on the dropdown list again all other categories except the one I just clicked disappeared.  To fix this I created a new variable in the product_list function called product_drop which kept the full list of categories at all times.

I created an issue in github projects and used a development branch called [all-categories-bug](https://github.com/rockymiss/mcrocks-shop/issues/61 )to deal with this issue.  
</details>
