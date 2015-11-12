#!/Users/thomaseffland/.virtualenvs/health/bin/python
"""
The commandline entrypoint into the package

    ** All modules are run through this **

    To add you functionality, just import you module and add click commands

"""
import click

@click.group()
def main():
    pass

""" Add commands to the main group here"""

# model and database related
import pyhealth.models.models as models
@main.command()
@click.argument('really')
def dropdb(really):
    """ Drop every single table in the database...DANGEROUS 
        pass 'yes' or 'y' if you really want to do this..."""
    if really.lower() == "yes" or really.lower()=="y":
        models.dropAllTables()
    else:
        "Failed to drop because you weren't sure"

@main.command()
def initdb():
    """ Initialize database """
    models.setupDB()

from pyhealth.sources import yelp_fast as Yelp
@main.command()
@click.option('-y', '--yelp', is_flag=True, help="update yelp")
# @profile
def download(yelp):
    """ download content from sources"""
    if yelp:
        # fname = Yelp.downloadLatestYelpData()
        # data = Yelp.unzipYelpFeed(fname)
        # data = 'pyhealth/sources/yelpfiles/yelp_businesses.json'
        # Yelp.updateDBFromFeed(data, geocode=False)
        Yelp.geocodeUnknownLocations()
        
    return

# the main function DON'T TOUCH        
if __name__ == "__main__":
    main()


### SIMPLE PYTHON EXPERIMENT ###
#from pyhealth.experiments.simpletwitterclassify import run
#run()

