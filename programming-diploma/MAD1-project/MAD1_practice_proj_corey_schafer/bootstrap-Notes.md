# Bootstrap with cdn

- So yea we don't need to install the entire bootstrap instead we can just cdn links to link our custom styles
- Using cdn has its own drawbacks, but that is a separate discussion

# Bootstrap's global environment settings

- so the default setting of bootstrap is border-box and not content-box which means that width and height of the element will be calculated on the basis in which padding will also be included
- without doctype html 5 at the top, bootstrap won't work
- we need meta tag with viewport property to make sure that the designs remain responsive in nature
- reboot are the set of similar global CSS settings (sort of default settings) that bootstrap does to make sure that the web app that we make is compatible in every browser
- in Bootstrap, we enable the js which offers us many features using the data attributes that are available for each bootstrap component
- we can pass the values of these data attributes individually but bootstrap allows us to have the feature of passing multiple configurations through a single data-bs-config using JSON object
- just like tailwind, bootstrap also has breakpoints which can help us to write responsive design effectively

# Bootstrap components and utility classess

## Container

- container class gives us a responsive container, and like we can set that this container will take all the width of the screen till some certain breakpoint
- So like let's say that we want that till medium breakpoint our container should take all the available space and then take some less space then can make a .container-md class there
- .container-fluid is a class which just takes up all the space that is present in the entire screen regardless of the width
- .container's width is influenced by its parent container like if the container only has 50px width then .container-fluid will only take space upto 50px and not the entire screen-width although it is not a good practice to use it in these type of situations where we're using container inside divs which don't have the available space to their magic instead just use the regular divs

## Container-grid

- So like our container class also supports another feature where can like make grids, and in these grids we make row class divs with col class nested divs inside them and then keep on adding more col class divs in the row class div
- by default the cells in the grid will accomodate the center position when we mention text-center class at the parent container and the child containers will inherit that text-center property and then the rest content will be horizontally padded at the centre by default through default gutters available in bootstrap
- also classess like these support responsive breakpoints col-sm-4 will make sure that col takes 4 width after small breakpoint only similar to tailwind, now this col-4 will take 1/3rd part of the width for the column, since for responsive reasons
- The entire width of the container is divided into 12 parts, and here our column is taking 4 parts out of those 12 columns
- and we can decide accordingly which column to have how much space out of the container width
- gutter classes to manipulate the horizontal and vertical padding available for each cell, like we can use gx-number again wahi number of slots out of the container will be available to the padding and for vertical padding we use gy-some-number
- order-classes to make sure that we can order the columns too like col order-1 se the column will come at 1st position only no matter what
- nesting of grid-containers is also available like this :-
  <div class="container text-center">
  <div class="row">
  <div class="col-sm-3">
  Level 1: .col-sm-3
  </div>
  <div class="col-sm-9">
  <div class="row">
  <div class="col-8 col-sm-6">
  Level 2: .col-8 .col-sm-6
  </div>
  <div class="col-4 col-sm-6">
  Level 2: .col-4 .col-sm-6
  </div>
  </div>
  </div>
  </div>
  </div>

- 
    <div class="col col-lg-2">
      1 of 3
    </div>
    <div class="col-md-auto">
      Variable width content
    </div>
    <div class="col col-lg-2">
      3 of 3
    </div>

# Navbar tutorial 

<header class="site-header"> 
  <nav class="navbar navbar-expand-md navbar-dark bg-steel fixed-top"> (navbar setups a responsive navbar element, navbar-expand-md class makes sure that the navbar expands when the screen size reaches md, navbar-dark class ensures that the text names inside the navbar element is light for the dark background of the navbar, bg-steel and fixed-top are self-explanatory)
    <div class="container">
      <a class="navbar-brand mr-4" href="/">Flask Blog</a> (images inside this navbar-brand-class anchor tag is automatically vertically aligned and made responsive)
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggle" aria-controls="navbarToggle" aria-expanded="false" aria-label="Toggle navigation"> (these aria attributes are for the accesibility reasons)
        <span class="navbar-toggler-icon"></span> (hamburger icon aayega yaha pe)
      </button>
      <div class="collapse navbar-collapse" id="navbarToggle"> (ye id automatically collapse hojata using js using the button above)
        <div class="navbar-nav mr-auto"> (navbar-nav me links aate hai navbar ke)
          <a class="nav-item nav-link" href="/">Home</a>
          <a class="nav-item nav-link" href="/about">About</a>
        </div>
        <!-- Navbar Right Side -->
        <div class="navbar-nav">
          <a class="nav-item nav-link" href="/login">Login</a>
          <a class="nav-item nav-link" href="/register">Register</a>
        </div>
      </div>
    </div>
  </nav>
</header>