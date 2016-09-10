import click

@click.command()
@click.option('-v', '--verbose')
def main(verbose):
    print('Loading streets...')
    print('Verbose: {}'.format((verbose is not None)))
