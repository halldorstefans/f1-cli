import click
import requests
import pandas as pd

BASEPATH = 'http://ergast.com/api/f1/'
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    '''Formula 1 Command-Line Tool to get race results, schedule and standings'''
    pass

@cli.command()
@click.option('-s', '--season', default='current', help='Specify the race season. Defaults to the current season')
@click.option('-r', '--round', default='last', help='Specify the round number. Defaults to the latest round')
def results(season, round):
    '''
    List the results for a specific race.\n
    Displays the latest race by default
    '''
    url = BASEPATH + f'{season}/{round}/results.json'

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

    raceSeason = responseData['RaceTable']['Races'][0]['season']
    raceName = responseData['RaceTable']['Races'][0]['raceName']
    raceLocation = responseData['RaceTable']['Races'][0]['Circuit']['Location']['country']

    click.echo(f'Race results for the {raceSeason} {raceName} in {raceLocation}:\n')

    df = pd.DataFrame(data=resultTable, columns=["Pos", "Racer", "Constructor","Status"])
    
    click.echo(df.to_string(index=False))


@cli.command()
@click.option('-s', '--season', default='current', help='Specify the race season. Defaults to the current season')
@click.option('-n', '--next', default=False, help='Display the schedule for next race')
def schedule(season, next):
    '''
    List the schedule for a specific race.\n
    Displays the latest race by default
    '''

    url = BASEPATH + f'{season}.json'

    if (next == True):
        url = BASEPATH + f'{season}/next.json'    

    scheduleTable = []

    response = requests.get(url)
    
    if (response.ok == False):
        click.echo(f'Something went wrong. Request returned status: {response.status_code} - {response.reason}')
        return
    
    responseData = response.json()['MRData']

    for result in responseData['RaceTable']['Races']:
        raceSeason = result['season']
        raceRound = result['round']
        raceName = result['raceName']
        raceLocation = result['Circuit']['Location']['country']
        raceDate = result['date']
        raceTime = result['time']

        scheduleTable.append([raceSeason, raceRound, raceName, raceLocation, raceDate, raceTime])

    df = pd.DataFrame(data=scheduleTable, columns=["Season", "Round", "Name", "Location", "Date", "Time"])
    
    click.echo(df.to_string(index=False))

@cli.command()
@click.option('-s', '--standings', required=True, default='current', help='Specify whether you want to see the \'driver\' or \'constructor\' standings')
@click.option('-y', '--season', default='current', help='Specify the race season. Defaults to the current season')
def standings(standings, season):
    '''
    List the driver/constructor standings for a specific season.\n
    Displays the current season by default
    '''

    url = BASEPATH

    if (standings == 'driver'):
        url += f'{season}/driverStandings.json'
    elif (standings == 'constructor'):
        url += f'{season}/constructorStandings.json'
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

        df = pd.DataFrame(data=standingsTable, columns=["Pos", "Points", "Racer", "Constructor"])
    
        click.echo(df.to_string(index=False))
    else:
        for result in responseData['ConstructorStandings']:
            position = result['position']
            points = result['points']
            constructor = result['Constructor']['name']

            standingsTable.append([position, points, constructor])

        df = pd.DataFrame(data=standingsTable, columns=["Pos", "Points", "Constructor"])
    
        click.echo(df.to_string(index=False))