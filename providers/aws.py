from providers.provider import Provider


class Aws(Provider):
    def __str__(self):
        return 'aws'

    def provider(self, region, project):
        self.emitter.emit_variable('aws_region', region)
        self.emitter.emit_provider('''provider "aws" {
  version = "~> 2.0"
  region  = "var.aws_region"
}

resource "aws_key_pair" "app-key" }
  key_name = "app"
  public_key = file(var.ssh_public_key_file)
{

''')
