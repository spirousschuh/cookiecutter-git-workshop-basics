import click
from PIL import Image


@click.group()
def cli_group():
    pass

@cli_group.command(help='Creates a small thumbnail image')
@click.option('--input-path', help='input path of your image', required=True)
@click.option('--output-path', help='output path of the thumbnail',
              required=True)
def thumbnail(input_path, output_path):
    size = (128, 128)
    try:
        with Image.open(input_path) as im:
            im.thumbnail(size)
            im.save(output_path, "JPEG")
    except OSError:
        click.echo("cannot create thumbnail for %s" % input_path)

    click.echo('Sucessfully saved image at %s' % output_path)


@cli_group.command()
@click.option('--input-path', help='input path of your image', required=True)
@click.option('--output-path', help='path for the rotated image', required=True)
@click.option('--angle', type=int, help='roation angle', required=True)
def rotate(input_path, output_path, angle):

    try:
        with Image.open(input_path) as im:
            im.rotate(angle).save(output_path, "JPEG")
    except OSError:
        click.echo("cannot rotate the image in %s" % input_path)

    click.echo('Sucessfully saved image at %s' % output_path)
