import click
import requests
from tabulate import tabulate

BASEPATH = 'http://ergast.com/api/f1/'
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    '''Formula 1 Command-Line Tool to get race results, schedule and standings'''
    pass

@cli.command()
@click.option('-y', '--year', default='current', help='Specify the race year. Defaults to the current year')
@click.option('-r', '--round', default='last', help='Specify the round number. Defaults to the latest round')
def results(year, round):
    '''
    List the results for a specific or latest race
    '''
    url = BASEPATH + f'{year}/{round}/results.json'

    resultTable = []

    response = requests.get(url)
    
    if (response.ok == False):
        click.echo(f'Something went wrong. Request returned status: {response.status_code} - {response.reason}')
        return
    
    responseData = response.json()['MRData']

    for result in responseData['RaceTable']['Races'][0]['Results']:
        position = result['position']
        racerName = (result['Driver']['givenName'], result['Driver']['familyName'])
        constructor = result['Constructor']['name']
        resultStatus = result['status']

        resultTable.append([position, ' '.join(racerName), constructor, resultStatus])

    raceYear = responseData['RaceTable']['Races'][0]['season']
    raceName = responseData['RaceTable']['Races'][0]['raceName']
    raceLocation = responseData['RaceTable']['Races'][0]['Circuit']['Location']['country']

    click.echo(f'Race results for the {raceYear} {raceName} in {raceLocation}:\n')

    click.echo(tabulate(resultTable, headers=["Pos", "Racer", "Constructor","Status"]))


@cli.command()
@click.option('-y', '--year', default='current', help='Specify the race year. Defaults to the current year')
@click.option('-n', '--next', default=False, help='Display the schedule for next race')
def schedule(year, next):
    '''
    List the schedule for a specific or latest race
    '''

    url = BASEPATH + f'{year}.json'

    if (next == True):
        url = f'http://ergast.com/api/f1/{year}/next.json'    

    scheduleTable = []

    response = requests.get(url)
    
    if (response.ok == False):
        click.echo(f'Something went wrong. Request returned status: {response.status_code} - {response.reason}')
        return
    
    responseData = response.json()['MRData']

    for result in responseData['RaceTable']['Races']:
        raceYear = result['season']
        raceRound = result['round']
        raceName = result['raceName']
        raceLocation = result['Circuit']['Location']['country']
        raceDate = result['date']
        raceTime = result['time']

        scheduleTable.append([raceYear, raceRound, raceName, raceLocation, raceDate, raceTime])

    click.echo(tabulate(scheduleTable, headers=["Year", "Round", "Name", "Location", "Date", "Time"]))

@cli.command()
@click.option('-s', '--standings', required=True, default='current', help='Specify whether you want to see the \'driver\' or \'constructor\' standings')
@click.option('-y', '--year', default='current', help='Specify the race year. Defaults to the current year')
def standings(standings, year):
    '''
    List the driver/constructor standings for a specific or current year
    '''

    url = BASEPATH

    if (standings == 'driver'):
        url += f'{year}/driverStandings.json'
    elif (standings == 'constructor'):
        url += f'{year}/constructorStandings.json'
    else:
        click.echo('Value for \'standings\' not correct')
        return
    
    response = requests.get(url)
    
    if (response.ok == False):
        click.echo(f'Something went wrong. Request returned status: {response.status_code} - {response.reason}')
        click.echo(url)
        return

    standingsTable = []

    responseData = response.json()['MRData']['StandingsTable']['StandingsLists'][0]

    if (standings == 'driver'):
        for result in responseData['DriverStandings']:
            position = result['position']
            points = result['points']
            racerName = (result['Driver']['givenName'], result['Driver']['familyName'])
            constructor = result['Constructors'][0]['name']

            standingsTable.append([position, points, ' '.join(racerName), constructor])

        click.echo(tabulate(standingsTable, headers=["Pos", "Points", "Racer", "Constructor"]))
    else:
        for result in responseData['ConstructorStandings']:
            position = result['position']
            points = result['points']
            constructor = result['Constructor']['name']

            standingsTable.append([position, points, constructor])

        click.echo(tabulate(standingsTable, headers=["Pos", "Points", "Constructor"]))