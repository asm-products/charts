
CHARTSPREE
----------

Make charts in seconds

Use our URL to inject charts into your website. The data is supplied via the URL, no Javascript required. Plus, if you need Lorem Ipsum charts, we've got you covered.

Example:

    <img src="//chartspree.io/bar.svg?Foo=1,1,2,3,5">


## Pies, Bars and Lines

There are 3 different types of charts. Choose one by changing the path.

#### Pies

    chartspree.io/pie.svg?Things=5&Stuff=2

#### Bars

    chartspree.io/bar.svg?Things=lorem_exp

#### Lines

    chartspree.io/line.svg?Things=lorem_flat

## Choose a Style

Just by adding _style=Stylename to the URL

#### Light (default)

    chartspree.io/bar.svg?Foo=lorem_exp&_style=light

#### Dark

    chartspree.io/bar.svg?Foo=lorem_exp&_style=dark

## Supplying data

You can just append the data for the chart to the URL parameters.

#### Bars and Lines

Generally you provide DataSet=<list-of-values>. For example:

    chartspree.io/line.svg?Things=1,2,3

You can also have multiple datasets, like:

    chartspree.io/line.svg?Some=1,2,3&Thing=2,3,4

Finally, you can add labels to the x axis:

    chartspree.io/bar.svg?Likes=3,2,4&_labels=Jan,Feb,Mar

#### Pies

For pies it's mostly the same, except you have names for sections and one value per section.

    chartspree.io/pie.svg?Some=1&Thing=2

## Other fancy features

Here are some additional neat features that Chartspree provide.

#### Generate placeholder data

If you're prototyping and need placeholder charts, we have a solution for you. Instead of providing numbers, you can just use one of these keywords.

    chartspree.io/bar.svg?Stuff=lorem_exp

    chartspree.io/bar.svg?Stuff=lorem_hockey

    chartspree.io/bar.svg?Stuff=lorem_bell

    chartspree.io/bar.svg?Stuff=lorem_flat

#### Customize the appearance of (line) charts

    <img src="http://chartspree.io/line.svg?Foo=lorem_hockey&_show_legend=false&_height=300px&_interpolate=cubic&_fill=true">

#### Show off with hover effects

Use an <object> tag instead of images. This gives you fancy hover-states.

    <object type="image/svg+xml" data="http://chartspree.io/line.svg?Some=lorem_flat&Stuff=lorem_flat&_interpolate=cubic &_fill=true&_height=300px"></object>

## Questions you might have

#### How much does it cost?

For now, Chartspree is free and is limited to 10,000 views per chart per month. If you need more, please reach out to team@chartspree.io.

#### What charting library did you use?

Chartspree is based on pygal, an awesome charting library for Python.

--------



Running your own copy of Chartspree 
------------------------------------

### Running on localhost

You'll need python 2.7 and should [install pip](https://pip.pypa.io/en/latest/installing.html), and create a [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) for the server. 

Once your environment is setup, clone the source and cd into the root of the Chartspree repository. Then 

1. Install the cairo library. If you're on a mac you can:

        brew install cairo

2. Run:

        pip install -r requirements.txt

3. Install redis and run `redis-server`.
4. Run:

        python manage.py runserver


### Running on heroku

You will need to install the [heroku toolbelt](https://toolbelt.heroku.com/).

Once your environment is setup, clone the source and cd into the root of the Chartspree repository. Then run:

    heroku apps:create [your project name]

then


    git push heroku

Your new project will be running at [your project name].herokuapp.com.


### Dependencies

Chartspree requires Redis. If you're deploying to heroku you can get an addon, such as redistogo. To install redistogo into your project just run the command:

    heroku addons:add redistogo


### Configuring Chartspree

Take a look at the `charts/settings.py` file for a list of environment variables that should be set 
in order for Charts to work correctly.

You can set these environment variables by creating a new file called `dev.env` in the root of the
project and then use [Foreman](http://ddollar.github.io/foreman/) to run the application.

    foreman start -e dev.env
