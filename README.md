# What's Cooking?

"What's Cooking?" is a public online blog-style platform where users can find recipes shared by food-loving people from around the globe. If someone wants to share their recipe or be able to comment and like others', they can register and log in. 

This interactive platform is designed to be an inspiration for those days when you don't know what to cook or simply want to try something new.

![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1698071210/am_i_responsive_tcp3td.png)

Click [here](https://what-s-cooking-a7be1440512e.herokuapp.com/) to view the live site.

# Table of Contents
- [Database Diagram](#database-diagram)
  - [Planning](#planning)
  - [Final Result](#final-result)

- [User Experience](#user-experience)
  - [Agile](#agile)
  - [Strategy](#strategy)
  - [Scope](#scope)
  - [Structure](#structure)
  - [Skeleton](#skeleton)
  - [Surface](#surface)

- [Technologies Used](#technologies-used)
  - [Languages](#languages)
  - [Frameworks, Libraries and Programs](#frameworks-libraries-and-programs)

- [Features](#features)
  - [Existing Features](#existing-features)
  - [Future Features](#future-features)

- [Testing and Validation](#testing-and-validation)
  
- [Fixed Bugs](#fixed-bugs)

- [Known Issues](#known-issues)

- [Credits](#credits)
  - [Media](#media)
  - [Content](#content)
  - [Acknowledgements](#acknowledgements)

- [Deployment](#deployment)

- [Development](#development)
  - [Fork](#fork)
  - [Clone](#clone)

  
## Database Diagram

The database model diagram was designed using [Lucidchart]("https://www.lucidchart.com/pages/sv"). The first draft of the entity relationship diagram is nearly the same as the models used in the final database. 

### Planning

![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1697040883/static/images/models_in_the_beginning.c0b363f73f04.png)

At this stage, the ingredients an servings fields are missing.

### Final Result

![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1697040885/static/images/final_models.ad88f2449a6e.png)

#### Recipe Model
  - The main model that contains all the fields needed for the recipe to be complete. Of course you can add other fields (like cooking time, difficulty level, nutritional value, and so on), but that values are not vital for the site to work and can be added later.
  - Is based on the "I think therefore I blog" walkthrough project. Some adjustments and additions were made to fit the needs of my project.

#### Comment Model
  - Enable logged-in users to add comments to different recipes.
  - Is based on the "I think therefore I blog" walkthrough project.

#### Category Model
  - The custom model.
  - Enable users to place recipes in different categories.
  - Make it possible to "sort" recipes by categories.

[Back to top ⇧](#table-of-contents)


## User Experience

I used the design thinking approach to create a clutter-free website with only necessary information, making it easy for users to navigate. 

To maximize the user approach, I interviewed my friend Josefine throughout the process. Among other things, she provided valuable tips on displaying categories on each recipe card, which indeed makes the user experience better.

### Agile

I employed the agile methodology, starting from the planning stage and continuing until the final product was built. To ensure that I stayed organized and on track, I utilized a GitHub project and a [Kanban board](https://github.com/users/Kattis91/projects/3/views/1). Information about User Stories can be found in the subsection below⇩ 

**Five planes of User Experience:**

### Strategy

My User Stories can be found [here](https://github.com/Kattis91/what-is-cooking/issues). All User Stories include:
 - Acceptance Criteria
 - Tasks
 - Labels (MoSCoW Priotarization)

Some of the User Stories are part of an EPIC.

Please, go to [TESTING.md](TESTING.md) if you want to come to the section where I test my User Stories.

#### Key Project Goal

Planning what to cook can be a struggle for many. The key project goal of the blog is to establish a visually appealing and user-friendly open-source recipe database. It should not be challenging for users to find what they are looking for. 

Therefore, I have included **categories** on the homepage of the site: 

  - It is a useful feature for users who have a specific food preference and do not want to waste time browsing through all the recipes. By clicking on a category, they can easily find dishes that meet their specific criteria, such as vegetarian dishes. This leads to a more efficient and enjoyable user experience.

  - As for those who don't know what they want, seeing categories can help them narrow down their choices and ultimately get some inspiration and ideas.

With easy-to-follow links, the site is highly navigable.

#### Target Audience

The best part of the blog is that it caters to almost everyone. Of course, you need to be old enough to be in the kitchen.

Whether you are uncertain about meal choices, a food-lover seeking culinary knowledge, or simply a "hungry" person desiring to learn new recipes, tips, and cooking techniques, everybody is welcome!

#### User Requirements and Expectations:

- A brief and simple description of the site’s purpose.

- Easy to navigate the site to find information.

- A quick and thorough overview of the site's features and functionalities.

- Links and functions work as expected.

- Feedback when ineracting with the site.

- Possibility to view the site on a range of device sizes.

### Scope

#### Content | Functionality Requirements:

- Easily accessible navigation bar with the links that have easily understandable names.

- Responsive design.

- A brief and simple description of the site’s purpose.

- A complete collection of recipes.

- A thorough list of ingredients and step-by-step instructions to follow.

- A possibility to sort recipes by categories.

- A possibility to read comments.

#### Authentication:

- Add registration/login features that give the user access to extra functionality.

- Add Logout functionality for safety reasons.

#### Functionality for logged-in users:

  - **CRUD functionality:**

    - Implement feature that allows user to **C**reate recipes.

    - Implement feature that allows user to **R**ead recipes.

    - Implement feature that allows user to **U**pdate recipes.

    - Implement feature that allows user to **D**elete recipes.

  - **Comment and like feature:**

    - Enable logged-in users to post comments on any of the published recipes.

    - Enable logged-in users to like/unlike published recipes.


### Structure

The blog is divided into different pages. Some of the pages are accessible only for logged in users. The blog structure allows users to access recipes via the recipes page or by sorting them through different categories. All users can access detailed information about each recipe by clicking on the recipe card. Users who are logged in can publish, edit, and delete their own recipes, and interact with other recipes by liking and commenting on them.

**For detailed information about all existing features see the section [Existing Features](#existing-features).**


### Skeleton

I created wireframes using [Figma](https://www.figma.com/).

<details>
<summary>Home page</summary>

LEFT: all users | RIGHT: logged-in users.

![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1698070413/wireframes_home_page_yzr4qc.png)

</details>

<details>
<summary>Recipe page</summary>

![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1698070413/wireframes_recipes_page_ab1x0w.png)

</details>

<details>
<summary>Recipe detail page</summary>

LEFT: all users | RIGHT: logged-in users.

![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1698070413/wireframes_recipe_detail_page_xrr53z.png)

</details>

<details>
<summary>Add a Recipe page</summary>

![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1698070413/wireframes_add_a_recipe_page_r1ea4a.png)

</details>

<details>

<summary>Sign Up</summary>

![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1698070605/wireframes_sign_up_xvkbyi.png)

</details>

<details>
<summary>Login</summary>

![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1698070413/wireframes_sign_in_jds4rh.png)

</details>

<details>
<summary>Logout</summary>

![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1698070413/wireframes_sign_out_eahchw.png)

</details>

### Surface

#### Colour Scheme

The choice of colors depends on the background image chosen for home, sign up, login, and logout pages.

![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1697465308/static/images/colour_scheme.20c06536a086.png)

 - **`9AA5AF`** is the primary color used throughout the pages:
   - Welcome message.
   - Category boxes on the home page.
   - Recipe cards.
   - Add | Edit recipe forms.
   - Sign Up | Login | Logout forms.
   - Confirmation message when choosing to delete a recipe.
  
 - **`BAA6B1`** is used to style the navbar, the footer and the "View Recipe" button.

 - **`000000`** is the primary text color used throughout the pages.

 - **`850000`** is used for links and hover styling on navbar and footer. The color was chosen with the help of [Color Contrast Analyzer](https://dequeuniversity.com/rules/axe/4.7/color-contrast) (provided by Lighthouse testing) in order for background and foreground colors to have a sufficient contrast ratio.

 - **`E1DDDD`** is used as the background color for all recipe-related pages including recipes, recipe details, add recipe, edit recipe and categories.

#### Button styling

All buttons throughout the pages have the same styling, ensuring uniformity and providing a seamless user experience. 
 
I went with following colors:
  - `GREEN` that usually is associated with "YES" | "SAVE" | "OK".
  - `#850000` that usually is associated with "NO" | "CANCEL" | "GO BACK".
  - `WHITE` for the text in order to get a sufficient contrast ratio.

    ![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1697633882/static/images/buttons_edit_delete.e24beb2a6eb9.png)
  
<details>

<summary>Click here to see all the buttons</summary>

- Sign up: 
    
  ![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1697633861/static/images/sign_up_button.0940135d3c68.png)

- Sign in:
   
  ![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1697633870/static/images/sign_in_button.fbfe033373f6.png)
  
- Logout:

  ![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1698070747/logout_buttons_hr62xk.png)

- Add a recipe:

  ![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1697633871/static/images/buttons_add_a_recipe_form.214a4d7e1147.png)

- Update a recipe:

  ![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1697633873/static/images/buttons_update_a_recipe.e9fd1ac91f38.png)

- Delete confirmation:

  ![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1697633865/static/images/buttons_delete_recipe.1baafc8c42e4.png)

- Edit | Delete:

  ![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1697633882/static/images/buttons_edit_delete.e24beb2a6eb9.png)

- Submit (when leaving a comment):

  ![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1698070830/submit_button_ia096k.png)

</details>

#### Recipe images:

Users have the option to upload images in various sizes. To ensure consistency, I made sure that all recipe cards on the same line had the same height. The size of the images doesn't affect the layout of the recipe detail page. All sections are uploaded correctly as they should be.

![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1698072781/images_of_different_sizes_cm5b33.png)

#### Typography

[Google Fonts](https://fonts.google.com/) was used to import the chosen fonts for use in the site. 
[Typ.io](https://typ.io/) was used to see what fonts go together.

- I have used **"Bitter"** for all the headings throughout the pages.

  ![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1698064743/bitter_font_v556wt.png)

- For the paragraphs I went with **"Opens Sans"**

  ![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1698064743/open_sans_font_jga0iw.png)

[Back to top ⇧](#table-of-contents)

## Technologies Used

### Languages
 
  - HTML
  - CSS
  - Python
  - JavaScript

### Frameworks, Libraries and Programs

  - [Django](https://www.djangoproject.com/)
   
  - [Django-Allauth](https://docs.allauth.org/en/latest/)
    - used for User authenticaion (sign up, sign in and sign out features).

  - [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
    - used to control rendering behaviour of Django forms.

  - [Gunicorn](https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/gunicorn/)
    - Python HTTP server for WSGI applications.
  
  - [psycopg2](https://pypi.org/project/psycopg2/)
    - PostgreSQL database adapter for the Python programming language.
  
  - [Summernote](https://summernote.org/)
    - WYSIWYG editor. Used for ingredients and instruction fields on the Admin site and instructions field in the "Add a recipe" form.

  - [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/index.html)
    - The library that allows the web app to serve its static files.
    - "Whitenoise storage" was removed before final deployment as the app functioned fine without it.

  - [ElepantSQL](https://www.elephantsql.com/)
    - The database used by the deployed project on Heroku.

  - [Cloudinary](https://cloudinary.com/)
    - The cloud platform used to store static media files.

  - [Git](https://git-scm.com/)
    - used for version controll.

  - [GitPod](https://www.gitpod.io/)
    - The IDE used to create the site.

  - [GitHub](https://github.com/)
    - The code hosting platform used to save and store the files for the website.

  - [Heroku](https://www.heroku.com/)
    - The cloud platform used to deploy the project into live environment.

  - [Bootstrap](https://getbootstrap.com/)
    - The front-end development framework used for styling along with custom CSS.
  
  - [Lucidchart](https://www.lucidchart.com/pages/sv)
    - The diagramming application used to create ERD diagrams.

  - [Am I responsive?](https://ui.dev/amiresponsive)
    - used to see how the site looks on a range of devices.

[Back to top ⇧](#table-of-contents)

## Features

### Existing Features

#### Navigation Bar

- The navigation bar is complete and responsive. It appears consistently on every page, making navigation more convenient.

- This section facilitates seamless navigation between pages, eliminating the need to rely on the "back button".

- Clicking on the Logo and "Home" will always redirect the user to the home page.

- When the user clicks on "Recipes", they will be directed to a page containing all available recipes.

- Logo and links to the home and recipes pages are **available for all users**. However, there are some differences in how the navigation bar looks for non-logged and logged-in users.
 
  - **Non-logged users:**

    ![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1698065541/navigation_bar_logout_e5pziy.png)
    
    - The navigation bar contains links for the Logo, Home, Recipes, Sign Up, and Login pages.
    - Clicking "Sign Up" or "Login" directs users to the pages with respective forms.

  - **Logged-in users:**
    
    ![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1698065541/navigation_bar_login_domjug.png)

    - The navigation bar contains links for the Logo, Home, Recipes, Add Recipe, and Logout pages.
    - Clicking "Add Recipe" takes the user to a page where they can fill in a form to publish a recipe.
    - Clicking "Logout" directs users to the confirmation page.

- On smaller devices, the navigation bar is displayed using a hamburger menu:

  ![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1698065541/navbar_hamburger_menu_mculka.png) 

  ![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1698065541/navbar_hamburger_menu_links_vdmfto.png)

#### Welcome message

![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1697191595/static/images/welcome_message.2ef1f108f567.png)

- This section welcomes users to the blog.

- Tells users that:
  - It is a recipe blog.
  - It is possible to publish own recipes.

#### Categories

![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1698066224/categories_xsgfy3.png)

- This section shows all the categories available right now.

- Clicking on a category redirects the user to all recipes within that category. The "BACK" button takes the user back to the homepage.
  
  - There are some recipes available:
    ![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1697563078/static/images/category_recipes.2be814ef0284.png)

  - No recipes are available within the selected category.
     
    - Logged-in users:
      ![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1697563051/static/images/category_no_recipes_logged_in.e770123eaa9d.png)

    - Unlogged users:
      ![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1697563075/static/images/category_no_recipes_unlogged_users.f8ebd9bdc2cb.png)


#### Footer

![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1697191592/static/images/footer.078e93c57a23.png)

- This section contains links to the appropriate social media platforms. By clicking on them, they will open in a new tab.

- The footer remains consistent across all pages.

#### Sign Up

![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1697376101/static/images/sign_up_form.f49ed81b91fc.png)

- The form enables users to register and create an account.

- The form includes following fields:
  - Username
  - Email
  - Password
  - Password (again)

- Email field is optional.

#### Login

![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1697376103/static/images/sign_in_form.9a00efc66dfb.png)

- The form enables users to log in.

- When a user logs in, they gain the ability to:
  - comment on existing recipes,
  - create new recipes.
  - edit/delete their own recipes.

- A message indicating that the operation was successful is shown on the screen.

#### Logout

![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1698066570/sign_out_oksgx5.png)

- When the user clicks on Logout in the navbar, they are redirected to a page displaying a confirmation message above.

  - SIGN OUT:
    - The user redirects to the home page.
    - A message indicating that the operation was successful is shown on the screen.

  - REMAIN LOGGED IN:
    - The user redirects to the home page.


#### Recipes page

![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1698066665/recipes_page_tjxtf4.png)

- This page shows a list of all the published recipes.

- Information displayed:
  - recipe image;
  - recipe title;
  - create date;
  - category;
  - estimated time of cooking;
  - "View Recipe" button.

- By clicking the "View Recipe" button, the user redirects to a page containing detailed information about that specific recipe.

#### Recipe detail page

The recipe detail page includes the following information:

  - The recipe image (or the default image if the recipe image doesn't load).
  
  - Information field containing some extra information for recipe authors.
    
    - Available for all users:
    
      ![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1697376100/static/images/recipe_view_visitors.45a5b88174b1.png)

      - recipe title;
      - estimated time of cooking;
      - category;
      - number of servings;
      - recipe author;
      - create date;
      - likes icon:
        - logged-in users can like recipes;
        - no-logged users can only see the number of likes.
      - comment icon that shows the number of comments on the selected recipe.
    
    - Extra functionality for the recipe authors:
   
      ![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1697376095/static/images/recipe_view_author.7712060f0483.png)

      - EDIT
        - By clicking the "EDIT" button, the user is redirected to the page with a form where they can edit the recipe posted by them.
        - The form has the same fields as the "Add a Recipe" form.
        - All the form fields are prepopulated.
      
      - DELETE
        - By clicking the "DELETE" button, the user is redirected to the page where they get a question about whether they are sure that they want to delete the recipe.
       
          ![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1698066873/delete_confirmation_n6eny3.png)
          - The recipe gets deleted when the user clicks the "DELETE RECIPE" button. The user is redirected to the home page.
          - The user is redirected to the home page when clicked the "GO BACK" button.

  - Ingredients section.

  - Instructions section.

  - Comments section:
    
    - There are some comments on the recipe:

      ![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1697376107/static/images/comments.c245aa6c507c.png)
    
    - There are NO comments:

      ![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1697376099/static/images/no_comments.937fab397a78.png)

    - Leave a comment (available ONLY for logged-in users):

      ![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1697376117/static/images/leave_a_comment.d764d9137d00.png)

#### Add a Recipe page

- This page includes a form that allows users who are logged in to publish their own recipes.

- Available fields:
  - Title
  ![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1697376105/static/images/form_title.92e76d13f3ee.png)
  - Category (Dropdown menu)
  ![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1697376112/static/images/form_category.63f3dc7d46c1.png)
  - Image
  ![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1697376114/static/images/form_featured_image.969458f814d3.png)
  - Ingredients
  ![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1697376098/static/images/form_ingredients.1644f639b558.png)
  - Instructions (Summernote field)
  ![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1697376106/static/images/form_instructions.6e139006d641.png)
  - Estimated time
  ![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1697376116/static/images/form_estimated_time.f78b54b4e36b.png)
  - Servings
  ![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1697376109/static/images/form_servings.b8ed7c47f0b4.png)
  
  - Buttons

    ![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1697633871/static/images/buttons_add_a_recipe_form.214a4d7e1147.png)
   
    - SAVE:

      - After correctly submitting the form, the user will be redirected to the recipes page upon clicking the save button.

      - A success message is displayed to the user.

    - "CANCEL" button:

       - When the user clicks on the 'go back' button, they will be redirected to the recipes page.


### Future Features

- Make it possible for logged-in users to save recipes as their favorites.

- Add a feature that allows users to click on the author's name and view all the recipes published by that author.

- Add some other choices, like difficulty level, meal type, cuisine.

- Enable users to log in using their social media accounts.

[Back to top ⇧](#table-of-contents)

## Testing and Validation.

Detailed testing of the site can be found at [TESTING.md](TESTING.md). 

Testing includes following:

- Validator testing
- Responsivness & Browser Compability Testing
- Manual Testing
- Automated Testing
- Testing of User Stories
- Lighthouse

## Fixed Bugs

  - Static files were not loading in the deployed Heroku app. The local preview looked just the way it should, but checking the deployed site, none of the styling was there, and the images weren't loading.
    - **Fix**: Install [Whitenoise](https://whitenoise.readthedocs.io/en/latest/index.html) and put some lines of code in settings.py as mentioned in the link.
    - **Update**: The app is working without Whitenoise.

  - Chosen colors (`#71777ce6, whitesmoke and #ffc107`) didn't have sufficient contrast ratio. 
    - **Fix**: Use [Color Contrast Analyzer](https://dequeuniversity.com/rules/axe/4.7/color-contrast) provided by Lighthouse testing to find new colors working good together (see more in the Design section).

  - "Add a Recipe" form.
    
    - When filling out the form, users were presented with a drop-down menu that allowed them to select an author for their recipe. The menu displayed the usernames of every registered user on the website. However, despite the selection made by the user, the recipe was still published under their own name. This bug caused confusion, leading to a poorer user experience.
      - **Fix**: Delete the "author" field from the RecipeForm. The recipe is still published in the user's name without causing any issues or confusion for the user.
    
    - The recipe image failed to display. The default image appeared instead whenever a recipe was published.
      - **Fix**: It turned out that the enctype attribute was missed. I added *enctype="multipart/form-data"* to be able to upload images.

    - The slug wouldn't generate for the recipes submitted via the form.
      - **Fix**: Import slugify and include the helper method into the Recipe model.

        ![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1697563055/static/images/slugify.ef34fa449a66.png)

    - It was possible to choose zero and enter very large numbers into the estimated_time and servings fields.
      
      ![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1697563056/static/images/max_value_validator.49f534e0e390.png)
      
      - **Fix**: Add validate_nonzero function. Import and add MaxValueValidator.
        
        ![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1697563050/static/images/validate_nozero.2cf483305233.png)

    - The layout of the recipe detail page was affected when a user entered a single long word. For example, the one long word typed in the Ingredients field overflowed into the Instructions field and continued beyond the right boundary of the page until the word was finished, causing the page's layout to break. 
      - **Fix**: 
        - Wrap the fields in the container. 
        - Use the word-wrap property with the value of break-word to be able to break the long words and wrap them onto the next line.
    
  - **Forbidden (403). CSRF verification failed. Request aborted.** message was displayed when I was trying to log in to the admin site in the beginning of the project.
    - **Fix**: `Add CSRF_TRUSTED_ORIGINS=['https://*.YOUR_DOMAIN.COM']` to settings.py

## Known issues

Not really a bug, and maybe not even an issue, but like and comment icons don't match each other for logged in users. However, the liking functionality works as it should, so I leave it as is.

- Logged-in users:

  ![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1698077238/likes_and_comments_logged_in_dd4lli.png)

- Unlogged users: 
  
  ![image](https://res.cloudinary.com/dx0imlozl/image/upload/v1698077238/likes_and_comments_unlogged_in_zitubp.png)

[Back to top ⇧](#table-of-contents)

## Credits

### Media

- All the images used on the website are downloaded from [Unsplash](https://unsplash.com/).

- [Favicon Generator](https://favicon.io/favicon-converter/) was used to generate a favicon from the image.

- [Font Awesome](https://fontawesome.com/) was used to add the icons to the Logo and recipe detail page (estimated time, categories, servings, the number of likes, and the number of comments).

- The recipes published by me are taken from [BBC Good Food](https://www.bbcgoodfood.com/recipes).

### Content

- The main code of this project is based on the Code Institute tutorial ["I Think Therefore I Blog"](https://github.com/Code-Institute-Solutions/Django3blog) with changes made to suit my project. [Django Documentation](https://docs.djangoproject.com/en/4.2/) was used throughout the project.

- I found Stack Overflow to be an excellent source of inspiration and a valuable channel for gaining knowledge. Things I learned and borrow from there:
 
  - Instructions on how to put different background images/background colors on different pages ([click here to read more](https://stackoverflow.com/questions/61434945/putting-a-different-background-image-on-a-different-page-in-a-website))

  - Instructions on how to make navbar links active depending on the page a user is viewing ([click here to read more](https://stackoverflow.com/questions/46617375/how-do-i-show-an-active-link-in-a-django-navigation-bar-dropdown-list))

  - Ability to create/update and delete recipes while getting a success message displayed is achieved by following instructions in two different Stack Overflow articles.
    - [Create/update](https://stackoverflow.com/questions/67366138/django-display-message-after-creating-a-post);
    - [Delete](https://stackoverflow.com/questions/47636968/django-messages-for-a-successfully-delete-add-or-edit-item).

  - A method to generate slug for recipes submitted through the site form ([click here to read more](https://stackoverflow.com/questions/837828/how-do-i-create-a-slug-in-django)).

  - PositiveIntegerFields (estimated_time and servings) were validated by following instructions in this [article](https://stackoverflow.com/questions/2248617/0-value-in-django-positiveintegerfield).

- The option to sort recipes by category was implemented following [Very Academy](https://www.youtube.com/watch?v=S9-Bt1JgRjQ&t=2137s) tutorial. I made some modifications in order to show my categories in the form of clickable "boxes" instead of displaying them in the navbar.

- The CSS code for category boxes to zoom/scale in on hover was borrowed from [W3Schools](https://www.w3schools.com/howto/howto_css_zoom_hover.asp).

- [Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/) was used to generate Django Secret Key.

### Acknowledgements

I would like to aknowledge the following people:

  - Sean from the Tutor Assistance team for teaching me about the CSS word-wrap Property (used on the recipe detail page), helping me with my models testing and with updating timeout function for alert messages due to utilizing the newer version of Bootstrap. 

  - My mentor Jubril for good briefings, feedback and tip. 

  - Daisy_mentor (#project-portfolio-4) for sharing information about closing completed User Stories.

  - Kay (the facilitator in my team) for always patiently answering all my questions during our Monday sessions &#128512;

  - Karolis_5P and Emma S-A_5P (Peer Code Review) who took time to look at my project, check the functionality and come up with valuable feedback.

  - Tutor Assistance Team for helping me out with diverse things throughout the project.

[Back to top ⇧](#table-of-contents)

## Deployment

### Installing Django and supporting libraries

- Install **Gunicorn**(the server that is used to run Django on Heroku): `pip3 install django gunicorn`

- Install **dj_database_url** and **pyscopg2**(connect to PostegreSQL): `pip 3 install dj_database_url pyscopg2`

- Install **Cloudinary** (The cloud platform used to store static media files): `pip3 install dj3-cloudinary-storage`

- Install **Whitenoise** (The library that allows the web app to serve its static files.): `pip3 install whitenoise`


### Create App

- Create Project.

- Create App.

- Add App to installed apps in **settings.py**:

  ````
  INSTALLED_APPS = [
    ...
    'APP_NAME',
  ]
  ````

### Create a new external database

- Navigate to **ElephantSQL.com** and click **“Get a managed database today”**.

- Click **Create New Instance**.

- Set up your plan:
  - give your plan a Name;
  - select the Tiny Turtle (Free) plan.

- Click **“Select Region”** and select a data center near you.

- Click **"Review"**, check that your details are correct and click **“Create instance”**.

- Return to the dashboard and click on the database instance name for this project.

- Copy the database URL.


### Create the Heroku app

 - Sign up for Heroku and accept terms of service.

 - Click the **"Create a new app"** button.

 - Give your app a name and select the region closest to you. A name must be unique.
  

### Create an env.py file

- Create **env.py** file and check that the file is included in the **.gitignore file**.

- Import os library: `import os`.

- Set environment variables:
  - **DATABASE_URL** with the value you just copied from ElephantSQL: `os.environ["DATABASE_URL"]="<copiedURL>`
  - **SECRET_KEY**: `os.environ["SECRET_KEY"] = "randomSecretKey"` ([Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/) was used to generate a secret key).


### Update settings.py

- Add the following code:

  ````
  import os
  import dj_database_url
  if os.path.isfile('env.py'):
      import env
  ````

- Remove the insecure secret key provided by Django. Change your SECRET_KEY variable to the following: `SECRET_KEY = os.environ.get('SECRET_KEY')`

- Comment out the original **DATABASES** variable and add the code below:

  ````
  DATABASES = {
      'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
  }
  ````

- Save all files and make migrations: `python3 manage.py migrate`


### Connecting Heroku to the database

- Go back to the Heroku dashboard and open the **Settings** tab:

- Create _Config Vars_:
  - KEY: **PORT** | VALUE: **8000**.
  - KEY: **SECRET_KEY** | VALUE: **randomSecretKey**(the value that is in env.py)
  - KEY: **DATABASE_URL** | VALUE: **ElephantSQL database url**(no quotation marks needed)
  - KEY: **DISABLE_COLLECTSTATIC** | VALUE: **1** (Temporary to be able to deploy the project as we do not have any static files yet)


### Get static and media files stored on Cloudinary

- Create a Cloudinary account (steps can be found in the [Code Institutes](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/b31493372e764469823578613d11036b/9236975633b64a12a61a00e0cca7c47d/?child=first) tutorial in LMS).

- Copy **API Environment Variable** in the Cloudinary dashboard.

- Go back to **env.py** and add a new environment vriable:
  - **CLOUDINARY_URL** with the value just copied from the dashboard ⇧(remove CLOUDINARY_URL in the beginning).

- HEROKU: Add a new _Config Var_ with the KEY **CLOUDINARY_URL**, and the same value(URL) as in the step above.

- **settings.py**:

  - Add Cloudinary Libraries to installed apps (the order is important):

    ````
    INSTALLED_APPS = [
      ...,
      'cloudinary_storage',
      'django.contrib.staticfiles',
      'cloudinary',
      ...,
    ]
    ````
  
  - Tell Django to use Cloudinary to store media and static files:
   
    ````
    STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    MEDIA_URL = '/media/'
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    ````
 
### Tell Django where templates will be stored

  - Link file to the templates directory in Heroku. _Place under the BASE_DIR line_:

    `TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')`

  - Change the templates directory to TEMPLATES_DIR:

    ````
    TEMPLATES = [
    {
      ...,
      'DIRS': [TEMPLATES_DIR],
      ...,
          ],
        },
      },
    ]
    ````

### Add Heroku Hostname to ALLOWED_HOSTS

  ````
  ALLOWED_HOSTS = ['app-name.herokuapp.com', 'localhost']
  ````

### Create a Procfile

`web: gunicorn whatscooking.wsgi`


### Go back to Heroku

- Click on the **"Deploy"** section on the top of the page.

- Select **GitHub** as deployment method and click the **"Connect to GitHub"** button.

- Search for the repository for this project, _what-is-cooking_. 

- Click **"Connect"** to link up Heroku app to the GitHub repository.

- Click on **"Deploy Branch"**.

- Click the **"Enable Automatic Deploys"** button to make it possible for Heroku to rebuild the app a new change is pushed to GitHub repository.

[Back to top ⇧](#table-of-contents)

## Development 

## Fork

- Log in to **GitHub** and ind the repository for this project, [_Kattis91/what-is-cooking_](https://github.com/Kattis91/what-is-cooking).

- In the top-right corner of the page, click **Fork**.

- Type some new name into the "Repository name" field to distinguish your fork from the upstream repository.

- Click **Create Fork**.

- The fork is now in your personal account and can be changed in the way you want.

## Clone

- On **GitHub**, navigate to your fork of the _what-is-cooking_ repository.

- Above the list of files, click **<>Code**.

- Copy the **URL** for the repository. Repository can be cloned in three different ways:
  - **HTTPS**;
  - **SSH**;
  - **GitHub CLI**.

- Open Terminal and change the current working directory to the location where you want the cloned directory.

- Type `git clone`, and paste the URL you copied earlier. Press **Enter**


