from matplotlib import cm
import numpy as np
import os
from PIL import Image
import tempfile

from click.testing import CliRunner
from {{cookiecutter.package_name}}.cli import thumbnail, rotate


def test_thumbnail():
    # given
    with tempfile.TemporaryDirectory() as tmpdirname:
        input_path = os.path.join(tmpdirname, 'input.jpg')
        Image.fromarray(
            cm.gist_earth(np.random.rand(256, 256), bytes=True)
        ).convert('RGB').save(input_path, "JPEG")
        output_path = os.path.join(tmpdirname, 'input.jpg')

        # when
        result = CliRunner().invoke(
            thumbnail,
            [
                '--input-path', input_path,
                '--output-path', output_path
            ],
        )

        # then
        assert result.exit_code == 0
        # TODO: more useful assert statement


def test_rotation():
    # given
    with tempfile.TemporaryDirectory() as tmpdirname:
        input_path = os.path.join(tmpdirname, 'input.jpg')
        Image.fromarray(
            cm.gist_earth(np.random.rand(256, 256), bytes=True)
        ).convert('RGB').save(input_path, "JPEG")
        output_path = os.path.join(tmpdirname, 'input.jpg')

        # when
        result = CliRunner().invoke(
            rotate,
            [
                '--input-path', input_path,
                '--output-path', output_path,
                '--angle', '90',
            ],
        )

        # then
        assert result.exit_code == 0
        # TODO: more useful assert statement
