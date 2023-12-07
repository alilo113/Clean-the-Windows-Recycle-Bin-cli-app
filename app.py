import click
import ctypes

@click.command()
@click.option('--confirm', is_flag=True, help='Confirm before deleting.')
def clear_recycle_bin(confirm):
    confirmation = click.confirm('Are you sure you want to clear the Recycle Bin?', default=False)

    if confirmation:
        try:
            ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, 0)
            click.echo("The Bin cleared successfully!!!")
            return 0  # Return 0 for success
        except OSError as e:
            click.echo(f"Error: {e}")
            return 1  # Return 1 for error
    
    click.echo("Operation canceled.")
    return 2  # Return 2 for cancellation

if __name__ == '__main__':
    exit_code = clear_recycle_bin()
    exit(exit_code)