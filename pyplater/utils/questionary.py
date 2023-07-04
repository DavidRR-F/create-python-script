import click
import questionary

class QuestionaryInput(click.Option):
    def __init__(self, param_decls=None, **attrs):
        click.Option.__init__(self, param_decls, **attrs)

    def prompt_for_value(self, ctx):
        val = questionary.text(self.prompt).ask()
        return val
    
class QuestionaryConfirm(click.Option):
    def __init__(self, param_decls=None, **attrs):
        click.Option.__init__(self, param_decls, **attrs)

    def prompt_for_value(self, ctx):
        val = questionary.confirm(self.prompt).ask()
        return val    
    
class QuestionaryOption(click.Option):

    def __init__(self, param_decls=None, **attrs):
        click.Option.__init__(self, param_decls, **attrs)
        if not isinstance(self.type, click.Choice):
            raise Exception('Choice Option type arg must be click.Choice')

    def prompt_for_value(self, ctx):
        val = questionary.select(f"Choose {self.prompt}:", choices=self.type.choices).unsafe_ask()
        return val