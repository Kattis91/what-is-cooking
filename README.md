# What's Cooking?

"What's Cooking?" is a public online blog-style platform where users can find recipes shared by food-loving people from around the globe. If someone wants to share their recipe or be able to comment and like others', they can register and log in. 

This interactive platform is designed to be an inspiration for those days when you don't know what to cook or simply want to try something new.


## Testing

### Manual Testing

| Feature | Expect | Action | Result | Pass/Fail |
|---------|--------|--------|--------|-----------|
| Navigation Bar. **Logo** (available for all users) | When the user clicks "WHAT'S COOKING?", they should be redirected to the homepage of the site. | Click on "WHAT'S COOKING?" in the navigation bar at the left top of the page. | The user is redirected to the home page of the site. | Pass |
| Navigation Bar. **Home** (available for all users) | When the user clicks "Home", they should be redirected to the homepage of the site. | Click on Home in the navigation bar at the top of the page. | The user is redirected to the home page of the site. | Pass |
| Navigation Bar. **Recipes** (available for all users) | When the user clicks "Recipes", they should be redirected to the recipes page of the site. | Click on Recipes in the navigation bar at the top of the page. | The user is redirected to the recipes page of the site. | Pass |
| Navigation Bar. **Sign Up** (available for all users) | When the user clicks "Sign Up" they should be redirected to the registration page. | Click on Sign Up in the navigation bar at the top of the page | The user is redirected to the registration page. | Pass |
| Navigation Bar. **Login** (available for all users) | When the user clicks "Sign In" they should be redirected to the sign in page. | Click on Sign In in the navigation bar at the top of the page. | The user is redirected to the sign in page. | Pass |
| Navigation Bar. **Add Recipe** (available for only logged-in users) | When the user clicks "Add Recipe", they should be redirected to a form page to submit their recipe. | Click on Add Recipe in the navigation bar at the top of the page. | The user is redirected to the form page. | Pass |
| Navigation Bar. **Logout** (available for only logged-in users) | When the user clicks "Logout", they should be redirected to a confirmation page before signing out. | Click on Logout in the navigation bar at the top of the page. | The user is redirected to the sign out confirmation page. | Pass |
| Link to Facebook (icon)| When clicked, links to a Facebook page in a new tab. | Click on the Facebook icon in the footer of the page. | Facebook page opens in a new tab. | Pass |
| Link to Instagram (icon) | When clicked, links to an Instagram page in a new tab.| Click on the Instagram icon in the footer of the page. | Instagram page opens in a new tab. | Pass |
| Link to TikTok (icon) | When clicked, links to a Tiktok page in a new tab. | Click on the TikTok icon in the footer of the page. | TikTok page opens in a new tab. | Pass |
| Link to YouTube (icon) | When clicked, links to a YoutTube page in a new tab.| Click on the Youtube icon in the footer of the page. | YouTube page opens in a new tab. | Pass |
| Categories | Each category box should be clickable. When the user clicks on a category, they should be directed to a page containing recipes only from that category. | Click on a category on the home page. | The user is directed to the page with the recipes within the chosen category. | Pass |
| Categories. No recipes. Logged-in users | If there are categories with no recipes yet, the user should get a clear message about that, along with the link to the "Add recipe" page. | Click on a category on the home page. | The user is directed to the page with the recipes within the chosen category. If there are no recipes available in the selected category, the user can see a message that reads "There are no recipes in this category yet. Do you want to be the first to share something here?" The message stating "Then you can do that by following the link: Add Recipe" is also displayed on the page. | Pass |
| Categories. No recipes. Unlogged users | If there are categories with no recipes yet, the user should get a clear message about that, along with the information that the user must be logged in to be able to post a recipe. | Click on a category on the home page. | The user is directed to the page with the recipes within the chosen category. If there are no recipes available in the selected category, the user can see a message that reads "There are no recipes in this category yet. Do you want to be the first to share something here?" Messages stating "You need to login first. You can do that by following the link: Sign In" and "Haven't created an account yet? Follow the link and become our new member: Sign Up" are also displayed on the page. | Pass |
| Categories. The "BACK" buton" | When the user is on the page with the recipes of the selected category, they should be able to click the "BACK" button to return to the home page of the site. | Click the "BACK" button on the page with the recipes of the selected category. | The user is directed to the home page of the site. | Pass |



