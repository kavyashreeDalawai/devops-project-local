import unittest
from click.testing import CliRunner
from service import create_app
from service.common.cli_commands import db_create


class TestCliCommands(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

    def test_db_create_command(self):
        runner = CliRunner()
        # Bind the live dynamic app application context loop directly to the runner mixin
        with self.app.app_context():
            result = runner.invoke(db_create, obj={"app": self.app})
            self.assertEqual(result.exit_code, 0)
